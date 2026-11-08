"""Optional pure-ASGI project service for the separate private store.

Authentication uses the shared access leaf before receiving request bodies.
The leaf and Uvicorn are imported only when creating/serving an application.
"""
from __future__ import annotations

import argparse
import asyncio
import errno
import json
import math
import re
import threading
import time
from collections.abc import Awaitable, Callable, Iterator
from concurrent.futures import ThreadPoolExecutor
from contextlib import AbstractContextManager, contextmanager, suppress
from dataclasses import dataclass
from functools import partial
from importlib import import_module
from pathlib import Path
from typing import Any, BinaryIO

from nirs4all_datasets.private_store import PrivateStore, PrivateStoreError, StoreContext, StoreLimits

Scope = dict[str, Any]
Message = dict[str, Any]
Receive = Callable[[], Awaitable[Message]]
Send = Callable[[Message], Awaitable[None]]
_HASH = r"[0-9a-f]{64}"
_SUBMISSION = r"[0-9a-f]{32}"
_CHUNK_BYTES = 65_536


@dataclass(frozen=True)
class Route:
    """Every accepted route and its required right is declared here."""

    method: str
    pattern: str
    right: str
    operation: str


ROUTES = (
    Route("POST", r"/v1/submissions", "datasets.add", "begin"),
    Route("PUT", rf"/v1/submissions/(?P<submission_id>{_SUBMISSION})/files/(?P<sha256>{_HASH})", "datasets.add", "put_file"),
    Route("POST", rf"/v1/submissions/(?P<submission_id>{_SUBMISSION})/commit", "datasets.add", "commit"),
    Route("GET", r"/v1/records", "datasets.read", "list_records"),
    Route("GET", rf"/v1/records/(?P<record_id>{_HASH})", "datasets.read", "get_record"),
    Route("GET", rf"/v1/records/(?P<record_id>{_HASH})/files/(?P<sha256>{_HASH})", "datasets.read", "read_file"),
)


class ServiceConfigurationError(Exception):
    """Safe startup failure without credential contents or filesystem paths."""


@dataclass(frozen=True)
class TransferLimits:
    """Immediate admission, with capacity reserved against any single project."""

    uploads: int = 8
    project_uploads: int = 2
    downloads: int = 4
    project_downloads: int = 1
    send_timeout: float = 15.0
    operations: int = 16
    project_operations: int = 4
    json_bytes: int = 2_097_152
    list_records: int = 100
    shutdown_timeout: float = 2.0

    def __post_init__(self) -> None:
        if any(type(v) is not int or not 1 <= v <= 64 for v in (self.uploads, self.project_uploads, self.downloads, self.project_downloads, self.operations, self.project_operations)):
            raise ValueError("invalid transfer limits")
        if self.project_uploads >= self.uploads or self.project_downloads >= self.downloads or self.project_operations >= self.operations:
            raise ValueError("per-project limits must leave capacity for other projects")
        for timeout in (self.send_timeout, self.shutdown_timeout):
            if type(timeout) not in (int, float) or not math.isfinite(timeout) or timeout <= 0:
                raise ValueError("invalid timeout")
        if type(self.json_bytes) is not int or not 256 <= self.json_bytes <= 67_108_864 or type(self.list_records) is not int or self.list_records <= 0:
            raise ValueError("invalid JSON response limits")


class _Admission:
    def __init__(self, total: int, per_project: int) -> None:
        self.total, self.per_project = total, per_project
        self.active = 0
        self.projects: dict[str, int] = {}
        self.lock = threading.Lock()

    @contextmanager
    def reserve(self, project: str) -> Iterator[None]:
        with self.lock:
            count = self.projects.get(project, 0)
            if self.active >= self.total or count >= self.per_project:
                raise PrivateStoreError("store_busy", 503)
            self.active += 1
            self.projects[project] = count + 1
        try:
            yield
        finally:
            with self.lock:
                self.active -= 1
                self.projects[project] -= 1
                if not self.projects[project]:
                    del self.projects[project]


class _ResponseStarted(OSError):
    """Close a partial response; never attempt a second response start."""


@dataclass
class _Response:
    target: Send
    started: bool = False

    async def send(self, message: Message) -> None:
        if message["type"] == "http.response.start":
            if self.started:
                raise _ResponseStarted("response already started")
            # A failed start may already have written headers to the transport.
            self.started = True
        await self.target(message)


class _Download:
    def __init__(self, manager: AbstractContextManager[tuple[BinaryIO, int]]) -> None:
        self.manager = manager
        self.stream: BinaryIO | None = None
        self.size = 0

    def open(self) -> None:
        self.stream, self.size = self.manager.__enter__()

    def read(self) -> bytes:
        assert self.stream is not None
        return self.stream.read(_CHUNK_BYTES)

    def close(self) -> None:
        if self.stream is not None:
            try:
                self.manager.__exit__(None, None, None)
            finally:
                self.stream = None


class _Body:
    """Count actual ASGI bytes, with a total deadline and bounded output chunks."""

    def __init__(self, receive: Receive, cap: int, timeout: float) -> None:
        self.receive = receive
        self.cap = cap
        self.deadline = time.monotonic() + timeout
        self.count = 0
        self.done = False
        self.buffer = memoryview(b"")
        self.pending: asyncio.Future[Message] | None = None
        self.aborted = False

    def abort(self) -> None:
        self.aborted = True
        if self.pending is not None:
            self.pending.cancel()

    async def next(self) -> bytes:
        if self.aborted:
            raise PrivateStoreError("client_disconnected")
        while not self.buffer:
            if self.done:
                return b""
            remaining = self.deadline - time.monotonic()
            if remaining <= 0:
                raise PrivateStoreError("request_timeout", 408)
            try:
                self.pending = asyncio.ensure_future(self.receive())
                message = await asyncio.wait_for(self.pending, timeout=remaining)
            except TimeoutError as exc:
                raise PrivateStoreError("request_timeout", 408) from exc
            finally:
                self.pending = None
            if message.get("type") == "http.disconnect":
                raise PrivateStoreError("client_disconnected")
            chunk = message.get("body", b"")
            if message.get("type") != "http.request" or not isinstance(chunk, bytes):
                raise PrivateStoreError("invalid_request")
            self.count += len(chunk)
            if self.count > self.cap:
                raise PrivateStoreError("request_too_large", 413)
            self.done = not message.get("more_body", False)
            self.buffer = memoryview(chunk)
        chunk = bytes(self.buffer[:_CHUNK_BYTES])
        self.buffer = self.buffer[_CHUNK_BYTES:]
        return chunk

    async def collect(self) -> bytes:
        result = bytearray()
        while chunk := await self.next():
            result.extend(chunk)
        return bytes(result)

    def iterate(self, loop: asyncio.AbstractEventLoop) -> Iterator[bytes]:
        # Called in the store worker. No receive is scheduled until the store
        # actually asks for a chunk, after its scope/manifest/digest checks.
        while True:
            future = asyncio.run_coroutine_threadsafe(self.next(), loop)
            try:
                chunk = future.result(timeout=max(0.0, self.deadline - time.monotonic()) + 1)
            except TimeoutError as exc:
                future.cancel()
                raise PrivateStoreError("request_timeout", 408) from exc
            if not chunk:
                return
            yield chunk


class ProjectService:
    """An application with a fixed credential snapshot and project-scoped store."""

    def __init__(self, store: PrivateStore, leaf: Any, verifier: Any, *, body_timeout: float, transfers: TransferLimits) -> None:
        self.store = store
        self._leaf = leaf
        self._verifier = verifier
        self.body_timeout = body_timeout
        self.transfers = transfers
        self._uploads = _Admission(transfers.uploads, transfers.project_uploads)
        self._downloads = _Admission(transfers.downloads, transfers.project_downloads)
        self._operations = _Admission(transfers.operations, transfers.project_operations)
        # Every store pool has more workers than admitted jobs. Store operations
        # never enter asyncio's default executor, including metadata and reads.
        self._upload_executor = ThreadPoolExecutor(max_workers=transfers.uploads + 2, thread_name_prefix="n4ds-upload")
        self._download_executor = ThreadPoolExecutor(max_workers=transfers.downloads + 2, thread_name_prefix="n4ds-download")
        self._store_executor = ThreadPoolExecutor(max_workers=transfers.operations + 2, thread_name_prefix="n4ds-store")

    def close(self) -> None:
        self._upload_executor.shutdown(wait=False, cancel_futures=True)
        self._download_executor.shutdown(wait=False, cancel_futures=True)
        self._store_executor.shutdown(wait=False, cancel_futures=True)

    @staticmethod
    async def _drain(future: asyncio.Future[Any]) -> None:
        # Repeated cancellation must not free admission while a thread is still
        # running; resets/shutdown cannot turn bounded work into detached work.
        while not future.done():
            with suppress(Exception, asyncio.CancelledError):
                await asyncio.shield(future)
        with suppress(Exception, asyncio.CancelledError):
            future.result()

    @staticmethod
    async def _run_transfer(executor: ThreadPoolExecutor, operation: Callable[..., Any], *args: Any) -> Any:
        future = asyncio.get_running_loop().run_in_executor(executor, operation, *args)
        try:
            return await asyncio.shield(future)
        except asyncio.CancelledError:
            # Retain admission and file ownership until the in-flight IO ends.
            await ProjectService._drain(future)
            raise

    async def _download(self, context: StoreContext, params: dict[str, str], send: Send) -> None:
        with self._downloads.reserve(context.project_id):
            deadline = time.monotonic() + self.transfers.send_timeout
            handle = _Download(self.store.open_file(context, params["record_id"], params["sha256"]))
            started = False
            cancelled = False

            async def timed_send(message: Message) -> None:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise TimeoutError("download deadline")
                await asyncio.wait_for(send(message), timeout=remaining)

            try:
                await self._run_transfer(self._download_executor, handle.open)
                if time.monotonic() >= deadline:
                    raise TimeoutError("download deadline")
                # Once start is attempted its completion is ambiguous on a
                # disconnected socket; never send a second start after failure.
                started = True
                await timed_send({"type": "http.response.start", "status": 200, "headers": [
                    (b"content-type", b"application/octet-stream"), (b"content-length", str(handle.size).encode("ascii")),
                    (b"cache-control", b"no-store"), (b"x-content-type-options", b"nosniff"),
                ]})
                while chunk := await self._run_transfer(self._download_executor, handle.read):
                    await timed_send({"type": "http.response.body", "body": chunk, "more_body": True})
                await timed_send({"type": "http.response.body", "body": b""})
            except asyncio.CancelledError:
                cancelled = True
                raise
            except Exception as exc:
                if started:
                    raise _ResponseStarted("download interrupted") from None
                if isinstance(exc, TimeoutError):
                    raise PrivateStoreError("request_timeout", 408) from None
                raise
            finally:
                # In-flight reads have been drained. Closing these read-only
                # handles needs no executor and must work after lifespan shutdown.
                # Cleanup must never turn cancellation into a new HTTP response.
                if cancelled:
                    with suppress(Exception):
                        handle.close()
                else:
                    with suppress(OSError):
                        handle.close()

    async def _respond(self, send: Send, status: int, value: Any) -> None:
        # Encode incrementally under a hard cap, never dump an unbounded list.
        encoded = bytearray()
        for part in json.JSONEncoder(ensure_ascii=False, allow_nan=False, separators=(",", ":")).iterencode(value):
            block = part.encode("utf-8")
            if len(encoded) + len(block) > self.transfers.json_bytes:
                if isinstance(value, dict) and value.get("status") in {"created", "already_present"} and isinstance(value.get("record"), dict):
                    # The write already succeeded. Return a bounded receipt,
                    # rather than misreporting its outcome as a failed intake.
                    receipt = {"status": value["status"], "record_id": value["record"]["record_id"]}
                    encoded = bytearray(json.dumps(receipt, separators=(",", ":")).encode("utf-8"))
                else:
                    status = 413
                    encoded = bytearray(b'{"error":"response_too_large"}')
                break
            encoded.extend(block)
        body = bytes(encoded)
        headers = [
            (b"content-type", b"application/json; charset=utf-8"),
            (b"content-length", str(len(body)).encode("ascii")),
            (b"cache-control", b"no-store"),
            (b"x-content-type-options", b"nosniff"),
        ]
        if status == 401:
            headers.append((b"www-authenticate", b"Bearer"))
        if status == 503:
            headers.append((b"retry-after", b"1"))
        deadline = time.monotonic() + self.transfers.send_timeout

        async def timed_send(message: Message) -> None:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError("JSON send deadline")
            await asyncio.wait_for(send(message), timeout=remaining)

        try:
            await timed_send({"type": "http.response.start", "status": status, "headers": headers})
            for start in range(0, len(body), _CHUNK_BYTES):
                await timed_send({"type": "http.response.body", "body": body[start:start + _CHUNK_BYTES], "more_body": True})
            await timed_send({"type": "http.response.body", "body": b""})
        except (TimeoutError, OSError):
            raise _ResponseStarted("JSON response interrupted") from None

    @staticmethod
    def _headers(scope: Scope) -> dict[bytes, list[bytes]]:
        headers: dict[bytes, list[bytes]] = {}
        for name, value in scope.get("headers", []):
            headers.setdefault(name.lower(), []).append(value)
        return headers

    @staticmethod
    def _request_headers(scope: Scope, headers: dict[bytes, list[bytes]], cap: int) -> None:
        # No query credentials, project selectors, compression, or ambiguous
        # lengths. Content-Length is only an early check, never the byte counter.
        if scope.get("query_string") or any(name.startswith(b"x-") and b"project" in name for name in headers):
            raise PrivateStoreError("invalid_request")
        if headers.get(b"content-encoding", [b"identity"]) != [b"identity"]:
            raise PrivateStoreError("unsupported_media_type", 415)
        lengths = headers.get(b"content-length", [])
        if len(lengths) > 1 or lengths and re.fullmatch(rb"[0-9]{1,20}", lengths[0]) is None:
            raise PrivateStoreError("invalid_request")
        if lengths and int(lengths[0]) > cap:
            raise PrivateStoreError("request_too_large", 413)

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] == "lifespan":
            while True:
                message = await receive()
                if message["type"] == "lifespan.startup":
                    await send({"type": "lifespan.startup.complete"})
                elif message["type"] == "lifespan.shutdown":
                    self.close()
                    await send({"type": "lifespan.shutdown.complete"})
                    return
        if scope["type"] == "websocket":
            await send({"type": "websocket.close", "code": 1008})
            return
        if scope["type"] != "http":
            return
        response = _Response(send)
        send = response.send
        method, path = scope.get("method", ""), scope.get("path", "")
        if method == "GET" and path == "/healthz" and not scope.get("query_string"):
            await self._respond(send, 200, {"status": "ok"})
            return
        route = None
        params: dict[str, str] = {}
        for candidate in ROUTES:
            match = re.fullmatch(candidate.pattern, path)
            if candidate.method == method and match is not None:
                route, params = candidate, match.groupdict()
                break
        headers = self._headers(scope)
        authorizations = headers.get(b"authorization", [])
        authorization = authorizations[0].decode("latin-1") if len(authorizations) == 1 else None
        try:
            principal = self._verifier.verify(self._leaf.parse_bearer(authorization), service="datasets", required_rights=[route.right] if route else [])
        except self._leaf.AccessError as exc:
            # AccessError.detail includes principal identifiers. Expose codes only.
            await self._respond(send, exc.status, {"error": exc.code})
            return
        if route is None:
            await self._respond(send, 404, {"error": "not_found"})
            return
        context = StoreContext(principal.project_id, principal.principal_id)
        try:
            with self._operations.reserve(context.project_id):
                await self._authorized(route, params, principal, context, scope, headers, receive, response)
                return
        except _ResponseStarted:
            raise
        except PrivateStoreError as exc:
            status, result = exc.status, {"error": exc.code}
        except OSError as exc:
            full = exc.errno in (errno.ENOSPC, errno.EDQUOT)
            status, result = 507 if full else 500, {"error": "insufficient_storage" if full else "storage_failure"}
        except Exception:
            status, result = 500, {"error": "internal_error"}
        if response.started:
            raise _ResponseStarted("response interrupted") from None
        await self._respond(send, status, result)

    async def _authorized(self, route: Route, params: dict[str, str], principal: Any, context: StoreContext, scope: Scope, headers: dict[bytes, list[bytes]], receive: Receive, response: _Response) -> None:
        send = response.send
        try:
            if route.operation == "read_file":
                self._request_headers(scope, headers, 0)
                await self._download(context, params, send)
                return
            status, result = await self._dispatch(route.operation, params, context, scope, headers, receive)
            if "datasets.read" not in principal.rights and "record" in result:
                result = {"status": result["status"], "record_id": result["record"]["record_id"]}
        except _ResponseStarted:
            raise
        except PrivateStoreError as exc:
            status, result = exc.status, {"error": exc.code}
        except OSError as exc:
            full = exc.errno in (errno.ENOSPC, errno.EDQUOT)
            status, result = 507 if full else 500, {"error": "insufficient_storage" if full else "storage_failure"}
        except Exception:
            # Neither paths, credential details nor internal tracebacks are HTTP data.
            status, result = 500, {"error": "internal_error"}
        if response.started:
            raise _ResponseStarted("response interrupted") from None
        # A disconnected send must never be retried as a second response start.
        # Keep operation admission while sending JSON: slow readers cannot
        # release slots and accumulate response buffers without bound.
        await self._respond(send, status, result)

    async def _dispatch(self, operation: str, params: dict[str, str], context: StoreContext, scope: Scope, headers: dict[bytes, list[bytes]], receive: Receive) -> tuple[int, Any]:
        cap = self.store.limits.max_file_bytes if operation == "put_file" else self.store.limits.max_manifest_bytes if operation == "begin" else 0
        self._request_headers(scope, headers, cap)
        body = _Body(receive, cap, self.body_timeout)
        if operation == "begin":
            content_type = headers.get(b"content-type", [])
            if len(content_type) != 1 or content_type[0].split(b";", 1)[0].strip().lower() != b"application/json":
                raise PrivateStoreError("unsupported_media_type", 415)
            manifest = await body.collect()
            result = await self._run_transfer(self._store_executor, self.store.begin, context, manifest)
        elif operation == "put_file":
            with self._uploads.reserve(context.project_id):
                worker = asyncio.get_running_loop().run_in_executor(self._upload_executor, self.store.put_file, context, params["submission_id"], params["sha256"], body.iterate(asyncio.get_running_loop()))
                try:
                    result = await asyncio.shield(worker)
                except asyncio.CancelledError:
                    body.abort()
                    await self._drain(worker)
                    raise
        elif operation == "commit":
            await body.collect()
            result = await self._run_transfer(self._store_executor, self.store.commit, context, params["submission_id"])
        elif operation == "list_records":
            operation_call = partial(self.store.list_records, context, max_metadata_bytes=self.transfers.json_bytes - 32, max_records=self.transfers.list_records)
            result = {"records": await self._run_transfer(self._store_executor, operation_call)}
        elif operation == "get_record":
            result = await self._run_transfer(self._store_executor, partial(self.store.get_record, context, params["record_id"], max_metadata_bytes=self.transfers.json_bytes))
        else:
            raise PrivateStoreError("not_found", 404)
        status = 202 if result.get("status") == "pending" else 201 if result.get("status") == "created" else 200
        return status, result


def create_app(*, store: str | Path, credential_store: str | Path, host: str = "127.0.0.1", tls: bool = False, trusted_proxy: bool = False,
               limits: StoreLimits | None = None, body_timeout: float = 30.0, transfers: TransferLimits | None = None) -> ProjectService:
    """Load a credential snapshot; reject insecure or unusable configurations."""
    try:
        leaf = import_module("nirs4all_access")
    except ImportError as exc:
        raise ServiceConfigurationError("project-service dependencies are unavailable") from exc
    try:
        leaf.require_secure_transport(host, tls=tls, trusted_proxy=trusted_proxy)
        if type(body_timeout) not in (int, float) or not math.isfinite(body_timeout) or body_timeout <= 0:
            raise ServiceConfigurationError("invalid body timeout")
        records = leaf.load_credential_store(credential_store)
        now = time.time()
        if not any(not r.revoked and (r.expires_at is None or r.expires_at > now) and "datasets" in r.principal.services
                   and r.principal.rights.intersection({"datasets.read", "datasets.add"}) for r in records):
            raise ServiceConfigurationError("no active datasets credentials")
        verifier = leaf.ProjectTokenVerifier(records)
        private_store = PrivateStore(store, limits=limits)
    except ServiceConfigurationError:
        raise
    except (OSError, ValueError, leaf.CredentialStoreError, PrivateStoreError) as exc:
        raise ServiceConfigurationError("invalid project-service configuration") from exc
    return ProjectService(private_store, leaf, verifier, body_timeout=body_timeout, transfers=transfers or TransferLimits())


def main(argv: list[str] | None = None) -> None:
    """Run an explicitly configured local service; never provision hosting."""
    parser = argparse.ArgumentParser(prog="n4a-datasets-project")
    commands = parser.add_subparsers(dest="command", required=True)
    serve = commands.add_parser("serve", help="Serve the private project store on loopback")
    serve.add_argument("--store", required=True, type=Path)
    serve.add_argument("--credentials", required=True, type=Path)
    serve.add_argument("--host", choices=("127.0.0.1", "::1", "localhost"), default="127.0.0.1")
    serve.add_argument("--port", type=int, default=8046)
    serve.add_argument("--body-timeout", type=float, default=30.0)
    serve.add_argument("--max-file-bytes", type=int, default=StoreLimits.max_file_bytes)
    serve.add_argument("--max-manifest-bytes", type=int, default=StoreLimits.max_manifest_bytes)
    serve.add_argument("--upload-limit", type=int, default=TransferLimits.uploads)
    serve.add_argument("--project-upload-limit", type=int, default=TransferLimits.project_uploads)
    serve.add_argument("--download-limit", type=int, default=TransferLimits.downloads)
    serve.add_argument("--project-download-limit", type=int, default=TransferLimits.project_downloads)
    serve.add_argument("--send-timeout", type=float, default=TransferLimits.send_timeout)
    serve.add_argument("--operation-limit", type=int, default=TransferLimits.operations)
    serve.add_argument("--project-operation-limit", type=int, default=TransferLimits.project_operations)
    serve.add_argument("--max-json-bytes", type=int, default=TransferLimits.json_bytes)
    serve.add_argument("--max-list-records", type=int, default=TransferLimits.list_records)
    serve.add_argument("--shutdown-timeout", type=float, default=TransferLimits.shutdown_timeout)
    args = parser.parse_args(argv)
    try:
        if not 0 <= args.port <= 65535:
            raise ServiceConfigurationError("invalid port")
        limits = StoreLimits(max_file_bytes=args.max_file_bytes, max_manifest_bytes=args.max_manifest_bytes)
        transfers = TransferLimits(args.upload_limit, args.project_upload_limit, args.download_limit, args.project_download_limit, args.send_timeout,
                                   args.operation_limit, args.project_operation_limit, args.max_json_bytes, args.max_list_records, args.shutdown_timeout)
        app = create_app(store=args.store, credential_store=args.credentials, host=args.host, limits=limits, body_timeout=args.body_timeout, transfers=transfers)
        uvicorn = import_module("uvicorn")
    except (ServiceConfigurationError, ValueError, ImportError):
        parser.exit(2, "Unable to start project service: check dependencies and configuration.\n")
    # Suppress protocol logging before Uvicorn constructs any connection handler.
    # Request rejection inside ASGI cannot sanitize pre-app HTTP/WS query logs.
    quiet_logs = {"version": 1, "disable_existing_loggers": False, "handlers": {"null": {"class": "logging.NullHandler"}},
                  "loggers": {name: {"handlers": ["null"], "propagate": False, "level": "CRITICAL"}
                              for name in ("uvicorn", "uvicorn.error", "uvicorn.access", "uvicorn.asgi")}}
    try:
        uvicorn.run(app, host=args.host, port=args.port, access_log=False, log_config=quiet_logs, log_level="critical", proxy_headers=False, server_header=False,
                    loop="asyncio", http="h11", ws="none", timeout_graceful_shutdown=transfers.shutdown_timeout)
    except SystemExit as exc:
        if exc.code not in (None, 0):
            parser.exit(1, "Unable to start project service.\n")
        raise
    except (OSError, RuntimeError, ValueError):
        parser.exit(1, "Unable to start project service.\n")


if __name__ == "__main__":
    main()
