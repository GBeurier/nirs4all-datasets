"""Convert a v2.0 leaf (id-keyed CSVs) into the per-source, sample-identity-joined canonical form.

A v2.0 leaf is a directory of ``;``-delimited CSVs whose first column is ``observation_id``:

* ``X.csv`` / ``X1.csv`` / ``X2.csv`` ... — one per spectral block: ``observation_id`` + numeric
  wavelength columns;
* ``Y.csv`` — ``observation_id`` + target columns (optional);
* ``M.csv`` — ``dataset_id``, ``observation_id``, optionally ``sample_id``, ``split_original``, and
  arbitrary metadata columns (optional).

The canonical form keeps each X block **separate** (one Parquet per source) and links everything by
**sample identity**, never by row position. Sources may carry different numbers of observations
(asymmetric repetitions); they are joined through ``observation_id -> sample_id`` (from ``M.csv`` if it
declares ``sample_id``, else identity). ``variables`` and ``splits`` are keyed per ``sample_id`` (one
row per sample). Parquet is chosen because Dataverse does not auto-ingest it, so the uploaded bytes
stay byte-identical to the local ones (the SHA-256 verification in ``access.py`` depends on that).

On-disk layout under ``<dataset_dir>/canonical/``::

    sources/<source_id>.parquet   observation_id (str), sample_id (str), <spectral cols> (float32)
    variables.parquet             sample_id (str), <all non-spectral Y/M cols> (native dtype)  [optional]
    splits/<name>.parquet         sample_id (str), partition (str) [, fold (int)]               [optional]
    dataset.json                  loadable manifest (see :func:`resolve_config`)

The descriptor passed in carries the id columns (:class:`IdentitySpec`), the alignment level, and the
declared sources; this module uses them but stays robust when the on-disk X-file set differs (it warns
and converts whatever blocks it finds).
"""
from __future__ import annotations

import csv
import json
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from nirs4all_datasets import __version__ as _PKG_VERSION
from nirs4all_datasets.bootstrap import _metadata_aliases, _original_sample_alias
from nirs4all_datasets.curation import is_provenance_column, normalize_variable
from nirs4all_datasets.manifest import sha256_file
from nirs4all_datasets.schema import AlignmentLevel, ConversionStatus, DatasetDescriptor, VarType

CONVERTER_NAME = "nirs4all-datasets-canonical"
CONVERTER_VERSION = (_PKG_VERSION or "2.0") + "+curation.1"
CANONICAL_FORMAT_VERSION = "1.1"
JOIN_KEY = "sample_id"
_OBS_KEY = "observation_id"
_READ_CHUNK = 8192  # X read chunk (rows) for big files (e.g. the 40k-row OSSL)
# Non-spectral M columns that are structural plumbing, never user-facing variables.
_M_STRUCTURAL = frozenset({"dataset_id", "source_sample_index", "split_original", "split_source"})


@dataclass
class CanonicalResult:
    """Outcome of a raw->canonical conversion of one v2.0 leaf."""

    dataset_dir: Path
    canonical_dir: Path
    config: dict[str, Any]
    converter_name: str
    converter_version: str
    status: ConversionStatus
    canonical_hashes: dict[str, str] = field(default_factory=dict)  # canonical basename -> sha256
    row_counts: dict[str, int] = field(default_factory=dict)  # source_id / 'variables' / 'split:<name>' -> rows
    warnings: list[str] = field(default_factory=list)


def _sniff_sep(path: Path) -> str:
    """Sniff the delimiter of a tabular file; default to ``;`` (the v2.0 convention)."""
    with path.open("r", encoding="utf-8", errors="replace", newline="") as fh:
        sample = fh.read(8192)
    if not sample:
        return ";"
    # A one-column v2 header has no delimiter. Commas in its data are values, not evidence that
    # the file is comma-delimited (e.g. chemical names such as 1,3-dimethyl...).
    header = sample.splitlines()[0]
    if not any(delimiter in header for delimiter in ";,\t"):
        return ";"
    try:
        return csv.Sniffer().sniff(header, delimiters=";,\t").delimiter
    except csv.Error:
        return ";"


def _write_table(table: pa.Table, path: Path) -> str:
    """Write an Arrow table to Parquet (zstd) and return its SHA-256."""
    path.parent.mkdir(parents=True, exist_ok=True)
    pq.write_table(table, path, compression="zstd")
    return sha256_file(path)


def _x_files(leaf: Path) -> dict[str, Path]:
    """Map each on-disk spectral block to its source_id (``X`` / ``X1`` / ``X2`` ...).

    A block file is named ``X.csv`` (single source, source_id ``X``) or ``X<n>.csv`` (source_id
    ``X<n>``). Returns ``{source_id: path}`` ordered by source_id.
    """
    blocks: dict[str, Path] = {}
    for path in sorted(leaf.glob("X*.csv")):
        stem = path.stem
        if re.fullmatch(r"X(?:\d+|_[A-Za-z0-9_]+)?", stem):
            blocks[stem] = path
    return blocks


def _read_obs_to_sample(leaf: Path, ids_sample: str, text_cols: set[str], dataset_id: str = "", source_context: dict[str, str] | None = None) -> tuple[pd.DataFrame | None, bool, list[str]]:
    """Read ``M.csv`` and build the ``observation_id -> sample_id`` mapping.

    Returns ``(m_df, has_sample_id, warnings)`` where ``m_df`` is the full metadata table (or ``None``
    when there is no ``M.csv``). When ``M.csv`` lacks the declared ``sample_id`` column, the caller
    derives ``sample_id := observation_id`` (each observation is its own sample group).
    """
    warnings: list[str] = []
    m_path = leaf / "M.csv"
    if not m_path.exists():
        return None, False, warnings
    m = pd.read_csv(m_path, sep=_sniff_sep(m_path), dtype=dict.fromkeys(text_cols | {_OBS_KEY, ids_sample, JOIN_KEY}, str), keep_default_na=False)
    if _OBS_KEY not in m.columns:
        warnings.append(f"M.csv has no {_OBS_KEY!r} column; ignoring metadata and using identity sample_id.")
        return None, False, warnings
    if ids_sample == _OBS_KEY:
        if JOIN_KEY in m.columns:
            m = m.rename(columns={JOIN_KEY: _original_sample_alias(leaf)})
        return m, False, warnings
    has_sample = ids_sample in m.columns
    if has_sample:
        m[ids_sample] = m[ids_sample].astype("string").str.strip().replace("", pd.NA)
        conflicts = m.groupby(_OBS_KEY, dropna=False)[ids_sample].nunique(dropna=True)
        if (conflicts > 1).any():
            raise ValueError("M.csv: observation_id maps to conflicting sample_id values")
    return m, has_sample, warnings


def _sample_for(obs: pd.Series, m: pd.DataFrame | None, has_sample: bool, ids_sample: str) -> tuple[pd.Series, int]:
    """Map an observation_id series to its sample_id (via ``M.csv`` if present, else identity).

    Returns ``(sample_id_series, n_orphans)``. An *orphan* is an observation_id present in the source
    but absent from ``M.csv``'s ``observation_id -> sample_id`` table: it falls back to identity
    (``sample_id := observation_id``) and is counted so the caller can warn. With no sample mapping
    (``m is None`` or no ``sample_id`` column) every row is identity by design and nothing is orphaned.
    """
    obs_str = obs.astype(str)
    if m is None or not has_sample:
        return obs_str, 0
    lookup = m.drop_duplicates(subset=[_OBS_KEY]).set_index(_OBS_KEY)[ids_sample]
    mapped = obs_str.map(lookup)
    n_orphans = int(mapped.isna().sum())
    return mapped.fillna(obs_str).astype(str), n_orphans


def _convert_source(path: Path, source_id: str, m: pd.DataFrame | None, has_sample: bool, ids_sample: str, canonical: Path) -> tuple[dict[str, Any] | None, str | None, int, set[str], list[str]]:
    """Convert one X block to ``canonical/sources/<source_id>.parquet``.

    Reads spectral columns as float32 (chunked for large files), prepends ``observation_id`` (str) and
    the joined ``sample_id`` (str). Returns ``(source_entry, sha256, n_rows, sample_ids, warnings)``;
    ``source_entry`` and ``sha256`` are ``None`` when the block is malformed (first column is not
    ``observation_id``) — the block is then skipped (not written) rather than crashing, so the rest of
    the conversion proceeds. ``sample_ids`` is the set of sample_ids backed by this source's spectra.
    """
    warnings: list[str] = []
    sep = _sniff_sep(path)
    header = pd.read_csv(path, sep=sep, nrows=0)
    cols = list(header.columns)
    if not cols or cols[0] != _OBS_KEY:
        warnings.append(f"{path.name}: first column is {cols[0] if cols else '<none>'!r}, expected {_OBS_KEY!r}; skipping this block.")
        return None, None, 0, set(), warnings
    spectral_cols = list(cols[1:])
    dtypes: dict[str, Any] = {_OBS_KEY: str} | dict.fromkeys(spectral_cols, "float32")

    obs_chunks: list[pd.Series] = []
    spectral_chunks: list[pd.DataFrame] = []
    missing_spectral = {column: ["", "NA", "N/A", "NaN", "nan", "null", "NULL", "<NA>"] for column in spectral_cols}
    for chunk in pd.read_csv(path, sep=sep, dtype=dtypes, chunksize=_READ_CHUNK, keep_default_na=False, na_values=missing_spectral):
        obs_chunks.append(chunk[_OBS_KEY].astype(str))
        spectral_chunks.append(chunk[spectral_cols])
    obs = pd.concat(obs_chunks, ignore_index=True) if obs_chunks else pd.Series([], dtype=str, name=_OBS_KEY)
    spectral = pd.concat(spectral_chunks, ignore_index=True) if spectral_chunks else pd.DataFrame(columns=spectral_cols)
    if obs.str.strip().eq("").any() or not obs.is_unique:
        raise ValueError(f"{path.name}: observation_id must be nonempty and unique within the spectral source")

    if obs.duplicated().any():
        raise ValueError(f"{path.name}: observation_id must be unique within each source")
    sample, n_orphans = _sample_for(obs, m, has_sample, ids_sample)
    if n_orphans:
        warnings.append(f"{path.name}: {n_orphans} observation_id(s) have no row in M.csv; used identity sample_id for them.")
    arrays: dict[str, pa.Array] = {
        _OBS_KEY: pa.array(obs.to_numpy(), type=pa.string()),
        JOIN_KEY: pa.array(sample.to_numpy(), type=pa.string()),
    }
    for col in spectral_cols:
        arrays[col] = pa.array(spectral[col].to_numpy(dtype="float32"), type=pa.float32())
    table = pa.table(arrays)

    out = canonical / "sources" / f"{source_id}.parquet"
    sha = _write_table(table, out)
    axis_vals = [_to_float(c) for c in spectral_cols]
    numeric = [v for v in axis_vals if v is not None]
    entry: dict[str, Any] = {
        "source_id": source_id,
        "path": f"canonical/sources/{source_id}.parquet",
        "n_observations": int(len(obs)),
        "n_variables": len(spectral_cols),
        "duplicate_vectors": {
            "distinct": int(len(spectral) - spectral.duplicated().sum()),
            "additional_copies": int(spectral.duplicated().sum()),
            "semantics": "equal stored spectral values; not proof of technical reacquisition; no rows removed",
        },
        "axis_unit": None,
        "axis_min": min(numeric) if numeric else None,
        "axis_max": max(numeric) if numeric else None,
    }
    return entry, sha, int(len(obs)), set(sample.tolist()), warnings


def _to_float(value: str) -> float | None:
    """Parse a wavelength header to float, or ``None`` if it is not numeric."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _build_variables(leaf: Path, m: pd.DataFrame | None, has_sample: bool, ids_sample: str, spectral_samples: set[str], numeric_cols: set[str], text_cols: set[str], aliases: dict[str, str], column_mapping: dict[str, str] | None = None) -> tuple[pd.DataFrame | None, list[str]]:
    """Build the per-sample variables table (Y columns UNION extra M columns), one row per sample_id.

    Y.csv columns and non-structural M columns are merged on ``observation_id``, then collapsed to one
    row per ``sample_id`` (the first value wins; a divergent value within a sample emits a warning).
    ``spectral_samples`` is the set of sample_ids backed by at least one X source; a variables row whose
    sample_id is *not* in it is a phantom (Y/M without spectra) and is warned about (kept, not dropped).
    Returns ``(variables_df, warnings)`` — ``variables_df`` is ``None`` when there is nothing to write.
    """
    warnings: list[str] = []
    frames: list[pd.DataFrame] = []

    y_path = leaf / "Y.csv"
    if y_path.exists():
        y = pd.read_csv(y_path, sep=_sniff_sep(y_path), dtype=dict.fromkeys(text_cols | {_OBS_KEY}, str), keep_default_na=False, na_values=[""])
        y = y.rename(columns=column_mapping or {})
        if y.columns.duplicated().any():
            raise ValueError("declared variable mapping creates duplicate Y columns")
        if _OBS_KEY not in y.columns:
            # Some upstream packages export X/Y/M as paired rows, without a key in Y. Only attach
            # M's keys when an X block independently confirms its complete observation order.
            paired = False
            if m is not None and len(y) == len(m) and m[_OBS_KEY].notna().all() and m[_OBS_KEY].is_unique:
                for x_path in _x_files(leaf).values():
                    x_ids = pd.read_csv(x_path, sep=_sniff_sep(x_path), usecols=[0], dtype=str).iloc[:, 0]
                    if x_ids.name == _OBS_KEY and x_ids.equals(m[_OBS_KEY]):
                        y.insert(0, _OBS_KEY, m[_OBS_KEY].to_numpy())
                        warnings.append(f"Y.csv has no {_OBS_KEY!r}; assumed Y/M row pairing and attached M.csv IDs. M observation order matches {x_path.name}.")
                        paired = True
                        break
            if not paired:
                warnings.append(f"Y.csv has no {_OBS_KEY!r} and paired row order cannot be verified; skipping targets.")
        if _OBS_KEY in y.columns and y.shape[1] > 1:
            frames.append(y)

    if m is not None:
        # Drop structural plumbing + the standardization script's `source_*` provenance-tracking columns
        # (file paths, repo refs, grouped-export notes): these are bookkeeping, not sample measurements.
        keep = [_OBS_KEY] + [c for c in m.columns if c not in _M_STRUCTURAL and c != _OBS_KEY and c != ids_sample and not (str(c).startswith("source_") and is_provenance_column(str(c)))]
        m_extra = m[keep].rename(columns=aliases | (column_mapping or {}))
        if m_extra.columns.duplicated().any():
            raise ValueError("declared variable mapping creates duplicate metadata columns")
        if m_extra.shape[1] > 1:
            frames.append(m_extra)

    if not frames:
        return None, warnings

    merged = frames[0]
    for extra in frames[1:]:
        overlap = (set(merged.columns) & set(extra.columns)) - {_OBS_KEY}
        extra = extra.drop(columns=list(overlap)) if overlap else extra
        if overlap:
            warnings.append(f"variables: dropped duplicate columns {sorted(overlap)} (kept the first source's values).")
        merged = merged.merge(extra, on=_OBS_KEY, how="outer")

    merged[JOIN_KEY], _ = _sample_for(merged[_OBS_KEY], m, has_sample, ids_sample)
    value_cols = [c for c in merged.columns if c not in (_OBS_KEY, JOIN_KEY)]
    varying = False
    for col in value_cols:
        per_sample_distinct = merged.groupby(JOIN_KEY, dropna=False)[col].nunique(dropna=True)
        if (per_sample_distinct > 1).any():
            varying = True
            warnings.append(f"variables: column {col!r} varies within a sample_id; retained at observation grain.")
    merged.attrs["observation_variables"] = merged.copy()
    grouped = merged[[_OBS_KEY, JOIN_KEY, *value_cols]].copy() if varying else merged.groupby(JOIN_KEY, dropna=False, sort=False)[value_cols].first().reset_index()
    grouped[JOIN_KEY] = grouped[JOIN_KEY].astype(str)
    # Coerce comma-decimal float columns (European locales export "12,5") to real floats -- but ONLY for
    # columns the descriptor declares NUMERIC, so a genuinely numeric target/metadata is not stranded as an
    # unparseable string while a declared-categorical code (e.g. "001") is never silently turned into a float.
    for col in value_cols:
        if col not in numeric_cols or pd.api.types.is_numeric_dtype(grouped[col]):
            continue
        text = grouped[col].astype("string").str.strip()
        nonblank = text[text.notna() & (text != "") & (text.str.lower() != "nan")]
        if nonblank.empty:
            continue
        as_num = pd.to_numeric(nonblank.str.replace(",", ".", regex=False), errors="coerce")
        if as_num.notna().all():
            grouped[col] = pd.to_numeric(text.str.replace(",", ".", regex=False), errors="coerce")
    phantom = sorted(set(grouped[JOIN_KEY]) - spectral_samples)
    if phantom:
        warnings.append(f"variables: {len(phantom)} sample_id(s) have Y/metadata but no spectra in any source (e.g. {phantom[:3]}); kept.")
    result = grouped[([_OBS_KEY] if varying else []) + [JOIN_KEY] + value_cols]
    result.attrs["observation_variables"] = merged.attrs["observation_variables"]
    return result, warnings


def _build_split(m: pd.DataFrame | None, has_sample: bool, ids_sample: str) -> tuple[pd.DataFrame | None, str | None, list[str]]:
    """Build the native split table from ``M.csv`` ``split_original`` (one row per sample_id).

    Returns ``(split_df, name, warnings)`` or ``(None, None, [])`` when there is no native split. The
    name is ``original``; never invents a split. A foldable layout is not present in v2.0 data, so no
    ``fold`` column is emitted. When a sample_id's observations disagree on their partition (only
    possible at SAMPLE alignment with repetitions), the first partition wins and a warning is emitted —
    silently picking one would be a correctness hazard.
    """
    warnings: list[str] = []
    if m is None or "split_original" not in m.columns:
        return None, None, warnings
    raw = m["split_original"].astype("string").str.strip()
    has_value = raw.notna() & (raw != "") & (raw.str.lower() != "nan")
    if not has_value.any():
        return None, None, warnings
    sample, _ = _sample_for(m[_OBS_KEY], m, has_sample, ids_sample)
    split = pd.DataFrame({JOIN_KEY: sample.astype(str), "partition": raw})
    split = split[has_value.to_numpy()].reset_index(drop=True)
    if (split.groupby(JOIN_KEY, dropna=False)["partition"].nunique(dropna=True) > 1).any():
        warnings.append("split 'original': a sample occurs in multiple partitions; retained the observation-level assignments (potential group leakage).")
        split.insert(0, _OBS_KEY, m.loc[has_value, _OBS_KEY].to_numpy())
        return split, "original", warnings
    split = split.drop_duplicates(subset=[JOIN_KEY], keep="first").reset_index(drop=True)
    return split, "original", warnings


def build_canonical(leaf_dir: str | Path, descriptor: DatasetDescriptor, out_dir: str | Path, *, source_context: dict[str, str] | None = None) -> CanonicalResult:
    """Convert a v2.0 leaf into the canonical per-source, sample-identity-joined form.

    Wipes ``<out_dir>/canonical/`` first (no stale artifacts), then writes one Parquet per X block
    (``sources/<source_id>.parquet``), the per-sample ``variables.parquet`` (omitted when there is no
    Y and no extra M column), any native ``splits/<name>.parquet`` (never invented), and the loadable
    ``dataset.json``. Robust to: no Y, multi-block, a missing ``sample_id`` column (identity fallback),
    and large files (spectral columns read as float32 in chunks).

    Args:
        leaf_dir: The v2.0 leaf directory (``X*.csv`` / ``Y.csv`` / ``M.csv``).
        descriptor: The dataset descriptor (carries ``ids``, ``alignment_level``, declared ``sources``).
        out_dir: The dataset directory; the canonical tree is written under ``out_dir/canonical``.

    Returns:
        A :class:`CanonicalResult`. ``status`` is ``OK`` (no warnings), ``PARTIAL`` (warnings), or
        ``FAILED`` (no convertible X block).
    """
    leaf = Path(leaf_dir)
    out = Path(out_dir)
    canonical = out / "canonical"
    if canonical.exists():
        shutil.rmtree(canonical)
    canonical.mkdir(parents=True)

    warnings: list[str] = []
    ids_sample = descriptor.ids.sample_id
    source_identity_rules = {"mendeley_human_arm_muscle_vis_swir_reflectance", "ossl_lucas_visnir_soil_all_y", "ossl_lucas_mir_soil_all_y", "ucph_granules_ambient_moisture_api_nir", "ucph_granules_moisture_controlled_api_nir", "dryad_rice_leaf_reflectance_manual", "flanagan_api_compounds_raman", "drug_compound_flanagan_raman", "drug_common_application_flanagan_raman", "drug_solvent_reagent_flanagan_raman"}
    if descriptor.id in source_identity_rules:
        ids_sample = JOIN_KEY
    aliases = _metadata_aliases(leaf)
    column_mapping = {v.original_name: v.name for v in descriptor.variables if v.original_name and v.original_name != v.name}
    if len(column_mapping) != sum(bool(v.original_name and v.original_name != v.name) for v in descriptor.variables):
        raise ValueError("original variable names must map unambiguously")
    text_cols = {v.name for v in descriptor.variables if v.type is not VarType.NUMERIC}
    text_cols.update(v.original_name for v in descriptor.variables if v.original_name and v.type is not VarType.NUMERIC)
    text_cols.update(name for name, alias in aliases.items() if alias in text_cols)
    m, has_sample, m_warnings = _read_obs_to_sample(leaf, ids_sample, text_cols, descriptor.id, source_context)
    warnings.extend(m_warnings)
    from nirs4all_datasets.curation import curate_bundle, write_curated

    # The raw, unified variables remain available; curated M/Y/structure/passport
    # are separate observation-level views with an exhaustive source mapping.
    curated = curate_bundle(leaf, descriptor.id, soilsite=Path(source_context["soilsite"]) if source_context and source_context.get("soilsite") else None, assume_paired_y=True, numeric_names={v.name for v in descriptor.variables if v.type is VarType.NUMERIC}, categorical_names={v.name for v in descriptor.variables if v.type is VarType.CATEGORICAL}, allow_unaligned_y=True, verify_spectral_order=True, variable_specs=descriptor.variables)
    warnings.extend(curated.warnings)
    if m is not None:
        enriched = curated.enriched_metadata
        for column in enriched:
            if column not in m:
                m[column] = enriched[column].to_numpy()
        if ids_sample != _OBS_KEY:
            m[ids_sample] = curated.structure.set_index(_OBS_KEY)[JOIN_KEY].reindex(m[_OBS_KEY]).to_numpy()
            has_sample = bool(curated.structure[JOIN_KEY].notna().any())
    identity = curated.report["identity"]
    (canonical / "identity.json").write_text(json.dumps(identity, indent=2), encoding="utf-8")
    if descriptor.ids.sample_id_available and not has_sample:
        warnings.append(f"descriptor declares sample_id available but {ids_sample!r} is absent from M.csv; using identity sample_id.")

    x_files = _x_files(leaf)
    declared = {s.source_id for s in descriptor.sources}
    found = set(x_files)
    if declared != found:
        warnings.append(f"declared sources {sorted(declared)} != on-disk X blocks {sorted(found)}; converting the on-disk blocks.")

    hashes: dict[str, str] = {}
    if m is not None:
        original_metadata = curated.original_metadata.copy()
        original_metadata.attrs.clear()
        hashes["provenance.parquet"] = _write_table(pa.Table.from_pandas(original_metadata, preserve_index=False), canonical / "provenance.parquet")
    row_counts: dict[str, int] = {}
    source_entries: list[dict[str, Any]] = []
    spectral_samples: set[str] = set()
    unit_by_id = {s.source_id: s.axis_unit.value for s in descriptor.sources}
    for source_id, path in x_files.items():
        entry, sha, n_rows, src_samples, src_warnings = _convert_source(path, source_id, m, has_sample, ids_sample, canonical)
        warnings.extend(src_warnings)
        if entry is None or sha is None:
            continue
        entry["axis_unit"] = unit_by_id.get(source_id)
        source_entries.append(entry)
        hashes[f"sources/{source_id}.parquet"] = sha
        row_counts[source_id] = n_rows
        spectral_samples |= src_samples

    if not source_entries:
        warnings.append("no X block found (expected X.csv or X<n>.csv); nothing converted.")
        config = _dataset_json(descriptor, source_entries, variables_path=None, split_refs=[])
        (canonical / "dataset.json").write_text(json.dumps(config, indent=2, sort_keys=True), encoding="utf-8")
        return CanonicalResult(out, canonical, config, CONVERTER_NAME, CONVERTER_VERSION, ConversionStatus.FAILED, hashes, row_counts, warnings)

    numeric_cols = {v.name for v in descriptor.variables if v.type is VarType.NUMERIC}
    numeric_cols.update(item["canonical_name"] for item in curated.report["enrichments"] if item["canonical_name"] in {"longitude", "latitude", "location_error_m"})
    variables, var_warnings = _build_variables(leaf, m, has_sample, ids_sample, spectral_samples, numeric_cols, text_cols, aliases, column_mapping)
    warnings.extend(var_warnings)
    variables_path: str | None = None
    if variables is not None:
        observation_variables = variables.attrs.pop("observation_variables", None)
        variables.attrs.clear()
        if observation_variables is not None:
            observation_variables.attrs.clear()
        normalization = []
        for variable in descriptor.variables:
            if variable.name in variables:
                variables[variable.name], record = normalize_variable(variables[variable.name], variable)
                normalization.append(record)
            if observation_variables is not None and variable.name in observation_variables:
                observation_variables[variable.name], _ = normalize_variable(observation_variables[variable.name], variable)
        if observation_variables is not None:
            hashes["observations.parquet"] = _write_table(pa.Table.from_pandas(observation_variables, preserve_index=False), canonical / "observations.parquet")
            row_counts["observation_variables"] = len(observation_variables)
        (canonical / "curation.json").write_text(json.dumps({"protocol_version": "1", "variables": normalization}, indent=2, allow_nan=False), encoding="utf-8")
        out_var = canonical / "variables.parquet"
        hashes["variables.parquet"] = _write_table(pa.Table.from_pandas(variables, preserve_index=False), out_var)
        row_counts["variables"] = int(len(variables))
        variables_path = "canonical/variables.parquet"

    split_refs: list[dict[str, str]] = []
    split_df, split_name, split_warnings = _build_split(m, has_sample, ids_sample)
    warnings.extend(split_warnings)
    if split_df is not None and split_name is not None:
        out_split = canonical / "splits" / f"{split_name}.parquet"
        hashes[f"splits/{split_name}.parquet"] = _write_table(pa.Table.from_pandas(split_df, preserve_index=False), out_split)
        row_counts[f"split:{split_name}"] = int(len(split_df))
        split_refs.append({"name": split_name, "path": f"canonical/splits/{split_name}.parquet"})

    config = _dataset_json(descriptor, source_entries, variables_path=variables_path, split_refs=split_refs)
    if variables is not None:
        config["variables"]["join_key"] = _OBS_KEY if _OBS_KEY in variables else JOIN_KEY
    for entry in config["splits"]:
        if split_df is not None:
            entry["join_key"] = _OBS_KEY if _OBS_KEY in split_df else JOIN_KEY
    curation_config = write_curated(curated, canonical / "curation")
    curation_config["tables"] = {name: Path(path).relative_to(out).as_posix() for name, path in curation_config["tables"].items()}
    curation_config["mapping"] = Path(curation_config["mapping"]).relative_to(out).as_posix()
    curation_config["identity"] = curated.report["identity"]
    config["curation"] = curation_config
    config["identity"] = identity
    for path in sorted((canonical / "curation").iterdir()):
        hashes[path.relative_to(canonical).as_posix()] = sha256_file(path)
    (canonical / "dataset.json").write_text(json.dumps(config, indent=2, sort_keys=True), encoding="utf-8")

    status = ConversionStatus.PARTIAL if warnings else ConversionStatus.OK
    return CanonicalResult(out, canonical, config, CONVERTER_NAME, CONVERTER_VERSION, status, hashes, row_counts, warnings)


def _dataset_json(descriptor: DatasetDescriptor, sources: list[dict[str, Any]], *, variables_path: str | None, split_refs: list[dict[str, str]]) -> dict[str, Any]:
    """Assemble the loadable ``dataset.json`` manifest from the converted artifacts."""
    return {
        "format_version": CANONICAL_FORMAT_VERSION,
        "id": descriptor.id,
        "join_key": JOIN_KEY,
        "alignment_level": descriptor.alignment_level.value,
        "sources": sources,
        "variables": {"path": variables_path} if variables_path is not None else None,
        "splits": split_refs,
    }


def resolve_config(dataset_dir: str | Path) -> dict[str, Any]:
    """Read ``<dataset_dir>/canonical/dataset.json`` and absolutize every Parquet path.

    The on-disk manifest stores portable relative paths (``canonical/...``); this returns a dict whose
    ``sources[].path``, ``variables.path``, and ``splits[].path`` are absolute, ready to load.
    """
    root = Path(dataset_dir)
    config: dict[str, Any] = json.loads((root / "canonical" / "dataset.json").read_text(encoding="utf-8"))
    for entry in config.get("sources", []):
        entry["path"] = (root / entry["path"]).resolve().as_posix()
    variables = config.get("variables")
    if variables is not None and variables.get("path") is not None:
        variables["path"] = (root / variables["path"]).resolve().as_posix()
    for split in config.get("splits", []):
        split["path"] = (root / split["path"]).resolve().as_posix()
    curation = config.get("curation")
    if curation:
        curation["mapping"] = str((root / curation["mapping"]).resolve())
        curation["tables"] = {name: str((root / path).resolve()) for name, path in curation["tables"].items()}
    return config
