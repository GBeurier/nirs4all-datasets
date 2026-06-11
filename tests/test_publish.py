"""Tests for the publication governance gate and orchestration (schema 2.0, no network)."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from nirs4all_datasets import schema as s
from nirs4all_datasets.publish import (
    PublicationBlocked,
    assert_publishable,
    publish_dataset,
    to_dataverse_metadata,
    update_dataset,
)


def _descriptor(
    *,
    tier: str = "public",
    dataverse: dict[str, Any] | None = None,
    origin_sources: list[dict[str, Any]] | None = None,
    governance_over: dict[str, Any] | None = None,
) -> s.DatasetDescriptor:
    """Build a schema-2.0 descriptor (clean public-tier open-license dataset by default)."""
    gov: dict[str, Any] = {
        "license": "CC-BY-4.0", "owner_steward": "Lab", "redistribution_rights": "open under CC-BY-4.0",
        "consent_ethics_status": "n/a", "anonymization_status": "n/a", "permitted_use": "research", "access_policy": "open",
    }
    if governance_over:
        gov.update(governance_over)
    kwargs: dict[str, Any] = {
        "id": "corn", "name": "Corn protein", "description": "example", "domain": "agriculture",
        "keywords": ["nir", "corn"],
        "sources": [{"source_id": "X1", "instrument_name": "m5", "axis_unit": "nm", "signal_type": "absorbance", "n_observations": 80, "n_variables": 700}],
        "variables": [{"name": "protein", "role": "target", "type": "numeric", "unit": "%"}],
        "provenance": {"contributor": "Lab"},
        "governance": gov,
        "tier": tier,
        "datacite": {"authors": [{"name": "Doe", "orcid": "0000-0002-1825-0097", "affiliation": "CIRAD"}]},
        "origin_sources": [{"kind": "zenodo", "locator": "10.5281/zenodo.1", "access": "open", "license": "CC-BY-4.0"}] if origin_sources is None else origin_sources,
    }
    if dataverse is not None:
        kwargs["dataverse"] = dataverse
    return s.DatasetDescriptor(**kwargs)


# ---------------------------------------------------------------------------
# governance gate
# ---------------------------------------------------------------------------
def test_assert_publishable_passes_for_clean_public() -> None:
    assert_publishable(_descriptor())  # clean public-tier open-license descriptor


def test_assert_publishable_blocks_public_with_non_open_license() -> None:
    with pytest.raises(PublicationBlocked):
        assert_publishable(_descriptor(governance_over={"license": "CC-BY-NC-4.0"}))


def test_assert_publishable_blocks_public_with_missing_governance() -> None:
    with pytest.raises(PublicationBlocked):
        assert_publishable(_descriptor(governance_over={"redistribution_rights": None}))


def test_assert_publishable_blocks_public_with_non_open_origin() -> None:
    with pytest.raises(PublicationBlocked):
        assert_publishable(_descriptor(origin_sources=[{"kind": "manual", "locator": "10.5281/zenodo.1", "access": "manual"}]))


@pytest.mark.parametrize("tier", ["private", "anonymized"])
def test_assert_publishable_passes_for_non_public_tier(tier: str) -> None:
    # Non-public tiers are token-gated, never gated on governance/license openness -> no blockers.
    assert_publishable(_descriptor(tier=tier, governance_over={"license": "proprietary", "redistribution_rights": None}))


# ---------------------------------------------------------------------------
# DataCite metadata mapping
# ---------------------------------------------------------------------------
def test_to_dataverse_metadata_maps_authors_and_license() -> None:
    meta = to_dataverse_metadata(_descriptor(), contact_email="a@b.c", subjects=["Chemistry"])
    dsv = meta["datasetVersion"]
    fields = {f["typeName"]: f for f in dsv["metadataBlocks"]["citation"]["fields"]}
    assert fields["title"]["value"] == "Corn protein"
    assert fields["author"]["value"][0]["authorName"]["value"] == "Doe"
    assert dsv["license"]["name"] == "CC BY 4.0"  # mapped from SPDX CC-BY-4.0


# ---------------------------------------------------------------------------
# mock client
# ---------------------------------------------------------------------------
class _FakeClient:
    """Stand-in DataverseClient recording every upload/replace/publish call (no network)."""

    def __init__(self, *, existing: dict[str, dict] | None = None) -> None:
        self.calls: list[tuple] = []
        self.existing = existing or {}

    def create_dataset(self, collection: str, metadata: dict) -> str:
        self.calls.append(("create", collection))
        return "doi:10.70112/NEW"

    def upload_file(self, doi: str, path: Path, *, tab_ingest: bool = False, description: str | None = None, directory_label: str | None = None, restrict: bool = False) -> dict:
        self.calls.append(("upload", Path(path).name, tab_ingest, directory_label, restrict))
        return {}

    def replace_file(self, file_id: int, path: Path, *, tab_ingest: bool = False, directory_label: str | None = None, restrict: bool = False) -> dict:
        self.calls.append(("replace", file_id, Path(path).name, restrict))
        return {}

    def file_checksums(self, doi: str, version: str = ":latest-published") -> dict[str, dict]:
        self.calls.append(("checksums", doi))
        return self.existing

    def publish_dataset(self, doi: str, *, version_type: str = "major") -> dict:
        self.calls.append(("publish", doi, version_type))
        return {"versionNumber": 2 if doi == "doi:10.70112/EXISTING" else 1}

    def wait_for_indexing(self, doi: str, **_: Any) -> None:
        self.calls.append(("wait", doi))


def _write_canonical(dataset_dir: Path, *names: str) -> None:
    canonical = dataset_dir / "canonical"
    canonical.mkdir()
    for name in names:
        (canonical / name).write_bytes(name.encode())


# ---------------------------------------------------------------------------
# publish_dataset
# ---------------------------------------------------------------------------
def test_publish_orchestration(tmp_path: Path) -> None:
    _write_canonical(tmp_path, "X.parquet", "Y.parquet")
    client = _FakeClient()

    result = publish_dataset(_descriptor(), tmp_path, client, collection="nirs", contact_email="a@b.c")  # type: ignore[arg-type]

    assert result == {"doi": "doi:10.70112/NEW", "files": 2, "version": 1}
    assert [c[0] for c in client.calls] == ["create", "upload", "upload", "publish", "wait"]
    uploads = [c for c in client.calls if c[0] == "upload"]
    assert all(u[2] is False for u in uploads)  # tabIngest disabled
    assert all(u[3] == "canonical" for u in uploads)  # directory label preserved


def test_publish_public_uploads_unrestricted(tmp_path: Path) -> None:
    _write_canonical(tmp_path, "X.parquet")
    client = _FakeClient()
    publish_dataset(_descriptor(tier="public"), tmp_path, client, collection="nirs", contact_email="a@b.c")  # type: ignore[arg-type]
    uploads = [c for c in client.calls if c[0] == "upload"]
    assert uploads and all(u[4] is False for u in uploads)  # public tier -> restrict=False


def test_publish_private_uploads_restricted(tmp_path: Path) -> None:
    _write_canonical(tmp_path, "X.parquet")
    client = _FakeClient()
    publish_dataset(_descriptor(tier="private"), tmp_path, client, collection="nirs", contact_email="a@b.c")  # type: ignore[arg-type]
    uploads = [c for c in client.calls if c[0] == "upload"]
    assert uploads and all(u[4] is True for u in uploads)  # non-public tier -> restrict=True


def test_publish_refuses_existing_doi(tmp_path: Path) -> None:
    _write_canonical(tmp_path, "X.parquet")
    descriptor = _descriptor(dataverse={"doi": "10.70112/EXISTING"})
    with pytest.raises(NotImplementedError):
        publish_dataset(descriptor, tmp_path, _FakeClient(), collection="nirs", contact_email="a@b.c")  # type: ignore[arg-type]


def test_publish_refuses_non_publishable(tmp_path: Path) -> None:
    _write_canonical(tmp_path, "X.parquet")
    with pytest.raises(PublicationBlocked):
        publish_dataset(_descriptor(governance_over={"license": "CC-BY-NC-4.0"}), tmp_path, _FakeClient(), collection="nirs", contact_email="a@b.c")  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# update_dataset
# ---------------------------------------------------------------------------
def test_update_dataset_replaces_existing_and_adds_new(tmp_path: Path) -> None:
    _write_canonical(tmp_path, "X.parquet", "Y.parquet")
    client = _FakeClient(existing={"X.parquet": {"type": "MD5", "value": "abc", "file_id": 5}})
    descriptor = _descriptor(dataverse={"doi": "10.70112/EXISTING"})

    result = update_dataset(descriptor, tmp_path, client)  # type: ignore[arg-type]

    assert result == {"doi": "10.70112/EXISTING", "files": 2, "version": 2}
    assert [c[0] for c in client.calls] == ["checksums", "replace", "upload", "publish", "wait"]
    assert ("replace", 5, "X.parquet", False) in client.calls  # existing file replaced in place
    assert any(c[0] == "upload" and c[1] == "Y.parquet" for c in client.calls)  # new file added


def test_update_dataset_requires_existing_doi(tmp_path: Path) -> None:
    _write_canonical(tmp_path, "X.parquet")
    with pytest.raises(ValueError):
        update_dataset(_descriptor(), tmp_path, _FakeClient())  # type: ignore[arg-type]


def test_update_dataset_restricts_files_when_not_public(tmp_path: Path) -> None:
    _write_canonical(tmp_path, "X.parquet")
    client = _FakeClient(existing={"X.parquet": {"type": "MD5", "value": "abc", "file_id": 5}})
    descriptor = _descriptor(tier="private", dataverse={"doi": "10.70112/EXISTING"})
    update_dataset(descriptor, tmp_path, client)  # type: ignore[arg-type]
    assert ("replace", 5, "X.parquet", True) in client.calls  # non-public tier -> restrict=True


# ---------------------------------------------------------------------------
# record_publication
# ---------------------------------------------------------------------------
def test_record_publication_updates_manifest(tmp_path: Path) -> None:
    from nirs4all_datasets.manifest import read_manifest, write_manifest
    from nirs4all_datasets.publish import record_publication
    from nirs4all_datasets.schema import FileEntry, FileRole, Manifest

    manifest = Manifest(
        dataset_id="corn", processing_hash="b" * 64, converter_name="c", converter_version="1",
        files=[FileEntry(path="canonical/X.parquet", role=FileRole.CANONICAL, sha256="a" * 64, size=10)],
    )
    write_manifest(manifest, tmp_path / "manifest.json")
    client = _FakeClient(existing={"X.parquet": {"type": "MD5", "value": "native123", "file_id": 9}})

    record_publication(tmp_path, client, "doi:10.70112/EXISTING", 2)  # type: ignore[arg-type]

    refreshed = read_manifest(tmp_path / "manifest.json")
    entry = refreshed.files[0]
    assert entry.file_id == 9
    assert entry.native_checksum_type == "MD5" and entry.native_checksum == "native123"
    assert refreshed.doi == "10.70112/EXISTING" and refreshed.dataset_version == "2"
