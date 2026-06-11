#!/usr/bin/env python3
"""Validate catalog descriptors, subsets, and manifests against the schema.

CI gate (mirrors ``nirs4all-methods/catalog/scripts/validate.py``):

* every ``catalog/datasets/<id>.yaml`` parses as a :class:`DatasetDescriptor` whose
  ``id`` matches its filename and is unique;
* every ``subsets/<id>.yaml`` parses and references a known parent;
* every ``cards/<id>/manifest.json`` (if present) parses as a :class:`Manifest`.

Usage::

    python catalog/scripts/validate.py                  # schema validity (default)
    python catalog/scripts/validate.py --check           # alias of the default
    python catalog/scripts/validate.py --check-publish    # also require public/embargo datasets to be publishable
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "src"))

import yaml  # noqa: E402
from pydantic import ValidationError  # noqa: E402

from nirs4all_datasets.schema import DatasetDescriptor, Manifest, Subset, Tier  # noqa: E402


def _load_yaml(path: Path) -> dict[str, object]:
    with path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: top-level YAML must be a mapping.")
    return data


def validate_descriptors(root: Path, *, check_publish: bool) -> tuple[dict[str, DatasetDescriptor], list[str]]:
    """Validate all descriptors. Return (id -> descriptor, error messages)."""
    errors: list[str] = []
    found: dict[str, DatasetDescriptor] = {}
    for path in sorted((root / "catalog" / "datasets").glob("*.yaml")):
        try:
            descriptor = DatasetDescriptor(**_load_yaml(path))
        except (ValidationError, ValueError) as exc:
            errors.append(f"{path.name}: {exc}")
            continue
        if descriptor.id != path.stem:
            errors.append(f"{path.name}: id {descriptor.id!r} does not match filename stem {path.stem!r}.")
        if descriptor.id in found:
            errors.append(f"{path.name}: duplicate dataset id {descriptor.id!r}.")
        found[descriptor.id] = descriptor
        if check_publish and descriptor.tier is Tier.PUBLIC:
            for blocker in descriptor.publication_blockers():
                errors.append(f"{path.name}: not publishable: {blocker}")
    return found, errors


def validate_subsets(root: Path, known_ids: set[str]) -> list[str]:
    """Validate all subset definitions against their parents."""
    errors: list[str] = []
    sdir = root / "subsets"
    if not sdir.exists():
        return errors
    for path in sorted(sdir.glob("*.yaml")):
        try:
            subset = Subset(**_load_yaml(path))
        except (ValidationError, ValueError) as exc:
            errors.append(f"{path.name}: {exc}")
            continue
        if subset.id != path.stem:
            errors.append(f"{path.name}: id {subset.id!r} does not match filename stem {path.stem!r}.")
        if subset.parent not in known_ids:
            errors.append(f"{path.name}: parent {subset.parent!r} is not a known dataset.")
    return errors


def validate_manifests(root: Path, known_ids: set[str]) -> list[str]:
    """Validate any committed dataset manifests."""
    errors: list[str] = []
    datasets = root / "datasets"
    if not datasets.exists():
        return errors
    for path in sorted(datasets.glob("*/manifest.json")):
        try:
            manifest = Manifest(**json.loads(path.read_text(encoding="utf-8")))
        except (ValidationError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"{path.parent.name}/manifest.json: {exc}")
            continue
        if manifest.dataset_id not in known_ids:
            errors.append(f"{path.parent.name}/manifest.json: dataset_id {manifest.dataset_id!r} is unknown.")
    return errors


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="alias of the default run")
    parser.add_argument("--check-publish", action="store_true", help="also require public/embargo datasets to be publishable")
    args = parser.parse_args(argv)

    descriptors, errors = validate_descriptors(REPO, check_publish=args.check_publish)
    errors += validate_subsets(REPO, set(descriptors))
    errors += validate_manifests(REPO, set(descriptors))

    if errors:
        print(f"FAIL: {len(errors)} catalog error(s):", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1
    print(f"OK: {len(descriptors)} descriptor(s) valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
