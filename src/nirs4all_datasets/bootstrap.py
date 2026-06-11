"""Author schema-2.0 descriptors from the v2.0 standardized NIRS packages.

Each ``NIRS DB/v2.0/<leaf>/`` is a Frictionless-style package: a machine-readable
``dataset_card.json`` declaring its spectral blocks, targets, metadata fields, splits, license and
origin sources, alongside ``X*.csv`` / ``Y.csv`` / ``M.csv`` (all ``;``-delimited, column 0 =
``observation_id``). :func:`build_descriptor_from_card` maps one such card onto a schema-2.0
:class:`~nirs4all_datasets.schema.DatasetDescriptor`; :func:`bootstrap` sweeps the whole ``v2.0/``
tree idempotently (content-addressed skip, managed-orphan prune, committed reconciliation report).

Boundary: this module only *authors* descriptors (modality / axis-unit / variable-type / license
inference, honest governance defaults) from an already-standardized package. It re-implements no
NIRS/IO logic — the spectral blocks, targets and split facts are read verbatim from the card; the
raw bytes have already been converted upstream by each package's ``source_to_standard.py``.
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import yaml

from nirs4all_datasets.manifest import metadata_hash
from nirs4all_datasets.schema import (
    _OPEN_LICENSES,
    AlignmentLevel,
    AxisUnit,
    DatasetDescriptor,
    Generation,
    Governance,
    IdentitySpec,
    Modality,
    OriginSource,
    Provenance,
    PublicationRef,
    Source,
    SourceAccess,
    SourceKind,
    SourceMode,
    SplitRef,
    Tier,
    Variable,
    VariableRole,
    VarType,
    Versions,
)

GENERATOR = "bootstrap-v2"
GENERATOR_VERSION = "1"

# Id columns that link spectra <-> samples <-> Y/metadata; never authored as a Variable.
_ID_COLUMNS = frozenset({"observation_id", "sample_id", "dataset_id"})

# Data-repository DOI prefixes -> (OriginSource.kind, human repository name). A DOI under one of these
# is where the *bytes* live (-> origin_sources); any other 10.x DOI is a journal paper (-> publications).
_DATA_DOI_PREFIXES: dict[str, tuple[str, str]] = {
    "10.57745": ("dataverse", "Recherche Data Gouv"),
    "10.15454": ("dataverse", "Portail Data INRAE"),
    "10.18710": ("dataverse", "DataverseNO"),
    "10.7910": ("dataverse", "Harvard Dataverse"),
    "10.34725": ("dataverse", "Dataverse"),
    "10.18167": ("dataverse", "CIRAD Dataverse"),
    "10.5281": ("zenodo", "Zenodo"),
    "10.6084": ("figshare", "figshare"),
    "10.5061": ("url", "Dryad"),
}
_DOI_IN_TEXT = re.compile(r"(10\.\d{4,9}/[^\s,;\"'<>]+)")

# Variable names that are categorical/identifier regardless of dtype (an integer-encoded ``*_type`` or
# a numeric ``row_no`` is not a numeric target). Applied to a token-normalized name (camelCase +
# separators -> ``_``); whole-token match so soil props like ``rubidium``/``carbon`` don't false-hit.
_CLF_NAME_RE = re.compile(
    r"(?:^|_)(id|type|class|category|categorical|label|group|species|genus|family|name|code|smiles|inchi|inchikey|formula|variety|cultivar|origin|authenticity|adulteration|material|mineral|subclass|date|datetime|timestamp|row|rowno|unnamed|observation)(?:_|$)",
    re.IGNORECASE,
)
_NA_TOKENS = frozenset({"", "nan", "na", "null", "none", "n/a", "<na>", "."})

# ``spectroscopy_type`` tokens -> Modality. Checked most-specific first; default NIR.
_MODALITY_MAP: tuple[tuple[str, Modality], ...] = (
    ("raman", Modality.RAMAN),
    ("ftir", Modality.MIR),
    ("mir", Modality.MIR),
    ("tir", Modality.TIR),
    ("ecostress", Modality.OTHER),
    ("vswir", Modality.VSWIR),
    ("vis-nir", Modality.NIR),
    ("visnir", Modality.NIR),
    ("uv-vis", Modality.UV_VIS),
    ("uvvis", Modality.UV_VIS),
    ("hyperspectral", Modality.HYPERSPECTRAL),
    ("nir", Modality.NIR),
    ("ir", Modality.MIR),
)

# License names / URLs observed in v2.0 cards -> open SPDX. Substring match on the lower-cased value;
# ND/NC variants are intentionally absent (not open). Only used when public release is allowed.
_OPEN_LICENSE_HINTS: tuple[tuple[str, str], ...] = (
    ("cc0", "CC0-1.0"),
    ("public domain dedication", "PDDL-1.0"),
    ("odc-pddl", "PDDL-1.0"),
    ("attribution share-alike", "CC-BY-SA-4.0"),
    ("cc-by-sa", "CC-BY-SA-4.0"),
    ("by-sa", "CC-BY-SA-4.0"),
    ("open database license", "ODbL-1.0"),
    ("odbl", "ODbL-1.0"),
    ("odc-odbl", "ODbL-1.0"),
    ("attribution license", "ODC-By-1.0"),
    ("odc-by", "ODC-By-1.0"),
    ("cc-by-4.0", "CC-BY-4.0"),
    ("cc-by 4.0", "CC-BY-4.0"),
    ("cc by 4.0", "CC-BY-4.0"),
    ("creative commons attribution", "CC-BY-4.0"),
    ("cc-by", "CC-BY-4.0"),
)


def slugify(text: str) -> str:
    """Lowercase slug matching the descriptor id pattern ``^[a-z0-9]+(_[a-z0-9]+)*$``."""
    slug = re.sub(r"[^a-z0-9]+", "_", str(text).lower()).strip("_")
    return re.sub(r"_+", "_", slug)


def _norm_key(name: str) -> str:
    """Normalize a column name for robust matching (lowercase, drop all non-alphanumerics)."""
    return re.sub(r"[^a-z0-9]", "", str(name).lower())


def _norm_tokens(name: str) -> str:
    """Token form of a name: split camelCase, collapse separators to ``_`` (so ``LeafNumber`` -> ``leaf_number``, ``plant.id`` -> ``plant_id``)."""
    spaced = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", str(name))
    return re.sub(r"[^a-z0-9]+", "_", spaced.lower()).strip("_")


def _is_float(value: str) -> bool:
    try:
        float(value.replace(",", "."))
        return True
    except ValueError:
        return False


def _extract_doi(text: str) -> str | None:
    """Pull a bare DOI out of a ``doi:`` / ``https://doi.org/...`` / raw string; None if absent."""
    match = _DOI_IN_TEXT.search(str(text))
    return match.group(1).rstrip(".") if match else None


def _classify_origin(raw: Any) -> tuple[str, dict[str, Any] | str | None]:
    """Classify an origin candidate (a URL or DOI string).

    Returns ``('source', origin_kwargs)`` for a data home (DOI in a data repo, or a data URL),
    ``('paper', doi)`` for a journal/publisher DOI, ``('manual', text)`` for a non-DOI non-URL note,
    or ``('skip', None)`` when blank. This is what keeps a *paper* DOI out of ``origin_sources``.
    """
    if raw is None:
        return ("skip", None)
    text = str(raw).strip()
    if not text or text.lower() in ("none", "nan", "n/a"):
        return ("skip", None)
    doi = _extract_doi(text)
    if doi:
        prefix = doi.split("/", 1)[0]
        if prefix in _DATA_DOI_PREFIXES:
            kind, repo = _DATA_DOI_PREFIXES[prefix]
            return ("source", {"kind": kind, "mode": "raw", "locator": doi, "access": "open", "title": repo})
        return ("paper", doi)  # any other DOI is a journal/publisher DOI -> publication, not a data source
    if text.lower().startswith("http"):
        host = urlparse(text).netloc.lower()
        if "zenodo.org" in host:
            return ("source", {"kind": "zenodo", "mode": "raw", "locator": text, "access": "open", "title": "Zenodo"})
        if "github.com" in host:
            return ("source", {"kind": "url", "mode": "raw", "locator": text, "access": "open", "title": "GitHub"})
        # registration/click-through portals must be fetched by hand.
        access = "manual" if any(h in host for h in ("esdac.jrc", "eigenvector.com", "ucphchemometrics", "rdrr.io")) else "open"
        return ("source", {"kind": "url", "mode": "raw", "locator": text, "access": access})
    return ("manual", text)


def _dir_fingerprint(path: Path) -> str:
    """Cheap content fingerprint of a leaf dir: sha256 over its sorted ``(name, size)`` files."""
    parts = [f"{p.name}:{p.stat().st_size}" for p in sorted(path.iterdir()) if p.is_file()]
    return hashlib.sha256("\n".join(parts).encode("utf-8")).hexdigest()


def _v2_axis_unit(block: dict[str, Any]) -> AxisUnit:
    """Map one v2.0 spectral block's ``axis_unit`` onto our enum (only nm/cm-1 are representable)."""
    unit = str(block.get("axis_unit") or "").strip().lower()
    if "cm-1" in unit or "wavenumber" in unit:
        return AxisUnit.WAVENUMBER
    if unit in ("nm", "nanometer", "nanometers") or "wavelength (nm)" in unit:
        return AxisUnit.WAVELENGTH
    return AxisUnit.NONE  # micrometers / unknown -> not representable; declared honestly as none


def _v2_modality(spectroscopy_type: Any) -> Modality:
    """Map a card ``spectroscopy_type`` (e.g. ``"NIR/VIS-NIR"``, ``"Raman"``) onto a :class:`Modality` (default NIR)."""
    low = str(spectroscopy_type or "").lower()
    for token, modality in _MODALITY_MAP:
        if token in low:
            return modality
    return Modality.NIR


def _to_float(value: Any) -> float | None:
    """Parse a card axis bound (often a numeric string like ``"1100"``) to float; None if absent/garbage."""
    if value is None:
        return None
    try:
        return float(str(value).replace(",", "."))
    except ValueError:
        return None


def _v2_numeric_columns(y_path: Path, sample_rows: int = 80) -> dict[str, bool]:
    """Per-column numeric-ness of a v2.0 ``Y.csv`` (header + a sample), to type a target without an
    explicit ``target_types`` entry: mostly-numeric -> numeric, else categorical. Keyed by ``_norm_key``."""
    if not y_path.exists():
        return {}
    lines = [ln for ln in y_path.read_text(encoding="utf-8", errors="replace").splitlines() if ln.strip()][: sample_rows + 1]
    if len(lines) < 2:
        return {}
    delim = ";" if lines[0].count(";") >= lines[0].count(",") else ","
    headers = [h.strip().strip('"').strip("'") for h in lines[0].split(delim)]
    numeric: dict[str, bool] = {}
    for i, header in enumerate(headers):
        vals = [row.split(delim)[i].strip().strip('"').strip("'") for row in lines[1:] if i < len(row.split(delim))]
        nonempty = [v for v in vals if v.lower() not in _NA_TOKENS]
        if not nonempty:
            numeric[_norm_key(header)] = True  # no evidence -> default numeric
            continue
        ok = sum(1 for v in nonempty if _is_float(v))
        numeric[_norm_key(header)] = ok >= 0.8 * len(nonempty)
    return numeric


def find_v2_leaves(source_root: str | Path) -> list[Path]:
    """v2.0 standardized leaves: dirs under ``v2.0/`` holding a ``dataset_card.json`` + ``Y.csv``.

    Each is a Frictionless-style package (machine-readable card declaring targets/sources/license), so
    the descriptor is authored from the card -- no free-text guessing.
    """
    base = Path(source_root) / "v2.0"
    if not base.is_dir():
        return []
    return sorted(d for d in base.iterdir() if d.is_dir() and (d / "dataset_card.json").exists() and (d / "Y.csv").exists())


def _csv_header(path: Path) -> list[str]:
    """First (``;``-preferred) header row of a v2.0 CSV; ``[]`` if missing/empty."""
    if not path.exists() or path.stat().st_size == 0:
        return []
    try:
        line = path.open("r", encoding="utf-8", errors="replace").readline().strip()
    except OSError:
        return []
    if not line:
        return []
    delim = ";" if line.count(";") >= line.count(",") else ","
    return [h.strip().strip('"').strip("'") for h in line.split(delim)]


def _open_spdx(card: dict[str, Any]) -> str | None:
    """Best-effort open SPDX id for a card's license (name or URL); ``None`` if not an open license."""
    lic = card.get("license_summary") or {}
    rights = card.get("rights") or {}
    haystack = " ".join(
        str(v).lower()
        for v in (
            lic.get("license_name"),
            lic.get("license"),
            lic.get("spdx"),
            lic.get("license_url"),
            rights.get("license_name"),
            rights.get("license"),
            rights.get("spdx"),
            rights.get("license_url"),
        )
        if v
    )
    if not haystack.strip():
        return None
    for token, spdx in _OPEN_LICENSE_HINTS:
        if token in haystack:
            return spdx if spdx in _OPEN_LICENSES else None
    return None


def _build_sources(card: dict[str, Any], warnings: list[str]) -> list[Source]:
    """One :class:`Source` per ``spectral_blocks[]`` entry; fall back to a single ``X`` source + warn."""
    blocks = card.get("spectral_blocks") or []
    sources: list[Source] = []
    for block in blocks:
        block_id = str(block.get("block_id") or "X").strip() or "X"
        n_rows = block.get("n_rows")
        n_vars = block.get("n_spectral_variables")
        sources.append(
            Source(
                source_id=block_id,
                name=str(block.get("block_name")) if block.get("block_name") else None,
                instrument_name=str(block.get("instrument_name")) if block.get("instrument_name") else None,
                modality=_v2_modality(block.get("spectroscopy_type") or card.get("spectral_data_summary", {}).get("spectroscopy_type")),
                axis_unit=_v2_axis_unit(block),
                axis_min=_to_float(block.get("axis_min")),
                axis_max=_to_float(block.get("axis_max")),
                axis_resolution=_to_float(block.get("axis_resolution")),
                n_observations=int(n_rows) if isinstance(n_rows, (int, float)) else None,
                n_variables=int(n_vars) if isinstance(n_vars, (int, float)) else None,
            )
        )
    if not sources:
        warnings.append("dataset_card.json declares no spectral_blocks; single 'X' source assumed")
        sources.append(Source(source_id="X", modality=_v2_modality(card.get("spectral_data_summary", {}).get("spectroscopy_type"))))
    return sources


def _build_variables(card: dict[str, Any], leaf_dir: Path) -> list[Variable]:
    """Targets (``target_summary``) + metadata (``metadata_fields_summary``), id columns excluded, deduped.

    Targets are typed from ``target_types`` (numeric/categorical), overridden to CATEGORICAL for an
    identifier-looking name, and otherwise inferred from the ``Y.csv`` dtype (default NUMERIC). Metadata
    columns carry no type evidence beyond their name, so they default to NUMERIC (the card does not
    profile them; the qualify stage refines per-variable dataviz later).
    """
    tsum = card.get("target_summary") or {}
    target_vars = [str(v) for v in (tsum.get("target_variables") or [])]
    target_types = {str(k): str(v).lower() for k, v in (tsum.get("target_types") or {}).items()}
    y_numeric = _v2_numeric_columns(leaf_dir / "Y.csv")

    def _vartype(name: str) -> VarType:
        if _CLF_NAME_RE.search(_norm_tokens(name)):
            return VarType.CATEGORICAL
        kind = target_types.get(name, "")
        if kind.startswith("regress") or kind.startswith("numeric"):
            return VarType.NUMERIC
        if kind and ("class" in kind or "label" in kind or "categor" in kind or "identifier" in kind):
            return VarType.CATEGORICAL
        # No explicit type (or ``regression_or_label``): infer from the Y column dtype, defaulting to
        # NUMERIC (the NIRS norm) -- never blanket-categorical.
        return VarType.CATEGORICAL if y_numeric.get(_norm_key(name)) is False else VarType.NUMERIC

    variables: list[Variable] = []
    seen: set[str] = set()
    for name in target_vars:
        if name in _ID_COLUMNS or name in seen:
            continue
        seen.add(name)
        variables.append(Variable(name=name, role=VariableRole.TARGET, type=_vartype(name)))

    m_fields = [str(f) for f in ((card.get("metadata_fields_summary") or {}).get("m_fields") or [])]
    for name in m_fields:
        if name in _ID_COLUMNS or name in seen:
            continue
        seen.add(name)
        vtype = VarType.CATEGORICAL if _CLF_NAME_RE.search(_norm_tokens(name)) else VarType.NUMERIC
        variables.append(Variable(name=name, role=VariableRole.METADATA, type=vtype))
    return variables


def _harvest_origins(card: dict[str, Any], leaf_dir: Path, warnings: list[str]) -> tuple[list[OriginSource], list[PublicationRef]]:
    """Collect origin sources (data homes) and publications (journal DOIs) declared by the card.

    Origins come from ``detected_sources[].url``, ``source_summary.source_url`` and the ``official_source``
    url/doi lists; the maintainer ``source_to_standard.py`` is added as a SCRIPT origin when present.
    Local filesystem paths (e.g. ``D:\\...``) are ignored. Publication DOIs come from
    ``associated_publications[].doi`` (``' | '``-split for multi-DOI strings) plus any journal DOI a
    harvested URL resolves to.
    """
    origins: list[OriginSource] = []
    publications: list[PublicationRef] = []
    seen_loc: set[str] = set()
    seen_doi: set[str] = set()

    candidates: list[Any] = [e.get("url") for e in (card.get("detected_sources") or []) if isinstance(e, dict) and e.get("url")]
    candidates.append((card.get("source_summary") or {}).get("source_url"))
    official = card.get("official_source") or {}
    for key in ("download_urls", "landing_urls", "urls", "doi", "download_page", "landing_page", "source_page", "url"):
        value = official.get(key)
        candidates.extend(value if isinstance(value, list) else [value])

    for raw_url in candidates:
        if not raw_url or not (str(raw_url).startswith("http") or _extract_doi(str(raw_url))):
            continue  # skip blanks + local filesystem paths
        kind, payload = _classify_origin(raw_url)
        if kind == "source" and isinstance(payload, dict) and payload["locator"] not in seen_loc:
            seen_loc.add(payload["locator"])
            try:
                origins.append(OriginSource(**payload))
            except Exception as exc:  # noqa: BLE001 - a malformed url must not abort the leaf
                warnings.append(f"unparseable origin source {raw_url!r}: {exc}")
        elif kind == "paper" and isinstance(payload, str) and payload not in seen_doi:
            seen_doi.add(payload)
            publications.append(PublicationRef(doi=payload))

    for pub in card.get("associated_publications") or []:
        if not isinstance(pub, dict):
            continue
        title = str(pub.get("title")) if pub.get("title") else None
        for piece in str(pub.get("doi") or "").split("|"):
            doi = _extract_doi(piece)
            if not doi:
                continue
            # A DOI in associated_publications under a data-repository prefix (figshare/zenodo/dataverse)
            # is where the *bytes* live, not a journal paper -> route it to origin_sources; only a true
            # journal/publisher DOI becomes a publication. This also prevents listing a data DOI twice.
            kind, payload = _classify_origin(doi)
            if kind == "source" and isinstance(payload, dict) and payload["locator"] not in seen_loc:
                seen_loc.add(payload["locator"])
                try:
                    origins.append(OriginSource(**payload))
                except Exception as exc:  # noqa: BLE001 - a malformed DOI must not abort the leaf
                    warnings.append(f"unparseable origin source {doi!r}: {exc}")
            elif kind == "paper" and doi not in seen_doi:
                seen_doi.add(doi)
                publications.append(PublicationRef(doi=doi, title=title))

    if (leaf_dir / "source_to_standard.py").exists():
        origins.append(OriginSource(kind=SourceKind.SCRIPT, mode=SourceMode.RAW, locator="source_to_standard.py", access=SourceAccess.MANUAL, title="standardization script (maintainer-only)"))
    return origins, publications


def _public_release_allowed(card: dict[str, Any]) -> bool:
    """Whether the card permits public redistribution (``license_summary`` or ``rights`` block)."""
    lic = card.get("license_summary") or {}
    rights = card.get("rights") or {}
    return bool(lic.get("public_release_allowed", rights.get("public_release_allowed", False)))


def _build_governance(card: dict[str, Any], source_name: str, license_spdx: str | None, public_ok: bool) -> Governance:
    """Honest governance: open SPDX if cleared+known, else ``LicenseRef-not-cleared``; consent/anonymization unassessed."""
    lic = card.get("license_summary") or {}
    rights = card.get("rights") or {}
    rights_notes = lic.get("rights_notes") or rights.get("rights_notes") or lic.get("notes") or rights.get("notes")
    license_id = license_spdx if (public_ok and license_spdx) else "LicenseRef-not-cleared"
    return Governance(
        license=license_id,
        owner_steward=source_name,
        redistribution_rights=str(rights_notes) if rights_notes else ("Open redistribution permitted by the source license." if license_id in _OPEN_LICENSES else "Redistribution not cleared; verify source terms before release."),
        consent_ethics_status="Not assessed (auto-generated from v2.0 package; verify before release).",
        anonymization_status="Not assessed (auto-generated from v2.0 package; verify before release).",
        permitted_use="Research and benchmarking." if public_ok else "Research and benchmarking; private use only.",
        access_policy="Open per source license." if license_id in _OPEN_LICENSES else "Manual download / private-use-only per source.",
    )


def build_descriptor_from_card(leaf_dir: Path) -> tuple[DatasetDescriptor, list[str]]:
    """Author a schema-2.0 descriptor for one v2.0 package from its authoritative ``dataset_card.json``.

    Maps the card's spectral blocks -> :class:`Source` list, targets+metadata -> :class:`Variable`
    list (id columns excluded), alignment level / sample-id availability / native split, license +
    governance, and origin sources + publications. No NIRS/IO logic is re-implemented; the conversion
    has already happened upstream.
    """
    warnings: list[str] = []
    card = json.loads((leaf_dir / "dataset_card.json").read_text(encoding="utf-8"))
    did = slugify(card.get("dataset_id") or leaf_dir.name)

    sources = _build_sources(card, warnings)
    variables = _build_variables(card, leaf_dir)

    org = card.get("spectral_organization") or {}
    raw_level = str(org.get("alignment_level") or "observation").strip().lower()
    alignment_level = AlignmentLevel.SAMPLE if raw_level == "sample" else AlignmentLevel.OBSERVATION

    m_header = _csv_header(leaf_dir / "M.csv")
    sample_id_available = "sample_id" in m_header
    ids = IdentitySpec(sample_id_available=sample_id_available)

    split_summary = card.get("split_summary") or {}
    splits: list[SplitRef] = []
    if split_summary.get("original_split_available"):
        splits = [SplitRef(name="original", kind="train_test", applied=False, documented_origin=str(split_summary.get("notes")) if split_summary.get("notes") else None)]

    public_ok = _public_release_allowed(card)
    license_spdx = _open_spdx(card)
    tier = Tier.PUBLIC if (public_ok and license_spdx is not None) else Tier.PRIVATE

    source_name = str((card.get("source_summary") or {}).get("source_name") or "NIRS DB v2.0 collection")
    governance = _build_governance(card, source_name, license_spdx, public_ok)
    origins, publications = _harvest_origins(card, leaf_dir, warnings)

    repro = card.get("reproducibility_assessment") or {}
    reproducibility = {str(k): str(v) for k, v in repro.items() if v is not None}

    n_targets = sum(1 for v in variables if v.role is VariableRole.TARGET)
    family = slugify(did.split("_")[0]) or None
    dataset_name = str(card.get("dataset_name") or leaf_dir.name)

    descriptor = DatasetDescriptor(
        id=did,
        name=dataset_name,
        description=f"{dataset_name}. v2.0 standardized NIRS package: {len(sources)} spectral source(s), {n_targets} declared target(s). Auto-generated from dataset_card.json (verify before publication).",
        domain=family,
        keywords=[k for k in ["nir", "v2", family] if k],
        citation=f"https://doi.org/{publications[0].doi}" if publications and publications[0].doi else None,
        sources=sources,
        variables=variables,
        ids=ids,
        alignment_level=alignment_level,
        splits=splits,
        tier=tier,
        versions=Versions(),
        provenance=Provenance(contributor=source_name, ingest_reader="v2.0-standardized", warnings=warnings),
        governance=governance,
        origin_sources=origins,
        publications=publications,
        reproducibility=reproducibility,
        generation=Generation(
            managed=True,
            generator=GENERATOR,
            generator_version=GENERATOR_VERSION,
            source_relpath=f"v2.0/{leaf_dir.name}",
            source_fingerprint=_dir_fingerprint(leaf_dir),
        ),
    )
    return descriptor, warnings


def _write_descriptor(descriptor: DatasetDescriptor, path: Path) -> None:
    """Write a descriptor as clean YAML with an auto-generated banner."""
    data = descriptor.model_dump(mode="json", exclude_none=True)
    banner = "# AUTO-GENERATED by nirs4all-datasets `bootstrap`. Edit freely; set generation.managed: false to protect from regeneration.\n"
    path.write_text(banner + yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")


def bootstrap(source_root: str | Path, catalog_root: str | Path, *, force: bool = False, prune: bool = False) -> dict[str, Any]:
    """Generate/refresh schema-2.0 descriptors for every v2.0 leaf under ``source_root``.

    Idempotent: a human-edited descriptor (``generation.managed`` false/absent) is never overwritten
    without ``force``; a managed one is rewritten only when ``force`` or its ``metadata_hash`` changed.

    Reconciliation (``new replaces old``): a *managed* descriptor whose id the source no longer
    produces is an orphan. With ``prune`` it (and its ``datasets/<id>`` dir) is deleted; human-authored
    orphans are always kept and only flagged. A committed ``catalog/reconciliation.json`` records the
    full add/update/remove diff. Returns ``{created, updated, skipped, errors, ids, removed,
    kept_human_orphans, pruned}``.
    """
    out_dir = Path(catalog_root) / "catalog" / "datasets"
    out_dir.mkdir(parents=True, exist_ok=True)

    report: dict[str, Any] = {"created": [], "updated": [], "skipped": [], "errors": [], "ids": {}}

    items: list[tuple[DatasetDescriptor, list[str], str]] = []
    for leaf_dir in find_v2_leaves(source_root):
        rel = f"v2.0/{leaf_dir.name}"
        try:
            descriptor, warns = build_descriptor_from_card(leaf_dir)
            items.append((descriptor, warns, rel))
        except Exception as exc:  # noqa: BLE001 - one bad package must not abort the sweep
            report["errors"].append({"leaf": rel, "error": f"{type(exc).__name__}: {exc}"})

    seen_ids: dict[str, str] = {}
    for descriptor, warns, source_relpath in items:
        did = descriptor.id
        if did in seen_ids:
            report["errors"].append({"leaf": source_relpath, "error": f"id collision {did!r} (kept {seen_ids[did]})"})
            continue
        seen_ids[did] = source_relpath
        report["ids"][did] = source_relpath

        path = out_dir / f"{did}.yaml"
        if path.exists():
            try:
                old = DatasetDescriptor(**(yaml.safe_load(path.read_text(encoding="utf-8")) or {}))
            except Exception:  # noqa: BLE001 - unreadable existing descriptor: leave it for a human
                report["skipped"].append({"id": did, "reason": "existing descriptor unreadable"})
                continue
            if not (old.generation and old.generation.managed) and not force:
                report["skipped"].append({"id": did, "reason": "human-managed (generation.managed not set)"})
                continue
            if not force and metadata_hash(old) == metadata_hash(descriptor):
                report["skipped"].append({"id": did, "reason": "unchanged"})
                continue
            _write_descriptor(descriptor, path)
            report["updated"].append({"id": did, "warnings": warns})
        else:
            _write_descriptor(descriptor, path)
            report["created"].append({"id": did, "warnings": warns})

    # Reconciliation: prune managed orphans (descriptors the source no longer produces); never touch a
    # human-authored descriptor (only flag it). Always write a committed reconciliation report.
    new_ids = set(report["ids"])
    removed: list[str] = []
    kept_human: list[str] = []
    for path in sorted(out_dir.glob("*.yaml")):
        did = path.stem
        if did in new_ids:
            continue
        try:
            old = DatasetDescriptor(**(yaml.safe_load(path.read_text(encoding="utf-8")) or {}))
        except Exception:  # noqa: BLE001 - unreadable: leave it for a human
            continue
        if old.generation and old.generation.managed:
            removed.append(did)
            if prune:
                path.unlink()
                data_dir = Path(catalog_root) / "datasets" / did
                if data_dir.exists():
                    shutil.rmtree(data_dir)  # drop the orphan's tracked card/manifest + any local bytes
        else:
            kept_human.append(did)
    report["removed"] = sorted(removed)
    report["kept_human_orphans"] = sorted(kept_human)
    report["pruned"] = bool(prune)

    recon = {
        "source_root": str(source_root),
        "n_datasets": len(new_ids),
        "created": sorted(c["id"] for c in report["created"]),
        "updated": sorted(u["id"] for u in report["updated"]),
        "skipped": report["skipped"],
        "removed_managed_orphans": report["removed"],
        "pruned": bool(prune),
        "kept_human_orphans": report["kept_human_orphans"],
        "id_collisions": [e for e in report["errors"] if "collision" in e["error"]],
        "errors": [e for e in report["errors"] if "collision" not in e["error"]],
    }
    (Path(catalog_root) / "catalog" / "reconciliation.json").write_text(json.dumps(recon, indent=2, sort_keys=True), encoding="utf-8")
    return report
