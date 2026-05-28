"""Render a Datasheets-for-Datasets ``card.md`` from a descriptor + its card.

Follows the seven Gebru et al. (2021) sections. Pure descriptor/card -> Markdown (no nirs4all,
no templating dependency). Fields with no source render as ``*Not specified.*`` -- honest gaps,
never fabricated.
"""
from __future__ import annotations

import math
from typing import Any

from nirs4all_datasets.schema import DatasetDescriptor


def _na(value: Any) -> str:
    if value is None or value == "" or value == []:
        return "*Not specified.*"
    # Inline context: collapse newlines and neutralize table pipes so a descriptor string
    # cannot inject extra headings/bullets/rows.
    return str(value).replace("\r", " ").replace("\n", " ").replace("|", "\\|").strip()


def _fmt(value: Any, nd: int = 3) -> str:
    """Compact rendering of a number (rounded) for the datasheet; falls back to ``_na``."""
    if isinstance(value, bool) or value is None:
        return _na(value)
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        return _na(None) if not math.isfinite(value) else f"{value:.{nd}g}"
    return _na(value)


def render_datasheet(descriptor: DatasetDescriptor, card: dict[str, Any]) -> str:
    """Return a Datasheets-for-Datasets Markdown document for a dataset."""
    gov = descriptor.governance
    prov = descriptor.provenance
    inst = descriptor.instrument
    inventory = card.get("inventory", {})
    spectral = card.get("spectral", {})
    quality = card.get("quality", {})
    dim = card.get("dimensionality") or {}
    shift = (card.get("shift") or {}).get("target") or {}

    targets = ", ".join(f"{t.name} ({t.task_type.value}{', ' + t.unit if t.unit else ''})" for t in descriptor.targets)
    conversion = prov.conversion_status.value if prov.conversion_status is not None else None

    if "standardized_mean_diff" in shift:
        shift_summary = f"std. mean diff {_fmt(shift.get('standardized_mean_diff'))}, KS {_fmt(shift.get('ks_statistic'))} (p {_fmt(shift.get('ks_p'))}), Wasserstein {_fmt(shift.get('wasserstein'))}"
    elif "jensen_shannon" in shift:
        shift_summary = f"Jensen–Shannon {_fmt(shift.get('jensen_shannon'))}, max class-proportion Δ {_fmt(shift.get('max_abs_proportion_delta'))}"
    else:
        shift_summary = _na(None)

    lines = [
        f"# Datasheet — {descriptor.name}",
        "",
        "_Generated from the dataset descriptor and identity card (Datasheets for Datasets, Gebru et al. 2021)._",
        "",
        "## Motivation",
        "",
        f"- **Domain / purpose:** {_na(descriptor.domain)}",
        f"- **Description:** {_na(descriptor.description)}",
        f"- **Contributor:** {_na(prov.contributor)}",
        "",
        "## Composition",
        "",
        f"- **Instances:** {_na(inventory.get('n_samples', descriptor.n_samples))} spectra × "
        f"{_na(inventory.get('n_features', descriptor.n_features))} wavelengths, {_na(inventory.get('n_sources', descriptor.n_sources))} source(s).",
        f"- **Modality / instrument:** {_na(inst.modality.value)} — {_na(inst.vendor)} {_na(inst.model)} (firmware {_na(inst.firmware)}).",
        f"- **Spectral axis:** {_na(spectral.get('wavelength_range'))} {_na(spectral.get('wavelength_unit'))}; signal type {_na(spectral.get('signal_type'))}.",
        f"- **Targets:** {_na(targets)}",
        f"- **Contains missing values:** {_na(quality.get('has_nan'))}",
        "",
        "## Statistics",
        "",
        f"- **PCA / dimensionality:** effective rank {_fmt(dim.get('effective_rank'))}; "
        f"{_na(dim.get('n_components_95'))} PC(s) → 95% variance, {_na(dim.get('n_components_99'))} → 99%.",
        f"- **Train↔test target shift:** {shift_summary}",
        "",
        "## Collection process",
        "",
        f"- **Collection date:** {_na(prov.collection_date)}",
        f"- **Reference method:** {_na(prov.reference_method)}",
        f"- **Lab protocol:** {_na(prov.lab_protocol)}",
        f"- **Consent / ethics status:** {_na(gov.consent_ethics_status)}",
        f"- **Anonymization status:** {_na(gov.anonymization_status)}",
        "",
        "## Preprocessing / cleaning / labeling",
        "",
        f"- **Conversion:** {_na(prov.ingest_reader)} (status {_na(conversion)}).",
        f"- **Known exclusions:** {_na(prov.known_exclusions)}",
        "",
        "## Uses",
        "",
        f"- **Permitted use:** {_na(gov.permitted_use)}",
        f"- **Citation:** {_na(descriptor.citation)}",
        "",
        "## Distribution",
        "",
        f"- **License:** {_na(gov.license)}",
        f"- **Visibility:** {_na(gov.visibility.value)}",
        f"- **Confidentiality class:** {_na(gov.confidentiality_class.value)}",
        f"- **DOI:** {_na(descriptor.dataverse.doi)}",
        f"- **Redistribution rights:** {_na(gov.redistribution_rights)}",
        "",
        "## Maintenance",
        "",
        f"- **Owner / steward:** {_na(gov.owner_steward)}",
        f"- **Version:** {_na(descriptor.version)}",
        f"- **Access policy:** {_na(gov.access_policy)}",
        "",
    ]
    return "\n".join(lines)
