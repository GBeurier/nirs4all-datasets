"""Build a dataset identity ``card.json`` by reusing nirs4all + the descriptive metrics.

The card combines hand-authored identity/provenance (the descriptor) with computed inventory,
spectral, target, quality, and integrity sections. nirs4all does the heavy lifting
(``get_dataset_metadata``, ``detect_signal_type``, ``nan_summary``, outlier-filter stats,
``core.metrics.get_stats``); :mod:`nirs4all_datasets.qualify.metrics` fills the gaps.

Section keys are stable: when an optional computation fails, the value is ``None`` and a message
is appended to the card's ``warnings`` list (failures are never silently dropped). The outlier
path is seeded (``random_state=0``) so the card is reproducible apart from the volatile
``integrity.generated_at`` timestamp. All values are sanitized to finite JSON (no NaN/Inf).
"""
from __future__ import annotations

import json
import math
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import numpy as np

from nirs4all_datasets.ingest import resolve_config
from nirs4all_datasets.manifest import descriptor_hash
from nirs4all_datasets.qualify import metrics
from nirs4all_datasets.qualify.plots import render_card_assets
from nirs4all_datasets.schema import DatasetDescriptor

SCHEMA_VERSION = "1.0"


def _jsonify(obj: Any) -> Any:
    """Recursively convert numpy scalars/arrays and replace non-finite floats with None."""
    if isinstance(obj, (float, np.floating)):
        value = float(obj)
        return value if math.isfinite(value) else None
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.ndarray):
        return [_jsonify(v) for v in obj.tolist()]
    if isinstance(obj, dict):
        return {k: _jsonify(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_jsonify(v) for v in obj]
    return obj


def _features(dataset: Any, selector: dict[str, str]) -> np.ndarray:
    x = dataset.x(selector, layout="2d", concat_source=False)
    return np.asarray(x[0] if isinstance(x, list) else x, dtype=float)


def _train_features(dataset: Any) -> np.ndarray:
    train = _features(dataset, {"partition": "train"})
    return train if train.shape[0] else _features(dataset, {})


def _inventory(dataset: Any) -> dict[str, Any]:
    n_features = dataset.num_features if isinstance(dataset.num_features, int) else dataset.num_features[0]
    inventory: dict[str, Any] = {
        "n_samples": int(dataset.num_samples),
        "n_features": int(n_features),
        "n_sources": int(dataset.n_sources),
        "task_type": dataset.task_type.value if dataset.task_type is not None else None,
        "n_folds": int(dataset.num_folds),
        "metadata_columns": list(dataset.metadata_columns),
        "partitions": None,
    }
    if dataset.is_classification:
        inventory["num_classes"] = int(dataset.num_classes)
    parts = [str(p) for p in dataset.index_column("partition")]
    labels = Counter(p for p in parts if p and p != "None")
    if labels:
        inventory["partitions"] = dict(labels)
    return inventory


def _native_axis(dataset: Any, unit: str) -> np.ndarray | None:
    """Wavelength axis in its *native* unit (so spacing is meaningful); None for non-spectral axes."""
    if unit == "nm":
        return np.asarray(dataset.wavelengths_nm(0), dtype=float)
    if unit == "cm-1":
        return np.asarray(dataset.wavelengths_cm1(0), dtype=float)
    return None


def _spectral(dataset: Any, base: dict[str, Any], n_features: int, warnings: list[str]) -> dict[str, Any]:
    unit = dataset.header_unit(0)
    spectral: dict[str, Any] = {
        "wavelength_unit": unit,
        "n_wavelengths": int(n_features),
        "wavelength_range": base.get("wavelength_range"),
        "spacing": None,
        "spacing_unit": None,
        "signal_type": None,
        "signal_type_confidence": None,
        "signal_type_reason": None,
    }
    axis = _native_axis(dataset, unit)
    if axis is not None and axis.size:
        spectral["spacing"] = metrics.wavelength_spacing(axis)
        spectral["spacing_unit"] = unit
    elif unit in ("none", "index", "text"):
        warnings.append(f"wavelength spacing not computed for non-spectral axis (unit={unit!r})")
    try:
        signal_type, confidence, reason = dataset.detect_signal_type(0)
        spectral["signal_type"] = getattr(signal_type, "value", str(signal_type))
        spectral["signal_type_confidence"] = float(confidence)
        spectral["signal_type_reason"] = reason
    except Exception as exc:  # noqa: BLE001 - detection is best-effort
        warnings.append(f"signal type detection failed: {type(exc).__name__}")
    return spectral


def _targets(dataset: Any, base: dict[str, Any], warnings: list[str]) -> dict[str, Any]:
    if dataset.is_classification:
        distribution = (base.get("y_stats") or {}).get("class_distribution") or {}
        out: dict[str, Any] = {"task_type": "classification", "class_distribution": distribution, "balance": None}
        if distribution:
            out["balance"] = metrics.class_balance(list(distribution.values()))
        return out
    y = np.asarray(dataset.y({}), dtype=float).ravel()
    try:
        import nirs4all.core.metrics as core_metrics

        stats = core_metrics.get_stats(y)
    except Exception as exc:  # noqa: BLE001 - fall back to dataset metadata
        warnings.append(f"regression stats fallback: {type(exc).__name__}")
        stats = base.get("y_stats", {})
    return {"task_type": "regression", "stats": stats, "shape": metrics.distribution_shape(y)}


def _quality(dataset: Any, x_outlier_method: str, warnings: list[str]) -> dict[str, Any]:
    quality: dict[str, Any] = {"has_nan": bool(dataset.has_nan), "nan": dataset.nan_summary, "x_outliers": None}
    train = _train_features(dataset)
    quality["spectral"] = metrics.spectral_quality(train)
    try:
        from nirs4all.operators.filters import XOutlierFilter

        filt = XOutlierFilter(method=x_outlier_method, random_state=0)
        filt.fit(train)
        quality["x_outliers"] = {"method": x_outlier_method, **filt.get_filter_stats(train)}
    except Exception as exc:  # noqa: BLE001 - outlier detection is best-effort
        warnings.append(f"x-outlier detection failed: {type(exc).__name__}")
    return quality


def build_card(dataset_dir: str | Path, descriptor: DatasetDescriptor, *, compute_assets: bool = True, x_outlier_method: str = "robust_mahalanobis") -> dict[str, Any]:
    """Build (and write) the identity card for a dataset directory.

    Loads the canonical form via :func:`resolve_config`, assembles the card, renders the plot
    assets into ``<dataset_dir>/assets/`` and writes a finite, JSON-valid ``<dataset_dir>/card.json``.
    """
    import nirs4all
    from nirs4all.data import DatasetConfigs

    dataset_dir = Path(dataset_dir)
    dataset = DatasetConfigs(resolve_config(dataset_dir)).get_dataset_at(0)
    base = dataset.get_dataset_metadata(include_y_stats=True) or {}
    gov = descriptor.governance
    warnings: list[str] = []
    if dataset.n_sources != 1:
        warnings.append(f"multi-source dataset (n_sources={dataset.n_sources}); profiling source 0 only")

    inventory = _inventory(dataset)
    card: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "identity": {
            "id": descriptor.id,
            "name": descriptor.name,
            "version": descriptor.version,
            "domain": descriptor.domain,
            "description": descriptor.description,
            "keywords": descriptor.keywords,
            "license": gov.license,
            "visibility": gov.visibility.value,
            "doi": descriptor.dataverse.doi,
        },
        "inventory": inventory,
        "spectral": _spectral(dataset, base, inventory["n_features"], warnings),
        "targets": _targets(dataset, base, warnings),
        "quality": _quality(dataset, x_outlier_method, warnings),
        "integrity": {
            "content_hash": dataset.content_hash(),
            "nirs4all_version": nirs4all.__version__,
            "descriptor_hash": descriptor_hash(descriptor),
            "generated_at": datetime.now(UTC).isoformat(),  # volatile (excluded from reproducibility)
        },
        "warnings": warnings,
        "assets": {},
    }

    if compute_assets:
        card["assets"] = render_card_assets(dataset, dataset_dir / "assets")

    card = _jsonify(card)
    (dataset_dir / "card.json").write_text(json.dumps(card, indent=2, sort_keys=True, allow_nan=False), encoding="utf-8")
    return card
