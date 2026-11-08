"""Project-service contract tests and real loopback Uvicorn integration."""
from __future__ import annotations

import asyncio
import copy
import errno
import hashlib
import http.client
import ipaddress
import json
import os
import socket
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import replace
from pathlib import Path

import pytest

leaf = pytest.importorskip("nirs4all_access")

from nirs4all_datasets.private_store import DISK_FLOOR_BYTES, StoreLimits
from nirs4all_datasets.project_service import ServiceConfigurationError, create_app, main

DATA = b"Synthetic opaque private bytes\x00\xff"
DIGEST = hashlib.sha256(DATA).hexdigest()
ROUTE_CASES = [
    ("POST", "/v1/submissions", "add"),
    ("PUT", "/v1/submissions/" + "a" * 32 + "/files/" + DIGEST, "add"),
    ("POST", "/v1/submissions/" + "a" * 32 + "/commit", "add"),
    ("GET", "/v1/records", "read"),
    ("GET", "/v1/records/" + "a" * 64, "read"),
    ("GET", "/v1/records/" + "a" * 64 + "/files/" + DIGEST, "read"),
]


@pytest.fixture(autouse=True)
def loopback_only(monkeypatch):
    connect, connect_ex, resolve = socket.socket.connect, socket.socket.connect_ex, socket.getaddrinfo

    def check(address):
        try:
            allowed = isinstance(address, tuple) and ipaddress.ip_address(address[0]).is_loopback
        except ValueError:
            allowed = False
        if not allowed:
            raise AssertionError("External network forbidden")

    def guarded(sock, address):
        check(address)
        return connect(sock, address)

    def guarded_ex(sock, address):
        check(address)
        return connect_ex(sock, address)

    def guarded_dns(host, port, *args, **kwargs):
        check((host, port))
        return resolve(host, port, *args, **kwargs)

    monkeypatch.setattr(socket.socket, "connect", guarded)
    monkeypatch.setattr(socket.socket, "connect_ex", guarded_ex)
    monkeypatch.setattr(socket, "getaddrinfo", guarded_dns)


@pytest.fixture
def credentials(tmp_path):
    tokens, records = {}, []
    for name, project, service, rights in [
        ("a", "project-a", "datasets", ("read", "add")),
        ("b", "project-b", "datasets", ("read", "add")),
        ("reader", "project-a", "datasets", ("read",)),
        ("writer", "project-a", "datasets", ("add",)),
        ("wrong", "project-a", "arena", ("read",)),
        ("revoked", "project-a", "datasets", ("read", "add")),
        ("expired", "project-a", "datasets", ("read", "add")),
    ]:
        principal = leaf.ProjectPrincipal(project, name, frozenset({service}), frozenset(f"{service}.{right}" for right in rights))
        token, record = leaf.issue_credential(principal)
        tokens[name] = token
        if name == "revoked":
            record = replace(record, revoked=True)
        elif name == "expired":
            record = replace(record, expires_at=time.time() - 1)
        records.append(record)
    path = tmp_path / "credentials.json"
    leaf.write_credential_store(path, records)
    return path, tokens, records


@pytest.fixture
def app(tmp_path, credentials):
    service = create_app(store=tmp_path / "private-store", credential_store=credentials[0])
    yield service
    service.close()


@pytest.fixture
def manifest():
    return {"descriptor": {"id": "service_example", "name": "Example", "description": "Asserted metadata",
                           "sources": [{"source_id": "X"}], "provenance": {"contributor": "Asserted"}, "governance": {"license": "NOASSERTION"},
                           "origin_sources": [{"kind": "zenodo", "locator": "10.5281/zenodo.1"}],
                           "retrieval": {"routes": [{"id": "inert", "locator": "http://169.254.169.254/never-fetch"}]}}, "files": []}


def file_manifest(manifest):
    result = copy.deepcopy(manifest)
    result["files"] = [{"path": "asserted/opaque.bin", "sha256": DIGEST, "size": len(DATA), "byte_source": "unknown"}]
    return result


async def asgi_call(app, method, path, *, token=None, body=b"", chunks=None, headers=(), query=b"", forbid_body=False, events=None):
    sent, received = [], []
    frames = list(events) if events is not None else [{"type": "http.request", "body": chunk, "more_body": i < len(parts) - 1}
                                                     for parts in [list(chunks) if chunks is not None else [body]] for i, chunk in enumerate(parts)]

    async def receive():
        received.append(True)
        if forbid_body:
            raise AssertionError("Body read before refusal")
        if not frames:
            raise AssertionError("Unexpected extra body read")
        return frames.pop(0)

    async def send(message):
        sent.append(message)

    request_headers = [(b"content-type", b"application/json"), *headers]
    if token is not None:
        request_headers.append((b"authorization", ("Bearer " + token).encode()))
    scope = {"type": "http", "http_version": "1.1", "method": method, "path": path, "raw_path": path.encode(),
             "query_string": query, "headers": request_headers, "scheme": "http", "server": ("127.0.0.1", 8000), "client": ("127.0.0.1", 12345)}
    await app(scope, receive, send)
    assert sent[0]["type"] == "http.response.start"
    response_body = b"".join(m.get("body", b"") for m in sent[1:])
    return sent[0]["status"], response_body, dict(sent[0]["headers"]), len(received)


def call(*args, **kwargs):
    status, body, headers, count = asyncio.run(asgi_call(*args, **kwargs))
    return status, json.loads(body) if headers[b"content-type"].startswith(b"application/json") else body, headers, count


def begin(app, tokens, manifest, who="a"):
    status, result, _, _ = call(app, "POST", "/v1/submissions", token=tokens[who], body=json.dumps(manifest).encode())
    assert status in (200, 201, 202), result
    return result


def upload(app, tokens, manifest, who="a"):
    pending = begin(app, tokens, file_manifest(manifest), who)
    if pending["status"] == "already_present":
        return pending["record"]
    prefix = "/v1/submissions/" + pending["submission_id"]
    assert call(app, "PUT", prefix + "/files/" + DIGEST, token=tokens[who], chunks=[DATA[:5], DATA[5:]])[0] == 200
    status, result, _, _ = call(app, "POST", prefix + "/commit", token=tokens[who])
    assert status in (200, 201), result
    return result["record"]


@pytest.mark.parametrize(("method", "path", "right"), ROUTE_CASES)
@pytest.mark.parametrize("who", [None, "revoked", "expired", "wrong", "insufficient"])
def test_authentication_and_rights_refuse_before_every_body(app, credentials, method, path, right, who):
    tokens = credentials[1]
    name = ("reader" if right == "add" else "writer") if who == "insufficient" else who
    status, result, headers, count = call(app, method, path, token=tokens[name] if name else None, forbid_body=True)
    assert status == (403 if who in {"wrong", "insufficient"} else 401)
    assert count == 0
    assert result["error"] in {"invalid_credential", "service_not_granted", "missing_rights"}
    assert (headers.get(b"www-authenticate") == b"Bearer") == (status == 401)
    assert not app.store.root.exists()


@pytest.mark.parametrize(("method", "path"), [("GET", "/unknown"), ("DELETE", "/v1/records"), ("HEAD", "/v1/records"), ("GET", "/v1/projects/project-b/records"), ("PUT", "/v1/submissions/../files/" + DIGEST), ("GET", "/v1/records/" + "a" * 64 + "\n")])
def test_closed_table_has_no_fallback_routes(app, credentials, method, path):
    assert call(app, method, path, forbid_body=True)[0] == 401
    assert call(app, method, path, token=credentials[1]["a"], forbid_body=True)[0] == 404


def test_duplicate_or_query_credentials_and_project_selectors_are_never_used(app, credentials):
    token = credentials[1]["a"]
    assert call(app, "GET", "/v1/records", query=("token=" + token).encode(), forbid_body=True)[0] == 401
    duplicate = [(b"authorization", ("Bearer " + token).encode())]
    assert call(app, "GET", "/v1/records", token=token, headers=duplicate, forbid_body=True)[0] == 401
    for headers, query in [([(b"x-project-id", b"project-b")], b""), ([(b"x-custom-project", b"project-b")], b""), ([], b"project=project-b")]:
        assert call(app, "GET", "/v1/records", token=token, headers=headers, query=query, forbid_body=True)[0] == 400


def test_health_has_no_paths_tokens_or_body_reads(app, credentials):
    assert call(app, "GET", "/healthz", forbid_body=True)[:2] == (200, {"status": "ok"})
    assert not app.store.root.exists()


def test_metadata_only_preserves_assertions_and_first_stamps_after_restart(app, credentials, manifest):
    tokens = credentials[1]
    result = begin(app, tokens, manifest)
    record = result["record"]
    assert record["descriptor"] == manifest["descriptor"]
    assert record["project_id"] == "project-a" and record["principal_id"] == "a"
    assert record["rights_status"] == record["provenance_status"] == "asserted_unverified"
    assert record["content_validated"] == "hash_only"
    assert not {"tier", "versions", "dataverse", "generation"}.intersection(record["descriptor"])
    restarted = create_app(store=app.store.root, credential_store=credentials[0])
    repeated = begin(restarted, tokens, manifest, "writer")
    assert repeated == {"status": "already_present", "record_id": record["record_id"]}
    assert call(restarted, "GET", "/v1/records", token=tokens["reader"])[1] == {"records": [record]}


def test_manifest_first_uploads_pending_hidden_and_restart(app, credentials, manifest):
    tokens = credentials[1]
    assert call(app, "PUT", ROUTE_CASES[1][1], token=tokens["a"], forbid_body=True)[0] == 404
    assert not app.store.root.exists()
    pending = begin(app, tokens, file_manifest(manifest))
    assert call(app, "GET", "/v1/records", token=tokens["a"])[1] == {"records": []}
    prefix = "/v1/submissions/" + pending["submission_id"]
    assert call(app, "PUT", prefix + "/files/" + "0" * 64, token=tokens["a"], forbid_body=True)[:2] == (400, {"error": "undeclared_digest"})
    assert call(app, "POST", prefix + "/commit", token=tokens["a"])[:2] == (409, {"error": "missing_blob"})
    assert call(app, "PUT", prefix + "/files/" + DIGEST, token=tokens["a"], chunks=[DATA[:5], DATA[5:]])[0] == 200
    restarted = create_app(store=app.store.root, credential_store=credentials[0])
    assert call(restarted, "POST", prefix + "/commit", token=tokens["a"])[0] == 201
    assert call(restarted, "GET", "/v1/records/" + pending["record_id"] + "/files/" + DIGEST, token=tokens["a"])[1] == DATA


def test_foreign_resources_are_404_and_ids_are_independent(app, credentials, manifest):
    tokens = credentials[1]
    pending = begin(app, tokens, file_manifest(manifest), "b")
    prefix = "/v1/submissions/" + pending["submission_id"]
    assert call(app, "PUT", prefix + "/files/" + DIGEST, token=tokens["a"], forbid_body=True)[0] == 404
    assert call(app, "POST", prefix + "/commit", token=tokens["a"])[0] == 404
    b_record = upload(app, tokens, manifest, "b")
    for path in ("/v1/records/" + b_record["record_id"], "/v1/records/" + b_record["record_id"] + "/files/" + DIGEST):
        assert call(app, "GET", path, token=tokens["a"])[0] == 404
    assert call(app, "GET", "/v1/records", token=tokens["a"])[1] == {"records": []}
    a_record = upload(app, tokens, manifest, "a")
    assert a_record["record_id"] == b_record["record_id"]
    assert a_record["project_id"] != b_record["project_id"]
    paths = list(app.store.root.rglob(DIGEST))
    assert len(paths) == 2 and paths[0].stat().st_ino != paths[1].stat().st_ino


@pytest.mark.parametrize(("change", "error"), [
    ({"byte_source": "public_origin_download"}, "public_origin_download_refused"),
    ({"fetch": True}, "fetch_or_mirror_refused"), ({"path": "../bad"}, "invalid_filename"),
    ({"legal_attestation": True}, "unknown_field"),
])
def test_manifest_refusal_happens_before_any_payload_storage(app, credentials, manifest, change, error):
    submission = file_manifest(manifest)
    submission["files"][0].update(change)
    assert call(app, "POST", "/v1/submissions", token=credentials[1]["a"], body=json.dumps(submission).encode())[:2] == (400, {"error": error})
    assert not app.store.root.exists()


@pytest.mark.parametrize(("body", "code"), [(DATA[:-1], "size_mismatch"), (DATA + b"x", "size_mismatch"), (b"x" * len(DATA), "digest_mismatch")])
def test_upload_integrity_failures_are_safe_and_retryable(app, credentials, manifest, body, code):
    pending = begin(app, credentials[1], file_manifest(manifest))
    path = "/v1/submissions/" + pending["submission_id"] + "/files/" + DIGEST
    assert call(app, "PUT", path, token=credentials[1]["a"], body=body)[:2] == (400, {"error": code})
    assert not list(app.store.root.rglob(DIGEST))
    assert not list(app.store.root.rglob(".tmp-*"))
    assert upload(app, credentials[1], manifest)["files"][0]["byte_source"] == "unknown"


def test_corrected_manifest_after_failed_upload_can_keep_identity(app, credentials, manifest):
    wrong = file_manifest(manifest)
    typo = hashlib.sha256(b"mistyped").hexdigest()
    wrong["files"][0]["sha256"] = typo
    pending = begin(app, credentials[1], wrong)
    path = "/v1/submissions/" + pending["submission_id"] + "/files/" + typo
    assert call(app, "PUT", path, token=credentials[1]["a"], body=DATA)[1] == {"error": "digest_mismatch"}
    record = upload(app, credentials[1], manifest)
    assert record["descriptor"] == manifest["descriptor"]


def test_unsafe_foreign_project_and_corrupt_pending_do_not_block_http_writes(app, credentials, manifest, tmp_path):
    upload(app, credentials[1], manifest, "b")
    b_root = app.store.root / "projects" / hashlib.sha256(b"project-b").hexdigest()
    target = tmp_path / "untouched"
    target.write_bytes(b"untouched")
    (b_root / "evil").symlink_to(target)
    reopened = create_app(store=app.store.root, credential_store=credentials[0])
    pending = begin(reopened, credentials[1], file_manifest(manifest))
    a_root = app.store.root / "projects" / hashlib.sha256(b"project-a").hexdigest()
    (a_root / "pending" / (pending["submission_id"] + ".json")).write_bytes(b"{broken")
    other = copy.deepcopy(manifest)
    other["descriptor"]["id"] = "unrelated"
    assert begin(reopened, credentials[1], other)["status"] == "created"
    prefix = "/v1/submissions/" + pending["submission_id"]
    assert call(reopened, "PUT", prefix + "/files/" + DIGEST, token=credentials[1]["a"], forbid_body=True)[:2] == (409, {"error": "corrupt_record"})
    assert call(reopened, "POST", "/v1/submissions", token=credentials[1]["b"], body=json.dumps(other).encode())[:2] == (400, {"error": "symlink_refused"})
    assert target.read_bytes() == b"untouched"


@pytest.mark.parametrize("raw", [b"\xff", b"{}", b'{"descriptor":{},"descriptor":{}}', b"\xef\xbb\xbf{}", "{}".encode("utf-16")])
def test_bad_transport_json_is_refused_without_storage(app, credentials, raw):
    assert call(app, "POST", "/v1/submissions", token=credentials[1]["a"], body=raw)[:2] == (400, {"error": "invalid_manifest"})
    assert not app.store.root.exists()


def test_response_disconnect_does_not_start_a_second_response(app, credentials):
    async def probe():
        starts = []

        async def receive():
            raise AssertionError("GET must not read a body")

        async def send(message):
            if message["type"] == "http.response.start":
                starts.append(message)
            else:
                raise OSError(errno.EPIPE, "client disconnected")

        scope = {"type": "http", "method": "GET", "path": "/v1/records", "headers": [(b"authorization", ("Bearer " + credentials[1]["a"]).encode())]}
        with pytest.raises(OSError):
            await app(scope, receive, send)
        assert len(starts) == 1

    asyncio.run(probe())


def test_manifest_limits_count_actual_frames_without_trusting_length(tmp_path, credentials, manifest):
    app = create_app(store=tmp_path / "private-store", credential_store=credentials[0], limits=StoreLimits(max_manifest_bytes=10))
    for headers in ([], [(b"content-length", b"1")]):
        assert call(app, "POST", "/v1/submissions", token=credentials[1]["a"], chunks=[b"12345", b"678901"], headers=headers)[0] == 413
    assert call(app, "POST", "/v1/submissions", token=credentials[1]["a"], headers=[(b"content-length", b"11")], forbid_body=True)[0] == 413
    assert not app.store.root.exists()


def test_upload_limits_count_actual_chunks_and_disconnect_cleanup(tmp_path, credentials, manifest):
    app = create_app(store=tmp_path / "private-store", credential_store=credentials[0], limits=StoreLimits(max_file_bytes=len(DATA)))
    pending = begin(app, credentials[1], file_manifest(manifest))
    path = "/v1/submissions/" + pending["submission_id"] + "/files/" + DIGEST
    assert call(app, "PUT", path, token=credentials[1]["a"], chunks=[DATA[:5], DATA[5:] + b"x"], headers=[(b"content-length", b"1")])[0] == 413
    events = [{"type": "http.request", "body": DATA[:3], "more_body": True}, {"type": "http.disconnect"}]
    assert call(app, "PUT", path, token=credentials[1]["a"], events=events)[:2] == (400, {"error": "client_disconnected"})
    assert not list(app.store.root.rglob(DIGEST))
    assert not list(app.store.root.rglob(".tmp-*"))


@pytest.mark.parametrize("headers", [[(b"content-length", b"-1")], [(b"content-length", b"1"), (b"content-length", b"1")], [(b"content-encoding", b"gzip")]])
def test_ambiguous_or_encoded_bodies_refused_before_receive(app, credentials, headers):
    assert call(app, "POST", "/v1/submissions", token=credentials[1]["a"], headers=headers, forbid_body=True)[0] in (400, 415)


def test_store_io_errors_and_disk_floor_do_not_leak_paths_or_tokens(app, credentials, manifest, monkeypatch):
    token = credentials[1]["a"]

    def eio(*args, **kwargs):
        raise OSError(errno.EIO, "private path and token " + str(app.store.root) + token)

    with monkeypatch.context() as patch:
        patch.setattr(app.store, "list_records", eio)
        assert call(app, "GET", "/v1/records", token=token)[:2] == (500, {"error": "storage_failure"})
    with monkeypatch.context() as patch:
        from types import SimpleNamespace
        patch.setattr(os, "fstatvfs", lambda _: SimpleNamespace(f_bavail=DISK_FLOOR_BYTES - 1, f_frsize=1))
        assert call(app, "POST", "/v1/submissions", token=token, body=json.dumps(manifest).encode())[:2] == (507, {"error": "insufficient_storage"})
    assert not app.store.root.exists()


def test_credential_snapshot_revocation_applies_at_restart(app, credentials):
    path, tokens, records = credentials
    changed = [replace(r, revoked=True) if r.principal.principal_id == "a" else r for r in records]
    leaf.write_credential_store(path, changed)
    assert call(app, "GET", "/v1/records", token=tokens["a"])[0] == 200
    restarted = create_app(store=app.store.root, credential_store=path)
    assert call(restarted, "GET", "/v1/records", token=tokens["a"], forbid_body=True)[0] == 401


@pytest.mark.parametrize("kind", ["empty", "expired", "revoked", "wrong_service", "missing", "fifo"])
def test_invalid_or_inactive_credentials_refuse_startup_without_leaks(tmp_path, credentials, kind):
    path, _, records = credentials
    if kind == "missing":
        path.unlink()
    elif kind == "fifo":
        path.unlink()
        os.mkfifo(path)
    else:
        selected = [] if kind == "empty" else [r for r in records if r.principal.principal_id == {"expired": "expired", "revoked": "revoked", "wrong_service": "wrong"}[kind]]
        leaf.write_credential_store(path, selected)
    with pytest.raises(ServiceConfigurationError) as caught:
        create_app(store=tmp_path / "private-store", credential_store=path)
    assert str(tmp_path) not in str(caught.value)
    assert not (tmp_path / "private-store").exists()


def test_secure_transport_and_cli_require_explicit_local_configuration(tmp_path, credentials, capsys):
    with pytest.raises(ServiceConfigurationError):
        create_app(store=tmp_path / "private-store", credential_store=credentials[0], host="example.org")
    create_app(store=tmp_path / "private-store", credential_store=credentials[0], host="example.org", tls=True)
    with pytest.raises(SystemExit) as caught:
        main(["serve"])
    assert caught.value.code == 2
    with pytest.raises(SystemExit) as caught:
        main(["serve", "--store", str(tmp_path / "store"), "--credentials", "/missing/private/path"])
    assert caught.value.code == 2
    assert "/missing/private/path" not in capsys.readouterr().err


def test_total_body_deadline_cleans_upload(app, credentials, manifest):
    pending = begin(app, credentials[1], file_manifest(manifest))
    app.body_timeout = 0.02
    path = "/v1/submissions/" + pending["submission_id"] + "/files/" + DIGEST

    async def probe():
        sent = []

        async def receive():
            await asyncio.sleep(1)
            return {"type": "http.request", "body": DATA}

        async def send(message):
            sent.append(message)

        await app({"type": "http", "method": "PUT", "path": path, "headers": [(b"authorization", ("Bearer " + credentials[1]["a"]).encode())]}, receive, send)
        assert sent[0]["status"] == 408

    asyncio.run(probe())
    assert not list(app.store.root.rglob(".tmp-*"))
    assert not list(app.store.root.rglob(DIGEST))


def test_cancelled_asgi_upload_releases_temp_lease_and_worker(app, credentials, manifest):
    pending = begin(app, credentials[1], file_manifest(manifest))
    path = "/v1/submissions/" + pending["submission_id"] + "/files/" + DIGEST

    async def probe():
        entered = asyncio.Event()

        async def receive():
            entered.set()
            await asyncio.sleep(100)
            return {"type": "http.request", "body": DATA}

        async def send(message):
            raise AssertionError("A cancelled upload must not send a new response")

        scope = {"type": "http", "method": "PUT", "path": path, "headers": [(b"authorization", ("Bearer " + credentials[1]["a"]).encode())]}
        task = asyncio.create_task(app(scope, receive, send))
        await asyncio.wait_for(entered.wait(), timeout=2)
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await asyncio.wait_for(task, timeout=2)

    asyncio.run(probe())
    assert not list(app.store.root.rglob(".tmp-*"))
    assert not list(app.store.root.rglob(DIGEST))


def test_base_offline_store_imports_and_commits_without_service_or_leaf(tmp_path, manifest):
    script = """
import importlib.abc,json,sys
root, source, manifest = json.load(sys.stdin)
sys.path.insert(0,source)
class Blocker(importlib.abc.MetaPathFinder):
 def find_spec(self, fullname, path=None, target=None):
  if fullname.split('.')[0] in {'nirs4all_access','uvicorn','fastapi','starlette','requests','pandas','pyarrow'}:
   raise AssertionError('Optional dependency imported: '+fullname)
sys.meta_path.insert(0,Blocker())
from nirs4all_datasets.private_store import PrivateStore,StoreContext
import nirs4all_datasets.project_service
assert PrivateStore(root).begin(StoreContext('offline','operator'),manifest)['status']=='created'
"""
    repo = Path(__file__).resolve().parents[1]
    result = subprocess.run([str(repo / ".venv/bin/python"), "-I", "-B", "-c", script], input=json.dumps([str(tmp_path / "offline"), str(repo / "src"), manifest]), capture_output=True, text=True, timeout=10)
    assert result.returncode == 0, result.stderr


@pytest.fixture
def live_server(app):
    uvicorn = pytest.importorskip("uvicorn")
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(("127.0.0.1", 0))
    listener.listen(64)
    port = listener.getsockname()[1]
    server = uvicorn.Server(uvicorn.Config(app, host="127.0.0.1", port=port, loop="asyncio", http="h11", ws="none", lifespan="on", access_log=False, log_level="critical", server_header=False, proxy_headers=False))
    thread = threading.Thread(target=server.run, kwargs={"sockets": [listener]}, daemon=True)
    thread.start()
    deadline = time.monotonic() + 5
    while not server.started and thread.is_alive() and time.monotonic() < deadline:
        time.sleep(0.01)
    try:
        assert server.started, "Loopback Uvicorn did not start"
        yield port
    finally:
        server.should_exit = True
        thread.join(10)
        listener.close()
        assert not thread.is_alive(), "Loopback Uvicorn did not stop"


def http_request(port, method, path, *, token=None, body=None, chunked=False):
    connection = http.client.HTTPConnection("127.0.0.1", port, timeout=5)
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = "Bearer " + token
    try:
        connection.request(method, path, body=body, headers=headers, encode_chunked=chunked)
        response = connection.getresponse()
        payload = response.read()
        return response.status, json.loads(payload) if response.getheader("Content-Type", "").startswith("application/json") else payload
    finally:
        connection.close()


def test_real_loopback_manifest_stream_commit_query_and_restart(live_server, app, credentials, manifest):
    port, tokens = live_server, credentials[1]
    assert http_request(port, "GET", "/healthz") == (200, {"status": "ok"})
    assert http_request(port, "GET", "/v1/records")[0] == 401
    submission = file_manifest(manifest)
    status, pending = http_request(port, "POST", "/v1/submissions", token=tokens["a"], body=json.dumps(submission).encode())
    assert status == 202
    prefix = "/v1/submissions/" + pending["submission_id"]
    assert http_request(port, "PUT", prefix + "/files/" + DIGEST, token=tokens["b"], body=DATA)[0] == 404
    assert http_request(port, "PUT", prefix + "/files/" + DIGEST, token=tokens["a"], body=iter([DATA[:5], DATA[5:]]), chunked=True)[0] == 200
    assert http_request(port, "POST", prefix + "/commit", token=tokens["a"])[0] == 201
    assert http_request(port, "GET", "/v1/records/" + pending["record_id"] + "/files/" + DIGEST, token=tokens["a"])[1] == DATA
    reopened = create_app(store=app.store.root, credential_store=credentials[0])
    assert call(reopened, "GET", "/v1/records/" + pending["record_id"], token=tokens["a"])[0] == 200


def test_real_loopback_auth_replies_before_promised_body(live_server, credentials):
    for who, expected in [(None, 401), ("reader", 403)]:
        headers = b"" if who is None else ("Authorization: Bearer " + credentials[1][who] + "\r\n").encode()
        with socket.create_connection(("127.0.0.1", live_server), timeout=3) as connection:
            connection.sendall(b"POST /v1/submissions HTTP/1.1\r\nHost: 127.0.0.1\r\nContent-Type: application/json\r\nContent-Length: 999999\r\n" + headers + b"\r\n")
            # No request-body byte is sent. A pre-body front door replies now.
            response = connection.recv(4096)
            assert response.startswith(f"HTTP/1.1 {expected} ".encode()), response
            if expected == 401:
                assert b"www-authenticate: Bearer" in response


def test_real_loopback_eight_identical_and_cross_project_writers(live_server, credentials, manifest):
    port, tokens = live_server, credentials[1]

    def writer(who):
        deadline = time.monotonic() + 3
        while True:
            status, result = http_request(port, "POST", "/v1/submissions", token=tokens[who], body=json.dumps(manifest).encode())
            if status != 503:
                assert status in (200, 201)
                return result
            assert result == {"error": "store_busy"}
            assert time.monotonic() < deadline
            time.sleep(0.02)

    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(writer, ["a"] * 8))
    assert sum(r["status"] == "created" for r in results) == 1
    assert all(r["record"] == results[0]["record"] for r in results)
    with ThreadPoolExecutor(max_workers=2) as pool:
        cross = list(pool.map(writer, ["a", "b"]))
    assert [r["record"]["project_id"] for r in cross] == ["project-a", "project-b"]


def test_real_loopback_stalled_upload_does_not_block_same_project(live_server, app, credentials, manifest):
    port, tokens = live_server, credentials[1]
    _, pending = http_request(port, "POST", "/v1/submissions", token=tokens["a"], body=json.dumps(file_manifest(manifest)).encode())
    path = "/v1/submissions/" + pending["submission_id"] + "/files/" + DIGEST
    other = copy.deepcopy(manifest)
    other["descriptor"]["id"] = "another"
    with socket.create_connection(("127.0.0.1", port), timeout=3) as connection:
        connection.sendall((f"PUT {path} HTTP/1.1\r\nHost: 127.0.0.1\r\nAuthorization: Bearer {tokens['a']}\r\nContent-Length: {len(DATA)}\r\n\r\n").encode() + DATA[:3])
        deadline = time.monotonic() + 3
        while not list(app.store.root.rglob(".tmp-*")) and time.monotonic() < deadline:
            time.sleep(0.01)
        assert list(app.store.root.rglob(".tmp-*"))
        assert http_request(port, "POST", "/v1/submissions", token=tokens["a"], body=json.dumps(other).encode())[0] == 201
        connection.sendall(DATA[3:])
        assert connection.recv(4096).startswith(b"HTTP/1.1 200 ")


def test_real_loopback_chunked_cap_enforced_without_content_length(live_server, app, credentials):
    payload = iter([b"x" * 65_536] * 17)
    status, result = http_request(live_server, "POST", "/v1/submissions", token=credentials[1]["a"], body=payload, chunked=True)
    assert (status, result) == (413, {"error": "request_too_large"})
    assert not app.store.root.exists()


def test_real_entrypoint_process_restart_preserves_records_and_reloads_revocations(tmp_path, credentials, manifest):
    path, tokens, records = credentials
    root = tmp_path / "cli-private-store"
    script = """
import ipaddress,runpy,socket
connect,resolve=socket.socket.connect,socket.getaddrinfo
def check(address):
 if not isinstance(address,tuple) or not ipaddress.ip_address(address[0]).is_loopback:
  raise AssertionError('External network forbidden')
def guarded(sock,address):
 check(address)
 return connect(sock,address)
def dns(host,port,*args,**kwargs):
 check((host,port))
 return resolve(host,port,*args,**kwargs)
socket.socket.connect=guarded
socket.getaddrinfo=dns
runpy.run_module('nirs4all_datasets.project_service',run_name='__main__')
"""
    record = None
    for restart in (False, True):
        with socket.socket() as reservation:
            reservation.bind(("127.0.0.1", 0))
            port = reservation.getsockname()[1]
        process = subprocess.Popen([sys.executable, "-B", "-c", script, "serve", "--store", str(root), "--credentials", str(path), "--port", str(port)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        try:
            deadline = time.monotonic() + 5
            while time.monotonic() < deadline and process.poll() is None:
                try:
                    if http_request(port, "GET", "/healthz")[0] == 200:
                        break
                except (ConnectionError, OSError):
                    time.sleep(0.02)
            else:
                pytest.fail("Local serve entrypoint did not start")
            if not restart:
                status, result = http_request(port, "POST", "/v1/submissions", token=tokens["a"], body=json.dumps(manifest).encode())
                assert status == 201
                record = result["record"]
                leaf.write_credential_store(path, [replace(r, revoked=True) if r.principal.principal_id == "a" else r for r in records])
                assert http_request(port, "GET", "/v1/records", token=tokens["a"])[0] == 200
            else:
                assert http_request(port, "GET", "/v1/records", token=tokens["a"])[0] == 401
                assert http_request(port, "GET", "/v1/records", token=tokens["reader"]) == (200, {"records": [record]})
        finally:
            process.terminate()
            try:
                stdout, stderr = process.communicate(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                stdout, stderr = process.communicate(timeout=5)
            assert all(token not in stdout + stderr for token in tokens.values())
