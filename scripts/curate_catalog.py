#!/usr/bin/env python3
"""Rebuild existing catalog datasets using the audited curation contracts (#23/#24).

Uses only supplied local standardized bundles and soilsite; source scripts are
never executed. Raw and canonical payloads remain gitignored. Existing identity,
licensing, access tiers, acquisition routes and publications are preserved.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

import pandas as pd
import yaml

from nirs4all_datasets.bootstrap import GENERATOR_VERSION, _dir_fingerprint, _write_descriptor, build_descriptor_from_card, find_v2_leaves, slugify
from nirs4all_datasets.canonical import CONVERTER_VERSION
from nirs4all_datasets.catalog import build_catalog
from nirs4all_datasets.curation import catalog_curation_report
from nirs4all_datasets.manifest import metadata_hash, read_manifest, sha256_file, write_manifest
from nirs4all_datasets.organize import organize
from nirs4all_datasets.qualify.profile import _integrity, _jsonify, _variable_section, card_metadata_fresh, qualify, write_card
from nirs4all_datasets.schema import DatasetDescriptor, FileRole, Tier, VarType


def refresh_views(root: Path, leaf: Path) -> dict[str, Any]:
    """Refresh metadata views only when input hashes and source-unit membership are unchanged."""
    from nirs4all_datasets.curation import card_curation, curate_bundle, write_curated
    from nirs4all_datasets.qualify import anonymize, croissant, datasheet

    dataset_id = slugify(leaf.name)
    descriptor = DatasetDescriptor(**yaml.safe_load((root / "catalog" / "datasets" / f"{dataset_id}.yaml").read_text(encoding="utf-8")))
    dataset_dir = root / "datasets" / dataset_id
    canonical = dataset_dir / "canonical"
    report_path = canonical / "curation" / "mapping.json"
    previous = json.loads(report_path.read_text(encoding="utf-8"))
    result = curate_bundle(leaf, dataset_id, assume_paired_y=True, numeric_names={v.name for v in descriptor.variables if v.type is VarType.NUMERIC}, categorical_names={v.name for v in descriptor.variables if v.type is VarType.CATEGORICAL}, allow_unaligned_y=True, verify_spectral_order=True, variable_specs=descriptor.variables)
    if previous.get("source_hashes") != result.report.get("source_hashes") or previous.get("enrichments") != result.report.get("enrichments"):
        raise ValueError("source inputs/enrichment changed: a full canonical rebuild is required")
    old_structure = pd.read_parquet(canonical / "curation" / "structure.parquet")
    pd.testing.assert_frame_equal(old_structure, result.structure, check_dtype=False)
    write_curated(result, canonical / "curation")
    manifest_path = dataset_dir / "manifest.json"
    manifest = read_manifest(manifest_path)
    updated_files = {path.relative_to(dataset_dir).as_posix(): path for path in (canonical / "curation").iterdir() if path.is_file()}
    manifest.files = [entry.model_copy(update={"sha256": sha256_file(updated_files[entry.path]), "size": updated_files[entry.path].stat().st_size}) if entry.path in updated_files else entry for entry in manifest.files]
    manifest.canonical_hashes = {Path(entry.path).name: entry.sha256 for entry in manifest.files if entry.role is FileRole.CANONICAL and entry.path.endswith(".parquet")}
    write_manifest(manifest, manifest_path)
    tracked = catalog_curation_report(result.report, anonymized=descriptor.tier is Tier.ANONYMIZED)
    (root / "catalog" / "curation" / f"{dataset_id}.json").write_text(json.dumps(tracked, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    card = json.loads((dataset_dir / "card.json").read_text(encoding="utf-8"))
    config = json.loads((canonical / "dataset.json").read_text(encoding="utf-8"))
    block = config.get("variables")
    if block:
        variables = pd.read_parquet(dataset_dir / block["path"])
        warnings: list[str] = []
        card["variables"] = [_variable_section(var, variables[var.name], warnings, compute_histogram=True) for var in descriptor.variables if var.name in variables]
    card["curation"] = card_curation(result.report)
    card["integrity"] = _integrity(dataset_dir, descriptor, [])
    card = _jsonify(anonymize.public_card(card, descriptor.tier))
    public_descriptor = anonymize.public_descriptor(descriptor)
    write_card(card, dataset_dir / "card.json")
    (dataset_dir / "card.md").write_text(datasheet.render_datasheet(card, public_descriptor), encoding="utf-8")
    (dataset_dir / "croissant.json").write_text(json.dumps(croissant.render_croissant(card, public_descriptor, hashes=manifest.canonical_hashes), indent=2, sort_keys=True), encoding="utf-8")
    identity = result.report["identity"]
    return {"dataset_id": dataset_id, "n_observations": len(result.structure), "n_samples": identity["n_samples"], "identity_status": identity["status"], "observations_per_unit": identity["observations_per_unit"], "technical_repetitions": identity["technical_repetitions"], "n_M": len(result.report["views"]["M"]), "n_Y": len(result.report["views"]["Y"]), "M": result.report["views"]["M"], "Y": result.report["views"]["Y"], "warnings": result.warnings if descriptor.tier is not Tier.ANONYMIZED else [], "metadata_hash": metadata_hash(descriptor), "skipped": True}


def migrate_one(root: Path, leaf: Path, source_tree: Path, *, force: bool = False) -> dict[str, Any]:
    dataset_id = slugify(leaf.name)
    descriptor_path = root / "catalog" / "datasets" / f"{dataset_id}.yaml"
    descriptor = DatasetDescriptor(**yaml.safe_load(descriptor_path.read_text(encoding="utf-8")))
    before = descriptor.model_copy(deep=True)
    dataset_dir = root / "datasets" / dataset_id
    for destination in [dataset_dir / "raw", dataset_dir / "canonical"]:
        if not destination.resolve().is_relative_to(root.resolve()):
            raise ValueError("refusing a dataset output outside the repository root")
    # Read source facts through the same bootstrap implementation used by future rebuilds.
    authored, _ = build_descriptor_from_card(leaf)
    descriptor.ids = authored.ids
    if descriptor.ids.sample_id_available:
        descriptor.alignment_level = authored.alignment_level
    existing = {var.name for var in descriptor.variables}
    for var in authored.variables:
        if var.name not in existing:
            descriptor.variables.append(var)
            existing.add(var.name)
    for var in descriptor.variables:
        if var.name == "api_reference_percent_w_w":
            var.unit = "% w/w"
    descriptor.provenance.warnings = [warning for warning in descriptor.provenance.warnings if not warning.startswith("Observation identity is used as the canonical join key because source sample_id")]
    identity_warnings = [warning for warning in authored.provenance.warnings if warning.startswith("Curation identity contract:")]
    descriptor.provenance.warnings = list(dict.fromkeys([*descriptor.provenance.warnings, *identity_warnings]))
    if descriptor.generation:
        descriptor.generation.generator_version = GENERATOR_VERSION
        descriptor.generation.source_relpath = leaf.relative_to(source_tree).as_posix()
        descriptor.generation.source_fingerprint = _dir_fingerprint(leaf)
    if descriptor.provenance.ingest_reader_version != CONVERTER_VERSION:
        major, minor, _ = descriptor.versions.content.split(".", 2)
        descriptor.versions.content = f"{major}.{int(minor) + 1}.0"
    descriptor.provenance.ingest_reader_version = CONVERTER_VERSION
    # No rights changes are part of scientific curation.
    assert descriptor.tier == before.tier and descriptor.governance == before.governance
    assert descriptor.retrieval == before.retrieval and descriptor.origin_sources == before.origin_sources
    result = organize(leaf, descriptor, root / "datasets", force=force)
    if result.conversion_status and result.conversion_status.value == "failed":
        raise ValueError("canonical conversion failed: " + "; ".join(result.conversion_warnings))
    descriptor.provenance.conversion_status = result.conversion_status
    _write_descriptor(descriptor, descriptor_path)
    if not result.skipped or not card_metadata_fresh(dataset_dir, descriptor):
        qualify(dataset_dir, descriptor, compute_assets=True, compute_pca=False)
    mapping_path = dataset_dir / "canonical" / "curation" / "mapping.json"
    report = json.loads(mapping_path.read_text(encoding="utf-8"))
    tracked = catalog_curation_report(report, anonymized=descriptor.tier is Tier.ANONYMIZED)
    (root / "catalog" / "curation" / f"{dataset_id}.json").write_text(json.dumps(tracked, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    identity = report["identity"]
    return {"dataset_id": dataset_id, "n_observations": len(pd.read_parquet(dataset_dir / "canonical" / "curation" / "structure.parquet")), "n_samples": identity["n_samples"], "identity_status": identity["status"], "observations_per_unit": identity["observations_per_unit"], "technical_repetitions": identity["technical_repetitions"], "n_M": len(report["views"]["M"]), "n_Y": len(report["views"]["Y"]), "M": report["views"]["M"], "Y": report["views"]["Y"], "warnings": result.conversion_warnings if descriptor.tier is not Tier.ANONYMIZED else [], "metadata_hash": metadata_hash(descriptor), "skipped": result.skipped}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_tree", type=Path)
    parser.add_argument("--root", type=Path, default=REPO)
    parser.add_argument("--soilsite", type=Path)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--only", help="Comma-separated existing dataset IDs")
    parser.add_argument("--force", action="store_true", help="Rebuild even when cached inputs are unchanged.")
    parser.add_argument("--refresh-curation-only", action="store_true", help="Refresh views/card variables from unchanged inputs; assert source-unit membership is unchanged.")
    options = parser.parse_args()
    root, source_tree = options.root.resolve(), options.source_tree.resolve()
    if options.soilsite:
        os.environ["NIRS4ALL_OSSL_SOILSITE"] = str(options.soilsite.resolve())
    (root / "catalog" / "curation").mkdir(parents=True, exist_ok=True)
    catalog_ids = {path.stem for path in (root / "catalog" / "datasets").glob("*.yaml")}
    selected = set(options.only.split(",")) if options.only else catalog_ids
    leaves = [leaf for leaf in find_v2_leaves(source_tree) if slugify(leaf.name) in selected & catalog_ids]
    report: dict[str, Any] = {"schema_version": "1.0", "issues": [23, 24], "processed": [], "errors": [], "missing_local_sources": sorted((selected & catalog_ids) - {slugify(leaf.name) for leaf in leaves})}
    with ThreadPoolExecutor(max_workers=max(1, options.workers)) as pool:
        futures = {pool.submit(refresh_views, root, leaf) if options.refresh_curation_only else pool.submit(migrate_one, root, leaf, source_tree, force=options.force): leaf for leaf in leaves}
        for future in as_completed(futures):
            leaf = futures[future]
            try:
                row = future.result()
                report["processed"].append(row)
                print(f"OK {row['dataset_id']}: samples={row['n_samples']}, M={row['n_M']}, Y={row['n_Y']}", flush=True)
            except Exception as exc:  # isolate a broken source and retain its actionable failure
                report["errors"].append({"dataset_id": slugify(leaf.name), "error": f"{type(exc).__name__}: {exc}"})
                print(f"ERROR {leaf.name}: {type(exc).__name__}: {exc}", flush=True)
    report["processed"].sort(key=lambda row: row["dataset_id"])
    report["errors"].sort(key=lambda row: row["dataset_id"])
    (root / "catalog" / "curation" / "summary.json").write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    with (root / "catalog" / "curation" / "datasets.csv").open("w", encoding="utf-8-sig", newline="") as stream:
        fields = ["dataset_id", "n_observations", "n_samples", "identity_status", "observations_per_unit", "technical_repetitions", "n_M", "n_Y", "M", "Y"]
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter=";", extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        for row in report["processed"]:
            writer.writerow({**row, **{name: json.dumps(row[name], ensure_ascii=False) for name in ["observations_per_unit", "M", "Y"]}})
    build_catalog(root)
    print(f"DONE processed={len(report['processed'])} errors={len(report['errors'])} missing={len(report['missing_local_sources'])}", flush=True)
    return int(bool(report["errors"] or report["missing_local_sources"]))


if __name__ == "__main__":
    raise SystemExit(main())
