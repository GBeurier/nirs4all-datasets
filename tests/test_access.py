"""Tests for the access layer (local load real; remote fetch mocked, no network)."""
from __future__ import annotations

from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

import numpy as np
import pytest
import yaml

from nirs4all_datasets import schema as s
from nirs4all_datasets.access import canonical_file_ids, canonical_registry, fetch_private, fetch_public, load, load_local
from nirs4all_datasets.manifest import sha256_bytes, write_manifest

_HASH = "a" * 64


def _manifest() -> s.Manifest:
    files = [
        {"path": "raw/a.opus", "role": "raw", "sha256": "b" * 64, "size": 1},
        {"path": "canonical/X.parquet", "role": "canonical", "sha256": "c" * 64, "size": 2, "file_id": 11},
        {"path": "canonical/nirs4all_config.json", "role": "canonical", "sha256": "d" * 64, "size": 3, "file_id": 12},
    ]
    return s.Manifest(dataset_id="corn", descriptor_hash=_HASH, converter_name="c", converter_version="1", files=files)


def test_canonical_registry_and_file_ids() -> None:
    manifest = _manifest()
    assert canonical_registry(manifest) == {"X.parquet": "c" * 64, "nirs4all_config.json": "d" * 64}
    assert canonical_file_ids(manifest) == {"X.parquet": 11, "nirs4all_config.json": 12}


def test_fetch_public_uses_doi_and_sha256_registry(tmp_path: Path) -> None:
    pytest.importorskip("pooch")
    fake_pup = MagicMock()
    fake_pup.fetch.side_effect = lambda name: str(tmp_path / name)
    with patch("pooch.create", return_value=fake_pup) as create:
        out = fetch_public("doi:10.70112/ABC", {"X.parquet": "c" * 64}, tmp_path)  # doi: prefix is normalized
    kwargs = create.call_args.kwargs
    assert kwargs["base_url"] == "doi:10.70112/ABC/"
    assert kwargs["registry"] == {"X.parquet": "sha256:" + "c" * 64}
    assert out["X.parquet"] == tmp_path / "X.parquet"


def test_fetch_private_downloads_and_verifies(tmp_path: Path) -> None:
    content = b"parquet-bytes"
    registry = {"X.parquet": sha256_bytes(content)}
    session = MagicMock()
    resp = MagicMock()
    resp.ok = True
    resp.is_redirect = False
    resp.content = content
    session.get.return_value = resp

    out = fetch_private({"X.parquet": 11}, registry, tmp_path, instance="https://dv.example", token="TKN", session=session)

    args, kwargs = session.get.call_args
    assert args[0] == "https://dv.example/api/access/datafile/11"
    assert kwargs["headers"] == {"X-Dataverse-key": "TKN"}
    assert out["X.parquet"].read_bytes() == content


def test_fetch_private_rejects_checksum_mismatch(tmp_path: Path) -> None:
    session = MagicMock()
    resp = MagicMock()
    resp.ok = True
    resp.is_redirect = False
    resp.content = b"wrong-bytes"
    session.get.return_value = resp
    with pytest.raises(RuntimeError, match="checksum mismatch"):
        fetch_private({"X.parquet": 11}, {"X.parquet": _HASH}, tmp_path, instance="https://dv.example", token="TKN", session=session)


def _write_registry(tmp_path: Path, *, visibility: str = "public", doi: str | None = "10.70112/ABC", local: bool = False) -> Path:
    """A minimal registry: one descriptor + manifest, optionally with local canonical data."""
    (tmp_path / "catalog" / "datasets").mkdir(parents=True)
    descriptor = {
        "id": "corn", "name": "Corn", "version": "1.0.0", "description": "x",
        "instrument": {"modality": "NIR"}, "targets": [{"name": "y", "task_type": "regression"}],
        "provenance": {"contributor": "Lab"},
        "governance": {
            "license": "CC-BY-4.0", "visibility": visibility,
            "confidentiality_class": "public" if visibility == "public" else "internal",
            "owner_steward": "L", "redistribution_rights": "r", "consent_ethics_status": "n/a",
            "anonymization_status": "n/a", "permitted_use": "r", "access_policy": "o",
        },
        "dataverse": ({"doi": doi} if doi else {}),
    }
    (tmp_path / "catalog" / "datasets" / "corn.yaml").write_text(yaml.safe_dump(descriptor), encoding="utf-8")
    dataset_dir = tmp_path / "datasets" / "corn"
    dataset_dir.mkdir(parents=True)
    write_manifest(_manifest(), dataset_dir / "manifest.json")
    if local:
        (dataset_dir / "canonical").mkdir()
        (dataset_dir / "canonical" / "nirs4all_config.json").write_text("{}", encoding="utf-8")
    return tmp_path


def test_load_prefers_local_canonical(tmp_path: Path, monkeypatch: Any) -> None:
    root = _write_registry(tmp_path, local=True)
    seen: dict[str, Path] = {}
    monkeypatch.setattr("nirs4all_datasets.access.load_local", lambda d: seen.setdefault("dir", Path(d)))
    monkeypatch.setattr("nirs4all_datasets.access.fetch_and_load", lambda *a, **k: pytest.fail("must not fetch when local present"))
    load("corn", root=root)
    assert seen["dir"] == root / "datasets" / "corn"


def test_load_public_fetches_by_doi_without_token(tmp_path: Path, monkeypatch: Any) -> None:
    root = _write_registry(tmp_path, visibility="public", local=False)
    rec: dict[str, Any] = {}
    monkeypatch.setattr("nirs4all_datasets.access.fetch_and_load", lambda name, doi, manifest, **k: rec.update(name=name, doi=doi, token=k.get("token")))
    load("corn", root=root)
    assert rec["name"] == "corn" and rec["doi"] == "10.70112/ABC" and rec["token"] is None


def test_load_restricted_resolves_token_from_settings(tmp_path: Path, monkeypatch: Any) -> None:
    root = _write_registry(tmp_path, visibility="restricted", local=False)
    rec: dict[str, Any] = {}
    monkeypatch.setattr("nirs4all_datasets.access.fetch_and_load", lambda name, doi, manifest, **k: rec.update(token=k.get("token")))
    monkeypatch.setenv("NIRS4ALL_DATAVERSE_TOKEN", "TKN-XYZ")
    load("corn", root=root)
    assert rec["token"] == "TKN-XYZ"


def test_load_explicit_token_wins(tmp_path: Path, monkeypatch: Any) -> None:
    root = _write_registry(tmp_path, visibility="restricted", local=False)
    rec: dict[str, Any] = {}
    monkeypatch.setattr("nirs4all_datasets.access.fetch_and_load", lambda name, doi, manifest, **k: rec.update(token=k.get("token")))
    load("corn", root=root, token="EXPLICIT")
    assert rec["token"] == "EXPLICIT"


def test_load_unpublished_without_local_raises(tmp_path: Path) -> None:
    root = _write_registry(tmp_path, doi=None, local=False)
    with pytest.raises(ValueError, match="not published"):
        load("corn", root=root)


def test_public_api_is_exposed() -> None:
    import nirs4all_datasets as n4ad

    assert all(callable(getattr(n4ad, fn)) for fn in ("load", "load_local", "list", "card"))


def test_load_local_round_trip(tmp_path: Path) -> None:
    pytest.importorskip("nirs4all")
    from nirs4all.data import SpectroDataset

    from nirs4all_datasets.ingest import write_canonical

    ds = SpectroDataset("tiny")
    ds.add_samples(np.random.RandomState(0).rand(15, 5).astype("float32"), headers=[str(1000 + i) for i in range(5)], header_unit="nm")
    ds.add_targets(np.linspace(0.0, 1.0, 15))
    write_canonical(ds, tmp_path)
    try:
        loaded = load_local(tmp_path).get_dataset_at(0)
    except Exception as exc:  # noqa: BLE001
        if "categorical_mode" in str(exc):
            pytest.skip("requires the nirs4all ParquetLoader fix")
        raise
    assert loaded.num_samples == 15
