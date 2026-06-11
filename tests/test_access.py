"""Tests for the access layer: local resolution real, remote fetch mocked (no network)."""
from __future__ import annotations

from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

import pytest
import yaml

from nirs4all_datasets import schema as s
from nirs4all_datasets.access import canonical_file_ids, canonical_registry, default_cache_dir, fetch_from_origin, fetch_private, fetch_public, get
from nirs4all_datasets.config import Settings
from nirs4all_datasets.manifest import sha256_bytes
from nirs4all_datasets.schema import DatasetDescriptor

_HASH = "a" * 64


def _manifest() -> s.Manifest:
    """A manifest with one raw + two canonical files (one with a Dataverse file id)."""
    files = [
        {"path": "raw/a.opus", "role": "raw", "sha256": "b" * 64, "size": 1},
        {"path": "canonical/sources/X.parquet", "role": "canonical", "sha256": "c" * 64, "size": 2, "file_id": 11},
        {"path": "canonical/dataset.json", "role": "canonical", "sha256": "d" * 64, "size": 3, "file_id": 12},
    ]
    return s.Manifest(dataset_id="corn", processing_hash=_HASH, converter_name="c", converter_version="1", files=files)


def _write_descriptor(root: Path, descriptor: DatasetDescriptor) -> None:
    """Write ``<root>/catalog/datasets/<id>.yaml`` for the access resolver to find."""
    descriptors = root / "catalog" / "datasets"
    descriptors.mkdir(parents=True, exist_ok=True)
    (descriptors / f"{descriptor.id}.yaml").write_text(yaml.safe_dump(descriptor.model_dump(mode="json", exclude_none=True)), encoding="utf-8")


def _build_local(root: Path, v2_leaf: Any, tmp_path: Path, name: str = "corn", **leaf_kwargs: Any) -> DatasetDescriptor:
    """Build a real catalog entry under ``root``: canonical bytes + a descriptor YAML."""
    from nirs4all_datasets.bootstrap import build_descriptor_from_card
    from nirs4all_datasets.organize import organize

    leaf = v2_leaf(tmp_path / "src" / name, **leaf_kwargs)
    descriptor, _ = build_descriptor_from_card(leaf)
    organize(leaf, descriptor, root / "datasets")
    _write_descriptor(root, descriptor)
    return descriptor


# =============================================================================
# Fetch primitives + registries (no network; mocked sessions / pooch)
# =============================================================================
def test_default_cache_dir() -> None:
    pytest.importorskip("pooch")
    assert isinstance(default_cache_dir(), Path)


def test_canonical_registry_and_file_ids() -> None:
    manifest = _manifest()
    assert canonical_registry(manifest) == {"X.parquet": "c" * 64, "dataset.json": "d" * 64}
    assert canonical_file_ids(manifest) == {"X.parquet": 11, "dataset.json": 12}


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


# =============================================================================
# fetch_from_origin (open canonical DOI only; raw / manual / script never auto-fetched)
# =============================================================================
def _origin_descriptor(*origins: s.OriginSource) -> DatasetDescriptor:
    return DatasetDescriptor(
        id="corn",
        name="Corn",
        description="x",
        sources=[s.Source(source_id="X")],
        provenance=s.Provenance(contributor="L"),
        governance=s.Governance(license="CC-BY-4.0"),
        origin_sources=list(origins),
    )


def test_fetch_from_origin_canonical_verifies_against_manifest(tmp_path: Path, monkeypatch: Any) -> None:
    desc = _origin_descriptor(s.OriginSource(kind="zenodo", mode="canonical", locator="10.5281/zenodo.9", access="open"))
    seen: dict[str, Any] = {}
    monkeypatch.setattr("nirs4all_datasets.access.fetch_public", lambda doi, reg, cache: seen.update(doi=doi, reg=reg) or {})
    out = fetch_from_origin("corn", desc, _manifest(), cache_dir=tmp_path)
    assert out == tmp_path / "corn"
    assert seen["doi"] == "10.5281/zenodo.9"
    assert seen["reg"] == canonical_registry(_manifest())  # verified against the manifest, not the source


def test_fetch_from_origin_skips_raw_manual_and_script(tmp_path: Path) -> None:
    desc = _origin_descriptor(
        s.OriginSource(kind="script", mode="raw", locator="scripts/corn.py", access="open"),
        s.OriginSource(kind="url", mode="raw", locator="https://example.org/x.zip", access="manual"),
        s.OriginSource(kind="zenodo", mode="raw", locator="10.5281/zenodo.9", access="open"),  # raw-mode origin: re-ingestion, not byte-identical
    )
    assert fetch_from_origin("corn", desc, _manifest(), cache_dir=tmp_path) is None


# =============================================================================
# get() — local-first, forwarding, the token gate, and unknown names
# =============================================================================
def test_get_local_first_returns_nirsdataset(tmp_path: Path, v2_leaf: Any, monkeypatch: Any) -> None:
    root = tmp_path / "root"
    _build_local(root, v2_leaf, tmp_path, "corn", blocks=("X1", "X2"), sample_of={"o1": "s1", "o2": "s2"}, public=True)
    # any fetch attempt is a test failure: a present canonical dir must load with no network.
    monkeypatch.setattr("nirs4all_datasets.access.fetch_public", lambda *a, **k: pytest.fail("must not fetch when local present"))
    monkeypatch.setattr("nirs4all_datasets.access.fetch_private", lambda *a, **k: pytest.fail("must not fetch when local present"))
    ds = get("corn", root=root)
    assert ds.id == "corn"
    assert ds.sources() == ["X1", "X2"]


def test_get_forwards_source_and_split(tmp_path: Path, v2_leaf: Any) -> None:
    root = tmp_path / "root"
    _build_local(root, v2_leaf, tmp_path, "mono", blocks=("X",), sample_of=None, split={"o1": "cal", "o2": "val"}, public=True)
    ds = get("mono", root=root, source="X", split="original")
    assert ds.sources() == ["X"]
    # invalid source / split are validated at the boundary.
    with pytest.raises(KeyError):
        get("mono", root=root, source="NOPE")
    with pytest.raises(KeyError):
        get("mono", root=root, split="ghost")


def test_get_private_without_token_raises_before_any_fetch(tmp_path: Path, v2_leaf: Any, monkeypatch: Any) -> None:
    root = tmp_path / "root"
    descriptor = _build_local(root, v2_leaf, tmp_path, "priv", blocks=("X",), sample_of=None)  # non-public -> private tier
    assert descriptor.tier is s.Tier.PRIVATE
    # Pin a Dataverse DOI so resolution reaches the personal-DOI branch (where the token gate lives),
    # then remove the local canonical bytes so it is not served locally.
    import shutil

    shutil.rmtree(root / "datasets" / "priv" / "canonical")
    raw = yaml.safe_load((root / "catalog" / "datasets" / "priv.yaml").read_text())
    raw["dataverse"] = {"instance": "https://dv.example", "doi": "10.70112/ABC"}
    (root / "catalog" / "datasets" / "priv.yaml").write_text(yaml.safe_dump(raw), encoding="utf-8")

    # No token anywhere: explicit None, no env var, tokenless settings -> the gate must fire BEFORE fetch.
    monkeypatch.delenv("NIRS4ALL_DATAVERSE_TOKEN", raising=False)
    monkeypatch.setattr("nirs4all_datasets.config.get_settings", lambda **k: Settings(instance="https://dv.example", token=None))
    monkeypatch.setattr("nirs4all_datasets.access.fetch_public", lambda *a, **k: pytest.fail("must not fetch without a token"))
    monkeypatch.setattr("nirs4all_datasets.access.fetch_private", lambda *a, **k: pytest.fail("must not fetch without a token"))
    monkeypatch.setattr("nirs4all_datasets.access.fetch_by_doi", lambda *a, **k: pytest.fail("must not fetch without a token"))

    with pytest.raises(RuntimeError, match="token is required"):
        get("priv", root=root)


def test_get_private_with_token_calls_fetch_by_doi(tmp_path: Path, v2_leaf: Any, monkeypatch: Any) -> None:
    root = tmp_path / "root"
    _build_local(root, v2_leaf, tmp_path, "priv", blocks=("X",), sample_of=None)
    import shutil

    shutil.rmtree(root / "datasets" / "priv" / "canonical")
    raw = yaml.safe_load((root / "catalog" / "datasets" / "priv.yaml").read_text())
    raw["dataverse"] = {"instance": "https://dv.example", "doi": "10.70112/ABC"}
    (root / "catalog" / "datasets" / "priv.yaml").write_text(yaml.safe_dump(raw), encoding="utf-8")

    rec: dict[str, Any] = {}

    def _fake_fetch_by_doi(dataset_id: str, doi: str, manifest: Any, **kwargs: Any) -> Path:
        rec.update(dataset_id=dataset_id, doi=doi, token=kwargs.get("token"))
        return root / "datasets" / "priv"  # _wrap is mocked below, so the bytes need not exist

    # fetch_by_doi is only reached WITH a token -> assert the explicit token flowed through.
    monkeypatch.setattr("nirs4all_datasets.access.fetch_by_doi", _fake_fetch_by_doi)
    monkeypatch.setattr("nirs4all_datasets.access._wrap", lambda d, desc, **k: f"WRAPPED:{Path(d).name}")

    out = get("priv", root=root, token="EXPLICIT", instance="https://dv.example")
    assert rec["dataset_id"] == "priv"
    assert rec["doi"] == "10.70112/ABC"
    assert rec["token"] == "EXPLICIT"
    assert out == "WRAPPED:priv"


def test_get_unknown_name_raises_filenotfound(tmp_path: Path) -> None:
    root = tmp_path / "root"
    (root / "catalog" / "datasets").mkdir(parents=True)
    with pytest.raises(FileNotFoundError):
        get("ghost", root=root)


def test_get_no_doi_no_local_guides_to_origin_sources(tmp_path: Path, v2_leaf: Any) -> None:
    # A public dataset with no DOI and only a manual origin cannot be auto-fetched -> actionable error.
    root = tmp_path / "root"
    _build_local(root, v2_leaf, tmp_path, "pub", blocks=("X",), sample_of=None, public=True)
    import shutil

    shutil.rmtree(root / "datasets" / "pub" / "canonical")
    raw = yaml.safe_load((root / "catalog" / "datasets" / "pub.yaml").read_text())
    raw["origin_sources"] = [{"kind": "url", "mode": "raw", "locator": "https://esdac.example/lucas", "access": "manual"}]
    (root / "catalog" / "datasets" / "pub.yaml").write_text(yaml.safe_dump(raw), encoding="utf-8")
    with pytest.raises(ValueError, match="origin source"):
        get("pub", root=root)


def test_public_api_is_exposed() -> None:
    import nirs4all_datasets as n4ad

    assert all(callable(getattr(n4ad, fn)) for fn in ("get", "list", "card"))
