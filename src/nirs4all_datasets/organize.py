"""Idempotent local organization: preserve raw, convert to canonical, write the manifest.

Given a raw v2.0 leaf and its descriptor, this places the raw bytes under
``<datasets_root>/<id>/raw/``, converts them to the canonical per-source / sample-identity-joined
form (:func:`nirs4all_datasets.canonical.build_canonical`), and writes the manifest. Re-running on
unchanged inputs is a no-op (the manifest's content hashes decide), so adding new datasets and
re-running only (re)processes the new or changed ones.
"""
from __future__ import annotations

import shutil
from dataclasses import dataclass, field
from pathlib import Path

from nirs4all_datasets.canonical import CONVERTER_NAME, CONVERTER_VERSION, CanonicalResult, build_canonical
from nirs4all_datasets.manifest import build_manifest, needs_rebuild, read_manifest, sha256_file, write_manifest
from nirs4all_datasets.schema import ConversionStatus, DatasetDescriptor, Tier


@dataclass
class OrganizeResult:
    """Outcome of organizing one dataset."""

    dataset_id: str
    dataset_dir: Path
    manifest_path: Path
    skipped: bool
    reasons: list[str] = field(default_factory=list)
    canonical_result: CanonicalResult | None = None
    conversion_status: ConversionStatus | None = None
    conversion_warnings: list[str] = field(default_factory=list)


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


def _source_raw_pairs(source: Path) -> list[tuple[str, Path]]:
    """Map each source file to the ``raw/<relpath>`` it will occupy under the dataset dir.

    Used to compare *source* bytes against the previous manifest before copying anything.
    """
    if source.is_file():
        return [(f"raw/{source.name}", source)]
    return [(f"raw/{p.relative_to(source).as_posix()}", p) for p in sorted(source.rglob("*")) if p.is_file()]


def organize(
    source: str | Path,
    descriptor: DatasetDescriptor,
    datasets_root: str | Path,
    *,
    force: bool = False,
    source_context: dict[str, str] | None = None,
) -> OrganizeResult:
    """Place raw, (re)build the canonical form + manifest for one dataset, idempotently.

    Skips work when the descriptor and raw bytes are unchanged and the canonical outputs are intact
    (``verify_outputs``). Pass ``force=True`` to rebuild regardless. The converter identity is this
    package's own canonical converter (decoupled from any nirs4all version), so a nirs4all upgrade no
    longer forces a rebuild — only a change in the raw bytes, the processing-relevant descriptor
    fields, or this package's converter version does.
    """
    source = Path(source)
    if not source.exists():
        raise FileNotFoundError(f"organize source does not exist: {source}")

    dataset_dir = Path(datasets_root) / descriptor.id
    dataset_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = dataset_dir / "manifest.json"
    previous = read_manifest(manifest_path) if manifest_path.exists() else None
    from nirs4all_datasets.curation import contract_hash, find_soilsite

    converter_config = {"curation_contract_sha256": contract_hash(descriptor.id)}
    soilsite = find_soilsite(source) if descriptor.id.startswith("ossl_") else None
    if soilsite:
        converter_config["soilsite_sha256"] = sha256_file(soilsite)

    converter_config.update({f"source_context:{key}": sha256_file(path) for key, path in sorted((source_context or {}).items())})
    changed, reasons = needs_rebuild(
        descriptor,
        dataset_dir=dataset_dir,
        previous=previous,
        converter_name=CONVERTER_NAME,
        converter_version=CONVERTER_VERSION,
        converter_config=converter_config,
        raw_files=_source_raw_pairs(source),
        verify_outputs=True,
    )
    if previous is not None and not changed and not force:
        return OrganizeResult(descriptor.id, dataset_dir, manifest_path, skipped=True, conversion_status=previous.conversion_status, conversion_warnings=previous.conversion_warnings)

    placed = _place_raw(source, dataset_dir)
    result = build_canonical(source, descriptor, dataset_dir, source_context=source_context)
    manifest = build_manifest(
        descriptor,
        dataset_dir=dataset_dir,
        converter_name=result.converter_name,
        converter_version=result.converter_version,
        converter_config=converter_config,
        row_counts=result.row_counts,
        raw_files=placed,
        conversion_status=result.status,
        # Manifests are tracked/public; anonymized warnings can identify variables.
        conversion_warnings=(
            ["conversion warning details withheld for anonymized dataset"] * len(result.warnings)
            if descriptor.tier is Tier.ANONYMIZED else result.warnings
        ),
    )
    write_manifest(manifest, manifest_path)
    if result.status is ConversionStatus.FAILED:
        # A card from an earlier successful conversion must not represent this failed output.
        for name in ("card.json", "card.md", "croissant.json", "card.anon.json"):
            (dataset_dir / name).unlink(missing_ok=True)
    return OrganizeResult(descriptor.id, dataset_dir, manifest_path, skipped=False, reasons=reasons, canonical_result=result, conversion_status=result.status, conversion_warnings=result.warnings)
