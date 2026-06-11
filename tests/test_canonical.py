"""Tests for the canonical writer (id-keyed CSV -> per-source Parquet, sample-identity join)."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from nirs4all_datasets.bootstrap import build_descriptor_from_card
from nirs4all_datasets.canonical import build_canonical, resolve_config


def _build(leaf: Path, out: Path) -> tuple[Any, dict[str, Any]]:
    desc, _ = build_descriptor_from_card(leaf)
    res = build_canonical(leaf, desc, out)
    dataset_json = json.loads((out / "canonical" / "dataset.json").read_text())
    return res, dataset_json


def test_single_source(tmp_path: Path, v2_leaf: Any) -> None:
    leaf = v2_leaf(tmp_path / "src" / "ds_single", sample_of={"o1": "s1", "o2": "s2"})
    res, dj = _build(leaf, tmp_path / "out")
    assert res.status.value == "ok"
    assert [s["source_id"] for s in dj["sources"]] == ["X"]
    assert dj["join_key"] == "sample_id" and dj["variables"] is not None
    assert (tmp_path / "out" / "canonical" / "sources" / "X.parquet").exists()
    assert (tmp_path / "out" / "canonical" / "variables.parquet").exists()
    assert dj["splits"] == []


def test_multi_block(tmp_path: Path, v2_leaf: Any) -> None:
    leaf = v2_leaf(tmp_path / "src" / "ds_multi", blocks=("X1", "X2"), sample_of={"o1": "s1", "o2": "s2"})
    res, dj = _build(leaf, tmp_path / "out")
    assert res.status.value in ("ok", "partial")
    assert {s["source_id"] for s in dj["sources"]} == {"X1", "X2"}
    assert all((tmp_path / "out" / "canonical" / "sources" / f"{b}.parquet").exists() for b in ("X1", "X2"))


def test_asymmetric_sources_join_by_sample(tmp_path: Path, v2_leaf: Any) -> None:
    # X1 has 3 spectra, X2 has 2 — different sizes; aligned by sample_id, never by row position.
    leaf = v2_leaf(
        tmp_path / "src" / "ds_asym",
        blocks=("X1", "X2"),
        block_obs={"X1": ["o1", "o2", "o3"], "X2": ["o4", "o5"]},
        sample_of={"o1": "s1", "o2": "s1", "o3": "s1", "o4": "s2", "o5": "s2"},
    )
    res, dj = _build(leaf, tmp_path / "out")
    assert res.status.value in ("ok", "partial")  # must NOT crash on differing row counts
    assert res.row_counts.get("X1") == 3 and res.row_counts.get("X2") == 2
    assert res.row_counts.get("variables") == 2  # two samples s1, s2


def test_no_targets_omits_variables_when_empty(tmp_path: Path, v2_leaf: Any) -> None:
    leaf = v2_leaf(tmp_path / "src" / "ds_xonly", targets={})  # no Y columns, no extra M
    res, dj = _build(leaf, tmp_path / "out")
    assert res.status.value in ("ok", "partial")
    assert dj["variables"] is None
    assert not (tmp_path / "out" / "canonical" / "variables.parquet").exists()


def test_native_split_preserved(tmp_path: Path, v2_leaf: Any) -> None:
    leaf = v2_leaf(
        tmp_path / "src" / "ds_split",
        sample_of={"o1": "s1", "o2": "s2"},
        split={"o1": "calibration", "o2": "test"},
    )
    res, dj = _build(leaf, tmp_path / "out")
    assert [s["name"] for s in dj["splits"]] == ["original"]
    assert (tmp_path / "out" / "canonical" / "splits" / "original.parquet").exists()


def test_resolve_config_absolutizes(tmp_path: Path, v2_leaf: Any) -> None:
    leaf = v2_leaf(tmp_path / "src" / "ds_resolve", sample_of={"o1": "s1", "o2": "s2"})
    _build(leaf, tmp_path / "out")
    cfg = resolve_config(tmp_path / "out")
    for src in cfg["sources"]:
        assert Path(src["path"]).is_absolute() and Path(src["path"]).exists()


def test_organize_idempotent(tmp_path: Path, v2_leaf: Any) -> None:
    pytest.importorskip("pyarrow")
    from nirs4all_datasets.organize import organize

    leaf = v2_leaf(tmp_path / "src" / "ds_org", sample_of={"o1": "s1", "o2": "s2"})
    desc, _ = build_descriptor_from_card(leaf)
    datasets = tmp_path / "datasets"
    first = organize(leaf, desc, datasets, force=False)
    assert (datasets / "ds_org" / "canonical" / "dataset.json").exists()
    assert (datasets / "ds_org" / "manifest.json").exists()
    second = organize(leaf, desc, datasets, force=False)
    assert second.skipped  # unchanged inputs -> skipped (incremental)
