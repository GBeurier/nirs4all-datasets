"""Card plots (matplotlib, non-interactive Agg backend) written as PNGs.

The MVP set is the two most informative dataset plots: the mean spectrum +/- std envelope and
the target distribution. Wavelength axes reuse nirs4all's ``get_x_values_and_label`` helper when
available so the units (nm / cm-1) are correct.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

_COLOR = "#0b7285"


def _x_axis(dataset: Any, n_features: int) -> tuple[np.ndarray, str]:
    try:
        from nirs4all.utils.header_units import get_x_values_and_label

        values, label = get_x_values_and_label(dataset.headers(0), dataset.header_unit(0), n_features)
        return np.asarray(values, dtype=float), str(label)
    except Exception:  # noqa: BLE001 - fall back to feature index
        return np.arange(n_features, dtype=float), "feature index"


def _features(dataset: Any) -> np.ndarray:
    x = dataset.x({}, layout="2d", concat_source=False)
    return np.asarray(x[0] if isinstance(x, list) else x, dtype=float)


def spectra_envelope(dataset: Any, out_path: Path) -> None:
    """Plot the mean spectrum with a +/- 1 std band."""
    x = _features(dataset)
    axis, label = _x_axis(dataset, x.shape[1])
    mean = np.nanmean(x, axis=0)
    std = np.nanstd(x, axis=0)
    fig, ax = plt.subplots(figsize=(7.0, 3.5))
    ax.plot(axis, mean, lw=1.0, color=_COLOR)
    ax.fill_between(axis, mean - std, mean + std, alpha=0.25, color=_COLOR, linewidth=0)
    ax.set_xlabel(label)
    ax.set_ylabel("signal")
    ax.set_title("Mean spectrum ± std")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def target_distribution(dataset: Any, out_path: Path) -> None:
    """Histogram (regression) or class-count bar (classification) of the target."""
    y = np.asarray(dataset.y({})).ravel()
    fig, ax = plt.subplots(figsize=(5.0, 3.5))
    if dataset.is_classification:
        values, counts = np.unique(y, return_counts=True)
        ax.bar([str(v) for v in values], counts, color=_COLOR)
        ax.set_ylabel("count")
        ax.tick_params(axis="x", rotation=45)
    else:
        finite = y.astype(float)
        finite = finite[np.isfinite(finite)]
        ax.hist(finite, bins=min(30, max(5, finite.size // 5)), color=_COLOR)
        ax.set_xlabel("target")
        ax.set_ylabel("count")
    ax.set_title("Target distribution")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def _partitions(dataset: Any, n: int) -> np.ndarray:
    try:
        parts = np.array([str(p) for p in dataset.index_column("partition")])
        if parts.shape[0] == n:
            return parts
    except Exception:  # noqa: BLE001 - partition column may be absent
        pass
    return np.array(["all"] * n)


def _targets_1d(dataset: Any) -> np.ndarray | None:
    try:
        y = np.asarray(dataset.y({})).ravel()
        return y if y.size else None
    except Exception:  # noqa: BLE001 - targetless datasets may raise on y access
        return None


def pca_scatter(dataset: Any, out_path: Path) -> bool:
    """PC1×PC2 scatter (NaN-imputed, subsampled), colored by target (continuous) or class."""
    from nirs4all.analysis.projections import compute_pca_projection

    from nirs4all_datasets.qualify import metrics

    x = _features(dataset)
    if x.ndim != 2 or x.shape[0] < 3 or x.shape[1] < 2:
        return False
    filled, _ = metrics.impute_columns(x)
    n = filled.shape[0]
    idx = np.sort(np.random.RandomState(0).choice(n, 4000, replace=False)) if n > 4000 else np.arange(n)
    proj = compute_pca_projection(np.asarray(filled[idx], dtype="float64"), max_components=2, variance_threshold=0.999)
    coords = np.asarray(proj["coordinates"], dtype=float)
    if coords.shape[1] < 2:
        return False
    evr = proj["explained_variance_ratio"]
    y = _targets_1d(dataset)
    fig, ax = plt.subplots(figsize=(5.2, 4.2))
    if y is not None and y.shape[0] == n and dataset.is_classification:
        ys = y[idx]
        for cls in np.unique(ys):
            mask = ys == cls
            ax.scatter(coords[mask, 0], coords[mask, 1], s=10, alpha=0.7, label=f"{int(cls)}")
        ax.legend(title="class", fontsize=7, markerscale=1.3)
    elif y is not None and y.shape[0] == n:
        sc = ax.scatter(coords[:, 0], coords[:, 1], s=10, alpha=0.7, c=y[idx].astype(float), cmap="viridis")
        fig.colorbar(sc, ax=ax, label="target")
    else:
        ax.scatter(coords[:, 0], coords[:, 1], s=10, alpha=0.7, color=_COLOR)
    ax.set_xlabel(f"PC1 ({evr[0] * 100:.1f}%)")
    ax.set_ylabel(f"PC2 ({evr[1] * 100:.1f}%)" if len(evr) > 1 else "PC2")
    ax.set_title("PCA projection")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return True


def class_or_quantile_spectra(dataset: Any, out_path: Path) -> bool:
    """Per-class mean spectra (classification) or per-quartile mean spectra (regression)."""
    from matplotlib import colormaps

    x = _features(dataset)
    if x.ndim != 2 or x.shape[0] < 2 or x.shape[1] < 2:
        return False
    axis, label = _x_axis(dataset, x.shape[1])
    y = _targets_1d(dataset)
    fig, ax = plt.subplots(figsize=(7.0, 3.5))
    if y is not None and y.shape[0] == x.shape[0] and dataset.is_classification:
        classes = np.unique(y)
        for cls, col in zip(classes, colormaps["viridis"](np.linspace(0, 1, max(len(classes), 1))), strict=False):
            ax.plot(axis, np.nanmean(x[y == cls], axis=0), lw=1.0, color=col, label=f"{int(cls)}")
        ax.legend(title="class", fontsize=7, ncol=2)
        ax.set_title("Mean spectrum per class")
    elif y is not None and y.shape[0] == x.shape[0] and np.isfinite(y.astype(float)).any():
        yf = y.astype(float)
        finite = np.isfinite(yf)
        edges = np.quantile(yf[finite], [0.0, 0.25, 0.5, 0.75, 1.0])
        colors = colormaps["viridis"](np.linspace(0, 1, 4))
        for i in range(4):
            lo, hi = float(edges[i]), float(edges[i + 1])
            mask = finite & (yf >= lo) & ((yf <= hi) if i == 3 else (yf < hi))
            if mask.sum():
                ax.plot(axis, np.nanmean(x[mask], axis=0), lw=1.0, color=colors[i], label=f"Q{i + 1} [{lo:.3g}, {hi:.3g}]")
        ax.legend(title="target quartile", fontsize=7)
        ax.set_title("Mean spectrum per target quartile")
    else:
        ax.plot(axis, np.nanmean(x, axis=0), lw=1.0, color=_COLOR)
        ax.set_title("Mean spectrum")
    ax.set_xlabel(label)
    ax.set_ylabel("signal")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return True


def train_test_overlay(dataset: Any, out_path: Path) -> bool:
    """Overlay train vs test mean spectra (±std); only when both partitions are present."""
    x = _features(dataset)
    parts = _partitions(dataset, x.shape[0])
    labels = set(parts.tolist())
    if not {"train", "test"} <= labels:
        return False
    axis, label = _x_axis(dataset, x.shape[1])
    fig, ax = plt.subplots(figsize=(7.0, 3.5))
    for name, color in (("train", _COLOR), ("test", "#e8590c")):
        mask = parts == name
        if mask.sum():
            mean, std = np.nanmean(x[mask], axis=0), np.nanstd(x[mask], axis=0)
            ax.plot(axis, mean, lw=1.0, color=color, label=f"{name} (n={int(mask.sum())})")
            ax.fill_between(axis, mean - std, mean + std, alpha=0.15, color=color, linewidth=0)
    ax.legend(fontsize=8)
    ax.set_xlabel(label)
    ax.set_ylabel("signal")
    ax.set_title("Train vs test mean spectrum")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return True


def render_card_assets(dataset: Any, assets_dir: Path, warnings: list[str] | None = None) -> dict[str, str]:
    """Render the card plots into ``assets_dir``; return {name: relative path} for the card.

    Each plot is best-effort: a failure (or a plot that does not apply, e.g. target plots on a
    targetless dataset, or the train/test overlay without a split) is recorded as a warning and
    skipped, never failing the whole card.
    """
    assets_dir = Path(assets_dir)
    assets_dir.mkdir(parents=True, exist_ok=True)
    warnings = warnings if warnings is not None else []
    try:
        has_targets = np.asarray(dataset.y({})).size > 0
    except Exception:  # noqa: BLE001 - targetless datasets may raise on y access
        has_targets = False

    plots: list[tuple[str, Any, bool]] = [
        ("spectra_envelope", spectra_envelope, True),
        ("target_distribution", target_distribution, has_targets),
        ("pca_scatter", pca_scatter, True),
        ("class_spectra", class_or_quantile_spectra, True),
        ("train_test_overlay", train_test_overlay, True),
    ]
    assets: dict[str, str] = {}
    for name, fn, applicable in plots:
        if not applicable:
            continue
        path = assets_dir / f"{name}.png"
        try:
            if fn(dataset, path) is not False and path.exists():
                assets[name] = f"assets/{name}.png"
        except Exception as exc:  # noqa: BLE001 - one plot must never fail the dataset
            warnings.append(f"plot {name} failed: {type(exc).__name__}")
    return assets
