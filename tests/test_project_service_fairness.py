"""N6–N11: bounded store work, JSON backpressure and real CLI shutdown."""
from __future__ import annotations

import asyncio
import copy
import hashlib
import json
import os
import socket
import subprocess
import sys
import threading
import time
from contextlib import ExitStack
from dataclasses import replace

import pytest
import test_project_service as base
import test_project_service_admission as support

from nirs4all_datasets.private_store import PrivateStoreError, StoreContext
from nirs4all_datasets.project_service import TransferLimits

app = base.app
credentials = base.credentials
manifest = base.manifest
loopback_only = base.loopback_only


@pytest.mark.parametrize(("operation", "reset"), [("get_record", False), ("list_records", False), ("get_record", True), ("commit", False), ("begin", False)])
def test_n6_112_requests_cannot_queue_one_projects_store_work(app, credentials, manifest, monkeypatch, operation, reset):
    tokens = credentials[1]
    pending = base.begin(app, tokens, base.file_manifest(manifest))
    prefix = "/v1/submissions/" + pending["submission_id"]
    assert base.call(app, "PUT", prefix + "/files/" + base.DIGEST, token=tokens["a"], body=base.DATA)[0] == 200
    assert base.call(app, "POST", prefix + "/commit", token=tokens["a"])[0] == 201
    body = b""
    if operation == "get_record":
        method, path, actor = "GET", "/v1/records/" + pending["record_id"], "reader"
    elif operation == "list_records":
        method, path, actor = "GET", "/v1/records", "reader"
    elif operation == "commit":
        method, path, actor = "POST", prefix + "/commit", "writer"
    else:
        method, path, actor = "POST", "/v1/submissions", "writer"
        other = copy.deepcopy(manifest)
        other["descriptor"]["id"] = "other"
        body = json.dumps(other).encode()
    original = getattr(app.store, operation)
    release = threading.Event()
    counts = {"calls": 0, "active": 0, "peak": 0}
    lock = threading.Lock()

    def slow(context, *args, **kwargs):
        if context.project_id != "project-a":
            return original(context, *args, **kwargs)
        with lock:
            counts["calls"] += 1
            counts["active"] += 1
            counts["peak"] = max(counts["peak"], counts["active"])
        try:
            assert release.wait(5)
            return original(context, *args, **kwargs)
        finally:
            with lock:
                counts["active"] -= 1

    monkeypatch.setattr(app.store, operation, slow)

    async def probe():
        requests = [asyncio.create_task(base.asgi_call(app, method, path, token=tokens[actor], body=body)) for _ in range(112)]
        try:
            deadline = time.monotonic() + 2
            while sum(request.done() for request in requests) < 112 - app.transfers.project_operations:
                assert time.monotonic() < deadline
                await asyncio.sleep(0.001)
            rejected = [request.result() for request in requests if request.done()]
            assert len(rejected) == 112 - app.transfers.project_operations
            assert all(result[0] == 503 and result[2][b"retry-after"] == b"1" for result in rejected)
            if reset:
                for _ in range(2):
                    for request in requests:
                        if not request.done():
                            request.cancel()
                    await asyncio.sleep(0.02)
                assert app._operations.projects["project-a"] == app.transfers.project_operations

            async def b_upload():
                submitted = base.file_manifest(manifest)
                submitted["descriptor"]["id"] = "b_upload"
                response = await base.asgi_call(app, "POST", "/v1/submissions", token=tokens["b"], body=json.dumps(submitted).encode())
                assert response[0] == 202
                sid = json.loads(response[1])["submission_id"]
                path = "/v1/submissions/" + sid
                assert (await base.asgi_call(app, "PUT", path + "/files/" + base.DIGEST, token=tokens["b"], body=base.DATA))[0] == 200
                assert (await base.asgi_call(app, "POST", path + "/commit", token=tokens["b"]))[0] == 201

            async def b_write():
                assert (await base.asgi_call(app, "POST", "/v1/submissions", token=tokens["b"], body=json.dumps(manifest).encode()))[0] == 201

            async def b_read():
                assert (await base.asgi_call(app, "GET", "/v1/records", token=tokens["b"]))[0] == 200

            await asyncio.wait_for(asyncio.gather(b_read(), b_write(), b_upload()), timeout=1)
        finally:
            release.set()
            await asyncio.gather(*requests, return_exceptions=True)

    asyncio.run(probe())
    assert counts["calls"] == counts["peak"] == app.transfers.project_operations
    assert app._operations.active == 0


@pytest.mark.parametrize(("method", "path", "right"), base.ROUTE_CASES)
def test_n6_global_operation_admission_is_before_executor_or_body(app, credentials, monkeypatch, method, path, right):
    def forbidden(*args, **kwargs):
        raise AssertionError("Full operation admission cannot submit executor work")

    monkeypatch.setattr(app._store_executor, "submit", forbidden)
    monkeypatch.setattr(app._upload_executor, "submit", forbidden)
    monkeypatch.setattr(app._download_executor, "submit", forbidden)
    with ExitStack() as held:
        for i in range(app.transfers.operations):
            held.enter_context(app._operations.reserve(f"project-{i // app.transfers.project_operations}"))
        result = base.call(app, method, path, token=credentials[1]["a"], forbid_body=True)
        assert result[:2] == (503, {"error": "store_busy"})
        assert result[2][b"retry-after"] == b"1" and result[3] == 0
        assert base.call(app, method, path, token="invalid", forbid_body=True)[0] == 401


def test_n7_bounded_lists_refuse_before_loading_all_metadata(app, credentials, manifest, monkeypatch):
    context = StoreContext("project-a", "operator")
    for i in range(4):
        item = copy.deepcopy(manifest)
        item["descriptor"]["id"] = f"large_{i}"
        item["descriptor"]["description"] = "x" * 700_000
        app.store.begin(context, item)
    calls = []
    original = app.store.get_record

    def counted(*args, **kwargs):
        calls.append(kwargs.get("max_metadata_bytes"))
        return original(*args, **kwargs)

    monkeypatch.setattr(app.store, "get_record", counted)
    result = base.call(app, "GET", "/v1/records", token=credentials[1]["reader"])
    assert result[:2] == (413, {"error": "response_too_large"})
    assert len(calls) == 3 and calls[-1] < 700_000
    app.transfers = replace(app.transfers, list_records=2)
    calls.clear()
    assert base.call(app, "GET", "/v1/records", token=credentials[1]["reader"])[0] == 413
    assert calls == []


@pytest.mark.parametrize("ending", ["deadline", "cancel"])
def test_n7_json_admission_send_deadline_and_cleanup(app, credentials, manifest, ending):
    base.begin(app, credentials[1], manifest)
    app.transfers = replace(app.transfers, send_timeout=0.2)

    async def probe():
        blocked = asyncio.Event()
        starts = []
        bodies = []

        async def send(message):
            if message["type"] == "http.response.start":
                starts.append(message)
            else:
                bodies.append(True)
                if len(bodies) == app.transfers.project_operations:
                    blocked.set()
                await asyncio.sleep(100)

        async def receive():
            raise AssertionError("GET cannot read request body")

        tasks = [asyncio.create_task(app({"type": "http", "method": "GET", "path": "/v1/records", "headers": [(b"authorization", ("Bearer " + credentials[1]["a"]).encode())]}, receive, send)) for _ in range(app.transfers.project_operations)]
        await asyncio.wait_for(blocked.wait(), timeout=1)
        result = await base.asgi_call(app, "GET", "/v1/records", token=credentials[1]["a"], forbid_body=True)
        assert result[0] == 503
        assert (await base.asgi_call(app, "GET", "/v1/records", token=credentials[1]["b"]))[0] == 200
        if ending == "cancel":
            for task in tasks:
                task.cancel()
        results = await asyncio.wait_for(asyncio.gather(*tasks, return_exceptions=True), timeout=1)
        assert all(isinstance(result, asyncio.CancelledError if ending == "cancel" else OSError) for result in results)
        assert len(starts) == app.transfers.project_operations

    asyncio.run(probe())
    assert app._operations.active == 0
    assert base.call(app, "GET", "/v1/records", token=credentials[1]["a"])[0] == 200


def test_n7_real_cli_nonreading_lists_are_refused_with_bounded_rss(tmp_path, credentials, manifest):
    token = credentials[1]["a"]
    with support.cli_server(tmp_path, credentials) as server:
        for i in range(16):
            item = copy.deepcopy(manifest)
            item["descriptor"]["id"] = f"large_{i}"
            item["descriptor"]["description"] = "d" * 1_000_000
            assert base.http_request(server.port, "POST", "/v1/submissions", token=token, body=json.dumps(item).encode())[0] == 201

        def rss():
            with open(f"/proc/{server.process.pid}/status") as status:
                return int(next(line for line in status if line.startswith("VmRSS:")).split()[1]) * 1024

        baseline = rss()
        clients = [support.raw_headers(server.port, "GET", "/v1/records", token) for _ in range(24)]
        try:
            time.sleep(0.2)
            assert rss() - baseline < 96 * 1024 * 1024
            for client in clients:
                assert client.recv(1024).startswith((b"HTTP/1.1 413 ", b"HTTP/1.1 503 "))
            assert base.http_request(server.port, "GET", "/v1/records", token=credentials[1]["b"])[0] == 200
        finally:
            for client in clients:
                client.close()


@pytest.mark.parametrize("kind", ["json", "download", "upload"])
def test_n8_real_cli_graceful_shutdown_is_bounded_with_client_alive(tmp_path, credentials, manifest, kind):
    token = credentials[1]["a"]
    with support.cli_server(tmp_path, credentials, "--max-json-bytes", "8388608", "--send-timeout", "30", "--body-timeout", "30", "--shutdown-timeout", "0.5") as server:
        if kind == "json":
            for i in range(5):
                item = copy.deepcopy(manifest)
                item["descriptor"]["id"] = f"large_{i}"
                item["descriptor"]["description"] = "d" * 1_000_000
                assert base.http_request(server.port, "POST", "/v1/submissions", token=token, body=json.dumps(item).encode())[0] == 201
            method, path, size, prefix = "GET", "/v1/records", None, b""
        else:
            data = b"x" * (8 * 1024 * 1024)
            digest = hashlib.sha256(data).hexdigest()
            item = copy.deepcopy(manifest)
            item["files"] = [{"path": "large.bin", "size": len(data), "sha256": digest, "byte_source": "unknown"}]
            _, pending = base.http_request(server.port, "POST", "/v1/submissions", token=token, body=json.dumps(item).encode())
            submission_path = "/v1/submissions/" + pending["submission_id"]
            if kind == "download":
                assert base.http_request(server.port, "PUT", submission_path + "/files/" + digest, token=token, body=data)[0] == 200
                _, record = base.http_request(server.port, "POST", submission_path + "/commit", token=token)
                method, path, size, prefix = "GET", "/v1/records/" + record["record"]["record_id"] + "/files/" + digest, None, b""
            else:
                method, path, size, prefix = "PUT", submission_path + "/files/" + digest, len(data), b"x" * 100
        # Do not read or close this socket until the process has exited.
        with support.raw_headers(server.port, method, path, token, size=size, prefix=prefix) as client:
            time.sleep(0.2)
            start = time.monotonic()
            server.process.terminate()
            server.process.wait(timeout=3)
            assert time.monotonic() - start < 3
    assert server.stdout == server.stderr == b""


def test_n9_real_cli_port_collision_reports_fixed_path_free_failure(tmp_path, credentials):
    with socket.socket() as busy:
        busy.bind(("127.0.0.1", 0))
        busy.listen()
        port = busy.getsockname()[1]
        result = subprocess.run([sys.executable, "-B", "-m", "nirs4all_datasets.project_service", "serve", "--store", str(tmp_path / "private-store"), "--credentials", str(credentials[0]), "--port", str(port)], capture_output=True, timeout=5)
    assert result.returncode == 1
    assert result.stdout == b""
    assert result.stderr == b"Unable to start project service.\n"
    assert not (tmp_path / "private-store").exists()


@pytest.mark.parametrize("declared", [1, len(base.DATA) + 7])
def test_n10_known_blob_wrong_declared_size_is_not_corrupt(app, credentials, manifest, declared):
    base.upload(app, credentials[1], manifest)
    wrong = base.file_manifest(manifest)
    wrong["descriptor"]["id"] = "different_record"
    wrong["files"][0]["size"] = declared
    pending = base.begin(app, credentials[1], wrong)
    assert base.call(app, "POST", "/v1/submissions/" + pending["submission_id"] + "/commit", token=credentials[1]["a"])[:2] == (400, {"error": "size_mismatch"})
    assert len(base.call(app, "GET", "/v1/records", token=credentials[1]["a"])[1]["records"]) == 1


def test_n7_small_response_cap_preserves_successful_write_receipts(app, credentials, manifest):
    app.transfers = replace(app.transfers, json_bytes=512)
    first = base.begin(app, credentials[1], manifest)
    assert set(first) == {"status", "record_id"} and first["status"] == "created"
    assert base.begin(app, credentials[1], manifest) == {"status": "already_present", "record_id": first["record_id"]}
    assert base.call(app, "GET", "/v1/records/" + first["record_id"], token=credentials[1]["a"])[:2] == (413, {"error": "response_too_large"})
    app.transfers = replace(app.transfers, json_bytes=2_097_152)
    assert base.call(app, "GET", "/v1/records/" + first["record_id"], token=credentials[1]["a"])[0] == 200


def test_n6_verification_is_fresh_but_deduplicated_within_each_request(app, credentials, manifest, monkeypatch):
    item = base.file_manifest(manifest)
    item["files"].append(dict(item["files"][0], path="alias.bin"))
    pending = base.begin(app, credentials[1], item)
    path = "/v1/submissions/" + pending["submission_id"]
    assert base.call(app, "PUT", path + "/files/" + base.DIGEST, token=credentials[1]["a"], body=base.DATA)[0] == 200
    record = base.call(app, "POST", path + "/commit", token=credentials[1]["a"])[1]["record"]
    original = app.store._blob
    calls = []

    def observed(*args, **kwargs):
        calls.append(True)
        return original(*args, **kwargs)

    monkeypatch.setattr(app.store, "_blob", observed)
    route = "/v1/records/" + record["record_id"]
    assert base.call(app, "GET", route, token=credentials[1]["a"])[0] == 200
    assert len(calls) == 1
    next(app.store.root.rglob(base.DIGEST)).write_bytes(b"x" * len(base.DATA))
    assert base.call(app, "GET", route, token=credentials[1]["a"])[:2] == (409, {"error": "corrupt_record"})
    assert len(calls) == 2
