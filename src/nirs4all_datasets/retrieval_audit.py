"""Machine-readable audit of descriptor retrieval readiness.

The audit is intentionally static: it never executes NIRS DB scripts and never
touches the network. It gives maintainers a stable worklist for converting
datasets from "documented/private only" to declarative retrieval routes.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

import yaml

from nirs4all_datasets.catalog import descriptor_paths
from nirs4all_datasets.schema import DatasetDescriptor, SourceAccess, SourceKind, SourceMode

AUDIT_SCHEMA = "1.0"
_URL_RE = re.compile(r"https?://[^\s'\"<>]+")
_DOI_RE = re.compile(r"\b10\.\d{4,9}/[^\s'\"<>]+")


def _script_path(source_tree: Path | None, dataset_id: str) -> Path | None:
    if source_tree is None:
        return None
    path = source_tree / "v2.0" / dataset_id / "source_to_standard.py"
    return path if path.exists() else None


def _script_family(dataset_id: str, script: Path | None) -> str | None:
    if script is None:
        return None
    for prefix, family in (
        ("ossl_", "ossl"),
        ("ecostress_", "ecostress"),
        ("ecosis_", "ecosis"),
        ("timeseries_", "timeseries_classification"),
        ("rruff_", "rruff"),
        ("chembl_", "chembl"),
    ):
        if dataset_id.startswith(prefix):
            return family
    return dataset_id.split("_", 1)[0] if "_" in dataset_id else "dataset_specific"


def _script_info(path: Path | None) -> dict[str, Any] | None:
    if path is None:
        return None
    text = path.read_text(encoding="utf-8", errors="replace")
    return {
        "path": str(path),
        "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "n_lines": text.count("\n") + (0 if text.endswith("\n") else 1),
        "urls": sorted(set(_URL_RE.findall(text))),
        "dois": sorted(set(_DOI_RE.findall(text))),
        "imports_pandas": "import pandas" in text or "from pandas" in text,
        "imports_requests": "import requests" in text or "from requests" in text,
    }


def _origin_dicts(descriptor: DatasetDescriptor) -> list[dict[str, str | None]]:
    return [
        {
            "kind": origin.kind.value,
            "mode": origin.mode.value,
            "locator": origin.locator,
            "access": origin.access.value,
        }
        for origin in descriptor.origin_sources
    ]


def _propose_route(descriptor: DatasetDescriptor, script: Path | None) -> tuple[str, list[str]]:
    blockers: list[str] = []
    if descriptor.retrieval.routes:
        return descriptor.retrieval.routes[0].method.value, blockers

    open_fetchable = [
        origin
        for origin in descriptor.origin_sources
        if origin.access is SourceAccess.OPEN and origin.kind in {SourceKind.DATAVERSE, SourceKind.ZENODO, SourceKind.FIGSHARE, SourceKind.URL}
    ]
    if any(origin.mode is SourceMode.CANONICAL for origin in open_fetchable):
        return "canonical_fetch", blockers
    if any(origin.mode is SourceMode.RAW for origin in open_fetchable):
        if script is None:
            blockers.append("raw origin is declared, but no NIRS DB conversion script was found")
        return "raw_retrieve", blockers

    if any(origin.access is SourceAccess.TOKEN for origin in descriptor.origin_sources) or descriptor.tier.value in {"private", "anonymized"}:
        blockers.append("requires token-gated hosted fallback or source credential")
        return "token_required", blockers
    if any(origin.access is SourceAccess.MANUAL for origin in descriptor.origin_sources):
        blockers.append("manual or click-through access must be represented explicitly")
        return "manual", blockers
    if script is not None:
        blockers.append("script exists but no open origin is declared in the descriptor")
        return "delegate", blockers

    blockers.append("no machine-actionable source or script found")
    return "documented_only", blockers


def audit_entry(root: str | Path, descriptor: DatasetDescriptor, *, source_tree: str | Path | None = None) -> dict[str, Any]:
    """Build one static retrieval audit row."""
    root = Path(root)
    source_root = Path(source_tree) if source_tree is not None else (root / "NIRS DB" if (root / "NIRS DB").exists() else None)
    script = _script_path(source_root, descriptor.id)
    proposed_route_type, blockers = _propose_route(descriptor, script)
    existing_routes = [
        {
            "id": route.id,
            "method": route.method.value,
            "provider": route.provider.value,
            "access": route.access.value,
            "resource_count": len(route.resources),
        }
        for route in descriptor.retrieval.routes
    ]
    return {
        "dataset_id": descriptor.id,
        "tier": descriptor.tier.value,
        "origins": _origin_dicts(descriptor),
        "retrieval_status": descriptor.retrieval.status.value,
        "existing_routes": existing_routes,
        "script_family": _script_family(descriptor.id, script),
        "script": _script_info(script),
        "proposed_route_type": proposed_route_type,
        "blockers": blockers,
    }


def build_retrieval_audit(
    root: str | Path,
    *,
    source_tree: str | Path | None = None,
    write: bool = True,
    out: str | Path | None = None,
) -> dict[str, Any]:
    """Write ``catalog/retrieval_audit.json`` from descriptors and optional NIRS DB scripts."""
    root = Path(root)
    source_root = Path(source_tree) if source_tree is not None else (root / "NIRS DB" if (root / "NIRS DB").exists() else None)
    rows = [
        audit_entry(root, DatasetDescriptor(**(yaml.safe_load(path.read_text(encoding="utf-8")) or {})), source_tree=source_root)
        for path in descriptor_paths(root)
    ]
    by_route: dict[str, int] = {}
    by_family: dict[str, int] = {}
    for row in rows:
        by_route[row["proposed_route_type"]] = by_route.get(row["proposed_route_type"], 0) + 1
        family = row["script_family"] or "none"
        by_family[family] = by_family.get(family, 0) + 1
    report = {
        "schema": AUDIT_SCHEMA,
        "n_datasets": len(rows),
        "source_tree": str(source_root) if source_root is not None else None,
        "summary": {
            "by_proposed_route_type": dict(sorted(by_route.items())),
            "by_script_family": dict(sorted(by_family.items())),
            "n_with_script": sum(1 for row in rows if row["script"] is not None),
            "n_with_existing_routes": sum(1 for row in rows if row["existing_routes"]),
        },
        "datasets": rows,
    }
    if write:
        out_path = Path(out) if out is not None else root / "catalog" / "retrieval_audit.json"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
        if out is None:
            write_dataverse_pending_report(root, report)
    return report


def render_dataverse_pending_md(report: dict[str, Any]) -> str:
    """Render the token-gated datasets awaiting private Dataverse upload."""
    rows = [row for row in report["datasets"] if row["proposed_route_type"] == "token_required"]
    lines = [
        "# Dataverse Pending Datasets",
        "",
        "_Generated by `n4a-datasets retrieval-audit`. These datasets currently have no public",
        "machine-actionable source route. They should stay visible in the catalog and become",
        "retrievable once their private Dataverse DOI/version/file ids are added to the descriptors._",
        "",
        "## Required Descriptor Updates",
        "",
        "For each dataset, upload the canonical files to the private Dataverse, restrict files as",
        "needed, then fill `dataverse.doi`, `dataverse.dataset_version`, and manifest `file_id`s.",
        "",
        f"## Pending ({len(rows)})",
        "",
        "| dataset_id | tier | current origins | blockers |",
        "|------------|------|-----------------|----------|",
    ]
    for row in rows:
        origins = ", ".join(f"{o['kind']}:{o['access']}" for o in row["origins"]) or "none"
        blockers = "; ".join(row["blockers"]) or "private Dataverse upload pending"
        lines.append(f"| `{row['dataset_id']}` | {row['tier']} | {origins} | {blockers} |")
    return "\n".join(lines) + "\n"


def write_dataverse_pending_report(root: str | Path, report: dict[str, Any]) -> Path:
    """Write ``docs/DATAVERSE_PENDING.md`` next to the human-readable audit docs."""
    out = Path(root) / "docs" / "DATAVERSE_PENDING.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_dataverse_pending_md(report), encoding="utf-8")
    return out
