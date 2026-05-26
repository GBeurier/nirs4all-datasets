"""Content hashing and the incremental manifest engine.

A dataset's manifest is its content-addressed source of truth: per-file local SHA-256
(authoritative for byte identity, stored alongside but never replaced by the Dataverse
native checksum), a stable ``descriptor_hash``, and the converter identity. Re-processing is
driven by comparing the *inputs* (raw files + descriptor + converter name/version/config)
against the previous manifest -- unchanged inputs are skipped.

``descriptor_hash`` excludes publish-assigned Dataverse fields (``doi``/``dataset_version``)
so publishing does not spuriously trigger a rebuild.
"""
from __future__ import annotations

import hashlib
import json
import os
from collections.abc import Iterable
from datetime import UTC, datetime
from pathlib import Path

from nirs4all_datasets.schema import DatasetDescriptor, FileEntry, FileRole, Manifest

_CHUNK = 1 << 20
# Descriptor fields assigned at publish time; excluded from the processing hash.
_HASH_EXCLUDE: dict = {"dataverse": {"doi", "dataset_version"}}


def sha256_file(path: str | Path, chunk: int = _CHUNK) -> str:
    """Return the streaming SHA-256 hex digest of a file's bytes."""
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(chunk), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_bytes(data: bytes) -> str:
    """Return the SHA-256 hex digest of an in-memory blob."""
    return hashlib.sha256(data).hexdigest()


def descriptor_hash(descriptor: DatasetDescriptor) -> str:
    """Stable hash of a descriptor's *processing-relevant* content.

    Independent of YAML formatting and of publish-assigned Dataverse identifiers.
    """
    data = descriptor.model_dump(mode="json", exclude=_HASH_EXCLUDE)
    return sha256_bytes(json.dumps(data, sort_keys=True, separators=(",", ":")).encode("utf-8"))


def _relpath(path: str | Path, base: Path) -> str:
    """Path relative to ``base``; raises if it resolves outside (no basename collisions)."""
    resolved = Path(path).resolve()
    try:
        return str(resolved.relative_to(base.resolve()))
    except ValueError as exc:
        raise ValueError(f"file {path} is outside dataset_dir {base}; raw files must live under the dataset directory.") from exc


def _file_entry(path: Path, role: FileRole, base: Path) -> FileEntry:
    return FileEntry(path=_relpath(path, base), role=role, sha256=sha256_file(path), size=path.stat().st_size)


def build_manifest(
    descriptor: DatasetDescriptor,
    *,
    dataset_dir: str | Path,
    converter_name: str,
    converter_version: str,
    converter_config: dict[str, str],
    row_counts: dict[str, int],
    raw_files: Iterable[str | Path] = (),
) -> Manifest:
    """Build a :class:`Manifest` from a dataset's raw + canonical files and provenance.

    ``canonical_hashes`` is derived from the enumerated canonical Parquet files (so the
    manifest is internally consistent). Every file under ``canonical/`` is recorded.
    """
    base = Path(dataset_dir)
    files: list[FileEntry] = [_file_entry(Path(raw), FileRole.RAW, base) for raw in raw_files]
    canonical = base / "canonical"
    if canonical.exists():
        for entry in sorted(canonical.rglob("*")):
            if entry.is_file():
                files.append(_file_entry(entry, FileRole.CANONICAL, base))
    canonical_hashes = {Path(fe.path).name: fe.sha256 for fe in files if fe.role is FileRole.CANONICAL and fe.path.endswith(".parquet")}
    return Manifest(
        dataset_id=descriptor.id,
        descriptor_hash=descriptor_hash(descriptor),
        converter_name=converter_name,
        converter_version=converter_version,
        converter_config=dict(converter_config),
        files=files,
        canonical_hashes=canonical_hashes,
        row_counts={k: int(v) for k, v in row_counts.items()},
        doi=descriptor.dataverse.doi,
        dataset_version=descriptor.dataverse.dataset_version,
        created_at=datetime.now(UTC).isoformat(),
    )


def write_manifest(manifest: Manifest, path: str | Path) -> None:
    """Atomically write a manifest as pretty JSON (temp file + os.replace)."""
    path = Path(path)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(manifest.model_dump_json(indent=2), encoding="utf-8")
    os.replace(tmp, path)


def read_manifest(path: str | Path) -> Manifest:
    """Read a manifest from JSON."""
    return Manifest(**json.loads(Path(path).read_text(encoding="utf-8")))


def needs_rebuild(
    descriptor: DatasetDescriptor,
    *,
    dataset_dir: str | Path,
    previous: Manifest | None,
    converter_name: str | None = None,
    converter_version: str | None = None,
    converter_config: dict[str, str] | None = None,
    raw_files: Iterable[str | Path] = (),
    verify_outputs: bool = False,
) -> tuple[bool, list[str]]:
    """Decide whether a dataset must be (re)processed by comparing inputs to ``previous``.

    Inputs are the raw files, the descriptor, and the full converter identity
    (name + version + config) -- canonical outputs are derived from these. A size pre-filter
    avoids hashing unchanged files. With ``verify_outputs`` the recorded canonical files are
    also checked on disk (skip then also guarantees the local outputs are intact).

    Returns ``(changed, reasons)``; ``reasons`` is empty iff processing can be skipped.
    """
    if previous is None:
        return True, ["new dataset (no previous manifest)"]

    base = Path(dataset_dir)
    reasons: list[str] = []
    if descriptor_hash(descriptor) != previous.descriptor_hash:
        reasons.append("descriptor changed")
    if converter_name is not None and converter_name != previous.converter_name:
        reasons.append(f"converter changed ({previous.converter_name} -> {converter_name})")
    if converter_version is not None and converter_version != previous.converter_version:
        reasons.append(f"converter version changed ({previous.converter_version} -> {converter_version})")
    if converter_config is not None and dict(converter_config) != previous.converter_config:
        reasons.append("converter config changed")

    previous_raw = {fe.path: fe for fe in previous.files if fe.role is FileRole.RAW}
    current_raw = {_relpath(raw, base): Path(raw) for raw in raw_files}
    if set(current_raw) != set(previous_raw):
        reasons.append("raw file set changed")
    else:
        for rel, path in current_raw.items():
            entry = previous_raw[rel]
            if not path.exists():
                reasons.append(f"raw file missing: {rel}")
            elif path.stat().st_size != entry.size or sha256_file(path) != entry.sha256:
                reasons.append(f"raw file changed: {rel}")

    if verify_outputs:
        for fe in previous.files:
            if fe.role is FileRole.CANONICAL:
                out = base / fe.path
                if not out.exists() or out.stat().st_size != fe.size or sha256_file(out) != fe.sha256:
                    reasons.append(f"canonical output missing or corrupt: {fe.path}")
    return (bool(reasons), reasons)


def manifest_diff(old: Manifest, new: Manifest) -> dict[str, list[str]]:
    """Return ``{'added','removed','changed'}`` file paths between two manifests (for tombstones)."""
    old_map = {fe.path: fe.sha256 for fe in old.files}
    new_map = {fe.path: fe.sha256 for fe in new.files}
    added = sorted(set(new_map) - set(old_map))
    removed = sorted(set(old_map) - set(new_map))
    changed = sorted(path for path in set(old_map) & set(new_map) if old_map[path] != new_map[path])
    return {"added": added, "removed": removed, "changed": changed}
