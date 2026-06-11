"""Descriptive metrics that fill the gaps nirs4all does not expose for a dataset card.

Pure ``numpy``/``scipy`` functions (no nirs4all import, no I/O). Each returns a JSON-serializable
dict with a stable key set (``None`` values for degenerate input), so the card schema is constant.

Definitions are deliberately documented and conservative:

* class balance uses normalized Shannon entropy and the max/min imbalance ratio;
* distribution shape reports skewness/excess-kurtosis and a D'Agostino normality p-value that is
  *descriptive only* (never a quality gate);
* ``noise_proxy_db`` is a high-frequency smoothness/noise proxy from the spectral second difference
  (NOT an instrument SNR), with the MAD normal-scaled (x1.4826);
* wavelength spacing summarizes the sampling grid.
"""
from __future__ import annotations

import warnings

import numpy as np
from scipy import stats
from scipy.spatial.distance import jensenshannon

_CLASS_KEYS = ("n_classes", "normalized_entropy", "imbalance_ratio", "gini_simpson", "minority_fraction")
_SHAPE_KEYS = ("n", "skewness", "kurtosis", "normality_p", "is_normal")
_QUALITY_KEYS = ("noise_proxy_db", "smoothness", "dynamic_range", "saturation_fraction")
_SPACING_KEYS = ("mean", "std", "min", "max", "median", "is_uniform")
_TARGET_SHIFT_KEYS = ("n_train", "n_test", "mean_train", "mean_test", "std_train", "std_test", "standardized_mean_diff", "ks_statistic", "ks_p", "wasserstein")
_CLASS_SHIFT_KEYS = ("n_classes", "max_abs_proportion_delta", "jensen_shannon", "unseen_in_test", "unseen_in_train")


def _nulls(keys: tuple[str, ...]) -> dict[str, object]:
    return dict.fromkeys(keys, None)


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
    # Robust noise floor: median over samples of the normal-scaled MAD of the 2nd difference,
    # divided by sqrt(6) to undo the variance inflation of differencing white noise twice.
    mad = stats.median_abs_deviation(second_diff, axis=1, scale=1.0)
    noise = float(np.median(mad) * 1.4826 / np.sqrt(6.0))
    noise_proxy_db = float(20.0 * np.log10(signal / noise)) if (noise > 0 and signal > 0) else None
    vmax = float(np.nanmax(arr))
    return {
        "noise_proxy_db": noise_proxy_db,
        "smoothness": float(np.mean(np.sqrt(np.mean(second_diff**2, axis=1)))),
        "dynamic_range": float(np.nanmax(mean_spectrum) - np.nanmin(mean_spectrum)),
        "saturation_fraction": float(np.mean(arr >= vmax)) if np.isfinite(vmax) else None,
    }


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
