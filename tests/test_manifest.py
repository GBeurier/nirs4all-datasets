"""Tests for the incremental manifest engine (schema 2.0)."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from nirs4all_datasets import schema as s
from nirs4all_datasets.manifest import (
    build_manifest,
    manifest_diff,
    metadata_hash,
    needs_rebuild,
    processing_hash,
    read_manifest,
    sha256_bytes,
    write_manifest,
)


def _descriptor(content: str = "1.0.0", dataverse: dict[str, Any] | None = None, **over: Any) -> s.DatasetDescriptor:
    kwargs: dict[str, Any] = {
        "id": "corn",
        "name": "Corn",
        "description": "example",
        "sources": [{"source_id": "X1", "axis_unit": "nm"}],
        "variables": [{"name": "protein", "role": "target", "type": "numeric"}],
        "provenance": {"contributor": "Lab"},
        "governance": {"license": "CC-BY-4.0"},
        "versions": {"content": content},
    }
    if dataverse is not None:
        kwargs["dataverse"] = dataverse
    kwargs.update(over)
    return s.DatasetDescriptor(**kwargs)


def _raw_file(tmp_path: Path, content: bytes = b"v1") -> Path:
    raw = tmp_path / "raw"
    raw.mkdir(exist_ok=True)
    path = raw / "a.opus"
    path.write_bytes(content)
    return path


def _canonical(tmp_path: Path) -> None:
    canonical = tmp_path / "canonical" / "sources"
    canonical.mkdir(parents=True, exist_ok=True)
    (canonical / "X1.parquet").write_bytes(b"x-bytes")
    (tmp_path / "canonical" / "variables.parquet").write_bytes(b"y-bytes")
    (tmp_path / "canonical" / "dataset.json").write_text("{}", encoding="utf-8")


def _full_manifest(tmp_path: Path, raw: Path, converter_config: dict[str, str] | None = None) -> Any:
    return build_manifest(
        _descriptor(),
        dataset_dir=tmp_path,
        converter_name="c",
        converter_version="1",
        converter_config=converter_config or {},
        row_counts={"X1": 10},
        raw_files=[raw],
    )


def test_processing_hash_stable_and_sensitive() -> None:
    assert processing_hash(_descriptor()) == processing_hash(_descriptor())
    assert processing_hash(_descriptor("1.0.0")) != processing_hash(_descriptor("2.0.0"))  # content version is byte-relevant


def test_processing_hash_excludes_publish_and_protocol() -> None:
    plain = processing_hash(_descriptor())
    published = processing_hash(_descriptor(dataverse={"doi": "10.70112/abc", "dataset_version": "2.0"}))
    protocol = processing_hash(_descriptor(versions={"content": "1.0.0", "schema_protocol": "9.9"}))
    retrieval = processing_hash(_descriptor(retrieval={"status": "token_required", "blockers": ["upload pending"]}))
    assert plain == published == protocol == retrieval  # none of these distribution/protocol edits rebuilds canonical


def test_metadata_hash_excludes_retrieval_routes() -> None:
    base = _descriptor()
    edited = _descriptor(retrieval={"status": "token_required", "blockers": ["upload pending"]})
    assert metadata_hash(base) == metadata_hash(edited)


def test_descriptive_edits_skip_rebuild_but_refresh_card() -> None:
    base = _descriptor()
    edited = base.model_copy(update={
        "tier": s.Tier.PUBLIC,
        "origin_sources": [s.OriginSource(kind="zenodo", locator="10.5281/zenodo.1")],
        "variables": [s.Variable(name="protein", role="metadata")],
    })
    assert processing_hash(base) == processing_hash(edited)  # descriptive -> no canonical rebuild
    assert metadata_hash(base) != metadata_hash(edited)  # but the card must refresh


def test_build_records_all_canonical_and_derives_hashes(tmp_path: Path) -> None:
    _canonical(tmp_path)
    raw = _raw_file(tmp_path)
    manifest = _full_manifest(tmp_path, raw)
    paths = {fe.path: fe.role.value for fe in manifest.files}
    assert paths["raw/a.opus"] == "raw"
    assert paths["canonical/sources/X1.parquet"] == "canonical"
    assert paths["canonical/dataset.json"] == "canonical"  # non-parquet canonical recorded too
    assert manifest.canonical_hashes["X1.parquet"] == sha256_bytes(b"x-bytes")
    assert "dataset.json" not in manifest.canonical_hashes  # only parquet in canonical_hashes

    write_manifest(manifest, tmp_path / "manifest.json")
    restored = read_manifest(tmp_path / "manifest.json")
    assert restored.processing_hash == manifest.processing_hash
    assert {fe.path for fe in restored.files} == set(paths)


def test_raw_outside_dataset_dir_rejected(tmp_path: Path) -> None:
    outside = tmp_path.parent / "outside_raw.bin"
    outside.write_bytes(b"x")
    with pytest.raises(ValueError):
        build_manifest(_descriptor(), dataset_dir=tmp_path, converter_name="c", converter_version="1", converter_config={}, row_counts={}, raw_files=[outside])


def test_needs_rebuild_inputs(tmp_path: Path) -> None:
    _canonical(tmp_path)
    raw = _raw_file(tmp_path)
    previous = _full_manifest(tmp_path, raw)

    assert needs_rebuild(_descriptor(), dataset_dir=tmp_path, previous=None, raw_files=[raw])[0] is True
    changed, reasons = needs_rebuild(_descriptor(), dataset_dir=tmp_path, previous=previous, converter_name="c", converter_version="1", converter_config={}, raw_files=[raw])
    assert changed is False and reasons == []
    assert needs_rebuild(_descriptor("2.0.0"), dataset_dir=tmp_path, previous=previous, raw_files=[raw])[0] is True  # content bump
    assert needs_rebuild(_descriptor(), dataset_dir=tmp_path, previous=previous, converter_version="2", raw_files=[raw])[0] is True
    assert needs_rebuild(_descriptor(), dataset_dir=tmp_path, previous=previous, converter_config={"x": "y"}, raw_files=[raw])[0] is True


def test_needs_rebuild_raw_changes(tmp_path: Path) -> None:
    raw = _raw_file(tmp_path)
    previous = _full_manifest(tmp_path, raw)
    raw.write_bytes(b"v2-much-longer-content")
    assert needs_rebuild(_descriptor(), dataset_dir=tmp_path, previous=previous, converter_version="1", raw_files=[raw])[0] is True
    raw.unlink()
    changed, reasons = needs_rebuild(_descriptor(), dataset_dir=tmp_path, previous=previous, raw_files=[raw])
    assert changed is True and any("missing" in r for r in reasons)


def test_verify_outputs_detects_missing_canonical(tmp_path: Path) -> None:
    _canonical(tmp_path)
    raw = _raw_file(tmp_path)
    previous = _full_manifest(tmp_path, raw)
    (tmp_path / "canonical" / "sources" / "X1.parquet").unlink()
    changed, reasons = needs_rebuild(_descriptor(), dataset_dir=tmp_path, previous=previous, converter_version="1", raw_files=[raw], verify_outputs=True)
    assert changed is True and any("canonical output" in r for r in reasons)


def test_manifest_diff() -> None:
    def fe(path: str, h: str) -> s.FileEntry:
        return s.FileEntry(path=path, role="canonical", sha256=h, size=1)

    old = s.Manifest(dataset_id="d", processing_hash="a" * 64, converter_name="c", converter_version="1", files=[fe("X", "a" * 64), fe("Y", "b" * 64)])
    new = s.Manifest(dataset_id="d", processing_hash="a" * 64, converter_name="c", converter_version="1", files=[fe("X", "c" * 64), fe("Z", "d" * 64)])
    assert manifest_diff(old, new) == {"added": ["Z"], "removed": ["Y"], "changed": ["X"]}
