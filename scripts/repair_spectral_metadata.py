#!/usr/bin/env python3
"""Repair reviewed spectral declarations and rebuild from an existing local raw cache.

Dry-run by default. Originals are read-only, scientific payloads stay gitignored,
and canonical bytes/cards are rebuilt rather than changing historical hashes.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

from nirs4all_datasets.bootstrap import _build_sources, _spectral_blocks, _spectral_metadata, _v2_axis_scale, _write_descriptor
from nirs4all_datasets.catalog import build_catalog
from nirs4all_datasets.manifest import read_manifest, sha256_file
from nirs4all_datasets.organize import organize
from nirs4all_datasets.qualify.profile import qualify
from nirs4all_datasets.schema import AxisUnit, ConversionStatus, DatasetDescriptor


def corrected_descriptor(descriptor: DatasetDescriptor, card: dict[str, Any]) -> DatasetDescriptor:
    """Keep existing owner-reviewed fields; correct explicit units and reviewed technique errors."""
    updated = descriptor.model_copy(deep=True)
    warnings: list[str] = []
    authored = {source.source_id: source for source in _build_sources(card, warnings)}
    blocks = {str(block.get("block_id") or Path(str(block.get("x_file") or "X.csv")).stem): block for block in _spectral_blocks(card)}
    reviewed = _spectral_metadata().get(descriptor.id, {})
    for source in updated.sources:
        proposed = authored.get(source.source_id)
        block = blocks.get(source.source_id)
        if proposed is None or block is None:
            continue
        # Existing index/physical declarations may be a reviewed representation
        # correction (notably ChEMBL mode indices), more authoritative than the exporter.
        if source.source_id in reviewed or (proposed.axis_unit is not AxisUnit.NONE and (source.axis_unit is AxisUnit.NONE or _v2_axis_scale(block) != 1)):
            source.axis_unit = proposed.axis_unit
        if source.source_id in reviewed and proposed.axis_unit is AxisUnit.NONE:
            source.axis_min, source.axis_max, source.axis_resolution = proposed.axis_min, proposed.axis_max, proposed.axis_resolution
        if _v2_axis_scale(block) != 1:
            source.axis_min, source.axis_max = proposed.axis_min, proposed.axis_max
            source.axis_resolution = proposed.axis_resolution
            prefix = f"{source.source_id}: native axis unit"
            native_warnings = [warning for warning in warnings if warning.startswith(prefix)]
            if [warning for warning in updated.provenance.warnings if warning.startswith(prefix)] != native_warnings:
                updated.provenance.warnings = [warning for warning in updated.provenance.warnings if not warning.startswith(prefix)]
                updated.provenance.warnings.extend(native_warnings)
        if source.source_id in reviewed or str(block.get("spectroscopy_type") or "").lower() == "vis-swir":
            source.modality = proposed.modality
        if correction := reviewed.get(source.source_id):
            evidence = ", ".join(correction["evidence"])
            note = f"Spectral declaration for {source.source_id}: {correction['note']} Evidence: {evidence}"
            if note not in updated.provenance.warnings:
                updated.provenance.warnings.append(note)
    return updated


def rebuild_one(root: Path, source_cache: Path, dataset_id: str) -> dict[str, Any]:
    """Rebuild one affected dataset while preserving raw inputs and all non-spectral declarations."""
    descriptor_path = root / "catalog/datasets" / f"{dataset_id}.yaml"
    before = DatasetDescriptor(**yaml.safe_load(descriptor_path.read_text(encoding="utf-8")))
    raw = source_cache / dataset_id / "raw"
    card = json.loads((raw / "dataset_card.json").read_text(encoding="utf-8"))
    updated = corrected_descriptor(before, card)
    if updated == before:
        return {"id": dataset_id, "changed": False}
    destination = root / "datasets" / dataset_id
    if raw.resolve().is_relative_to(destination.resolve()) or destination.resolve().is_relative_to(raw.resolve()):
        raise ValueError("source cache and rebuild destination must be separate")
    previous = read_manifest(source_cache / dataset_id / "manifest.json")
    for entry in previous.files:
        if entry.path.startswith("raw/"):
            path = source_cache / dataset_id / entry.path
            if path.stat().st_size != entry.size or sha256_file(path) != entry.sha256:
                raise ValueError(f"{dataset_id}: supplied raw cache differs from its recorded manifest")
    # The source sidecar is also pinned: losing its enrichment would change the study.
    expected_soilsite = previous.converter_config.get("soilsite_sha256")
    if expected_soilsite:
        soilsite = Path(os.environ.get("NIRS4ALL_OSSL_SOILSITE", ""))
        if not soilsite.is_file() or sha256_file(soilsite) != expected_soilsite:
            raise ValueError(f"{dataset_id}: supply the original verified OSSL soilsite sidecar")
    if any(key.startswith("source_context:") for key in previous.converter_config):
        raise ValueError(f"{dataset_id}: reproduce the recorded source-context inputs before rebuilding")
    major, minor, patch = updated.versions.content.split(".")
    updated.versions.content = f"{major}.{minor}.{int(patch) + 1}"
    result = organize(raw, updated, root / "datasets", force=True)
    if result.conversion_status is ConversionStatus.FAILED:
        raise ValueError(f"{dataset_id}: canonical conversion failed")
    assert result.canonical_result is not None
    updated.provenance.ingest_reader_version = result.canonical_result.converter_version
    updated.provenance.conversion_status = result.conversion_status
    _write_descriptor(updated, descriptor_path)
    output = qualify(destination, updated)
    return {"id": dataset_id, "changed": True, "sources": [{key: source.get(key) for key in ("source_id", "modality", "axis_unit", "axis_min", "axis_max")} for source in output["sources"]], "integrity": output["integrity"]}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPO)
    parser.add_argument("--source-cache", type=Path, required=True, help="Read-only datasets directory containing each dataset's raw bundle and manifest")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--only", help="Comma-separated dataset IDs")
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    root, cache = args.root.resolve(), args.source_cache.resolve()
    selected = set(args.only.split(",")) if args.only else None
    affected = []
    for path in sorted((root / "catalog/datasets").glob("*.yaml")):
        if selected is not None and path.stem not in selected:
            continue
        card_path = cache / path.stem / "raw/dataset_card.json"
        if not card_path.is_file():
            continue  # Descriptor-only candidates stay unqualified.
        descriptor = DatasetDescriptor(**yaml.safe_load(path.read_text(encoding="utf-8")))
        if corrected_descriptor(descriptor, json.loads(card_path.read_text(encoding="utf-8"))) != descriptor:
            affected.append(descriptor.id)
    print(json.dumps({"write": args.write, "affected": affected}), flush=True)
    if not args.write:
        return
    results = []
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        for result in pool.map(lambda identifier: rebuild_one(root, cache, identifier), affected):
            results.append(result)
            print(json.dumps(result), flush=True)
    catalog = build_catalog(root)
    receipt = {"results": results, "n_datasets": catalog["n_datasets"], "summary": catalog["summary"]}
    if args.receipt:
        args.receipt.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
