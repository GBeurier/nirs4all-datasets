"""Tests for the schema 2.0 descriptor/manifest/subset models and the publication gate."""
from __future__ import annotations

from typing import Any

import pytest
from pydantic import ValidationError

from nirs4all_datasets import schema as s

_HASH = "a" * 64


def _gov(**over: Any) -> dict[str, Any]:
    base: dict[str, Any] = {
        "license": "CC-BY-4.0",
        "owner_steward": "Lab",
        "redistribution_rights": "open under CC-BY-4.0",
        "consent_ethics_status": "n/a",
        "anonymization_status": "n/a",
        "permitted_use": "research",
        "access_policy": "open",
    }
    base.update(over)
    return base


def _desc(**over: Any) -> dict[str, Any]:
    base: dict[str, Any] = {
        "id": "corn_eigenvector_nir",
        "name": "Corn (Eigenvector)",
        "description": "Multi-instrument NIR corn benchmark.",
        "sources": [{"source_id": "X1", "instrument_name": "m5", "axis_unit": "nm", "n_observations": 80, "n_variables": 700}],
        "variables": [{"name": "Moisture", "role": "target", "type": "numeric", "unit": "%"}],
        "provenance": {"contributor": "Eigenvector"},
        "governance": _gov(),
        "tier": "private",
    }
    base.update(over)
    return base


def test_valid_descriptor() -> None:
    d = s.DatasetDescriptor(**_desc())
    assert d.id == "corn_eigenvector_nir"
    assert [v.name for v in d.targets] == ["Moisture"]
    assert d.metadata_variables == []
    assert d.tier is s.Tier.PRIVATE
    assert d.retrieval.status is s.RetrievalStatus.DOCUMENTED_ONLY
    assert d.retrieval.routes == []
    assert d.publication_blockers() == []  # private tier is always publishable-valid (token-gated)


def test_dataset_can_have_no_variables() -> None:
    d = s.DatasetDescriptor(**_desc(variables=[]))  # X-only datasets are valid
    assert d.targets == [] and d.variables == []


@pytest.mark.parametrize("bad_id", ["Corn", "corn-protein", "corn__protein", "_corn", "corn_"])
def test_bad_id_rejected(bad_id: str) -> None:
    with pytest.raises(ValidationError):
        s.DatasetDescriptor(**_desc(id=bad_id))


def test_sources_required_and_source_ids_unique() -> None:
    with pytest.raises(ValidationError):
        s.DatasetDescriptor(**_desc(sources=[]))  # >=1 source required
    with pytest.raises(ValidationError):
        s.DatasetDescriptor(**_desc(sources=[{"source_id": "X"}, {"source_id": "X"}]))  # duplicate id


def test_versions_content_semver() -> None:
    s.DatasetDescriptor(**_desc(versions={"content": "2.1.0"}))
    with pytest.raises(ValidationError):
        s.DatasetDescriptor(**_desc(versions={"content": "1.0"}))


def test_bad_schema_version_rejected() -> None:
    with pytest.raises(ValidationError):
        s.DatasetDescriptor(**_desc(schema_version="9.9"))


@pytest.mark.parametrize("lic", ["CC-BY-4.0", "MIT", "proprietary", "LicenseRef-not-cleared", "MIT OR Apache-2.0"])
def test_accepted_license_syntax(lic: str) -> None:
    s.DatasetDescriptor(**_desc(governance=_gov(license=lic)))


def test_invalid_license_rejected() -> None:
    with pytest.raises(ValidationError):
        s.DatasetDescriptor(**_desc(governance=_gov(license="Invalid License!")))


def test_public_tier_requires_open_license() -> None:
    d = s.DatasetDescriptor(**_desc(tier="public", governance=_gov(license="CC-BY-NC-4.0")))
    assert any("open license" in b for b in d.publication_blockers())


def test_public_tier_requires_open_origin_sources() -> None:
    d = s.DatasetDescriptor(**_desc(
        tier="public",
        origin_sources=[{"kind": "zenodo", "locator": "10.5281/zenodo.1", "access": "manual"}],
    ))
    assert any("open origin sources" in b for b in d.publication_blockers())


def test_public_tier_blocks_non_open_origin_rehost() -> None:
    d = s.DatasetDescriptor(**_desc(
        tier="public",
        origin_sources=[{"kind": "zenodo", "locator": "10.5281/z", "access": "open", "license": "CC-BY-NC-4.0"}],
    ))
    assert any("cannot re-host" in b for b in d.publication_blockers())


def test_public_tier_requires_governance_fields() -> None:
    d = s.DatasetDescriptor(**_desc(tier="public", governance=_gov(owner_steward="  ")))
    assert any("owner_steward" in b for b in d.publication_blockers())


def test_private_and_anonymized_have_no_blockers() -> None:
    for tier in ("private", "anonymized"):
        d = s.DatasetDescriptor(**_desc(tier=tier, governance=_gov(license="proprietary")))
        assert d.publication_blockers() == []  # token-gated, never published openly


def test_origin_source_token_guard() -> None:
    s.OriginSource(kind="dataverse", locator="10.70112/x", access="token")  # Dataverse token ok
    s.OriginSource(kind="figshare", locator="10.6084/x", access="token", credential_ref="figshare_pat")
    with pytest.raises(ValidationError):
        s.OriginSource(kind="url", locator="http://x/y", access="token")  # non-Dataverse token needs credential_ref


def test_retrieval_route_and_resource_validation() -> None:
    d = s.DatasetDescriptor(**_desc(
        retrieval={
            "status": "raw_reproducible",
            "public_retrievable": True,
            "public_redistributable": False,
            "routes": [
                {
                    "id": "official_raw",
                    "method": "raw_retrieve",
                    "provider": "figshare",
                    "locator": "10.6084/m9.figshare.1",
                    "resources": [
                        {
                            "id": "spectra",
                            "role": "spectra",
                            "selector": {"kind": "api_file_name", "value": "spectra.csv"},
                            "file_name": "spectra.csv",
                            "format": "csv",
                            "sha256": _HASH.upper(),
                        }
                    ],
                    "canonicalization": {
                        "engine": "nirs4all_io",
                        "recipe_id": "demo_v1",
                        "recipe_version": "1.0.0",
                        "expected_layout": "v2_standard",
                        "expected_files": ["X.csv", "Y.csv", "M.csv"],
                    },
                }
            ],
        },
    ))
    route = d.retrieval.routes[0]
    assert d.retrieval.status is s.RetrievalStatus.RAW_REPRODUCIBLE
    assert route.resources[0].sha256 == _HASH
    assert route.canonicalization and route.canonicalization.engine is s.CanonicalizationEngine.NIRS4ALL_IO


def test_manual_retrieval_route_cannot_claim_automatic_download() -> None:
    with pytest.raises(ValidationError):
        s.RetrievalRoute(id="manual", method="manual", provider="manual", locator="https://example.org")
    with pytest.raises(ValidationError):
        s.RetrievalRoute(
            id="raw_manual_access",
            method="raw_retrieve",
            provider="url",
            access="manual",
            locator="https://example.org/raw.csv",
        )
    with pytest.raises(ValidationError):
        s.RetrievalRoute(
            id="canonical_manual_access",
            method="canonical_fetch",
            provider="dataverse",
            access="manual",
            locator="10.70112/ABC",
        )


@pytest.mark.parametrize(
    ("raw", "expected"),
    [("DOI: 10.1002/ppj2.70059", "10.1002/ppj2.70059"), ("https://doi.org/10.1111/abc", "10.1111/abc")],
)
def test_publication_ref_doi_normalization(raw: str, expected: str) -> None:
    assert s.PublicationRef(doi=raw).doi == expected


def test_publication_ref_invalid_doi() -> None:
    with pytest.raises(ValidationError):
        s.PublicationRef(doi="not-a-doi")


def test_dataverse_ref_doi() -> None:
    assert s.DataverseRef(doi="https://doi.org/10.57745/XYZ").doi == "10.57745/XYZ"
    with pytest.raises(ValidationError):
        s.DataverseRef(doi="11.1/x")


def test_file_entry_validation() -> None:
    fe = s.FileEntry(path="canonical/sources/X1.parquet", role="canonical", sha256=_HASH.upper(), size=10)
    assert fe.sha256 == _HASH  # normalized lowercase
    with pytest.raises(ValidationError):
        s.FileEntry(path="x", role="raw", sha256="deadbeef", size=1)  # too short
    with pytest.raises(ValidationError):
        s.FileEntry(path="x", role="raw", sha256=_HASH, size=1, native_checksum_type="MD5")  # unpaired


def test_manifest_processing_hash_field_and_unique_paths() -> None:
    files = [
        {"path": "canonical/sources/X.parquet", "role": "canonical", "sha256": _HASH, "size": 1},
        {"path": "canonical/sources/X.parquet", "role": "canonical", "sha256": _HASH, "size": 2},
    ]
    with pytest.raises(ValidationError):
        s.Manifest(dataset_id="corn", processing_hash=_HASH, converter_name="c", converter_version="1", files=files)
    m = s.Manifest(dataset_id="corn", processing_hash=_HASH, converter_name="c", converter_version="1")
    assert m.processing_hash == _HASH


def test_subset_selectors() -> None:
    with pytest.raises(ValidationError):
        s.Subset(id="sub_a", parent="corn")  # zero selectors
    with pytest.raises(ValidationError):
        s.Subset(id="sub_a", parent="corn", split="original", sample_ids=["x"])  # two
    with pytest.raises(ValidationError):
        s.Subset(id="sub_a", parent="corn", sample_ids=[])  # empty
    s.Subset(id="sub_a", parent="corn", split="original")  # one -> ok
    s.Subset(id="sub_b", parent="corn", sample_ids=["s1", "s2"])  # one -> ok


def test_json_schema_export() -> None:
    js = s.dataset_json_schema()
    assert js["title"] == "DatasetDescriptor" and "properties" in js


def test_enum_alignment_with_nirs4all() -> None:
    """Guard the nirs4all-mirrored enums against drift (skips if nirs4all absent). Acquisition enums
    (SourceKind/SourceAccess/Tier/VariableRole/VarType) are this package's own and are NOT mirrored."""
    cfg = pytest.importorskip("nirs4all.data.schema.config")
    assert {e.value for e in s.AxisUnit} == {e.value for e in cfg.HeaderUnit}
    assert {e.value for e in s.SignalType} == {e.value for e in cfg.SignalTypeEnum}
