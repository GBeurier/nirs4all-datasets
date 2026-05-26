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
    def __init__(self) -> None:
        self.calls: list[tuple] = []

    def create_dataset(self, collection: str, metadata: dict) -> str:
        self.calls.append(("create", collection))
        return "doi:10.70112/NEW"

    def upload_file(self, doi: str, path: Path, *, tab_ingest: bool = False, description: str | None = None, directory_label: str | None = None) -> dict:
        self.calls.append(("upload", Path(path).name, tab_ingest, directory_label))
        return {}

    def publish_dataset(self, doi: str, *, version_type: str = "major") -> dict:
        self.calls.append(("publish", doi, version_type))
        return {"versionNumber": 1}

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
