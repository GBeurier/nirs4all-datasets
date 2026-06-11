"""Render a Datasheets-for-Datasets ``card.md`` from a schema-2.0 card + descriptor.

Follows the seven Gebru et al. (2021) sections, adapted to a raw multi-source NIRS dataset: one row
per X :class:`~nirs4all_datasets.schema.Source` (instrument/axis/n), one row per
:class:`~nirs4all_datasets.schema.Variable` (role/type/stats), the sample-identity alignment, native
splits (documented, never applied), provenance with linked publications, governance keyed on the
visibility :class:`~nirs4all_datasets.schema.Tier`, and the integrity/version block.

Pure card+descriptor -> Markdown (no nirs4all, no templating dependency). Fields with no source
render as ``*Not specified.*`` — honest gaps, never fabricated.
"""
from __future__ import annotations

import math
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from nirs4all_datasets.schema import DatasetDescriptor

# Tier wording (Tier value -> a one-line distribution policy statement).
_TIER_WORDING = {
    "public": "Open — freely usable and redistributable under the stated license.",
    "private": "Private — export requires an access token (Dataverse); not openly redistributable.",
    "anonymized": "Anonymized — variable names are masked and numeric targets are normalized (z-scored); export requires a token.",
}


def _na(value: Any) -> str:
    """Render a value for inline Markdown, neutralizing newlines/pipes; ``*Not specified.*`` when empty."""
    if value is None or value == "" or value == []:
        return "*Not specified.*"
    return str(value).replace("\r", " ").replace("\n", " ").replace("|", "\\|").strip()


def _fmt(value: Any, nd: int = 4) -> str:
    """Compact rendering of a number (rounded) for the datasheet; falls back to ``_na``."""
    if isinstance(value, bool) or value is None:
        return _na(value)
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        return _na(None) if not math.isfinite(value) else f"{value:.{nd}g}"
    return _na(value)


def _source_rows(card: dict[str, Any]) -> list[str]:
    """One Markdown table row per source: instrument, modality, axis unit/range, n_obs x n_vars."""
    rows: list[str] = []
    for src in card.get("sources") or []:
        axis = f"{_fmt(src.get('axis_min'))}–{_fmt(src.get('axis_max'))} {_na(src.get('axis_unit'))}"
        rows.append(
            f"| {_na(src.get('source_id'))} | {_na(src.get('name'))} | {_na(src.get('instrument_name'))} | "
            f"{_na(src.get('modality'))} | {axis} | {_na(src.get('n_observations'))} | {_na(src.get('n_variables'))} |"
        )
    return rows


def _numeric_stat_cells(stats: dict[str, Any]) -> str:
    """Render numeric variable stats as a compact ``n / missing / range / mean±std`` cell."""
    rng = f"{_fmt(stats.get('min'))}–{_fmt(stats.get('max'))}" if stats.get("min") is not None or stats.get("max") is not None else "—"
    return f"n={_na(stats.get('n'))}, missing={_na(stats.get('n_missing'))}, range {rng}, mean {_fmt(stats.get('mean'))} ± {_fmt(stats.get('std'))}"


def _categorical_stat_cells(stats: dict[str, Any]) -> str:
    """Render categorical variable stats as ``n / missing / n_classes / top class``."""
    top = stats.get("top_classes") or []
    head = f"top {_na(top[0].get('name'))} (×{_na(top[0].get('count'))})" if top else "—"
    return f"n={_na(stats.get('n'))}, missing={_na(stats.get('n_missing'))}, classes={_na(stats.get('n_classes'))}, {head}"


def _variable_rows(card: dict[str, Any]) -> list[str]:
    """One Markdown table row per variable: name, role, type, unit, summary stats."""
    rows: list[str] = []
    for var in card.get("variables") or []:
        stats = var.get("stats") or {}
        if var.get("type") == "numeric":
            summary = _numeric_stat_cells(stats) if stats else _na(None)
        elif var.get("type") == "categorical":
            summary = _categorical_stat_cells(stats) if stats else _na(None)
        else:
            summary = _na(None)
        rows.append(
            f"| {_na(var.get('name'))} | {_na(var.get('role'))} | {_na(var.get('type'))} | "
            f"{_na(var.get('unit'))} | {summary} |"
        )
    return rows


def _split_lines(card: dict[str, Any]) -> list[str]:
    """One bullet per native split, documenting the partition counts (never applied)."""
    splits = card.get("splits") or []
    if not splits:
        return ["- *No native split documented.*"]
    lines: list[str] = []
    for split in splits:
        partitions = ", ".join(f"{name}: {count}" for name, count in (split.get("partitions") or {}).items()) or "*Not specified.*"
        lines.append(f"- **{_na(split.get('name'))}** (documented, not applied): {partitions}")
    return lines


def _publication_lines(descriptor: DatasetDescriptor) -> list[str]:
    """One bullet per related publication, with a resolvable DOI link when present."""
    if not descriptor.publications:
        return ["- *No related publication.*"]
    lines: list[str] = []
    for pub in descriptor.publications:
        link = f"[{pub.doi}](https://doi.org/{pub.doi})" if pub.doi else "*no DOI*"
        title = _na(pub.title)
        year = f" ({pub.year})" if pub.year else ""
        lines.append(f"- {title}{year} — {link}")
    return lines


def _origin_lines(card: dict[str, Any]) -> list[str]:
    """One bullet per origin source (where the bytes live): kind, access, license, locator."""
    origins = (card.get("provenance") or {}).get("origin_sources") or []
    if not origins:
        return ["- *No origin source recorded.*"]
    lines: list[str] = []
    for src in origins:
        title = _na(src.get("title"))
        lines.append(f"- {title} — kind `{_na(src.get('kind'))}`, access `{_na(src.get('access'))}`, license {_na(src.get('license'))}: `{_na(src.get('locator'))}`")
    return lines


def render_datasheet(card: dict[str, Any], descriptor: DatasetDescriptor) -> str:
    """Return a Datasheets-for-Datasets Markdown document for a schema-2.0 dataset.

    Args:
        card: The built ``card.json`` (THE CARD JSON CONTRACT).
        descriptor: The dataset descriptor (origin sources, publications, governance, versions).

    Returns:
        A Markdown string following the seven Gebru et al. (2021) datasheet sections.
    """
    identity = card.get("identity") or {}
    alignment = card.get("alignment") or {}
    provenance = card.get("provenance") or {}
    governance = card.get("governance") or {}
    integrity = card.get("integrity") or {}
    versions = card.get("versions") or {}
    reps = alignment.get("reps_per_sample") or {}
    tier = governance.get("tier") or identity.get("tier")

    reps_text = (
        f"{_fmt(reps.get('min'))}–{_fmt(reps.get('max'))} (mean {_fmt(reps.get('mean'))})"
        if reps else "1 (one observation per sample)"
    )

    lines = [
        f"# Datasheet — {_na(identity.get('name'))}",
        "",
        "_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._",
        "",
        "## Motivation",
        "",
        f"- **Domain / purpose:** {_na(identity.get('domain'))}",
        f"- **Description:** {_na(identity.get('description'))}",
        f"- **Keywords:** {_na(', '.join(identity.get('keywords') or []))}",
        f"- **Contributor:** {_na(provenance.get('contributor'))}",
        "",
        "## Composition",
        "",
        f"- **Alignment:** {_na(alignment.get('level'))} level; "
        f"{_na(alignment.get('n_samples'))} sample(s), {_na(alignment.get('n_observations_total'))} observation(s) total; "
        f"sample_id available: {_na(alignment.get('sample_id_available'))}.",
        f"- **Repetitions per sample:** {reps_text}.",
        "",
        "### Sources (X)",
        "",
        "| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |",
        "| --- | --- | --- | --- | --- | --- | --- |",
        *_source_rows(card),
        "",
        "### Variables (Y / metadata)",
        "",
        "| Name | Role | Type | Unit | Summary |",
        "| --- | --- | --- | --- | --- |",
        *(_variable_rows(card) or ["| *No variables (X-only dataset).* | | | | |"]),
        "",
        "## Statistics — splits",
        "",
        "Splits are **documented, never auto-applied** (the supervised task is a consumer choice).",
        "",
        *_split_lines(card),
        "",
        "## Collection process",
        "",
        f"- **Reference method:** {_na(provenance.get('reference_method'))}",
        f"- **Conversion status:** {_na(provenance.get('conversion_status'))}",
        "",
        "### Origin sources (where the bytes live)",
        "",
        *_origin_lines(card),
        "",
        "## Preprocessing / cleaning / labeling",
        "",
        f"- **Conversion warnings:** {_na('; '.join(provenance.get('warnings') or []) or None)}",
        "",
        "## Uses",
        "",
        f"- **Permitted use:** {_na(governance.get('permitted_use'))}",
        f"- **Access policy:** {_na(governance.get('access_policy'))}",
        "",
        "### Related publications",
        "",
        *_publication_lines(descriptor),
        "",
        "## Distribution",
        "",
        f"- **License:** {_na(governance.get('license'))}",
        f"- **Tier:** {_na(tier)} — {_na(_TIER_WORDING.get(tier) if tier else None)}",
        f"- **Redistribution rights:** {_na(governance.get('redistribution_rights'))}",
        f"- **DOI:** {_na(descriptor.dataverse.doi)}",
        "",
        "## Maintenance",
        "",
        f"- **Content version:** {_na(versions.get('content'))} | **schema/protocol:** {_na(versions.get('schema_protocol'))}",
        f"- **Content hash:** `{_na(integrity.get('content_hash'))}`",
        f"- **Processing hash:** `{_na(integrity.get('processing_hash'))}` | **metadata hash:** `{_na(integrity.get('metadata_hash'))}`",
        "",
    ]
    return "\n".join(lines)
