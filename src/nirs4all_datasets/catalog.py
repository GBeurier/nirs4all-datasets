"""Assemble the catalog index from descriptors + generated cards/manifests/health (schema 2.0).

The catalog (``catalog/datasets.yaml``) is a small, git-tracked index aggregating each descriptor
(``catalog/datasets/<id>.yaml``) with key fields from its generated card and manifest
(``datasets/<id>/card.json`` / ``manifest.json``) and the origin health report
(``catalog/health.json``). It is the source of truth for ``list``/``search`` and for the static site.
Building it is cheap (reads small YAML/JSON), so it is regenerated wholesale.

Staleness, not lies: a card/manifest whose ``processing_hash`` does not match the current descriptor is
treated as stale — its computed enrichment (counts, hashes, card protocol) is dropped and ``is_stale``
is set, so the index never advertises outdated facts for an edited descriptor.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from nirs4all_datasets.manifest import metadata_hash, processing_hash
from nirs4all_datasets.schema import DatasetDescriptor

SCHEMA_VERSION = "2.0"


def _read_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    return data


def descriptor_paths(root: str | Path) -> list[Path]:
    """All descriptor YAML files under ``<root>/catalog/datasets``."""
    return sorted((Path(root) / "catalog" / "datasets").glob("*.yaml"))


def _spectro_family(descriptor: DatasetDescriptor) -> str:
    """Honest spectroscopy family: the single source modality, or ``mixed`` when heterogeneous."""
    modalities = sorted({s.modality.value for s in descriptor.sources})
    return modalities[0] if len(modalities) == 1 else "mixed"


def catalog_entry(root: str | Path, descriptor: DatasetDescriptor, *, health: dict[str, Any] | None = None) -> dict[str, Any]:
    """Build one catalog index entry, enriched only by *fresh* card/manifest data + origin health.

    Multi-source and multi-Y aware: sources[], variables (targets + metadata), tier, both version axes,
    derived ``spectro_family``, and origin/health facts the site's whole-bank dataviz consumes.
    """
    data_dir = Path(root) / "datasets" / descriptor.id
    card = _read_json(data_dir / "card.json") or {}
    manifest = _read_json(data_dir / "manifest.json") or {}
    current = processing_hash(descriptor)
    current_meta = metadata_hash(descriptor)
    integ = card.get("integrity") or {}
    card_fresh = bool(card) and integ.get("processing_hash") == current
    manifest_fresh = bool(manifest) and manifest.get("processing_hash") == current
    card_meta_stale = bool(card) and "metadata_hash" in integ and integ.get("metadata_hash") != current_meta
    is_stale = (bool(card) and not card_fresh) or card_meta_stale or (bool(manifest) and not manifest_fresh)

    # Display fields come from the PUBLIC descriptor (masked name/targets/domain for the anonymized tier);
    # the integrity hashes above stay keyed to the real descriptor (the card/manifest were hashed from it).
    from nirs4all_datasets.qualify.anonymize import public_descriptor  # lazy: keeps `import catalog` light

    pub = public_descriptor(descriptor)
    alignment = card.get("alignment", {}) if card_fresh else {}
    targets = pub.targets
    metadata_vars = pub.metadata_variables
    n_features_total = sum(s.n_variables for s in pub.sources if s.n_variables is not None) or None

    entry: dict[str, Any] = {
        "id": pub.id,
        "name": pub.name,
        "domain": pub.domain,
        "tier": pub.tier.value,
        "license": pub.governance.license,
        "content_version": pub.versions.content,
        "schema_protocol": pub.versions.schema_protocol,
        "spectro_family": _spectro_family(pub),
        "modalities": sorted({s.modality.value for s in pub.sources}),
        "n_sources": len(pub.sources),
        "source_ids": [s.source_id for s in pub.sources],
        "n_features_total": n_features_total,
        "alignment_level": pub.alignment_level.value,
        "n_targets": len(targets),
        "targets": [t.name for t in targets],
        "n_metadata": len(metadata_vars),
        "has_split": bool(pub.splits),
        "splits": [s.name for s in pub.splits],
        "n_samples": alignment.get("n_samples"),
        "doi": pub.dataverse.doi,
        "origin_kinds": sorted({s.kind.value for s in pub.origin_sources}),
        "origin_access": sorted({s.access.value for s in pub.origin_sources}),
        "n_publications": len(pub.publications),
        "card_protocol": card.get("protocol_version") if card_fresh else None,
        "content_hash": integ.get("content_hash") if card_fresh else None,
        "processing_hash": current,
        "has_card": bool(card),
        "has_manifest": bool(manifest),
        "is_stale": is_stale,
        "publishable": not descriptor.publication_blockers(),
    }
    if health is not None:
        entry["health"] = health
    return entry


def _counter(values: Any) -> dict[str, int]:
    """Frequency map, ordered by descending count then key (stable for the site dataviz)."""
    out: dict[str, int] = {}
    for v in values:
        out[v] = out.get(v, 0) + 1
    return dict(sorted(out.items(), key=lambda kv: (-kv[1], kv[0])))


def _distribution(xs: list[int]) -> dict[str, int] | None:
    """min/median/max/total of a list of counts, or ``None`` when empty."""
    if not xs:
        return None
    s = sorted(xs)
    return {"min": s[0], "median": s[len(s) // 2], "max": s[-1], "total": sum(xs)}


def bank_summary(entries: list[dict[str, Any]]) -> dict[str, Any]:
    """Whole-bank (global) aggregate metrics over all catalog entries — powers the site's dataviz.

    Counts by tier / spectroscopy family / domain / license / origin kind, the #samples and
    #wavelengths distributions, and structural mixes (multi- vs single-source, with-target vs
    metadata-only, native split, degraded health). Pure aggregation of the per-dataset index.
    """
    return {
        "n_datasets": len(entries),
        "n_with_card": sum(1 for e in entries if e.get("has_card")),
        "n_stale": sum(1 for e in entries if e.get("is_stale")),
        "n_publishable": sum(1 for e in entries if e.get("publishable")),
        "n_multi_source": sum(1 for e in entries if (e.get("n_sources") or 0) > 1),
        "n_with_targets": sum(1 for e in entries if (e.get("n_targets") or 0) > 0),
        "n_metadata_only": sum(1 for e in entries if (e.get("n_targets") or 0) == 0),
        "n_with_split": sum(1 for e in entries if e.get("has_split")),
        "n_degraded": sum(1 for e in entries if (e.get("health") or {}).get("degraded")),
        "by_tier": _counter(e["tier"] for e in entries),
        "by_spectro_family": _counter(e["spectro_family"] for e in entries),
        "by_domain": _counter((e.get("domain") or "unknown") for e in entries),
        "license_mix": _counter(e["license"] for e in entries),
        "origin_kinds": _counter(k for e in entries for k in e.get("origin_kinds", [])),
        "samples": _distribution([e["n_samples"] for e in entries if e.get("n_samples")]),
        "features": _distribution([e["n_features_total"] for e in entries if e.get("n_features_total")]),
        "total_sources": sum(e.get("n_sources") or 0 for e in entries),
        "total_targets": sum(e.get("n_targets") or 0 for e in entries),
        "total_publications": sum(e.get("n_publications") or 0 for e in entries),
    }


def build_catalog(root: str | Path, *, write: bool = True) -> dict[str, Any]:
    """Assemble (and optionally write) ``catalog/datasets.yaml`` from all descriptors + health."""
    root = Path(root)
    health_map = (_read_json(root / "catalog" / "health.json") or {}).get("datasets", {})
    entries = [
        catalog_entry(root, DatasetDescriptor(**(yaml.safe_load(p.read_text(encoding="utf-8")) or {})), health=health_map.get(p.stem))
        for p in descriptor_paths(root)
    ]
    catalog = {"schema_version": SCHEMA_VERSION, "n_datasets": len(entries), "summary": bank_summary(entries), "datasets": entries}
    if write:
        (root / "catalog").mkdir(parents=True, exist_ok=True)
        (root / "catalog" / "datasets.yaml").write_text(yaml.safe_dump(catalog, sort_keys=False, allow_unicode=True), encoding="utf-8")
    return catalog


def load_catalog(root: str | Path) -> dict[str, Any]:
    """Read the assembled catalog index."""
    path = Path(root) / "catalog" / "datasets.yaml"
    if not path.exists():
        return {"schema_version": SCHEMA_VERSION, "n_datasets": 0, "datasets": []}
    result: dict[str, Any] = yaml.safe_load(path.read_text(encoding="utf-8"))
    return result


def search(root: str | Path, *, tier: str | None = None, domain: str | None = None, spectro_family: str | None = None, has_target: bool | None = None) -> list[dict[str, Any]]:
    """Filter catalog entries by tier, domain, spectroscopy family, and/or whether a target is declared."""
    entries: list[dict[str, Any]] = load_catalog(root).get("datasets", [])
    if tier is not None:
        entries = [e for e in entries if e.get("tier") == tier]
    if domain is not None:
        entries = [e for e in entries if e.get("domain") == domain]
    if spectro_family is not None:
        entries = [e for e in entries if e.get("spectro_family") == spectro_family]
    if has_target is not None:
        entries = [e for e in entries if (e.get("n_targets", 0) > 0) == has_target]
    return entries


def get_card(root: str | Path, dataset_id: str) -> dict[str, Any] | None:
    """Return a dataset's generated identity card, if present."""
    return _read_json(Path(root) / "datasets" / dataset_id / "card.json")
