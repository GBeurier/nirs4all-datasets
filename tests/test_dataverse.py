"""Tests for the Dataverse client (no network: an injected fake session)."""
from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from nirs4all_datasets.dataverse import DataverseClient, DataverseError, dataset_metadata


def _resp(json_data: dict, *, ok: bool = True, status: int = 200, method: str = "POST") -> MagicMock:
    resp = MagicMock()
    resp.ok = ok
    resp.status_code = status
    resp.reason = "OK" if ok else "Bad Request"
    resp.json.return_value = json_data
    resp.request.method = method
    resp.url = "https://dv.example/api/datasets/:persistentId/add?persistentId=doi:10.70112/ABC"
    return resp


def _client(session: MagicMock, token: str | None = "SECRET-TOKEN") -> DataverseClient:
    return DataverseClient(instance="https://dv.example", token=token, session=session)


def test_upload_file_puts_tab_ingest_in_jsondata(tmp_path: Path) -> None:
    f = tmp_path / "X.parquet"
    f.write_bytes(b"data")
    session = MagicMock()
    session.post.return_value = _resp({"data": {"files": [{"dataFile": {"id": 1}}]}})
    _client(session).upload_file("doi:10.70112/ABC", f, tab_ingest=False, directory_label="canonical")

    args, kwargs = session.post.call_args
    assert args[0].endswith("/api/datasets/:persistentId/add")
    assert kwargs["params"] == {"persistentId": "doi:10.70112/ABC"}
    assert kwargs["headers"] == {"X-Dataverse-key": "SECRET-TOKEN"}
    meta = json.loads(kwargs["data"]["jsonData"])
    assert meta["tabIngest"] == "false"
    assert meta["directoryLabel"] == "canonical"
    assert "file" in kwargs["files"]
    assert "key" not in args[0]


def test_publish_uses_actions_publish_endpoint() -> None:
    session = MagicMock()
    session.post.return_value = _resp({"data": {"versionNumber": 1}})
    _client(session).publish_dataset("doi:10.70112/ABC", version_type="major")
    args, kwargs = session.post.call_args
    assert args[0].endswith("/api/datasets/:persistentId/actions/:publish")
    assert kwargs["params"] == {"persistentId": "doi:10.70112/ABC", "type": "major"}


def test_wait_for_indexing_handles_empty_lock_list() -> None:
    session = MagicMock()
    session.get.return_value = _resp({"status": "OK", "data": []}, method="GET")
    _client(session).wait_for_indexing("doi:10.70112/ABC", timeout=5, interval=0.01)  # returns (no raise)


def test_file_checksums_parses_native_checksums() -> None:
    session = MagicMock()
    session.get.return_value = _resp({
        "data": {"files": [{"dataFile": {"id": 7, "filename": "X.parquet", "checksum": {"type": "MD5", "value": "abc"}}}]}
    })
    out = _client(session).file_checksums("doi:10.70112/ABC")
    assert out["X.parquet"] == {"type": "MD5", "value": "abc", "file_id": 7}


def test_error_is_token_free() -> None:
    session = MagicMock()
    session.post.return_value = _resp({"message": "bad"}, ok=False, status=400)
    with pytest.raises(DataverseError) as excinfo:
        _client(session, token="SUPER-SECRET").publish_dataset("doi:10.70112/ABC")
    assert "SUPER-SECRET" not in str(excinfo.value)


def test_no_token_means_no_auth_header() -> None:
    session = MagicMock()
    session.get.return_value = _resp({"data": {"files": []}}, method="GET")
    _client(session, token=None).get_version("doi:10.70112/ABC")
    assert session.get.call_args.kwargs["headers"] == {}


def test_dataset_metadata_maps_authors_license_and_validates_subjects() -> None:
    meta = dataset_metadata(
        title="Corn",
        description="desc",
        authors=[{"name": "Doe", "affiliation": "CIRAD", "orcid": "0000-0002-1825-0097"}],
        contact_email="a@b.c",
        subjects=["Chemistry"],
        keywords=["nir"],
        license={"name": "CC BY 4.0", "uri": "http://creativecommons.org/licenses/by/4.0"},
    )
    dsv = meta["datasetVersion"]
    by_name = {f["typeName"]: f for f in dsv["metadataBlocks"]["citation"]["fields"]}
    assert by_name["title"]["value"] == "Corn"
    assert by_name["author"]["value"][0]["authorIdentifier"]["value"] == "0000-0002-1825-0097"
    assert dsv["license"]["name"] == "CC BY 4.0"

    with pytest.raises(ValueError):
        dataset_metadata(title="x", description="d", authors=[{"name": "A"}], contact_email="a@b.c", subjects=["Nonsense"])
