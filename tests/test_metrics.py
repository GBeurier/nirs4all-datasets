"""Tests for the descriptive qualification metrics (pure, no nirs4all)."""
from __future__ import annotations

import numpy as np
import pytest

from nirs4all_datasets.qualify import metrics as m


def test_class_balance() -> None:
    balanced = m.class_balance([50, 50, 50])
    assert balanced["n_classes"] == 3
    assert balanced["normalized_entropy"] == pytest.approx(1.0)  # perfectly balanced
    assert balanced["imbalance_ratio"] == 1.0

    skewed = m.class_balance([90, 10])
    assert skewed["imbalance_ratio"] == 9.0
    assert 0.0 < skewed["normalized_entropy"] < 1.0  # type: ignore[operator]
    assert skewed["minority_fraction"] == 0.1

    assert m.class_balance([7])["normalized_entropy"] == 0.0  # single class guard
    assert m.class_balance([])["n_classes"] is None


def test_distribution_shape() -> None:
    rng = np.random.RandomState(0)
    normal = m.distribution_shape(rng.normal(size=2000))
    assert abs(normal["skewness"]) < 0.3  # type: ignore[arg-type]
    assert normal["is_normal"] is True

    skewed = m.distribution_shape(rng.exponential(size=2000))
    assert skewed["skewness"] > 0.5  # type: ignore[operator]

    small = m.distribution_shape([1.0, 2.0, 3.0, 4.0])  # n < 8
    assert small["normality_p"] is None and small["is_normal"] is None
    assert m.distribution_shape([5.0] * 10)["skewness"] is None  # constant -> degenerate


def test_spectral_quality_smooth_vs_noisy() -> None:
    base = np.linspace(0.0, 1.0, 200)
    smooth = np.tile(np.sin(base * 3), (30, 1))
    rng = np.random.RandomState(0)
    noisy = smooth + rng.normal(scale=0.2, size=smooth.shape)
    q_smooth = m.spectral_quality(smooth)
    q_noisy = m.spectral_quality(noisy)
    assert q_smooth["noise_proxy_db"] > q_noisy["noise_proxy_db"]  # type: ignore[operator]
    assert q_smooth["smoothness"] < q_noisy["smoothness"]  # type: ignore[operator]
    assert m.spectral_quality(np.zeros((1, 2)))["noise_proxy_db"] is None  # too few features


def test_wavelength_spacing() -> None:
    uniform = m.wavelength_spacing(np.arange(1000.0, 1100.0, 2.0))
    assert uniform["is_uniform"] is True
    assert uniform["mean"] == 2.0

    non_uniform = m.wavelength_spacing([1000.0, 1002.0, 1010.0, 1030.0])
    assert non_uniform["is_uniform"] is False
    assert m.wavelength_spacing([1000.0])["mean"] is None
