"""Publication to Dataverse: the governance gate, DataCite mapping, and orchestration.

Publishing is refused unless the descriptor's governance is complete and the data is not
confidential (see :meth:`DatasetDescriptor.publication_blockers`). Files are uploaded with
``tabIngest=false`` (preserving their sub-directory layout) and the whole version is published,
then we wait for indexing. Re-publishing an existing DOI (update/replace) is a later phase; this
orchestration only performs a first publication.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from nirs4all_datasets.dataverse import DataverseClient, dataset_metadata
from nirs4all_datasets.manifest import read_manifest, write_manifest
from nirs4all_datasets.schema import DatasetDescriptor, Tier


def _persistent_id(doi: str) -> str:
    """Dataverse API persistentId form (``doi:<suffix>``) from a bare or prefixed DOI."""
    return doi if doi.startswith("doi:") else f"doi:{doi}"

# SPDX -> Dataverse license object (open licences only; others inherit the collection default).
_LICENSE_MAP: dict[str, dict[str, str]] = {
    "CC0-1.0": {"name": "CC0 1.0", "uri": "http://creativecommons.org/publicdomain/zero/1.0"},
    "CC-BY-4.0": {"name": "CC BY 4.0", "uri": "http://creativecommons.org/licenses/by/4.0"},
    "CC-BY-SA-4.0": {"name": "CC BY-SA 4.0", "uri": "http://creativecommons.org/licenses/by-sa/4.0"},
}


class PublicationBlocked(RuntimeError):
    """Publication was refused by the governance gate."""


def assert_publishable(descriptor: DatasetDescriptor) -> None:
    """Raise :class:`PublicationBlocked` if the dataset must not be published."""
    blockers = descriptor.publication_blockers()
    if blockers:
        raise PublicationBlocked("dataset is not publishable:\n  - " + "\n  - ".join(blockers))


def to_dataverse_metadata(descriptor: DatasetDescriptor, *, contact_email: str, subjects: list[str] | None = None) -> dict[str, Any]:
    """Map a descriptor onto a Dataverse metadata payload (citation block + open license)."""
    if descriptor.datacite and descriptor.datacite.authors:
        authors = [{"name": a.name, "affiliation": a.affiliation, "orcid": a.orcid} for a in descriptor.datacite.authors]
    else:
        authors = [{"name": descriptor.governance.owner_steward or descriptor.provenance.contributor, "affiliation": None, "orcid": None}]
    return dataset_metadata(
        title=descriptor.name,
        description=descriptor.description,
        authors=authors,
        contact_email=contact_email,
        subjects=subjects or ["Other"],
        keywords=descriptor.keywords or None,
        license=_LICENSE_MAP.get(descriptor.governance.license),
    )


def _payload_files(dataset_dir: Path) -> list[tuple[Path, str]]:
    """Return (file, directory_label) pairs for canonical then raw files (label preserves layout)."""
    pairs: list[tuple[Path, str]] = []
    for sub in ("canonical", "raw"):
        root = dataset_dir / sub
        if not root.exists():
            continue
        for path in sorted(p for p in root.rglob("*") if p.is_file()):
            pairs.append((path, str(path.parent.relative_to(dataset_dir))))
    return pairs


def publish_dataset(
    descriptor: DatasetDescriptor,
    dataset_dir: str | Path,
    client: DataverseClient,
    *,
    collection: str,
    contact_email: str,
    subjects: list[str] | None = None,
    version_type: str = "major",
) -> dict[str, Any]:
    """Create, upload, and publish a dataset on Dataverse (first publication only).

    Returns ``{"doi", "files", "version"}``. Raises :class:`PublicationBlocked` if governance is
    incomplete, and ``NotImplementedError`` if the descriptor already has a DOI (update is a later phase).
    """
    assert_publishable(descriptor)
    if descriptor.dataverse.doi is not None:
        raise NotImplementedError(f"dataset already has DOI {descriptor.dataverse.doi}; use update_dataset() to publish a new version.")

    dataset_dir = Path(dataset_dir)
    restrict = descriptor.tier is not Tier.PUBLIC  # private/anonymized -> access-gated files
    doi = client.create_dataset(collection, to_dataverse_metadata(descriptor, contact_email=contact_email, subjects=subjects))

    files = _payload_files(dataset_dir)
    for path, directory_label in files:
        client.upload_file(doi, path, tab_ingest=False, directory_label=directory_label or None, restrict=restrict)

    result = client.publish_dataset(doi, version_type=version_type)
    client.wait_for_indexing(doi)
    return {"doi": doi, "files": len(files), "version": result.get("versionNumber")}


def update_dataset(
    descriptor: DatasetDescriptor,
    dataset_dir: str | Path,
    client: DataverseClient,
    *,
    version_type: str = "major",
) -> dict[str, Any]:
    """Publish a new version of an already-published dataset (replace changed files, add new ones).

    Requires ``descriptor.dataverse.doi``. Canonical/raw files present on Dataverse are replaced in
    place (so file ids stay stable); files not yet on Dataverse are added. Returns ``{"doi","files","version"}``.
    """
    assert_publishable(descriptor)
    if descriptor.dataverse.doi is None:
        raise ValueError("update_dataset requires descriptor.dataverse.doi (use publish_dataset for the first publication).")

    dataset_dir = Path(dataset_dir)
    pid = _persistent_id(descriptor.dataverse.doi)
    restrict = descriptor.tier is not Tier.PUBLIC
    existing = client.file_checksums(pid)  # filename -> {type, value, file_id}

    files = _payload_files(dataset_dir)
    for path, directory_label in files:
        info = existing.get(path.name)
        if info and info.get("file_id") is not None:
            client.replace_file(int(info["file_id"]), path, tab_ingest=False, directory_label=directory_label or None, restrict=restrict)
        else:
            client.upload_file(pid, path, tab_ingest=False, directory_label=directory_label or None, restrict=restrict)

    result = client.publish_dataset(pid, version_type=version_type)
    client.wait_for_indexing(pid)
    return {"doi": descriptor.dataverse.doi, "files": len(files), "version": result.get("versionNumber")}


def record_publication(dataset_dir: str | Path, client: DataverseClient, doi: str, dataset_version: Any) -> None:
    """Refresh the manifest after (re)publication: record Dataverse file ids + native checksums + version.

    This is what makes private/restricted access work: ``access.fetch_private`` downloads by the file
    ids recorded here (with a permitted token). No-op if there is no manifest.
    """
    manifest_path = Path(dataset_dir) / "manifest.json"
    if not manifest_path.exists():
        return
    manifest = read_manifest(manifest_path)
    checks = client.file_checksums(_persistent_id(doi))
    for entry in manifest.files:
        info = checks.get(Path(entry.path).name)
        if not info:
            continue
        if info.get("file_id") is not None:
            entry.file_id = int(info["file_id"])
        if info.get("type") and info.get("value"):
            entry.native_checksum_type = str(info["type"])
            entry.native_checksum = str(info["value"])
    manifest.doi = doi[4:] if doi.startswith("doi:") else doi
    if dataset_version is not None:
        manifest.dataset_version = str(dataset_version)
    write_manifest(manifest, manifest_path)
