"""Explicit source identity, variable normalization and consumer-role views.

Source bytes remain untouched. Rules are versioned and column scoped; source labels,
provenance and acquisition-level values remain available outside predictive views.
"""
from __future__ import annotations

import json
import re
from typing import Any

import numpy as np
import pandas as pd

from nirs4all_datasets.schema import DatasetDescriptor, Variable

CURATION_PROTOCOL = "1"
_ID_ALIASES = ("sample_id", "id_sample", "ID_sample", "SampleID", "source_sample_id")
_PASSPORT = frozenset({"dataset_id", "observation_id", "sample_id", "notes", "note", "license", "license_id", "license_url", "rights_status", "usage_scope", "source_file", "source_file_spectra", "source_file_metadata", "source_dataset_title", "source_dataset_url", "source_dataset_doi", "source_package_url", "source_resource", "source_relative_dir", "source_root", "source_grouped_y_exports", "source_member", "source_subset", "target_file", "source_url", "source_page", "sample_id_available", "public_release_allowed", "n_points_original", "axis_unit", "axis_min", "axis_max", "official_source_url", "official_data_url", "official_package_url", "standardization_batch", "ecosis_resource_id", "dataset", "dataset_slug", "dataset_title", "dataset_owner", "task_type", "trait_header", "trait_header_original", "target_original_name", "spectroscopy_type", "signal_type", "dimensions", "wavelength_note", "source_label", "split_original", "split_source", "original_split"})


def is_provenance_column(name: str) -> bool:
    """Known passport fields only; source_temperature remains experimental context."""
    lower = name.lower()
    return lower in _PASSPORT or lower.startswith(("manual_download", "license_", "doi_"))


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
    censored = text.str.match(r"^(?:[<>]=?\s*[-+]?\d|below\s+(?:lod|loq))", case=False, na=False)
    normalized = values.copy()
    normalized.loc[missing] = None
    invalid = pd.Series(False, index=values.index)
    if variable.type.value == "numeric":
        numeric_text = text
        if variable.thousands_separator:
            numeric_text = numeric_text.str.replace(variable.thousands_separator, "", regex=False)
        if variable.decimal_separator != ".":
            numeric_text = numeric_text.str.replace(variable.decimal_separator, ".", regex=False)
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
        match = re.fullmatch(r"([<>]=?)\s*([-+]?\d+(?:[.,]\d+)?)", row["raw"].strip())
        row["censoring"] = {"operator": match.group(1) if match else "below_detection_limit", "bound": float(match.group(2).replace(",", ".")) if match else None, "unit": variable.unit}
    return normalized, audit


def identity_frame(dataset_id: str, metadata: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    """Apply verified source-specific identities; never strip scan suffixes generically."""
    out = metadata.copy()
    if "observation_id" not in out or out["observation_id"].isna().any() or out["observation_id"].astype(str).str.strip().eq("").any() or out["observation_id"].duplicated().any():
        raise ValueError("M.csv requires unique nonempty observation_id values")
    report: dict[str, Any] = {"protocol_version": CURATION_PROTOCOL, "dataset_id": dataset_id, "sample_id_available": True, "unit": "source_declared", "independence": "unknown", "rule": "declared_identity"}
    primary_aliases = [name for name in _ID_ALIASES if name in out and name != "source_sample_id"]
    if len(primary_aliases) > 1:
        first = out[primary_aliases[0]].astype("string")
        for other in primary_aliases[1:]:
            values = out[other].astype("string")
            if not (first.eq(values) | (first.isna() & values.isna())).fillna(False).all():
                raise ValueError("ambiguous sample identity aliases; provide an explicit source mapping")
    report["identity_columns"] = {name: {"distinct": int(out[name].nunique(dropna=True)), "role": "hierarchical_source_identifier" if name == "source_sample_id" and primary_aliases else "sample_identity_alias"} for name in _ID_ALIASES if name in out}
    alias = next((name for name in _ID_ALIASES if name in out), None)
    if alias is not None and alias != "sample_id":
        out["sample_id"] = out[alias]
        report["original_column"] = alias
    if "sample_id" in out:
        out["source_sample_id_raw"] = out["sample_id"]
    if dataset_id == "mendeley_human_arm_muscle_vis_swir_reflectance" and {"subject_id", "arm_aspect_code"} <= set(out):
        out["sample_id"] = [json.dumps([str(a), str(b)], separators=(",", ":")) for a, b in zip(out["subject_id"], out["arm_aspect_code"], strict=True)]
        report.update(unit="subject_aspect", independence="group_by_subject", rule="subject_id_x_arm_aspect_code")
    elif dataset_id in {"ucph_granules_ambient_moisture_api_nir", "ucph_granules_moisture_controlled_api_nir"} and "sample_id" in out:
        labels = out["sample_id"].astype(str)
        matches = labels.str.extract(r"^(?P<vial>.+_v\d+)\.(?P<acquisition>[012])$")
        if matches.isna().any().any() or matches.groupby("vial")["acquisition"].agg(lambda v: set(v) != {"0", "1", "2"} or len(v) != 3).any():
            raise ValueError("UCPH granules identity requires exactly the documented .0/.1/.2 acquisitions per vial")
        out["original_sample_id"] = labels
        out["sample_id"] = matches["vial"]
        out["acquisition_index"] = matches["acquisition"]
        report.update(unit="vial", independence="group_by_batch", rule="ucph_granules_documented_triplicates", technical_reacquisitions=3)
    elif dataset_id in {"ossl_lucas_visnir_soil_all_y", "ossl_lucas_mir_soil_all_y"} and "ID_sample" in out:
        out["sample_id"] = out["ID_sample"].astype(str)
        report.update(unit="soil_layer_campaign", independence="group_by_site_when_soilsite_available", rule="ossl_documented_layer_identity")
    elif dataset_id in {"canopy_treatment_2009_2016_to_cedar_ecosis", "soil_elevation_2024_lake_fire_ecosis", "nirpy_milk_nir", "nirpy_milk_powder_nir"}:
        if "sample_id" in out:
            out["original_sample_id"] = out["sample_id"]
        out["sample_id"] = out["observation_id"]
        report.update(sample_id_available=False, unit="unavailable", rule="experiment_date_or_reused_label_is_not_specimen_identity", reason="physical_identity_not_documented")
    elif dataset_id == "dryad_rice_leaf_reflectance_manual" and {"variety", "source_sample_id"} <= set(out):
        out["sample_id"] = [json.dumps([str(a), str(b)], separators=(",", ":")) for a, b in zip(out["variety"], out["source_sample_id"], strict=True)]
        report.update(unit="variety_local_column", rule="variety_x_source_sample_id")
    elif dataset_id in {"flanagan_api_compounds_raman", "drug_compound_flanagan_raman", "drug_common_application_flanagan_raman", "drug_solvent_reagent_flanagan_raman"}:
        product = next((name for name in ("compound_key", "source_label", "product") if name in out), None)
        if product is None or out[product].isna().any() or out[product].astype(str).str.strip().eq("").any():
            raise ValueError("Flanagan acquisitions require the documented product identity")
        out["original_sample_id"] = out["sample_id"]
        out["sample_id"] = out[product].astype(str)
        report.update(unit="product", independence="preparations_unknown", rule="documented_product_label", technical_reacquisitions="documented_probe_repositioning")

    if "sample_id" not in out:
        out["sample_id"] = out["observation_id"]
        report.update(sample_id_available=False, unit="unavailable", reason="sample_id_absent")
    blank = out["sample_id"].isna() | out["sample_id"].astype(str).str.strip().eq("")
    if blank.any():
        # Missing IDs stay independent observations; never merge all blanks into one group.
        out.loc[blank, "sample_id"] = out.loc[blank, "observation_id"]
        report.update(sample_id_available=False, reason="partially_missing_sample_id")
    out["sample_id"] = out["sample_id"].astype(str)
    report.update(n_observations=len(out), n_units=int(out["sample_id"].nunique()) if report["sample_id_available"] else None)
    return out, report


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
        elif set(variable.derived_from) & set(y) or variable.equivalent_to in y or any((frame[name].eq(frame[target]) | (frame[name].isna() & frame[target].isna())).all() for target in y):
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


LUCAS_SOILSITE_FIELDS = {
    "id.dataset.site_ascii_txt": "site_id",
    "observation.date.begin_iso.8601_yyyy.mm.dd": "campaign_start_date",
    "observation.date.end_iso.8601_yyyy.mm.dd": "campaign_end_date",
    "longitude.point_wgs84_dd": "longitude",
    "latitude.point_wgs84_dd": "latitude",
    "location.point.error_any_m": "coordinate_uncertainty_m",
}


def enrich_lucas_metadata(metadata: pd.DataFrame, soilsite_path: str) -> tuple[pd.DataFrame, dict[str, Any]]:
    """Join source-versioned LUCAS sampling design, without reconstructing sites from coordinates."""
    from nirs4all_datasets.manifest import sha256_file

    site = pd.read_csv(soilsite_path, dtype=str, keep_default_na=False, na_values=[""])
    keys = ["dataset.code_ascii_txt", "id.layer_uuid_txt"]
    if not set(keys + list(LUCAS_SOILSITE_FIELDS)) <= set(site):
        raise ValueError("OSSL soilsite is missing documented LUCAS source fields")
    site = site[site[keys[0]] == "LUCAS.SSL"]
    if site[keys].isna().any().any() or site.duplicated(keys).any():
        raise ValueError("OSSL LUCAS soilsite join keys must be nonempty and unique")
    identity = next((name for name in ("ID_sample", "id_sample", "sample_id", "id.layer_uuid_txt") if name in metadata), None)
    if identity is None:
        raise ValueError("LUCAS observations need a documented OSSL layer identity")
    out = metadata.copy()
    if "dataset_code" in out and not out["dataset_code"].eq("LUCAS.SSL").all():
        raise ValueError("LUCAS metadata contains unexpected dataset codes")
    mapping = site.set_index(keys[1])
    if not out[identity].isin(mapping.index).all():
        raise ValueError("LUCAS metadata has layer IDs absent from soilsite; no positional fallback")
    for original, canonical in LUCAS_SOILSITE_FIELDS.items():
        matched = out[identity].map(mapping[original])
        if canonical in out and not out[canonical].fillna("").astype(str).equals(matched.fillna("").astype(str)):
            raise ValueError(f"LUCAS {canonical} conflicts with the pinned soilsite source")
        out[canonical] = matched
    out["campaign_year"] = out["campaign_start_date"].str.extract(r"^(\d{4})", expand=False)
    report = {
        "protocol_version": CURATION_PROTOCOL, "source_sha256": sha256_file(soilsite_path),
        "join": {"dataset.code_ascii_txt": "LUCAS.SSL", "id.layer_uuid_txt": identity},
        "field_mapping": LUCAS_SOILSITE_FIELDS,
        "derived": {"campaign_year": "year of campaign_start_date; source campaign interval, not individual collection date"},
        "n_observations": len(out), "n_sites": int(out["site_id"].nunique()),
        "campaign_counts": out["campaign_year"].value_counts().sort_index().to_dict(),
        "complete": {name: int(out[name].notna().sum()) for name in LUCAS_SOILSITE_FIELDS.values()},
        "grouping": "site_id keeps all campaigns of a site together; temporal follow-up is not a technical replicate",
    }
    return out, report
