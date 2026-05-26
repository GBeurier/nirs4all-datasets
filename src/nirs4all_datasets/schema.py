"""Pydantic models for dataset descriptors, manifests, and subsets.

The descriptor (``catalog/datasets/<id>.yaml``) is the hand-authored source of truth
for a dataset's identity, provenance, governance, and Dataverse location. The manifest
(``cards/<id>/manifest.json``) is machine-generated and drives incremental processing.

Two separate concerns:

* **Schema validity** (every field well-formed) — enforced by the model validators and
  the ``catalog/scripts/validate.py`` CI gate. Confidential/internal descriptors are
  *valid*; they simply must not be published.
* **Publishability** (safe to release on a public/institutional Dataverse) — enforced by
  :meth:`DatasetDescriptor.publication_blockers`, called by the publish workflow.

Enum *values* mirror nirs4all's canonical vocabulary (``nirs4all.data.schema.config``)
so a descriptor maps cleanly onto a ``DatasetConfigs``. The mirror is intentional (it
keeps schema validation free of a heavy nirs4all import); ``tests/test_schema.py`` guards
against drift by comparing against the real nirs4all enums when installed.
"""
from __future__ import annotations

import re
from datetime import date
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

SCHEMA_VERSION = "1.0"

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
    tokens = stripped.split()
    for token in tokens:
        if token in _SPDX_OPERATORS:
            continue
        bare = token.strip("()")
        if not bare or not _SPDX_TOKEN_RE.match(bare):
            raise ValueError(
                f"license {value!r} is not a valid SPDX id/expression, 'LicenseRef-<name>', or 'proprietary'."
            )
    return stripped


# =============================================================================
# Enums (values mirror nirs4all.data.schema.config; guarded by tests)
# =============================================================================
class TaskType(StrEnum):
    """Supervised task type (mirrors ``nirs4all`` ``TaskType``)."""

    AUTO = "auto"
    REGRESSION = "regression"
    BINARY_CLASSIFICATION = "binary_classification"
    MULTICLASS_CLASSIFICATION = "multiclass_classification"


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
    HYPERSPECTRAL = "hyperspectral"
    OTHER = "other"


class Visibility(StrEnum):
    """Publication visibility on the Dataverse instance."""

    PUBLIC = "public"
    RESTRICTED = "restricted"
    EMBARGO = "embargo"


class ConfidentialityClass(StrEnum):
    """Data confidentiality classification."""

    PUBLIC = "public"
    INTERNAL = "internal"
    CONFIDENTIAL = "confidential"


class ConversionStatus(StrEnum):
    """Outcome of raw->canonical conversion."""

    OK = "ok"
    PARTIAL = "partial"
    FAILED = "failed"


class FileRole(StrEnum):
    """Role of a stored file in a dataset."""

    RAW = "raw"
    CANONICAL = "canonical"


def _validate_schema_version(value: str) -> str:
    if value != SCHEMA_VERSION:
        raise ValueError(f"unsupported schema_version {value!r} (expected {SCHEMA_VERSION!r}).")
    return value


# =============================================================================
# Descriptor sub-models
# =============================================================================
class Target(BaseModel):
    """A prediction target carried by the dataset."""

    model_config = ConfigDict(extra="forbid")

    name: str
    task_type: TaskType
    unit: str | None = None
    range: tuple[float, float] | None = None


class Instrument(BaseModel):
    """Acquisition instrument and signal description (NIRS FAIR fields)."""

    model_config = ConfigDict(extra="forbid")

    vendor: str | None = None
    model: str | None = None
    serial: str | None = None
    firmware: str | None = None
    modality: Modality = Modality.NIR
    axis_unit: AxisUnit = AxisUnit.WAVELENGTH
    axis_range: tuple[float, float] | None = None
    signal_type: SignalType = SignalType.AUTO
    acquisition_settings: dict[str, str] = Field(default_factory=dict)


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


class DataCite(BaseModel):
    """Rich metadata mapped onto native Dataverse/DataCite fields at publish."""

    model_config = ConfigDict(extra="forbid")

    authors: list[Author] = Field(default_factory=list)
    funding: list[Funding] = Field(default_factory=list)
    related_publications: list[str] = Field(default_factory=list)
    related_software: list[str] = Field(default_factory=list)


class Governance(BaseModel):
    """Legal/ethical metadata. Publication is gated on these fields (see publication_blockers)."""

    model_config = ConfigDict(extra="forbid")

    license: str
    visibility: Visibility = Visibility.RESTRICTED
    confidentiality_class: ConfidentialityClass = ConfidentialityClass.INTERNAL
    owner_steward: str | None = None
    redistribution_rights: str | None = None
    consent_ethics_status: str | None = None
    anonymization_status: str | None = None
    permitted_use: str | None = None
    access_policy: str | None = None
    embargo_until: date | None = None

    @field_validator("license")
    @classmethod
    def _check_license_syntax(cls, value: str) -> str:
        return _validate_license_syntax(value)

    @model_validator(mode="after")
    def _check_embargo_present(self) -> Governance:
        # Structural check only: presence. The "not yet lapsed" check lives in the
        # publication gate so descriptors do not start failing as time passes.
        if self.visibility is Visibility.EMBARGO and self.embargo_until is None:
            raise ValueError("visibility 'embargo' requires 'embargo_until'.")
        return self


class DataverseRef(BaseModel):
    """Pointer to the dataset's Dataverse location and pinned version."""

    model_config = ConfigDict(extra="forbid")

    instance: str = "https://entrepot.recherche.data.gouv.fr"
    doi: str | None = None
    dataset_version: str | None = None

    @field_validator("doi")
    @classmethod
    def _normalize_doi(cls, value: str | None) -> str | None:
        if value is None:
            return None
        text = value.strip()
        for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
            if text.lower().startswith(prefix):
                text = text[len(prefix):]
                break
        if not _DOI_RE.match(text):
            raise ValueError(f"invalid DOI {value!r} (expected '10.<prefix>/<suffix>').")
        return text


# =============================================================================
# Descriptor
# =============================================================================
class DatasetDescriptor(BaseModel):
    """Hand-authored descriptor for one NIRS dataset (``catalog/datasets/<id>.yaml``)."""

    model_config = ConfigDict(extra="forbid")

    schema_version: str = SCHEMA_VERSION
    id: str
    name: str
    version: str = "0.1.0"
    description: str
    domain: str | None = None
    keywords: list[str] = Field(default_factory=list)
    citation: str | None = None

    instrument: Instrument
    targets: list[Target] = Field(min_length=1)
    repetition_column: str | None = None
    predefined_split: bool = False
    n_samples: int | None = Field(default=None, ge=1)
    n_features: int | None = Field(default=None, ge=1)
    n_sources: int = Field(default=1, ge=1)

    provenance: Provenance
    governance: Governance
    datacite: DataCite | None = None
    dataverse: DataverseRef = Field(default_factory=DataverseRef)

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

    @field_validator("version")
    @classmethod
    def _validate_version(cls, value: str) -> str:
        if not _SEMVER_RE.match(value):
            raise ValueError(f"version {value!r} must be semantic (e.g. '1.0.0').")
        return value

    def publication_blockers(self) -> list[str]:
        """Return reasons why this dataset must not be published (empty == publishable).

        Enforces: confidential is a hard stop; public visibility requires public
        confidentiality and an open license; a live embargo blocks; and every governance
        field required for responsible release must be a non-blank string.
        """
        blockers: list[str] = []
        gov = self.governance

        if gov.confidentiality_class is ConfidentialityClass.CONFIDENTIAL:
            blockers.append(
                "confidentiality_class is 'confidential': not allowed on Dataverse "
                "(requires DPO/legal approval and a dedicated secure backend)."
            )
        if gov.visibility is Visibility.PUBLIC and gov.confidentiality_class is not ConfidentialityClass.PUBLIC:
            blockers.append(
                f"visibility 'public' is inconsistent with confidentiality_class "
                f"{gov.confidentiality_class.value!r}."
            )
        if gov.visibility is Visibility.PUBLIC and gov.license not in _OPEN_LICENSES:
            blockers.append(
                f"visibility 'public' requires an open license (one of: {', '.join(sorted(_OPEN_LICENSES))}); "
                f"got {gov.license!r}."
            )
        if gov.visibility is Visibility.EMBARGO and gov.embargo_until and gov.embargo_until > date.today():
            blockers.append(f"under embargo until {gov.embargo_until.isoformat()}.")

        required = {
            "redistribution_rights": gov.redistribution_rights,
            "consent_ethics_status": gov.consent_ethics_status,
            "anonymization_status": gov.anonymization_status,
            "permitted_use": gov.permitted_use,
            "owner_steward": gov.owner_steward,
            "access_policy": gov.access_policy,
        }
        blockers.extend(f"governance.{field} is required for publication." for field, value in required.items() if _is_blank(value))
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
    descriptor_hash: str
    converter_name: str
    converter_version: str
    converter_config: dict[str, str] = Field(default_factory=dict)
    files: list[FileEntry] = Field(default_factory=list)
    canonical_hashes: dict[str, str] = Field(default_factory=dict)  # X/Y/M/folds -> sha256
    row_counts: dict[str, int] = Field(default_factory=dict)
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
# Subset (definition only; no data duplication)
# =============================================================================
class Subset(BaseModel):
    """A row-selector view over a parent dataset (no byte duplication)."""

    model_config = ConfigDict(extra="forbid")

    schema_version: str = SCHEMA_VERSION
    id: str
    parent: str
    description: str | None = None
    # Exactly one selector kind is expected.
    sample_ids: list[str] | None = None
    metadata_filter: dict[str, str] | None = None
    folds: list[int] | None = None

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
        selectors = [self.sample_ids, self.metadata_filter, self.folds]
        if sum(s is not None for s in selectors) != 1:
            raise ValueError("a subset must define exactly one of: sample_ids, metadata_filter, folds.")
        if self.sample_ids is not None and not self.sample_ids:
            raise ValueError("sample_ids must be non-empty.")
        if self.metadata_filter is not None and not self.metadata_filter:
            raise ValueError("metadata_filter must be non-empty.")
        if self.folds is not None:
            if not self.folds:
                raise ValueError("folds must be non-empty.")
            if any(f < 0 for f in self.folds):
                raise ValueError("fold ids must be non-negative.")
        return self


def dataset_json_schema() -> dict[str, object]:
    """Return the JSON Schema (Draft 2020-12) for :class:`DatasetDescriptor`."""
    return DatasetDescriptor.model_json_schema()


if __name__ == "__main__":  # pragma: no cover
    import json
    import sys

    out = sys.argv[1] if len(sys.argv) > 1 else "catalog/schema/dataset_v1.json"
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(dataset_json_schema(), fh, indent=2, sort_keys=True)
    print(f"wrote {out}")
