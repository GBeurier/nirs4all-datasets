"""Render an MLCommons Croissant 1.0 (JSON-LD) description from a descriptor + its card.

Pragmatic mapping for spectra: the spectrum is a single array-valued ``cr:Field`` (not one field
per wavelength), plus one field per target. Pure descriptor/card -> dict (no nirs4all). Validate
strictly with ``mlcroissant`` downstream if desired.
"""
from __future__ import annotations

from typing import Any

from nirs4all_datasets.schema import DatasetDescriptor

_CONTEXT: dict[str, Any] = {
    "@language": "en",
    "@vocab": "https://schema.org/",
    "citeAs": "cr:citeAs",
    "column": "cr:column",
    "conformsTo": "dct:conformsTo",
    "cr": "http://mlcommons.org/croissant/",
    "data": {"@id": "cr:data", "@type": "@json"},
    "dataType": {"@id": "cr:dataType", "@type": "@vocab"},
    "dct": "http://purl.org/dc/terms/",
    "extract": "cr:extract",
    "field": "cr:field",
    "fileObject": "cr:fileObject",
    "fileProperty": "cr:fileProperty",
    "format": "cr:format",
    "includes": "cr:includes",
    "isLiveDataset": "cr:isLiveDataset",
    "key": "cr:key",
    "md5": "cr:md5",
    "parentField": "cr:parentField",
    "path": "cr:path",
    "recordSet": "cr:recordSet",
    "references": "cr:references",
    "repeated": "cr:repeated",
    "sc": "https://schema.org/",
    "sha256": "sha256",
    "source": "cr:source",
    "subField": "cr:subField",
}

_TASK_DATATYPE = {
    "regression": "sc:Float",
    "binary_classification": "sc:Integer",
    "multiclass_classification": "sc:Integer",
}


def render_croissant(descriptor: DatasetDescriptor, card: dict[str, Any], *, files: list[tuple[str, str | None, int | None]] | None = None, instance: str | None = None) -> dict[str, Any]:
    """Return a Croissant 1.0 JSON-LD dict for a dataset.

    ``files`` is an ordered list of ``(filename, sha256, dataverse_file_id)``. When a file id and
    ``instance`` are available, ``FileObject.contentUrl`` points at the actual file bytes (the
    Dataverse access API), not the DOI landing page (which is the dataset-level ``url``). Fields
    are sourced from the X (spectrum) and Y (targets) file objects so the record set is actionable.
    """
    inst = instance or descriptor.dataverse.instance
    doi = descriptor.dataverse.doi
    landing = f"https://doi.org/{doi}" if doi else inst

    creators = []
    for author in (descriptor.datacite.authors if descriptor.datacite else []):
        person: dict[str, Any] = {"@type": "sc:Person", "name": author.name}
        if author.orcid:
            person["sameAs"] = f"https://orcid.org/{author.orcid}"
        if author.affiliation:
            person["affiliation"] = author.affiliation
        creators.append(person)

    distribution: list[dict[str, Any]] = []
    x_id: str | None = None
    y_id: str | None = None
    for filename, sha, file_id in (files or []):
        file_object: dict[str, Any] = {"@type": "cr:FileObject", "@id": filename, "name": filename, "encodingFormat": "application/vnd.apache.parquet"}
        if sha:
            file_object["sha256"] = sha
        if file_id is not None:
            file_object["contentUrl"] = f"{inst}/api/access/datafile/{file_id}"
        distribution.append(file_object)
        if x_id is None and filename.startswith("X"):
            x_id = filename
        if y_id is None and filename.startswith("Y"):
            y_id = filename

    spectrum: dict[str, Any] = {
        "@type": "cr:Field", "@id": "records/spectrum", "name": "spectrum",
        "description": "Spectral intensities across the wavelength axis.", "dataType": "sc:Float", "repeated": True,
    }
    if x_id:
        spectrum["source"] = {"fileObject": {"@id": x_id}}
    fields: list[dict[str, Any]] = [spectrum]
    for target in descriptor.targets:
        field: dict[str, Any] = {
            "@type": "cr:Field", "@id": f"records/{target.name}", "name": target.name,
            "description": f"Target '{target.name}' ({target.task_type.value}).",
            "dataType": _TASK_DATATYPE.get(target.task_type.value, "sc:Text"),
        }
        if y_id:
            field["source"] = {"fileObject": {"@id": y_id}, "extract": {"column": target.name}}
        fields.append(field)

    return {
        "@context": _CONTEXT,
        "@type": "sc:Dataset",
        "conformsTo": "http://mlcommons.org/croissant/1.0",
        "name": descriptor.id,
        "description": descriptor.description,
        "version": descriptor.version,
        "license": descriptor.governance.license,
        "url": landing,
        "citeAs": descriptor.citation,
        "keywords": descriptor.keywords,
        "creator": creators,
        "distribution": distribution,
        "recordSet": [
            {
                "@type": "cr:RecordSet", "@id": "records", "name": "records",
                "description": f"One record per spectrum ({(card.get('inventory') or {}).get('n_samples')} samples).",
                "field": fields,
            }
        ],
    }
