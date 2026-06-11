"""The distributable download contract (``catalog/index.json``) — schema, sanitization, determinism."""
from __future__ import annotations

import json

import pytest
import yaml

from nirs4all_datasets.index import INDEX_SCHEMA, build_index, load_index, resolve
from nirs4all_datasets.schema import DatasetDescriptor, Tier


def _write_dataset(root, descriptor: DatasetDescriptor, manifest: dict | None) -> None:
    (root / "catalog" / "datasets").mkdir(parents=True, exist_ok=True)
    (root / "catalog" / "datasets" / f"{descriptor.id}.yaml").write_text(
        yaml.safe_dump(descriptor.model_dump(mode="json"), sort_keys=False, allow_unicode=True), encoding="utf-8"
    )
    if manifest is not None:
        d = root / "datasets" / descriptor.id
        d.mkdir(parents=True, exist_ok=True)
        (d / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")


def _descriptor(**kw) -> DatasetDescriptor:
    base: dict = {
        "schema_version": "2.0",
        "id": "demo",
        "name": "Demo Set",
        "description": "A demo dataset.",
        "sources": [{"source_id": "X", "modality": "NIR", "axis_unit": "nm"}],
        "variables": [{"name": "Moisture", "role": "target", "type": "numeric"}],
        "tier": "public",
        "provenance": {"contributor": "Lab A"},
        "governance": {
            "license": "CC-BY-4.0",
            "owner_steward": "Lab A",
            "redistribution_rights": "open",
            "consent_ethics_status": "n/a",
            "anonymization_status": "n/a",
            "permitted_use": "research",
            "access_policy": "open",
        },
        "origin_sources": [{"kind": "zenodo", "mode": "canonical", "locator": "10.5281/zenodo.123", "access": "open"}],
    }
    base.update(kw)
    return DatasetDescriptor(**base)


def _manifest(dataset_id: str, *, file_id: int | None = None) -> dict:
    return {
        "schema_version": "2.0",
        "dataset_id": dataset_id,
        "processing_hash": "a" * 64,
        "converter_name": "nirs4all-datasets-canonical",
        "converter_version": "0.1.0",
        "files": [
            {"path": "raw/X.csv", "role": "raw", "sha256": "b" * 64, "size": 10},
            {"path": "canonical/sources/X.parquet", "role": "canonical", "sha256": "c" * 64, "size": 99, "file_id": file_id},
            {"path": "canonical/dataset.json", "role": "canonical", "sha256": "d" * 64, "size": 5, "file_id": None},
        ],
    }


def test_index_carries_download_contract(tmp_path):
    desc = _descriptor()
    _write_dataset(tmp_path, desc, _manifest("demo", file_id=678))
    idx = build_index(tmp_path)

    assert idx["schema"] == INDEX_SCHEMA
    assert idx["n_datasets"] == 1
    entry = resolve(idx, "demo")
    assert entry["tier"] == "public"
    assert entry["dataverse"]["instance"].startswith("https://")
    # only canonical files, never raw; basename + relpath + directory_label + sha256 + size + file_id
    names = {f["name"] for f in entry["files"]}
    assert names == {"X.parquet", "dataset.json"}
    parquet = next(f for f in entry["files"] if f["name"] == "X.parquet")
    assert parquet["relpath"] == "canonical/sources/X.parquet"
    assert parquet["directory_label"] == "canonical/sources"
    assert parquet["sha256"] == "c" * 64
    assert parquet["file_id"] == 678
    assert entry["origins"][0] == {"kind": "zenodo", "mode": "canonical", "locator": "10.5281/zenodo.123", "access": "open"}


def test_anonymized_descriptor_is_masked_in_index(tmp_path):
    desc = _descriptor(id="secret", tier=Tier.ANONYMIZED, variables=[{"name": "SecretYield", "role": "target", "type": "numeric"}])
    _write_dataset(tmp_path, desc, _manifest("secret"))
    entry = resolve(build_index(tmp_path), "secret")
    # the embedded descriptor must leak no identifying names
    blob = json.dumps(entry)
    assert "SecretYield" not in blob
    assert entry["descriptor"]["variables"][0]["name"] == "var_001"
    assert entry["descriptor"]["name"] == "secret"  # opaque id reused as display name


def test_index_is_deterministic_and_roundtrips(tmp_path):
    desc = _descriptor()
    _write_dataset(tmp_path, desc, _manifest("demo"))
    build_index(tmp_path)
    first = (tmp_path / "catalog" / "index.json").read_text()
    build_index(tmp_path)
    second = (tmp_path / "catalog" / "index.json").read_text()
    assert first == second  # byte-stable (sorted keys, fixed indent, one trailing newline)
    assert first.endswith("\n")
    assert load_index(tmp_path)["datasets"]["demo"]["tier"] == "public"


def test_resolve_unknown_raises(tmp_path):
    _write_dataset(tmp_path, _descriptor(), _manifest("demo"))
    with pytest.raises(KeyError):
        resolve(build_index(tmp_path), "nope")
