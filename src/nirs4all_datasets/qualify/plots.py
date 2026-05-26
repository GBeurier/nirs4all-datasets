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


def render_card_assets(dataset: Any, assets_dir: Path) -> dict[str, str]:
    """Render the card plots into ``assets_dir``; return {name: relative path} for the card."""
    assets_dir = Path(assets_dir)
    assets_dir.mkdir(parents=True, exist_ok=True)
    spectra_envelope(dataset, assets_dir / "spectra_envelope.png")
    target_distribution(dataset, assets_dir / "target_distribution.png")
    return {
        "spectra_envelope": "assets/spectra_envelope.png",
        "target_distribution": "assets/target_distribution.png",
    }
