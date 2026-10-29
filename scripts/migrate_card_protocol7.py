"""Explicitly migrate stored legacy card metadata to protocol 7, preserving raw calculations.

No canonical payload, descriptor, source variable or numerical kernel is rebuilt.
Historical raw values retain their original protocol; only signatures, names and
provenance are migrated, followed by deterministic metadata export rendering.
"""
from __future__ import annotations

import argparse
import json
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

import yaml

from nirs4all_datasets.catalog import build_catalog
from nirs4all_datasets.manifest import read_manifest
from nirs4all_datasets.qualify import anonymize, croissant, datasheet, metrics
from nirs4all_datasets.qualify.profile import write_card
from nirs4all_datasets.schema import DatasetDescriptor


def migrate_card(card: dict[str, Any]) -> dict[str, Any]:
    """Return a deterministic metadata migration; never mutate the supplied old card."""
    version = card.get("protocol_version")
    if version not in {"6", "7"}:
        raise ValueError("explicit card migration supports only protocol 6 or 7")
    provenance = card.get("qualification_provenance") or {}
    if card.get("assessment_mode", provenance.get("assessment_mode", "legacy")) != "legacy":
        raise ValueError("shared assessment cards require their own source/protocol context")
    result = deepcopy(card)
    for source in result.get("sources", []):
        profile = (source.get("spectral") or {}).get("profile")
        if isinstance(profile, dict):
            source["spectral"]["profile"] = metrics.migrate_profile_metadata(profile, from_protocol=version)
    result["protocol_version"] = "7"
    result["qualification_provenance"] = {
        "assessment_mode": "legacy",
        "legacy_calculation_protocol": provenance.get("legacy_calculation_protocol", version),
        "diagnostic_domain": None,
        "interpretation": "uncalibrated_heuristic_signature",
        "migration": {"from_protocol": (provenance.get("migration") or {}).get("from_protocol", version), "to_protocol": "7", "raw_kernels_recomputed": False},
    }
    return result


def migrate_tree(root: Path) -> list[str]:
    """Migrate tracked JSON cards and re-render their existing metadata export surfaces."""
    changed = []
    for path in sorted((root / "datasets").glob("*/card.json")):
        original = json.loads(path.read_text(encoding="utf-8"))
        migrated = migrate_card(original)
        if original == migrated:
            continue
        descriptor = DatasetDescriptor(**yaml.safe_load((root / "catalog/datasets" / f"{path.parent.name}.yaml").read_text(encoding="utf-8")))
        public_descriptor = anonymize.public_descriptor(descriptor)
        write_card(migrated, path)
        (path.parent / "card.md").write_text(datasheet.render_datasheet(migrated, public_descriptor), encoding="utf-8")
        manifest = read_manifest(path.parent / "manifest.json")
        (path.parent / "croissant.json").write_text(json.dumps(croissant.render_croissant(migrated, public_descriptor, hashes=manifest.canonical_hashes), sort_keys=True, indent=2), encoding="utf-8")
        changed.append(path.parent.name)
    build_catalog(root)
    return changed


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPO)
    arguments = parser.parse_args()
    print(f"Migrated {len(migrate_tree(arguments.root.resolve()))} cards; raw kernels and canonical bytes unchanged")
