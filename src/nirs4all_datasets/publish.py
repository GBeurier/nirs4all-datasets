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
from nirs4all_datasets.schema import DatasetDescriptor

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
        raise NotImplementedError(f"dataset already has DOI {descriptor.dataverse.doi}; updating an existing dataset is a later phase.")

    dataset_dir = Path(dataset_dir)
    doi = client.create_dataset(collection, to_dataverse_metadata(descriptor, contact_email=contact_email, subjects=subjects))

    files = _payload_files(dataset_dir)
    for path, directory_label in files:
        client.upload_file(doi, path, tab_ingest=False, directory_label=directory_label or None)

    result = client.publish_dataset(doi, version_type=version_type)
    client.wait_for_indexing(doi)
    return {"doi": doi, "files": len(files), "version": result.get("versionNumber")}
