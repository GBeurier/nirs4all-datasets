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


def test_named_spectral_blocks_and_missing_y(tmp_path: Path, v2_leaf: Any) -> None:
    leaf = v2_leaf(tmp_path / "ds", blocks=("X_reflectance", "X_absorbance"), targets={})
    (leaf / "Y.csv").unlink()
    res, config = _build(leaf, tmp_path / "out")
    assert res.status.value == "ok"
    assert {source["source_id"] for source in config["sources"]} == {"X_reflectance", "X_absorbance"}


def test_sample_ids_preserve_leading_zero_and_missing_falls_back(tmp_path: Path, v2_leaf: Any) -> None:
    import pandas as pd

    leaf = v2_leaf(tmp_path / "ds", sample_of={"o1": "001", "o2": ""})
    res, _ = _build(leaf, tmp_path / "out")
    source = pd.read_parquet(res.canonical_dir / "sources" / "X.parquet")
    assert source["sample_id"].tolist() == ["001", "o2"]
    assert any("identity sample_id" in warning for warning in res.warnings)


def test_categorical_codes_keep_leading_zeros(tmp_path: Path, v2_leaf: Any) -> None:
    import pandas as pd

    leaf = v2_leaf(tmp_path / "ds", targets={"variety": "categorical"})
    (leaf / "Y.csv").write_text("observation_id;variety\no1;001\no2;002\n")
    res, _ = _build(leaf, tmp_path / "out")
    variables = pd.read_parquet(res.canonical_dir / "variables.parquet")
    assert variables["variety"].tolist() == ["001", "002"]


def test_single_column_target_preserves_commas(tmp_path: Path, v2_leaf: Any) -> None:
    import pandas as pd

    leaf = v2_leaf(tmp_path / "ds", targets={"compound": "categorical"})
    (leaf / "Y.csv").write_text("compound\n1,3-dimethyl\n2,4-dimethyl\n")
    res, _ = _build(leaf, tmp_path / "out")
    variables = pd.read_parquet(res.canonical_dir / "variables.parquet")
    assert variables["compound"].tolist() == ["1,3-dimethyl", "2,4-dimethyl"]


def test_semicolon_metadata_with_comma_rich_values(tmp_path: Path, v2_leaf: Any) -> None:
    import pandas as pd

    leaf = v2_leaf(tmp_path / "ds", sample_of={"o1": "s1", "o2": "s2"}, extra_meta=("notes",))
    m = leaf / "M.csv"
    m.write_text("dataset_id;observation_id;sample_id;notes\nds;o1;s1;one,two,three,four\nds;o2;s2;five,six,seven,eight\n")
    res, _ = _build(leaf, tmp_path / "out")
    variables = pd.read_parquet(res.canonical_dir / "variables.parquet")
    assert variables["sample_id"].tolist() == ["s1", "s2"]
    assert variables["notes"].tolist() == ["one,two,three,four", "five,six,seven,eight"]


def test_keyless_paired_targets_use_verified_metadata_ids(tmp_path: Path, v2_leaf: Any) -> None:
    import pandas as pd

    leaf = v2_leaf(tmp_path / "ds", targets={"moisture": "numeric"}, sample_of={"o1": "s1", "o2": "s2"})
    (leaf / "Y.csv").write_text("moisture\n11.1\n14.0\n")
    desc, _ = build_descriptor_from_card(leaf)
    assert any("Y row pairing is not independently verified" in w for w in desc.provenance.warnings)
    res, _ = _build(leaf, tmp_path / "out")
    variables = pd.read_parquet(res.canonical_dir / "variables.parquet").set_index("sample_id")
    assert variables.loc["s1", "moisture"] == 11.1
    assert variables.loc["s2", "moisture"] == 14.0
    assert any("assumed Y/M row pairing" in w and "matches X.csv" in w for w in res.warnings)


def test_keyless_targets_reject_unverified_order(tmp_path: Path, v2_leaf: Any) -> None:
    leaf = v2_leaf(tmp_path / "ds", targets={"moisture": "numeric"}, sample_of={"o1": "s1", "o2": "s2"})
    (leaf / "Y.csv").write_text("moisture\n11.1\n14.0\n")
    x = leaf / "X.csv"
    lines = x.read_text().splitlines()
    x.write_text("\n".join([lines[0], *reversed(lines[1:])]) + "\n")
    res, _ = _build(leaf, tmp_path / "out")
    assert any("cannot be verified; skipping targets" in w for w in res.warnings)


def test_different_metadata_with_same_target_name_is_preserved(tmp_path: Path, v2_leaf: Any) -> None:
    import pandas as pd

    leaf = v2_leaf(tmp_path / "ds", targets={"treatment": "categorical"}, extra_meta=("treatment",))
    (leaf / "Y.csv").write_text("treatment\n0\n1\n")
    m_path = leaf / "M.csv"
    m = pd.read_csv(m_path, sep=";")
    m["treatment"] = ["control", "treated"]
    m.to_csv(m_path, sep=";", index=False)
    desc, _ = build_descriptor_from_card(leaf)
    assert any(v.name == "metadata_treatment" and v.role.value == "metadata" for v in desc.variables)
    res = build_canonical(leaf, desc, tmp_path / "out")
    variables = pd.read_parquet(res.canonical_dir / "variables.parquet")
    assert variables["treatment"].tolist() == ["0", "1"]
    assert variables["metadata_treatment"].tolist() == ["control", "treated"]


def test_asymmetric_sources_join_by_sample(tmp_path: Path, v2_leaf: Any) -> None:
    # X1 has 3 spectra, X2 has 2 — different sizes; aligned by sample_id, never by row position.
    leaf = v2_leaf(
        tmp_path / "src" / "ds_asym",
        blocks=("X1", "X2"),
        block_obs={"X1": ["o1", "o2", "o3"], "X2": ["o4", "o5"]},
        sample_of={"o1": "s1", "o2": "s1", "o3": "s1", "o4": "s2", "o5": "s2"},
    )
    (leaf / "Y.csv").write_text("observation_id;Moisture;variety\no1;1;A\no2;1;A\no3;1;A\no4;2;B\no5;2;B\n")
    res, dj = _build(leaf, tmp_path / "out")
    assert res.status.value in ("ok", "partial")  # must NOT crash on differing row counts
    assert res.row_counts.get("X1") == 3 and res.row_counts.get("X2") == 2
    assert res.row_counts.get("variables") == 2  # two samples s1, s2


def test_conflicting_sample_values_keep_each_observation_and_original_sample(tmp_path: Path, v2_leaf: Any) -> None:
    import pandas as pd

    leaf = v2_leaf(tmp_path / "ds", sample_of={"o1": "same", "o2": "same"}, extra_meta=("region",))
    desc, warnings = build_descriptor_from_card(leaf)
    assert desc.ids.sample_id == "observation_id" and not desc.ids.sample_id_available
    assert any("original physical-sample key" in w for w in warnings)
    assert any(v.name == "original_sample_id" for v in desc.metadata_variables)
    res = build_canonical(leaf, desc, tmp_path / "out")
    values = pd.read_parquet(res.canonical_dir / "variables.parquet")
    assert values["sample_id"].tolist() == ["o1", "o2"]
    assert values["original_sample_id"].tolist() == ["same", "same"]
    assert values["Moisture"].tolist() == [1.0, 1.5]
    source = pd.read_parquet(res.canonical_dir / "sources" / "X.parquet")
    assert source["sample_id"].tolist() == ["o1", "o2"]


def test_conflicting_multisource_keeps_sample_alignment_guard(tmp_path: Path, v2_leaf: Any) -> None:
    leaf = v2_leaf(tmp_path / "ds", blocks=("X1", "X2"), sample_of={"o1": "same", "o2": "same"})
    desc, _ = build_descriptor_from_card(leaf)
    assert desc.ids.sample_id == "observation_id"
    assert desc.alignment_level.value == "sample"


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
