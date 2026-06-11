"""The anonymized-tier transform: opaque variable names + z-scored numeric targets.

The ``anonymized`` :class:`~nirs4all_datasets.schema.Tier` keeps a dataset usable for benchmarking
while leaking no identifying information: every variable column is renamed to a generic ``var_NNN``
slot (order preserved), every NUMERIC target is z-scored (deterministic ``(x-mean)/std``), and any
identifying free text in the card (descriptions, contributor, origin/publication titles) is masked.

Two layers are transformed, by the plugin ``get()`` and the static site, in lock-step:

* :func:`anonymize_variables` rewrites the canonical ``variables.parquet`` frame (data);
* :func:`anonymize_card` rewrites the already-built ``card.json`` (metadata).

Both are pure (no network, no I/O) and deterministic — the same input always yields the same output,
so an anonymized artifact is reproducible. The ``{original: generic}`` name map returned by
:func:`anonymize_variables` is the single source of truth for the renaming; :func:`anonymize_card`
recomputes the identical map from the card so the two stay aligned without sharing state.
"""
from __future__ import annotations

import copy
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:  # keep the module import-light; pandas is only needed by anonymize_variables
    import pandas as pd

    from nirs4all_datasets.schema import DatasetDescriptor

# The canonical join key is structural plumbing, never a variable; it is always preserved verbatim.
_JOIN_KEY = "sample_id"
_MASK = "---"


def _generic_name(index: int) -> str:
    """Return the opaque slot name for the ``index``-th (0-based) variable column."""
    return f"var_{index + 1:03d}"


def _numeric_target_names(descriptor: DatasetDescriptor) -> set[str]:
    """Names of variables that are NUMERIC prediction targets (the only columns that get z-scored)."""
    from nirs4all_datasets.schema import VariableRole, VarType

    return {v.name for v in descriptor.variables if v.role is VariableRole.TARGET and v.type is VarType.NUMERIC}


def anonymize_variables(df: pd.DataFrame, descriptor: DatasetDescriptor) -> tuple[pd.DataFrame, dict[str, str]]:
    """Anonymize a canonical ``variables.parquet`` frame: z-score numeric targets, mask all names.

    Every NUMERIC target column is replaced by its z-score ``(x - mean) / std`` computed over the
    finite values (population std; when ``std == 0`` the column becomes all-zeros — a constant carries
    no distributional information to leak). Every variable column is then renamed to a generic
    ``var_NNN`` slot in its original left-to-right order. The ``sample_id`` join key is kept verbatim
    (it is structural, not a variable) and is **not** counted in the ``var_NNN`` numbering.

    Args:
        df: The canonical per-sample variables frame (``sample_id`` + one column per variable).
        descriptor: The dataset descriptor (its ``variables`` give each column's role/type).

    Returns:
        ``(df_out, name_map)`` — a new frame (the input is not mutated) and the ``{original: generic}``
        map for every renamed variable column (``sample_id`` is not in the map).
    """
    targets = _numeric_target_names(descriptor)
    out = df.copy()

    for col in out.columns:
        if col == _JOIN_KEY or col not in targets:
            continue
        series = out[col].astype("float64")
        finite = series[series.notna()]
        mean = float(finite.mean()) if len(finite) else 0.0
        std = float(finite.std(ddof=0)) if len(finite) else 0.0
        out[col] = (series - mean) / std if std > 0.0 else (series - mean) * 0.0

    name_map: dict[str, str] = {}
    rename: dict[str, str] = {}
    slot = 0
    for col in out.columns:
        if col == _JOIN_KEY:
            continue
        generic = _generic_name(slot)
        name_map[col] = generic
        rename[col] = generic
        slot += 1

    out = out.rename(columns=rename)
    return out, name_map


def _anonymize_numeric_stats(stats: dict[str, Any]) -> dict[str, Any]:
    """Replace a z-scored numeric variable's stats with range-free, normalized values.

    After z-scoring, the only honest distributional facts left are: the count, the missing count,
    mean ~ 0 and std ~ 1. Location/scale facts (min/max/median/quartiles) are dropped to ``None`` so
    the anonymized card cannot be used to reconstruct the original target range.
    """
    n = stats.get("n")
    n_missing = stats.get("n_missing")
    return {
        "n": n,
        "n_missing": n_missing,
        "min": None,
        "max": None,
        "mean": 0.0 if n else None,
        "std": 1.0 if n else None,
        "median": None,
        "q1": None,
        "q3": None,
    }


def _variable_index_map(card: dict[str, Any]) -> dict[str, str]:
    """Recompute the ``{original_name: var_NNN}`` map from the card's ``variables`` order.

    The card lists variables in the same left-to-right order as the canonical frame's columns, so the
    slot numbering matches :func:`anonymize_variables` without sharing state.
    """
    return {str(var.get("name")): _generic_name(i) for i, var in enumerate(card.get("variables") or [])}


def _mask_variable_assets(assets: list[str], name_map: dict[str, str]) -> list[str]:
    """Rewrite ``assets/variables/<name>.png`` paths so the basename is the opaque ``var_NNN`` slot.

    A variable asset path embeds the original variable name in its filename; left as-is it would leak
    the name an anonymized card must hide. The path is rebuilt with the masked slot name, preserving
    the directory and extension. A path that does not match a known variable is dropped (it could only
    carry an identifying name).
    """
    masked: list[str] = []
    for path in assets or []:
        head, _, basename = path.rpartition("/")
        stem, dot, ext = basename.partition(".")
        generic = name_map.get(stem)
        if generic is not None:
            masked.append(f"{head}/{generic}{dot}{ext}" if head else f"{generic}{dot}{ext}")
    return masked


def anonymize_card(card: dict[str, Any]) -> dict[str, Any]:
    """Return a deep-copied card with all identifying names and free text masked.

    Variable names are replaced by their ``var_NNN`` slot; a NUMERIC variable's stats are replaced by
    the z-scored ones (mean ~ 0, std ~ 1, range-free); identifying free text (identity name/description/
    keywords, every source's human names, provenance contributor/reference method, the titles of origin
    sources and publications, and the free-text governance fields) is masked. The card's ``warnings``
    (top-level, per-source, per-variable) are **emptied**: they routinely quote original variable names
    and authored free text (e.g. ``variable 'Moisture' declared numeric ...``) and would otherwise leak.
    DOIs/years/locators are kept (they are not personal and are needed for the anonymized tier's
    provenance), but their titles are removed. The input card is not mutated. Deterministic; no network.
    """
    out = copy.deepcopy(card)
    name_map = _variable_index_map(out)
    out["warnings"] = []  # warnings quote original variable names / authored free text -> drop wholesale

    identity = out.get("identity")
    if isinstance(identity, dict):
        identity["name"] = identity.get("id")  # the slug id is already opaque; reuse it as the display name
        identity["description"] = _MASK
        identity["keywords"] = []
        identity["domain"] = None  # the domain (e.g. "grapevine", "soil") reveals what the dataset is

    for source in out.get("sources") or []:
        if isinstance(source, dict):
            source["name"] = source.get("source_id")
            source["instrument_name"] = None
            source["warnings"] = []  # per-source warnings may quote authored text

    for var in out.get("variables") or []:
        if not isinstance(var, dict):
            continue
        var.pop("histogram", None)  # the raw-value histogram would leak the real distribution/range
        if "assets" in var:
            var["assets"] = _mask_variable_assets(var.get("assets") or [], name_map)
        original = str(var.get("name"))
        var["name"] = name_map.get(original, original)
        var["unit"] = None
        stats = var.get("stats")
        if var.get("type") == "numeric" and isinstance(stats, dict) and stats:
            var["stats"] = _anonymize_numeric_stats(stats)

    assets = out.get("assets")
    if isinstance(assets, dict) and "variables" in assets:
        assets["variables"] = _mask_variable_assets(assets.get("variables") or [], name_map)

    governance = out.get("governance")
    if isinstance(governance, dict):
        # license + tier are legal/structural facts (kept); the free-text policy fields can name the
        # original owner/source ("Eigenvector page says ...") and are masked.
        for field in ("permitted_use", "access_policy", "redistribution_rights"):
            if governance.get(field) is not None:
                governance[field] = _MASK

    provenance = out.get("provenance")
    if isinstance(provenance, dict):
        provenance["contributor"] = _MASK
        provenance["reference_method"] = None
        provenance["warnings"] = []  # provenance warnings may quote authored free text
        for origin in provenance.get("origin_sources") or []:
            if isinstance(origin, dict):
                origin["title"] = None
        for pub in provenance.get("publications") or []:
            if isinstance(pub, dict):
                pub["title"] = None

    return out


def public_card(card: dict[str, Any], tier: Any) -> dict[str, Any]:
    """The public-safe card for a ``tier``: :func:`anonymize_card` for ``ANONYMIZED``, else unchanged.

    The single chokepoint every reader of ``card.json`` (the CLI ``card``, the catalog, the site) goes
    through, so an anonymized card can never be served raw.
    """
    from nirs4all_datasets.schema import Tier

    return anonymize_card(card) if tier is Tier.ANONYMIZED else card


def public_descriptor(descriptor: DatasetDescriptor) -> DatasetDescriptor:
    """The public-safe descriptor for a dataset's tier.

    For the ``ANONYMIZED`` tier, a copy with every variable name masked to its ``var_NNN`` slot and every
    identifying field removed (name -> opaque id, description/keywords/domain/citation/contributor/origin &
    publication titles/DataCite); other tiers are returned unchanged. The catalog index, the plugin
    accessors, the datasheet/Croissant renderers and Dataverse publication all derive their descriptor
    fields from this, so no path can leak an anonymized identity.
    """
    from nirs4all_datasets.schema import Tier

    if descriptor.tier is not Tier.ANONYMIZED:
        return descriptor
    variables = [v.model_copy(update={"name": _generic_name(i), "unit": None}) for i, v in enumerate(descriptor.variables)]
    provenance = descriptor.provenance.model_copy(update={"contributor": _MASK, "reference_method": None})
    publications = [p.model_copy(update={"title": None}) for p in descriptor.publications]
    # A DOI / origin locator / Dataverse version resolves to the *named* dataset, so for the
    # anonymized tier they are dropped (not just title-masked): the acquisition pointers are
    # re-identifying. Fetching still works from the maintainer's real local descriptor.
    dataverse = descriptor.dataverse.model_copy(update={"doi": None, "dataset_version": None})
    return descriptor.model_copy(
        update={
            "name": descriptor.id,
            "description": _MASK,
            "keywords": [],
            "domain": None,
            "citation": None,
            "variables": variables,
            "provenance": provenance,
            "publications": publications,
            "origin_sources": [],
            "dataverse": dataverse,
            "datacite": None,
        }
    )
