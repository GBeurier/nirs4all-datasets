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


def test_spectral_profile_contains_requested_metric_families() -> None:
    axis = np.linspace(900.0, 1700.0, 80)
    base = np.sin(np.linspace(0, 5, 80)) * 0.02 + 0.5
    spectra = np.vstack([base + i * 0.001 for i in range(12)])
    spectra[0, 30] += 0.4  # spike
    spectra[1, 45:] += 0.25  # jump
    profile = m.spectral_profile(spectra, axis, sample_ids=[f"s{i // 2}" for i in range(12)])

    assert profile["integrity"]["nan_ratio"] == 0.0
    assert profile["amplitude"]["peak_to_peak"] > 0
    assert profile["noise"]["snr"] is not None
    assert profile["artefacts"]["spike_count"] >= 1
    assert profile["artefacts"]["jump_count"] >= 1
    assert profile["outliers"]["pca_q_ratio"] is not None
    assert profile["reference"]["sam_to_mean_spectrum_p95"] is not None
    assert profile["reference"]["affine_residual_rms_p95"] is not None
    assert profile["reference"]["xcorr_lag_p95_features"] is not None
    assert profile["repeatability"]["n_repeat_groups"] == 6
    assert set(profile["profile_scores"]) == set(m.profile_score_labels())
    assert profile["diagnostics"]


def test_diagnostic_hypotheses_rank_splice_like_signature() -> None:
    profile = {
        "profile_scores": {
            "integrity_risk": 0.0,
            "noise_risk": 0.05,
            "local_artefact_risk": 0.95,
            "shape_drift": 0.1,
            "outlier_pressure": 0.9,
            "reference_spread": 0.7,
            "repeatability_risk": 0.2,
            "structure_complexity": 0.2,
        },
        "noise": {"snr_db": 45.0},
        "amplitude": {"mean_reflectance": 0.5, "peak_to_peak": 0.2},
        "shape": {"baseline_slope": 0.01},
        "artefacts": {"spike_rate": 0.03, "jump_rate": 0.04, "clip_fraction": 0.0},
        "outliers": {"pca_q_ratio": 15.0, "hotelling_t2_ratio": 4.0, "mahalanobis_h_ratio": 2.0},
        "reference": {"sam_to_mean_spectrum_p95": 0.25, "rms_to_mean_spectrum_p95": 0.1},
        "repeatability": {"sam_intra_id": 0.02, "rms_intra_id": 0.01, "cv_intra_id": 0.02},
        "structure": {"local_outlier_factor_p95": 1.2, "density_cv": 0.2},
    }
    labels = [d["key"] for d in m.diagnostic_hypotheses(profile, top_k=3)]
    assert "splice" in labels or "vera25_like" in labels


def test_metric_catalog_and_technology_guidance_are_public_tables() -> None:
    catalog = m.metric_catalog()
    assert {"family", "metric", "detects", "high", "low", "causes", "formula", "score_note"} <= set(catalog[0])
    assert any(row["metric"] == "PCA Q (SPE)" for row in catalog)
    guidance = m.technology_guidance()
    assert any(row["technology"].startswith("MIR") for row in guidance)
    bugs = m.bug_method_catalog()
    assert any(row["family"] == "Label bugs" for row in bugs)


def test_metric_score_rows_join_values_scores_and_interpretation() -> None:
    axis = np.linspace(900.0, 1700.0, 80)
    base = np.sin(np.linspace(0, 5, 80)) * 0.02 + 0.5
    spectra = np.vstack([base + i * 0.001 for i in range(12)])
    profile = m.spectral_profile(spectra, axis, sample_ids=[f"s{i // 2}" for i in range(12)])
    rows = m.metric_score_rows(profile)

    assert rows
    q = next(row for row in rows if row["key"] == "outliers.pca_q_ratio")
    assert q["value"] == profile["outliers"]["pca_q_ratio"]
    assert q["score"] is not None
    assert q["level"] in {"faible", "moyen", "fort"}
    assert q["interpretation"]
    assert q["formula"] and q["score_note"]


def test_pca_score_plot_and_spectral_target_correlation() -> None:
    axis = np.linspace(1000.0, 1800.0, 60)
    y = np.linspace(0.0, 1.0, 20)
    rng = np.random.RandomState(0)
    spectra = np.vstack([0.4 + target * np.exp(-((axis - 1400.0) ** 2) / 15000.0) for target in y])
    spectra += rng.normal(scale=0.03, size=spectra.shape)
    score_plot = m.pca_score_plot(spectra)
    assert score_plot is not None
    assert len(score_plot["points"]) == 20

    corr = m.spectral_target_correlation(spectra, y, axis)
    assert corr is not None
    assert corr["max_abs_corr"] > 0.8
    assert 1300.0 < corr["argmax_axis"] < 1500.0
    assert len(corr["curve"]["axis"]) <= 140
