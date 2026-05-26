"""Tests for the descriptor/manifest/subset schema and the publication gate."""
from __future__ import annotations

from datetime import date, timedelta
from typing import Any

import pytest
from pydantic import ValidationError

from nirs4all_datasets import schema as s

_HASH = "a" * 64


def _gov(**over: Any) -> dict[str, Any]:
    base: dict[str, Any] = {
        "license": "CC-BY-4.0",
        "visibility": "public",
        "confidentiality_class": "public",
        "owner_steward": "Lab",
        "redistribution_rights": "CC-BY-4.0",
        "consent_ethics_status": "n/a",
        "anonymization_status": "n/a",
        "permitted_use": "research",
        "access_policy": "open",
    }
    base.update(over)
    return base


def _desc(**over: Any) -> dict[str, Any]:
    base: dict[str, Any] = {
        "id": "corn_protein",
        "name": "Corn protein",
        "version": "1.0.0",
        "description": "Example.",
        "instrument": {"modality": "NIR", "axis_unit": "nm", "signal_type": "absorbance"},
        "targets": [{"name": "protein", "task_type": "regression", "unit": "%"}],
        "provenance": {"contributor": "Lab"},
        "governance": _gov(),
    }
    base.update(over)
    return base


def test_valid_descriptor_is_publishable() -> None:
    d = s.DatasetDescriptor(**_desc())
    assert d.id == "corn_protein"
    assert d.publication_blockers() == []


@pytest.mark.parametrize("bad_id", ["Corn", "corn-protein", "corn__protein", "_corn", "corn_"])
def test_bad_id_rejected(bad_id: str) -> None:
    with pytest.raises(ValidationError):
        s.DatasetDescriptor(**_desc(id=bad_id))


def test_bad_version_rejected() -> None:
    with pytest.raises(ValidationError):
        s.DatasetDescriptor(**_desc(version="1.0"))


def test_bad_schema_version_rejected() -> None:
    with pytest.raises(ValidationError):
        s.DatasetDescriptor(**_desc(schema_version="9.9"))


def test_invalid_license_syntax_rejected() -> None:
    with pytest.raises(ValidationError):
        s.DatasetDescriptor(**_desc(governance=_gov(license="Invalid License!")))


@pytest.mark.parametrize("lic", ["CC-BY-4.0", "MIT", "proprietary", "LicenseRef-internal", "Apache-2.0 WITH LLVM-exception", "MIT OR Apache-2.0"])
def test_accepted_license_syntax(lic: str) -> None:
    s.DatasetDescriptor(**_desc(governance=_gov(license=lic)))


def test_public_requires_open_license() -> None:
    d = s.DatasetDescriptor(**_desc(governance=_gov(license="CC-BY-NC-4.0")))
    assert any("open license" in b for b in d.publication_blockers())


def test_public_confidentiality_consistency() -> None:
    d = s.DatasetDescriptor(**_desc(governance=_gov(confidentiality_class="internal")))
    assert any("inconsistent" in b for b in d.publication_blockers())


def test_confidential_blocks_publication() -> None:
    d = s.DatasetDescriptor(**_desc(governance=_gov(visibility="restricted", confidentiality_class="confidential")))
    assert any("confidential" in b for b in d.publication_blockers())


def test_whitespace_governance_field_blocks() -> None:
    d = s.DatasetDescriptor(**_desc(governance=_gov(owner_steward="   ")))
    assert any("owner_steward" in b for b in d.publication_blockers())


def test_embargo_requires_date_but_does_not_check_future_at_parse() -> None:
    # Missing embargo_until is a structural error.
    with pytest.raises(ValidationError):
        s.DatasetDescriptor(**_desc(governance=_gov(visibility="embargo", confidentiality_class="internal")))
    # A past embargo parses fine and is NOT blocked (embargo lapsed).
    past = _gov(visibility="embargo", confidentiality_class="internal", embargo_until=date.today() - timedelta(days=1))
    d_past = s.DatasetDescriptor(**_desc(governance=past))
    assert not any("embargo" in b for b in d_past.publication_blockers())
    # A live embargo parses fine but blocks publication.
    future = _gov(visibility="embargo", confidentiality_class="internal", embargo_until=date.today() + timedelta(days=30))
    d_future = s.DatasetDescriptor(**_desc(governance=future))
    assert any("embargo" in b for b in d_future.publication_blockers())


@pytest.mark.parametrize(
    ("raw", "expected"),
    [("doi:10.70112/abc", "10.70112/abc"), ("https://doi.org/10.57745/XYZ", "10.57745/XYZ"), ("10.18167/DVN1/ABCDEF", "10.18167/DVN1/ABCDEF")],
)
def test_doi_normalization(raw: str, expected: str) -> None:
    assert s.DataverseRef(doi=raw).doi == expected


@pytest.mark.parametrize("doi", ["not-a-doi", "10/abc", "11.1/x"])
def test_invalid_dois(doi: str) -> None:
    with pytest.raises(ValidationError):
        s.DataverseRef(doi=doi)


def test_file_entry_validation() -> None:
    fe = s.FileEntry(path="canonical/X.parquet", role="canonical", sha256=_HASH.upper(), size=10)
    assert fe.sha256 == _HASH  # normalized to lowercase
    with pytest.raises(ValidationError):
        s.FileEntry(path="x", role="raw", sha256="deadbeef", size=1)  # too short
    with pytest.raises(ValidationError):
        s.FileEntry(path="x", role="raw", sha256=_HASH, size=1, native_checksum_type="MD5")  # unpaired


def test_manifest_unique_paths() -> None:
    files = [
        {"path": "canonical/X.parquet", "role": "canonical", "sha256": _HASH, "size": 1},
        {"path": "canonical/X.parquet", "role": "canonical", "sha256": _HASH, "size": 2},
    ]
    with pytest.raises(ValidationError):
        s.Manifest(dataset_id="corn_protein", descriptor_hash=_HASH, converter_name="tabular", converter_version="0.1.0", files=files)


def test_subset_selectors() -> None:
    with pytest.raises(ValidationError):
        s.Subset(id="sub_a", parent="corn_protein")  # zero selectors
    with pytest.raises(ValidationError):
        s.Subset(id="sub_a", parent="corn_protein", folds=[0], sample_ids=["x"])  # two
    with pytest.raises(ValidationError):
        s.Subset(id="sub_a", parent="corn_protein", sample_ids=[])  # empty
    with pytest.raises(ValidationError):
        s.Subset(id="sub_a", parent="corn_protein", folds=[-1])  # negative
    s.Subset(id="sub_a", parent="corn_protein", folds=[0, 1])  # one -> ok


def test_json_schema_exports() -> None:
    js = s.dataset_json_schema()
    assert js["title"] == "DatasetDescriptor"
    assert "properties" in js


def test_enum_alignment_with_nirs4all() -> None:
    """Guard against drift from nirs4all's canonical vocabulary (skips if not installed)."""
    cfg = pytest.importorskip("nirs4all.data.schema.config")
    assert {e.value for e in s.TaskType} == {e.value for e in cfg.TaskType}
    assert {e.value for e in s.AxisUnit} == {e.value for e in cfg.HeaderUnit}
    assert {e.value for e in s.SignalType} == {e.value for e in cfg.SignalTypeEnum}
