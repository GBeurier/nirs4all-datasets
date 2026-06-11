"""Card plots (matplotlib, non-interactive Agg backend), read directly from canonical Parquet.

Two asset families, mirroring the card's two computed blocks:

* **per-source** (``assets/<source_id>/*.png``): the mean spectrum +/- std envelope and, when a 2D
  PCA projection is available, a PC1xPC2 scatter — one set per spectral block, so an asymmetric
  multi-source dataset is shown source-by-source;
* **per-variable** (``assets/variables/<name>.png``): a histogram (numeric) or a class-count bar
  (categorical) for *every* Y/metadata column — so a metadata-only dataset still gets dataviz.

Wavelength axes use the source's numeric column headers (the canonical spectral column names are the
wavelengths as strings) when parseable, else the feature index. Every plot is best-effort: a failure
or an inapplicable plot is recorded as a warning and skipped, never failing the card. The PCA path
reuses nirs4all's ``compute_pca_projection`` (None + warning when unavailable). Asset paths are
returned (relative to the dataset dir) so :mod:`profile` records them.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from nirs4all_datasets.qualify import metrics  # noqa: E402

_COLOR = "#0b7285"
_ACCENT = "#e8590c"
_PCA_MAX_ROWS = 4000
# Sanitize a source_id / variable name into a safe file stem (the card path uses the raw name; the
# file on disk is slugified so an exotic column name cannot escape assets/).
_SAFE_RE = re.compile(r"[^A-Za-z0-9._-]+")


def _safe_stem(name: str) -> str:
    """A filesystem-safe stem for an asset file (collapses unsafe chars to ``_``)."""
    stem = _SAFE_RE.sub("_", str(name)).strip("_")
    return stem or "unnamed"


def _spectral_block(df: Any) -> tuple[np.ndarray, np.ndarray, str]:
    """Return ``(spectra, axis, axis_label)`` for a source Parquet frame.

    ``spectra`` is the float spectral matrix (the columns after ``observation_id``/``sample_id``);
    ``axis`` is the numeric wavelength axis parsed from those column headers, or the feature index
    when the headers are not all numeric; ``axis_label`` names it.
    """
    spectral_cols = [c for c in df.columns if c not in ("observation_id", "sample_id")]
    spectra = df[spectral_cols].to_numpy(dtype="float64")
    parsed: list[float] = []
    numeric = True
    for col in spectral_cols:
        try:
            parsed.append(float(col))
        except (TypeError, ValueError):
            numeric = False
            break
    if numeric and parsed:
        return spectra, np.asarray(parsed, dtype="float64"), "wavelength"
    return spectra, np.arange(len(spectral_cols), dtype="float64"), "feature index"


def _spectra_envelope(spectra: np.ndarray, axis: np.ndarray, axis_label: str, out_path: Path, title: str) -> bool:
    """Mean spectrum with a +/- 1 std band; False if the block is too small to plot."""
    if spectra.ndim != 2 or spectra.shape[0] < 1 or spectra.shape[1] < 2:
        return False
    mean = np.nanmean(spectra, axis=0)
    std = np.nanstd(spectra, axis=0)
    fig, ax = plt.subplots(figsize=(7.0, 3.5))
    ax.plot(axis, mean, lw=1.0, color=_COLOR)
    ax.fill_between(axis, mean - std, mean + std, alpha=0.25, color=_COLOR, linewidth=0)
    ax.set_xlabel(axis_label)
    ax.set_ylabel("signal")
    ax.set_title(title)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return True


def _pca_scatter(spectra: np.ndarray, out_path: Path, title: str) -> bool:
    """PC1xPC2 scatter of a source's (NaN-imputed, subsampled) spectra; False if unavailable."""
    from nirs4all.analysis.projections import compute_pca_projection

    if spectra.ndim != 2 or spectra.shape[0] < 3 or spectra.shape[1] < 2:
        return False
    filled, _ = metrics.impute_columns(spectra)
    n = filled.shape[0]
    idx = np.sort(np.random.RandomState(0).choice(n, _PCA_MAX_ROWS, replace=False)) if n > _PCA_MAX_ROWS else np.arange(n)
    proj = compute_pca_projection(np.asarray(filled[idx], dtype="float64"), max_components=2, variance_threshold=0.999)
    coords = np.asarray(proj["coordinates"], dtype=float)
    if coords.ndim != 2 or coords.shape[1] < 2:
        return False
    evr = proj["explained_variance_ratio"]
    fig, ax = plt.subplots(figsize=(5.2, 4.2))
    ax.scatter(coords[:, 0], coords[:, 1], s=10, alpha=0.7, color=_COLOR)
    ax.set_xlabel(f"PC1 ({evr[0] * 100:.1f}%)")
    ax.set_ylabel(f"PC2 ({evr[1] * 100:.1f}%)" if len(evr) > 1 else "PC2")
    ax.set_title(title)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return True


def render_source_assets(source_id: str, df: Any, assets_dir: Path, warnings: list[str]) -> list[str]:
    """Render a source's plots into ``assets_dir/<source_id>/`` and return their relpaths.

    Args:
        source_id: The source identifier (``X`` / ``X1`` ...), used as the sub-directory + plot label.
        df: The source's Parquet frame (``observation_id``/``sample_id`` + spectral columns).
        assets_dir: The dataset's ``assets`` directory.
        warnings: List appended to on any per-plot failure.

    Returns:
        The relpaths (``assets/<source_id>/*.png``) of the plots that were written.
    """
    sub = assets_dir / _safe_stem(source_id)
    sub.mkdir(parents=True, exist_ok=True)
    spectra, axis, axis_label = _spectral_block(df)
    assets: list[str] = []
    plots: list[tuple[str, Any]] = [
        ("spectra_envelope", lambda p: _spectra_envelope(spectra, axis, axis_label, p, f"{source_id}: mean spectrum +/- std")),
        ("pca_scatter", lambda p: _pca_scatter(spectra, p, f"{source_id}: PCA projection")),
    ]
    for name, fn in plots:
        path = sub / f"{name}.png"
        try:
            if fn(path) and path.exists():
                assets.append(f"assets/{_safe_stem(source_id)}/{name}.png")
        except Exception as exc:  # noqa: BLE001 - one plot must never fail the dataset
            warnings.append(f"plot {source_id}/{name} failed: {type(exc).__name__}")
    return assets


def _variable_plot(values: Any, is_numeric: bool, out_path: Path, name: str) -> bool:
    """Histogram (numeric) or class-count bar (categorical) for one variable; False if nothing to show."""
    import pandas as pd

    fig, ax = plt.subplots(figsize=(5.0, 3.5))
    drawn = False
    if is_numeric:
        finite = np.asarray(values, dtype="float64").ravel()
        finite = finite[np.isfinite(finite)]
        if finite.size:
            ax.hist(finite, bins=min(30, max(5, finite.size // 5)), color=_COLOR)
            ax.set_xlabel(name)
            ax.set_ylabel("count")
            drawn = True
    else:
        counts = pd.Series(values).dropna().astype(str).value_counts().head(20)
        if counts.size:
            ax.bar([str(i) for i in counts.index], counts.to_numpy(), color=_ACCENT)
            ax.set_ylabel("count")
            ax.tick_params(axis="x", rotation=45)
            drawn = True
    if not drawn:
        plt.close(fig)
        return False
    ax.set_title(f"{name} distribution")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return True


def render_variable_asset(name: str, values: Any, is_numeric: bool, assets_dir: Path, warnings: list[str]) -> list[str]:
    """Render one variable's dataviz into ``assets_dir/variables/`` and return its relpath (or ``[]``)."""
    sub = assets_dir / "variables"
    sub.mkdir(parents=True, exist_ok=True)
    stem = _safe_stem(name)
    path = sub / f"{stem}.png"
    try:
        if _variable_plot(values, is_numeric, path, name) and path.exists():
            return [f"assets/variables/{stem}.png"]
    except Exception as exc:  # noqa: BLE001 - one plot must never fail the dataset
        warnings.append(f"plot variables/{name} failed: {type(exc).__name__}")
    return []
