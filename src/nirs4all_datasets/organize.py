"""Idempotent local organization: preserve raw, ingest to canonical, write the manifest.

Given a raw ``source`` and its descriptor, this places the raw bytes under
``<datasets_root>/<id>/raw/``, converts them to the canonical form, and writes the manifest.
Re-running on unchanged inputs is a no-op (the manifest's content hashes decide), so adding
new datasets and re-running only (re)processes the new or changed ones.
"""
from __future__ import annotations

import shutil
from dataclasses import dataclass, field
from pathlib import Path

from nirs4all_datasets.ingest import IngestResult, ingest
from nirs4all_datasets.manifest import build_manifest, needs_rebuild, read_manifest, write_manifest
from nirs4all_datasets.schema import DatasetDescriptor


@dataclass
class OrganizeResult:
    """Outcome of organizing one dataset."""

    dataset_id: str
    dataset_dir: Path
    manifest_path: Path
    skipped: bool
    reasons: list[str] = field(default_factory=list)
    ingest_result: IngestResult | None = None


def _converter_identity(source: Path) -> tuple[str | None, str | None]:
    """Cheap converter name+version for the rebuild decision (detects a nirs4all/io upgrade)."""
    if source.is_dir():
        import nirs4all

        return "nirs4all-DatasetConfigs", nirs4all.__version__
    import nirs4all_io as nio

    return "nirs4all-io", nio.__version__


def _place_raw(source: Path, dataset_dir: Path) -> list[Path]:
    """Copy ``source`` into ``dataset_dir/raw/`` (cleaned first, so removed files do not linger)."""
    raw_dir = dataset_dir / "raw"
    if raw_dir.exists():
        shutil.rmtree(raw_dir)
    raw_dir.mkdir(parents=True)
    placed: list[Path] = []
    if source.is_file():
        dst = raw_dir / source.name
        shutil.copy2(source, dst)
        placed.append(dst)
    else:
        for entry in sorted(source.rglob("*")):
            if entry.is_file():
                dst = raw_dir / entry.relative_to(source)
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(entry, dst)
                placed.append(dst)
    return placed


def organize(
    source: str | Path,
    descriptor: DatasetDescriptor,
    datasets_root: str | Path,
    *,
    target: str | None = None,
    signal: str | None = None,
    force: bool = False,
) -> OrganizeResult:
    """Place raw, (re)build the canonical form + manifest for one dataset, idempotently.

    Skips work when the descriptor and raw bytes are unchanged and the canonical outputs are
    intact (``verify_outputs``). Pass ``force=True`` to rebuild regardless.
    """
    source = Path(source)
    if not source.exists():
        raise FileNotFoundError(f"organize source does not exist: {source}")

    dataset_dir = Path(datasets_root) / descriptor.id
    dataset_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = dataset_dir / "manifest.json"
    previous = read_manifest(manifest_path) if manifest_path.exists() else None

    placed = _place_raw(source, dataset_dir)
    converter_name, converter_version = _converter_identity(source)
    changed, reasons = needs_rebuild(
        descriptor,
        dataset_dir=dataset_dir,
        previous=previous,
        converter_name=converter_name,
        converter_version=converter_version,
        raw_files=placed,
        verify_outputs=True,
    )
    if previous is not None and not changed and not force:
        return OrganizeResult(descriptor.id, dataset_dir, manifest_path, skipped=True)

    result = ingest(source, dataset_dir, target=target, signal=signal)
    manifest = build_manifest(
        descriptor,
        dataset_dir=dataset_dir,
        converter_name=result.converter_name,
        converter_version=result.converter_version,
        converter_config=result.converter_config,
        row_counts=result.row_counts,
        raw_files=placed,
    )
    write_manifest(manifest, manifest_path)
    return OrganizeResult(descriptor.id, dataset_dir, manifest_path, skipped=False, reasons=reasons, ingest_result=result)
