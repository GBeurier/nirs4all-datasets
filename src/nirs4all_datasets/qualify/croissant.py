"""Render an MLCommons Croissant 1.0 (JSON-LD) description from a schema-2.0 card + descriptor.

The canonical layout is multi-source: one Parquet per X :class:`~nirs4all_datasets.schema.Source`
(spectra) plus an optional ``variables.parquet`` (Y/metadata). The mapping mirrors that:

* each ``sources[]`` Parquet -> a ``cr:FileObject``, and (when present) ``variables.parquet`` -> a
  ``cr:FileObject``;
* each source -> a ``cr:RecordSet`` with an array-valued ``spectrum`` field (the spectrum is one
  array-valued field, not one field per wavelength) keyed by ``sample_id``;
* each :class:`~nirs4all_datasets.schema.Variable` -> a ``cr:Field`` in a ``variables`` RecordSet,
  typed from its ``role``/``type``;
* ``origin_sources`` + ``publications`` -> ``citation``/``url``; ``tier`` -> ``license``/usage notes.

Pure card+descriptor -> dict (no nirs4all, no network). Validate strictly with ``mlcroissant``
downstream if desired.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
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

# Map a schema-2.0 VarType to a schema.org/Croissant dataType.
_VARTYPE_DATATYPE = {
    "numeric": "sc:Float",
    "categorical": "sc:Integer",
    "text": "sc:Text",
    "identifier": "sc:Text",
    "datetime": "sc:Date",
}
_PARQUET_FORMAT = "application/vnd.apache.parquet"

# Tier -> a short usage note appended to the dataset description (the SPDX license stays the legal fact).
_TIER_USAGE = {
    "public": "Open tier: freely usable and redistributable under the stated license.",
    "private": "Private tier: export requires an access token; not openly redistributable.",
    "anonymized": "Anonymized tier: variable names are masked and numeric targets are normalized (z-scored).",
}


def _creators(descriptor: DatasetDescriptor) -> list[dict[str, Any]]:
    """Map DataCite authors to schema.org Persons (empty when no DataCite block)."""
    creators: list[dict[str, Any]] = []
    for author in descriptor.datacite.authors if descriptor.datacite else []:
        person: dict[str, Any] = {"@type": "sc:Person", "name": author.name}
        if author.orcid:
            person["sameAs"] = f"https://orcid.org/{author.orcid}"
        if author.affiliation:
            person["affiliation"] = author.affiliation
        creators.append(person)
    return creators


def _file_objects(card: dict[str, Any], hashes: dict[str, str], inst: str, file_ids: dict[str, int]) -> tuple[list[dict[str, Any]], dict[str, str]]:
    """Build a FileObject per source Parquet (+ variables.parquet); return ``(objects, {source_id: file @id})``.

    ``hashes`` maps a canonical basename (``X1.parquet`` / ``variables.parquet``) to its SHA-256;
    ``file_ids`` maps it to a Dataverse file id, so ``contentUrl`` points at the file bytes when known.
    """
    objects: list[dict[str, Any]] = []
    source_file_id: dict[str, str] = {}

    def _emit(file_id: str, basename: str, name: str) -> None:
        obj: dict[str, Any] = {"@type": "cr:FileObject", "@id": file_id, "name": name, "encodingFormat": _PARQUET_FORMAT}
        sha = hashes.get(basename)
        if sha:
            obj["sha256"] = sha
        dv_id = file_ids.get(basename)
        if dv_id is not None:
            obj["contentUrl"] = f"{inst}/api/access/datafile/{dv_id}"
        objects.append(obj)

    for source in card.get("sources") or []:
        source_id = source.get("source_id")
        basename = f"{source_id}.parquet"
        file_id = f"file/{basename}"
        source_file_id[source_id] = file_id
        _emit(file_id, basename, source.get("name") or source_id)

    if card.get("variables"):
        _emit("file/variables.parquet", "variables.parquet", "variables")

    return objects, source_file_id


def _source_record_sets(card: dict[str, Any], source_file_id: dict[str, str]) -> list[dict[str, Any]]:
    """One RecordSet per source: a sample_id key field + an array-valued spectrum field."""
    record_sets: list[dict[str, Any]] = []
    for source in card.get("sources") or []:
        source_id = source.get("source_id")
        file_id = source_file_id.get(source_id)
        key_field: dict[str, Any] = {
            "@type": "cr:Field", "@id": f"{source_id}/sample_id", "name": "sample_id",
            "description": "Sample identity (join key across sources and variables).", "dataType": "sc:Text",
        }
        spectrum: dict[str, Any] = {
            "@type": "cr:Field", "@id": f"{source_id}/spectrum", "name": "spectrum",
            "description": f"Spectral intensities across the {source.get('axis_unit') or 'axis'} axis.",
            "dataType": "sc:Float", "repeated": True,
        }
        if file_id:
            key_field["source"] = {"fileObject": {"@id": file_id}, "extract": {"column": "sample_id"}}
            spectrum["source"] = {"fileObject": {"@id": file_id}}
        record_sets.append({
            "@type": "cr:RecordSet", "@id": source_id, "name": source_id,
            "description": f"Spectra from source '{source.get('name') or source_id}' ({source.get('n_observations')} observations x {source.get('n_variables')} wavelengths).",
            "key": {"@id": f"{source_id}/sample_id"},
            "field": [key_field, spectrum],
        })
    return record_sets


def _variables_record_set(card: dict[str, Any]) -> dict[str, Any] | None:
    """A single RecordSet over variables.parquet: one Field per Variable (typed by role/type)."""
    variables = card.get("variables") or []
    if not variables:
        return None
    key_field: dict[str, Any] = {
        "@type": "cr:Field", "@id": "variables/sample_id", "name": "sample_id",
        "description": "Sample identity (join key).", "dataType": "sc:Text",
        "source": {"fileObject": {"@id": "file/variables.parquet"}, "extract": {"column": "sample_id"}},
    }
    fields: list[dict[str, Any]] = [key_field]
    for var in variables:
        name = var.get("name")
        unit = f", unit {var['unit']}" if var.get("unit") else ""
        field: dict[str, Any] = {
            "@type": "cr:Field", "@id": f"variables/{name}", "name": name,
            "description": f"Variable '{name}' (role {var.get('role')}, type {var.get('type')}{unit}).",
            "dataType": _VARTYPE_DATATYPE.get(var.get("type"), "sc:Text"),
            "source": {"fileObject": {"@id": "file/variables.parquet"}, "extract": {"column": name}},
        }
        fields.append(field)
    return {
        "@type": "cr:RecordSet", "@id": "variables", "name": "variables",
        "description": "Per-sample target and metadata variables.",
        "key": {"@id": "variables/sample_id"},
        "field": fields,
    }


def render_croissant(card: dict[str, Any], descriptor: DatasetDescriptor, *, hashes: dict[str, str] | None = None, file_ids: dict[str, int] | None = None, instance: str | None = None) -> dict[str, Any]:
    """Return a Croissant 1.0 JSON-LD dict for a schema-2.0 dataset.

    Args:
        card: The built ``card.json`` (THE CARD JSON CONTRACT) — drives the distribution and record sets.
        descriptor: The dataset descriptor — supplies creators, origin sources, publications, citation.
        hashes: Optional ``{canonical_basename: sha256}`` (from the manifest) to stamp FileObjects.
        file_ids: Optional ``{canonical_basename: dataverse_file_id}`` to point ``contentUrl`` at bytes.
        instance: Dataverse instance base URL (defaults to the descriptor's).

    Returns:
        A Croissant 1.0 JSON-LD ``sc:Dataset`` dict (one FileObject per source Parquet + variables,
        one RecordSet per source plus a variables RecordSet).
    """
    inst = instance or descriptor.dataverse.instance
    doi = descriptor.dataverse.doi
    landing = f"https://doi.org/{doi}" if doi else inst

    identity = card.get("identity") or {}
    governance = card.get("governance") or {}
    tier = governance.get("tier") or identity.get("tier")
    description = identity.get("description") or descriptor.description
    usage = _TIER_USAGE.get(tier) if tier else None
    if usage:
        description = f"{description}\n\n{usage}"

    objects, source_file_id = _file_objects(card, hashes or {}, inst, file_ids or {})
    record_sets = _source_record_sets(card, source_file_id)
    variables_rs = _variables_record_set(card)
    if variables_rs is not None:
        record_sets.append(variables_rs)

    citation = descriptor.citation
    pubs_url = [pub.doi and f"https://doi.org/{pub.doi}" for pub in descriptor.publications if pub.doi]
    origin_url = [src.locator for src in descriptor.origin_sources if src.locator]

    return {
        "@context": _CONTEXT,
        "@type": "sc:Dataset",
        "conformsTo": "http://mlcommons.org/croissant/1.0",
        "name": identity.get("id") or descriptor.id,
        "description": description,
        "version": (card.get("versions") or {}).get("content") or descriptor.versions.content,
        "license": governance.get("license") or descriptor.governance.license,
        "url": landing,
        "sameAs": [u for u in (pubs_url + origin_url) if u],
        "citeAs": citation,
        "keywords": identity.get("keywords") or descriptor.keywords,
        "creator": _creators(descriptor),
        "distribution": objects,
        "recordSet": record_sets,
    }
