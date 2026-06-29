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
        "retrieval": {
            "status": "raw_reproducible",
            "public_retrievable": True,
            "public_redistributable": False,
            "routes": [
                {
                    "id": "official_raw",
                    "method": "raw_retrieve",
                    "provider": "zenodo",
                    "locator": "10.5281/zenodo.123",
                    "resources": [
                        {
                            "id": "archive",
                            "role": "archive",
                            "selector": {"kind": "zenodo_key", "value": "demo.zip"},
                            "file_name": "demo.zip",
                            "format": "zip",
                        }
                    ],
                    "canonicalization": {"engine": "nirs4all_io", "recipe_id": "demo_v1"},
                }
            ],
        },
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
    assert entry["retrieval"]["status"] == "raw_reproducible"
    assert entry["retrieval"]["routes"][0]["resources"][0]["selector"] == {"kind": "zenodo_key", "value": "demo.zip"}
    assert entry["descriptor"]["retrieval"] == entry["retrieval"]


def test_index_synthesizes_raw_retrieval_from_open_direct_url(tmp_path):
    desc = _descriptor(
        origin_sources=[
            {
                "kind": "url",
                "mode": "raw",
                "locator": "https://example.test/data/raw.csv",
                "access": "open",
            }
        ],
        retrieval={},
    )
    _write_dataset(tmp_path, desc, _manifest("demo", file_id=678))
    entry = resolve(build_index(tmp_path), "demo")

    route = entry["retrieval"]["routes"][0]
    assert entry["retrieval"]["status"] == "raw_reproducible"
    assert route["method"] == "raw_retrieve"
    assert route["provider"] == "url"
    assert route["resources"][0]["selector"] == {"kind": "direct_url", "value": "https://example.test/data/raw.csv"}
    assert route["resources"][0]["format"] == "csv"


def test_index_synthesizes_raw_retrieval_from_nirs_db_raw_manifest(tmp_path):
    desc = _descriptor(
        origin_sources=[{"kind": "url", "mode": "raw", "locator": "https://example.test/landing", "access": "open"}],
        retrieval={},
    )
    _write_dataset(tmp_path, desc, _manifest("demo", file_id=678))
    raw_dir = tmp_path / "NIRS DB" / "v2.0" / "demo"
    raw_dir.mkdir(parents=True)
    (raw_dir / "raw_manifest.csv").write_text(
        "\n".join(
            [
                "dataset_id;source_kind;source_path_or_url;local_path_if_any;file_name;file_role;file_size_bytes;date_accessed_or_checked;used_for_conversion;notes",
                "demo;controlled_download;https://example.test/raw/001.jdx;;001.jdx;source_jcamp_dx;123;2026-01-01;yes;",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    entry = resolve(build_index(tmp_path), "demo")
    route = entry["retrieval"]["routes"][0]

    assert route["id"] == "nirs_db_raw_manifest"
    assert route["resources"][0]["selector"] == {"kind": "direct_url", "value": "https://example.test/raw/001.jdx"}
    assert route["resources"][0]["file_name"] == "001.jdx"
    assert route["resources"][0]["format"] == "jcamp_dx"
    assert route["resources"][0]["size"] == 123
    assert route["canonicalization"]["engine"] == "nirs4all_formats"


def test_open_raw_origin_without_safe_route_is_not_token_required(tmp_path):
    desc = _descriptor(
        tier="private",
        origin_sources=[
            {
                "kind": "url",
                "mode": "raw",
                "locator": "https://example.test/dataset-landing-page",
                "access": "open",
            },
            {"kind": "script", "mode": "raw", "locator": "source_to_standard.py", "access": "manual"},
        ],
        retrieval={},
    )
    _write_dataset(tmp_path, desc, _manifest("demo", file_id=678))
    entry = resolve(build_index(tmp_path), "demo")

    assert entry["retrieval"]["status"] == "missing_delegate"
    assert entry["retrieval"]["routes"] == []
    assert entry["retrieval"]["public_retrievable"] is True


def test_index_synthesizes_jpl_ecostress_route(tmp_path):
    desc = _descriptor(
        id="ecostress_lunar_tir_2124points",
        tier="private",
        origin_sources=[
            {"kind": "url", "mode": "raw", "locator": "https://speclib.jpl.nasa.gov/download", "access": "open"},
            {"kind": "url", "mode": "raw", "locator": "https://speclib.jpl.nasa.gov/", "access": "open"},
            {"kind": "script", "mode": "raw", "locator": "source_to_standard.py", "access": "manual"},
        ],
        publications=[{"doi": "10.1016/j.rse.2019.05.015", "title": "The ECOSTRESS spectral library version 1.0"}],
        retrieval={},
    )
    _write_dataset(tmp_path, desc, _manifest("ecostress_lunar_tir_2124points", file_id=678))
    entry = resolve(build_index(tmp_path), "ecostress_lunar_tir_2124points")
    r = entry["retrieval"]

    # The family stops being publicly invisible: a structured JPL route + public_retrievable.
    assert r["public_retrievable"] is True
    assert r["public_redistributable"] is False
    route = next(rt for rt in r["routes"] if rt["provider"] == "jpl_ecostress")
    assert route["method"] == "raw_retrieve"
    assert route["access"] == "open"
    assert route["landing_url"] == "https://speclib.jpl.nasa.gov/download"
    assert route["citation"] == "10.1016/j.rse.2019.05.015"
    res = route["resources"][0]
    assert res["selector"] == {"kind": "api_file_name", "value": "lunar"}  # second id token == JPL category
    assert res["format"] == "zip"
    assert res["unpack"] == {"archive": True, "members": []}
    assert route["canonicalization"]["engine"] == "delegate"
    assert route["canonicalization"]["delegate"] == "source_to_standard.py"
    # Honest: the shared converter + exact bulk endpoint are still missing, so status is not over-claimed.
    assert r["status"] == "missing_delegate"
    assert any("endpoint" in b.lower() for b in r["blockers"])
    assert entry["descriptor"]["retrieval"] == r


def test_index_synthesizes_ecostress_direct_urls_from_raw_manifest(tmp_path):
    desc = _descriptor(
        id="ecostress_lunar_tir_2124points",
        tier="private",
        origin_sources=[
            {"kind": "url", "mode": "raw", "locator": "https://speclib.jpl.nasa.gov/download", "access": "open"},
            {"kind": "script", "mode": "raw", "locator": "source_to_standard.py", "access": "manual"},
        ],
        retrieval={},
    )
    _write_dataset(tmp_path, desc, _manifest("ecostress_lunar_tir_2124points", file_id=678))
    raw_dir = tmp_path / "NIRS DB" / "v2.0" / "ecostress_lunar_tir_2124points"
    raw_dir.mkdir(parents=True)
    (raw_dir / "raw_manifest.csv").write_text(
        "\n".join(
            [
                "source_file;file_name;category",
                r"D:\VS projects\ecostress_nirs_database\input_data\extracted\lunar\soil.lunar.maria.fine.tir.12070_405.jhu.becknic.spectrum.txt;soil.lunar.maria.fine.tir.12070_405.jhu.becknic.spectrum.txt;lunar",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    entry = resolve(build_index(tmp_path), "ecostress_lunar_tir_2124points")
    route = entry["retrieval"]["routes"][0]
    res = route["resources"][0]

    assert entry["retrieval"]["status"] == "raw_reproducible"
    assert route["provider"] == "url"
    assert route["automated_download_allowed"] is True
    assert res["role"] == "spectra"
    assert res["format"] == "ecostress_spectrum_txt"
    assert res["selector"] == {
        "kind": "direct_url",
        "value": "https://speclib.jpl.nasa.gov/ecospeclibdata/soil.lunar.maria.fine.tir.12070_405.jhu.becknic.spectrum.txt",
    }
    assert route["canonicalization"]["engine"] == "rust_recipe"
    assert route["canonicalization"]["recipe_id"] == "jpl_ecostress_spectrum_txt_v1"


def test_ecostress_route_skips_unknown_category(tmp_path):
    # Same JPL host, but the id's second token is not a known ECOSTRESS material category:
    # fall back to the generic opaque behavior, never a wrong jpl_ecostress route.
    desc = _descriptor(
        id="ecostress_notacategory_tir_10points",
        tier="private",
        origin_sources=[
            {"kind": "url", "mode": "raw", "locator": "https://speclib.jpl.nasa.gov/download", "access": "open"},
            {"kind": "script", "mode": "raw", "locator": "source_to_standard.py", "access": "manual"},
        ],
        retrieval={},
    )
    _write_dataset(tmp_path, desc, _manifest("ecostress_notacategory_tir_10points", file_id=678))
    entry = resolve(build_index(tmp_path), "ecostress_notacategory_tir_10points")
    assert entry["retrieval"]["routes"] == []
    assert entry["retrieval"]["status"] == "missing_delegate"


def test_anonymized_descriptor_is_masked_in_index(tmp_path):
    desc = _descriptor(
        id="secret",
        tier=Tier.ANONYMIZED,
        variables=[{"name": "SecretYield", "role": "target", "type": "numeric"}],
        dataverse={"instance": "https://dv.example", "doi": "10.70112/SECRET", "dataset_version": "1.0"},
    )
    _write_dataset(tmp_path, desc, _manifest("secret", file_id=678))
    entry = resolve(build_index(tmp_path), "secret")
    # the embedded descriptor must leak no identifying names
    blob = json.dumps(entry)
    assert "SecretYield" not in blob
    assert entry["descriptor"]["variables"][0]["name"] == "var_001"
    assert entry["descriptor"]["name"] == "secret"  # opaque id reused as display name
    # acquisition pointers that would re-identify the dataset are stripped from the PUBLIC index
    assert entry["dataverse"]["doi"] is None
    assert entry["dataverse"]["dataset_version"] is None
    assert entry["origins"] == []
    assert entry["retrieval"]["routes"] == []
    assert entry["retrieval"]["status"] == "token_required"
    assert entry["descriptor"]["retrieval"] == entry["retrieval"]
    assert all(f["file_id"] is None for f in entry["files"])
    assert "10.70112/SECRET" not in blob
    assert "10.5281/zenodo.123" not in blob
    assert "demo.zip" not in blob


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
