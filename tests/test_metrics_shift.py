"""Tests for the enriched descriptive metrics (effective rank, shift, NaN imputation)."""
from __future__ import annotations

import numpy as np

from nirs4all_datasets.qualify import metrics


def test_effective_rank_bounds() -> None:
    assert metrics.effective_rank([1.0, 0.0, 0.0]) == 1.0  # one dominant component
    er = metrics.effective_rank([1.0, 1.0, 1.0, 1.0])
    assert abs(er - 4.0) < 1e-9  # flat spectrum -> full participation
    assert metrics.effective_rank([]) is None
    assert metrics.effective_rank([float("nan"), -1.0]) is None


def test_impute_columns_preserves_rows_and_reports() -> None:
    x = np.array([[1.0, np.nan, 3.0], [3.0, 5.0, np.nan], [5.0, 7.0, 9.0]])
    filled, report = metrics.impute_columns(x)
    assert filled.shape == x.shape  # rows never dropped
    assert np.isfinite(filled).all()
    assert filled[0, 1] == 6.0  # column mean of {5,7}
    assert report == {"n_nan_cells": 2, "n_nan_rows": 2, "n_nan_columns": 2}


def test_impute_columns_uses_reference_means() -> None:
    ref = np.array([[10.0, 10.0], [20.0, 20.0]])
    x = np.array([[np.nan, 1.0]])
    filled, _ = metrics.impute_columns(x, reference=ref)
    assert filled[0, 0] == 15.0  # mean of the reference column, not of x


def test_impute_all_nan_column_becomes_zero() -> None:
    filled, report = metrics.impute_columns(np.array([[np.nan, 1.0], [np.nan, 2.0]]))
    assert (filled[:, 0] == 0.0).all()
    assert report["n_nan_columns"] == 1


def test_target_shift_regression() -> None:
    rng = np.random.RandomState(0)
    a = rng.normal(0, 1, 200)
    b = rng.normal(2, 1, 120)  # shifted +2 sigma
    out = metrics.target_shift(a, b)
    assert out["n_train"] == 200 and out["n_test"] == 120
    assert out["standardized_mean_diff"] > 1.0
    assert 0.0 <= out["ks_statistic"] <= 1.0
    assert out["wasserstein"] > 1.0


def test_target_shift_degenerate() -> None:
    assert metrics.target_shift([1.0], [2.0])["standardized_mean_diff"] is None


def test_class_shift_and_unseen() -> None:
    out = metrics.class_shift({"a": 10, "b": 10}, {"a": 5, "c": 5})
    assert out["n_classes"] == 3
    assert out["unseen_in_test"] == ["b"]  # b only in train
    assert out["unseen_in_train"] == ["c"]  # c only in test
    assert 0.0 <= out["jensen_shannon"] <= 1.0
    identical = metrics.class_shift({"a": 5, "b": 5}, {"a": 3, "b": 3})
    assert identical["jensen_shannon"] == 0.0 and identical["max_abs_proportion_delta"] == 0.0
