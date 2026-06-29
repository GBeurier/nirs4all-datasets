"""User-facing retrieval helpers.

This module is intentionally separate from :mod:`nirs4all_datasets.access`.
``get()`` returns a canonical :class:`NirsDataset`; ``retrieve()`` acquires raw
bytes and, by default, asks the Rust reader stack to stage every supported raw
resource. Dataset-specific canonical assembly is still explicit.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, cast


def _opts(
    *,
    cache_dir: str | Path | None,
    timeout_secs: int | None,
    max_total_bytes: int | None = None,
    token: str | None = None,
    instance: str | None = None,
) -> dict[str, Any]:
    out: dict[str, Any] = {}
    if cache_dir is not None:
        out["cache_dir"] = str(cache_dir)
    if timeout_secs is not None:
        out["timeout_secs"] = timeout_secs
    if max_total_bytes is not None:
        out["max_total_bytes"] = max_total_bytes
    if token is not None:
        out["token"] = token
    if instance is not None:
        out["instance"] = instance
    return out


def _select_route(retrieval: dict[str, Any], route_id: str | None) -> dict[str, Any] | None:
    routes = [cast(dict[str, Any], route) for route in retrieval.get("routes") or [] if isinstance(route, dict)]
    if route_id is not None:
        for route in routes:
            if route.get("id") == route_id:
                return route
        raise KeyError(f"retrieval route {route_id!r} is not available.")
    for route in sorted(routes, key=lambda r: int(r.get("priority", 100))):
        if route.get("method") == "raw_retrieve" and route.get("access", "open") == "open" and route.get("automated_download_allowed", True):
            return route
    return None


def retrieve(
    dataset_id: str,
    *,
    root: str | Path = ".",
    route_id: str | None = None,
    cache_dir: str | Path | None = None,
    token: str | None = None,
    instance: str | None = None,
    timeout_secs: int | None = None,
    max_total_bytes: int | None = None,
    prepare: bool = True,
) -> dict[str, Any]:
    """Retrieve a dataset's available bytes by id and return a structured status.

    Resolution order:
    1. first open ``retrieval.routes[]`` raw route, or the requested ``route_id``;
    2. canonical Dataverse fetch when a DOI is present in the resolved contract;
    3. a clear exception for token-pending/manual/delegate-only datasets.

    The return value always includes ``dataset_id`` and ``kind`` (``"raw"`` or
    ``"canonical"``). Raw results are downloaded resources plus optional
    ``preparation`` artifacts; they are not a canonical :class:`NirsDataset`.
    """
    from nirs4all_datasets import _acquire
    from nirs4all_datasets.index import load_index

    index = load_index(root)
    resolved = _acquire.resolve(index, dataset_id)
    retrieval = resolved.get("retrieval") or {}
    route = _select_route(retrieval, route_id)
    if route is not None:
        request = {"dataset_id": dataset_id, "route": route}
        result = _acquire.retrieve_raw(
            request,
            _opts(cache_dir=cache_dir, timeout_secs=timeout_secs, max_total_bytes=max_total_bytes),
        )
        out = {"dataset_id": dataset_id, "kind": "raw", "retrieval_status": retrieval.get("status"), **result}
        if prepare and result.get("ok"):
            out["preparation"] = _acquire.prepare_raw(request, _opts(cache_dir=cache_dir, timeout_secs=None))
        return out

    if resolved.get("doi"):
        result = _acquire.fetch(
            resolved,
            _opts(cache_dir=cache_dir, timeout_secs=timeout_secs, token=token, instance=instance),
        )
        return {"dataset_id": dataset_id, "kind": "canonical", "retrieval_status": retrieval.get("status"), **result}

    status = retrieval.get("status", "documented_only")
    blockers = retrieval.get("blockers") or []
    detail = f": {'; '.join(blockers)}" if blockers else ""
    if status == "token_required":
        raise RuntimeError(
            f"{dataset_id!r} is pending token-gated Dataverse hosting and has no DOI in the index yet{detail}. "
            f"See docs/DATAVERSE_PENDING.md; once uploaded, fetch it with nirs4all_datasets.get({dataset_id!r}, token=...)."
        )
    raise ValueError(f"{dataset_id!r} has no automatic retrieval route yet (status={status!r}){detail}.")


# =============================================================================
# Report: docs/DATAVERSE_PENDING.md — the token-gated datasets pending a private Dataverse upload
# =============================================================================
# These are the true private datasets: no open machine-actionable raw route exists, so neither
# ``retrieve()`` nor ``get()`` can fetch their bytes until they are uploaded to a personal Dataverse and
# a token-gated DOI is minted. This is a strict subset of the ``upload_pending`` set in
# ``docs/PRIVATE_DATASETS.md`` (which lists every non-public dataset without a DOI, including the many
# that ARE openly retrievable from their origin). The retrieval status that marks them is
# ``token_required``.
_PENDING_STATUS = "token_required"


def _load_index(root: str | Path, index: dict[str, Any] | str | Path | None) -> dict[str, Any]:
    """Resolve the index argument to a loaded index dict (a dict, a path, or a registry root)."""
    from nirs4all_datasets.index import load_index

    if index is None:
        return load_index(root)
    if isinstance(index, (str, Path)):
        return load_index(index)
    return index


def pending_dataverse_datasets(index: dict[str, Any]) -> list[dict[str, Any]]:
    """Return the ``token_required`` datasets pending a private Dataverse upload (sorted by id).

    Each row reports why the dataset is stuck (no open route) and what is still missing: its DOI, dataset
    version and per-file Dataverse ids are all unminted (they are created on first ``publish``). Pure
    formatting of the already-built ``catalog/index.json`` — no recomputation, no network.
    """
    datasets: dict[str, Any] = index.get("datasets", {})
    rows: list[dict[str, Any]] = []
    for did in sorted(datasets):
        entry = datasets[did]
        retrieval = entry.get("retrieval") or {}
        if retrieval.get("status") != _PENDING_STATUS:
            continue
        descriptor = entry.get("descriptor") or {}
        dataverse = entry.get("dataverse") or {}
        files = entry.get("files") or []
        rows.append(
            {
                "id": did,
                "name": str(descriptor.get("name") or did),
                "tier": str(entry.get("tier") or descriptor.get("tier") or ""),
                "license": str((descriptor.get("governance") or {}).get("license") or "—"),
                "origins": sorted({str(o.get("kind")) for o in (entry.get("origins") or [])}),
                "instance": str(dataverse.get("instance") or ""),
                "doi": dataverse.get("doi"),
                "dataset_version": dataverse.get("dataset_version"),
                "n_canonical_files": len(files),
                "n_file_ids": sum(1 for f in files if f.get("file_id") is not None),
                "blockers": list(retrieval.get("blockers") or []),
            }
        )
    return rows


def render_dataverse_pending_md(rows: list[dict[str, Any]]) -> str:
    """Render ``docs/DATAVERSE_PENDING.md`` from :func:`pending_dataverse_datasets` rows."""
    lines = [
        "# Datasets pending a private Dataverse upload",
        "",
        "_Generated by `n4a-datasets dataverse-pending` from `catalog/index.json`. These are the datasets",
        "whose retrieval status is `token_required`._",
        "",
        f"These **{len(rows)}** datasets are the true private datasets of the bank: they have **no open**",
        "**machine-actionable raw route**, so neither `nirs4all_datasets.retrieve()` (raw) nor",
        "`nirs4all_datasets.get()` (canonical) can fetch their bytes. They are **not yet uploaded** to a",
        "personal Dataverse, so each one is still missing:",
        "",
        "- a **DOI** (the persistent identifier minted on first publish);",
        "- a **dataset version** (assigned by Dataverse at publish);",
        "- the per-file **Dataverse file ids** (assigned when the canonical files are uploaded).",
        "",
        "Their metadata and metrics are public in the catalog and on the site; only the **bytes** are gated.",
        "This list is a strict subset of the maintainer-only private upload worklist: the other",
        "non-public datasets without a DOI are openly retrievable from their origin.",
        "",
        "## Upload one",
        "",
        "First publish mints the DOI + version + per-file ids and writes the DOI back into",
        "`catalog/datasets/<id>.yaml`, so this list shrinks automatically and `get(id, token=...)` starts working:",
        "",
        "```bash",
        "n4a-datasets publish <id> --collection <your-collection> --contact-email you@example.org",
        "```",
        "",
        "Needs a Dataverse token (see [PUBLISHING.md](PUBLISHING.md)).",
        "",
        f"## Pending uploads ({len(rows)})",
        "",
        "| id | name | tier | license | origin(s) | DOI | version | file ids |",
        "|----|------|------|---------|-----------|-----|---------|----------|",
    ]
    for r in rows:
        origins = ", ".join(r["origins"]) or "—"
        doi = r["doi"] or "⏳ pending"
        version = r["dataset_version"] or "⏳ pending"
        file_ids = f"⏳ 0/{r['n_canonical_files']} (minted on upload)" if r["n_file_ids"] == 0 else f"{r['n_file_ids']}/{r['n_canonical_files']}"
        lines.append(f"| `{r['id']}` | {r['name']} | {r['tier']} | {r['license']} | {origins} | {doi} | {version} | {file_ids} |")
    return "\n".join(lines) + "\n"


def build_dataverse_pending_report(
    root: str | Path = ".",
    *,
    index: dict[str, Any] | str | Path | None = None,
    write: bool = True,
    out: str | Path | None = None,
) -> dict[str, Any]:
    """Build (and optionally write) ``docs/DATAVERSE_PENDING.md`` from the index.

    Returns the structured payload (``{schema, n_pending, datasets}``) so callers and tests need not parse
    the markdown.
    """
    rows = pending_dataverse_datasets(_load_index(root, index))
    if write:
        out_path = Path(out) if out is not None else Path(root) / "docs" / "DATAVERSE_PENDING.md"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(render_dataverse_pending_md(rows), encoding="utf-8")
    return {"schema": "1.0", "n_pending": len(rows), "datasets": rows}
