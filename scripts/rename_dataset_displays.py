#!/usr/bin/env python3
"""Apply an audited display-name crosswalk without requalifying measured data.

Only descriptor.name, card.identity.name and card.integrity.metadata_hash change.
The existing Datasets renderers refresh the datasheet and Croissant views. Every
row is checked before any write; stale cards and unexpected current names fail.
"""
from __future__ import annotations

import argparse
import copy
import csv
import json
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

from nirs4all_datasets.catalog import build_catalog
from nirs4all_datasets.manifest import metadata_hash, processing_hash, read_manifest
from nirs4all_datasets.qualify import anonymize, croissant, datasheet
from nirs4all_datasets.qualify.profile import card_metadata_fresh
from nirs4all_datasets.schema import DatasetDescriptor


def plan_rename(path: Path, previous: str, name: str, dataset_dir: Path) -> dict[Path, str]:
    """Reject non-name drift and retain all existing measured/qualification sections."""
    text = path.read_text(encoding="utf-8")
    descriptor = DatasetDescriptor(**yaml.safe_load(text))
    if not name.strip() or name != name.strip() or any(c in name for c in "\r\n\t"):
        raise ValueError(f"{descriptor.id}: invalid display name")
    if descriptor.name not in {previous, name}:
        raise ValueError(f"{descriptor.id}: current name differs from both audited names")
    updated = descriptor.model_copy(update={"name": name})
    assert descriptor.model_dump(exclude={"name"}) == updated.model_dump(exclude={"name"})
    assert processing_hash(descriptor) == processing_hash(updated)
    outputs: dict[Path, str] = {}
    if descriptor.name != name:
        document = yaml.compose(text)
        assert isinstance(document, yaml.MappingNode)
        nodes = [value for key, value in document.value if key.value == "name"]
        if len(nodes) != 1:
            raise ValueError(f"{descriptor.id}: expected exactly one top-level name")
        node = nodes[0]
        # JSON quoted strings are valid YAML scalars. Preserve every other YAML byte.
        outputs[path] = text[:node.start_mark.index] + json.dumps(name, ensure_ascii=False) + text[node.end_mark.index:]
        parsed = DatasetDescriptor(**yaml.safe_load(outputs[path]))
        if parsed != updated:
            raise ValueError(f"{descriptor.id}: name-only YAML edit changed other fields")

    card_path = dataset_dir / "card.json"
    if not card_path.exists():
        if any((dataset_dir / p).exists() for p in ("card.md", "croissant.json", "manifest.json")):
            raise ValueError(f"{descriptor.id}: incomplete qualified artifact set")
        return outputs  # Descriptor-only candidates remain unqualified.
    card = json.loads(card_path.read_text(encoding="utf-8"))
    if not card_metadata_fresh(card_path, descriptor):
        raise ValueError(f"{descriptor.id}: stale metadata; refresh independently before renaming")
    if card["identity"]["id"] != descriptor.id or card["identity"]["name"] != descriptor.name:
        raise ValueError(f"{descriptor.id}: card identity disagrees with descriptor")
    manifest = read_manifest(dataset_dir / "manifest.json")
    if manifest.processing_hash != processing_hash(descriptor) or card["integrity"]["processing_hash"] != manifest.processing_hash:
        raise ValueError(f"{descriptor.id}: stale processing identity; rebuild independently before renaming")
    if descriptor.name == name:
        return outputs
    renamed = copy.deepcopy(card)
    renamed["identity"]["name"] = name
    renamed["integrity"]["metadata_hash"] = metadata_hash(updated)
    # Keep generated_at, numerical profiles, repetitions, content hashes and
    # producer provenance from the real qualification, without claiming a rebuild.
    outputs[card_path] = json.dumps(renamed, indent=2, sort_keys=True, allow_nan=False)
    public = anonymize.public_descriptor(updated)
    outputs[dataset_dir / "card.md"] = datasheet.render_datasheet(renamed, public)
    document = croissant.render_croissant(renamed, public, hashes=manifest.canonical_hashes, file_ids={}, instance=public.dataverse.instance)
    outputs[dataset_dir / "croissant.json"] = json.dumps(document, indent=2, sort_keys=True, allow_nan=False)
    return {p: value for p, value in outputs.items() if not p.exists() or p.read_text(encoding="utf-8") != value}


def apply_crosswalk(root: Path, mapping: Path, *, write: bool = False) -> dict[str, Any]:
    with mapping.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    by_id = {r["dataset_id"]: r for r in rows}
    if len(by_id) != len(rows) or not rows:
        raise ValueError("Crosswalk must have nonempty, unique dataset IDs")
    paths = {p.stem: p for p in (root / "catalog/datasets").glob("*.yaml")}
    if missing := set(by_id) - set(paths):
        raise ValueError(f"Crosswalk IDs missing from catalog: {sorted(missing)}")
    names = [by_id[identifier]["display_name"] if identifier in by_id else yaml.safe_load(p.read_text(encoding="utf-8"))["name"] for identifier, p in paths.items()]
    normalized = [" ".join(n.split()).casefold() for n in names]
    if len(set(normalized)) != len(normalized):
        raise ValueError("Proposed names are not unique across the full catalog")
    planned: dict[Path, str] = {}
    for identifier, row in by_id.items():
        planned.update(plan_rename(paths[identifier], row["previous_display_name"], row["display_name"], root / "datasets" / identifier))
    if write:
        for path, text in planned.items():
            path.write_text(text, encoding="utf-8")
        if planned:
            build_catalog(root, write=True)
    return {"datasets": len(rows), "changed_files_before_index": len(planned), "write": write}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPO)
    parser.add_argument("--mapping", type=Path, default=REPO / "catalog/documentation/dataset-display-names-20261105.csv")
    parser.add_argument("--write", action="store_true", help="Apply after validating every row; otherwise validate only")
    args = parser.parse_args()
    print(json.dumps(apply_crosswalk(args.root, args.mapping, write=args.write), indent=2))


if __name__ == "__main__":
    main()
