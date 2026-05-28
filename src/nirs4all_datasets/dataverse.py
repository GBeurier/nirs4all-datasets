"""Minimal Dataverse Native API client (plain REST via ``requests``).

Only what the registry needs: create a dataset, upload files (with ``tabIngest=false`` inside
the ``jsonData`` part so the canonical bytes are never mangled by tabular ingest), publish a
whole version, read a version's files + native checksums, wait for locks (ingest/indexing) to
clear, and delete a dirty draft.

The token travels only in the ``X-Dataverse-key`` header (never as a ``?key=`` query parameter,
never logged). A :class:`requests.Session` can be injected for testing without network.
"""
from __future__ import annotations

import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import requests

# Dataverse citation "subject" controlled vocabulary (validated before publish).
DATAVERSE_SUBJECTS = frozenset(
    {
        "Agricultural Sciences", "Arts and Humanities", "Astronomy and Astrophysics",
        "Business and Management", "Chemistry", "Computer and Information Science",
        "Earth and Environmental Sciences", "Engineering", "Law", "Mathematical Sciences",
        "Medicine, Health and Life Sciences", "Physics", "Social Sciences", "Other",
    }
)


class DataverseError(RuntimeError):
    """A Dataverse API call failed (message is token-free)."""


@dataclass
class DataverseClient:
    """Thin client for one Dataverse instance.

    Attributes:
        instance: Base URL (e.g. ``https://entrepot.recherche.data.gouv.fr``), no trailing slash.
        token: API token (only needed for writes and private reads).
        session: Optional injected :class:`requests.Session` (tests).
        timeout: Per-request timeout in seconds.
    """

    instance: str
    token: str | None = None
    session: requests.Session | None = None
    timeout: float = 60.0

    def _sess(self) -> requests.Session:
        return self.session if self.session is not None else requests.Session()

    def _headers(self) -> dict[str, str]:
        return {"X-Dataverse-key": self.token} if self.token else {}

    def _url(self, path: str) -> str:
        return f"{self.instance}{path}"

    def _data(self, resp: requests.Response, action: str) -> Any:
        """Return the API ``data`` payload (dict or list), raising a token-free error on failure."""
        if not resp.ok:
            raise DataverseError(f"{action} failed: HTTP {resp.status_code} {resp.reason} for {resp.request.method} {resp.url.split('?', 1)[0]}")
        payload = resp.json()
        return payload.get("data", payload) if isinstance(payload, dict) else payload

    def _data_dict(self, resp: requests.Response, action: str) -> dict[str, Any]:
        data = self._data(resp, action)
        if not isinstance(data, dict):
            raise DataverseError(f"{action}: unexpected non-object response.")
        return data

    def create_dataset(self, collection: str, metadata: dict[str, Any]) -> str:
        """Create a draft dataset in ``collection``; return its persistent id (DOI)."""
        resp = self._sess().post(self._url(f"/api/dataverses/{collection}/datasets"), headers=self._headers(), json=metadata, timeout=self.timeout)
        return str(self._data_dict(resp, "create_dataset")["persistentId"])

    def upload_file(self, doi: str, path: str | Path, *, tab_ingest: bool = False, description: str | None = None, directory_label: str | None = None, restrict: bool = False) -> dict[str, Any]:
        """Upload one file to a dataset draft. ``tab_ingest=False`` (default) keeps bytes pristine.

        File metadata (``tabIngest``, ``restrict``, ``description``, ``directoryLabel``) goes in the
        ``jsonData`` multipart part, as Dataverse requires; ``directory_label`` preserves sub-directory
        structure; ``restrict=True`` marks the file access-restricted (download needs a permitted token).
        """
        path = Path(path)
        metadata: dict[str, str] = {"tabIngest": "true" if tab_ingest else "false"}
        if restrict:
            metadata["restrict"] = "true"
        if description:
            metadata["description"] = description
        if directory_label:
            metadata["directoryLabel"] = directory_label
        with path.open("rb") as fh:
            resp = self._sess().post(
                self._url("/api/datasets/:persistentId/add"),
                params={"persistentId": doi},
                headers=self._headers(),
                files={"file": (path.name, fh)},
                data={"jsonData": json.dumps(metadata)},
                timeout=self.timeout,
            )
        return self._data_dict(resp, "upload_file")

    def replace_file(self, file_id: int, path: str | Path, *, tab_ingest: bool = False, directory_label: str | None = None, restrict: bool = False) -> dict[str, Any]:
        """Replace an existing datafile's content (creates a new draft version on publish).

        ``file_id`` is the current Dataverse datafile id; ``forceReplace`` allows a differing content
        type. Used by the versioned-update flow to re-upload changed canonical bytes in place.
        """
        path = Path(path)
        metadata: dict[str, str] = {"forceReplace": "true", "tabIngest": "true" if tab_ingest else "false"}
        if restrict:
            metadata["restrict"] = "true"
        if directory_label:
            metadata["directoryLabel"] = directory_label
        with path.open("rb") as fh:
            resp = self._sess().post(
                self._url(f"/api/files/{file_id}/replace"),
                headers=self._headers(),
                files={"file": (path.name, fh)},
                data={"jsonData": json.dumps(metadata)},
                timeout=self.timeout,
            )
        return self._data_dict(resp, "replace_file")

    def restrict_file(self, file_id: int, restrict: bool = True) -> None:
        """Restrict (or, with ``restrict=False``, un-restrict) a published/draft datafile."""
        resp = self._sess().put(
            self._url(f"/api/files/{file_id}/restrict"),
            headers=self._headers(),
            data="true" if restrict else "false",
            timeout=self.timeout,
        )
        if not resp.ok:
            raise DataverseError(f"restrict_file failed: HTTP {resp.status_code} {resp.reason}")

    def dataset_db_id(self, doi: str) -> int:
        """Return the numeric database id of a dataset (needed by the role-assignment endpoints)."""
        resp = self._sess().get(self._url("/api/datasets/:persistentId/"), params={"persistentId": doi}, headers=self._headers(), timeout=self.timeout)
        return int(self._data_dict(resp, "dataset_db_id")["id"])

    def assign_role(self, dataset_db_id: int, assignee: str, role: str) -> dict[str, Any]:
        """Grant ``role`` on a dataset to ``assignee`` (``@user`` or ``&group``). Returns the assignment."""
        resp = self._sess().post(
            self._url(f"/api/datasets/{dataset_db_id}/assignments"),
            headers=self._headers(),
            json={"assignee": assignee, "role": role},
            timeout=self.timeout,
        )
        return self._data_dict(resp, "assign_role")

    def list_assignments(self, dataset_db_id: int) -> list[dict[str, Any]]:
        """List role assignments on a dataset (each has ``id``, ``assignee``, ``_roleAlias``)."""
        resp = self._sess().get(self._url(f"/api/datasets/{dataset_db_id}/assignments"), headers=self._headers(), timeout=self.timeout)
        data = self._data(resp, "list_assignments")
        return data if isinstance(data, list) else []

    def delete_assignment(self, dataset_db_id: int, assignment_id: int) -> None:
        """Revoke a role assignment by its id."""
        resp = self._sess().delete(self._url(f"/api/datasets/{dataset_db_id}/assignments/{assignment_id}"), headers=self._headers(), timeout=self.timeout)
        if not resp.ok:
            raise DataverseError(f"delete_assignment failed: HTTP {resp.status_code} {resp.reason}")

    def publish_dataset(self, doi: str, *, version_type: str = "major") -> dict[str, Any]:
        """Publish the dataset's draft as a whole version (``major`` or ``minor``)."""
        resp = self._sess().post(
            self._url("/api/datasets/:persistentId/actions/:publish"),
            params={"persistentId": doi, "type": version_type},
            headers=self._headers(),
            timeout=self.timeout,
        )
        return self._data_dict(resp, "publish_dataset")

    def get_version(self, doi: str, version: str = ":latest-published") -> dict[str, Any]:
        """Return a dataset version (use ``:latest-published``, ``:draft`` or ``x.y``)."""
        resp = self._sess().get(
            self._url(f"/api/datasets/:persistentId/versions/{version}"),
            params={"persistentId": doi},
            headers=self._headers(),
            timeout=self.timeout,
        )
        return self._data_dict(resp, "get_version")

    def file_checksums(self, doi: str, version: str = ":latest-published") -> dict[str, dict[str, Any]]:
        """Map filename -> {type, value, file_id} from a version's native checksums."""
        data = self.get_version(doi, version)
        out: dict[str, dict[str, Any]] = {}
        for entry in data.get("files", []):
            datafile = entry.get("dataFile", {})
            checksum = datafile.get("checksum", {})
            out[datafile.get("filename", entry.get("label", ""))] = {
                "type": checksum.get("type"),
                "value": checksum.get("value"),
                "file_id": datafile.get("id"),
            }
        return out

    def wait_for_indexing(self, doi: str, *, timeout: float = 180.0, interval: float = 3.0) -> None:
        """Block until the dataset has no active locks (``/locks`` returns an empty list)."""
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            resp = self._sess().get(self._url("/api/datasets/:persistentId/locks"), params={"persistentId": doi}, headers=self._headers(), timeout=self.timeout)
            if resp.ok and not self._data(resp, "locks"):
                return
            time.sleep(interval)
        raise DataverseError(f"dataset {doi} still locked after {timeout}s")

    def delete_draft(self, doi: str) -> None:
        """Delete a dataset's draft version (cleanup after a failed publish). No-op if absent."""
        resp = self._sess().delete(self._url("/api/datasets/:persistentId/versions/:draft"), params={"persistentId": doi}, headers=self._headers(), timeout=self.timeout)
        if not resp.ok and resp.status_code != 404:
            raise DataverseError(f"delete_draft failed: HTTP {resp.status_code} {resp.reason}")


def dataset_metadata(
    *,
    title: str,
    description: str,
    authors: list[dict[str, str | None]],
    contact_email: str,
    subjects: list[str],
    keywords: list[str] | None = None,
    license: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Build a Dataverse dataset metadata payload (citation block + optional license).

    ``authors`` items use ``{name, affiliation, orcid}``. ``subjects`` must be in
    :data:`DATAVERSE_SUBJECTS` (validated here so failures happen before any network call).
    """
    invalid = [s for s in subjects if s not in DATAVERSE_SUBJECTS]
    if invalid:
        raise ValueError(f"subjects not in Dataverse controlled vocabulary: {invalid}")

    author_fields = []
    for author in authors:
        value: dict[str, Any] = {"authorName": {"typeName": "authorName", "multiple": False, "typeClass": "primitive", "value": author["name"]}}
        if author.get("affiliation"):
            value["authorAffiliation"] = {"typeName": "authorAffiliation", "multiple": False, "typeClass": "primitive", "value": author["affiliation"]}
        if author.get("orcid"):
            value["authorIdentifierScheme"] = {"typeName": "authorIdentifierScheme", "multiple": False, "typeClass": "controlledVocabulary", "value": "ORCID"}
            value["authorIdentifier"] = {"typeName": "authorIdentifier", "multiple": False, "typeClass": "primitive", "value": author["orcid"]}
        author_fields.append(value)

    fields: list[dict[str, Any]] = [
        {"typeName": "title", "multiple": False, "typeClass": "primitive", "value": title},
        {"typeName": "author", "multiple": True, "typeClass": "compound", "value": author_fields},
        {
            "typeName": "datasetContact", "multiple": True, "typeClass": "compound",
            "value": [{"datasetContactEmail": {"typeName": "datasetContactEmail", "multiple": False, "typeClass": "primitive", "value": contact_email}}],
        },
        {
            "typeName": "dsDescription", "multiple": True, "typeClass": "compound",
            "value": [{"dsDescriptionValue": {"typeName": "dsDescriptionValue", "multiple": False, "typeClass": "primitive", "value": description}}],
        },
        {"typeName": "subject", "multiple": True, "typeClass": "controlledVocabulary", "value": subjects},
    ]
    if keywords:
        fields.append({
            "typeName": "keyword", "multiple": True, "typeClass": "compound",
            "value": [{"keywordValue": {"typeName": "keywordValue", "multiple": False, "typeClass": "primitive", "value": kw}} for kw in keywords],
        })
    dataset_version: dict[str, Any] = {"metadataBlocks": {"citation": {"displayName": "Citation Metadata", "fields": fields}}}
    if license:
        dataset_version["license"] = license
    return {"datasetVersion": dataset_version}
