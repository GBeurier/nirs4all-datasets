"""Offline, project-isolated storage of asserted descriptors and opaque private bytes.

This module does not authenticate callers. The local operator supplies a trusted
context; a future authenticated service must construct it after authorization.
Origin metadata is inert. Hashes establish submitted byte integrity only.
"""
from __future__ import annotations

import errno
import hashlib
import json
import os
import re
import stat
import unicodedata
import uuid
from collections.abc import Iterable, Iterator, Mapping
from contextlib import ExitStack, contextmanager, suppress
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, BinaryIO, Literal

from filelock import FileLock, Timeout
from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from nirs4all_datasets.schema import DatasetDescriptor

if os.name == "posix":
    import fcntl

DISK_FLOOR_BYTES = 2_147_483_648
_EVIDENCE = {"provenance_status": "asserted_unverified", "rights_status": "asserted_unverified", "content_validated": "hash_only"}
_FETCH_KEYS = {"fetch", "mirror", "source_url", "download_url", "locator"}
_OWNED_KEYS = {"project_id", "principal_id", "submitted_at", "record_id", "submission_id", *_EVIDENCE}
_DEVICE = re.compile(r"(?:con|prn|aux|nul|com[1-9¹²³]|lpt[1-9¹²³])(?:\..*)?", re.IGNORECASE)


class PrivateStoreError(Exception):
    """A stable refusal code and the status intended for a future transport."""

    def __init__(self, code: str, status: int = 400) -> None:
        self.code = code
        self.status = status
        super().__init__(code)


class _ProjectLock(FileLock):
    """FileLock with descriptor-relative, no-follow lock-file acquisition."""

    def __init__(self, directory: int) -> None:
        super().__init__(".lock", timeout=30)
        self.directory = directory

    def _acquire(self) -> None:
        try:
            fd = os.open(".lock", os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW | os.O_NONBLOCK, 0o600, dir_fd=self.directory)
        except OSError as exc:
            if exc.errno == errno.ELOOP:
                raise PrivateStoreError("symlink_refused") from exc
            raise
        try:
            info = os.fstat(fd)
            if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
                raise PrivateStoreError("unsafe_store_file")
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            os.close(fd)
        except BaseException:
            os.close(fd)
            raise
        else:
            self._context.lock_file_fd = fd

    def _release(self) -> None:
        fd = self._context.lock_file_fd
        self._context.lock_file_fd = None
        if fd is not None:
            try:
                fcntl.flock(fd, fcntl.LOCK_UN)
            finally:
                os.close(fd)


@dataclass(frozen=True)
class _Staged:
    parts: tuple[str, ...]
    directory: int
    file: int
    name: str


def _canonical(value: Any) -> bytes:
    """Canonical JSON for this contract (UTF-8, sorted keys, no whitespace/NaN)."""
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")


def _json_types(value: Any) -> None:
    if type(value) is dict:
        for key, item in value.items():
            if type(key) is not str:
                raise PrivateStoreError("invalid_manifest")
            _json_types(item)
    elif type(value) is list:
        for item in value:
            _json_types(item)
    elif value is not None and type(value) not in (str, int, float, bool):
        raise PrivateStoreError("invalid_manifest")


def _pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise PrivateStoreError("invalid_manifest")
        result[key] = value
    return result


def _decode(data: bytes) -> Any:
    try:
        value = json.loads(data.decode("utf-8"), object_pairs_hook=_pairs)
        _json_types(value)
        _canonical(value)
        return value
    except (ValueError, TypeError, UnicodeError, RecursionError) as exc:
        raise PrivateStoreError("invalid_manifest") from exc


def _digest(value: str) -> str:
    if not isinstance(value, str) or re.fullmatch(r"[0-9a-f]{64}", value) is None:
        raise PrivateStoreError("invalid_digest")
    return value


def _filename(value: str) -> None:
    if not value or any(unicodedata.category(c).startswith("C") for c in value) or "\\" in value or ":" in value:
        raise PrivateStoreError("invalid_filename")
    for part in value.split("/"):
        if part in ("", ".", "..") or part.endswith((".", " ")) or _DEVICE.fullmatch(part) or any(c in part for c in '<>"|?*'):
            raise PrivateStoreError("invalid_filename")


def _refuse_keys(value: Mapping[str, Any], *, locator: bool = True) -> None:
    if _OWNED_KEYS.intersection(value) or "generation" in value:
        raise PrivateStoreError("server_owned_field")
    if (_FETCH_KEYS if locator else _FETCH_KEYS - {"locator"}).intersection(value):
        raise PrivateStoreError("fetch_or_mirror_refused")


class PrivateFile(BaseModel):
    """A declared opaque file; its path is metadata and is never opened."""

    model_config = ConfigDict(extra="forbid", strict=True, frozen=True)

    path: str
    sha256: str
    size: int = Field(ge=0)
    byte_source: Literal["user_provided", "unknown"]
    note: str | None = None

    @model_validator(mode="before")
    @classmethod
    def _declarations(cls, value: Any) -> Any:
        if isinstance(value, dict):
            _refuse_keys(value)
            if "byte_source" not in value:
                raise PrivateStoreError("byte_source_required")
            if value["byte_source"] == "public_origin_download":
                raise PrivateStoreError("public_origin_download_refused")
        return value

    @model_validator(mode="after")
    def _integrity(self) -> PrivateFile:
        _digest(self.sha256)
        _filename(self.path)
        return self


class PrivateSubmission(BaseModel):
    """Separate envelope; descriptor validation never persists model defaults.

    Use :meth:`parse` for stable refusal codes and strict JSON validation.
    File order is part of identity; JSON object key order is not.
    """

    model_config = ConfigDict(extra="forbid", strict=True, frozen=True)

    descriptor: dict[str, Any]
    files: list[PrivateFile]

    @model_validator(mode="before")
    @classmethod
    def _assertions(cls, value: Any) -> Any:
        if isinstance(value, dict):
            _refuse_keys(value)
            desc = value.get("descriptor")
            if isinstance(desc, dict):
                _refuse_keys(desc, locator=False)
                origins = desc.get("origin_sources", [])
                if isinstance(origins, list):
                    for origin in origins:
                        if isinstance(origin, dict) and {"alive", "last_checked"}.intersection(origin):
                            raise PrivateStoreError("server_owned_field")
                # Validate, then discard the model. The caller's JSON is the record.
                DatasetDescriptor.model_validate(desc)
        return value

    @model_validator(mode="after")
    def _files(self) -> PrivateSubmission:
        names = [unicodedata.normalize("NFC", item.path).casefold() for item in self.files]
        if len(names) != len(set(names)):
            raise PrivateStoreError("filename_conflict")
        sizes: dict[str, int] = {}
        for item in self.files:
            if item.sha256 in sizes and sizes[item.sha256] != item.size:
                raise PrivateStoreError("digest_size_conflict")
            sizes[item.sha256] = item.size
        if self.files and self.descriptor.get("tier", "private") != "private":
            raise PrivateStoreError("tier_unsupported_for_bytes")
        return self

    @classmethod
    def parse(cls, value: Mapping[str, Any] | bytes | PrivateSubmission) -> PrivateSubmission:
        try:
            if isinstance(value, cls):
                value = value.model_dump(exclude_unset=True)
            if not isinstance(value, bytes):
                _json_types(value)
                value = _canonical(value)
            return cls.model_validate(_decode(value))
        except ValidationError as exc:
            code = "unknown_field" if any(e["type"] == "extra_forbidden" for e in exc.errors()) else "invalid_manifest"
            raise PrivateStoreError(code) from exc
        except (TypeError, ValueError, UnicodeError, RecursionError) as exc:
            raise PrivateStoreError("invalid_manifest") from exc

    def canonical_json(self) -> bytes:
        return _canonical(self.model_dump(exclude_unset=True))

    @property
    def record_id(self) -> str:
        return hashlib.sha256(self.canonical_json()).hexdigest()

    @property
    def identity(self) -> bytes:
        # An undeclared content version is its own identity, never an injected 1.0.0.
        return _canonical([self.descriptor["id"], self.descriptor.get("versions", {}).get("content")])


@dataclass(frozen=True)
class StoreContext:
    """Operator-supplied identity, never taken from the submission envelope.

    This is a trust boundary, not an authentication or authorization mechanism.
    """

    project_id: str
    principal_id: str

    def __post_init__(self) -> None:
        for value in (self.project_id, self.principal_id):
            if not isinstance(value, str) or not value.strip() or len(value) > 1024 or any(unicodedata.category(c).startswith("C") for c in value):
                raise PrivateStoreError("invalid_context")


@dataclass(frozen=True)
class StoreLimits:
    """Positive limits; the disk floor cannot be reduced below 2 GiB."""

    max_manifest_bytes: int = 1_048_576
    max_file_bytes: int = 67_108_864
    max_submission_bytes: int = 268_435_456
    max_files: int = 128
    disk_floor_bytes: int = DISK_FLOOR_BYTES

    def __post_init__(self) -> None:
        if any(type(v) is not int or v <= 0 for v in vars(self).values()) or self.disk_floor_bytes < DISK_FLOOR_BYTES:
            raise ValueError("limits must be positive and the disk floor at least 2147483648 bytes")


class PrivateStore:
    """Manifest-first offline store with immutable records and per-project locks.

    ``root`` must be explicit, absolute, outside Git/catalog/datasets, and owned
    by the operator. POSIX descriptor-relative no-follow IO is required. Merely
    constructing or reading a store never creates directories or lock files.
    """

    def __init__(self, root: str | Path, *, limits: StoreLimits | None = None) -> None:
        if os.name != "posix" or not hasattr(os, "O_NOFOLLOW"):
            raise PrivateStoreError("platform_unsupported")
        self.root = Path(root)
        self.limits = limits or StoreLimits()
        self._validate_root()
        try:
            with self._directory(("projects",)):
                pass
        except FileNotFoundError:
            pass

    def _validate_root(self) -> None:
        if not self.root.is_absolute() or ".." in self.root.parts or any(p.casefold() in {"catalog", "datasets", ".git"} for p in self.root.parts):
            raise PrivateStoreError("unsafe_store_root")
        for path in (*reversed(self.root.parents), self.root):
            try:
                info = path.lstat()
            except FileNotFoundError:
                continue
            if stat.S_ISLNK(info.st_mode):
                raise PrivateStoreError("symlink_refused")
            if not stat.S_ISDIR(info.st_mode) or os.path.lexists(path / ".git"):
                raise PrivateStoreError("unsafe_store_root")
            if path == self.root and info.st_mode & 0o022:
                raise PrivateStoreError("unsafe_store_root")

    @contextmanager
    def _directory(self, parts: tuple[str, ...], *, create: bool = False) -> Iterator[int]:
        """Anchor every component at an open directory; never follow symlinks."""
        self._validate_root()
        fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
        try:
            for part in (*self.root.parts[1:], *parts):
                try:
                    try:
                        new_fd = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
                    except FileNotFoundError:
                        if not create:
                            raise
                        self._disk(fd, 4096)
                        try:
                            os.mkdir(part, mode=0o700, dir_fd=fd)
                            os.fsync(fd)
                        except FileExistsError:
                            pass
                        new_fd = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
                except OSError as exc:
                    if exc.errno in (errno.ELOOP, errno.ENOTDIR):
                        raise PrivateStoreError("symlink_or_path_refused") from exc
                    raise
                os.close(fd)
                fd = new_fd
            yield fd
        except OSError as exc:
            if exc.errno in (errno.ENOSPC, errno.EDQUOT):
                raise PrivateStoreError("insufficient_storage", 507) from exc
            raise
        finally:
            os.close(fd)

    @staticmethod
    def _project(context: StoreContext) -> tuple[str, ...]:
        if not isinstance(context, StoreContext):
            raise PrivateStoreError("invalid_context")
        return ("projects", hashlib.sha256(context.project_id.encode("utf-8")).hexdigest())

    def _disk(self, fd: int, needed: int = 0) -> None:
        usage = os.fstatvfs(fd)
        if usage.f_bavail * usage.f_frsize - needed < self.limits.disk_floor_bytes:
            raise PrivateStoreError("insufficient_storage", 507)

    @staticmethod
    def _open(fd: int, name: str) -> int:
        try:
            result = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=fd)
        except OSError as exc:
            if exc.errno == errno.ELOOP:
                raise PrivateStoreError("symlink_refused") from exc
            raise
        info = os.fstat(result)
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
            os.close(result)
            raise PrivateStoreError("unsafe_store_file")
        return result

    def _tree(self, fd: int, *, clean: bool = False) -> int:
        """Reject unsafe entries, optionally reclaim only our orphan temp names."""
        removed = 0
        with os.scandir(fd) as entries:
            for entry in entries:
                try:
                    info = entry.stat(follow_symlinks=False)
                except FileNotFoundError:
                    # Another project may have just completed an atomic write.
                    continue
                if stat.S_ISLNK(info.st_mode):
                    raise PrivateStoreError("symlink_refused")
                if stat.S_ISDIR(info.st_mode):
                    try:
                        child = os.open(entry.name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
                    except FileNotFoundError:
                        continue
                    try:
                        removed += self._tree(child, clean=clean)
                    finally:
                        os.close(child)
                elif not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
                    raise PrivateStoreError("unsafe_store_file")
                elif clean and re.fullmatch(r"\.tmp-[0-9a-f]{32}", entry.name):
                    try:
                        temporary = self._open(fd, entry.name)
                    except FileNotFoundError:
                        continue
                    try:
                        try:
                            fcntl.flock(temporary, fcntl.LOCK_EX | fcntl.LOCK_NB)
                        except BlockingIOError:
                            # A live upload owns this file, not the project lock.
                            continue
                        os.unlink(entry.name, dir_fd=fd)
                        removed += 1
                    finally:
                        os.close(temporary)
        if removed:
            os.fsync(fd)
        return removed

    @contextmanager
    def _write_project(self, context: StoreContext) -> Iterator[int]:
        # Check floor before even creating the root. Existing ancestors suffice.
        self._validate_root()
        ancestor = self.root
        while not ancestor.exists():
            ancestor = ancestor.parent
        ancestor_fd = os.open(ancestor, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        try:
            self._disk(ancestor_fd)
        finally:
            os.close(ancestor_fd)
        parts = self._project(context)
        with self._directory(parts, create=True) as fd:
            try:
                with _ProjectLock(fd):
                    self._same_directory(parts, fd)
                    self._tree(fd, clean=True)
                    self._disk(fd)
                    yield fd
            except Timeout as exc:
                raise PrivateStoreError("store_busy", 503) from exc

    def _same_directory(self, parts: tuple[str, ...], fd: int) -> None:
        with self._directory(parts) as current:
            left, right = os.fstat(fd), os.fstat(current)
            if (left.st_dev, left.st_ino) != (right.st_dev, right.st_ino):
                raise PrivateStoreError("store_path_changed", 409)

    def _manifest(self, value: Mapping[str, Any] | bytes | PrivateSubmission) -> PrivateSubmission:
        if isinstance(value, bytes) and len(value) > self.limits.max_manifest_bytes:
            raise PrivateStoreError("request_too_large", 413)
        submission = PrivateSubmission.parse(value)
        if len(submission.canonical_json()) > self.limits.max_manifest_bytes or len(submission.files) > self.limits.max_files:
            raise PrivateStoreError("request_too_large", 413)
        if any(f.size > self.limits.max_file_bytes for f in submission.files) or sum(f.size for f in submission.files) > self.limits.max_submission_bytes:
            raise PrivateStoreError("request_too_large", 413)
        return submission

    def _read_json(self, parts: tuple[str, ...], name: str, *, max_bytes: int | None = None) -> dict[str, Any]:
        with self._directory(parts) as directory, os.fdopen(self._open(directory, name), "rb") as stream:
            # Stored integrity is independent of today's intake limits.
            if max_bytes is not None and os.fstat(stream.fileno()).st_size > max_bytes:
                raise PrivateStoreError("response_too_large", 413)
            data = stream.read() if max_bytes is None else stream.read(max_bytes + 1)
            if max_bytes is not None and len(data) > max_bytes:
                raise PrivateStoreError("response_too_large", 413)
        try:
            value = _decode(data)
        except PrivateStoreError as exc:
            raise PrivateStoreError("corrupt_record", 409) from exc
        if not isinstance(value, dict):
            raise PrivateStoreError("corrupt_record", 409)
        return value

    @contextmanager
    def _temporary(self, parts: tuple[str, ...]) -> Iterator[_Staged]:
        """Create and lease a temp inode while the caller holds the project lock."""
        with self._directory(parts, create=True) as directory:
            temporary = ".tmp-" + uuid.uuid4().hex
            fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=directory)
            try:
                fcntl.flock(fd, fcntl.LOCK_EX)
                yield _Staged(parts, directory, fd, temporary)
            finally:
                try:
                    with suppress(FileNotFoundError):
                        os.unlink(temporary, dir_fd=directory)
                finally:
                    os.close(fd)

    def _receive(self, staged: _Staged, chunks: Iterable[bytes], *, expected: PrivateFile | None = None) -> None:
        """Stream outside the project lock into an already leased inode."""
        count = 0
        digest = hashlib.sha256()
        for chunk in chunks:
            if not isinstance(chunk, bytes):
                raise PrivateStoreError("invalid_chunk")
            count += len(chunk)
            if expected is not None:
                if count > self.limits.max_file_bytes:
                    raise PrivateStoreError("request_too_large", 413)
                if count > expected.size:
                    raise PrivateStoreError("size_mismatch")
            self._disk(staged.directory, len(chunk))
            view = memoryview(chunk)
            while view:
                written = os.write(staged.file, view)
                if written <= 0:
                    raise OSError(errno.ENOSPC, "short write")
                view = view[written:]
            digest.update(chunk)
        if expected is not None:
            if count != expected.size:
                raise PrivateStoreError("size_mismatch")
            if digest.hexdigest() != expected.sha256:
                raise PrivateStoreError("digest_mismatch")
        os.fsync(staged.file)

    def _publish(self, staged: _Staged, name: str, *, expected: PrivateFile | None = None) -> None:
        self._same_directory(staged.parts, staged.directory)
        # Never publish a replacement path in place of the leased inode.
        with os.fdopen(self._open(staged.directory, staged.name), "rb") as stream:
            left, right = os.fstat(staged.file), os.fstat(stream.fileno())
            if (left.st_dev, left.st_ino) != (right.st_dev, right.st_ino):
                raise PrivateStoreError("store_path_changed", 409)
            if expected is not None:
                digest = hashlib.sha256()
                count = 0
                while chunk := stream.read(65_536):
                    count += len(chunk)
                    digest.update(chunk)
                if count != expected.size or digest.hexdigest() != expected.sha256:
                    raise PrivateStoreError("corrupt_record", 409)
        self._tree(staged.directory)
        if expected is None or name not in os.listdir(staged.directory):
            os.replace(staged.name, name, src_dir_fd=staged.directory, dst_dir_fd=staged.directory)
        os.fsync(staged.directory)

    def _atomic(self, parts: tuple[str, ...], name: str, chunks: Iterable[bytes]) -> None:
        with self._temporary(parts) as staged:
            self._receive(staged, chunks)
            self._publish(staged, name)

    def _names(self, parts: tuple[str, ...], *, limit: int | None = None) -> list[str]:
        try:
            with self._directory(parts) as fd:
                if limit is not None:
                    names = []
                    with os.scandir(fd) as entries:
                        for entry in entries:
                            if re.fullmatch(r"\.tmp-[0-9a-f]{32}", entry.name) is None:
                                names.append(entry.name)
                                if len(names) > limit:
                                    raise PrivateStoreError("response_too_large", 413)
                    self._tree(fd)
                    return sorted(names)
                self._tree(fd)
                return sorted(name for name in os.listdir(fd) if re.fullmatch(r"\.tmp-[0-9a-f]{32}", name) is None)
        except FileNotFoundError:
            return []

    def _stored_submission(self, value: dict[str, Any], context: StoreContext, *, pending: bool) -> PrivateSubmission:
        keys = {"descriptor", "files", "record_id", "project_id", "principal_id", "submitted_at", *_EVIDENCE}
        if pending:
            keys.add("submission_id")
        try:
            if set(value) != keys or value["project_id"] != context.project_id or any(value[k] != v for k, v in _EVIDENCE.items()):
                raise ValueError
            StoreContext(value["project_id"], value["principal_id"])
            datetime.fromisoformat(value["submitted_at"])
            descriptor, files = value["descriptor"], value["files"]
            if type(descriptor) is not dict or type(descriptor.get("id")) is not str or not descriptor["id"] or type(files) is not list:
                raise ValueError
            versions = descriptor.get("versions", {})
            if type(versions) is not dict or "content" in versions and type(versions["content"]) is not str:
                raise ValueError
            stored_files = []
            sizes: dict[str, int] = {}
            for item in files:
                if type(item) is not dict or set(item) - {"path", "sha256", "size", "byte_source", "note"} or not {"path", "sha256", "size", "byte_source"} <= set(item):
                    raise ValueError
                if type(item["path"]) is not str or not item["path"] or type(item["size"]) is not int or item["size"] < 0:
                    raise ValueError
                digest = _digest(item["sha256"])
                if item["byte_source"] not in ("user_provided", "unknown") or item.get("note") is not None and type(item["note"]) is not str:
                    raise ValueError
                if digest in sizes and sizes[digest] != item["size"]:
                    raise ValueError
                sizes[digest] = item["size"]
                stored_files.append(PrivateFile.model_construct(_fields_set=set(item), **item))
            # Intake schema/defaults/limits are deliberately not run on old data.
            submission = PrivateSubmission.model_construct(descriptor=descriptor, files=stored_files)
            if submission.record_id != value["record_id"]:
                raise ValueError
            if pending:
                self._submission_id(value["submission_id"])
            return submission
        except (ValueError, TypeError, KeyError, PrivateStoreError) as exc:
            raise PrivateStoreError("corrupt_record", 409) from exc

    def _match(self, context: StoreContext, submission: PrivateSubmission) -> tuple[dict[str, Any] | None, bool]:
        project = self._project(context)
        match = None
        for name in self._names((*project, "records")):
            value = self._read_json((*project, "records"), name)
            other = self._stored_submission(value, context, pending=False)
            if name != other.record_id + ".json":
                raise PrivateStoreError("corrupt_record", 409)
            if other.identity == submission.identity and other.record_id != submission.record_id:
                raise PrivateStoreError("record_id_conflict", 409)
            if other.record_id == submission.record_id:
                match = value
        if match is not None:
            return match, False
        # Only the index for this exact content is read; unrelated broken pending
        # JSON cannot wedge a project or reserve an unpublished identity.
        try:
            index = self._read_json((*project, "pending_index"), submission.record_id + ".json")
        except FileNotFoundError:
            return None, False
        try:
            if set(index) != {"submission_id"}:
                raise ValueError
            value = self._pending(context, index["submission_id"])
            if value["record_id"] != submission.record_id:
                raise ValueError
        except (KeyError, ValueError, PrivateStoreError) as exc:
            raise PrivateStoreError("corrupt_record", 409) from exc
        return value, True

    @staticmethod
    def _submission_id(value: str) -> str:
        if not isinstance(value, str) or re.fullmatch(r"[0-9a-f]{32}", value) is None:
            raise PrivateStoreError("not_found", 404)
        return value

    def _pending(self, context: StoreContext, submission_id: str) -> dict[str, Any]:
        self._submission_id(submission_id)
        try:
            value = self._read_json((*self._project(context), "pending"), submission_id + ".json")
        except FileNotFoundError as exc:
            raise PrivateStoreError("not_found", 404) from exc
        self._stored_submission(value, context, pending=True)
        if value["submission_id"] != submission_id:
            raise PrivateStoreError("corrupt_record", 409)
        return value

    def _blob(self, context: StoreContext, file: PrivateFile, *, collect: bool = False, size_error: str = "corrupt_record") -> bytes:
        parts = (*self._project(context), "blobs", "sha256", file.sha256[:2])
        digest = hashlib.sha256()
        count = 0
        result = bytearray()
        try:
            with self._directory(parts) as directory, os.fdopen(self._open(directory, file.sha256), "rb") as stream:
                while chunk := stream.read(65_536):
                    count += len(chunk)
                    if count > file.size and size_error == "corrupt_record":
                        raise PrivateStoreError("corrupt_record", 409)
                    digest.update(chunk)
                    if collect:
                        result.extend(chunk)
        except FileNotFoundError as exc:
            raise PrivateStoreError("missing_blob", 409) from exc
        if digest.hexdigest() != file.sha256:
            raise PrivateStoreError("corrupt_record", 409)
        if count != file.size:
            raise PrivateStoreError(size_error, 400 if size_error == "size_mismatch" else 409)
        return bytes(result)

    def _verify(self, context: StoreContext, value: dict[str, Any], *, pending: bool) -> None:
        submission = self._stored_submission(value, context, pending=pending)
        checked = set()
        for file in submission.files:
            if file.sha256 in checked:
                continue
            checked.add(file.sha256)
            try:
                self._blob(context, file, size_error="size_mismatch" if pending else "corrupt_record")
            except PrivateStoreError as exc:
                if exc.code == "missing_blob" and not pending:
                    raise PrivateStoreError("corrupt_record", 409) from exc
                raise

    def begin(self, context: StoreContext, manifest: Mapping[str, Any] | bytes | PrivateSubmission) -> dict[str, Any]:
        """Refuse the manifest before writing anything; commit metadata immediately."""
        self._project(context)
        submission = self._manifest(manifest)
        with self._write_project(context):
            found, pending = self._match(context, submission)
            if found is not None:
                if not pending:
                    self._verify(context, found, pending=False)
                    return {"status": "already_present", "record": found}
                return {"status": "pending", "submission_id": found["submission_id"], "record_id": submission.record_id}
            value = {**json.loads(submission.canonical_json()), **_EVIDENCE, "record_id": submission.record_id,
                     "project_id": context.project_id, "principal_id": context.principal_id, "submitted_at": datetime.now(UTC).isoformat()}
            project = self._project(context)
            if not submission.files:
                self._atomic((*project, "records"), submission.record_id + ".json", [_canonical(value)])
                return {"status": "created", "record": value}
            submission_id = uuid.uuid4().hex
            value["submission_id"] = submission_id
            self._atomic((*project, "pending"), submission_id + ".json", [_canonical(value)])
            self._atomic((*project, "pending_index"), submission.record_id + ".json", [_canonical({"submission_id": submission_id})])
            return {"status": "pending", "submission_id": submission_id, "record_id": submission.record_id}

    def put_file(self, context: StoreContext, submission_id: str, sha256: str, chunks: Iterable[bytes]) -> dict[str, Any]:
        """Consume chunks only for a previously accepted, declared digest.

        Actual bytes are counted irrespective of any transport Content-Length.
        Even a deduplicated upload must match its declared size and digest.
        """
        _digest(sha256)
        # Read before taking a write lock so an unknown submission creates nothing.
        self._pending(context, submission_id)
        with ExitStack() as stack:
            with self._write_project(context):
                pending = self._pending(context, submission_id)
                submission = self._stored_submission(pending, context, pending=True)
                file = next((f for f in submission.files if f.sha256 == sha256), None)
                if file is None:
                    raise PrivateStoreError("undeclared_digest")
                found, is_pending = self._match(context, submission)
                if found is not None and not is_pending:
                    self._verify(context, found, pending=False)
                parts = (*self._project(context), "blobs", "sha256", sha256[:2])
                # The cleaner cannot observe an unleased live temp: creation and
                # flock both occur under this short initial project lock.
                staged = stack.enter_context(self._temporary(parts))
            self._receive(staged, chunks, expected=file)
            with self._write_project(context):
                self._pending(context, submission_id)
                found, is_pending = self._match(context, submission)
                if found is not None and not is_pending:
                    self._verify(context, found, pending=False)
                try:
                    self._blob(context, file)
                except PrivateStoreError as exc:
                    if exc.code != "missing_blob":
                        raise
                self._publish(staged, sha256, expected=file)
                return {"status": "stored", "sha256": sha256, "size": file.size, "content_validated": "hash_only"}

    def commit(self, context: StoreContext, submission_id: str) -> dict[str, Any]:
        """Verify every declared blob and atomically write the immutable record last."""
        self._pending(context, submission_id)
        with self._write_project(context):
            value = self._pending(context, submission_id)
            submission = self._stored_submission(value, context, pending=True)
            found, pending = self._match(context, submission)
            if found is not None and not pending:
                self._verify(context, found, pending=False)
                return {"status": "already_present", "record": found}
            self._verify(context, value, pending=True)
            record = {k: v for k, v in value.items() if k != "submission_id"}
            self._atomic((*self._project(context), "records"), submission.record_id + ".json", [_canonical(record)])
            return {"status": "created", "record": record}

    def get_record(self, context: StoreContext, record_id: str, *, max_metadata_bytes: int | None = None) -> dict[str, Any]:
        """Read a committed record; missing or damaged payloads are never served."""
        _digest(record_id)
        try:
            value = self._read_json((*self._project(context), "records"), record_id + ".json", max_bytes=max_metadata_bytes)
        except FileNotFoundError as exc:
            raise PrivateStoreError("not_found", 404) from exc
        if value.get("record_id") != record_id:
            raise PrivateStoreError("corrupt_record", 409)
        self._verify(context, value, pending=False)
        return value

    def list_records(self, context: StoreContext, *, max_metadata_bytes: int | None = None, max_records: int | None = None) -> list[dict[str, Any]]:
        """List committed records only; never create a root or expose pending data."""
        names = self._names((*self._project(context), "records"), limit=max_records)
        if any(re.fullmatch(r"[0-9a-f]{64}\.json", name) is None for name in names):
            raise PrivateStoreError("corrupt_record", 409)
        records = []
        remaining = max_metadata_bytes
        for name in names:
            record = self.get_record(context, name[:-5], max_metadata_bytes=remaining)
            if remaining is not None:
                remaining -= len(_canonical(record)) + 1
                if remaining < 0:
                    raise PrivateStoreError("response_too_large", 413)
            records.append(record)
        return records

    def read_file(self, context: StoreContext, record_id: str, sha256: str) -> bytes:
        """Return opaque bytes belonging to a sound record in this project."""
        _digest(sha256)
        value = self.get_record(context, record_id)
        submission = self._stored_submission(value, context, pending=False)
        file = next((f for f in submission.files if f.sha256 == sha256), None)
        if file is None:
            raise PrivateStoreError("not_found", 404)
        return self._blob(context, file, collect=True)

    @contextmanager
    def open_file(self, context: StoreContext, record_id: str, sha256: str) -> Iterator[tuple[BinaryIO, int]]:
        """Open a verified, anchored inode for bounded-memory opaque downloads.

        Verification completes before yielding. The consumer must close this
        context, including after disconnects; paths are never exposed to it.
        """
        _digest(sha256)
        value = self.get_record(context, record_id)
        submission = self._stored_submission(value, context, pending=False)
        file = next((f for f in submission.files if f.sha256 == sha256), None)
        if file is None:
            raise PrivateStoreError("not_found", 404)
        try:
            with self._directory((*self._project(context), "blobs", "sha256", sha256[:2])) as directory, os.fdopen(self._open(directory, sha256), "rb") as stream:
                digest = hashlib.sha256()
                count = 0
                while chunk := stream.read(65_536):
                    count += len(chunk)
                    if count > file.size:
                        raise PrivateStoreError("corrupt_record", 409)
                    digest.update(chunk)
                if count != file.size or digest.hexdigest() != sha256:
                    raise PrivateStoreError("corrupt_record", 409)
                stream.seek(0)
                yield stream, file.size
        except FileNotFoundError as exc:
            raise PrivateStoreError("corrupt_record", 409) from exc

    def recover(self, context: StoreContext) -> int:
        """Remove orphan temporary files after restart under the project lock.

        Every authorized write also performs this recovery. Committed blobs and
        pending manifests are retained; deletion/garbage collection is deferred.
        """
        parts = self._project(context)
        try:
            with self._directory(parts) as fd:
                self._tree(fd)
                with _ProjectLock(fd):
                    self._same_directory(parts, fd)
                    return self._tree(fd, clean=True)
        except FileNotFoundError:
            return 0
        except Timeout as exc:
            raise PrivateStoreError("store_busy", 503) from exc
