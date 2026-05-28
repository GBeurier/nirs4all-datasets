"""Tests for the publication governance gate and orchestration (no network)."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from nirs4all_datasets import schema as s
from nirs4all_datasets.publish import PublicationBlocked, assert_publishable, publish_dataset, to_dataverse_metadata


def _descriptor(*, dataverse: dict[str, Any] | None = None, **gov_over: Any) -> s.DatasetDescriptor:
    gov: dict[str, Any] = {
        "license": "CC-BY-4.0", "visibility": "public", "confidentiality_class": "public",
        "owner_steward": "Lab", "redistribution_rights": "CC-BY-4.0", "consent_ethics_status": "n/a",
        "anonymization_status": "n/a", "permitted_use": "research", "access_policy": "open",
    }
    gov.update(gov_over)
    kwargs: dict[str, Any] = {
        "id": "corn", "name": "Corn protein", "version": "1.0.0", "description": "example",
        "instrument": {"modality": "NIR"}, "targets": [{"name": "protein", "task_type": "regression"}],
        "keywords": ["nir", "corn"], "provenance": {"contributor": "Lab"}, "governance": gov,
        "datacite": {"authors": [{"name": "Doe", "orcid": "0000-0002-1825-0097"}]},
    }
    if dataverse is not None:
        kwargs["dataverse"] = dataverse
    return s.DatasetDescriptor(**kwargs)


def test_assert_publishable_passes_and_blocks() -> None:
    assert_publishable(_descriptor())
    with pytest.raises(PublicationBlocked):
        assert_publishable(_descriptor(confidentiality_class="confidential", visibility="restricted"))
    with pytest.raises(PublicationBlocked):
        assert_publishable(_descriptor(redistribution_rights=None))


def test_to_dataverse_metadata_maps_authors_and_license() -> None:
    meta = to_dataverse_metadata(_descriptor(), contact_email="a@b.c", subjects=["Chemistry"])
    dsv = meta["datasetVersion"]
    fields = {f["typeName"]: f for f in dsv["metadataBlocks"]["citation"]["fields"]}
    assert fields["title"]["value"] == "Corn protein"
    assert fields["author"]["value"][0]["authorName"]["value"] == "Doe"
    assert dsv["license"]["name"] == "CC BY 4.0"  # mapped from SPDX CC-BY-4.0


class _FakeClient:
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


def test_publish_orchestration(tmp_path: Path) -> None:
    canonical = tmp_path / "canonical"
    canonical.mkdir()
    (canonical / "X.parquet").write_bytes(b"x")
    (canonical / "Y.parquet").write_bytes(b"y")
    client = _FakeClient()

    result = publish_dataset(_descriptor(), tmp_path, client, collection="nirs", contact_email="a@b.c")  # type: ignore[arg-type]

    assert result["doi"] == "doi:10.70112/NEW"
    assert result["files"] == 2
    assert [c[0] for c in client.calls] == ["create", "upload", "upload", "publish", "wait"]
    uploads = [c for c in client.calls if c[0] == "upload"]
    assert all(u[2] is False for u in uploads)  # tabIngest disabled
    assert all(u[3] == "canonical" for u in uploads)  # directory label preserved


def test_publish_refuses_confidential(tmp_path: Path) -> None:
    with pytest.raises(PublicationBlocked):
        publish_dataset(_descriptor(confidentiality_class="confidential", visibility="restricted"), tmp_path, _FakeClient(), collection="nirs", contact_email="a@b.c")  # type: ignore[arg-type]


def test_publish_refuses_existing_doi(tmp_path: Path) -> None:
    descriptor = _descriptor(dataverse={"doi": "10.70112/EXISTING"})
    with pytest.raises(NotImplementedError):
        publish_dataset(descriptor, tmp_path, _FakeClient(), collection="nirs", contact_email="a@b.c")  # type: ignore[arg-type]


def test_publish_restricts_files_when_not_public(tmp_path: Path) -> None:
    canonical = tmp_path / "canonical"
    canonical.mkdir()
    (canonical / "X.parquet").write_bytes(b"x")
    client = _FakeClient()
    publish_dataset(_descriptor(visibility="restricted", confidentiality_class="internal"), tmp_path, client, collection="nirs", contact_email="a@b.c")  # type: ignore[arg-type]
    uploads = [c for c in client.calls if c[0] == "upload"]
    assert uploads and all(u[4] is True for u in uploads)  # restrict flag set for non-public visibility


def test_update_dataset_replaces_existing_and_adds_new(tmp_path: Path) -> None:
    from nirs4all_datasets.publish import update_dataset

    canonical = tmp_path / "canonical"
    canonical.mkdir()
    (canonical / "X.parquet").write_bytes(b"x")
    (canonical / "Y.parquet").write_bytes(b"y")
    client = _FakeClient(existing={"X.parquet": {"type": "MD5", "value": "abc", "file_id": 5}})
    descriptor = _descriptor(dataverse={"doi": "10.70112/EXISTING"})

    result = update_dataset(descriptor, tmp_path, client)  # type: ignore[arg-type]

    assert result == {"doi": "10.70112/EXISTING", "files": 2, "version": 2}
    kinds = [c[0] for c in client.calls]
    assert kinds == ["checksums", "replace", "upload", "publish", "wait"]
    assert ("replace", 5, "X.parquet", False) in client.calls  # existing file replaced in place
    assert any(c[0] == "upload" and c[1] == "Y.parquet" for c in client.calls)  # new file added


def test_record_publication_updates_manifest(tmp_path: Path) -> None:
    from nirs4all_datasets.manifest import read_manifest, write_manifest
    from nirs4all_datasets.publish import record_publication
    from nirs4all_datasets.schema import FileEntry, FileRole, Manifest

    manifest = Manifest(
        dataset_id="corn", descriptor_hash="b" * 64, converter_name="c", converter_version="1",
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
