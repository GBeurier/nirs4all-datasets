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

import numpy as np
from scipy import stats

_CLASS_KEYS = ("n_classes", "normalized_entropy", "imbalance_ratio", "gini_simpson", "minority_fraction")
_SHAPE_KEYS = ("n", "skewness", "kurtosis", "normality_p", "is_normal")
_QUALITY_KEYS = ("noise_proxy_db", "smoothness", "dynamic_range", "saturation_fraction")
_SPACING_KEYS = ("mean", "std", "min", "max", "median", "is_uniform")


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
