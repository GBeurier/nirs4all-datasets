"""Descriptive metrics that fill the gaps nirs4all does not expose for a dataset card.

Descriptive adapters and statistics (no nirs4all import or I/O). Roughness delegates lazily to
Methods; unavailable native support remains explicit. Each returns a JSON-serializable
dict with a stable key set (``None`` values for degenerate input), so the card schema is constant.

Definitions are deliberately documented and conservative:

* class balance uses normalized Shannon entropy and the max/min imbalance ratio;
* distribution shape reports skewness/excess-kurtosis and a D'Agostino normality p-value that is
  *descriptive only* (never a quality gate);
* ``noise_proxy_db`` is a high-frequency smoothness/noise proxy from the spectral second difference
  (NOT an instrument SNR), with the MAD normal-scaled (x1.4826);
* wavelength spacing summarizes the sampling grid;
* ``spectral_profile`` groups integrity / amplitude / noise / artefact / PCA / reference /
  repeatability metrics into a dataset-property explorer profile.
"""
from __future__ import annotations

import math
import warnings
from collections.abc import Iterable, Mapping
from copy import deepcopy
from typing import Any, cast

import numpy as np
from scipy import stats
from scipy.integrate import trapezoid
from scipy.spatial.distance import jensenshannon

_CLASS_KEYS = ("n_classes", "normalized_entropy", "imbalance_ratio", "gini_simpson", "minority_fraction")
_SHAPE_KEYS = ("n", "skewness", "kurtosis", "normality_p", "is_normal")
_QUALITY_KEYS = ("noise_proxy_db", "smoothness", "dynamic_range", "saturation_fraction")
_SPACING_KEYS = ("mean", "std", "min", "max", "median", "is_uniform")
_TARGET_SHIFT_KEYS = ("n_train", "n_test", "mean_train", "mean_test", "std_train", "std_test", "standardized_mean_diff", "ks_statistic", "ks_p", "wasserstein")
_CLASS_SHIFT_KEYS = ("n_classes", "max_abs_proportion_delta", "jensen_shannon", "unseen_in_test", "unseen_in_train")
_INTEGRITY_KEYS = ("nan_ratio", "inf_count", "finite_ratio", "zero_ratio", "zero_column_ratio")
_AMPLITUDE_KEYS = ("mean_reflectance", "area_under_curve", "peak_to_peak", "variance")
_NOISE_KEYS = ("noise_rms", "snr", "snr_db", "bandwise_snr_min", "bandwise_snr_median", "worst_band_index", "worst_band_axis")
_ARTEFACT_KEYS = ("spike_count", "spike_rate", "jump_count", "jump_rate", "clip_fraction")
_SHAPE_SPECTRAL_KEYS = ("baseline_slope", "curvature_rms", "d1_rms", "edge_noise_ratio")
_PCA_OUTLIER_KEYS = (
    "pca_q_median",
    "pca_q_p95",
    "pca_q_max",
    "pca_q_ratio",
    "hotelling_t2_median",
    "hotelling_t2_p95",
    "hotelling_t2_max",
    "hotelling_t2_ratio",
    "mahalanobis_h_median",
    "mahalanobis_h_p95",
    "mahalanobis_h_max",
    "mahalanobis_h_ratio",
)
_REFERENCE_KEYS = (
    "rms_to_mean_spectrum",
    "rms_to_mean_spectrum_p95",
    "sam_to_mean_spectrum",
    "sam_to_mean_spectrum_p95",
    "affine_offset_median",
    "affine_offset_p95_abs",
    "affine_gain_median",
    "affine_gain_p95_abs_delta",
    "affine_residual_rms_median",
    "affine_residual_rms_p95",
    "peak_position_std",
    "xcorr_lag_p95_features",
    "xcorr_lag_p95_axis",
)
_REPEATABILITY_KEYS = ("n_repeat_groups", "rms_intra_id", "sam_intra_id", "cv_intra_id", "distance_to_centroid_p95")
_STRUCTURE_KEYS = ("pca_score_density", "local_outlier_factor_p95", "isolation_forest_score_p95", "density_cv")
# Explicit compatibility aliases: these are roughness/distance proxies, not
# repeat-measured instrument SNR or the density-reachability Local Outlier Factor.
LEGACY_METRIC_ALIASES = {
    "noise.noise_rms": "noise.roughness_sigma_proxy",
    "noise.snr": "noise.roughness_signal_to_noise_proxy",
    "noise.snr_db": "noise.roughness_signal_to_noise_proxy_db",
    "noise.bandwise_snr_min": "noise.bandwise_roughness_signal_to_noise_proxy_min",
    "noise.bandwise_snr_median": "noise.bandwise_roughness_signal_to_noise_proxy_median",
    "structure.local_outlier_factor_p95": "structure.knn_distance_ratio_p95",
}


_PROFILE_SCORE_KEYS = (
    "integrity_risk",
    "noise_risk",
    "local_artefact_risk",
    "shape_drift",
    "outlier_pressure",
    "reference_spread",
    "repeatability_risk",
    "structure_complexity",
)

_PROFILE_LABELS = {
    "integrity_risk": "Integrity",
    "noise_risk": "Noise",
    "local_artefact_risk": "Local artifacts",
    "shape_drift": "Baseline/shape",
    "outlier_pressure": "PCA outliers",
    "reference_spread": "Distance to average spectrum",
    "repeatability_risk": "Repeatability",
    "structure_complexity": "Multi-regime structure",
}

_METRIC_CATALOG: list[dict[str, str]] = [
    {"family": "Data integrity", "metric": "Invalid/masked cell count (owner report)", "key": "integrity.missing_cells", "detects": "Null or masked cells in the evaluated population", "high": "To investigate", "low": "Complete according to the declared mask", "causes": "Missing data or validity mask; not evidence of an acquisition cause"},
    {"family": "Data integrity", "metric": "NaN ratio", "key": "integrity.nan_ratio", "detects": "Missing data", "high": "Corrupted spectrum", "low": "Full spectrum", "causes": "Acquisition/export error"},
    {"family": "Data integrity", "metric": "Inf count", "key": "integrity.inf_count", "detects": "Infinite values", "high": "Corruption", "low": "Normal", "causes": "Invalid calculations"},
    {"family": "Data integrity", "metric": "Zero ratio", "key": "integrity.zero_ratio", "detects": "Null columns or cells", "high": "Truncated spectrum", "low": "Normal", "causes": "Export, saturation"},
    {"family": "Overall amplitude", "metric": "Mean reflectance", "key": "amplitude.mean_reflectance", "detects": "Average level", "high": "Too light / background visible", "low": "Too dark", "causes": "Background, geometry"},
    {"family": "Overall amplitude", "metric": "Area under curve", "key": "amplitude.area_under_curve", "detects": "Overall intensity", "high": "Illumination difference", "low": "Normal", "causes": "Probe distance"},
    {"family": "Overall amplitude", "metric": "Peak-to-peak (PTP)", "key": "amplitude.peak_to_peak", "detects": "Dynamic range", "high": "Strong variability", "low": "Flat spectrum", "causes": "Saturation"},
    {"family": "Overall amplitude", "metric": "Variance", "key": "amplitude.variance", "detects": "Spectral variability", "high": "Normal or heterogeneous", "low": "Flat spectrum", "causes": "Bad contact"},
    {"family": "Noise", "metric": "Roughness sigma proxy", "key": "noise.noise_rms", "detects": "High frequency noise", "high": "Noisy", "low": "Stable", "causes": "Lamp, detector"},
    {"family": "Noise", "metric": "Roughness S/N proxy", "key": "noise.snr", "detects": "Signal quality", "high": "Good signal", "low": "Bad signal", "causes": "Acquisition"},
    {"family": "Noise", "metric": "Bandwise roughness S/N proxy", "key": "noise.bandwise_snr_min", "detects": "Localized noise", "high": "Reliable zone", "low": "Problem area", "causes": "Detector"},
    {"family": "Local artifacts", "metric": "Spike count", "key": "artefacts.spike_count", "detects": "Narrow peaks", "high": "Artifacts", "low": "Clean spectrum", "causes": "Cosmic rays, splice"},
    {"family": "Local artifacts", "metric": "Spike rate", "key": "artefacts.spike_rate", "detects": "Peak density", "high": "Suspicious spectrum", "low": "Normal", "causes": "Interpolation"},
    {"family": "Local artifacts", "metric": "Jump count", "key": "artefacts.jump_count", "detects": "Discontinuities", "high": "Detector connection", "low": "Continuous", "causes": "Splice"},
    {"family": "Local artifacts", "metric": "Jump rate", "key": "artefacts.jump_rate", "detects": "Jump frequency", "high": "Spectral problem", "low": "Normal", "causes": "Calibration"},
    {"family": "Local artifacts", "metric": "Clip fraction", "key": "artefacts.clip_fraction", "detects": "Saturation", "high": "Clipping", "low": "Normal", "causes": "Detector saturated"},
    {"family": "Spectral form", "metric": "Baseline slope", "key": "shape.baseline_slope", "detects": "Overall slope", "high": "Drift", "low": "Stable", "causes": "Illumination"},
    {"family": "Spectral form", "metric": "Curvature RMS", "key": "shape.curvature_rms", "detects": "Curvature", "high": "Unusual shape", "low": "Smooth", "causes": "Background, splice"},
    {"family": "Spectral form", "metric": "D1 RMS", "key": "shape.d1_rms", "detects": "Local variability", "high": "Structured spectrum", "low": "Flat", "causes": "Biology or artifact"},
    {"family": "Multivariate outliers", "metric": "PCA Q (SPE)", "key": "outliers.pca_q_ratio", "detects": "Not explained by PCA", "high": "Atypical spectrum", "low": "Compliant", "causes": "Artifact, mixture"},
    {"family": "Multivariate outliers", "metric": "Hotelling T²", "key": "outliers.hotelling_t2_ratio", "detects": "Extreme in PCA", "high": "Extreme but consistent", "low": "Central", "causes": "Natural variability"},
    {"family": "Multivariate outliers", "metric": "Mahalanobis H", "key": "outliers.mahalanobis_h_ratio", "detects": "Distance to cloud", "high": "Global outlier", "low": "Normal population", "causes": "Different domain"},
    {"family": "Comparison to average spectrum", "metric": "RMS to mean spectrum", "key": "reference.rms_to_mean_spectrum_p95", "detects": "Average distance", "high": "Different spectrum", "low": "Typical", "causes": "Domain shift"},
    {"family": "Comparison to average spectrum", "metric": "Spectral Angle Mapper (SAM)", "key": "reference.sam_to_mean_spectrum_p95", "detects": "Difference in shape", "high": "Different shape", "low": "Similar", "causes": "Background, geometry"},
    {"family": "Repeatability", "metric": "RMS intra-ID", "key": "repeatability.rms_intra_id", "detects": "Reproducibility", "high": "Poor repeatability", "low": "Stable", "causes": "Positioning"},
    {"family": "Repeatability", "metric": "SAM intra-ID", "key": "repeatability.sam_intra_id", "detects": "Shape variation", "high": "Unstable", "low": "Stable", "causes": "Acquisition"},
    {"family": "Repeatability", "metric": "CV intra-ID", "key": "repeatability.cv_intra_id", "detects": "Internal variability", "high": "Bad control", "low": "Stable", "causes": "Operator"},
    {"family": "Structure of the dataset", "metric": "PCA score density", "key": "structure.pca_score_density", "detects": "Clusters", "high": "Subpopulations", "low": "Homogeneous", "causes": "Different batches"},
    {"family": "Structure of the dataset", "metric": "kNN distance ratio (not LOF)", "key": "structure.local_outlier_factor_p95", "detects": "Local anomaly", "high": "Isolated spectrum", "low": "Normal population", "causes": "Rare cases"},
    {"family": "Structure of the dataset", "metric": "Isolation Forest score", "key": "structure.isolation_forest_score_p95", "detects": "Global anomaly", "high": "Atypical spectrum", "low": "Normal", "causes": "Various causes"},
]

_TECHNOLOGY_GUIDANCE: list[dict[str, str]] = [
    {"technology": "UV-Vis 300-1000 nm", "adaptations": "Baseline, overall slope, drift at edges 300-350 and 900-1000; metrics by zones", "anomalies": "Stray light, bad white, saturation, weak signal at the ends", "comment": "The edges are often unstable; also calculate edge/middle scores."},
    {"technology": "UV-Vis 300-1000 nm", "adaptations": "Saturation / clipping near max absorbance or max reflectance", "anomalies": "Signal clipped", "comment": "Very important if strong absorption."},
    {"technology": "UV-Vis 300-1000 nm", "adaptations": "Red-edge, peak position, band ratios for vegetation", "anomalies": "Biological shift or optical artifact", "comment": "Helps distinguish real change from acquisition problem."},
    {"technology": "UV-Vis 300-1000 nm", "adaptations": "Smoothness / roughness index", "anomalies": "High frequency noise", "comment": "Often more informative than the SNR alone."},
    {"technology": "MIR / ATR-FTIR", "adaptations": "ATR contact quality index: overall intensity, total area, depth of key bands", "anomalies": "Poor crystal-sample contact", "comment": "Crucial: many anomalies come from the ATR contact."},
    {"technology": "MIR / ATR-FTIR", "adaptations": "CO2 / H2O atmospheric bands", "anomalies": "Bad atmospheric correction", "comment": "Frequent spurious peaks."},
    {"technology": "MIR / ATR-FTIR", "adaptations": "Baseline curvature / rubber-band residual", "anomalies": "Diffusion, contact, baseline drift", "comment": "Very useful before PCA."},
    {"technology": "MIR / ATR-FTIR", "adaptations": "Peak position shift", "anomalies": "Bad spectral alignment/calibration", "comment": "Important in FTIR because small shifts count."},
    {"technology": "MIR / ATR-FTIR", "adaptations": "Band area ratios on known bands", "anomalies": "Chemically incoherent spectrum", "comment": "To be adapted by matrix: polysaccharides, proteins, lipids, etc."},
    {"technology": "HS-MS", "adaptations": "Total Ion Current (TIC), Base Peak Intensity (BPI)", "anomalies": "Weak injection, unstable ionization", "comment": "MS equivalent of the global spectral level."},
    {"technology": "HS-MS", "adaptations": "Number of peaks detected", "anomalies": "Poor or too noisy spectrum", "comment": "Too little = bad signal; too much = noise/contamination."},
    {"technology": "HS-MS", "adaptations": "Mass accuracy / m/z drift", "anomalies": "Mass calibration problem", "comment": "Fundamental in HRMS."},
    {"technology": "HS-MS", "adaptations": "Retention time drift if LC/GC-MS", "anomalies": "Chromatographic drift", "comment": "Monitor on standards/QC pools."},
    {"technology": "HS-MS", "adaptations": "Blank contamination score", "anomalies": "Contaminants / carry-over", "comment": "Compare samples vs blanks."},
    {"technology": "HS-MS", "adaptations": "Internal standard CV", "anomalies": "Instrumental variability", "comment": "Very robust if standards available."},
    {"technology": "HS-MS", "adaptations": "Missingness by feature", "anomalies": "Detection instability", "comment": "Crucial for filtering variables."},
    {"technology": "With repetitions", "adaptations": "Intra-sample RMS", "anomalies": "Overall repeatability", "comment": "Applicable to all technologies."},
    {"technology": "With repetitions", "adaptations": "SAM / intra-sample correlation", "anomalies": "Shape repeatability", "comment": "Very useful for spectra."},
    {"technology": "With repetitions", "adaptations": "Intra-sample CV per band / feature", "anomalies": "Local repeatability", "comment": "Detects unstable areas."},
    {"technology": "With repetitions", "adaptations": "ICC or variance components", "anomalies": "Share of sample vs. technical variance", "comment": "Very useful if several repetitions per sample."},
    {"technology": "With repetitions", "adaptations": "Distance to intra-ID centroid", "anomalies": "Aberrant repetition", "comment": "Allows you to flag the bad repetition rather than the entire sample."},
]

_BUG_METHODS: list[dict[str, str]] = [
    {"family": "Global spectral shift", "methods": "Inter-dataset average spectrum correlation, DTW, cross-correlation, comparison of peak positions", "detects": "Wavelength shift, misalignment, different interpolation", "status": "Partially calculated: cross-correlation lag and dispersion of peak positions vs. average spectrum."},
    {"family": "Baseline / offset / gain", "methods": "Regression each spectrum vs average spectrum: x = a + b ref + residual; followed by a, b, residual RMS", "detects": "Additive offset, multiplicative effect, baseline drift", "status": "Calculated in reference.affine_*."},
    {"family": "Row mixing / X-M-Y mismatch", "methods": "Index check, row hash, ID duplication, intra-ID spectral distance, inconsistent labels", "detects": "Mixed up rows, misaligned metadata, Y assigned to wrong spectrum", "status": "Partially covered by intra-ID repeatability; checks index/hash to add to the canonical pipeline."},
    {"family": "Information leak / poorly split repetitions", "methods": "GroupKFold by sample_id vs StratifiedKFold random; auditing partitions by sample_id", "detects": "Artificially good performance due to repetitions", "status": "Requires splits and benchmark model; not calculated by the descriptive card."},
    {"family": "Label bugs", "methods": "Close samples in X but different Y, confident learning, systematic FP/FN errors", "detects": "Inverted Y, input errors, ambiguous classes", "status": "Requires Y and/or model; recommended for supervised explorer."},
    {"family": "Hidden subdomains", "methods": "PCA/UMAP/t-SNE + unsupervised clustering + association with dataset/Y/date/operator", "detects": "Batches, campaigns, probes, backgrounds not provided", "status": "Partially calculated by PCA and distance ratio kNN (not LOF); UMAP/t-SNE outside the static card."},
    {"family": "Unknown localized artifacts", "methods": "Wavelength x dataset map: mean difference, variance difference, KS per wavelength", "detects": "Unanticipated anomalous spectral regions", "status": "To be calculated at the bank level when several datasets share a spectral axis."},
    {"family": "Instrumental breaks", "methods": "Discontinuities in derivatives, changepoint detection", "detects": "Splice, detector connection, local jump not provided", "status": "Calculated by jump/spike rates; more advanced changepoint to add."},
    {"family": "Spectral mixing/contamination", "methods": "NMF / unmixing / reconstruction by convex hull", "detects": "External component: background, plastic, soil", "status": "Not calculated automatically; requires component assumptions or large library."},
    {"family": "Unstable but predictive features", "methods": "Model importance vs. QC instability by variable", "detects": "Model that learns an artifact rather than a biological signal", "status": "Requires supervised model; recommended for benchmark reporting."},
]

_METRIC_FORMULAS: dict[str, str] = {
    "integrity.missing_cells": "Native Preflight count of cells unavailable under x/null and valid_mask; denominator stays in native_metric.denominators.n_cells. Not legacy NaN ratio.",
    "integrity.nan_ratio": "count(isnan(X)) / X.size",
    "integrity.inf_count": "count(isinf(X))",
    "integrity.zero_ratio": "count(X == 0) / count(finite X)",
    "amplitude.mean_reflectance": "mean(X finite)",
    "amplitude.area_under_curve": "trapezoid(mean_spectrum, spectral_axis)",
    "amplitude.peak_to_peak": "max(mean_spectrum) - min(mean_spectrum)",
    "amplitude.variance": "var(X finite)",
    "noise.noise_rms": "median MAD(second derivative) * 1.4826 / sqrt(6)",
    "noise.snr": "mean(abs(X)) / noise_rms",
    "noise.bandwise_snr_min": "min(abs(mean_spectrum) / local second-derivative noise)",
    "artefacts.spike_count": "count robust outliers in second derivative",
    "artefacts.spike_rate": "spike_count / (n_samples * (n_features - 2))",
    "artefacts.jump_count": "count robust outliers in first derivative",
    "artefacts.jump_rate": "jump_count / (n_samples * (n_features - 1))",
    "artefacts.clip_fraction": "fraction of finite cells equal to repeated min/max extrema",
    "shape.baseline_slope": "linear slope of mean_spectrum over normalized axis",
    "shape.curvature_rms": "median RMS(second derivative per spectrum)",
    "shape.d1_rms": "median RMS(first derivative per spectrum)",
    "outliers.pca_q_ratio": "p95(Q/SPE residual) / median(Q/SPE residual)",
    "outliers.hotelling_t2_ratio": "p95(Hotelling T2) / median(Hotelling T2)",
    "outliers.mahalanobis_h_ratio": "p95(sqrt(T2)) / median(sqrt(T2))",
    "reference.rms_to_mean_spectrum_p95": "p95 RMS distance to dataset mean spectrum",
    "reference.sam_to_mean_spectrum_p95": "p95 spectral angle to dataset mean spectrum",
    "repeatability.rms_intra_id": "median RMS distance to repeated-sample centroid",
    "repeatability.sam_intra_id": "median SAM to repeated-sample centroid",
    "repeatability.cv_intra_id": "median within-ID band CV",
    "structure.pca_score_density": "1 / median kNN distance in PCA score space",
    "structure.local_outlier_factor_p95": "p95(mean kNN distance / median population mean kNN distance) in PCA-score space; not LOF",
    "structure.isolation_forest_score_p95": "p95 IsolationForest anomaly score on PCA scores",
}

_METRIC_SCORE_NOTES: dict[str, str] = {
    "integrity.nan_ratio": "alert = min(1, nan_ratio / 0.05)",
    "integrity.inf_count": "alert = min(1, inf_count / 1)",
    "integrity.zero_ratio": "alert = min(1, zero_ratio / 0.05)",
    "amplitude.mean_reflectance": "alert reuses baseline/shape drift because absolute reflectance ranges are technology-dependent",
    "amplitude.area_under_curve": "alert reuses baseline/shape drift because area scale depends on axis and units",
    "amplitude.peak_to_peak": "alert increases when dynamic range is abnormally flat",
    "amplitude.variance": "alert increases when variance/dynamic range is abnormally flat",
    "noise.noise_rms": "alert = noise_rms / signal_scale, saturated at 5%",
    "noise.snr": "alert decreases with SNR dB; >=40 dB is treated as low alert",
    "noise.bandwise_snr_min": "alert decreases with worst-band SNR dB; >=35 dB is treated as low alert",
    "artefacts.spike_count": "alert follows spike_rate, saturated at 1%",
    "artefacts.spike_rate": "alert = min(1, spike_rate / 0.01)",
    "artefacts.jump_count": "alert follows jump_rate, saturated at 1%",
    "artefacts.jump_rate": "alert = min(1, jump_rate / 0.01)",
    "artefacts.clip_fraction": "alert = min(1, clip_fraction / 0.01)",
    "shape.baseline_slope": "alert = abs(slope / signal_scale), saturated at 0.5",
    "shape.curvature_rms": "alert = curvature_rms / signal_scale, saturated at 1%",
    "shape.d1_rms": "alert = d1_rms / signal_scale, saturated at 5%",
    "outliers.pca_q_ratio": "alert = min(1, pca_q_ratio / 8)",
    "outliers.hotelling_t2_ratio": "alert = min(1, hotelling_t2_ratio / 8)",
    "outliers.mahalanobis_h_ratio": "alert = min(1, mahalanobis_h_ratio / 4)",
    "reference.rms_to_mean_spectrum_p95": "alert = RMS_p95 / signal_scale, saturated at 25%",
    "reference.sam_to_mean_spectrum_p95": "alert = min(1, SAM_p95 / 0.35 rad)",
    "repeatability.rms_intra_id": "alert = RMS_intra_ID / signal_scale, saturated at 10%",
    "repeatability.sam_intra_id": "alert = min(1, SAM_intra_ID / 0.15 rad)",
    "repeatability.cv_intra_id": "alert = min(1, CV_intra_ID / 0.25)",
    "structure.pca_score_density": "alert follows density_cv/profile structure complexity, not raw density alone",
    "structure.local_outlier_factor_p95": "alert = min(1, max(0, kNN_distance_ratio_p95 - 1) / 2)",
    "structure.isolation_forest_score_p95": "alert follows structure complexity; raw score is implementation-dependent",
}

_METRIC_RISK_WHEN: dict[str, str] = {
    "noise.snr": "low",
    "noise.bandwise_snr_min": "low",
    "amplitude.mean_reflectance": "extreme",
    "amplitude.area_under_curve": "extreme",
    "amplitude.peak_to_peak": "low",
    "amplitude.variance": "low",
    "structure.pca_score_density": "heterogeneous",
}


def _nulls(keys: tuple[str, ...]) -> dict[str, object]:
    return dict.fromkeys(keys, None)


def _as_2d_float(x: object) -> np.ndarray:
    arr = np.asarray(x, dtype="float64")
    if arr.ndim != 2:
        return np.empty((0, 0), dtype="float64")
    return arr


def _finite_matrix(x: object) -> np.ndarray:
    arr = _as_2d_float(x).copy()
    if arr.size:
        arr[~np.isfinite(arr)] = np.nan
    return arr


def _axis(axis: object, n_features: int) -> np.ndarray:
    ax = np.asarray(axis, dtype="float64").ravel() if axis is not None else np.arange(n_features, dtype="float64")
    if ax.size != n_features or not np.isfinite(ax).all():
        return np.arange(n_features, dtype="float64")
    return ax


def _safe_nanmean(arr: np.ndarray, axis: int | None = None) -> np.ndarray | float:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        return cast(np.ndarray | float, np.nanmean(arr, axis=axis))


def _safe_nanstd(arr: np.ndarray, axis: int | None = None) -> np.ndarray | float:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        return cast(np.ndarray | float, np.nanstd(arr, axis=axis))


def _safe_nanpercentile(arr: np.ndarray, q: float, axis: int | None = None) -> np.ndarray | float:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        return cast(np.ndarray | float, np.nanpercentile(arr, q, axis=axis))


def _finite_values(arr: np.ndarray) -> np.ndarray:
    return cast(np.ndarray, arr[np.isfinite(arr)])


def _finite_float(value: Any) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    value_f = float(value)
    return value_f if math.isfinite(value_f) else None


def _ratio(value: Any, denominator: Any, *, scale: float = 1.0) -> float | None:
    if isinstance(value, bool) or isinstance(denominator, bool):
        return None
    if not isinstance(value, (int, float)) or not isinstance(denominator, (int, float)):
        return None
    if not math.isfinite(float(value)) or not math.isfinite(float(denominator)) or float(denominator) <= 0:
        return None
    return float(value) / float(denominator) * scale


def _saturate(v: Any, scale: float = 1.0) -> float | None:
    if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(float(v)):
        return None
    if scale <= 0:
        scale = 1.0
    return float(max(0.0, min(1.0, abs(float(v)) / scale)))


def _p95_over_median(values: np.ndarray) -> float | None:
    vals = _finite_values(values)
    if vals.size < 2:
        return None
    med = float(np.median(vals))
    p95 = float(np.percentile(vals, 95))
    return p95 / med if med > 0 else None


def _robust_outlier_mask(rows: np.ndarray, *, threshold: float = 8.0) -> np.ndarray:
    """Row-wise robust outlier mask using MAD, with std fallback when MAD is zero."""
    if rows.ndim != 2 or rows.size == 0:
        return np.zeros_like(rows, dtype=bool)
    out = np.zeros(rows.shape, dtype=bool)
    for i, row in enumerate(rows):
        finite = np.isfinite(row)
        vals = row[finite]
        if vals.size < 3:
            continue
        med = float(np.median(vals))
        mad = float(np.median(np.abs(vals - med))) * 1.4826
        scale = mad if mad > 0 else float(np.std(vals, ddof=1)) if vals.size > 1 else 0.0
        if scale <= 0 or not math.isfinite(scale):
            continue
        out[i, finite] = np.abs(vals - med) > threshold * scale
    return out


def _sam_to_ref(arr: np.ndarray, ref: np.ndarray) -> np.ndarray:
    filled, _report = impute_columns(arr, reference=arr)
    ref = np.asarray(ref, dtype="float64")
    if filled.ndim != 2 or ref.ndim != 1 or filled.shape[1] != ref.size:
        return np.empty(0, dtype="float64")
    num = filled @ ref
    den = np.linalg.norm(filled, axis=1) * float(np.linalg.norm(ref))
    ok = den > 0
    angles = np.full(filled.shape[0], np.nan, dtype="float64")
    angles[ok] = np.arccos(np.clip(num[ok] / den[ok], -1.0, 1.0))
    return angles


def _basic_pca(x: object, *, max_components: int = 12, variance_threshold: float = 0.95, max_rows: int = 800, min_components: int = 1) -> dict[str, Any] | None:
    arr = _finite_matrix(x)
    if arr.ndim != 2 or arr.shape[0] < 3 or arr.shape[1] < 2:
        return None
    filled, _report = impute_columns(arr)
    if filled.shape[0] > max_rows:
        idx = np.sort(np.random.RandomState(0).choice(filled.shape[0], max_rows, replace=False))
        filled = filled[idx]
    centered = filled - filled.mean(axis=0, keepdims=True)
    if not np.isfinite(centered).all() or float(np.var(centered)) <= 0:
        return None
    try:
        u, s, vt = np.linalg.svd(centered, full_matrices=False)
    except np.linalg.LinAlgError:
        return None
    if s.size == 0:
        return None
    eig = (s**2) / max(centered.shape[0] - 1, 1)
    total = float(eig.sum())
    if total <= 0 or not math.isfinite(total):
        return None
    evr = eig / total
    cum = np.cumsum(evr)
    k = int(np.searchsorted(cum, variance_threshold) + 1) if cum[-1] >= variance_threshold else min(max_components, eig.size)
    k = max(min_components, k)
    k = max(1, min(k, max_components, centered.shape[0] - 1, centered.shape[1], eig.size))
    scores = u[:, :k] * s[:k]
    recon = scores @ vt[:k, :]
    residual = centered - recon
    q = np.sum(residual**2, axis=1)
    safe_eig = np.where(eig[:k] > 1e-12, eig[:k], np.nan)
    with np.errstate(invalid="ignore", divide="ignore"):
        t2 = np.nansum((scores**2) / safe_eig, axis=1)
    h = np.sqrt(np.maximum(t2, 0.0))
    return {"scores": scores, "q": q, "t2": t2, "h": h, "explained_variance_ratio": evr[:k], "n_components": k}


def _summary_median_p95_max(values: np.ndarray, prefix: str) -> dict[str, object]:
    vals = _finite_values(values)
    if vals.size == 0:
        return {f"{prefix}_median": None, f"{prefix}_p95": None, f"{prefix}_max": None, f"{prefix}_ratio": None}
    med = float(np.median(vals))
    p95 = float(np.percentile(vals, 95))
    return {f"{prefix}_median": med, f"{prefix}_p95": p95, f"{prefix}_max": float(np.max(vals)), f"{prefix}_ratio": p95 / med if med > 0 else None}


def class_balance(counts: object) -> dict[str, object]:
    """Class-balance metrics from per-class counts (absent classes should not be passed)."""
    arr = np.asarray(counts, dtype=float)
    arr = arr[arr > 0]
    k = int(arr.size)
    total = float(arr.sum())
    if k == 0 or total == 0:
        return _nulls(_CLASS_KEYS)
    p = arr / total
    normalized_entropy = 0.0 if k == 1 else float(-np.sum(p * np.log(p)) / np.log(k))
    return {
        "n_classes": k,
        "normalized_entropy": normalized_entropy,
        "imbalance_ratio": float(arr.max() / arr.min()),
        "gini_simpson": float(1.0 - np.sum(p**2)),
        "minority_fraction": float(arr.min() / total),
    }


def distribution_shape(y: object) -> dict[str, object]:
    """Skewness, excess kurtosis and a *descriptive* D'Agostino normality test for a 1D target."""
    arr = np.asarray(y, dtype=float).ravel()
    arr = arr[np.isfinite(arr)]
    n = int(arr.size)
    if n < 3 or float(np.ptp(arr)) == 0.0:
        return {**_nulls(_SHAPE_KEYS), "n": n}
    normality_p: float | None = None
    is_normal: bool | None = None
    if n >= 8:
        normality_p = float(stats.normaltest(arr).pvalue)
        is_normal = bool(normality_p > 0.05)
    return {
        "n": n,
        "skewness": float(stats.skew(arr, bias=False)),
        "kurtosis": float(stats.kurtosis(arr, fisher=True, bias=False)),
        "normality_p": normality_p,
        "is_normal": is_normal,
    }


def spectral_quality(x: object) -> dict[str, object]:
    """Smoothness/noise/range proxies for a 2D spectra block ``(n_samples, n_features)``."""
    arr = np.asarray(x, dtype=float)
    if arr.ndim != 2 or arr.shape[0] < 1 or arr.shape[1] < 3:
        return _nulls(_QUALITY_KEYS)
    mean_spectrum = np.nanmean(arr, axis=0)
    signal = float(np.mean(np.abs(mean_spectrum)))
    second_diff = np.diff(arr, n=2, axis=1)
    # Preserve this older aggregate's strict missing-data contract: its previous
    # row-MAD/median chain was undefined if any input cell was nonfinite. The
    # source roughness metric separately supports incomplete observations.
    noise = _finite_float(spectral_noise(arr).get("noise_rms")) if np.isfinite(arr).all() else None
    noise_proxy_db = float(20.0 * np.log10(signal / noise)) if (noise is not None and noise > 0 and signal > 0) else None
    vmax = float(np.nanmax(arr))
    return {
        "noise_proxy_db": noise_proxy_db,
        "smoothness": float(np.mean(np.sqrt(np.mean(second_diff**2, axis=1)))),
        "dynamic_range": float(np.nanmax(mean_spectrum) - np.nanmin(mean_spectrum)),
        "saturation_fraction": float(np.mean(arr >= vmax)) if np.isfinite(vmax) else None,
    }


def spectral_integrity(x: object) -> dict[str, object]:
    """Data-integrity counters: missing values, infinities, zeros and fully-zero columns."""
    arr = _as_2d_float(x)
    if arr.ndim != 2 or arr.size == 0:
        return _nulls(_INTEGRITY_KEYS)
    nan = np.isnan(arr)
    inf = np.isinf(arr)
    finite = np.isfinite(arr)
    zeros = (arr == 0.0) & finite
    finite_per_col = finite.sum(axis=0)
    zero_cols = (finite_per_col > 0) & (zeros.sum(axis=0) == finite_per_col)
    return {
        "nan_ratio": float(nan.sum() / arr.size),
        "inf_count": int(inf.sum()),
        "finite_ratio": float(finite.sum() / arr.size),
        "zero_ratio": float(zeros.sum() / arr.size),
        "zero_column_ratio": float(zero_cols.sum() / arr.shape[1]) if arr.shape[1] else None,
    }


def spectral_amplitude(x: object, axis: object | None = None) -> dict[str, object]:
    """Global amplitude descriptors: mean level, area under the mean spectrum, PTP and variance."""
    arr = _finite_matrix(x)
    if arr.ndim != 2 or arr.size == 0 or not np.isfinite(arr).any():
        return _nulls(_AMPLITUDE_KEYS)
    mean_spectrum = np.asarray(_safe_nanmean(arr, axis=0), dtype="float64")
    finite_mean = np.isfinite(mean_spectrum)
    if not finite_mean.any():
        return _nulls(_AMPLITUDE_KEYS)
    ax = _axis(axis, arr.shape[1])
    if finite_mean.sum() >= 2:
        order = np.argsort(ax[finite_mean])
        area = float(trapezoid(mean_spectrum[finite_mean][order], ax[finite_mean][order]))
    else:
        area = None
    vals = _finite_values(arr)
    return {
        "mean_reflectance": float(np.mean(vals)),
        "area_under_curve": area,
        "peak_to_peak": float(np.nanmax(mean_spectrum) - np.nanmin(mean_spectrum)),
        "variance": float(np.nanvar(arr)),
    }


def spectral_noise(x: object, axis: object | None = None) -> dict[str, object]:
    """Delegate second-difference MAD roughness to the existing Methods procedure.

    Signal-to-roughness ratios are descriptive proxies, not instrument SNR.
    Native support is optional; unavailable support stays explicit and no Python
    numerical fallback runs. Axis coordinates are attached as catalog metadata.
    """
    arr = _finite_matrix(x)
    if arr.ndim != 2 or arr.shape[0] < 1 or arr.shape[1] < 3:
        return _proxy_fields("noise", _nulls(_NOISE_KEYS))
    try:
        from n4m import abi_version, version
        from n4m.roles import SpectralNoiseProxy
    except (ImportError, OSError, RuntimeError) as exc:
        return _proxy_fields("noise", {
            **_nulls(_NOISE_KEYS),
            "availability": "unavailable",
            "unavailable_reason": f"Second-difference MAD roughness requires nirs4all-methods >= 1.3.10 with ABI >= 2.20 and SpectralNoiseProxy ({type(exc).__name__}).",
        })
    # The public native procedure takes a finite DTO plus an explicit validity
    # mask. Zero-fill is transport only; excluded cells never enter the kernel.
    valid = np.isfinite(arr)
    parameters = {} if valid.all() else {"valid_mask": valid.astype(np.int64).ravel().tolist()}
    result = SpectralNoiseProxy(**parameters).run(np.where(valid, arr, 0.0))

    def measured(key: str) -> float | None:
        state = result.get(key + "_status")
        if state is None or int(np.asarray(state).ravel()[0]) != 0:
            return None
        return _finite_float(result.get(key))

    index = measured("worst_band_index")
    worst_index = int(index) if index is not None else None
    band_support = "bandwise_min_status" in result
    return _proxy_fields("noise", {
        "noise_rms": measured("global_noise_sigma"),
        "snr": measured("global_signal_noise_ratio"),
        "snr_db": measured("global_signal_noise_db"),
        "bandwise_snr_min": measured("bandwise_min"),
        "bandwise_snr_median": measured("bandwise_median"),
        "worst_band_index": worst_index,
        "worst_band_axis": float(_axis(axis, arr.shape[1])[worst_index]) if worst_index is not None else None,
        "producer": {
            "name": "nirs4all-methods", "engine_version": version(),
            "abi_version": ".".join(str(part) for part in abi_version()),
            "operation": "diagnostics.spectral_noise_proxy", "protocol_version": "spectral-second-difference-mad-index.v1",
        },
        **({} if band_support else {
            "availability": "partial",
            "unavailable_reason": "Installed Methods provides global roughness but lacks the bandwise output extension; bandwise values are unavailable.",
        }),
    })


def spectral_artefacts(x: object) -> dict[str, object]:
    """Local artefact counters: narrow spikes, abrupt jumps and exact clipping at repeated extrema."""
    arr = _finite_matrix(x)
    if arr.ndim != 2 or arr.size == 0:
        return _nulls(_ARTEFACT_KEYS)
    jumps = _robust_outlier_mask(np.diff(arr, axis=1), threshold=8.0) if arr.shape[1] >= 2 else np.zeros((arr.shape[0], 0), dtype=bool)
    spikes = _robust_outlier_mask(np.diff(arr, n=2, axis=1), threshold=8.0) if arr.shape[1] >= 3 else np.zeros((arr.shape[0], 0), dtype=bool)
    vals = _finite_values(arr)
    clip_fraction = None
    if vals.size:
        lo, hi = float(vals.min()), float(vals.max())
        eps = max(1e-12, max(abs(lo), abs(hi)) * 1e-8)
        clipped = (np.abs(arr - lo) <= eps) | (np.abs(arr - hi) <= eps)
        clip_fraction = float(np.isfinite(arr[clipped]).sum() / vals.size)
    jump_den = arr.shape[0] * max(arr.shape[1] - 1, 1)
    spike_den = arr.shape[0] * max(arr.shape[1] - 2, 1)
    return {
        "spike_count": int(spikes.sum()),
        "spike_rate": float(spikes.sum() / spike_den) if spike_den else None,
        "jump_count": int(jumps.sum()),
        "jump_rate": float(jumps.sum() / jump_den) if jump_den else None,
        "clip_fraction": clip_fraction,
    }


def spectral_shape_metrics(x: object, axis: object | None = None) -> dict[str, object]:
    """Shape descriptors: baseline slope, curvature, first-derivative RMS and edge instability."""
    arr = _finite_matrix(x)
    if arr.ndim != 2 or arr.shape[1] < 2 or not np.isfinite(arr).any():
        return _nulls(_SHAPE_SPECTRAL_KEYS)
    mean_spectrum = np.asarray(_safe_nanmean(arr, axis=0), dtype="float64")
    ax = _axis(axis, arr.shape[1])
    xnorm = (ax - ax.min()) / ((ax.max() - ax.min()) or 1.0)
    finite_mean = np.isfinite(mean_spectrum)
    slope = None
    if finite_mean.sum() >= 2:
        slope = float(np.polyfit(xnorm[finite_mean], mean_spectrum[finite_mean], 1)[0])
    d1 = np.diff(arr, axis=1)
    d2 = np.diff(arr, n=2, axis=1) if arr.shape[1] >= 3 else np.empty((arr.shape[0], 0), dtype="float64")
    d1_rms_rows = np.sqrt(np.asarray(_safe_nanmean(d1**2, axis=1), dtype="float64")) if d1.size else np.empty(0)
    d2_rms_rows = np.sqrt(np.asarray(_safe_nanmean(d2**2, axis=1), dtype="float64")) if d2.size else np.empty(0)
    edge_noise_ratio = None
    if arr.shape[1] >= 10:
        width = max(2, int(round(arr.shape[1] * 0.1)))
        edge = np.concatenate([arr[:, :width].ravel(), arr[:, -width:].ravel()])
        middle = arr[:, width:-width].ravel() if arr.shape[1] > 2 * width else np.empty(0)
        edge_std = float(np.nanstd(edge)) if np.isfinite(edge).any() else None
        mid_std = float(np.nanstd(middle)) if middle.size and np.isfinite(middle).any() else None
        edge_noise_ratio = edge_std / mid_std if edge_std is not None and mid_std is not None and mid_std > 0 else None
    return {
        "baseline_slope": slope,
        "curvature_rms": float(np.nanmedian(d2_rms_rows)) if d2_rms_rows.size and np.isfinite(d2_rms_rows).any() else None,
        "d1_rms": float(np.nanmedian(d1_rms_rows)) if d1_rms_rows.size and np.isfinite(d1_rms_rows).any() else None,
        "edge_noise_ratio": edge_noise_ratio,
    }


def pca_outlier_metrics(x: object, *, pca: dict[str, Any] | None = None) -> dict[str, object]:
    """PCA residual (Q/SPE), Hotelling T² and PCA-space Mahalanobis H summaries."""
    pca = pca or _basic_pca(x)
    if pca is None:
        return _nulls(_PCA_OUTLIER_KEYS)
    return {
        **_summary_median_p95_max(np.asarray(pca["q"], dtype="float64"), "pca_q"),
        **_summary_median_p95_max(np.asarray(pca["t2"], dtype="float64"), "hotelling_t2"),
        **_summary_median_p95_max(np.asarray(pca["h"], dtype="float64"), "mahalanobis_h"),
    }


def reference_similarity(x: object, axis: object | None = None) -> dict[str, object]:
    """Distance and spectral-angle spread around the dataset mean spectrum."""
    arr = _finite_matrix(x)
    if arr.ndim != 2 or arr.shape[0] < 1 or arr.shape[1] < 2:
        return _nulls(_REFERENCE_KEYS)
    filled, _report = impute_columns(arr)
    ref = filled.mean(axis=0)
    if not np.isfinite(ref).all() or float(np.linalg.norm(ref)) <= 0:
        return _nulls(_REFERENCE_KEYS)
    rms = np.sqrt(np.mean((filled - ref) ** 2, axis=1))
    sam = _sam_to_ref(filled, ref)
    affine = _affine_reference_metrics(filled, ref)
    shift = _shift_reference_metrics(filled, ref, axis)
    return {
        "rms_to_mean_spectrum": float(np.median(rms)) if rms.size else None,
        "rms_to_mean_spectrum_p95": float(np.percentile(rms, 95)) if rms.size else None,
        "sam_to_mean_spectrum": float(np.median(sam[np.isfinite(sam)])) if np.isfinite(sam).any() else None,
        "sam_to_mean_spectrum_p95": float(np.percentile(sam[np.isfinite(sam)], 95)) if np.isfinite(sam).any() else None,
        **affine,
        **shift,
    }


def _affine_reference_metrics(filled: np.ndarray, ref: np.ndarray) -> dict[str, object]:
    """Fit each spectrum as ``offset + gain * mean_spectrum`` and summarize the fit residuals."""
    ref = np.asarray(ref, dtype="float64")
    x = ref - float(np.mean(ref))
    denom = float(np.sum(x**2))
    if denom <= 0 or not math.isfinite(denom):
        return {
            "affine_offset_median": None,
            "affine_offset_p95_abs": None,
            "affine_gain_median": None,
            "affine_gain_p95_abs_delta": None,
            "affine_residual_rms_median": None,
            "affine_residual_rms_p95": None,
        }
    offsets: list[float] = []
    gains: list[float] = []
    residuals: list[float] = []
    ref_mean = float(np.mean(ref))
    for row in filled:
        y = np.asarray(row, dtype="float64")
        gain = float(np.sum((y - float(np.mean(y))) * x) / denom)
        offset = float(np.mean(y) - gain * ref_mean)
        residual = y - (offset + gain * ref)
        offsets.append(offset)
        gains.append(gain)
        residuals.append(float(np.sqrt(np.mean(residual**2))))
    off = np.asarray(offsets, dtype="float64")
    gain_arr = np.asarray(gains, dtype="float64")
    res = np.asarray(residuals, dtype="float64")
    return {
        "affine_offset_median": float(np.median(off)),
        "affine_offset_p95_abs": float(np.percentile(np.abs(off), 95)),
        "affine_gain_median": float(np.median(gain_arr)),
        "affine_gain_p95_abs_delta": float(np.percentile(np.abs(gain_arr - 1.0), 95)),
        "affine_residual_rms_median": float(np.median(res)),
        "affine_residual_rms_p95": float(np.percentile(res, 95)),
    }


def _shift_reference_metrics(filled: np.ndarray, ref: np.ndarray, axis: object | None = None) -> dict[str, object]:
    """Cheap within-dataset alignment proxy: peak-position spread and cross-correlation lag spread."""
    if filled.shape[1] < 5:
        return {"peak_position_std": None, "xcorr_lag_p95_features": None, "xcorr_lag_p95_axis": None}
    peak_positions = np.asarray([int(np.argmax(row)) for row in filled], dtype="float64")
    ref_centered = ref - float(np.mean(ref))
    if float(np.linalg.norm(ref_centered)) <= 0:
        return {"peak_position_std": float(np.std(peak_positions)), "xcorr_lag_p95_features": None, "xcorr_lag_p95_axis": None}
    max_lag = max(1, min(50, filled.shape[1] // 10))
    lags: list[int] = []
    for row in filled:
        y = row - float(np.mean(row))
        if float(np.linalg.norm(y)) <= 0:
            continue
        corr = np.correlate(y, ref_centered, mode="full")
        center = filled.shape[1] - 1
        window = corr[center - max_lag: center + max_lag + 1]
        if window.size:
            lags.append(int(np.argmax(window) - max_lag))
    lag_p95 = float(np.percentile(np.abs(lags), 95)) if lags else None
    ax = _axis(axis, filled.shape[1])
    step = float(np.median(np.abs(np.diff(np.sort(ax))))) if ax.size >= 2 else 1.0
    return {
        "peak_position_std": float(np.std(peak_positions)),
        "xcorr_lag_p95_features": lag_p95,
        "xcorr_lag_p95_axis": float(lag_p95 * step) if lag_p95 is not None and math.isfinite(step) else None,
    }


def repeatability_metrics(x: object, sample_ids: Iterable[object] | None = None) -> dict[str, object]:
    """Within-sample repeatability: RMS/SAM/CV around each repeated sample centroid."""
    arr = _finite_matrix(x)
    if arr.ndim != 2 or arr.shape[0] < 2 or arr.shape[1] < 2 or sample_ids is None:
        return {**_nulls(_REPEATABILITY_KEYS), "n_repeat_groups": 0}
    labels = list(sample_ids)
    if len(labels) != arr.shape[0]:
        return {**_nulls(_REPEATABILITY_KEYS), "n_repeat_groups": 0}
    # Build memberships once. Re-scanning all labels for every unique soil ID
    # is quadratic and cannot reveal any repeatability in singleton groups.
    memberships: dict[str, list[int]] = {}
    for index, label in enumerate(labels):
        if label is None or type(label).__name__ in {"NAType", "NaTType"}:
            continue
        if isinstance(label, (float, np.floating)) and not np.isfinite(label):
            continue
        key = str(label)
        if key.strip():
            memberships.setdefault(key, []).append(index)
    repeated = [np.asarray(indices) for indices in memberships.values() if len(indices) > 1]
    if not repeated:
        return {**_nulls(_REPEATABILITY_KEYS), "n_repeat_groups": 0}
    filled, _report = impute_columns(arr)
    rms_all: list[float] = []
    sam_all: list[float] = []
    cv_all: list[float] = []
    groups = 0
    for idx in repeated:
        groups += 1
        block = filled[idx]
        centroid = block.mean(axis=0)
        rms = np.sqrt(np.mean((block - centroid) ** 2, axis=1))
        rms_all.extend(float(v) for v in rms if math.isfinite(float(v)))
        sam = _sam_to_ref(block, centroid)
        sam_all.extend(float(v) for v in sam if math.isfinite(float(v)))
        band_mean = np.mean(block, axis=0)
        band_std = np.std(block, axis=0, ddof=1)
        with np.errstate(divide="ignore", invalid="ignore"):
            cv = band_std / np.maximum(np.abs(band_mean), 1e-12)
        finite_cv = cv[np.isfinite(cv)]
        if finite_cv.size:
            cv_all.append(float(np.median(finite_cv)))
    return {
        "n_repeat_groups": groups,
        "rms_intra_id": float(np.median(rms_all)) if rms_all else None,
        "sam_intra_id": float(np.median(sam_all)) if sam_all else None,
        "cv_intra_id": float(np.median(cv_all)) if cv_all else None,
        "distance_to_centroid_p95": float(np.percentile(rms_all, 95)) if rms_all else None,
    }


def dataset_structure_metrics(x: object, *, pca: dict[str, Any] | None = None) -> dict[str, object]:
    """PCA-score density, kNN distance ratio (not LOF), and optional IsolationForest."""
    pca = pca or _basic_pca(x, max_components=6, variance_threshold=0.95)
    if pca is None:
        return _proxy_fields("structure", _nulls(_STRUCTURE_KEYS))
    scores = np.asarray(pca["scores"], dtype="float64")
    if scores.shape[0] < 4:
        return _proxy_fields("structure", _nulls(_STRUCTURE_KEYS))
    if scores.shape[0] > 800:
        idx = np.sort(np.random.RandomState(0).choice(scores.shape[0], 800, replace=False))
        scores = scores[idx]
    diff = scores[:, None, :] - scores[None, :, :]
    dist = np.sqrt(np.sum(diff**2, axis=2))
    np.fill_diagonal(dist, np.inf)
    k = min(8, scores.shape[0] - 1)
    knn = np.partition(dist, k - 1, axis=1)[:, :k]
    knn_mean = np.mean(knn, axis=1)
    finite_knn = knn_mean[np.isfinite(knn_mean)]
    density = 1.0 / float(np.median(finite_knn)) if finite_knn.size and float(np.median(finite_knn)) > 0 else None
    lof = finite_knn / float(np.median(finite_knn)) if finite_knn.size and float(np.median(finite_knn)) > 0 else np.empty(0)
    isolation_p95 = None
    try:
        from sklearn.ensemble import IsolationForest

        model = IsolationForest(n_estimators=100, random_state=0, contamination="auto")
        raw = -model.fit(scores).score_samples(scores)
        isolation_p95 = float(np.percentile(raw[np.isfinite(raw)], 95)) if np.isfinite(raw).any() else None
    except Exception:  # noqa: BLE001 - optional dependency / degenerate data
        isolation_p95 = None
    return _proxy_fields("structure", {
        "pca_score_density": density,
        "local_outlier_factor_p95": float(np.percentile(lof, 95)) if lof.size else None,
        "isolation_forest_score_p95": isolation_p95,
        "density_cv": float(np.std(finite_knn) / np.mean(finite_knn)) if finite_knn.size and np.mean(finite_knn) > 0 else None,
    })


def aggregate_profile_scores(profiles: Iterable[dict[str, Any]]) -> dict[str, float | None] | None:
    """Aggregate only fully observed axes; a missing source is not a clean source."""
    rows = [profile.get("profile_scores") or {} for profile in profiles if isinstance(profile, dict)]
    if not rows:
        return None
    result: dict[str, float | None] = {}
    for key in _PROFILE_SCORE_KEYS:
        values = [_finite_float(row.get(key)) for row in rows]
        result[key] = None if any(value is None for value in values) else sum(value for value in values if value is not None) / len(values)
    return result


def _profile_scores(profile: dict[str, Any]) -> dict[str, float | None]:
    integrity = profile.get("integrity") or {}
    amp = profile.get("amplitude") or {}
    noise = profile.get("noise") or {}
    artefacts = profile.get("artefacts") or {}
    shape = profile.get("shape") or {}
    outliers = profile.get("outliers") or {}
    reference = profile.get("reference") or {}
    repeatability = profile.get("repeatability") or {}
    structure = profile.get("structure") or {}
    ptp = amp.get("peak_to_peak")
    mean_reflectance = _finite_float(amp.get("mean_reflectance"))
    mean_abs = abs(mean_reflectance) if mean_reflectance is not None else 0.0
    ptp_value = _finite_float(ptp)
    signal_scale = None if mean_reflectance is None and ptp_value is None else max(mean_abs, abs(ptp_value) if ptp_value is not None else 0.0, 1e-12)
    snr_db = _finite_float(noise.get("snr_db"))
    noise_from_snr = 0.0 if snr_db is not None and snr_db >= 40 else (1.0 - max(0.0, snr_db) / 40.0 if snr_db is not None else None)
    return {
        "integrity_risk": _max_score(_saturate(integrity.get("nan_ratio"), 0.05), _saturate(integrity.get("zero_column_ratio"), 0.02), _saturate(integrity.get("inf_count"), 1.0)),
        "noise_risk": _max_score(noise_from_snr, _saturate(_ratio(noise.get("noise_rms"), signal_scale), 0.05)),
        "local_artefact_risk": _max_score(_saturate(artefacts.get("spike_rate"), 0.01), _saturate(artefacts.get("jump_rate"), 0.01), _saturate(artefacts.get("clip_fraction"), 0.01)),
        "shape_drift": _max_score(_saturate(_ratio(shape.get("baseline_slope"), signal_scale), 0.5), _saturate(shape.get("edge_noise_ratio"), 3.0)),
        "outlier_pressure": _max_score(_saturate(outliers.get("pca_q_ratio"), 8.0), _saturate(outliers.get("hotelling_t2_ratio"), 8.0), _saturate(outliers.get("mahalanobis_h_ratio"), 4.0)),
        "reference_spread": _max_score(
            _saturate(_ratio(reference.get("rms_to_mean_spectrum_p95"), signal_scale), 0.25),
            _saturate(reference.get("sam_to_mean_spectrum_p95"), 0.35),
            _saturate(_ratio(reference.get("affine_residual_rms_p95"), signal_scale), 0.12),
            _saturate(reference.get("xcorr_lag_p95_features"), 5.0),
        ),
        "repeatability_risk": _max_score(_saturate(_ratio(repeatability.get("rms_intra_id"), signal_scale), 0.1), _saturate(repeatability.get("sam_intra_id"), 0.15), _saturate(repeatability.get("cv_intra_id"), 0.25)),
        "structure_complexity": _max_score(_saturate(structure.get("local_outlier_factor_p95"), 3.0), _saturate(structure.get("density_cv"), 1.5)),
    }


def profile_score_labels() -> dict[str, str]:
    """Human labels for the normalized profile-score axes used by the site radar charts."""
    return dict(_PROFILE_LABELS)


def metric_catalog() -> list[dict[str, str]]:
    """The documented dataset-property metric table, for UI/library consumers."""
    rows = deepcopy(_METRIC_CATALOG)
    for row in rows:
        key = row.get("key", "")
        row["formula"] = _METRIC_FORMULAS.get(key, "")
        row["score_note"] = _METRIC_SCORE_NOTES.get(key, "")
        row["risk_when"] = _METRIC_RISK_WHEN.get(key, "high")
        if key in LEGACY_METRIC_ALIASES:
            row["legacy_key"] = key
            row["key"] = LEGACY_METRIC_ALIASES[key]
    return rows


def technology_guidance() -> list[dict[str, str]]:
    """Technology-specific metric extensions that are useful once the source metadata supports them."""
    return deepcopy(_TECHNOLOGY_GUIDANCE)


def bug_method_catalog() -> list[dict[str, str]]:
    """Bug-hunting methods for alignment, leakage, labels, hidden domains and model artefacts."""
    return deepcopy(_BUG_METHODS)


def _metric_value(profile: dict[str, Any], key: str) -> Any:
    for candidate in (LEGACY_METRIC_ALIASES.get(key, key), key):
        value: Any = profile
        for part in candidate.split("."):
            if not isinstance(value, dict) or part not in value:
                break
            value = value[part]
        else:
            return value
    return None


def _proxy_fields(section: str, values: Mapping[str, object]) -> dict[str, object]:
    result = dict(values)
    for old, new in LEGACY_METRIC_ALIASES.items():
        family, old_name = old.split(".")
        if family == section and old_name in values:
            result.setdefault(new.split(".")[1], values[old_name])
    return result


def with_metric_semantics(profile: dict[str, Any]) -> dict[str, Any]:
    """Add truthful proxy names without deleting or changing historical values.

    This is a metadata migration, not a scientific recomputation. Existing canonical
    names are never overwritten by a legacy alias from a different producer.
    """
    result = deepcopy(profile)
    for old, new in LEGACY_METRIC_ALIASES.items():
        section, old_name = old.split(".")
        new_name = new.split(".")[1]
        values = result.get(section)
        if isinstance(values, dict) and old_name in values and new_name not in values:
            values[new_name] = values[old_name]
    result["legacy_metric_aliases"] = dict(LEGACY_METRIC_ALIASES)
    return result


def migrate_profile_metadata(profile: dict[str, Any], *, from_protocol: str, domain_context: str | None = None) -> dict[str, Any]:
    """Explicit, idempotent protocol6→7 labels/signatures migration; no raw kernel runs.

    Historical raw numeric fields stay under their old names. New proxy names are
    additive compatibility aliases. This does not equate legacy definitions with
    a different producer's scientific protocol.
    """
    if from_protocol not in {"6", "7"}:
        raise ValueError("metadata migration requires the explicit protocol6 or protocol7 input")
    result = with_metric_semantics(profile)
    result["diagnostics"] = diagnostic_hypotheses(result, top_k=8, domain_context=domain_context)
    prior = result.get("signature_metadata") or {}
    result["signature_metadata"] = {
        "source_protocol": prior.get("source_protocol", from_protocol),
        "presentation_protocol": "7",
        "raw_kernels_recomputed": False,
        "domain_context": domain_context,
    }
    return result


def _signal_scale(profile: dict[str, Any]) -> float | None:
    amp = profile.get("amplitude") or {}
    mean_reflectance = _finite_float(amp.get("mean_reflectance"))
    peak_to_peak = _finite_float(amp.get("peak_to_peak"))
    mean_abs = abs(mean_reflectance) if mean_reflectance is not None else 0.0
    ptp = abs(peak_to_peak) if peak_to_peak is not None else 0.0
    return None if mean_reflectance is None and peak_to_peak is None else max(mean_abs, ptp, 1e-12)


def _snr_alert(value: Any, *, good_db: float) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(float(value)) or float(value) <= 0:
        return None
    db = 20.0 * math.log10(float(value))
    return float(1.0 - max(0.0, min(1.0, db / good_db)))


def _metric_alert_score(profile: dict[str, Any], key: str, value: Any) -> float | None:
    scores = profile.get("profile_scores") or {}
    scale = _signal_scale(profile)
    if key == "integrity.nan_ratio":
        return _saturate(value, 0.05)
    if key == "integrity.inf_count":
        return _saturate(value, 1.0)
    if key == "integrity.zero_ratio":
        return _saturate(value, 0.05)
    if key in {"amplitude.mean_reflectance", "amplitude.area_under_curve"}:
        return _finite_float(scores.get("shape_drift"))
    if key in {"amplitude.peak_to_peak", "amplitude.variance"}:
        return _diagnostic_signals(profile)["flat"]
    if key == "noise.noise_rms":
        return _saturate(_ratio(value, scale), 0.05)
    if key == "noise.snr":
        return _snr_alert(value, good_db=40.0)
    if key == "noise.bandwise_snr_min":
        return _snr_alert(value, good_db=35.0)
    if key == "artefacts.spike_count":
        return _metric_alert_score(profile, "artefacts.spike_rate", _metric_value(profile, "artefacts.spike_rate"))
    if key == "artefacts.spike_rate":
        return _saturate(value, 0.01)
    if key == "artefacts.jump_count":
        return _metric_alert_score(profile, "artefacts.jump_rate", _metric_value(profile, "artefacts.jump_rate"))
    if key == "artefacts.jump_rate":
        return _saturate(value, 0.01)
    if key == "artefacts.clip_fraction":
        return _saturate(value, 0.01)
    if key == "shape.baseline_slope":
        return _saturate(_ratio(value, scale), 0.5)
    if key == "shape.curvature_rms":
        return _saturate(_ratio(value, scale), 0.01)
    if key == "shape.d1_rms":
        return _saturate(_ratio(value, scale), 0.05)
    if key == "outliers.pca_q_ratio":
        return _saturate(value, 8.0)
    if key == "outliers.hotelling_t2_ratio":
        return _saturate(value, 8.0)
    if key == "outliers.mahalanobis_h_ratio":
        return _saturate(value, 4.0)
    if key == "reference.rms_to_mean_spectrum_p95":
        return _saturate(_ratio(value, scale), 0.25)
    if key == "reference.sam_to_mean_spectrum_p95":
        return _saturate(value, 0.35)
    if key == "repeatability.rms_intra_id":
        return _saturate(_ratio(value, scale), 0.1)
    if key == "repeatability.sam_intra_id":
        return _saturate(value, 0.15)
    if key == "repeatability.cv_intra_id":
        return _saturate(value, 0.25)
    if key == "structure.pca_score_density":
        return _finite_float(scores.get("structure_complexity"))
    if key == "structure.local_outlier_factor_p95":
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(float(value)):
            return None
        return _saturate(max(0.0, float(value) - 1.0), 2.0)
    if key == "structure.isolation_forest_score_p95":
        return _finite_float(scores.get("structure_complexity"))
    return None


def _score_level(score: Any) -> str:
    if isinstance(score, bool) or not isinstance(score, (int, float)) or not math.isfinite(float(score)):
        return "not calculable"
    if float(score) >= 0.72:
        return "strong"
    if float(score) >= 0.42:
        return "medium"
    return "weak"


def _score_interpretation(item: dict[str, str], score: float | None) -> str:
    if score is None:
        return "Not enough information to score this metric on this dataset."
    if score >= 0.42:
        risk_when = _METRIC_RISK_WHEN.get(item["key"], "high")
        if risk_when == "low":
            return item["low"]
        if risk_when == "extreme":
            return f"Atypical value: {item['high']} or {item['low']}"
        if risk_when == "heterogeneous":
            return item["high"]
        return item["high"]
    return item["high"] if _METRIC_RISK_WHEN.get(item["key"]) == "low" else item["low"]


def metric_score_rows(profile: dict[str, Any]) -> list[dict[str, Any]]:
    """Calculated metric table for one spectral profile.

    Each row joins the metric documentation table with the dataset's actual value, a 0..1 alert score,
    the formula/proxy used, and the automatic interpretation. Higher ``score`` means stronger anomaly
    evidence for that metric; it is a descriptive QC signal, not a pass/fail threshold.
    """
    rows: list[dict[str, Any]] = []
    if not isinstance(profile, dict):
        return rows
    for item in _METRIC_CATALOG:
        value = _metric_value(profile, item["key"])
        score = _metric_alert_score(profile, item["key"], value)
        score_f = float(max(0.0, min(1.0, score))) if isinstance(score, (int, float)) and not isinstance(score, bool) and math.isfinite(float(score)) else None
        rows.append({
            **item,
            "key": LEGACY_METRIC_ALIASES.get(item["key"], item["key"]),
            "legacy_key": item["key"] if item["key"] in LEGACY_METRIC_ALIASES else None,
            "value": value,
            "score": score_f,
            "level": _score_level(score_f),
            "interpretation": _score_interpretation(item, score_f),
            "interpretation_kind": "descriptive_alert",
            "causal_confidence_status": "unvalidated",
            "formula": _METRIC_FORMULAS.get(item["key"], ""),
            "score_note": _METRIC_SCORE_NOTES.get(item["key"], ""),
            "risk_when": _METRIC_RISK_WHEN.get(item["key"], "high"),
        })
    return rows


def _diagnostic_signals(profile: dict[str, Any]) -> dict[str, float | None]:
    """Preserve unavailable evidence; observed zero is distinct from missing."""
    scores = profile.get("profile_scores") or _profile_scores(profile)
    out = profile.get("outliers") or {}
    art = profile.get("artefacts") or {}
    noise = profile.get("noise") or {}
    amp = profile.get("amplitude") or {}
    snr_db = _finite_float(noise.get("snr_db"))
    mean = _finite_float(amp.get("mean_reflectance"))
    ptp = _finite_float(amp.get("peak_to_peak"))
    flat = None if mean is None or ptp is None else 1.0 - min(1.0, abs(ptp) / max(abs(mean), 1e-12) / 0.08)
    return {
        "q": _saturate(out.get("pca_q_ratio"), 8.0),
        "h": _max_score(_saturate(out.get("hotelling_t2_ratio"), 8.0), _saturate(out.get("mahalanobis_h_ratio"), 4.0)),
        "spike": _saturate(art.get("spike_rate"), 0.01),
        "jump": _saturate(art.get("jump_rate"), 0.01),
        "clip": _saturate(art.get("clip_fraction"), 0.01),
        "noise": _finite_float(scores.get("noise_risk")),
        "snr_low": None if snr_db is None else 1.0 - max(0.0, min(1.0, snr_db / 40.0)),
        "snr_high": None if snr_db is None else max(0.0, min(1.0, (snr_db - 25.0) / 25.0)),
        "baseline": _finite_float(scores.get("shape_drift")),
        "reference": _finite_float(scores.get("reference_spread")),
        "repeatability": _finite_float(scores.get("repeatability_risk")),
        "structure": _finite_float(scores.get("structure_complexity")),
        "flat": flat,
        "amplitude": _finite_float(scores.get("shape_drift")),
    }


def _max_score(*parts: float | None) -> float | None:
    """Unknown contributors cannot establish that a maximum risk is low."""
    return None if not parts or any(v is None for v in parts) else max(v for v in parts if v is not None)


def _scale_score(value: float | None, weight: float) -> float | None:
    return None if value is None else value * weight


def _sum_score(*parts: float | None) -> float | None:
    return None if any(v is None for v in parts) else sum(v for v in parts if v is not None)


def _mean_score(*parts: float | None) -> float | None:
    if not parts or any(v is None or not math.isfinite(v) for v in parts):
        return None
    return max(0.0, min(1.0, sum(v for v in parts if v is not None) / len(parts)))


def _low(v: float | None) -> float | None:
    return None if v is None else 1.0 - max(0.0, min(1.0, v))


def _diagnostic_row(key: str, label: str, score: float | None, interpretation: str, evidence: list[tuple[str, float | None]]) -> dict[str, Any]:
    available = [(name, value) for name, value in evidence if value is not None]
    top = [(name, max(0.0, min(1.0, value))) for name, value in available if value >= 0.18]
    top.sort(key=lambda item: -item[1])
    return {
        "key": key, "label": label, "score": score,
        "strength": "unknown" if score is None else "strong" if score >= 0.72 else "medium" if score >= 0.42 else "weak",
        "score_kind": "heuristic_signature", "confidence_status": "unvalidated",
        "signal_strength": score,
        "score_explanation": "A signature at 0.78 is not a causal probability of 78%.",
        "recommended_verifications": [
            "Check the white/black reference actually acquired and its metadata.",
            "Check instrument, probe, geometry, campaign and processing/resampling log.",
            "Check the repeat protocol before interpreting an intra-ID dispersion.",
        ],
        "availability": "available" if score is not None else "partial" if available else "unavailable",
        "evidence_coverage": len(available) / len(evidence) if evidence else 0.0,
        "missing_evidence": [name for name, value in evidence if value is None],
        "evidence": [{"signal": name, "level": value} for name, value in top[:5]],
        "interpretation": interpretation,
        "interpretation_kind": "possible_cause" if key != "normal" else "descriptive_signature",
        "reference_scope": "dataset_mean_not_independent_reference",
    }


def diagnostic_hypotheses(profile: dict[str, Any], *, top_k: int | None = None, domain_context: str | None = None) -> list[dict[str, Any]]:
    """Automatic interpretation layer for a spectral profile.

    The rules mirror the diagnostic matrix used by the site. They intentionally return hypotheses
    ranked by evidence instead of hard labels; several physical causes can share the same metric
    signature.
    """
    if domain_context is not None and domain_context.casefold() != "vera25":
        raise ValueError("supported diagnostic domain_context is VERA25; omit it for generic hypotheses")
    s = _diagnostic_signals(profile)
    normal_bad = _max_score(s["q"], s["h"], s["spike"], s["jump"], s["clip"], s["noise"], s["baseline"], s["reference"], s["repeatability"], s["structure"])
    rows = [
        _diagnostic_row("normal", "Weak signatures observed", _low(normal_bad), "Weak signatures on available metrics; does not certify either physical validity or the absence of defects.", [("slight anomalies", _low(normal_bad))]),
        _diagnostic_row("very_noisy", "High spectral roughness signature", _mean_score(s["q"], s["noise"], s["noise"], s["snr_low"], s["spike"], _scale_score(s["reference"], 0.6)), "Weak signal, detector problem, lamp or unstable acquisition.", [("PCA Q", s["q"]), ("Roughness sigma proxy", s["noise"]), ("Low S/N roughness proxy", s["snr_low"]), ("Spike rate", s["spike"]), ("RMS/SAM to mean spectrum", s["reference"])]),
        _diagnostic_row("splice", "Signature compatible with a spectral splice", _mean_score(s["q"], s["spike"], s["jump"], s["reference"], _sum_score(_scale_score(s["snr_high"], 0.4), _scale_score(_low(s["noise"]), 0.3))), "Break at detector junctions, local calibration or different probe.", [("PCA Q", s["q"]), ("Spike rate", s["spike"]), ("Jump rate", s["jump"]), ("RMS/SAM to mean spectrum", s["reference"]), ("Undegraded roughness S/N proxy", s["snr_high"])]),
        _diagnostic_row("partial_coverage", "Signature compatible with partial coverage", _mean_score(s["q"], s["h"], s["baseline"], s["reference"], _scale_score(s["repeatability"], 0.65), _scale_score(_low(_max_score(s["spike"], s["jump"])), 0.55)), "Partial spot coverage; contribution from the background or support.", [("PCA Q", s["q"]), ("Mahalanobis / T2", s["h"]), ("Baseline/mean/area", s["baseline"]), ("RMS/SAM to mean spectrum", s["reference"]), ("Repeatability", s["repeatability"])]),
        _diagnostic_row("background_shift", "Signature compatible with a different background", _mean_score(s["q"], s["h"], s["baseline"], s["baseline"], s["reference"], _scale_score(_low(_max_score(s["spike"], s["jump"])), 0.45)), "Systematic effect of support, white/black, transflectance or measurement environment.", [("PCA Q", s["q"]), ("Mahalanobis / T2", s["h"]), ("Baseline/mean/area", s["baseline"]), ("RMS/SAM to mean spectrum", s["reference"])]),
        _diagnostic_row("out_of_domain", "Signature compatible with a population shift", _mean_score(s["h"], s["h"], s["reference"], _scale_score(s["structure"], 0.7), _low(_max_score(s["noise"], s["spike"], s["jump"]))), "Different but physically plausible variety, species, batch or condition.", [("Mahalanobis / T2", s["h"]), ("RMS/SAM to mean spectrum", s["reference"]), ("PCA structure", s["structure"]), ("weak artifacts", _low(_max_score(s["noise"], s["spike"], s["jump"])))]),
        _diagnostic_row("white_calibration", "Offset compatible with a different white reference", _mean_score(s["q"], _scale_score(s["h"], 0.7), s["baseline"], s["baseline"], s["reference"], _scale_score(_max_score(s["spike"], s["jump"]), 0.55)), "Systematic discrepancy between campaigns, instruments or white reference.", [("PCA Q", s["q"]), ("Mahalanobis / T2", s["h"]), ("Baseline/mean/area", s["baseline"]), ("RMS/SAM to mean spectrum", s["reference"]), ("local artifacts", _max_score(s["spike"], s["jump"]))]),
        _diagnostic_row("probe_geometry", "Signature compatible with a change in geometry", _mean_score(s["q"], s["h"], s["baseline"], s["reference"], s["repeatability"], _scale_score(_max_score(s["spike"], s["jump"]), 0.7), _scale_score(s["snr_high"], 0.35)), "Changing illumination, collection, angle or probe-sample distance.", [("PCA Q", s["q"]), ("Mahalanobis / T2", s["h"]), ("Baseline/mean/area", s["baseline"]), ("RMS/SAM to mean spectrum", s["reference"]), ("Repeatability", s["repeatability"])]),
        _diagnostic_row("clipping", "Signature compatible with clipping", _mean_score(s["clip"], s["clip"], s["q"], s["baseline"], _scale_score(s["jump"], 0.6)), "Detector saturated or insufficient dynamic range.", [("Clip fraction", s["clip"]), ("PCA Q", s["q"]), ("Baseline/mean/area", s["baseline"]), ("Jump rate", s["jump"])]),
        _diagnostic_row("resampling_error", "Signature compatible with resampling", _mean_score(s["q"], s["q"], s["spike"], s["jump"], _scale_score(_low(s["noise"]), 0.6), _scale_score(s["snr_high"], 0.5), _scale_score(_low(s["repeatability"]), 0.35)), "Digital artifacts or incorrect spectral processing.", [("PCA Q", s["q"]), ("Spike rate", s["spike"]), ("Jump rate", s["jump"]), ("Low roughness sigma proxy", _low(s["noise"])), ("High S/N roughness proxy", s["snr_high"])]),
        _diagnostic_row("flat_low_signal", "Flat spectrum/weak signal", _mean_score(s["q"], s["snr_low"], s["flat"], s["flat"], _scale_score(_low(_max_score(s["spike"], s["jump"])), 0.5)), "Bad contact, missing sample, degraded measurement or very low dynamic range.", [("PCA Q", s["q"]), ("Low S/N roughness proxy", s["snr_low"]), ("Very low variance", s["flat"]), ("weak artifacts", _low(_max_score(s["spike"], s["jump"])))]),
        _diagnostic_row("poor_repeatability", "Dispersion between observations of the same unit", _mean_score(s["repeatability"], s["repeatability"], _scale_score(_max_score(s["noise"], s["spike"], s["jump"]), 0.5)), "Unstable positioning, operator or protocol; investigate intra-ID repetitions.", [("Intra-ID RMS/SAM", s["repeatability"]), ("Variable noise/artifacts", _max_score(s["noise"], s["spike"], s["jump"]))]),
        _diagnostic_row("multi_regime", "Multi-regime dataset", _mean_score(s["structure"], s["reference"], _scale_score(s["q"], 0.8), _scale_score(s["h"], 0.8), _scale_score(s["repeatability"], 0.6)), "Mixture of campaigns, operators, batches, setups or spectral subpopulations.", [("PCA structure", s["structure"]), ("RMS/SAM to mean spectrum", s["reference"]), ("PCA Q", s["q"]), ("Mahalanobis / T2", s["h"]), ("Repeatability", s["repeatability"])]),
        _diagnostic_row("vera25_like", "Exploratory VERA25 pattern (specificity not validated)", _mean_score(s["q"], s["q"], s["h"], s["spike"], s["jump"], _scale_score(_low(s["noise"]), 0.55), _scale_score(s["snr_high"], 0.55), s["reference"], _scale_score(s["repeatability"], 0.75)), "Possible combination of probe + splice change, amplified by geometry, background or calibration.", [("PCA Q", s["q"]), ("Mahalanobis / T2", s["h"]), ("Spike rate", s["spike"]), ("Jump rate", s["jump"]), ("RMS/SAM to mean spectrum", s["reference"])]),
    ]
    required = {
        "normal": ["q", "h", "spike", "jump", "clip", "noise", "baseline", "reference", "repeatability", "structure"],
        "very_noisy": ["q", "noise", "snr_low", "spike", "reference"],
        "splice": ["q", "spike", "jump", "reference", "snr_high", "noise"],
        "partial_coverage": ["q", "h", "baseline", "reference", "repeatability", "spike", "jump"],
        "background_shift": ["q", "h", "baseline", "reference", "spike", "jump"],
        "out_of_domain": ["h", "reference", "structure", "noise", "spike", "jump"],
        "white_calibration": ["q", "h", "baseline", "reference", "spike", "jump"],
        "probe_geometry": ["q", "h", "baseline", "reference", "repeatability", "spike", "jump", "snr_high"],
        "clipping": ["clip", "q", "baseline", "jump"],
        "resampling_error": ["q", "spike", "jump", "noise", "snr_high", "repeatability"],
        "flat_low_signal": ["q", "snr_low", "flat", "spike", "jump"],
        "poor_repeatability": ["repeatability", "noise", "spike", "jump"],
        "multi_regime": ["structure", "reference", "q", "h", "repeatability"],
        "vera25_like": ["q", "h", "spike", "jump", "noise", "snr_high", "reference", "repeatability"],
    }
    if domain_context is None:
        rows = [row for row in rows if row["key"] != "vera25_like"]
    for row in rows:
        if row["key"] == "vera25_like":
            row["domain_context"] = "VERA25"
            row["specificity_status"] = "unvalidated"
        signals = required[row["key"]]
        missing = [name for name in signals if s[name] is None]
        row["missing_evidence"] = missing
        row["evidence_coverage"] = (len(signals) - len(missing)) / len(signals)
        row["availability"] = "available" if not missing else "unavailable" if len(missing) == len(signals) else "partial"
    rows.sort(key=lambda row: (row["score"] is None, -(row["score"] or 0.0)))
    if top_k is not None:
        rows = rows[:top_k]
    return rows


def diagnostic_presentation(row: dict[str, Any], *, domain_context: str | None = None) -> dict[str, Any] | None:
    """Present a historical hypothesis honestly without changing its stored score.

    Original cards remain untouched. The display uses current terminology and
    explicitly unvalidated interpretation metadata; a private/domain-specific
    VERA25 suggestion is suppressed unless the caller opts into that context.
    """
    templates = {item["key"]: item for item in diagnostic_hypotheses({}, domain_context=domain_context)}
    key = row.get("key")
    if key == "vera25_like" and domain_context is None:
        return None
    result = deepcopy(row)
    template = templates.get(key)
    if template is not None:
        for field in ("label", "score_kind", "confidence_status", "score_explanation", "recommended_verifications", "reference_scope", "interpretation", "interpretation_kind", "domain_context", "specificity_status"):
            if field in template:
                result[field] = template[field]
    result["signal_strength"] = result.get("score")
    score = _finite_float(result.get("score"))
    result["strength"] = "unknown" if score is None else "strong" if score >= 0.72 else "medium" if score >= 0.42 else "weak"
    for evidence in result.get("evidence") or []:
        if isinstance(evidence, dict) and isinstance(evidence.get("signal"), str):
            evidence["signal"] = evidence["signal"].replace("RMS/SAM référence", "RMS/SAM to mean spectrum")
            evidence["signal"] = evidence["signal"].replace("Noise RMS", "Roughness sigma proxy").replace("SNR", "Roughness S/N proxy")
    return result


def spectral_profile(x: object, axis: object | None = None, *, sample_ids: Iterable[object] | None = None, domain_context: str | None = None) -> dict[str, Any]:
    """Full source-level property profile for a spectral matrix ``X``.

    The profile is intentionally descriptive, not a pass/fail QC gate. ``profile_scores`` are heuristic
    0..1 axes for visual comparison where higher means more risk / heterogeneity on that axis.
    """
    arr = _as_2d_float(x)
    ax = _axis(axis, arr.shape[1]) if arr.ndim == 2 and arr.shape[1] else np.empty(0, dtype="float64")
    pca = _basic_pca(arr)
    profile: dict[str, Any] = {
        "integrity": spectral_integrity(arr),
        "amplitude": spectral_amplitude(arr, ax),
        "noise": spectral_noise(arr, ax),
        "artefacts": spectral_artefacts(arr),
        "shape": spectral_shape_metrics(arr, ax),
        "outliers": pca_outlier_metrics(arr, pca=pca),
        "reference": reference_similarity(arr, ax),
        "repeatability": repeatability_metrics(arr, sample_ids),
        "structure": dataset_structure_metrics(arr, pca=pca),
    }
    profile["profile_scores"] = _profile_scores(profile)
    profile["diagnostics"] = diagnostic_hypotheses(profile, top_k=8, domain_context=domain_context)
    return with_metric_semantics(profile)


def wavelength_spacing(wavelengths: object) -> dict[str, object]:
    """Summary of the wavelength sampling grid (and whether it is uniform)."""
    wl = np.asarray(wavelengths, dtype=float)
    wl = wl[np.isfinite(wl)]
    if wl.size < 2:
        return _nulls(_SPACING_KEYS)
    steps = np.diff(np.sort(wl))
    mean = float(steps.mean())
    return {
        "mean": mean,
        "std": float(steps.std()),
        "min": float(steps.min()),
        "max": float(steps.max()),
        "median": float(np.median(steps)),
        "is_uniform": bool(steps.std() / abs(mean) < 1e-3) if mean != 0 else None,
    }


def effective_rank(explained_variance: object) -> float | None:
    """Participation ratio of the eigenvalue spectrum, ``(Σλ)² / Σλ²`` (a soft dimensionality, ≥1).

    Reported as a lower bound when only the leading components are supplied (truncated spectrum).
    """
    lam = np.asarray(explained_variance, dtype=float)
    lam = lam[np.isfinite(lam) & (lam > 0)]
    if lam.size == 0:
        return None
    return float((lam.sum() ** 2) / float(np.sum(lam**2)))


def spectral_curve(spectra: object, axis: object, *, max_points: int = 140) -> dict[str, list[float]] | None:
    """Subsampled per-wavelength quantile bands of a spectra block — the site's spectra-with-quantiles chart.

    Returns ``{axis, q05, q25, median, q75, q95, mean}`` (each a list over up to ``max_points`` wavelengths,
    evenly subsampled along the spectral axis), or ``None`` when there is nothing to summarize. Pure data;
    the site renders it as an interactive SVG (no matplotlib).
    """
    arr = np.asarray(spectra, dtype="float64")
    if arr.ndim != 2 or arr.shape[0] < 1 or arr.shape[1] < 2:
        return None
    ax = np.asarray(axis, dtype="float64")
    cols = arr.shape[1]
    idx = np.unique(np.linspace(0, cols - 1, num=min(max_points, cols)).round().astype(int))
    sub = arr[:, idx]
    with warnings.catch_warnings():  # all-NaN columns -> nan; the site skips non-finite points
        warnings.simplefilter("ignore", RuntimeWarning)
        q05, q25, med, q75, q95 = np.nanpercentile(sub, [5, 25, 50, 75, 95], axis=0)
        mean = np.nanmean(sub, axis=0)

    def _row(values: np.ndarray) -> list[float]:
        return [float(v) for v in values]

    return {"axis": _row(ax[idx]), "q05": _row(q05), "q25": _row(q25), "median": _row(med), "q75": _row(q75), "q95": _row(q95), "mean": _row(mean)}


def pca_score_plot(spectra: object, *, max_points: int = 800) -> dict[str, Any] | None:
    """Subsampled PCA PC1/PC2 score cloud for the site's dataset explorer."""
    arr = _finite_matrix(spectra)
    if arr.ndim != 2 or arr.shape[0] < 3 or arr.shape[1] < 2:
        return None
    idx = np.arange(arr.shape[0])
    if arr.shape[0] > max_points:
        idx = np.sort(np.random.RandomState(0).choice(arr.shape[0], max_points, replace=False))
    pca = _basic_pca(arr[idx], max_components=2, variance_threshold=0.8, max_rows=max_points, min_components=2)
    if pca is None:
        return None
    scores = np.asarray(pca["scores"], dtype="float64")
    if scores.shape[1] < 2:
        return None
    evr = np.asarray(pca.get("explained_variance_ratio"), dtype="float64")
    return {
        "explained_variance_ratio": [float(v) for v in evr[:2]],
        "points": [{"x": float(scores[i, 0]), "y": float(scores[i, 1])} for i in range(scores.shape[0])],
    }


def spectral_target_correlation(spectra: object, y: object, axis: object, *, max_points: int = 140) -> dict[str, Any] | None:
    """Per-wavelength Pearson correlation between a spectra block and one numeric target.

    Input rows must already be aligned one-to-one at sample level. The result is descriptive; it is
    not a predictive model and does not imply out-of-sample performance.
    """
    x = _finite_matrix(spectra)
    target = np.asarray(y, dtype="float64").ravel()
    if x.ndim != 2 or x.shape[0] < 3 or x.shape[1] < 2 or target.size != x.shape[0]:
        return None
    valid_rows = np.isfinite(target) & np.isfinite(x).any(axis=1)
    x = x[valid_rows]
    target = target[valid_rows]
    if x.shape[0] < 3 or float(np.nanstd(target)) <= 0:
        return None
    filled, _report = impute_columns(x)
    y0 = target - float(np.mean(target))
    x0 = filled - filled.mean(axis=0, keepdims=True)
    denom = np.sqrt(np.sum(x0**2, axis=0) * float(np.sum(y0**2)))
    corr = np.full(filled.shape[1], np.nan, dtype="float64")
    ok = denom > 0
    corr[ok] = np.sum(x0[:, ok] * y0[:, None], axis=0) / denom[ok]
    abs_corr = np.abs(corr)
    ax = _axis(axis, filled.shape[1])
    finite = np.isfinite(abs_corr)
    if not finite.any():
        return None
    best = int(np.nanargmax(abs_corr))
    idx = np.unique(np.linspace(0, filled.shape[1] - 1, num=min(max_points, filled.shape[1])).round().astype(int))
    return {
        "n": int(x.shape[0]),
        "max_abs_corr": float(abs_corr[best]),
        "argmax_axis": float(ax[best]),
        "mean_abs_corr": float(np.nanmean(abs_corr)),
        "frac_abs_corr_gt_0_5": float(np.mean(abs_corr[finite] >= 0.5)),
        "curve": {"axis": [float(v) for v in ax[idx]], "corr": [float(v) for v in corr[idx]], "abs_corr": [float(v) for v in abs_corr[idx]]},
    }


def histogram_bins(values: object, *, n_bins: int = 24) -> dict[str, list[float]] | None:
    """Histogram (``{edges, counts}``) of a numeric column — the site's per-variable distribution chart.

    ``edges`` has ``n_bins + 1`` entries; ``counts`` has ``n_bins``. ``None`` when there are too few finite
    values or zero range (a constant column carries no distribution).
    """
    arr = np.asarray(values, dtype="float64").ravel()
    arr = arr[np.isfinite(arr)]
    if arr.size < 2:
        return None
    lo, hi = float(arr.min()), float(arr.max())
    if hi <= lo:
        return None
    counts, edges = np.histogram(arr, bins=n_bins, range=(lo, hi))
    return {"edges": [float(e) for e in edges], "counts": [int(c) for c in counts]}


def impute_columns(x: object, *, reference: object | None = None) -> tuple[np.ndarray, dict[str, int]]:
    """Replace NaN in a 2D block with column means (of ``reference`` if given, else of ``x``).

    Rows are never dropped (sample count preserved); all-NaN columns become 0. Returns
    ``(filled, report)`` counting affected cells/rows/columns so the card can disclose imputation.
    """
    arr = np.array(x, dtype="float64", copy=True)
    if arr.ndim != 2:
        return arr, {"n_nan_cells": 0, "n_nan_rows": 0, "n_nan_columns": 0}
    nan_mask = ~np.isfinite(arr)
    report = {
        "n_nan_cells": int(nan_mask.sum()),
        "n_nan_rows": int(np.any(nan_mask, axis=1).sum()),
        "n_nan_columns": int(np.any(nan_mask, axis=0).sum()),
    }
    if report["n_nan_cells"]:
        ref = np.asarray(reference, dtype="float64") if reference is not None else arr
        with warnings.catch_warnings():  # all-NaN columns -> nan (replaced by 0 below); silence "Mean of empty slice"
            warnings.simplefilter("ignore", RuntimeWarning)
            col_mean = np.nanmean(ref if ref.shape[1:] == arr.shape[1:] else arr, axis=0)
        col_mean = np.where(np.isfinite(col_mean), col_mean, 0.0)
        rows, cols = np.where(nan_mask)
        arr[rows, cols] = np.take(col_mean, cols)
    return arr, report


def target_shift(y_train: object, y_test: object) -> dict[str, object]:
    """Regression train↔test target shift: standardized mean difference, KS test, Wasserstein distance."""
    a = np.asarray(y_train, dtype=float).ravel()
    a = a[np.isfinite(a)]
    b = np.asarray(y_test, dtype=float).ravel()
    b = b[np.isfinite(b)]
    if a.size < 2 or b.size < 2:
        return _nulls(_TARGET_SHIFT_KEYS)
    pooled = float(np.sqrt((a.var(ddof=1) + b.var(ddof=1)) / 2.0))
    ks = stats.ks_2samp(a, b)
    return {
        "n_train": int(a.size), "n_test": int(b.size),
        "mean_train": float(a.mean()), "mean_test": float(b.mean()),
        "std_train": float(a.std(ddof=1)), "std_test": float(b.std(ddof=1)),
        "standardized_mean_diff": float((b.mean() - a.mean()) / pooled) if pooled > 0 else None,
        "ks_statistic": float(ks.statistic), "ks_p": float(ks.pvalue),
        "wasserstein": float(stats.wasserstein_distance(a, b)),
    }


def class_shift(train_counts: dict[str, int], test_counts: dict[str, int]) -> dict[str, object]:
    """Classification train↔test label shift: max class-proportion delta + Jensen-Shannon distance."""
    classes = sorted(set(train_counts) | set(test_counts))
    unseen_test = [c for c in classes if train_counts.get(c, 0) > 0 and test_counts.get(c, 0) == 0]
    unseen_train = [c for c in classes if test_counts.get(c, 0) > 0 and train_counts.get(c, 0) == 0]
    p = np.array([train_counts.get(c, 0) for c in classes], dtype=float)
    q = np.array([test_counts.get(c, 0) for c in classes], dtype=float)
    if not classes or p.sum() == 0 or q.sum() == 0:
        return {**_nulls(_CLASS_SHIFT_KEYS), "n_classes": len(classes), "unseen_in_test": unseen_test, "unseen_in_train": unseen_train}
    js = jensenshannon(p / p.sum(), q / q.sum(), base=2)
    return {
        "n_classes": len(classes),
        "max_abs_proportion_delta": float(np.max(np.abs(p / p.sum() - q / q.sum()))),
        "jensen_shannon": float(js) if np.isfinite(js) else None,
        "unseen_in_test": unseen_test,
        "unseen_in_train": unseen_train,
    }
