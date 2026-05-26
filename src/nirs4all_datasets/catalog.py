"""Assemble the catalog index from descriptors + generated cards/manifests.

The catalog (``catalog/datasets.yaml``) is a small, git-tracked index aggregating each
descriptor (``catalog/datasets/<id>.yaml``) with key fields from its generated card and manifest
(``datasets/<id>/card.json`` / ``manifest.json``). It is the source of truth for ``list``/``search``
and for the static site. Building it is cheap (reads small YAML/JSON), so it is regenerated wholesale.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from nirs4all_datasets.manifest import descriptor_hash
from nirs4all_datasets.schema import DatasetDescriptor

SCHEMA_VERSION = "1.0"


def _read_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    return data


def descriptor_paths(root: str | Path) -> list[Path]:
    """All descriptor YAML files under ``<root>/catalog/datasets``."""
    return sorted((Path(root) / "catalog" / "datasets").glob("*.yaml"))


def catalog_entry(root: str | Path, descriptor: DatasetDescriptor) -> dict[str, Any]:
    """Build one catalog index entry, enriched only by *fresh* card/manifest data.

    A card/manifest whose ``descriptor_hash`` does not match the current descriptor is treated as
    stale: its enrichment (counts, signal type, hashes) is ignored and ``is_stale`` is set, so the
    catalog never advertises outdated provenance for an edited descriptor.
    """
    data_dir = Path(root) / "datasets" / descriptor.id
    card = _read_json(data_dir / "card.json") or {}
    manifest = _read_json(data_dir / "manifest.json") or {}
    current = descriptor_hash(descriptor)
    card_fresh = bool(card) and (card.get("integrity") or {}).get("descriptor_hash") == current
    manifest_fresh = bool(manifest) and manifest.get("descriptor_hash") == current
    is_stale = (bool(card) and not card_fresh) or (bool(manifest) and not manifest_fresh)

    inventory = card.get("inventory", {}) if card_fresh else {}
    return {
        "id": descriptor.id,
        "name": descriptor.name,
        "version": descriptor.version,
        "domain": descriptor.domain,
        "visibility": descriptor.governance.visibility.value,
        "license": descriptor.governance.license,
        "task_type": descriptor.targets[0].task_type.value,
        "targets": [t.name for t in descriptor.targets],
        "doi": descriptor.dataverse.doi,
        "n_samples": inventory.get("n_samples", descriptor.n_samples),
        "n_features": inventory.get("n_features", descriptor.n_features),
        "signal_type": card.get("spectral", {}).get("signal_type") if card_fresh else None,
        "content_hash": (card.get("integrity") or {}).get("content_hash") if card_fresh else None,
        "descriptor_hash": current,
        "has_card": bool(card),
        "has_manifest": bool(manifest),
        "is_stale": is_stale,
        "publishable": not descriptor.publication_blockers(),
    }


def build_catalog(root: str | Path, *, write: bool = True) -> dict[str, Any]:
    """Assemble (and optionally write) ``catalog/datasets.yaml`` from all descriptors."""
    root = Path(root)
    entries = [catalog_entry(root, DatasetDescriptor(**(yaml.safe_load(p.read_text(encoding="utf-8")) or {}))) for p in descriptor_paths(root)]
    catalog = {"schema_version": SCHEMA_VERSION, "n_datasets": len(entries), "datasets": entries}
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


def search(root: str | Path, *, task_type: str | None = None, visibility: str | None = None, signal_type: str | None = None) -> list[dict[str, Any]]:
    """Filter catalog entries by task type, visibility, and/or signal type."""
    entries: list[dict[str, Any]] = load_catalog(root).get("datasets", [])
    if task_type is not None:
        entries = [e for e in entries if e.get("task_type") == task_type]
    if visibility is not None:
        entries = [e for e in entries if e.get("visibility") == visibility]
    if signal_type is not None:
        entries = [e for e in entries if e.get("signal_type") == signal_type]
    return entries


def get_card(root: str | Path, dataset_id: str) -> dict[str, Any] | None:
    """Return a dataset's generated identity card, if present."""
    return _read_json(Path(root) / "datasets" / dataset_id / "card.json")
