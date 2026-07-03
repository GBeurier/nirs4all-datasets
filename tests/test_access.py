"""Tests for the access layer: local resolution real, remote fetch mocked (no network).

The download itself lives in the native core (covered by `tests/test_acquire.py` and the Rust unit
tests); here we test `get()`'s *policy*: local-first, the token gate, actionable origin errors, and
that a resolved contract with a token is handed to the core.
"""
from __future__ import annotations

import sys
import types
from pathlib import Path
from typing import Any

import pytest
import yaml

from nirs4all_datasets import schema as s
from nirs4all_datasets.access import _has_fetchable_origin, _resolved_contract, get
from nirs4all_datasets.config import Settings
from nirs4all_datasets.schema import DatasetDescriptor


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


def _pin_doi(root: Path, name: str, doi: str = "10.70112/ABC") -> None:
    """Drop the local canonical bytes and pin a Dataverse DOI (forces a remote-fetch path)."""
    import shutil

    shutil.rmtree(root / "datasets" / name / "canonical")
    path = root / "catalog" / "datasets" / f"{name}.yaml"
    raw = yaml.safe_load(path.read_text())
    raw["dataverse"] = {"instance": "https://dv.example", "doi": doi}
    path.write_text(yaml.safe_dump(raw), encoding="utf-8")


def _fake_acquire(monkeypatch: Any, fetch: Any) -> None:
    """Install a fake acquisition module for access-policy tests.

    The native `_n4ds` extension is tested separately; these tests should not
    need it just to assert local-first and token-gate policy.
    """
    import nirs4all_datasets

    module = types.ModuleType("nirs4all_datasets._acquire")
    module.fetch = fetch
    monkeypatch.setitem(sys.modules, "nirs4all_datasets._acquire", module)
    monkeypatch.setattr(nirs4all_datasets, "_acquire", module, raising=False)


# =============================================================================
# Contract building + fetchable-origin policy (no network)
# =============================================================================
def test_has_fetchable_origin() -> None:
    desc = DatasetDescriptor(
        id="corn", name="Corn", description="x",
        sources=[s.Source(source_id="X")], provenance=s.Provenance(contributor="L"), governance=s.Governance(license="CC-BY-4.0"),
        origin_sources=[
            s.OriginSource(kind="script", mode="raw", locator="scripts/corn.py", access="open"),
            s.OriginSource(kind="url", mode="raw", locator="https://example.org/x.zip", access="manual"),
            s.OriginSource(kind="zenodo", mode="raw", locator="10.5281/zenodo.9", access="open"),  # raw mode: re-ingestion, not byte-identical
        ],
    )
    assert _has_fetchable_origin(desc) is False  # none is open + canonical + DOI
    desc.origin_sources.append(s.OriginSource(kind="zenodo", mode="canonical", locator="10.5281/zenodo.9", access="open"))
    assert _has_fetchable_origin(desc) is True


def test_resolved_contract_carries_files_and_pin(tmp_path: Path, v2_leaf: Any) -> None:
    root = tmp_path / "root"
    descriptor = _build_local(root, v2_leaf, tmp_path, "corn", blocks=("X",), sample_of=None, public=True)
    contract = _resolved_contract(root, descriptor)
    assert contract["id"] == "corn"
    assert contract["tier"] == "public"
    assert any(f["relpath"].endswith("X.parquet") for f in contract["files"])  # canonical files from the manifest


# =============================================================================
# get() — local-first, forwarding, the token gate, and unknown names
# =============================================================================
def test_get_local_first_returns_nirsdataset(tmp_path: Path, v2_leaf: Any, monkeypatch: Any) -> None:
    root = tmp_path / "root"
    _build_local(root, v2_leaf, tmp_path, "corn", blocks=("X1", "X2"), sample_of={"o1": "s1", "o2": "s2"}, public=True)
    # any fetch attempt is a test failure: a present canonical dir must load with no network.
    _fake_acquire(monkeypatch, lambda *a, **k: pytest.fail("must not fetch when local present"))
    ds = get("corn", root=root)
    assert ds.id == "corn"
    assert ds.sources() == ["X1", "X2"]


def test_get_local_reference_dataset_loads_through_io_package_bridge(tmp_path: Path, v2_leaf: Any) -> None:
    nirs4all_io = pytest.importorskip("nirs4all_io")
    if not callable(getattr(nirs4all_io, "to_dataset_package", None)):
        pytest.skip("installed nirs4all_io does not expose DatasetPackage support")

    root = tmp_path / "root"
    _build_local(
        root,
        v2_leaf,
        tmp_path,
        "bridge",
        blocks=("X1", "X2"),
        block_obs={"X1": ["o1", "o2"], "X2": ["p1", "p2"]},
        sample_of={"o1": "s1", "o2": "s2", "p1": "s1", "p2": "s2"},
        targets={"Moisture": "numeric"},
        extra_meta=("site",),
        public=True,
    )

    package = nirs4all_io.load(get("bridge", root=root), target="dataset_package")
    block = package.to_assembled().blocks["train"]

    assert len(block.X) == 2
    assert block.feature_headers == [["1100", "1102"], ["1100", "1102"]]
    assert block.y_headers == ["Moisture"]
    assert block.metadata["site"].tolist() == ["meta", "meta"]


def test_get_forwards_source_and_split(tmp_path: Path, v2_leaf: Any) -> None:
    root = tmp_path / "root"
    _build_local(root, v2_leaf, tmp_path, "mono", blocks=("X",), sample_of=None, split={"o1": "cal", "o2": "val"}, public=True)
    ds = get("mono", root=root, source="X", split="original")
    assert ds.sources() == ["X"]
    with pytest.raises(KeyError):
        get("mono", root=root, source="NOPE")
    with pytest.raises(KeyError):
        get("mono", root=root, split="ghost")


def test_get_private_without_token_raises_before_any_fetch(tmp_path: Path, v2_leaf: Any, monkeypatch: Any) -> None:
    root = tmp_path / "root"
    descriptor = _build_local(root, v2_leaf, tmp_path, "priv", blocks=("X",), sample_of=None)  # non-public -> private tier
    assert descriptor.tier is s.Tier.PRIVATE
    _pin_doi(root, "priv")

    monkeypatch.delenv("NIRS4ALL_DATAVERSE_TOKEN", raising=False)
    monkeypatch.setattr("nirs4all_datasets.config.get_settings", lambda **k: Settings(instance="https://dv.example", token=None))
    _fake_acquire(monkeypatch, lambda *a, **k: pytest.fail("must not fetch without a token"))

    with pytest.raises(RuntimeError, match="token is required"):
        get("priv", root=root)


def test_get_private_with_token_hands_contract_to_core(tmp_path: Path, v2_leaf: Any, monkeypatch: Any) -> None:
    root = tmp_path / "root"
    _build_local(root, v2_leaf, tmp_path, "priv", blocks=("X",), sample_of=None)
    _pin_doi(root, "priv")

    rec: dict[str, Any] = {}

    def _fake_fetch(contract: dict[str, Any], opts: dict[str, Any]) -> dict[str, Any]:
        rec.update(doi=contract["doi"], token=opts.get("token"), instance=opts.get("instance"))
        return {"dir": str(root / "datasets" / "priv"), "files": []}

    _fake_acquire(monkeypatch, _fake_fetch)
    monkeypatch.setattr("nirs4all_datasets.access._wrap", lambda d, desc, **k: f"WRAPPED:{Path(d).name}")

    out = get("priv", root=root, token="EXPLICIT", instance="https://dv.example")
    assert rec == {"doi": "10.70112/ABC", "token": "EXPLICIT", "instance": "https://dv.example"}
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
