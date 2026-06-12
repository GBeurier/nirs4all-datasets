"""An extensible, re-runnable metric registry for the qualification protocol.

The card records its :data:`PROTOCOL_VERSION` so a later ``--protocol-refresh`` can re-qualify
(recompute every metric from the canonical Parquet) *without* rebuilding the canonical bytes. The
registry is a thin index over the pure numerics already in :mod:`nirs4all_datasets.qualify.metrics`:
each metric is a ``(key, scope) -> callable`` registered with :func:`register`, retrievable by scope
with :func:`metrics_for`. Scopes are ``source`` (one spectral block), ``variable`` (one Y/metadata
column) and ``dataset`` (cross-source/aggregate). The wrapped callables do not reimplement any
numerics — they delegate to :mod:`metrics`; the registry only standardizes invocation and protocol
versioning so the metric set is extensible and the card is re-derivable.
"""
from __future__ import annotations

from collections.abc import Callable
from typing import Any, Literal

import numpy as np

from nirs4all_datasets.qualify import metrics

PROTOCOL_VERSION = "5"  # 5: dataset-property explorer profile + diagnostic hypotheses; 4: detected signal type; 3: scientific stats; 2: quantile curves + histogram bins

Scope = Literal["source", "variable", "dataset"]
MetricFn = Callable[..., Any]

_REGISTRY: dict[Scope, dict[str, MetricFn]] = {"source": {}, "variable": {}, "dataset": {}}


def register(key: str, scope: Scope) -> Callable[[MetricFn], MetricFn]:
    """Register a metric callable under ``key`` within ``scope`` (decorator).

    Args:
        key: The metric's stable key (unique within its scope).
        scope: One of ``"source"``, ``"variable"``, ``"dataset"``.

    Returns:
        The decorator, which records the function and returns it unchanged.
    """
    if scope not in _REGISTRY:
        raise ValueError(f"unknown metric scope {scope!r} (expected one of {sorted(_REGISTRY)}).")

    def _decorate(fn: MetricFn) -> MetricFn:
        if key in _REGISTRY[scope]:
            raise ValueError(f"metric {key!r} already registered in scope {scope!r}.")
        _REGISTRY[scope][key] = fn
        return fn

    return _decorate


def metrics_for(scope: Scope) -> dict[str, MetricFn]:
    """Return the registered metrics for ``scope`` as ``{key: callable}`` (a copy)."""
    if scope not in _REGISTRY:
        raise ValueError(f"unknown metric scope {scope!r} (expected one of {sorted(_REGISTRY)}).")
    return dict(_REGISTRY[scope])


# =============================================================================
# Source-scope metrics (one spectral block: 2D float array (n_observations, n_variables))
# =============================================================================
@register("spectral_quality", "source")
def _source_spectral_quality(spectra: np.ndarray) -> dict[str, Any]:
    """Smoothness/noise/range proxies for a source's spectra (delegates to :func:`metrics.spectral_quality`)."""
    return metrics.spectral_quality(spectra)


@register("spectral_profile", "source")
def _source_spectral_profile(spectra: np.ndarray, axis: np.ndarray | None = None, *, sample_ids: list[str] | None = None) -> dict[str, Any]:
    """Full dataset-property profile for a source's spectra."""
    return metrics.spectral_profile(spectra, axis, sample_ids=sample_ids)


@register("value_range", "source")
def _source_value_range(spectra: np.ndarray) -> dict[str, Any]:
    """Overall and per-wavelength-mean value extremes of a source's spectra (NaN-aware)."""
    arr = np.asarray(spectra, dtype="float64")
    if arr.ndim != 2 or arr.size == 0 or not np.isfinite(arr).any():
        return {"value_min": None, "value_max": None, "mean_min": None, "mean_max": None}
    col_mean = np.nanmean(arr, axis=0)
    return {
        "value_min": float(np.nanmin(arr)),
        "value_max": float(np.nanmax(arr)),
        "mean_min": float(np.nanmin(col_mean)),
        "mean_max": float(np.nanmax(col_mean)),
    }


# =============================================================================
# Variable-scope metrics (one Y/metadata column, native dtype)
# =============================================================================
@register("numeric_stats", "variable")
def _variable_numeric_stats(values: Any) -> dict[str, Any]:
    """Descriptive stats for a numeric variable (count/missing/quantiles)."""
    series = np.asarray(values, dtype="float64").ravel()
    n = int(series.size)
    finite = series[np.isfinite(series)]
    n_missing = int(n - finite.size)
    if finite.size == 0:
        return {"n": n, "n_missing": n_missing, "min": None, "max": None, "mean": None, "std": None, "median": None, "q1": None, "q3": None}
    q1, median, q3 = (float(v) for v in np.quantile(finite, [0.25, 0.5, 0.75]))
    return {
        "n": n,
        "n_missing": n_missing,
        "min": float(finite.min()),
        "max": float(finite.max()),
        "mean": float(finite.mean()),
        "std": float(finite.std(ddof=1)) if finite.size > 1 else 0.0,
        "median": median,
        "q1": q1,
        "q3": q3,
    }


@register("categorical_stats", "variable")
def _variable_categorical_stats(values: Any, *, top_k: int = 20) -> dict[str, Any]:
    """Class inventory for a categorical variable (count/missing/n_classes/top classes)."""
    import pandas as pd

    series = pd.Series(values)
    n = int(series.size)
    n_missing = int(series.isna().sum())
    counts = series.dropna().astype(str).value_counts()
    top = [{"name": str(name), "count": int(count)} for name, count in counts.head(top_k).items()]
    return {"n": n, "n_missing": n_missing, "n_classes": int(counts.size), "top_classes": top}


# =============================================================================
# Dataset-scope metrics (aggregate / alignment)
# =============================================================================
@register("reps_per_sample", "dataset")
def _dataset_reps_per_sample(counts_per_sample: Any) -> dict[str, Any] | None:
    """Min/max/mean spectra-per-sample over the per-sample observation counts (None if empty)."""
    arr = np.asarray(counts_per_sample, dtype="float64").ravel()
    arr = arr[np.isfinite(arr) & (arr > 0)]
    if arr.size == 0:
        return None
    return {"min": int(arr.min()), "max": int(arr.max()), "mean": float(arr.mean())}
