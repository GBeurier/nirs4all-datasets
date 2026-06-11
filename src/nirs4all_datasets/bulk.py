"""Bulk orchestration: organize + qualify many datasets in parallel, with failure isolation.

Given a registry root (holding ``catalog/datasets/<id>.yaml``) and the read-only source tree the
descriptors were generated from, this resolves each descriptor's ``generation.source_relpath`` back to
its raw leaf, then runs :func:`organize` (copy → canonical, incremental) and :func:`build_card` for
each — across a process pool, since card building is CPU-bound and per-dataset independent.

One dataset failing never aborts the run: each result carries a status (``ok``/``partial``/``failed``/
``skipped``) and reason. The machine-readable ``bulk_report.json`` is deterministic (sorted by id).
"""
from __future__ import annotations

import json
import os
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import yaml

from nirs4all_datasets.schema import DatasetDescriptor


def _load_descriptor(root: Path, dataset_id: str) -> DatasetDescriptor:
    path = root / "catalog" / "datasets" / f"{dataset_id}.yaml"
    return DatasetDescriptor(**(yaml.safe_load(path.read_text(encoding="utf-8")) or {}))


def _descriptor_ids(root: Path) -> list[str]:
    return sorted(p.stem for p in (root / "catalog" / "datasets").glob("*.yaml"))


def process_one(root_str: str, source_tree_str: str, dataset_id: str, *, skip_assets: bool, force: bool, protocol_refresh: bool = False) -> dict[str, Any]:
    """Organize + qualify a single dataset; return a status record (never raises).

    Module-level (picklable) so it can run inside a :class:`ProcessPoolExecutor` worker.
    ``protocol_refresh`` re-qualifies (rebuilds the card under a new metric protocol) even when the
    canonical bytes are unchanged — without rebuilding canonical.
    """
    from nirs4all_datasets.organize import organize
    from nirs4all_datasets.qualify.profile import card_metadata_fresh, qualify

    root, source_tree = Path(root_str), Path(source_tree_str)
    try:
        descriptor = _load_descriptor(root, dataset_id)
    except Exception as exc:  # noqa: BLE001 - report, never crash the pool
        return {"id": dataset_id, "status": "failed", "reason": f"descriptor: {type(exc).__name__}: {exc}"}

    rel = descriptor.generation.source_relpath if descriptor.generation else None
    if not rel:
        return {"id": dataset_id, "status": "skipped", "reason": "no generation.source_relpath (human descriptor)"}
    source = source_tree / rel
    if not source.exists():
        return {"id": dataset_id, "status": "failed", "reason": f"source missing: {rel}"}

    try:
        result = organize(source, descriptor, root / "datasets", force=force)
        # organize.skipped means canonical bytes are unchanged (descriptor_hash). The card also *displays*
        # provenance, so a metadata-only edit (sources/citation) must still rebuild it -> check metadata_hash.
        card_path = result.dataset_dir / "card.json"
        if result.skipped and not force and not protocol_refresh and card_metadata_fresh(card_path, descriptor):
            return {"id": dataset_id, "status": "skipped", "reason": "unchanged"}
        card = qualify(result.dataset_dir, descriptor, compute_assets=not skip_assets)
        warns = card.get("warnings") or []
        align = card.get("alignment") or {}
        n_features = sum((s.get("n_variables") or 0) for s in card.get("sources", [])) or None
        return {
            "id": dataset_id,
            "status": "partial" if warns else "ok",
            "n_samples": align.get("n_samples"),
            "n_features": n_features,
            "n_sources": len(card.get("sources", [])),
            "warnings": warns[:6],
        }
    except Exception as exc:  # noqa: BLE001 - isolate per-dataset failures
        return {"id": dataset_id, "status": "failed", "reason": f"{type(exc).__name__}: {exc}"}


def build_all(
    root: str | Path,
    source_tree: str | Path,
    *,
    workers: int | None = None,
    only: list[str] | None = None,
    skip_assets: bool = False,
    force: bool = False,
    protocol_refresh: bool = False,
    progress: Any = None,
) -> dict[str, Any]:
    """Organize + qualify every (or ``only``) descriptor under ``root`` against ``source_tree``.

    Returns a deterministic report ``{counts, results}`` (results sorted by id). ``progress`` is an
    optional ``callable(done, total, record)`` for live CLI output.
    """
    root, source_tree = Path(root), Path(source_tree)
    ids = sorted(only) if only else _descriptor_ids(root)
    n_workers = workers if workers is not None else min(6, max(1, (os.cpu_count() or 2) - 2))

    results: list[dict[str, Any]] = []
    if n_workers <= 1:
        for i, did in enumerate(ids, 1):
            rec = process_one(str(root), str(source_tree), did, skip_assets=skip_assets, force=force, protocol_refresh=protocol_refresh)
            results.append(rec)
            if progress:
                progress(i, len(ids), rec)
    else:
        with ProcessPoolExecutor(max_workers=n_workers) as pool:
            futures = {pool.submit(process_one, str(root), str(source_tree), did, skip_assets=skip_assets, force=force, protocol_refresh=protocol_refresh): did for did in ids}
            for i, fut in enumerate(as_completed(futures), 1):
                rec = fut.result()
                results.append(rec)
                if progress:
                    progress(i, len(ids), rec)

    results.sort(key=lambda r: r["id"])
    counts: dict[str, int] = {}
    for rec in results:
        counts[rec["status"]] = counts.get(rec["status"], 0) + 1
    return {"counts": counts, "n_datasets": len(results), "results": results}


def write_report(report: dict[str, Any], path: str | Path) -> None:
    """Write a deterministic ``bulk_report.json`` (gitignored; may contain local paths)."""
    Path(path).write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
