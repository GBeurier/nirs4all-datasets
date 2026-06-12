"""Build a dataset identity ``card.json`` directly from the canonical Parquet (schema 2.0).

The card is the qualification protocol's output: hand-authored identity/provenance/governance (the
descriptor) joined with computed alignment, per-source spectral, per-variable, split, and integrity
sections. It is re-derivable from the canonical bytes alone — :func:`build_card` reads
``canonical/dataset.json`` (via :func:`canonical.resolve_config`) and each source/variables/splits
Parquet, never the raw files — so a ``--protocol-refresh`` (bumping :data:`registry.PROTOCOL_VERSION`)
re-qualifies without rebuilding canonical bytes.

The numerics are not reimplemented here: they are the registered metrics
(:mod:`nirs4all_datasets.qualify.registry`, wrapping :mod:`metrics`) and nirs4all's
``compute_pca_projection``. Card invariants: every section key is stable (a failed optional
computation becomes ``None`` plus a ``warnings[]`` entry, never a dropped key) and every float is
finite-sanitized (no NaN/Inf in the JSON). The card is robust to no-Y (``variables == []``) and to
many-Y (e.g. OSSL's 53 targets + metadata).
"""
from __future__ import annotations

import json
import math
import os
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nirs4all_datasets.canonical import resolve_config
from nirs4all_datasets.manifest import metadata_hash, processing_hash, read_manifest, sha256_bytes
from nirs4all_datasets.qualify import anonymize, croissant, datasheet, registry
from nirs4all_datasets.schema import DatasetDescriptor, Variable, VariableRole, VarType

SCHEMA_VERSION = "2.0"
_OBS_KEY = "observation_id"
_SAMPLE_KEY = "sample_id"
_PCA_MAX_ROWS = 4000
_PCA_MAX_COMPONENTS = 30


# =============================================================================
# Finite-sanitization (salvaged from the prior profile.py)
# =============================================================================
def _jsonify(obj: Any) -> Any:
    """Recursively convert numpy scalars/arrays and replace non-finite floats with ``None``."""
    if isinstance(obj, bool):
        return obj
    if isinstance(obj, (float, np.floating)):
        value = float(obj)
        return value if math.isfinite(value) else None
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, np.ndarray):
        return [_jsonify(v) for v in obj.tolist()]
    if isinstance(obj, dict):
        return {k: _jsonify(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_jsonify(v) for v in obj]
    return obj


# =============================================================================
# Section builders
# =============================================================================
def _identity(descriptor: DatasetDescriptor) -> dict[str, Any]:
    return {
        "id": descriptor.id,
        "name": descriptor.name,
        "domain": descriptor.domain,
        "tier": descriptor.tier.value,
        "description": descriptor.description,
        "keywords": list(descriptor.keywords),
    }


def _versions(descriptor: DatasetDescriptor) -> dict[str, Any]:
    return {"content": descriptor.versions.content, "schema_protocol": descriptor.versions.schema_protocol}


def _governance(descriptor: DatasetDescriptor) -> dict[str, Any]:
    gov = descriptor.governance
    return {
        "license": gov.license,
        "tier": descriptor.tier.value,
        "permitted_use": gov.permitted_use,
        "access_policy": gov.access_policy,
        "redistribution_rights": gov.redistribution_rights,
    }


def _provenance(descriptor: DatasetDescriptor) -> dict[str, Any]:
    """Surfaced origin + citation block (where the bytes live + how to cite), with its own warnings."""
    prov = descriptor.provenance
    return {
        "contributor": prov.contributor,
        "reference_method": prov.reference_method,
        "conversion_status": prov.conversion_status.value if prov.conversion_status is not None else None,
        "origin_sources": [{"kind": s.kind.value, "locator": s.locator, "access": s.access.value, "license": s.license, "title": s.title} for s in descriptor.origin_sources],
        "publications": [{"doi": p.doi, "title": p.title, "year": p.year} for p in descriptor.publications],
        "warnings": list(prov.warnings),
    }


def _alignment(config: dict[str, Any], sample_ids: set[str], reps_counts: list[int], descriptor: DatasetDescriptor, source_profiles: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    n_observations_total = int(sum(int(s.get("n_observations") or 0) for s in config.get("sources", [])))
    reps = registry.metrics_for("dataset")["reps_per_sample"](np.asarray(reps_counts, dtype="float64")) if reps_counts else None
    from nirs4all_datasets.qualify import metrics

    return {
        "level": config.get("alignment_level"),
        "sample_id_available": bool(descriptor.ids.sample_id_available),
        "n_samples": len(sample_ids),
        "n_observations_total": n_observations_total,
        "reps_per_sample": reps,
        "profile_scores": metrics.aggregate_profile_scores(source_profiles or []),
    }


def _source_axis(spectral_cols: list[str]) -> np.ndarray:
    """The numeric wavelength axis parsed from the spectral column headers, or the feature index."""
    parsed: list[float] = []
    for col in spectral_cols:
        try:
            parsed.append(float(col))
        except (TypeError, ValueError):
            return np.arange(len(spectral_cols), dtype="float64")
    return np.asarray(parsed, dtype="float64") if parsed else np.arange(len(spectral_cols), dtype="float64")


def _dimensionality(pca: dict[str, Any] | None) -> dict[str, Any]:
    """Compact PCA dimensionality summary derived from the explained-variance ratios.

    ``effective_rank`` is the entropy-based participation ratio of the variance spectrum (≈ how many
    components really matter); ``n_components_95/99`` are the components to reach that cumulative
    variance; ``cumulative_top10`` is the variance captured by the first 10 components.
    """
    nulls = {"effective_rank": None, "n_components_95": None, "n_components_99": None, "cumulative_top10": None}
    if not pca:
        return nulls
    evr = [float(v) for v in (pca.get("explained_variance_ratio") or []) if isinstance(v, (int, float)) and not isinstance(v, bool)]
    if not evr:
        return nulls
    arr = np.asarray(evr, dtype="float64")
    cum = np.cumsum(arr)
    p = arr / arr.sum()
    effective_rank = float(np.exp(-np.sum(p * np.log(p + 1e-12))))
    n95 = int(np.searchsorted(cum, 0.95) + 1) if cum[-1] >= 0.95 else None
    n99 = int(np.searchsorted(cum, 0.99) + 1) if cum[-1] >= 0.99 else None
    return {"effective_rank": round(effective_rank, 2), "n_components_95": n95, "n_components_99": n99, "cumulative_top10": float(cum[min(9, len(cum) - 1)])}


def _source_section(entry: dict[str, Any], descriptor: DatasetDescriptor, warnings: list[str], *, compute_pca: bool, compute_curve: bool = False) -> tuple[dict[str, Any], pd.DataFrame, set[str]]:
    """Build one ``sources[]`` card entry from a source Parquet; return ``(section, frame, sample_ids)``.

    Reads the Parquet, computes the registered ``value_range``/``spectral_quality`` source metrics and
    (optionally) a PCA explained-variance summary, and pulls the declared :class:`Source` metadata
    (name/instrument/modality). ``sample_ids`` is the set of sample_ids backed by this source's spectra.
    """
    src_warnings: list[str] = []
    source_id = entry["source_id"]
    declared = next((s for s in descriptor.sources if s.source_id == source_id), None)
    df = pd.read_parquet(entry["path"])
    spectral_cols = [c for c in df.columns if c not in (_OBS_KEY, _SAMPLE_KEY)]
    spectra = df[spectral_cols].to_numpy(dtype="float64") if spectral_cols else np.empty((len(df), 0))
    sample_ids = set(df[_SAMPLE_KEY].astype(str)) if _SAMPLE_KEY in df.columns else set()
    sample_id_rows = df[_SAMPLE_KEY].astype(str).tolist() if _SAMPLE_KEY in df.columns else None

    source_metrics = registry.metrics_for("source")
    value_range = source_metrics["value_range"](spectra)
    n_outliers = _x_outliers(spectra, src_warnings)
    pca = _source_pca(spectra, src_warnings) if compute_pca else None

    from nirs4all_datasets.qualify import metrics

    axis = _source_axis(spectral_cols) if spectral_cols else np.empty(0, dtype="float64")
    spectral: dict[str, Any] = {
        "value_min": value_range["value_min"],
        "value_max": value_range["value_max"],
        "mean_min": value_range["mean_min"],
        "mean_max": value_range["mean_max"],
        "n_outliers": n_outliers,
        "pca": pca,
        "quality": metrics.spectral_quality(spectra),
        "spacing": metrics.wavelength_spacing(axis),
        "dimensionality": _dimensionality(pca),
        "profile": source_metrics["spectral_profile"](spectra, axis, sample_ids=sample_id_rows),
        "xy": [],
    }
    if compute_curve and spectral_cols:
        curve = metrics.spectral_curve(spectra, axis)
        if curve is not None:
            spectral["curve"] = curve
        score_plot = metrics.pca_score_plot(spectra)
        if score_plot is not None:
            spectral["score_plot"] = score_plot
    signal_type, signal_conf = _detect_signal_type(spectral_cols, spectra, src_warnings)
    warnings.extend(f"source {source_id}: {w}" for w in src_warnings)
    section = {
        "source_id": source_id,
        "name": declared.name if declared else None,
        "instrument_name": declared.instrument_name if declared else None,
        "modality": declared.modality.value if declared else None,
        "signal_type": signal_type,
        "signal_type_confidence": signal_conf,
        "axis_unit": entry.get("axis_unit"),
        "axis_min": entry.get("axis_min"),
        "axis_max": entry.get("axis_max"),
        "n_observations": int(entry.get("n_observations") or len(df)),
        "n_variables": int(entry.get("n_variables") or len(spectral_cols)),
        "spectral": spectral,
        "assets": [],
        "warnings": src_warnings,
    }
    return section, df, sample_ids


def _attach_xy_metrics(source_sections: list[dict[str, Any]], source_frames: list[pd.DataFrame], variable_sections: list[dict[str, Any]], variables_df: pd.DataFrame | None) -> None:
    """Attach lightweight X-Y metrics to each source: per-target spectral correlation curves."""
    if variables_df is None or _SAMPLE_KEY not in variables_df.columns:
        return
    from nirs4all_datasets.qualify import metrics

    numeric_targets = [v for v in variable_sections if v.get("role") == VariableRole.TARGET.value and v.get("type") == VarType.NUMERIC.value and v.get("name") in variables_df.columns]
    if not numeric_targets:
        return
    y_frame = variables_df[[_SAMPLE_KEY, *[str(v["name"]) for v in numeric_targets]]].copy()
    y_frame[_SAMPLE_KEY] = y_frame[_SAMPLE_KEY].astype(str)
    y_frame = y_frame.drop_duplicates(subset=[_SAMPLE_KEY], keep="first").set_index(_SAMPLE_KEY)
    for section, df in zip(source_sections, source_frames, strict=False):
        if _SAMPLE_KEY not in df.columns:
            continue
        spectral_cols = [c for c in df.columns if c not in (_OBS_KEY, _SAMPLE_KEY)]
        if not spectral_cols:
            continue
        grouped = df[[_SAMPLE_KEY, *spectral_cols]].copy()
        grouped[_SAMPLE_KEY] = grouped[_SAMPLE_KEY].astype(str)
        x_by_sample = grouped.groupby(_SAMPLE_KEY, sort=True)[spectral_cols].mean()
        common = x_by_sample.index.intersection(y_frame.index)
        if len(common) < 3:
            continue
        axis = _source_axis(spectral_cols)
        xy: list[dict[str, Any]] = []
        x_arr = x_by_sample.loc[common].to_numpy(dtype="float64")
        for target in numeric_targets:
            name = str(target["name"])
            y = pd.to_numeric(y_frame.loc[common, name], errors="coerce").to_numpy(dtype="float64")
            corr = metrics.spectral_target_correlation(x_arr, y, axis)
            if corr is not None:
                xy.append({"target": name, **corr})
        if xy:
            section.setdefault("spectral", {})["xy"] = xy


def _x_outliers(spectra: np.ndarray, warnings: list[str]) -> int | None:
    """Count multivariate outliers via nirs4all's ``XOutlierFilter`` (NaN-imputed); None if unavailable."""
    if spectra.ndim != 2 or spectra.shape[0] < 3 or spectra.shape[1] < 2:
        return None
    from nirs4all_datasets.qualify import metrics

    filled, _ = metrics.impute_columns(spectra)
    try:
        from nirs4all.operators.filters import XOutlierFilter

        filt = XOutlierFilter(method="robust_mahalanobis", random_state=0)
        filt.fit(filled)
        stats = filt.get_filter_stats(filled)
    except Exception as exc:  # noqa: BLE001 - outlier detection is best-effort
        warnings.append(f"x-outlier detection failed: {type(exc).__name__}")
        return None
    for key in ("n_excluded", "num_outliers", "n_filtered", "n_outliers"):
        if key in stats:
            try:
                return int(stats[key])
            except (TypeError, ValueError):
                break
    warnings.append("x-outlier count not reported by XOutlierFilter")
    return None


def _source_pca(spectra: np.ndarray, warnings: list[str]) -> dict[str, Any] | None:
    """PCA explained-variance summary of a source's (NaN-imputed, subsampled) spectra; None if unavailable."""
    if spectra.ndim != 2 or spectra.shape[0] < 2 or spectra.shape[1] < 2:
        return None
    from nirs4all_datasets.qualify import metrics

    filled, _ = metrics.impute_columns(spectra)
    n = filled.shape[0]
    idx = np.sort(np.random.RandomState(0).choice(n, _PCA_MAX_ROWS, replace=False)) if n > _PCA_MAX_ROWS else np.arange(n)
    sub = filled[idx]
    k = int(min(_PCA_MAX_COMPONENTS, sub.shape[0] - 1, sub.shape[1]))
    if k < 1:
        return None
    try:
        from nirs4all.analysis.projections import compute_pca_projection

        proj = compute_pca_projection(np.asarray(sub, dtype="float64"), max_components=k, variance_threshold=0.999)
    except Exception as exc:  # noqa: BLE001 - PCA is best-effort
        warnings.append(f"PCA failed: {type(exc).__name__}")
        return None
    evr = [float(v) for v in proj["explained_variance_ratio"]]
    return {"n_components": int(proj["n_components"]), "explained_variance_ratio": evr}


def _detect_signal_type(spectral_cols: list[str], spectra: np.ndarray, warnings: list[str]) -> tuple[str | None, float]:
    """Detect the spectral signal type (absorbance / reflectance / transmittance / …) from the data,
    via nirs4all. The descriptors all carry ``auto`` (undeclared), so this is the only honest source.
    Returns ``(type|None, confidence)``; ``None`` when undeterminable or nirs4all is absent."""
    if spectra.ndim != 2 or spectra.shape[0] < 1 or spectra.shape[1] < 3:
        return None, 0.0
    try:
        from nirs4all.data.detection.detector import detect_signal_type

        st, conf = detect_signal_type(header=[str(c) for c in spectral_cols], data=spectra)
        return (str(st) if st else None), float(conf)
    except Exception as exc:  # noqa: BLE001 - detection is best-effort
        warnings.append(f"signal-type detection failed: {type(exc).__name__}")
        return None, 0.0


def _variable_type(var: Variable) -> bool:
    """Whether a declared variable is treated as numeric (``False`` => categorical dataviz/stats)."""
    return var.type is VarType.NUMERIC


def _variable_section(var: Variable, values: pd.Series, warnings: list[str], *, compute_histogram: bool = False) -> dict[str, Any]:
    """Build one ``variables[]`` card entry. Numeric or categorical stats per the declared type, but a
    variable *declared* numeric whose values do not parse as numbers is profiled as CATEGORICAL instead
    (the card's ``type`` records the effective type) — the descriptor's guess never yields empty stats.

    When ``compute_histogram`` and the effective type is numeric, a ``histogram`` block (``edges``/``counts``)
    is attached for the site's interactive distribution chart (categorical vars use ``stats.top_classes``)."""
    from nirs4all_datasets.qualify import metrics

    variable_metrics = registry.metrics_for("variable")
    effective_type = var.type
    histogram: dict[str, Any] | None = None
    shape: dict[str, Any] | None = None
    balance: dict[str, Any] | None = None
    if var.type is VarType.NUMERIC:
        numeric = pd.to_numeric(values, errors="coerce")
        if values.notna().any() and numeric.notna().sum() == 0:
            effective_type = VarType.CATEGORICAL
            stats = variable_metrics["categorical_stats"](values)
            balance = _class_balance(values)
        else:
            arr = numeric.to_numpy(dtype="float64")
            stats = variable_metrics["numeric_stats"](arr)
            shape = _distribution_shape(arr, stats)
            if compute_histogram:
                histogram = metrics.histogram_bins(arr)
    else:
        stats = variable_metrics["categorical_stats"](values)
        balance = _class_balance(values)
    section: dict[str, Any] = {
        "name": var.name,
        "role": var.role.value,
        "type": effective_type.value,
        "unit": var.unit,
        "stats": stats,
        "assets": [],
    }
    if histogram is not None:
        section["histogram"] = histogram
    if shape is not None:
        section["shape"] = shape
    if balance is not None:
        section["balance"] = balance
    return section


def _distribution_shape(arr: np.ndarray, stats: dict[str, Any]) -> dict[str, Any]:
    """Skewness / kurtosis / normality + coefficient of variation for a numeric variable."""
    from nirs4all_datasets.qualify import metrics

    sh = metrics.distribution_shape(arr)
    mean, std = stats.get("mean"), stats.get("std")
    cv = float(std / abs(mean)) if (isinstance(mean, (int, float)) and isinstance(std, (int, float)) and mean) else None
    return {"skewness": sh.get("skewness"), "kurtosis": sh.get("kurtosis"), "normality_p": sh.get("normality_p"), "is_normal": sh.get("is_normal"), "cv": cv}


def _class_balance(values: pd.Series) -> dict[str, Any] | None:
    """Class-balance metrics (entropy / imbalance / gini) from a categorical column's full counts."""
    from nirs4all_datasets.qualify import metrics

    counts = pd.Series(values).dropna().astype(str).value_counts().to_numpy()
    if counts.size == 0:
        return None
    return metrics.class_balance(counts)


def _splits_sections(config: dict[str, Any], warnings: list[str]) -> list[dict[str, Any]]:
    """Per-split partition counts from each ``splits/<name>.parquet`` (``applied`` is always False)."""
    sections: list[dict[str, Any]] = []
    for split in config.get("splits", []):
        name = split.get("name")
        try:
            df = pd.read_parquet(split["path"])
            counts = df["partition"].astype(str).value_counts()
            partitions = {str(k): int(v) for k, v in counts.items()}
        except Exception as exc:  # noqa: BLE001 - a malformed split must not fail the card
            warnings.append(f"split {name!r}: could not read partitions ({type(exc).__name__})")
            partitions = {}
        sections.append({"name": name, "applied": False, "partitions": partitions})
    return sections


def _content_hash(canonical_hashes: dict[str, str]) -> str:
    """Stable content hash: sha256 over the canonical basename->sha256 map sorted by basename."""
    payload = json.dumps(dict(sorted(canonical_hashes.items())), sort_keys=True, separators=(",", ":"))
    return sha256_bytes(payload.encode("utf-8"))


def _integrity(dataset_dir: Path, descriptor: DatasetDescriptor, warnings: list[str]) -> dict[str, Any]:
    """Integrity block: content hash (from the manifest's canonical hashes) + processing/metadata hashes."""
    manifest_path = dataset_dir / "manifest.json"
    canonical_hashes: dict[str, str] = {}
    if manifest_path.exists():
        try:
            canonical_hashes = dict(read_manifest(manifest_path).canonical_hashes)
        except Exception as exc:  # noqa: BLE001 - unreadable manifest -> content hash unavailable
            warnings.append(f"manifest unreadable; content_hash unavailable ({type(exc).__name__})")
    else:
        warnings.append("manifest.json absent; content_hash unavailable")
    return {
        "content_hash": _content_hash(canonical_hashes) if canonical_hashes else None,
        "processing_hash": processing_hash(descriptor),
        "metadata_hash": metadata_hash(descriptor),
        "manifest": "manifest.json",
    }


# =============================================================================
# Freshness predicate (consumed by catalog/cli) — name + semantics preserved
# =============================================================================
def card_metadata_fresh(card_path_or_dir: str | Path, descriptor: DatasetDescriptor) -> bool:
    """Whether an existing card displays up-to-date metadata for ``descriptor``.

    The card stores ``integrity.metadata_hash``; a metadata-only descriptor edit leaves the canonical
    bytes untouched yet must refresh the card. Accepts either the ``card.json`` path or the dataset
    directory (``<dir>/card.json``). A missing/unreadable card, or one lacking the field, is **not**
    fresh (so it gets rebuilt and picks up the current sections).
    """
    path = Path(card_path_or_dir)
    if path.is_dir():
        path = path / "card.json"
    if not path.exists():
        return False
    try:
        card = json.loads(path.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001 - unreadable card -> rebuild
        return False
    return (card.get("integrity") or {}).get("metadata_hash") == metadata_hash(descriptor)


# =============================================================================
# Card assembly
# =============================================================================
def build_card(dataset_dir: str | Path, descriptor: DatasetDescriptor, *, compute_assets: bool = True, compute_pca: bool = True) -> dict[str, Any]:
    """Build the identity card for a dataset directory from its canonical Parquet.

    Reads ``canonical/dataset.json`` (via :func:`resolve_config`) and each source/variables/splits
    Parquet; computes the alignment, per-source spectral, per-variable, split and integrity sections;
    optionally renders the plot assets (:mod:`plots`). Returns a finite-sanitized dict matching the
    schema-2.0 card contract (it does not write — :func:`write_card` / :func:`qualify` do).

    Args:
        dataset_dir: The dataset directory containing ``canonical/``.
        descriptor: The dataset descriptor (identity, variables, governance, provenance).
        compute_assets: Render the per-source/per-variable PNGs (off => no plot files, no asset paths).
        compute_pca: Compute the per-source PCA explained-variance summary (off => ``pca: null``).
    """
    dataset_dir = Path(dataset_dir)
    config = resolve_config(dataset_dir)
    warnings: list[str] = []

    # --- sources (per spectral block) ---
    source_sections: list[dict[str, Any]] = []
    source_frames: list[pd.DataFrame] = []
    source_profiles: list[dict[str, Any]] = []
    all_sample_ids: set[str] = set()
    reps_counts: list[int] = []
    for entry in config.get("sources", []):
        section, df, src_samples = _source_section(entry, descriptor, warnings, compute_pca=compute_pca, compute_curve=compute_assets)
        source_sections.append(section)
        source_frames.append(df)
        profile = (section.get("spectral") or {}).get("profile")
        if isinstance(profile, dict):
            source_profiles.append(profile)
        all_sample_ids |= src_samples
        if _SAMPLE_KEY in df.columns:
            reps_counts.extend(int(c) for c in df[_SAMPLE_KEY].astype(str).value_counts().to_numpy())

    # --- variables (Y + metadata; only those actually present in the canonical variables.parquet) ---
    variable_sections: list[dict[str, Any]] = []
    variables_block = config.get("variables")
    variables_df: pd.DataFrame | None = None
    if variables_block is not None and variables_block.get("path"):
        variables_df = pd.read_parquet(variables_block["path"])
    present_cols = set(variables_df.columns) if variables_df is not None else set()
    for var in descriptor.variables:
        if var.name not in present_cols:
            warnings.append(f"variable {var.name!r} declared but absent from canonical variables.parquet; skipped")
            continue
        variable_sections.append(_variable_section(var, variables_df[var.name], warnings, compute_histogram=compute_assets))  # type: ignore[index]

    _attach_xy_metrics(source_sections, source_frames, variable_sections, variables_df)

    # Visuals are inline SVG on the site, rendered from the card's own data (per-source spectral
    # quantile curves + per-variable histogram bins) — no matplotlib PNG assets. The ``assets`` block
    # is retained (empty) for schema stability.
    assets: dict[str, Any] = {"sources": {}, "variables": []}

    card: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "protocol_version": registry.PROTOCOL_VERSION,
        "generated_at": datetime.now(UTC).isoformat(),
        "identity": _identity(descriptor),
        "versions": _versions(descriptor),
        "alignment": _alignment(config, all_sample_ids, reps_counts, descriptor, source_profiles),
        "sources": source_sections,
        "variables": variable_sections,
        "splits": _splits_sections(config, warnings),
        "provenance": _provenance(descriptor),
        "integrity": _integrity(dataset_dir, descriptor, warnings),
        "governance": _governance(descriptor),
        "assets": assets,
        "warnings": warnings,
    }
    sanitized: dict[str, Any] = _jsonify(card)
    return sanitized


def write_card(card: dict[str, Any], path: str | Path) -> None:
    """Atomically write a card as pretty, finite JSON (temp file + ``os.replace``; ``allow_nan=False``)."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(card, indent=2, sort_keys=True, allow_nan=False), encoding="utf-8")
    os.replace(tmp, path)


def qualify(dataset_dir: str | Path, descriptor: DatasetDescriptor, *, compute_assets: bool = True, compute_pca: bool = True) -> dict[str, Any]:
    """Build, render assets for, and write ``<dataset_dir>/card.json``; return the card.

    The single qualify-stage entry point: it (re)derives the card from the canonical bytes (so a
    protocol refresh needs no rebuild), renders the per-source/per-variable plot assets into
    ``<dataset_dir>/assets/`` (when ``compute_assets``), and writes the full artifact set —
    ``card.json`` (machine-readable), ``card.md`` (Datasheets-for-Datasets), and ``croissant.json``
    (MLCommons Croissant JSON-LD).

    For the ``anonymized`` tier the written artifacts are the *public-safe* views (masked variable names,
    z-scored stats, no identifying free text): the tracked ``card.json``/``card.md``/``croissant.json`` are
    derived from :func:`anonymize.public_card` + :func:`anonymize.public_descriptor`, so an anonymized
    dataset cannot leak through any tracked or served artifact. Returns the written (public) card.
    """
    dataset_dir = Path(dataset_dir)
    full_card = build_card(dataset_dir, descriptor, compute_assets=compute_assets, compute_pca=compute_pca)
    card = anonymize.public_card(full_card, descriptor.tier)
    pub_descriptor = anonymize.public_descriptor(descriptor)
    write_card(card, dataset_dir / "card.json")

    manifest_path = dataset_dir / "manifest.json"
    hashes = read_manifest(manifest_path).canonical_hashes if manifest_path.exists() else {}
    (dataset_dir / "card.md").write_text(datasheet.render_datasheet(card, pub_descriptor), encoding="utf-8")
    croissant_doc = croissant.render_croissant(card, pub_descriptor, hashes=hashes, file_ids={}, instance=pub_descriptor.dataverse.instance)
    (dataset_dir / "croissant.json").write_text(json.dumps(croissant_doc, indent=2, sort_keys=True), encoding="utf-8")
    return card
