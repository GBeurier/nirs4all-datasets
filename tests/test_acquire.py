"""The embedded native acquisition core (``nirs4all_datasets._acquire`` over ``_n4ds``).

No network: only resolve / verify_cached / the pre-network token + not-fetchable gates.
"""
from __future__ import annotations

import hashlib

import pytest

from nirs4all_datasets import _acquire as core

_INDEX = {
    "schema": "1.0",
    "n_datasets": 2,
    "datasets": {
        "pub": {
            "tier": "public",
            "dataverse": {"instance": "https://dv.example", "doi": None, "dataset_version": None},
            "files": [{"name": "X.parquet", "relpath": "canonical/sources/X.parquet", "directory_label": "canonical/sources", "sha256": "ab" * 32, "size": 5, "file_id": None}],
            "origins": [{"kind": "url", "mode": "raw", "locator": "https://vendor/", "access": "manual"}],
            "retrieval": {
                "schema_version": "1.0",
                "status": "raw_reproducible",
                "routes": [{"id": "official", "method": "raw_retrieve", "provider": "url", "locator": "https://vendor/raw.csv", "resources": [{"id": "raw", "selector": {"kind": "direct_url", "value": "https://vendor/raw.csv"}}]}],
            },
            "descriptor": {"id": "pub"},
        },
        "priv": {
            "tier": "private",
            "dataverse": {"instance": "https://dv.example", "doi": "10.70112/PRIV", "dataset_version": "1.0"},
            "files": [{"name": "X.parquet", "relpath": "canonical/sources/X.parquet", "directory_label": "canonical/sources", "sha256": "cd" * 32, "size": 9, "file_id": 7}],
            "origins": [],
            "retrieval": {"schema_version": "1.0", "status": "token_required", "routes": []},
            "descriptor": {"id": "priv"},
        },
    },
}


def test_abi_version() -> None:
    assert core.abi_version()[0].isdigit()


def test_resolve_returns_contract() -> None:
    r = core.resolve(_INDEX, "pub")
    assert r["id"] == "pub"
    assert r["tier"] == "public"
    assert r["files"][0]["relpath"] == "canonical/sources/X.parquet"
    assert r["retrieval"]["status"] == "raw_reproducible"
    assert r["retrieval"]["routes"][0]["resources"][0]["selector"]["kind"] == "direct_url"


def test_resolve_unknown_raises_keyerror() -> None:
    with pytest.raises(KeyError):
        core.resolve(_INDEX, "nope")


def test_private_without_token_raises_runtimeerror_no_network(tmp_path) -> None:
    resolved = core.resolve(_INDEX, "priv")
    with pytest.raises(RuntimeError):
        core.fetch(resolved, {"cache_dir": str(tmp_path)})


def test_not_fetchable_raises_valueerror(tmp_path) -> None:
    resolved = core.resolve(_INDEX, "pub")  # public, no DOI, only a manual origin
    with pytest.raises(ValueError):
        core.fetch(resolved, {"cache_dir": str(tmp_path)})


def test_retrieve_raw_manual_route_raises_valueerror_no_network(tmp_path) -> None:
    request = {"dataset_id": "demo", "route": {"id": "manual", "method": "manual", "provider": "manual", "access": "manual", "locator": "https://example.org"}}
    with pytest.raises(ValueError):
        core.retrieve_raw(request, {"cache_dir": str(tmp_path)})


def test_verify_cached_missing_then_ok(tmp_path) -> None:
    body = b"hello"
    sha = hashlib.sha256(body).hexdigest()
    resolved = {
        "id": "demo",
        "tier": "public",
        "instance": "https://dv.example",
        "doi": None,
        "dataset_version": None,
        "files": [{"name": "X.parquet", "relpath": "canonical/sources/X.parquet", "directory_label": "canonical/sources", "sha256": sha, "size": len(body), "file_id": None}],
        "origins": [],
    }
    assert core.verify_cached(resolved, str(tmp_path))["files"][0]["status"] == "missing"
    p = tmp_path / "canonical" / "sources" / "X.parquet"
    p.parent.mkdir(parents=True)
    p.write_bytes(body)
    report = core.verify_cached(resolved, str(tmp_path))
    assert report["ok"] is True
    assert report["files"][0]["status"] == "ok"
