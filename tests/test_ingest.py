"""Tests for ingest / canonical-form writing and the nirs4all round-trip."""
from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np
import pytest

from nirs4all_datasets.ingest import _write_table, ingest, resolve_config, write_canonical

pytest.importorskip("nirs4all")
from nirs4all.data import DatasetConfigs, SpectroDataset  # noqa: E402


def _tiny_dataset(n: int = 20, f: int = 6) -> SpectroDataset:
    ds = SpectroDataset("tiny")
    rng = np.random.RandomState(0)
    x = rng.rand(n, f).astype("float32")
    headers = [str(1000 + 10 * i) for i in range(f)]
    ds.add_samples(x, headers=headers, header_unit="nm")
    ds.add_targets(np.linspace(0.0, 1.0, n))
    return ds


def _sample_regression() -> Path | None:
    candidates: list[Path] = []
    spec = importlib.util.find_spec("nirs4all")
    if spec and spec.origin:
        pkg = Path(spec.origin).parent
        candidates += [pkg.parent / "examples" / "sample_data" / "regression", pkg / "examples" / "sample_data" / "regression"]
    candidates.append(Path("/home/delete/nirs4all/nirs4all/examples/sample_data/regression"))
    return next((c for c in candidates if c.is_dir()), None)


def _maybe_skip_parquet(exc: Exception) -> None:
    if "categorical_mode" in str(exc):
        pytest.skip("requires the nirs4all ParquetLoader fix (drop loading-meta params before pd.read_parquet)")


def test_write_canonical_no_split(tmp_path: Path) -> None:
    config, hashes, rows = write_canonical(_tiny_dataset(), tmp_path)
    assert (tmp_path / "canonical" / "X.parquet").exists()
    assert (tmp_path / "canonical" / "nirs4all_config.json").exists()
    assert config["train_x"] == "canonical/X.parquet"
    assert "test_x" not in config
    assert rows["all"] == 20
    assert set(hashes) == {"X.parquet", "Y.parquet"}


def test_canonical_round_trip_via_resolve_config(tmp_path: Path) -> None:
    write_canonical(_tiny_dataset(), tmp_path)
    cfg = resolve_config(tmp_path)
    assert Path(cfg["train_x"]).is_absolute()
    try:
        ds = DatasetConfigs(cfg).get_dataset_at(0)
    except Exception as exc:  # noqa: BLE001
        _maybe_skip_parquet(exc)
        raise
    n_features = ds.num_features if isinstance(ds.num_features, int) else ds.num_features[0]
    assert ds.num_samples == 20
    assert n_features == 6
    assert ds.task_type is not None and ds.task_type.value == "regression"


def test_multisource_round_trip(tmp_path: Path) -> None:
    ds = SpectroDataset("ms")
    rng = np.random.RandomState(0)
    ds.add_samples(
        [rng.rand(20, 5).astype("float32"), rng.rand(20, 7).astype("float32")],
        headers=[[str(1000 + i) for i in range(5)], [str(2000 + i) for i in range(7)]],
        header_unit=["nm", "nm"],
    )
    ds.add_targets(np.linspace(0.0, 1.0, 20))
    config, _hashes, _rows = write_canonical(ds, tmp_path)
    assert isinstance(config["train_x"], list) and len(config["train_x"]) == 2
    try:
        loaded = DatasetConfigs(resolve_config(tmp_path)).get_dataset_at(0)
    except Exception as exc:  # noqa: BLE001
        _maybe_skip_parquet(exc)
        raise
    assert loaded.n_sources == 2
    assert list(loaded.num_features) == [5, 7]


def test_targetless_round_trip(tmp_path: Path) -> None:
    ds = SpectroDataset("tl")
    rng = np.random.RandomState(0)
    ds.add_samples(rng.rand(15, 5).astype("float32"), headers=[str(1000 + i) for i in range(5)], header_unit="nm")
    config, _hashes, _rows = write_canonical(ds, tmp_path)
    assert "train_y" not in config
    try:
        loaded = DatasetConfigs(resolve_config(tmp_path)).get_dataset_at(0)
    except Exception as exc:  # noqa: BLE001
        _maybe_skip_parquet(exc)
        raise
    assert loaded.num_samples == 15


def test_classification_round_trip(tmp_path: Path) -> None:
    ds = SpectroDataset("clf")
    rng = np.random.RandomState(0)
    ds.add_samples(rng.rand(30, 6).astype("float32"), headers=[str(1000 + 10 * i) for i in range(6)], header_unit="nm")
    ds.add_targets(np.array([0, 1, 2] * 10))  # 3 classes
    config, _hashes, _rows = write_canonical(ds, tmp_path)
    assert config["task_type"] == "multiclass_classification"
    try:
        loaded = DatasetConfigs(resolve_config(tmp_path)).get_dataset_at(0)
    except Exception as exc:  # noqa: BLE001
        if "categorical_mode" in str(exc):
            pytest.skip("requires the nirs4all ParquetLoader fix")
        raise
    assert loaded.is_classification
    assert loaded.num_classes == 3


def test_binary_classification_round_trip(tmp_path: Path) -> None:
    ds = SpectroDataset("bin")
    rng = np.random.RandomState(1)
    ds.add_samples(rng.rand(24, 5).astype("float32"), headers=[str(1000 + i) for i in range(5)], header_unit="nm")
    ds.add_targets(np.array([0, 1] * 12))
    config, _hashes, _rows = write_canonical(ds, tmp_path)
    assert config["task_type"] == "binary_classification"
    try:
        loaded = DatasetConfigs(resolve_config(tmp_path)).get_dataset_at(0)
    except Exception as exc:  # noqa: BLE001
        _maybe_skip_parquet(exc)
        raise
    assert loaded.is_classification and loaded.num_classes == 2


def test_task_type_override_forces_regression(tmp_path: Path) -> None:
    ds = SpectroDataset("ord")
    rng = np.random.RandomState(2)
    ds.add_samples(rng.rand(30, 5).astype("float32"), headers=[str(1000 + i) for i in range(5)], header_unit="nm")
    ds.add_targets(np.array([0, 1, 2] * 10))  # integer labels would auto-detect as classification
    config, _hashes, _rows = write_canonical(ds, tmp_path, task_type="regression")
    assert config["task_type"] == "regression"
    try:
        loaded = DatasetConfigs(resolve_config(tmp_path)).get_dataset_at(0)
    except Exception as exc:  # noqa: BLE001
        _maybe_skip_parquet(exc)
        raise
    assert loaded.is_regression


def test_write_table_validates_headers(tmp_path: Path) -> None:
    arr = np.zeros((3, 2), dtype="float32")
    with pytest.raises(ValueError):
        _write_table(arr, ["a", "a"], tmp_path / "dup.parquet")
    with pytest.raises(ValueError):
        _write_table(arr, ["a"], tmp_path / "short.parquet")


def test_target_names_mismatch_raises(tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        write_canonical(_tiny_dataset(), tmp_path, target_names=["a", "b"])


def test_split_round_trip_on_sample_data(tmp_path: Path) -> None:
    sample = _sample_regression()
    if sample is None:
        pytest.skip("sample_data/regression not found")
    res = ingest(sample, tmp_path)
    assert res.status.value in {"ok", "partial"}
    assert {"train", "test"} <= set(res.row_counts)
    assert (tmp_path / "canonical" / "Xtrain.parquet").exists()
    try:
        ds = DatasetConfigs(resolve_config(tmp_path)).get_dataset_at(0)
    except Exception as exc:  # noqa: BLE001
        _maybe_skip_parquet(exc)
        raise
    assert ds.num_samples == res.n_samples
