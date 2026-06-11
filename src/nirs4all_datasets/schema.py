"""Pydantic models for dataset descriptors, manifests, and subsets (schema 2.0).

A **dataset** is the *raw measured reality*, first-class — not a benchmark task. It carries:

* 1..n **X sources** (:class:`Source`) kept separate, possibly of different sizes (asymmetric
  spectral repetitions); aligned by **sample identity** (:class:`IdentitySpec`), never by row position;
* 0..n **variables** (:class:`Variable`) — Y *and* metadata are the same kind of thing (every metadata
  column is a potential target). A dataset may declare no target at all (X-only / metadata-only);
* native **splits/folds** (:class:`SplitRef`) — documented, never auto-applied;
* a visibility **tier** (:class:`Tier`), provenance, origin sources, publications, and two version axes.

Two separate concerns are preserved from the prior schema:

* **Schema validity** (every field well-formed) — model validators + ``catalog/scripts/validate.py``.
* **Publishability** (safe to release openly) — :meth:`DatasetDescriptor.publication_blockers`. Private
  and anonymized tiers are *valid* in the catalog; they are simply token-gated, never published openly.

The acquisition vocabulary (``SourceKind``/``SourceMode``/``SourceAccess``/``VariableRole``/``VarType``/
``Tier``) is this package's OWN domain. ``AxisUnit``/``SignalType``/``Modality`` mirror nirs4all's
vocabulary by value (kept import-light); ``tests/test_schema.py`` guards against drift.
"""
from __future__ import annotations

import re
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

SCHEMA_VERSION = "2.0"

# Slug / semver / DOI / hash patterns.
_ID_RE = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+)*$")
_SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")
# Opaque DOI suffix (prefix differs: RDG 10.70112/10.57745, CIRAD 10.18167/...).
_DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
# A single SPDX licence token (broad syntactic check, not the full SPDX list).
_SPDX_TOKEN_RE = re.compile(r"^[A-Za-z0-9.+-]+$")
_SPDX_OPERATORS = frozenset({"AND", "OR", "WITH"})

# Open licences acceptable for *public* release (Open Definition compatible).
# NC/ND variants are intentionally excluded (not open data).
_OPEN_LICENSES = frozenset(
    {
        "CC0-1.0", "CC-BY-4.0", "CC-BY-SA-4.0",
        "ODbL-1.0", "ODC-By-1.0", "PDDL-1.0",
        "etalab-2.0",
        "MIT", "BSD-3-Clause", "Apache-2.0", "CeCILL-2.1",
    }
)


def _is_blank(value: str | None) -> bool:
    """Whether a string is missing or whitespace-only."""
    return value is None or not value.strip()


def _validate_license_syntax(value: str) -> str:
    """Accept ``proprietary``, ``LicenseRef-*``, or an SPDX-expression-shaped string."""
    stripped = value.strip()
    if not stripped:
        raise ValueError("license must be non-empty.")
    if stripped == "proprietary" or stripped.startswith("LicenseRef-"):
        return stripped
    for token in stripped.split():
        if token in _SPDX_OPERATORS:
            continue
        bare = token.strip("()")
        if not bare or not _SPDX_TOKEN_RE.match(bare):
            raise ValueError(f"license {value!r} is not a valid SPDX id/expression, 'LicenseRef-<name>', or 'proprietary'.")
    return stripped


def _normalize_doi(value: str | None) -> str | None:
    """Strip a ``doi:``/``https://doi.org/...`` prefix; validate the bare ``10.x/y`` form."""
    if value is None:
        return None
    text = value.strip()
    for prefix in ("https://doi.org/", "http://doi.org/", "https://dx.doi.org/", "http://dx.doi.org/", "doi:"):
        if text.lower().startswith(prefix):
            text = text[len(prefix):].strip()
            break
    if not _DOI_RE.match(text):
        raise ValueError(f"invalid DOI {value!r} (expected '10.<prefix>/<suffix>').")
    return text


# =============================================================================
# Enums
# =============================================================================
# --- mirror nirs4all.data.schema.config (guarded by tests) ---------------------------------------
class AxisUnit(StrEnum):
    """Spectral axis unit (mirrors ``nirs4all`` ``HeaderUnit``)."""

    WAVENUMBER = "cm-1"
    WAVELENGTH = "nm"
    NONE = "none"
    TEXT = "text"
    INDEX = "index"


class SignalType(StrEnum):
    """Signal type (mirrors ``nirs4all`` ``SignalTypeEnum``)."""

    AUTO = "auto"
    ABSORBANCE = "absorbance"
    REFLECTANCE = "reflectance"
    REFLECTANCE_PERCENT = "reflectance%"
    TRANSMITTANCE = "transmittance"
    TRANSMITTANCE_PERCENT = "transmittance%"
    LOG_1_R = "log(1/R)"
    KUBELKA_MUNK = "kubelka-munk"


class Modality(StrEnum):
    """Spectroscopic modality."""

    NIR = "NIR"
    MIR = "MIR"
    RAMAN = "Raman"
    UV_VIS = "UV-Vis"
    VSWIR = "VSWIR"
    TIR = "TIR"
    HYPERSPECTRAL = "hyperspectral"
    OTHER = "other"


# --- this package's own domain --------------------------------------------------------------------
class Tier(StrEnum):
    """Visibility / access tier (replaces the prior visibility + confidentiality split)."""

    PUBLIC = "public"  # everything shown + exportable by all (from the origin)
    PRIVATE = "private"  # everything shown; export requires a token (Dataverse)
    ANONYMIZED = "anonymized"  # metadata names masked + Y normalized; export requires a token


class VariableRole(StrEnum):
    """Role of a non-spectral column. There is no intrinsic Y/metadata distinction; a metadata
    column is a *potential* target. ``target`` is set only when the source explicitly declares it."""

    TARGET = "target"
    METADATA = "metadata"


class VarType(StrEnum):
    """Statistical type of a variable (drives the card's per-variable dataviz)."""

    NUMERIC = "numeric"
    CATEGORICAL = "categorical"
    TEXT = "text"
    IDENTIFIER = "identifier"
    DATETIME = "datetime"


class AlignmentLevel(StrEnum):
    """How a source's spectra align to samples / to other sources."""

    OBSERVATION = "observation"  # one spectrum per sample, sources share the observation order
    SAMPLE = "sample"  # spectra group under sample_id; sources may differ in size (asymmetric reps)


class ConversionStatus(StrEnum):
    """Outcome of raw->canonical conversion."""

    OK = "ok"
    PARTIAL = "partial"
    FAILED = "failed"


class FileRole(StrEnum):
    """Role of a stored file in a dataset."""

    RAW = "raw"
    CANONICAL = "canonical"


class SourceKind(StrEnum):
    """Where a dataset's original (authoritative) bytes live."""

    DATAVERSE = "dataverse"  # any Dataverse instance (data-gouv, CIRAD, Harvard, INRAE...)
    ZENODO = "zenodo"
    FIGSHARE = "figshare"
    URL = "url"  # direct file(s) over http(s)
    SCRIPT = "script"  # reproducible acquisition script (maintainer-side only; never run on consumer get)
    MANUAL = "manual"  # licence requires a manual download; we only document + checksum


class SourceMode(StrEnum):
    """What an origin source yields.

    ``canonical`` = the full canonical set, verifiable byte-for-byte against the manifest. ``raw`` =
    original vendor files re-ingested locally (the re-ingested canonical is a *reproduction*).
    """

    CANONICAL = "canonical"
    RAW = "raw"


class SourceAccess(StrEnum):
    """How an origin source is reached."""

    OPEN = "open"  # public, no credential
    TOKEN = "token"  # needs a host-scoped credential (referenced by name, never stored here)
    MANUAL = "manual"  # human must fetch it (click-through licence, registration...)


def _validate_schema_version(value: str) -> str:
    if value != SCHEMA_VERSION:
        raise ValueError(f"unsupported schema_version {value!r} (expected {SCHEMA_VERSION!r}).")
    return value


# =============================================================================
# Descriptor sub-models
# =============================================================================
class Source(BaseModel):
    """One X source = one instrument / acquisition, kept separate. Sources may differ in size
    (asymmetric repetitions); they are linked by sample identity, never by row position."""

    model_config = ConfigDict(extra="forbid")

    source_id: str  # "X", "X1", ... (matches the canonical parquet + the spectral block)
    name: str | None = None
    vendor: str | None = None
    instrument_name: str | None = None
    modality: Modality = Modality.NIR
    axis_unit: AxisUnit = AxisUnit.NONE
    axis_min: float | None = None
    axis_max: float | None = None
    axis_resolution: float | None = None
    signal_type: SignalType = SignalType.AUTO
    n_observations: int | None = Field(default=None, ge=0)
    n_variables: int | None = Field(default=None, ge=0)

    @field_validator("source_id")
    @classmethod
    def _check_source_id(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Source.source_id must be non-empty.")
        return value.strip()


class Variable(BaseModel):
    """A non-spectral column (a target OR a metadata column — the same kind of thing). Carries no
    task_type: the supervised task is a *consumer* choice (pick a variable + a split), not a property
    of the dataset."""

    model_config = ConfigDict(extra="forbid")

    name: str
    role: VariableRole = VariableRole.METADATA
    type: VarType = VarType.NUMERIC
    unit: str | None = None
    classes: list[str] | None = None  # ordered class names for a categorical variable


class SplitRef(BaseModel):
    """A native split/fold, *documented but never auto-applied*. ``applied`` is always False here."""

    model_config = ConfigDict(extra="forbid")

    name: str
    kind: str = "train_test"  # train_test | kfold | group | custom
    path: str | None = None  # canonical/splits/<name>.parquet (sample_id -> partition [+ fold])
    n_folds: int | None = Field(default=None, ge=1)
    documented_origin: str | None = None
    applied: bool = False


class Versions(BaseModel):
    """Two independent version axes (see DESIGN §5)."""

    model_config = ConfigDict(extra="forbid")

    content: str = "1.0.0"  # bumps when the dataset bytes change (semver)
    schema_protocol: str = SCHEMA_VERSION  # bumps when the metric/schema protocol evolves (re-qualify, not rebuild)

    @field_validator("content")
    @classmethod
    def _check_content(cls, value: str) -> str:
        if not _SEMVER_RE.match(value):
            raise ValueError(f"versions.content {value!r} must be semantic (e.g. '1.0.0').")
        return value


class IdentitySpec(BaseModel):
    """The id columns that link spectra <-> samples <-> Y/metadata. ``observation_id`` is per-spectrum;
    ``sample_id`` is the physical sample (groups repetitions). When ``sample_id`` is unavailable, each
    observation is its own sample group."""

    model_config = ConfigDict(extra="forbid")

    observation_id: str = "observation_id"
    sample_id: str = "sample_id"
    sample_id_available: bool = True


class Provenance(BaseModel):
    """Where the data came from and how it was converted."""

    model_config = ConfigDict(extra="forbid")

    contributor: str
    collection_date: str | None = None
    reference_method: str | None = None
    lab_protocol: str | None = None
    raw_sha256: list[str] = Field(default_factory=list)
    ingest_reader: str | None = None
    ingest_reader_version: str | None = None
    conversion_status: ConversionStatus | None = None
    warnings: list[str] = Field(default_factory=list)
    known_exclusions: str | None = None


class Author(BaseModel):
    """A dataset author for DataCite/Dataverse metadata."""

    model_config = ConfigDict(extra="forbid")

    name: str
    orcid: str | None = None
    affiliation: str | None = None
    ror: str | None = None


class Funding(BaseModel):
    """Funding information for DataCite metadata."""

    model_config = ConfigDict(extra="forbid")

    funder: str
    award_number: str | None = None
    award_title: str | None = None


class PublicationRef(BaseModel):
    """A related publication (the *paper*), for citation. ``doi`` is a journal/publisher DOI — distinct
    from a data-repository DOI, which is an :class:`OriginSource` (where the *bytes* live)."""

    model_config = ConfigDict(extra="forbid")

    doi: str | None = None
    title: str | None = None
    authors: list[str] = Field(default_factory=list)
    year: int | None = None
    citation: str | None = None  # free-text or a resolved CSL/APA string
    bibtex: str | None = None

    @field_validator("doi")
    @classmethod
    def _norm_doi(cls, value: str | None) -> str | None:
        return _normalize_doi(value)


class DataCite(BaseModel):
    """Rich metadata mapped onto native Dataverse/DataCite fields at publish."""

    model_config = ConfigDict(extra="forbid")

    authors: list[Author] = Field(default_factory=list)
    funding: list[Funding] = Field(default_factory=list)
    related_publications: list[PublicationRef] = Field(default_factory=list)
    related_software: list[str] = Field(default_factory=list)


class Governance(BaseModel):
    """Legal/ethical metadata. Public release is gated on these fields (see publication_blockers)."""

    model_config = ConfigDict(extra="forbid")

    license: str
    owner_steward: str | None = None
    redistribution_rights: str | None = None
    consent_ethics_status: str | None = None
    anonymization_status: str | None = None
    permitted_use: str | None = None
    access_policy: str | None = None

    @field_validator("license")
    @classmethod
    def _check_license_syntax(cls, value: str) -> str:
        return _validate_license_syntax(value)


class DataverseRef(BaseModel):
    """Pointer to the dataset's (future) personal Dataverse location and pinned version — the
    token-gated fallback for private/anonymized data and for origins that have rotted."""

    model_config = ConfigDict(extra="forbid")

    instance: str = "https://entrepot.recherche.data.gouv.fr"
    doi: str | None = None
    dataset_version: str | None = None

    @field_validator("doi")
    @classmethod
    def _norm_doi(cls, value: str | None) -> str | None:
        return _normalize_doi(value)


class OriginSource(BaseModel):
    """An original (authoritative) home of a dataset's bytes — where to fetch from, never checksums
    (the manifest is the single byte-identity authority). Excluded from the processing hash."""

    model_config = ConfigDict(extra="forbid")

    kind: SourceKind
    mode: SourceMode = SourceMode.RAW
    locator: str  # version-pinned DOI ('10.x/y'), URL, or 'scripts/<id>.py'
    access: SourceAccess = SourceAccess.OPEN
    credential_ref: str | None = None  # NAME of a host-scoped secret; never the secret value
    license: str | None = None  # SPDX of the source, if it differs from governance.license
    title: str | None = None
    expected_files: list[str] = Field(default_factory=list)  # basenames to fetch (no checksums here)
    last_checked: str | None = None  # ISO timestamp of the last health-check
    alive: bool | None = None  # last health-check result
    notes: str | None = None

    @field_validator("locator")
    @classmethod
    def _check_locator(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("OriginSource.locator must be non-empty.")
        return value.strip()

    @field_validator("license")
    @classmethod
    def _check_license(cls, value: str | None) -> str | None:
        return _validate_license_syntax(value) if value is not None else None

    @model_validator(mode="after")
    def _check_access(self) -> OriginSource:
        if self.access is SourceAccess.TOKEN and self.kind is not SourceKind.DATAVERSE and self.credential_ref is None:
            raise ValueError("token access to a non-Dataverse source requires a credential_ref (host-scoped secret name).")
        return self


class Generation(BaseModel):
    """Provenance for a machine-generated descriptor (bulk bootstrap). Present only on auto-generated
    descriptors; excluded from the processing hash so refreshing it never triggers a rebuild."""

    model_config = ConfigDict(extra="forbid")

    managed: bool = False
    generator: str | None = None
    generator_version: str | None = None
    source_relpath: str | None = None
    source_fingerprint: str | None = None


# =============================================================================
# Descriptor
# =============================================================================
class DatasetDescriptor(BaseModel):
    """Descriptor for one RAW NIRS dataset (``catalog/datasets/<id>.yaml``)."""

    model_config = ConfigDict(extra="forbid")

    schema_version: str = SCHEMA_VERSION
    id: str
    name: str
    description: str
    domain: str | None = None
    keywords: list[str] = Field(default_factory=list)
    citation: str | None = None

    sources: list[Source] = Field(min_length=1)
    variables: list[Variable] = Field(default_factory=list)  # may be empty (X-only datasets are valid)
    ids: IdentitySpec = Field(default_factory=IdentitySpec)
    alignment_level: AlignmentLevel = AlignmentLevel.OBSERVATION
    splits: list[SplitRef] = Field(default_factory=list)

    tier: Tier = Tier.PRIVATE
    versions: Versions = Field(default_factory=Versions)

    provenance: Provenance
    governance: Governance
    origin_sources: list[OriginSource] = Field(default_factory=list)  # where the bytes live; excl. from processing hash
    publications: list[PublicationRef] = Field(default_factory=list)
    datacite: DataCite | None = None
    dataverse: DataverseRef = Field(default_factory=DataverseRef)
    reproducibility: dict[str, str] = Field(default_factory=dict)
    generation: Generation | None = None  # set on auto-generated descriptors; excluded from processing hash

    @field_validator("schema_version")
    @classmethod
    def _check_schema_version(cls, value: str) -> str:
        return _validate_schema_version(value)

    @field_validator("id")
    @classmethod
    def _validate_id(cls, value: str) -> str:
        if not _ID_RE.match(value):
            raise ValueError(f"id {value!r} must match {_ID_RE.pattern} (lowercase, digits, single underscores).")
        return value

    @model_validator(mode="after")
    def _check_source_ids_unique(self) -> DatasetDescriptor:
        ids = [s.source_id for s in self.sources]
        if len(ids) != len(set(ids)):
            raise ValueError("source_id values must be unique within a dataset.")
        return self

    @property
    def targets(self) -> list[Variable]:
        """The variables explicitly declared as prediction targets (may be empty)."""
        return [v for v in self.variables if v.role is VariableRole.TARGET]

    @property
    def metadata_variables(self) -> list[Variable]:
        """The non-target variables (potential targets; shown with their own dataviz)."""
        return [v for v in self.variables if v.role is VariableRole.METADATA]

    def publication_blockers(self) -> list[str]:
        """Reasons this dataset must not be published *openly* (empty == publishable).

        Only the ``public`` tier is gated: it requires an open license, open origin sources (no
        re-hosting non-open data as open), and the responsible-release governance fields. ``private``
        and ``anonymized`` are valid catalog entries — they are token-gated, never published openly.
        """
        if self.tier is not Tier.PUBLIC:
            return []
        blockers: list[str] = []
        gov = self.governance
        if gov.license not in _OPEN_LICENSES:
            blockers.append(f"public tier requires an open license (one of: {', '.join(sorted(_OPEN_LICENSES))}); got {gov.license!r}.")
        for src in self.origin_sources:
            if src.kind is SourceKind.SCRIPT:
                continue  # a reproduction script (maintainer-only) is provenance, not a public data home
            if src.access is not SourceAccess.OPEN:
                blockers.append(f"public tier requires open origin sources; {src.locator!r} has access {src.access.value!r}.")
            if src.license is not None and src.license not in _OPEN_LICENSES:
                blockers.append(f"origin source {src.locator!r} is licensed {src.license!r} (not open): cannot re-host as open data under {gov.license!r}.")
        required = {
            "redistribution_rights": gov.redistribution_rights,
            "consent_ethics_status": gov.consent_ethics_status,
            "anonymization_status": gov.anonymization_status,
            "permitted_use": gov.permitted_use,
            "owner_steward": gov.owner_steward,
            "access_policy": gov.access_policy,
        }
        blockers.extend(f"governance.{field} is required for public release." for field, value in required.items() if _is_blank(value))
        return blockers


# =============================================================================
# Manifest (machine-generated; drives incremental processing)
# =============================================================================
class FileEntry(BaseModel):
    """One stored file (raw or canonical) with integrity + Dataverse identity."""

    model_config = ConfigDict(extra="forbid")

    path: str
    role: FileRole
    sha256: str  # local, authoritative for byte identity
    size: int = Field(ge=0)
    native_checksum_type: str | None = None  # e.g. "MD5"/"UNF" (Dataverse-reported)
    native_checksum: str | None = None
    file_id: int | None = None  # Dataverse database file id
    file_metadata_id: int | None = None

    @field_validator("sha256")
    @classmethod
    def _validate_sha256(cls, value: str) -> str:
        text = value.strip().lower()
        if not _SHA256_RE.match(text):
            raise ValueError("sha256 must be 64 lowercase hex characters.")
        return text

    @model_validator(mode="after")
    def _check_native_checksum_paired(self) -> FileEntry:
        if (self.native_checksum_type is None) != (self.native_checksum is None):
            raise ValueError("native_checksum_type and native_checksum must be set together.")
        return self


class Manifest(BaseModel):
    """Content-addressed manifest of a dataset version (source of truth for incrementality)."""

    model_config = ConfigDict(extra="forbid")

    schema_version: str = SCHEMA_VERSION
    dataset_id: str
    processing_hash: str  # content-derived; drives canonical rebuild
    converter_name: str
    converter_version: str
    converter_config: dict[str, str] = Field(default_factory=dict)
    files: list[FileEntry] = Field(default_factory=list)
    canonical_hashes: dict[str, str] = Field(default_factory=dict)  # canonical basename -> sha256
    row_counts: dict[str, int] = Field(default_factory=dict)  # per-source / targets / metadata
    doi: str | None = None
    dataset_version: str | None = None
    expected_previous_version: str | None = None
    created_at: str | None = None

    @field_validator("schema_version")
    @classmethod
    def _check_schema_version(cls, value: str) -> str:
        return _validate_schema_version(value)

    @model_validator(mode="after")
    def _check_unique_paths(self) -> Manifest:
        paths = [f.path for f in self.files]
        if len(paths) != len(set(paths)):
            raise ValueError("manifest file paths must be unique.")
        return self


# =============================================================================
# Subset (definition only; no data duplication) — keyed by sample identity
# =============================================================================
class Subset(BaseModel):
    """A sample-selector view over a parent dataset (no byte duplication)."""

    model_config = ConfigDict(extra="forbid")

    schema_version: str = SCHEMA_VERSION
    id: str
    parent: str
    description: str | None = None
    # Exactly one selector kind is expected (all keyed by sample_id).
    sample_ids: list[str] | None = None
    metadata_filter: dict[str, str] | None = None
    split: str | None = None  # name of a native SplitRef on the parent

    @field_validator("schema_version")
    @classmethod
    def _check_schema_version(cls, value: str) -> str:
        return _validate_schema_version(value)

    @field_validator("id", "parent")
    @classmethod
    def _validate_slug(cls, value: str) -> str:
        if not _ID_RE.match(value):
            raise ValueError(f"{value!r} must match {_ID_RE.pattern}.")
        return value

    @model_validator(mode="after")
    def _validate_selector(self) -> Subset:
        selectors = [self.sample_ids, self.metadata_filter, self.split]
        if sum(s is not None for s in selectors) != 1:
            raise ValueError("a subset must define exactly one of: sample_ids, metadata_filter, split.")
        if self.sample_ids is not None and not self.sample_ids:
            raise ValueError("sample_ids must be non-empty.")
        if self.metadata_filter is not None and not self.metadata_filter:
            raise ValueError("metadata_filter must be non-empty.")
        return self


def dataset_json_schema() -> dict[str, object]:
    """Return the JSON Schema (Draft 2020-12) for :class:`DatasetDescriptor`."""
    return DatasetDescriptor.model_json_schema()


if __name__ == "__main__":  # pragma: no cover
    import json
    import sys

    out = sys.argv[1] if len(sys.argv) > 1 else "catalog/schema/dataset_v2.json"
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(dataset_json_schema(), fh, indent=2, sort_keys=True)
    print(f"wrote {out}")
