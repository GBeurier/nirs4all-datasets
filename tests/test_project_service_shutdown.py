"""Targeted N8 closure: executor shutdown, response state and real Ctrl-C."""
from __future__ import annotations

import asyncio
import copy
import hashlib
import json
import os
import signal
import socket
import subprocess
import sys
import time
from contextlib import contextmanager
from dataclasses import replace

import pytest
import test_project_service as base
import test_project_service_admission as support

import nirs4all_datasets.project_service as service_module

app = base.app
credentials = base.credentials
manifest = base.manifest
loopback_only = base.loopback_only


@pytest.mark.parametrize("cleanup_error", [False, True])
def test_cancelled_download_keeps_cancellation_after_executor_shutdown(app, credentials, manifest, monkeypatch, cleanup_error):
    record = base.upload(app, credentials[1], manifest)
    app.transfers = replace(app.transfers, send_timeout=60)
    path = "/v1/records/" + record["record_id"] + "/files/" + base.DIGEST
    streams, responses, wire = [], [], []
    original_open, original_respond = app.store.open_file, app._respond
    original_close = service_module._Download.close

    @contextmanager
    def observed_open(*args):
        with original_open(*args) as opened:
            streams.append(opened[0])
            yield opened

    async def observed_response(send, status, value):
        responses.append(status)
        await original_respond(send, status, value)

    def fail_cleanup(handle):
        original_close(handle)
        raise RuntimeError("simulated cleanup failure")

    monkeypatch.setattr(app.store, "open_file", observed_open)
    monkeypatch.setattr(app, "_respond", observed_response)
    if cleanup_error:
        monkeypatch.setattr(service_module._Download, "close", fail_cleanup)

    async def probe():
        blocked = asyncio.Event()

        async def receive():
            raise AssertionError("Downloads do not read request bodies")

        async def send(message):
            wire.append(message)
            if message["type"] == "http.response.body":
                blocked.set()
                await asyncio.sleep(100)

        task = asyncio.create_task(app({"type": "http", "method": "GET", "path": path,
                                       "headers": [(b"authorization", ("Bearer " + credentials[1]["a"]).encode())]}, receive, send))
        await asyncio.wait_for(blocked.wait(), timeout=2)
        # Match Uvicorn's ordering: response cancellation may resume only after
        # lifespan shutdown has already closed all executors.
        app.close()
        start = time.monotonic()
        task.cancel("shutdown-cancel")
        with pytest.raises(asyncio.CancelledError) as caught:
            await asyncio.wait_for(task, timeout=1)
        assert caught.value.args == ("shutdown-cancel",)
        assert time.monotonic() - start < 0.5

    asyncio.run(probe())
    assert [m["status"] for m in wire if m["type"] == "http.response.start"] == [200]
    assert responses == []
    assert streams and all(stream.closed for stream in streams)
    assert app._downloads.active == app._operations.active == 0


@pytest.mark.parametrize("kind", ["download_cleanup", "json_send"])
def test_post_header_runtime_failure_never_attempts_a_second_response(app, credentials, manifest, monkeypatch, kind):
    record = base.upload(app, credentials[1], manifest)
    wire, responses = [], []
    original_close, original_respond = service_module._Download.close, app._respond

    def fail_cleanup(handle):
        original_close(handle)
        raise RuntimeError("cleanup failed after response start")

    async def observed_response(send, status, value):
        responses.append(status)
        await original_respond(send, status, value)

    monkeypatch.setattr(app, "_respond", observed_response)
    if kind == "download_cleanup":
        monkeypatch.setattr(service_module._Download, "close", fail_cleanup)
        path = "/v1/records/" + record["record_id"] + "/files/" + base.DIGEST
    else:
        path = "/v1/records"

    async def probe():
        async def receive():
            raise AssertionError("GET cannot read a body")

        async def send(message):
            wire.append(message)
            if kind == "json_send" and message["type"] == "http.response.body":
                raise RuntimeError("send failed after headers")

        with pytest.raises(OSError, match="response interrupted"):
            await app({"type": "http", "method": "GET", "path": path,
                       "headers": [(b"authorization", ("Bearer " + credentials[1]["a"]).encode())]}, receive, send)

    asyncio.run(probe())
    assert [m["status"] for m in wire if m["type"] == "http.response.start"] == [200]
    assert responses == ([] if kind == "download_cleanup" else [200])
    assert app._operations.active == app._downloads.active == 0


@pytest.mark.parametrize("shutdown_timeout", [0.5, 2.0])
def test_real_cli_sigint_stuck_download_exits_near_shutdown_limit(tmp_path, credentials, manifest, shutdown_timeout):
    threshold = 2_684_354_560
    usage = os.statvfs(tmp_path)
    assert usage.f_bavail * usage.f_frsize >= threshold + 32 * 1024 * 1024
    # Eight MiB exceeds socket buffers while keeping synthetic scratch small.
    data = b"x" * (8 * 1024 * 1024)
    digest = hashlib.sha256(data).hexdigest()
    item = copy.deepcopy(manifest)
    item["files"] = [{"path": "stuck.bin", "size": len(data), "sha256": digest, "byte_source": "unknown"}]
    token = credentials[1]["a"]
    with support.cli_server(tmp_path, credentials, "--send-timeout", "60", "--shutdown-timeout", str(shutdown_timeout)) as server:
        _, pending = base.http_request(server.port, "POST", "/v1/submissions", token=token, body=json.dumps(item).encode())
        prefix = "/v1/submissions/" + pending["submission_id"]
        assert base.http_request(server.port, "PUT", prefix + "/files/" + digest, token=token, body=data)[0] == 200
        _, record = base.http_request(server.port, "POST", prefix + "/commit", token=token)
        path = "/v1/records/" + record["record"]["record_id"] + "/files/" + digest
        with socket.socket() as client:
            client.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 4096)
            client.settimeout(3)
            client.connect(("127.0.0.1", server.port))
            client.sendall((f"GET {path} HTTP/1.1\r\nHost: 127.0.0.1\r\nAuthorization: Bearer {token}\r\n\r\n").encode())
            headers = bytearray()
            while b"\r\n\r\n" not in headers:
                headers.extend(client.recv(1))
                assert len(headers) < 4096
            assert headers.startswith(b"HTTP/1.1 200 ")
            time.sleep(0.2)
            start = time.monotonic()
            server.process.send_signal(signal.SIGINT)
            # Keep the client alive; send neither a reset nor a second signal.
            server.process.wait(timeout=shutdown_timeout + 1.25)
            elapsed = time.monotonic() - start
            assert elapsed < shutdown_timeout + 1.25
    assert server.stdout == server.stderr == b""
    print(f"SIGINT: shutdown limit={shutdown_timeout:.1f}s, exit={elapsed:.2f}s, CLI logs=0 bytes")
    usage = os.statvfs(tmp_path)
    assert usage.f_bavail * usage.f_frsize >= threshold


def test_real_cli_invalid_web_concurrency_has_fixed_startup_diagnostic(tmp_path, credentials):
    environment = dict(os.environ, WEB_CONCURRENCY="abc")
    result = subprocess.run([sys.executable, "-B", "-m", "nirs4all_datasets.project_service", "serve",
                             "--store", str(tmp_path / "store"), "--credentials", str(credentials[0]), "--port", "0"],
                            env=environment, capture_output=True, timeout=5)
    assert result.returncode == 1
    assert result.stdout == b""
    assert result.stderr == b"Unable to start project service.\n"
    assert not (tmp_path / "store").exists()
