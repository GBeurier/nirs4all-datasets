"""Tests for the robustness fixes in the folder ingest path (NA, empty metadata, naming)."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

from nirs4all_datasets.ingest import _build_folder_config, _has_data_rows, resolve_config, write_canonical

pytest.importorskip("nirs4all")
from nirs4all.data import DatasetConfigs, SpectroDataset  # noqa: E402


def test_has_data_rows(tmp_path: Path) -> None:
    empty = tmp_path / "e.csv"
    empty.write_text("", encoding="utf-8")
    header_only = tmp_path / "h.csv"
    header_only.write_text("a;b;c\n", encoding="utf-8")
    full = tmp_path / "f.csv"
    full.write_text("a;b;c\n1;2;3\n", encoding="utf-8")
    assert not _has_data_rows(empty) and not _has_data_rows(header_only) and _has_data_rows(full)
    assert not _has_data_rows(tmp_path / "missing.csv")


def _leaf(path: Path, *, nan: bool = False, empty_meta: bool = False, cal_naming: bool = False) -> Path:
    path.mkdir(parents=True)
    xrow = "0.1;0.2;0.3" if not nan else "0.1;;0.3"  # empty middle cell -> NaN
    xname = "Xcal.csv" if cal_naming else "Xtrain.csv"
    yname = "Ycal.csv" if cal_naming else "Ytrain.csv"
    (path / xname).write_text(f"1100;1102;1104\n{xrow}\n0.2;0.3;0.4\n0.3;0.4;0.5\n", encoding="utf-8")
    (path / yname).write_text("Brix\n3.1\n3.2\n3.3\n", encoding="utf-8")
    if empty_meta:
        (path / "Mtrain.csv").write_text("", encoding="utf-8")
    return path


def test_build_folder_config_injects_na_policy_and_unit(tmp_path: Path) -> None:
    cfg, warns = _build_folder_config(_leaf(tmp_path / "d"), header_unit="nm", na_policy="ignore")
    assert cfg["train_x_params"]["na_policy"] == "ignore"
    assert cfg["train_x_params"]["header_unit"] == "nm"
    assert cfg["train_y_params"]["na_policy"] == "ignore"


def test_build_folder_config_drops_empty_metadata(tmp_path: Path) -> None:
    cfg, warns = _build_folder_config(_leaf(tmp_path / "d", empty_meta=True), header_unit="nm", na_policy="ignore")
    assert "train_group" not in cfg  # empty Mtrain.csv must not reach the loader
    assert any("metadata" in w for w in warns)


def test_nan_x_loads_with_ignore_policy(tmp_path: Path) -> None:
    cfg, _ = _build_folder_config(_leaf(tmp_path / "d", nan=True), header_unit="nm", na_policy="ignore")
    ds = DatasetConfigs(cfg).get_dataset_at(0)
    assert ds.num_samples == 3  # NaN row preserved, not dropped or aborted
    assert ds.has_nan


def test_cal_val_naming_recognized(tmp_path: Path) -> None:
    cfg, _ = _build_folder_config(_leaf(tmp_path / "d", cal_naming=True), header_unit="nm", na_policy="ignore")
    assert cfg.get("train_x") and cfg["train_x"].endswith("Xcal.csv")


def test_write_canonical_persists_na_policy(tmp_path: Path) -> None:
    ds = SpectroDataset("t")
    rng = np.random.RandomState(0)
    ds.add_samples(rng.rand(12, 5).astype("float32"), headers=[str(1000 + i) for i in range(5)], header_unit="nm")
    ds.add_targets(np.linspace(0.0, 1.0, 12))
    config, _hashes, _rows = write_canonical(ds, tmp_path)
    assert config["train_x_params"]["na_policy"] == "ignore"  # so build_card's reload never aborts on NaN
    assert config["train_y_params"]["na_policy"] == "ignore"
    # resolve_config keeps the params intact
    assert resolve_config(tmp_path)["train_x_params"]["na_policy"] == "ignore"
