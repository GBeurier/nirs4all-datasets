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
from scipy import stats

from nirs4all_datasets.ingest import resolve_config
from nirs4all_datasets.manifest import descriptor_hash, metadata_hash, read_manifest
from nirs4all_datasets.qualify import metrics
from nirs4all_datasets.qualify.croissant import render_croissant
from nirs4all_datasets.qualify.datasheet import render_datasheet
from nirs4all_datasets.qualify.plots import render_card_assets
from nirs4all_datasets.schema import DatasetDescriptor, FileRole

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
    return np.asarray(x[0] if isinstance(x, list) else x, dtype="float32")  # float32 to bound memory on large X


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


def _native_axis(dataset: Any, unit: str, src: int = 0) -> np.ndarray | None:
    """Wavelength axis in its *native* unit (so spacing is meaningful); None for non-spectral axes.

    Exception-safe: some headers carry unit suffixes (e.g. ``852.78_nm``) nirs4all cannot parse to a
    float axis — that degrades the spectral summary but must never fail the card.
    """
    try:
        if unit == "nm":
            return np.asarray(dataset.wavelengths_nm(src), dtype=float)
        if unit == "cm-1":
            return np.asarray(dataset.wavelengths_cm1(src), dtype=float)
    except Exception:  # noqa: BLE001 - unparseable header axis is non-fatal
        return None
    return None


def _per_source(dataset: Any) -> list[dict[str, Any]]:
    """Per-source spectral summary (for multi-source datasets)."""
    features = dataset.num_features if isinstance(dataset.num_features, list) else [dataset.num_features]
    entries: list[dict[str, Any]] = []
    for src in range(dataset.n_sources):
        unit = dataset.header_unit(src)
        entry: dict[str, Any] = {"source": src, "n_features": int(features[src]), "wavelength_unit": unit, "spacing": None, "signal_type": None}
        axis = _native_axis(dataset, unit, src)
        if axis is not None and axis.size:
            entry["spacing"] = metrics.wavelength_spacing(axis)
            entry["wavelength_range"] = [float(axis.min()), float(axis.max())]
        try:
            signal_type, confidence, _ = dataset.detect_signal_type(src)
            entry["signal_type"] = getattr(signal_type, "value", str(signal_type))
            entry["signal_type_confidence"] = float(confidence)
        except Exception:  # noqa: BLE001 - detection optional
            pass
        entries.append(entry)
    return entries


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
        if spectral["wavelength_range"] is None:  # derive from the (parsed) axis if nirs4all didn't supply it
            spectral["wavelength_range"] = [float(axis.min()), float(axis.max())]
    elif unit in ("none", "index", "text"):
        warnings.append(f"wavelength spacing not computed for non-spectral axis (unit={unit!r})")
    else:
        warnings.append(f"wavelength axis unavailable (unit={unit!r}; header values not parseable, e.g. unit-suffixed)")
    try:
        signal_type, confidence, reason = dataset.detect_signal_type(0)
        spectral["signal_type"] = getattr(signal_type, "value", str(signal_type))
        spectral["signal_type_confidence"] = float(confidence)
        spectral["signal_type_reason"] = reason
    except Exception as exc:  # noqa: BLE001 - detection is best-effort
        warnings.append(f"signal type detection failed: {type(exc).__name__}")
    return spectral


def _targets(dataset: Any, base: dict[str, Any], warnings: list[str]) -> dict[str, Any]:
    try:
        has_targets = np.asarray(dataset.y({})).size > 0
    except Exception:  # noqa: BLE001 - targetless datasets may raise on y access
        has_targets = False
    if not has_targets:
        return {"task_type": None, "note": "no targets (unsupervised / prediction set)"}
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
    quality["spectral"] = metrics.spectral_quality(train)  # nan-aware (nanmean/MAD)
    filled, imputed = metrics.impute_columns(train)  # XOutlierFilter (Mahalanobis/PCA) cannot ingest NaN
    try:
        from nirs4all.operators.filters import XOutlierFilter

        filt = XOutlierFilter(method=x_outlier_method, random_state=0)
        filt.fit(filled)
        quality["x_outliers"] = {"method": x_outlier_method, "imputed": imputed if imputed["n_nan_cells"] else None, **filt.get_filter_stats(filled)}
    except Exception as exc:  # noqa: BLE001 - outlier detection is best-effort
        warnings.append(f"x-outlier detection failed: {type(exc).__name__}")
    return quality


_DIM_MAX_ROWS = 4000
_DIM_MAX_COMPONENTS = 60


def _subsample(x: np.ndarray, max_rows: int, seed: int) -> tuple[np.ndarray, int]:
    """Row-subsample (seeded) to bound PCA/plot cost on large datasets; returns ``(x, n_rows_used)``."""
    if x.shape[0] <= max_rows:
        return x, int(x.shape[0])
    idx = np.sort(np.random.RandomState(seed).choice(x.shape[0], max_rows, replace=False))
    return x[idx], int(max_rows)


def _partition_set(dataset: Any) -> set[str]:
    try:
        return {str(p) for p in dataset.index_column("partition")}
    except Exception:  # noqa: BLE001 - partition column may be absent
        return set()


def _class_counts(dataset: Any, partition: str) -> dict[str, int]:
    """Per-partition class counts keyed by the (integer) class index as a string."""
    y = np.asarray(dataset.y({"partition": partition})).ravel()
    if y.size == 0:
        return {}
    vals, counts = np.unique(y, return_counts=True)
    out: dict[str, int] = {}
    for v, c in zip(vals, counts, strict=False):
        try:
            key = str(int(v))
        except (ValueError, TypeError):
            key = str(v)
        out[key] = int(c)
    return out


def _dimensionality(dataset: Any, warnings: list[str]) -> dict[str, Any] | None:
    """PCA dimensionality summary of the (NaN-imputed, subsampled) training spectra.

    Reuses nirs4all's ``compute_pca_projection``; reports leading explained variance, components to
    reach 95%/99% variance (censored ``">k"`` when truncated), and the effective rank, with the
    row/component budget and any imputation disclosed (honest, reproducible).
    """
    from nirs4all.analysis.projections import compute_pca_projection

    x = _train_features(dataset)
    if x.ndim != 2 or x.shape[0] < 2 or x.shape[1] < 2:
        return None
    filled, imputed = metrics.impute_columns(x)
    sub, n_rows = _subsample(filled, _DIM_MAX_ROWS, seed=0)
    k = int(min(_DIM_MAX_COMPONENTS, sub.shape[0] - 1, sub.shape[1]))
    if k < 2:
        return None
    try:
        proj = compute_pca_projection(np.asarray(sub, dtype="float64"), max_components=k, variance_threshold=0.999)
    except Exception as exc:  # noqa: BLE001 - PCA is best-effort
        warnings.append(f"dimensionality (PCA) failed: {type(exc).__name__}")
        return None
    evr = np.asarray(proj["explained_variance_ratio"], dtype=float)
    cum = np.cumsum(evr)

    def _n_for(threshold: float) -> int | str:
        if cum.size == 0 or float(cum[-1]) < threshold:
            return f">{k}"
        return int(np.searchsorted(cum, threshold) + 1)

    return {
        "n_rows_used": int(n_rows),
        "n_features": int(x.shape[1]),
        "n_components_computed": int(k),
        "explained_variance_ratio": [float(v) for v in evr[:10]],
        "cumulative_variance_top10": float(cum[min(9, cum.size - 1)]),
        "n_components_95": _n_for(0.95),
        "n_components_99": _n_for(0.99),
        "effective_rank": metrics.effective_rank(proj["explained_variance"]),
        "imputed": imputed if imputed["n_nan_cells"] else None,
        "seed": 0,
    }


def _x_pca_shift(dataset: Any, warnings: list[str]) -> dict[str, Any] | None:
    """Train↔test covariate shift: standardized centroid distance + PC1 KS in a shared PCA space."""
    from nirs4all.analysis.projections import compute_pca_projection

    xtr, _ = _subsample(metrics.impute_columns(_features(dataset, {"partition": "train"}))[0], _DIM_MAX_ROWS, seed=0)
    raw_test = _features(dataset, {"partition": "test"})
    xte, _ = _subsample(metrics.impute_columns(raw_test, reference=_features(dataset, {"partition": "train"}))[0], _DIM_MAX_ROWS, seed=1)
    if xtr.shape[0] < 2 or xte.shape[0] < 2 or xtr.shape[1] != xte.shape[1]:
        return None
    stacked = np.asarray(np.vstack([xtr, xte]), dtype="float64")
    k = int(min(10, stacked.shape[0] - 1, stacked.shape[1]))
    if k < 2:
        return None
    try:
        proj = compute_pca_projection(stacked, max_components=k, variance_threshold=0.999)
    except Exception as exc:  # noqa: BLE001 - best-effort
        warnings.append(f"x-shift PCA failed: {type(exc).__name__}")
        return None
    coords = np.asarray(proj["coordinates"], dtype=float)
    scale = np.sqrt(np.where(np.asarray(proj["explained_variance"], dtype=float) > 0, proj["explained_variance"], 1.0))
    tr, te = coords[: xtr.shape[0]], coords[xtr.shape[0] :]
    ks = stats.ks_2samp(tr[:, 0], te[:, 0])
    return {
        "pc_space_centroid_distance_std": float(np.sqrt(np.sum(((te.mean(0) - tr.mean(0)) / scale) ** 2))),
        "pc1_ks_statistic": float(ks.statistic),
        "pc1_ks_p": float(ks.pvalue),
        "n_components": int(k),
    }


def _shift(dataset: Any, warnings: list[str]) -> dict[str, Any] | None:
    """Train↔test distribution shift (only when a test partition exists)."""
    if "test" not in _partition_set(dataset):
        return None
    out: dict[str, Any] = {"covariate": _x_pca_shift(dataset, warnings)}
    try:
        if dataset.is_classification:
            out["target"] = metrics.class_shift(_class_counts(dataset, "train"), _class_counts(dataset, "test"))
        else:
            ytr = np.asarray(dataset.y({"partition": "train"}), dtype=float)
            yte = np.asarray(dataset.y({"partition": "test"}), dtype=float)
            out["target"] = metrics.target_shift(ytr, yte)
    except Exception as exc:  # noqa: BLE001 - best-effort
        warnings.append(f"target shift failed: {type(exc).__name__}")
        out["target"] = None
    return out


def _target_partitions(dataset: Any, warnings: list[str]) -> dict[str, Any] | None:
    """Per-partition target summary (train vs test): regression stats or class counts."""
    present = [p for p in ("train", "test") if p in _partition_set(dataset)]
    if len(present) < 2:
        return None
    if dataset.is_classification:
        return {p: _class_counts(dataset, p) for p in present}
    import nirs4all.core.metrics as core_metrics

    out: dict[str, Any] = {}
    for p in present:
        y = np.asarray(dataset.y({"partition": p}), dtype=float).ravel()
        y = y[np.isfinite(y)]
        try:
            out[p] = core_metrics.get_stats(y) if y.size else None
        except Exception:  # noqa: BLE001 - best-effort
            out[p] = None
    return out


def _provenance_section(descriptor: DatasetDescriptor) -> dict[str, Any]:
    """Surfaced origin + citation block: where the bytes come from and how to cite the dataset.

    ``sources`` are the original (authoritative) homes (data DOIs/URLs); ``publications`` are the
    related papers (journal DOIs). The two are kept apart so a paper is never advertised as a data
    source. ``republished_doi`` is our own minted Dataverse DOI when published.
    """
    pubs = descriptor.datacite.related_publications if descriptor.datacite else []
    return {
        "contributor": descriptor.provenance.contributor,
        "reference_method": descriptor.provenance.reference_method,
        "sources": [{"kind": s.kind.value, "mode": s.mode.value, "locator": s.locator, "access": s.access.value, "license": s.license, "title": s.title} for s in descriptor.sources],
        "citation": descriptor.citation,
        "publications": [{"doi": p.doi, "title": p.title, "authors": p.authors, "year": p.year, "citation": p.citation} for p in pubs],
        "republished_doi": descriptor.dataverse.doi,
        "dataset_version": descriptor.dataverse.dataset_version,
    }


def _traceability(descriptor: DatasetDescriptor, manifest: Any, manifest_fresh: bool) -> dict[str, Any]:
    """The origin -> raw -> canonical -> card hash chain. The manifest is the byte-identity authority.

    ``manifest_fresh`` is False when the manifest's ``descriptor_hash`` no longer matches the current
    descriptor (a rebuild is due); then the per-file hashes are omitted rather than reported stale.
    """
    raw = [fe.sha256 for fe in manifest.files if fe.role is FileRole.RAW] if manifest_fresh else []
    canonical = {Path(fe.path).name: fe.sha256 for fe in manifest.files if fe.role is FileRole.CANONICAL and fe.path.endswith(".parquet")} if manifest_fresh else {}
    return {
        "origin_locators": [s.locator for s in descriptor.sources],
        "raw_sha256": raw or list(descriptor.provenance.raw_sha256),
        "canonical_sha256": canonical,
        "manifest_fresh": bool(manifest_fresh),
    }


def card_metadata_fresh(card_path: str | Path, descriptor: DatasetDescriptor) -> bool:
    """Whether an existing ``card.json`` displays up-to-date provenance (origin sources, citations).

    Canonical bytes are governed by ``descriptor_hash`` (organize/manifest); the card *also* displays
    metadata, so a metadata-only edit leaves canonical untouched yet must refresh the card. The card
    stores ``integrity.metadata_hash`` for this check. A card that is missing/unreadable or lacks the
    field is treated as **not** fresh (so it gets rebuilt and picks up the current sections).
    """
    path = Path(card_path)
    if not path.exists():
        return False
    try:
        card = json.loads(path.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001 - unreadable card -> rebuild
        return False
    return (card.get("integrity") or {}).get("metadata_hash") == metadata_hash(descriptor)


def build_card(dataset_dir: str | Path, descriptor: DatasetDescriptor, *, compute_assets: bool = True, x_outlier_method: str = "robust_mahalanobis") -> dict[str, Any]:
    """Build (and write) the identity card for a dataset directory.

    Loads the canonical form via :func:`resolve_config`, assembles the card, renders the plot
    assets into ``<dataset_dir>/assets/`` and writes a finite, JSON-valid ``<dataset_dir>/card.json``.
    """
    import nirs4all
    from nirs4all.data import DatasetConfigs

    dataset_dir = Path(dataset_dir)
    dataset = DatasetConfigs(resolve_config(dataset_dir)).get_dataset_at(0)
    warnings: list[str] = []
    try:  # best-effort: e.g. unit-suffixed headers can break the (optional) wavelength_range it computes
        base = dataset.get_dataset_metadata(include_y_stats=True) or {}
    except Exception as exc:  # noqa: BLE001
        warnings.append(f"dataset metadata partially unavailable: {type(exc).__name__}")
        base = {}
    gov = descriptor.governance
    if dataset.n_sources != 1:
        warnings.append(f"multi-source dataset (n_sources={dataset.n_sources}); profiling source 0 only")

    manifest_path = dataset_dir / "manifest.json"
    manifest = read_manifest(manifest_path) if manifest_path.exists() else None
    manifest_fresh = manifest is not None and manifest.descriptor_hash == descriptor_hash(descriptor)

    inventory = _inventory(dataset)
    targets = _targets(dataset, base, warnings)
    if "note" not in targets:  # supervised → attach the per-partition (train/test) breakdown
        targets["partitions"] = _target_partitions(dataset, warnings)
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
        "provenance": _provenance_section(descriptor),
        "inventory": inventory,
        "spectral": _spectral(dataset, base, inventory["n_features"], warnings),
        "targets": targets,
        "dimensionality": _dimensionality(dataset, warnings),
        "shift": _shift(dataset, warnings),
        "quality": _quality(dataset, x_outlier_method, warnings),
        "per_source": _per_source(dataset) if dataset.n_sources > 1 else None,
        "integrity": {
            "content_hash": dataset.content_hash(),
            "nirs4all_version": nirs4all.__version__,
            "descriptor_hash": descriptor_hash(descriptor),
            "metadata_hash": metadata_hash(descriptor),
            "traceability": _traceability(descriptor, manifest, manifest_fresh),
            "generated_at": datetime.now(UTC).isoformat(),  # volatile (excluded from reproducibility)
        },
        "warnings": warnings,
        "assets": {},
    }

    if compute_assets:
        card["assets"] = render_card_assets(dataset, dataset_dir / "assets", warnings)

    card = _jsonify(card)
    (dataset_dir / "card.json").write_text(json.dumps(card, indent=2, sort_keys=True, allow_nan=False), encoding="utf-8")

    # FAIR metadata: human-readable datasheet + machine-readable Croissant.
    (dataset_dir / "card.md").write_text(render_datasheet(descriptor, card), encoding="utf-8")
    files: list[tuple[str, str | None, int | None]] = []
    if manifest_fresh and manifest is not None:  # only a fresh manifest is trusted (computed above)
        files = [(Path(fe.path).name, fe.sha256, fe.file_id) for fe in manifest.files if fe.role is FileRole.CANONICAL and fe.path.endswith(".parquet")]
    croissant = render_croissant(descriptor, card, files=files, instance=descriptor.dataverse.instance)
    (dataset_dir / "croissant.json").write_text(json.dumps(croissant, indent=2), encoding="utf-8")
    return card
