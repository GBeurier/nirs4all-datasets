"""Versioned, observation-preserving scientific views over immutable source variables.

M/Y are consumer views, not a destructive rewrite of the source. Every input column
has a mapping and a decision; identifiers, passport and other measurements remain
available separately. Dataset-specific identity contracts never become global
suffix-stripping or grouping heuristics.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
import unicodedata
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any, cast

import numpy as np
import pandas as pd

from nirs4all_datasets.schema import DatasetDescriptor, Variable, VarType

CURATION_VERSION = "1.1"
_OBS = "observation_id"
_SAMPLE = "sample_id"
_IDS = {"sample_id", "id_sample", "sampleid", "observation_id", "dataset_id"}
_PASSPORT = {
    "dataset", "dataset_title", "dataset_owner", "dataset_slug", "dataset_code", "collection_name",
    "notes", "license", "license_url", "rights_status", "usage_scope", "public_release_allowed",
    "source_file", "source_url", "source_root", "source_relative_dir", "source_resource", "source_script_reference",
    "source_package_url", "source_dataset_url", "source_dataset_doi", "official_source_url",
    "n_points_original", "axis_unit", "axis_min", "axis_max", "feature_count_per_dimension", "dimensions",
    "wavelength_note", "manual_download", "manual_download_file", "manual_download_source_dir",
    "standardization_batch", "ecosis_resource_id", "target_file", "trait_header", "trait_header_original",
    "task_type", "active_status", "replaces_dataset_id", "source_grouped_y_exports",
}
_GROUPING = {"subject_id", "source_sample_id", "source_label", "batch_number", "plot_id", "site_id", "leaf_id", "original_sample_id"}
_ACQUISITION = {"spectral_rep", "spectralrep", "replicate_index_within_subject_aspect", "replicate_index", "scan_index"}
_MISSING = {"", "nan", "null", "<na>", "nat", "n/a", "nodata", "no data", "missing", "unknown", "not measured", "not provided", "not available", "-", "--"}
_CENSORED = re.compile(r"^\s*(<=|>=|<|>|≤|≥)\s*([+-]?(?:\d+(?:[.,]\d*)?|[.,]\d+)(?:e[+-]?\d+)?)\s*$", re.I)
_API_DATASETS = {"ucph_granules_ambient_moisture_api_nir", "ucph_granules_moisture_controlled_api_nir"}


def canonical_name(name: str) -> str:
    text = unicodedata.normalize("NFKC", str(name)).strip()
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", text)
    return re.sub(r"[^\w]+", "_", text.casefold(), flags=re.UNICODE).strip("_") or "unnamed"


@lru_cache(maxsize=1)
def _contracts() -> dict[str, Any]:
    return cast(dict[str, Any], json.loads(Path(__file__).with_name("curation_contracts.json").read_text(encoding="utf-8"))["datasets"])


def contract_for(dataset_id: str) -> dict[str, Any]:
    return cast(dict[str, Any], _contracts().get(dataset_id, {}))


def contract_hash(dataset_id: str) -> str:
    payload = {"version": CURATION_VERSION, "contract": contract_for(dataset_id)}
    return hashlib.sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def _strings(values: pd.Series) -> pd.Series:
    return values.astype("string").str.normalize("NFKC").str.strip()


def normalize_missing(values: pd.Series, *, tokens: list[str] | None = None, sentinels: list[str] | None = None, identifier: bool = False) -> pd.Series:
    """Whole-token rules only. Ambiguous NA/ND/none and numeric sentinels need explicit rules.

    In particular ``none`` may be a control, ``NA`` a country/category, ``ND``
    a censored result, and a negative number a real measurement. Identifiers
    retain all nonempty spellings and leading zeros.
    """
    text = _strings(values)
    vocabulary = {""} if identifier else _MISSING
    vocabulary = vocabulary | {str(token).casefold().strip() for token in (tokens or [])}
    mask = text.str.casefold().isin(vocabulary)
    if not identifier:
        mask |= text.str.casefold().str.fullmatch(r"not[ _](?:available|provided)(?:[ _].*)?", na=False)
    if sentinels:
        mask |= text.isin(sentinels)
        numeric_sentinels = [number for value in sentinels if (number := _finite_float(value)) is not None]
        if numeric_sentinels:
            mask |= pd.to_numeric(text.str.replace(",", ".", regex=False), errors="coerce").isin(numeric_sentinels)
    return text.mask(mask)


def _finite_float(value: Any) -> float | None:
    # Python accepts digit separators in float("20_11"); CSV numeric parsing does
    # not, and these spellings can be source identifiers rather than quantities.
    if "_" in str(value):
        return None
    try:
        number = float(str(value).replace(",", "."))
        return number if math.isfinite(number) else None
    except (ValueError, TypeError):
        return None


def variable_stats(values: pd.Series, *, numeric: bool) -> dict[str, Any]:
    present = values.dropna()
    distinct = int(present.nunique())
    result: dict[str, Any] = {"n_rows": len(values), "n_present": len(present), "n_missing": int(values.isna().sum()), "completeness_pct": 100 * len(present) / len(values) if len(values) else 0.0, "n_unique": distinct, "type": "numeric" if numeric else "categorical"}
    if numeric:
        censored = present.astype(str).str.match(_CENSORED)
        parsed = [_finite_float(value) for value in present[~censored]]
        numbers = [value for value in parsed if value is not None]
        bounds = set()
        for value in present[censored].astype(str):
            match = _CENSORED.fullmatch(value)
            if match:
                bounds.add((match.group(1), _finite_float(match.group(2))))
        # Lexical spellings 1 / 1.0 / 1,0 are one quantitative value.
        result["n_unique"] = len(set(numbers)) + len(bounds)
        result.update({"min": min(numbers) if numbers else None, "max": max(numbers) if numbers else None, "n_censored": int(censored.sum()), "n_invalid": sum(value is None for value in parsed)})
    else:
        counts = present.value_counts()
        result["imbalance_ratio"] = float(counts.max() / counts.min()) if len(counts) else None
    return result


def _semantic_role(name: str, source_role: str, declared: dict[str, Any]) -> str:
    normalized = canonical_name(name)
    if normalized in _IDS or normalized in _GROUPING:
        return "identifier"
    if normalized in _ACQUISITION or normalized in {"split_original", "split_source", "original_split", "source_sample_index"}:
        return "acquisition_index"
    if normalized in _PASSPORT or normalized.startswith("manual_download_"):
        return "provenance"
    return str(declared.get("semantic_role") or ("measured_trait" if source_role == "Y" else "experimental_context"))


def identity_view(dataset_id: str, metadata: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    """Return observation -> source unit, with unavailable/partial identity explicit."""
    contract = contract_for(dataset_id).get("identity", {})
    columns = list(contract.get("columns", []))
    method = contract.get("method")
    if not method:
        aliases = [c for c in metadata if canonical_name(c) in {"sample_id", "id_sample", "sampleid"}]
        if len(aliases) > 1:
            first = normalize_missing(metadata[aliases[0]], identifier=True)
            for alias in aliases[1:]:
                other = normalize_missing(metadata[alias], identifier=True)
                if not (first.eq(other) | (first.isna() & other.isna())).fillna(False).all():
                    raise ValueError("ambiguous sample identity aliases; provide an explicit source mapping")
        columns = aliases[:1]
        method = "column" if columns else "unavailable"
    result = metadata[[_OBS]].copy()
    sample = pd.Series(pd.NA, index=metadata.index, dtype="string")
    missing_columns = [column for column in columns if column not in metadata]
    if method != "unavailable" and not missing_columns:
        pieces = [normalize_missing(metadata[column], identifier=True) for column in columns]
        if method == "column":
            sample = pieces[0]
        elif method == "composite":
            complete = pd.concat(pieces, axis=1).notna().all(axis=1)
            sample.loc[complete] = pd.concat(pieces, axis=1).loc[complete].apply(lambda row: json.dumps(row.tolist(), ensure_ascii=False, separators=(",", ":")), axis=1)
        elif method == "granule_vial":
            # This suffix rule belongs ONLY to the two protocol-audited UCPH imports.
            if dataset_id not in _API_DATASETS:
                raise ValueError("granule_vial identity is restricted to the audited UCPH datasets")
            parsed = pieces[0].str.extract(r"^(?P<vial>.+_v\d+)\.(?P<scan>[012])$")
            if parsed.isna().any().any():
                raise ValueError(f"{dataset_id}: labels do not satisfy the documented vial.scan contract")
            if parsed.duplicated().any():
                raise ValueError(f"{dataset_id}: duplicate vial/scan keys")
            if parsed.groupby("vial")["scan"].agg(lambda values: set(values) != {"0", "1", "2"} or len(values) != 3).any():
                raise ValueError(f"{dataset_id}: incomplete documented vial.scan triplicates")
            sample = parsed["vial"].astype("string")
            result["acquisition_index"] = parsed["scan"].astype("string")
        else:
            raise ValueError(f"unknown identity method {method!r}")
    result[_SAMPLE] = sample
    for name in metadata:
        normalized = canonical_name(name)
        if name != _OBS and (normalized in _GROUPING or normalized in _ACQUISITION or name in columns):
            if normalized == _SAMPLE:
                normalized = "original_sample_id" if "source_sample_id" in metadata else "source_sample_id"
            if normalized not in result:
                result[normalized] = metadata[name].astype("string")
    counts = sample.dropna().value_counts()
    report = {"method": method, "source_columns": columns, "sample_id_available": bool(len(sample) and sample.notna().all()), "status": "unavailable" if sample.isna().all() else ("partial" if sample.isna().any() else "available"), "n_samples": int(len(counts)) if len(counts) else None, "n_observations_with_identity": int(sample.notna().sum()), "n_missing_identity": int(sample.isna().sum()), "observations_per_unit": {str(k): int(v) for k, v in counts.value_counts().sort_index().items()}, "technical_repetitions": contract.get("technical_repetitions"), "unit": contract.get("unit", "Source-declared unit; biological independence not established"), "conclusion": contract.get("conclusion"), "missing_source_columns": missing_columns, "evidence": contract.get("evidence", [])}
    return result, report


_SOILSITE_MAPPING = {
    "id.dataset.site_ascii_txt": "site_id",
    "longitude.point_wgs84_dd": "longitude",
    "latitude.point_wgs84_dd": "latitude",
    "observation.date.begin_iso.8601_yyyy.mm.dd": "campaign_date_begin",
    "observation.date.end_iso.8601_yyyy.mm.dd": "campaign_date_end",
    "location.point.error_any_m": "location_error_m",
}


def find_soilsite(leaf: Path) -> Path | None:
    """Resolve a local cache only: no network, mutation, or source script execution."""
    import os

    configured = os.environ.get("NIRS4ALL_OSSL_SOILSITE")
    if configured:
        path = Path(configured)
        if not path.is_file():
            raise FileNotFoundError(f"NIRS4ALL_OSSL_SOILSITE does not name a file: {path}")
        return path
    candidates = [leaf / "ossl_soilsite_L0_v1.2.csv.gz", leaf / "raw" / "ossl_soilsite_L0_v1.2.csv.gz"]
    if len(leaf.parents) >= 2:
        candidates.append(leaf.parents[1] / "nirs_datasets_ready" / "ossl_nirs_database" / "input_data" / "raw" / "ossl_soilsite_L0_v1.2.csv.gz")
    return next((path for path in candidates if path.is_file()), None)


def enrich_ossl(dataset_id: str, metadata: pd.DataFrame, soilsite: Path | None) -> tuple[pd.DataFrame, list[dict[str, Any]], list[str]]:
    """Join OSSL design fields by dataset code + layer UUID, preserving source grain."""
    if not dataset_id.startswith("ossl_"):
        return metadata, [], []
    if soilsite is None:
        return metadata, [], ["OSSL design enrichment pending: supply the original soilsite file (NIRS4ALL_OSSL_SOILSITE or --soilsite)."]
    if "dataset_code" not in metadata or "ID_sample" not in metadata:
        return metadata, [], ["OSSL design enrichment pending: dataset_code and ID_sample source keys are required."]
    headers = pd.read_csv(soilsite, compression="infer", nrows=0).columns
    required = ["dataset.code_ascii_txt", "id.layer_uuid_txt"]
    if any(column not in headers for column in required):
        raise ValueError("OSSL soilsite lacks its documented dataset/layer join keys")
    selected = [*required, *[column for column in _SOILSITE_MAPPING if column in headers]]
    site = pd.read_csv(soilsite, compression="infer", usecols=selected, dtype=str, keep_default_na=False)
    site = site[site[required[0]].isin(metadata["dataset_code"].unique())]
    if site.duplicated(required).any():
        raise ValueError("OSSL soilsite dataset/layer keys are not unique")
    if site[required].apply(lambda values: values.str.strip().eq("")).any().any():
        raise ValueError("OSSL soilsite contains empty join keys")
    enriched = metadata.merge(site, left_on=["dataset_code", "ID_sample"], right_on=required, how="left", validate="many_to_one", indicator="_soilsite_join", sort=False)
    if len(enriched) != len(metadata) or not enriched[_OBS].equals(metadata[_OBS].reset_index(drop=True)):
        raise ValueError("OSSL enrichment changed observation identity/order")
    missing = int((enriched["_soilsite_join"] != "both").sum())
    evidence = []
    from nirs4all_datasets.manifest import sha256_file

    digest = sha256_file(soilsite)
    for original, canonical in _SOILSITE_MAPPING.items():
        if original not in enriched:
            continue
        values = enriched[original]
        if canonical in metadata:
            conflict = metadata[canonical].astype("string").fillna("").ne("") & values.astype("string").fillna("").ne("") & metadata[canonical].astype("string").ne(values.astype("string"))
            if conflict.any():
                raise ValueError(f"OSSL enrichment conflicts with existing {canonical}")
            values = metadata[canonical].replace("", pd.NA).combine_first(values)
        enriched[canonical] = values
        evidence.append({"resource": soilsite.name, "sha256": digest, "original_name": original, "canonical_name": canonical, "operation": "join_dataset_layer", "join_keys": required})
    # Only LUCAS has a verified correspondence between the source period and campaign label.
    if dataset_id.startswith("ossl_lucas_") and "campaign_date_begin" in enriched:
        enriched["campaign_year"] = enriched["campaign_date_begin"].astype("string").str.extract(r"^(\d{4})-", expand=False)
        evidence.append({"resource": soilsite.name, "sha256": digest, "original_name": "observation.date.begin_iso.8601_yyyy.mm.dd", "canonical_name": "campaign_year", "operation": "LUCAS campaign label = year of source period start; not individual sampling year"})
    enriched = enriched.drop(columns=[*required, *[c for c in _SOILSITE_MAPPING if c in enriched], "_soilsite_join"])
    warnings = [f"OSSL soilsite join: {missing} observations lack a matched source layer"] if missing else []
    return enriched, evidence, warnings


@dataclass
class CuratedTables:
    metadata: pd.DataFrame
    targets: pd.DataFrame
    structure: pd.DataFrame
    passport: pd.DataFrame
    measurements: pd.DataFrame
    report: dict[str, Any]
    enriched_metadata: pd.DataFrame
    original_metadata: pd.DataFrame
    original_targets: pd.DataFrame
    warnings: list[str] = field(default_factory=list)


def curate_tables(dataset_id: str, metadata: pd.DataFrame, targets: pd.DataFrame | None = None, *, soilsite: Path | None = None, numeric_names: set[str] | None = None, categorical_names: set[str] | None = None, missing_rules: dict[str, dict[str, Any]] | None = None, source_fields: dict[str, dict[str, Any]] | None = None) -> CuratedTables:
    """Build curated M/Y at observation grain; raw inputs are never edited or aggregated.

    ``missing_rules`` is keyed by ``M:<original_name>`` / ``Y:<original_name>``.
    Numeric sentinel rules must explicitly carry ``confirmed=True``. All rules,
    aliases, conflicts and exclusions are written into the mapping report.
    """
    metadata = metadata.copy().reset_index(drop=True)
    targets = targets.copy().reset_index(drop=True) if targets is not None else pd.DataFrame(columns=[_OBS])
    originals = (metadata.copy(), targets.copy())
    for role, frame in [("M", metadata), ("Y", targets)]:
        if _OBS not in frame:
            raise ValueError(f"{role} must be explicitly keyed by observation_id")
        # Acquisition keys are opaque: trimming them in only one table breaks
        # otherwise valid source joins (the Drosophila corpus has a padded ID).
        ids = frame[_OBS].astype("string")
        if ids.isna().any() or ids.str.strip().eq("").any() or ids.duplicated().any():
            raise ValueError(f"{role}: observation_id must be nonempty and unique")
        frame[_OBS] = ids
    metadata, enrichments, warnings = enrich_ossl(dataset_id, metadata, soilsite)
    structure, identity = identity_view(dataset_id, metadata)
    universe = pd.Index(list(dict.fromkeys([*metadata[_OBS].tolist(), *targets[_OBS].tolist()])), name=_OBS)
    bases = pd.DataFrame(index=universe)
    outputs = {name: bases.copy() for name in ["M", "Y", "passport", "measurements"]}
    entries: list[dict[str, Any]] = []
    policy = contract_for(dataset_id)
    numeric_names = numeric_names or set()
    categorical_names = categorical_names or set()
    missing_rules = missing_rules or {}
    source_fields = source_fields or {}
    target_identities = {canonical_name(name) for name in targets.columns if name != _OBS}
    for original in targets.columns:
        declared = {**policy.get("fields", {}).get("Y", {}).get(original, {}), **source_fields.get(f"Y:{original}", {})}
        target_identities.add(canonical_name(declared.get("name") or original))
    # Y first ensures M copies/aliases cannot shadow the selected response.
    for role, source in [("Y", targets), ("M", metadata)]:
        frame = source.set_index(_OBS).reindex(universe)
        for original in frame:
            rule = {**policy.get("fields", {}).get(role, {}).get(original, {}), **source_fields.get(f"{role}:{original}", {})}
            name = str(rule.get("name") or canonical_name(original))
            # Harmonize identifiers/case even when a historical mapping used a source spelling.
            name = canonical_name(name)
            semantic = _semantic_role(original, role, rule)
            if dataset_id in _API_DATASETS and original == "api_reference_percent_w_w":
                semantic, name = "measured_trait", original
            if dataset_id in _API_DATASETS and original == "api_concentration_design_percent":
                semantic = "target_copy"
            declared_responses = [*rule.get("derived_from", []), *([rule["equivalent_to"]] if rule.get("equivalent_to") else [])]
            if role == "M" and any(canonical_name(reference) in target_identities for reference in declared_responses):
                semantic = "target_copy"
            missing = dict(rule.get("missing_rule") or {})
            missing.update(missing_rules.get(f"{role}:{original}", {}))
            if missing.get("sentinels") and not missing.get("confirmed"):
                raise ValueError(f"{role}:{original}: numeric sentinel rules require explicit source confirmation")
            values = normalize_missing(frame[original], tokens=missing.get("tokens"), sentinels=missing.get("sentinels"), identifier=semantic == "identifier")
            numeric = original in numeric_names or name in numeric_names
            categorical = semantic in {"identifier", "acquisition_index"} or original in categorical_names or name in categorical_names or rule.get("statistical_type") == "categorical"
            if categorical:
                numeric = False
            elif rule.get("statistical_type") == "numeric":
                numeric = True
            elif not numeric and semantic not in {"identifier", "acquisition_index", "provenance"}:
                nonempty = values.dropna()
                numeric = bool(len(nonempty)) and all(_finite_float(value) is not None or _CENSORED.fullmatch(str(value)) for value in nonempty)
            dialect_audit: dict[str, Any] | None = None
            if numeric and ("decimal_separator" in rule or "thousands_separator" in rule):
                # Reuse the canonical normalizer. Preserve textual censored/invalid
                # forms in these source views; typed model values live in variables.parquet.
                specification = Variable(name=name, unit=rule.get("unit"), decimal_separator=rule.get("decimal_separator", ","), thousands_separator=rule.get("thousands_separator"))
                normalized, dialect_audit = normalize_variable(values, specification)
                values = pd.Series([
                    original_value if record["status"] in {"invalid", "censored"} else None if pd.isna(value) else str(value)
                    for original_value, value, record in zip(values, normalized, dialect_audit["rows"], strict=True)
                ], index=values.index, dtype="string")
            stats = variable_stats(values, numeric=numeric)
            if numeric and not stats.get("n_invalid") and not stats.get("n_censored"):
                values = pd.to_numeric(values.astype("string").str.replace(",", ".", regex=False), errors="raise").astype("Float64")
            destination = "Y" if role == "Y" and semantic == "measured_trait" else "M"
            if semantic == "measured_trait" and role == "M":
                destination = "measurements"
            if semantic in {"identifier", "acquisition_index", "provenance", "derived_auxiliary", "target_copy"}:
                destination = "passport"
            reasons: list[str] = []
            if destination == "M" and (name in outputs['Y'] or semantic == "target_copy"):
                destination = "passport"
                reasons.append("target excluded from predictive metadata")
            operation = "rename" if name != original else "identity"
            output_name = "source_sample_id" if name == _SAMPLE else name
            output = outputs[destination]
            if output_name in output:
                present = values.notna() & output[output_name].notna()
                existing_units = {entry.get("unit") for entry in entries if entry.get("view") == destination and entry.get("canonical_name") == output_name and entry.get("unit")}
                unit_conflict = bool(existing_units and rule.get("unit") and rule["unit"] not in existing_units)
                if values[present].equals(output.loc[present, output_name]) and not unit_conflict:
                    output[output_name] = output[output_name].combine_first(values)
                    operation = "coalesce_compatible_aliases"
                else:
                    suffix = 2
                    while f"{name}_{suffix}" in output:
                        suffix += 1
                    output_name = f"{name}_{suffix}"
                    output[output_name] = values
                    operation = "keep_conflicting_homonyms_separate"
                    reasons.append("conflicting aliases; no overwrite")
                    if unit_conflict:
                        reasons.append("different source units; no implicit conversion")
            else:
                output[output_name] = values
            entries.append({"source_resource": f"{role}.csv", "original_name": original, "canonical_name": output_name, "original_role": role, "semantic_role": semantic, "view": destination, "operation": operation, "value_normalization": "NFKC and outer-whitespace trim; numeric parsing when declared; original values retained", "grain": "observation", "unit": rule.get("unit"), "missing_rule": {"rule_version": CURATION_VERSION, "tokens": sorted(_MISSING) if semantic != "identifier" else [""], **missing}, "stats": stats, "reasons": reasons})
            if dialect_audit is not None:
                entries[-1]["numeric_dialect"] = {key: dialect_audit[key] for key in ("decimal_separator", "thousands_separator")}
                entries[-1]["value_issues"] = [{"observation_id": observation, **record} for observation, record in zip(values.index, dialect_audit["rows"], strict=True) if record["status"] in {"invalid", "censored"}]
        entries.append({"source_resource": f"{role}.csv", "original_name": _OBS, "canonical_name": _OBS, "original_role": role, "semantic_role": "identifier", "view": "structure", "operation": "identity", "grain": "observation"})
    variable_sections = []
    for view in ["M", "Y"]:
        for name in outputs[view].columns.tolist():
            origins = [entry for entry in entries if entry.get("view") == view and entry.get("canonical_name") == name]
            numeric = any(entry.get("stats", {}).get("type") == "numeric" for entry in origins)
            stats = variable_stats(outputs[view][name], numeric=numeric)
            if stats["n_unique"] < 2:
                alias = f"{view.casefold()}_{name}"
                outputs["passport"][alias] = outputs[view].pop(name)
                for entry in origins:
                    entry["view"] = "passport"
                    entry["canonical_name"] = alias
                    entry["reasons"].append("empty" if stats["n_unique"] == 0 else "constant")
            else:
                units = {entry["unit"] for entry in origins if entry.get("unit")}
                if numeric and not stats.get("n_invalid") and not stats.get("n_censored"):
                    outputs[view][name] = pd.to_numeric(outputs[view][name].astype("string").str.replace(",", ".", regex=False), errors="raise").astype("Float64")
                unit = "% w/w" if dataset_id in _API_DATASETS and name == "api_reference_percent_w_w" else (next(iter(units)) if len(units) == 1 else None)
                variable_sections.append({"name": name, "view": view, "grain": "observation", "unit": unit, "stats": stats, "source_columns": [{"resource": entry["source_resource"], "name": entry["original_name"]} for entry in origins]})
    # Categorical encodings/aliases of a response are unsafe predictive covariates.
    # Check functional dependence only for fields already identified by contract;
    # equality of two unrelated scientific traits alone never merges them.
    for name in outputs["M"].columns.tolist():
        matching_targets = [target for target in outputs["Y"] if name == target]
        if matching_targets:
            outputs["passport"][f"metadata_{name}"] = outputs["M"].pop(name)
    for view, output in outputs.items():
        output.insert(0, _SAMPLE, structure.set_index(_OBS)[_SAMPLE].reindex(universe))
        outputs[view] = output.reset_index()
    for entry in entries:
        entry["variable_id"] = f"{dataset_id}:{entry['canonical_name']}"
        entry["mapping_version"] = CURATION_VERSION
    report = {"schema_version": CURATION_VERSION, "dataset_id": dataset_id, "contract_sha256": contract_hash(dataset_id), "grain": "observation", "identity": identity, "views": {name: [column for column in output if column not in {_OBS, _SAMPLE}] for name, output in outputs.items()}, "mapping": entries, "variables": variable_sections, "enrichments": enrichments, "warnings": warnings, "missing_policy": "Whole-token text rules; NA/ND/none preserved unless a column rule says otherwise; no unconfirmed numeric sentinels or implicit imputation.", "source_values": "Immutable original M/Y tables retained separately; mappings do not make many-to-one NA normalization reversible."}
    return CuratedTables(outputs["M"], outputs["Y"], structure, outputs["passport"], outputs["measurements"], report, metadata, originals[0], originals[1], warnings)


def read_bundle(leaf: Path, *, assume_paired_y: bool = False, allow_unaligned_y: bool = False, verify_spectral_order: bool = False) -> tuple[pd.DataFrame, pd.DataFrame, list[str]]:
    from nirs4all_datasets.canonical import _sniff_sep

    warnings = []
    tables = {}
    for role in ["M", "Y"]:
        path = leaf / f"{role}.csv"
        tables[role] = pd.read_csv(path, sep=_sniff_sep(path), dtype=str, keep_default_na=False) if path.is_file() else pd.DataFrame(columns=[_OBS])
    m, y = tables["M"], tables["Y"]
    if _OBS not in m and len(m):
        raise ValueError("M.csv must declare observation_id")
    if _OBS not in y:
        can_pair = assume_paired_y and len(y) == len(m) and m[_OBS].ne("").all() and m[_OBS].is_unique
        if can_pair and verify_spectral_order:
            from nirs4all_datasets.canonical import _x_files

            can_pair = False
            for path in _x_files(leaf).values():
                ids = pd.read_csv(path, sep=_sniff_sep(path), usecols=[0], dtype=str, keep_default_na=False).iloc[:, 0]
                if ids.name == _OBS and ids.equals(m[_OBS]):
                    can_pair = True
                    break
        if can_pair:
            y.insert(0, _OBS, m[_OBS].to_numpy())
            warnings.append("Y/M row pairing explicitly assumed; not independently verified by target identifiers.")
        elif allow_unaligned_y:
            y = pd.DataFrame(columns=[_OBS, *y.columns])
            warnings.append("Y alignment unavailable: keyless targets were excluded from aligned views; original Y retained unchanged.")
        else:
            raise ValueError("Y.csv has no observation_id; pass an explicit source pairing contract (--assume-paired-y) or supply keyed targets")
    return m, y, warnings


def write_curated(tables: CuratedTables, directory: Path) -> dict[str, Any]:
    """Write heavy view tables outside Git and their small, versioned mapping report."""
    directory.mkdir(parents=True, exist_ok=True)
    paths = {}
    for name, table in [("M", tables.metadata), ("Y", tables.targets), ("structure", tables.structure), ("passport", tables.passport), ("measurements", tables.measurements), ("original_M", tables.original_metadata), ("original_Y", tables.original_targets)]:
        path = directory / f"{name}.parquet"
        table.to_parquet(path, index=False, compression="zstd")
        paths[name] = str(path)
    (directory / "mapping.json").write_text(json.dumps(tables.report, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    return {"schema_version": CURATION_VERSION, "grain": "observation", "join_key": _OBS, "tables": paths, "mapping": str(directory / "mapping.json")}


def _source_fields(leaf: Path) -> dict[str, dict[str, Any]]:
    """Read author-declared units/missing tokens; never infer numerical sentinels."""
    path = leaf / "datapackage.json"
    if not path.is_file():
        return {}
    package = json.loads(path.read_text(encoding="utf-8"))
    result = {}
    for resource in package.get("resources", []):
        name = Path(str(resource.get("path", ""))).stem.upper()
        if name not in {"M", "Y"}:
            continue
        schema = resource.get("schema") or {}
        if not isinstance(schema, dict):
            continue
        for field_spec in schema.get("fields", []):
            field_name = field_spec.get("name")
            if not field_name:
                continue
            entry: dict[str, Any] = {}
            tokens = field_spec.get("missingValues", schema.get("missingValues"))
            if isinstance(tokens, list):
                entry["missing_rule"] = {"tokens": [str(token) for token in tokens], "evidence": f"datapackage.json/{name}/schema/{field_name}/missingValues", "confirmed": True}
            if isinstance(field_spec.get("unit"), str):
                entry["unit"] = field_spec["unit"]
            statistical_type = field_spec.get("type")
            if statistical_type in {"integer", "number"}:
                entry["statistical_type"] = "numeric"
            elif statistical_type in {"string", "boolean", "date", "datetime", "time"}:
                entry["statistical_type"] = "categorical"
            for source_key, canonical_key in [("decimalChar", "decimal_separator"), ("groupChar", "thousands_separator")]:
                if source_key in field_spec:
                    entry[canonical_key] = field_spec[source_key]
            if "decimal_separator" in entry or "thousands_separator" in entry:
                Variable(name=str(field_name), decimal_separator=entry.get("decimal_separator", ","), thousands_separator=entry.get("thousands_separator"))
            if entry:
                result[f"{name}:{field_name}"] = entry
    return result


def curate_bundle(leaf: Path, dataset_id: str, *, soilsite: Path | None = None, assume_paired_y: bool = False, numeric_names: set[str] | None = None, categorical_names: set[str] | None = None, allow_unaligned_y: bool = False, verify_spectral_order: bool = False, variable_specs: list[Variable] | None = None) -> CuratedTables:
    m, y, warnings = read_bundle(leaf, assume_paired_y=assume_paired_y, allow_unaligned_y=allow_unaligned_y, verify_spectral_order=verify_spectral_order)
    if m.empty and not y.empty:
        m = y[[_OBS]].copy()
    fields = _source_fields(leaf)
    for variable in variable_specs or []:
        original = variable.original_name or variable.name
        for role, frame in [("M", m), ("Y", y)]:
            if original not in frame:
                continue
            field_rule = fields.setdefault(f"{role}:{original}", {})
            # The curated descriptor carries the reviewed scientific type. Source
            # CSV schemas can label measured numbers as strings (UCPH Granules).
            if "type" in variable.model_fields_set and variable.type in {VarType.NUMERIC, VarType.CATEGORICAL}:
                field_rule["statistical_type"] = variable.type.value
            for key in ["unit", "semantic_role", "equivalent_to", "derived_from"]:
                value = getattr(variable, key)
                if value:
                    field_rule[key] = value
            for key in ["decimal_separator", "thousands_separator"]:
                if key in variable.model_fields_set:
                    field_rule[key] = getattr(variable, key)
    result = curate_tables(dataset_id, m, y, soilsite=soilsite or (find_soilsite(leaf) if dataset_id.startswith("ossl_") else None), numeric_names=numeric_names, categorical_names=categorical_names, source_fields=fields)
    result.warnings.extend(warnings)
    result.report["warnings"] = result.warnings
    if any(warning.startswith("Y/M row pairing explicitly assumed;") for warning in warnings):
        # Keep the original keyless Y schema intact. The added aligned key is a
        # derivation from M, not a column that existed in the source Y file.
        result.original_targets = result.original_targets.drop(columns=[_OBS])
        for entry in result.report["mapping"]:
            if entry["source_resource"] == "Y.csv" and entry["original_name"] == _OBS:
                entry.update({"source_resource": "M.csv", "target_resource": "Y.csv", "operation": "assumed_row_pairing_to_Y", "independently_verified_target_ids": False, "M_X_order_checked": verify_spectral_order})
    if any(warning.startswith("Y alignment unavailable:") for warning in warnings):
        from nirs4all_datasets.canonical import _sniff_sep

        original_y = pd.read_csv(leaf / "Y.csv", sep=_sniff_sep(leaf / "Y.csv"), dtype=str, keep_default_na=False)
        result.original_targets = original_y
        result.report["mapping"] = [entry for entry in result.report["mapping"] if not (entry["source_resource"] == "Y.csv" and entry["original_name"] == _OBS)]
        for entry in result.report["mapping"]:
            if entry["source_resource"] == "Y.csv":
                entry["view"] = "unavailable"
                entry["operation"] = "unaligned_target_preserved_in_original_Y"
                entry["stats"] = variable_stats(normalize_missing(original_y[entry["original_name"]]), numeric=entry.get("stats", {}).get("type") == "numeric")
    from nirs4all_datasets.manifest import sha256_file

    result.report["source_hashes"] = {f"{role}.csv": sha256_file(leaf / f"{role}.csv") for role in ["M", "Y"] if (leaf / f"{role}.csv").is_file()}
    return result


def card_curation(report: dict[str, Any]) -> dict[str, Any]:
    """Keep cards compact; the exhaustive mapping remains a separately verified artifact."""
    return {**{key: value for key, value in report.items() if key != "mapping"}, "mapping": "canonical/curation/mapping.json"}


def curate_tree(source_tree: Path, output: Path, *, soilsite: Path | None = None, assume_paired_y: bool = False, only: set[str] | None = None) -> dict[str, Any]:
    """Recompute small, reviewable curation reports without reading spectra or publishing data."""
    if (source_tree / "dataset_card.json").is_file():
        leaves = [source_tree]
    else:
        base = next((source_tree / name for name in ["v2.0", "standardized_datasets"] if (source_tree / name).is_dir()), source_tree)
        leaves = sorted(path.parent for path in base.glob("*/dataset_card.json"))
    output.mkdir(parents=True, exist_ok=True)
    summary: dict[str, Any] = {"schema_version": CURATION_VERSION, "processed": [], "errors": [], "assume_paired_y": assume_paired_y}
    for leaf in leaves:
        card = json.loads((leaf / "dataset_card.json").read_text(encoding="utf-8"))
        from nirs4all_datasets.bootstrap import slugify

        dataset_id = slugify(card.get("dataset_id") or leaf.name)
        if only and dataset_id not in only:
            continue
        try:
            # Dataset cards explicitly marked anonymized must not publish raw mappings.
            result = curate_bundle(leaf, dataset_id, soilsite=soilsite, assume_paired_y=assume_paired_y)
            report = result.report
            if str(card.get("tier", "")).casefold() == "anonymized":
                report = {"schema_version": CURATION_VERSION, "dataset_id": dataset_id, "view_counts": {key: len(value) for key, value in result.report["views"].items()}, "mapping": "withheld for anonymized tier"}
            (output / f"{dataset_id}.json").write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
            summary["processed"].append({"dataset_id": dataset_id, "n_observations": len(result.structure), "n_samples": result.report["identity"]["n_samples"], "identity_status": result.report["identity"]["status"], "n_M": len(result.report["views"]["M"]), "n_Y": len(result.report["views"]["Y"]), "warnings": result.warnings})
        except (ValueError, KeyError, OSError) as exc:
            summary["errors"].append({"dataset_id": dataset_id, "error": str(exc)})
    (output / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    return summary


# Descriptor-driven adapters preserve typed original-name/dialect contracts.
CURATION_PROTOCOL = CURATION_VERSION
_ID_ALIASES = ("sample_id", "id_sample", "ID_sample", "SampleID", "source_sample_id")
_DESCRIPTOR_PASSPORT = frozenset({"dataset_id", "observation_id", "sample_id", "notes", "note", "license", "license_id", "license_url", "rights_status", "usage_scope", "source_file", "source_file_spectra", "source_file_metadata", "source_dataset_title", "source_dataset_url", "source_dataset_doi", "source_package_url", "source_resource", "source_relative_dir", "source_root", "source_grouped_y_exports", "source_member", "source_subset", "target_file", "source_url", "source_page", "sample_id_available", "public_release_allowed", "n_points_original", "axis_unit", "axis_min", "axis_max", "official_source_url", "official_data_url", "official_package_url", "standardization_batch", "ecosis_resource_id", "dataset", "dataset_slug", "dataset_title", "dataset_owner", "task_type", "trait_header", "trait_header_original", "target_original_name", "spectroscopy_type", "signal_type", "dimensions", "wavelength_note", "source_label", "split_original", "split_source", "original_split"})


def is_provenance_column(name: str) -> bool:
    """Known passport fields only; source_temperature remains experimental context."""
    lower = name.lower()
    return lower in _DESCRIPTOR_PASSPORT or lower.startswith(("manual_download", "license_", "doi_"))


def semantic_role(name: str, *, target: bool = False) -> str:
    """Classify known plumbing exactly; scientific API/reference names stay measured."""
    lower = name.lower()
    if target:
        return "measured_trait"
    if is_provenance_column(name):
        return "provenance"
    if lower.endswith("_id") or lower.endswith("_identifier") or lower in {"spectralrep", "class_index", "replicate", "compound_rep_index", "batch_number", "pot_number", "acquisition_index"}:
        return "identifier"
    return "experimental_context"


def normalize_variable(values: pd.Series, variable: Variable) -> tuple[pd.Series, dict[str, Any]]:
    """Apply only declared missing/dialect rules, retaining per-row raw tokens and reasons."""
    raw = values.astype("string")
    text = raw.str.strip()
    missing = values.isna() | text.eq("").fillna(False)
    declared = {token.casefold() for token in variable.missing_values}
    missing |= text.str.casefold().isin(declared)
    reasons = pd.Series("", index=values.index, dtype="string")
    reasons.loc[missing] = "not_reported"
    censored = pd.Series(False, index=values.index)
    normalized = values.copy()
    normalized.loc[missing] = None
    invalid = pd.Series(False, index=values.index)
    if variable.type.value == "numeric":
        numeric_text = text
        if variable.thousands_separator:
            # Reject malformed groups instead of turning 0.1 into 1 under a
            # declared dot-thousands/comma-decimal dialect.
            group = re.escape(variable.thousands_separator)
            decimal = re.escape(variable.decimal_separator)
            integer = rf"(?:\d+|\d{{1,3}}(?:{group}\d{{3}})+)"
            number = rf"[+-]?(?:{integer}(?:{decimal}\d*)?|{decimal}\d+)(?:[eE][+-]?\d+)?"
            candidate = text.str.replace(r"^(?:[<>]=?|≤|≥)\s*", "", regex=True)
            valid_grouping = candidate.str.fullmatch(number, na=False)
            numeric_text = numeric_text.mask(~valid_grouping & ~text.str.match(r"^below\s+(?:lod|loq)(?:\s.*)?$", case=False, na=False))
            numeric_text = numeric_text.str.replace(variable.thousands_separator, "", regex=False)
        if variable.decimal_separator != ".":
            numeric_text = numeric_text.str.replace(variable.decimal_separator, ".", regex=False)
        censored = numeric_text.str.match(_CENSORED, na=False) | numeric_text.str.match(r"^below\s+(?:lod|loq)(?:\s.*)?$", case=False, na=False)
        parsed = pd.to_numeric(numeric_text.mask(missing | censored), errors="coerce")
        sentinel = parsed.isin(variable.numeric_sentinels)
        missing |= sentinel
        reasons.loc[sentinel] = "declared_sentinel"
        invalid = ~missing & ~censored & (parsed.isna() | ~np.isfinite(parsed))
        reasons.loc[invalid] = "invalid"
        reasons.loc[censored] = "censored"
        normalized = parsed.mask(missing | censored | invalid)
    audit: dict[str, Any] = {
        "protocol_version": CURATION_PROTOCOL, "original_name": variable.original_name or variable.name,
        "name": variable.name, "total": len(values), "present": int((~missing & ~invalid & ~censored).sum()),
        "missing": int(missing.sum()), "invalid": int(invalid.sum()), "censored": int(censored.sum()),
        "distinct": int(normalized.nunique(dropna=True)), "unit": variable.unit,
        "missing_values": list(variable.missing_values), "numeric_sentinels": list(variable.numeric_sentinels),
        "decimal_separator": variable.decimal_separator, "thousands_separator": variable.thousands_separator,
        "rows": [{"raw": None if pd.isna(value) else str(value), "status": str(reason)} for value, reason in zip(values, reasons, strict=True)],
    }
    for row in audit["rows"]:
        if row["status"] != "censored":
            continue
        token = row["raw"].strip()
        if variable.thousands_separator:
            token = token.replace(variable.thousands_separator, "")
        if variable.decimal_separator != ".":
            token = token.replace(variable.decimal_separator, ".")
        match = _CENSORED.fullmatch(token)
        operator = {"≤": "<=", "≥": ">="}.get(match.group(1), match.group(1)) if match else "below_detection_limit"
        row["censoring"] = {"operator": operator, "bound": float(match.group(2).replace(",", ".")) if match else None, "unit": variable.unit}
    return normalized, audit


def consumer_views(frame: pd.DataFrame, descriptor: DatasetDescriptor, *, targets: list[str] | None = None) -> dict[str, Any]:
    """Build explicit Y/M/structure/passport views while keeping every original column.

    Only declared targets are default Y. Scientific names containing API/reference
    are not passport evidence. Target aliases/copies/declared derivations stay out of M.
    """
    target_names = targets if targets is not None else [v.name for v in descriptor.targets]
    unknown = set(target_names) - {v.name for v in descriptor.variables}
    if unknown:
        raise ValueError(f"unknown target variables: {sorted(unknown)}")
    y = [name for name in target_names if name in frame]
    m, structure, passport = [], ["sample_id"] if "sample_id" in frame else [], []
    decisions = []
    for variable in descriptor.variables:
        name = variable.name
        if name not in frame or name in y:
            continue
        role = variable.semantic_role or semantic_role(name, target=variable.role.value == "target")
        if role in {"provenance", "governance"}:
            passport.append(name)
            reason = role
        elif role in {"identifier", "acquisition_index"}:
            structure.append(name)
            reason = role
        elif set(variable.derived_from) & set(y) or variable.equivalent_to in y:
            reason = "target_copy_or_declared_derivation"
        elif descriptor.id.startswith("ucph_granules_") and "api_reference_percent_w_w" in y and name == "api_concentration_design_percent":
            reason = "target_design_information"
        elif frame[name].nunique(dropna=True) < 2:
            reason = "empty_or_constant"
        elif role != "experimental_context":
            reason = "not_experimental_context"
        else:
            m.append(name)
            reason = "experimental_context"
        decisions.append({"name": name, "role": role, "reason": reason})
    def select(names: list[str]) -> pd.DataFrame:
        keys = ["sample_id"] if "sample_id" in frame and "sample_id" not in names else []
        return frame[keys + names].copy()
    return {"protocol_version": CURATION_PROTOCOL, "Y": select(y), "M": select(m), "structure": select(structure), "passport": select(passport), "decisions": decisions, "original": frame.copy()}


LUCAS_SOILSITE_FIELDS = {key: {"campaign_date_begin": "campaign_start_date", "campaign_date_end": "campaign_end_date", "location_error_m": "coordinate_uncertainty_m"}.get(value, value) for key, value in _SOILSITE_MAPPING.items()}


def identity_frame(dataset_id: str, metadata: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    """Adapt the shared identity contract for legacy descriptor consumers."""
    structure, report = identity_view(dataset_id, metadata)
    out = metadata.copy()
    if "sample_id" in out:
        out["source_sample_id_raw"] = out["sample_id"]
    for column in structure:
        if column != _OBS:
            out[column] = structure[column]
    missing = out[_SAMPLE].isna()
    out.loc[missing, _SAMPLE] = out.loc[missing, _OBS]
    aliases = [name for name in _ID_ALIASES if name in metadata]
    report = {**report, "protocol_version": CURATION_PROTOCOL, "dataset_id": dataset_id,
              "sample_id_available": report["status"] == "available", "n_units": report["n_samples"] if report["status"] == "available" else None,
              "n_observations": len(metadata), "rule": report["method"], "independence": "unknown",
              "identity_columns": {name: {"distinct": int(metadata[name].nunique(dropna=True)), "role": "hierarchical_source_identifier" if name == "source_sample_id" else "sample_identity_alias"} for name in aliases}}
    return out, report


def enrich_lucas_metadata(metadata: pd.DataFrame, soilsite_path: str) -> tuple[pd.DataFrame, dict[str, Any]]:
    """Compatibility projection over the owner OSSL join; no second join implementation."""
    enriched, evidence, warnings = enrich_ossl("ossl_lucas_visnir_soil_all_y", metadata, Path(soilsite_path))
    if warnings:
        raise ValueError("; ".join(warnings))
    enriched = enriched.rename(columns={value: LUCAS_SOILSITE_FIELDS[key] for key, value in _SOILSITE_MAPPING.items()})
    from nirs4all_datasets.manifest import sha256_file
    report = {"protocol_version": CURATION_PROTOCOL, "source_sha256": sha256_file(soilsite_path), "field_mapping": LUCAS_SOILSITE_FIELDS,
              "derived": {"campaign_year": "source period start year; not individual collection date"},
              "n_sites": int(enriched["site_id"].nunique()), "evidence": evidence}
    return enriched, report
