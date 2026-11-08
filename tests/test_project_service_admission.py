"""Final WORK closure: isolation under saturation, bounded sends and CLI logs."""
from __future__ import annotations

import asyncio
import copy
import hashlib
import http.client
import json
import os
import socket
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from contextlib import ExitStack, contextmanager
from types import SimpleNamespace

import pytest
import test_project_service as support
from test_project_service import DATA, DIGEST, asgi_call, begin, call, file_manifest, http_request, leaf, upload

from nirs4all_datasets.project_service import TransferLimits, create_app

app = support.app
credentials = support.credentials
manifest = support.manifest
loopback_only = support.loopback_only


@contextmanager
def cli_server(tmp_path, credentials, *options):
    """Use the actual module CLI, not a test client or runpy wrapper."""
    with socket.socket() as reservation:
        reservation.bind(("127.0.0.1", 0))
        port = reservation.getsockname()[1]
    root = tmp_path / "cli-store"
    command = [sys.executable, "-B", "-m", "nirs4all_datasets.project_service", "serve", "--store", str(root),
               "--credentials", str(credentials[0]), "--port", str(port), *options]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    running = SimpleNamespace(port=port, process=process, root=root, stdout=b"", stderr=b"")
    try:
        deadline = time.monotonic() + 5
        while time.monotonic() < deadline and process.poll() is None:
            try:
                if http_request(port, "GET", "/healthz")[0] == 200:
                    break
            except OSError:
                time.sleep(0.01)
        else:
            pytest.fail("Real CLI did not start")
        yield running
    finally:
        process.terminate()
        try:
            running.stdout, running.stderr = process.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            running.stdout, running.stderr = process.communicate(timeout=5)


def wait_until(predicate, timeout=3):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if predicate():
            return
        time.sleep(0.01)
    pytest.fail("Expected transfer state did not become visible")


def raw_headers(port, method, path, token, *, size=None, extra=b"", prefix=b""):
    connection = socket.create_connection(("127.0.0.1", port), timeout=3)
    length = b"" if size is None else f"Content-Length: {size}\r\n".encode()
    authorization = b"" if token is None else ("Authorization: Bearer " + token + "\r\n").encode()
    connection.sendall(f"{method} {path} HTTP/1.1\r\nHost: 127.0.0.1\r\n".encode() + authorization + length + extra + b"\r\n" + prefix)
    return connection


def test_n1_real_cli_saturated_a_keeps_b_reads_writes_uploads_under_one_second(tmp_path, credentials, manifest):
    tokens = credentials[1]
    data = b"s" * 50_000
    digest = hashlib.sha256(data).hexdigest()
    submission = copy.deepcopy(manifest)
    submission["files"] = [{"path": "stall.bin", "size": len(data), "sha256": digest, "byte_source": "unknown"}]
    with cli_server(tmp_path, credentials) as server:
        _, pending = http_request(server.port, "POST", "/v1/submissions", token=tokens["a"], body=json.dumps(submission).encode())
        path = "/v1/submissions/" + pending["submission_id"] + "/files/" + digest
        stalled = [raw_headers(server.port, "PUT", path, tokens["a"], size=len(data), prefix=data[:100]) for _ in range(TransferLimits.project_uploads)]
        try:
            wait_until(lambda: len(list(server.root.rglob(".tmp-*"))) == TransferLimits.project_uploads)
            # Reproduce the old 28-socket attack, but excess requests send no body.
            for _ in range(28 - len(stalled)):
                with raw_headers(server.port, "PUT", path, tokens["a"], size=len(data), extra=b"Expect: 100-continue\r\n") as excess:
                    start = time.monotonic()
                    reply = excess.recv(4096)
                    assert reply.startswith(b"HTTP/1.1 503 "), reply
                    assert b"100 Continue" not in reply
                    assert time.monotonic() - start < 1
            start = time.monotonic()
            assert http_request(server.port, "GET", "/v1/records", token=tokens["b"])[0] == 200
            assert time.monotonic() - start < 1
            start = time.monotonic()
            assert http_request(server.port, "POST", "/v1/submissions", token=tokens["b"], body=json.dumps(manifest).encode())[0] == 201
            assert time.monotonic() - start < 1
            other = file_manifest(manifest)
            other["descriptor"]["id"] = "other_upload"
            start = time.monotonic()
            _, b_pending = http_request(server.port, "POST", "/v1/submissions", token=tokens["b"], body=json.dumps(other).encode())
            prefix = "/v1/submissions/" + b_pending["submission_id"]
            assert http_request(server.port, "PUT", prefix + "/files/" + DIGEST, token=tokens["b"], body=DATA)[0] == 200
            assert http_request(server.port, "POST", prefix + "/commit", token=tokens["b"])[0] == 201
            assert time.monotonic() - start < 1
        finally:
            for connection in stalled:
                connection.close()
        wait_until(lambda: not list(server.root.rglob(".tmp-*")))
        assert http_request(server.port, "PUT", path, token=tokens["a"], body=data)[0] == 200


def test_n1_global_admission_is_pre_body_and_uploads_never_use_default_executor(tmp_path, credentials, manifest):
    path, tokens, records = credentials
    c_token, c_record = leaf.issue_credential(leaf.ProjectPrincipal("project-c", "c", frozenset({"datasets"}), frozenset({"datasets.read", "datasets.add"})))
    leaf.write_credential_store(path, [*records, c_record])
    tokens = {**tokens, "c": c_token}
    service = create_app(store=tmp_path / "store", credential_store=path, transfers=TransferLimits(uploads=2, project_uploads=1))
    paths = {who: "/v1/submissions/" + begin(service, tokens, file_manifest(manifest), who)["submission_id"] + "/files/" + DIGEST for who in ("a", "b", "c")}

    async def probe():
        # Even a one-thread metadata pool remains responsive with both upload
        # admission slots held by stalled bodies in their dedicated executor.
        asyncio.get_running_loop().set_default_executor(ThreadPoolExecutor(max_workers=1))
        entered = {who: asyncio.Event() for who in ("a", "b")}

        async def stall(who):
            async def receive():
                entered[who].set()
                await asyncio.sleep(100)
                return {"type": "http.request", "body": DATA}

            async def send(message):
                pass

            await service({"type": "http", "method": "PUT", "path": paths[who], "headers": [(b"authorization", ("Bearer " + tokens[who]).encode())]}, receive, send)

        workers = [asyncio.create_task(stall(who)) for who in ("a", "b")]
        try:
            await asyncio.wait_for(asyncio.gather(*(event.wait() for event in entered.values())), timeout=2)
            response = await asgi_call(service, "PUT", paths["c"], token=tokens["c"], forbid_body=True)
            assert response[0] == 503 and response[3] == 0
            assert json.loads(response[1]) == {"error": "store_busy"}
            assert (await asyncio.wait_for(asgi_call(service, "GET", "/v1/records", token=tokens["c"]), timeout=1))[0] == 200
            other = copy.deepcopy(manifest)
            other["descriptor"]["id"] = "metadata"
            assert (await asyncio.wait_for(asgi_call(service, "POST", "/v1/submissions", token=tokens["c"], body=json.dumps(other).encode()), timeout=1))[0] == 201
        finally:
            for worker in workers:
                worker.cancel()
            await asyncio.gather(*workers, return_exceptions=True)

    try:
        asyncio.run(probe())
        assert service._uploads.active == 0
        assert not list(service.store.root.rglob(".tmp-*"))
    finally:
        service.close()


@pytest.mark.parametrize("ending", ["deadline", "cancel"])
def test_n2_streaming_deadline_admission_and_cleanup(app, credentials, manifest, monkeypatch, ending):
    a_record = upload(app, credentials[1], manifest, "a")
    b_record = upload(app, credentials[1], manifest, "b")
    app.transfers = TransferLimits(send_timeout=0.1)
    a_path = "/v1/records/" + a_record["record_id"] + "/files/" + DIGEST
    b_path = "/v1/records/" + b_record["record_id"] + "/files/" + DIGEST

    def no_materialization(*args, **kwargs):
        raise AssertionError("Service downloads must not materialize read_file()")

    monkeypatch.setattr(app.store, "read_file", no_materialization)
    streams = []
    original = app.store.open_file

    @contextmanager
    def tracked(*args):
        with original(*args) as result:
            streams.append(result[0])
            yield result

    monkeypatch.setattr(app.store, "open_file", tracked)

    async def probe():
        blocked = asyncio.Event()
        starts = []

        async def send(message):
            if message["type"] == "http.response.start":
                starts.append(message)
            else:
                assert len(message.get("body", b"")) <= 65_536
                blocked.set()
                await asyncio.sleep(100)

        async def receive():
            raise AssertionError("Download does not receive a request body")

        task = asyncio.create_task(app({"type": "http", "method": "GET", "path": a_path, "headers": [(b"authorization", ("Bearer " + credentials[1]["a"]).encode())]}, receive, send))
        await asyncio.wait_for(blocked.wait(), timeout=2)
        assert (await asgi_call(app, "GET", a_path, token=credentials[1]["a"], forbid_body=True))[0] == 503
        b_response = await asgi_call(app, "GET", b_path, token=credentials[1]["b"], forbid_body=True)
        assert b_response[0] == 200 and b_response[1] == DATA
        if ending == "cancel":
            task.cancel()
            with pytest.raises(asyncio.CancelledError):
                await asyncio.wait_for(task, timeout=1)
        else:
            with pytest.raises(OSError, match="download interrupted"):
                await asyncio.wait_for(task, timeout=1)
        assert len(starts) == 1

    asyncio.run(probe())
    assert streams and all(stream.closed for stream in streams)
    assert app._downloads.active == 0
    assert call(app, "GET", a_path, token=credentials[1]["a"])[1] == DATA


def test_n2_failed_download_start_never_attempts_second_start(app, credentials, manifest):
    record = upload(app, credentials[1], manifest)
    path = "/v1/records/" + record["record_id"] + "/files/" + DIGEST

    async def probe():
        starts = []

        async def receive():
            raise AssertionError("Download cannot read a request body")

        async def send(message):
            if message["type"] == "http.response.start":
                starts.append(message)
            raise OSError("client disconnected during response start")

        with pytest.raises(OSError):
            await app({"type": "http", "method": "GET", "path": path, "headers": [(b"authorization", ("Bearer " + credentials[1]["a"]).encode())]}, receive, send)
        assert len(starts) == 1

    asyncio.run(probe())
    assert app._downloads.active == 0


def test_n2_global_download_admission_refuses_before_io_or_body(app, credentials, manifest, monkeypatch):
    record = upload(app, credentials[1], manifest)

    def forbidden(*args, **kwargs):
        raise AssertionError("Full download admission must refuse before file IO")

    monkeypatch.setattr(app.store, "open_file", forbidden)
    with ExitStack() as active:
        for i in range(app.transfers.downloads):
            active.enter_context(app._downloads.reserve(f"other-project-{i}"))
        result = call(app, "GET", "/v1/records/" + record["record_id"] + "/files/" + DIGEST, token=credentials[1]["a"], forbid_body=True)
        assert result[:2] == (503, {"error": "store_busy"})
        assert result[3] == 0
    assert app._downloads.active == 0


def test_n2_real_cli_non_readers_have_bounded_rss_and_release_on_deadline(tmp_path, credentials, manifest):
    tokens = credentials[1]
    data = b"x" * (8 * 1024 * 1024)
    digest = hashlib.sha256(data).hexdigest()
    submission = copy.deepcopy(manifest)
    submission["files"] = [{"path": "large.bin", "sha256": digest, "size": len(data), "byte_source": "unknown"}]
    with cli_server(tmp_path, credentials, "--send-timeout", "0.5") as server:
        _, pending = http_request(server.port, "POST", "/v1/submissions", token=tokens["a"], body=json.dumps(submission).encode())
        prefix = "/v1/submissions/" + pending["submission_id"]
        assert http_request(server.port, "PUT", prefix + "/files/" + digest, token=tokens["a"], body=data)[0] == 200
        _, record = http_request(server.port, "POST", prefix + "/commit", token=tokens["a"])
        download_path = "/v1/records/" + record["record"]["record_id"] + "/files/" + digest

        def rss():
            with open(f"/proc/{server.process.pid}/status") as status:
                return int(next(line for line in status if line.startswith("VmRSS:")).split()[1]) * 1024

        before = rss()
        clients = []
        try:
            for _ in range(24):
                client = socket.socket()
                client.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 4096)
                client.connect(("127.0.0.1", server.port))
                client.sendall((f"GET {download_path} HTTP/1.1\r\nHost: 127.0.0.1\r\nAuthorization: Bearer {tokens['a']}\r\n\r\n").encode())
                clients.append(client)
            time.sleep(0.15)
            assert rss() - before < 64 * 1024 * 1024
            time.sleep(0.6)
            # Expired non-reading connections cannot keep admission or an 8 MiB
            # materialized response alive. A new same-project reader succeeds.
            assert http_request(server.port, "GET", download_path, token=tokens["a"])[1] == data
        finally:
            for client in clients:
                client.close()


def test_real_cli_default_64_mib_boundary_streams_with_bounded_rss(tmp_path, credentials, manifest):
    chunk = b"z" * 65_536
    size = 64 * 1024 * 1024
    usage = os.statvfs(tmp_path)
    if usage.f_bavail * usage.f_frsize < size * 2 + 2_147_483_648:
        pytest.skip("Insufficient disk headroom above the required floor")
    digest = hashlib.sha256()
    for _ in range(size // len(chunk)):
        digest.update(chunk)
    expected = digest.hexdigest()
    submission = copy.deepcopy(manifest)
    submission["files"] = [{"path": "boundary.bin", "sha256": expected, "size": size, "byte_source": "unknown"}]
    token = credentials[1]["a"]
    with cli_server(tmp_path, credentials) as server:
        _, pending = http_request(server.port, "POST", "/v1/submissions", token=token, body=json.dumps(submission).encode())
        prefix = "/v1/submissions/" + pending["submission_id"]
        assert http_request(server.port, "PUT", prefix + "/files/" + expected, token=token, body=(chunk for _ in range(size // len(chunk))), chunked=True)[0] == 200
        _, record = http_request(server.port, "POST", prefix + "/commit", token=token)

        def rss():
            with open(f"/proc/{server.process.pid}/status") as status:
                return int(next(line for line in status if line.startswith("VmRSS:")).split()[1]) * 1024

        baseline = peak = rss()
        connection = http.client.HTTPConnection("127.0.0.1", server.port, timeout=5)
        try:
            connection.request("GET", "/v1/records/" + record["record"]["record_id"] + "/files/" + expected, headers={"Authorization": "Bearer " + token})
            response = connection.getresponse()
            assert response.status == 200
            received, measured = 0, hashlib.sha256()
            while block := response.read(65_536):
                received += len(block)
                measured.update(block)
                if received % (1024 * 1024) == 0:
                    peak = max(peak, rss())
            assert received == size and measured.hexdigest() == expected
            assert peak - baseline < 32 * 1024 * 1024
        finally:
            connection.close()


def test_n4_add_only_receipts_never_disclose_another_principals_stamps(app, credentials, manifest):
    tokens = credentials[1]
    original = begin(app, tokens, manifest)["record"]
    for who in ("writer",):
        assert begin(app, tokens, manifest, who) == {"status": "already_present", "record_id": original["record_id"]}
        assert call(app, "GET", "/v1/records/" + original["record_id"], token=tokens[who], forbid_body=True)[0] == 403
    other = file_manifest(manifest)
    other["descriptor"]["id"] = "pending_by_a"
    pending = begin(app, tokens, other)
    prefix = "/v1/submissions/" + pending["submission_id"]
    assert call(app, "PUT", prefix + "/files/" + DIGEST, token=tokens["a"], body=DATA)[0] == 200
    first = call(app, "POST", prefix + "/commit", token=tokens["writer"])
    assert first[:2] == (201, {"status": "created", "record_id": pending["record_id"]})
    assert call(app, "POST", prefix + "/commit", token=tokens["writer"])[:2] == (200, {"status": "already_present", "record_id": pending["record_id"]})


def test_n5_same_project_dedup_allows_commit_without_reupload(app, credentials, manifest):
    tokens = credentials[1]
    upload(app, tokens, manifest, "a")
    same_bytes = file_manifest(manifest)
    same_bytes["descriptor"]["id"] = "different_record_same_bytes"
    pending = begin(app, tokens, same_bytes, "writer")
    assert call(app, "POST", "/v1/submissions/" + pending["submission_id"] + "/commit", token=tokens["writer"])[0] == 201
    foreign = begin(app, tokens, same_bytes, "b")
    assert call(app, "POST", "/v1/submissions/" + foreign["submission_id"] + "/commit", token=tokens["b"])[:2] == (409, {"error": "missing_blob"})


def test_real_cli_http_and_websocket_arbitrary_query_values_never_log_bearer(tmp_path, credentials):
    token = credentials[1]["a"]
    encoded = "".join(f"%{byte:02X}" for byte in token.encode())
    with cli_server(tmp_path, credentials) as server:
        assert http_request(server.port, "GET", "/v1/records", token=token)[0] == 200
        for secret in (token, encoded):
            for path in ("/v1/records?unrelated_value=" + secret, "/unknown?anything_at_all=" + secret):
                for websocket in (False, True):
                    upgrade = (b"Connection: Upgrade\r\nUpgrade: websocket\r\nSec-WebSocket-Version: 13\r\n"
                               b"Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n") if websocket else b"Connection: close\r\n"
                    with raw_headers(server.port, "GET", path, token, extra=upgrade) as connection:
                        response = connection.recv(4096)
                        assert response.startswith((b"HTTP/1.1 400 ", b"HTTP/1.1 404 ")), response
        assert http_request(server.port, "GET", "/healthz")[0] == 200
    logs = server.stdout + server.stderr
    assert token.encode() not in logs
    assert encoded.encode() not in logs
    assert encoded.lower().encode() not in logs
    assert logs == b""


@pytest.mark.parametrize("options", [{"uploads": 1}, {"project_uploads": 8}, {"downloads": 1}, {"project_downloads": 4}, {"send_timeout": 0}, {"send_timeout": float("nan")}, {"uploads": True}])
def test_transfer_limits_fail_closed(options):
    with pytest.raises(ValueError):
        TransferLimits(**options)
