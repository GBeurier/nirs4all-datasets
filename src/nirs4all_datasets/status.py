"""Per-dataset readiness status + the human-validation registry.

Two axes, one automatic and one human:

* **State** (automatic, derived from the catalog/health): the processing stage
  (``described`` -> ``canonical`` -> ``qualified`` = metrics computed), whether the canonical bytes are
  materialized + checksummed, whether the origin is reachable, and how the data is distributed
  (``open`` from the origin / ``on_dataverse`` / ``upload_pending``).
* **Validation** (human, recorded in ``catalog/validation.yaml``): ``pending`` -> ``reviewed`` ->
  ``approved`` — a person has inspected and signed off the dataset. The registry is hand-editable and is
  never touched by ``bootstrap`` (so a human sign-off survives descriptor regeneration).

:func:`build_reports` renders two committed Markdown reports — ``docs/DATASET_STATUS.md`` (every dataset)
and ``docs/PRIVATE_DATASETS.md`` (the private/anonymized datasets still to upload to a personal Dataverse).
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from nirs4all_datasets.catalog import descriptor_paths, load_catalog

VALIDATION_STATES = ("pending", "reviewed", "approved")
_VALIDATION_PATH = ("catalog", "validation.yaml")


def validation_path(root: str | Path) -> Path:
    return Path(root).joinpath(*_VALIDATION_PATH)


def load_validation(root: str | Path) -> dict[str, dict[str, Any]]:
    """Read the human-validation registry (``catalog/validation.yaml``); ``{}`` if absent."""
    path = validation_path(root)
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    datasets = data.get("datasets") if isinstance(data, dict) else None
    return datasets if isinstance(datasets, dict) else {}


def init_validation(root: str | Path, *, write: bool = True) -> dict[str, dict[str, Any]]:
    """Ensure every catalogued dataset has a validation record (default ``pending``), preserving any
    existing human entries; prune records whose descriptor no longer exists. Returns the registry."""
    root = Path(root)
    ids = [p.stem for p in descriptor_paths(root)]
    existing = load_validation(root)
    registry: dict[str, dict[str, Any]] = {}
    for did in ids:
        rec = existing.get(did) or {}
        registry[did] = {
            "validation": rec.get("validation", "pending") if rec.get("validation") in VALIDATION_STATES else "pending",
            "reviewed_by": rec.get("reviewed_by"),
            "reviewed_at": rec.get("reviewed_at"),
            "notes": rec.get("notes"),
        }
    if write:
        validation_path(root).parent.mkdir(parents=True, exist_ok=True)
        banner = "# Human validation registry (hand-edit). Set validation to: pending | reviewed | approved.\n# `bootstrap` never touches this file, so a sign-off survives descriptor regeneration.\n"
        validation_path(root).write_text(banner + yaml.safe_dump({"datasets": registry}, sort_keys=True, allow_unicode=True), encoding="utf-8")
    return registry


def _distribution(entry: dict[str, Any]) -> str:
    """``open`` (public, fetched from the origin) / ``on_dataverse`` (private+DOI) / ``upload_pending``."""
    if entry.get("tier") == "public":
        return "open"
    return "on_dataverse" if entry.get("doi") else "upload_pending"


def _state(entry: dict[str, Any]) -> str:
    """Processing stage: ``qualified`` (metrics computed) / ``canonical`` / ``described``."""
    if entry.get("has_card") and not entry.get("is_stale"):
        return "qualified"
    return "canonical" if entry.get("has_manifest") else "described"


def _origin(entry: dict[str, Any]) -> str:
    """Origin reachability from the health probe: ``verified`` / ``degraded`` / ``unreachable`` / ``unverified``."""
    health = entry.get("health") or {}
    if health.get("degraded"):
        return "degraded"
    alive = health.get("alive")
    return {True: "verified", False: "unreachable", None: "unverified"}[alive]


def dataset_status(entry: dict[str, Any], validation: dict[str, Any] | None) -> dict[str, Any]:
    """The full status of one dataset = derived state + the recorded human validation."""
    return {
        "id": entry["id"],
        "tier": entry.get("tier"),
        "state": _state(entry),
        "metrics_computed": bool(entry.get("has_card") and not entry.get("is_stale")),
        "materialized": bool(entry.get("has_manifest")),
        "origin": _origin(entry),
        "validation": (validation or {}).get("validation", "pending"),
        "distribution": _distribution(entry),
        "n_samples": entry.get("n_samples"),
    }


def collect(root: str | Path) -> list[dict[str, Any]]:
    """Per-dataset status for every catalogued dataset (sorted by id)."""
    entries = load_catalog(root).get("datasets", [])
    validation = load_validation(root)
    return [dataset_status(e, validation.get(e["id"])) for e in sorted(entries, key=lambda e: e["id"])]


def _count(rows: list[dict[str, Any]], key: str) -> dict[str, int]:
    out: dict[str, int] = {}
    for r in rows:
        out[str(r[key])] = out.get(str(r[key]), 0) + 1
    return out


_ORIGIN_ICON = {"verified": "✅", "degraded": "⚠️", "unreachable": "❌", "unverified": "—"}
_VAL_ICON = {"pending": "⏳ pending", "reviewed": "👁 reviewed", "approved": "✅ approved"}
_DIST_ICON = {"open": "🌍 open", "on_dataverse": "🔒 dataverse", "upload_pending": "⬆️ upload-pending"}


def render_status_md(rows: list[dict[str, Any]]) -> str:
    """Render ``docs/DATASET_STATUS.md`` — summary + a one-row-per-dataset table."""
    by_tier = _count(rows, "tier")
    by_state = _count(rows, "state")
    by_origin = _count(rows, "origin")
    by_val = _count(rows, "validation")
    by_dist = _count(rows, "distribution")
    lines = [
        "# Dataset status",
        "",
        "_Generated by `n4a-datasets status`. **State / materialized / origin / distribution** are derived",
        "automatically from the catalog + health probe; **validation** is the human review status recorded in",
        "`catalog/validation.yaml` (hand-edited, never overwritten by `bootstrap`)._",
        "",
        "## Summary",
        f"- **{len(rows)} datasets** — " + ", ".join(f"{n} {t}" for t, n in sorted(by_tier.items())),
        "- **Processing:** " + ", ".join(f"{n} {s}" for s, n in sorted(by_state.items())) + " (qualified = metrics computed)",
        "- **Origin:** " + ", ".join(f"{n} {o}" for o, n in sorted(by_origin.items())),
        "- **Validation (human):** " + ", ".join(f"{n} {v}" for v, n in sorted(by_val.items())),
        "- **Distribution:** " + ", ".join(f"{n} {d}" for d, n in sorted(by_dist.items())),
        "",
        "## Legend",
        "- **state** — `described` → `canonical` → **`qualified`** (per-source/per-variable metrics computed)",
        "- **mat.** — ✅ canonical bytes materialized + SHA-256 in the manifest (download-verifiable)",
        "- **origin** — ✅ reachable · ⚠️ degraded (public, all open origins dead) · ❌ unreachable · — not probed",
        "- **validation** — ⏳ pending · 👁 reviewed · ✅ approved (human sign-off)",
        "- **distribution** — 🌍 open (from origin) · 🔒 on a personal Dataverse · ⬆️ to upload",
        "",
        "## Datasets",
        "| id | tier | state | mat. | origin | validation | distribution | samples |",
        "|----|------|-------|:----:|:------:|------------|--------------|--------:|",
    ]
    for r in rows:
        lines.append(
            f"| `{r['id']}` | {r['tier']} | {r['state']} | {'✅' if r['materialized'] else '—'} | "
            f"{_ORIGIN_ICON[r['origin']]} | {_VAL_ICON[r['validation']]} | {_DIST_ICON[r['distribution']]} | "
            f"{r['n_samples'] if r['n_samples'] is not None else '—'} |"
        )
    return "\n".join(lines) + "\n"


def render_private_md(root: str | Path, rows: list[dict[str, Any]]) -> str:
    """Render ``docs/PRIVATE_DATASETS.md`` — the private/anonymized datasets still to upload to Dataverse."""
    pending = [r for r in rows if r["distribution"] == "upload_pending"]
    on_dv = [r for r in rows if r["distribution"] == "on_dataverse"]
    desc_dir = Path(root) / "catalog" / "datasets"
    lines = [
        "# Private datasets to upload to Dataverse",
        "",
        f"_{len(pending)} private/anonymized dataset(s) are catalogued but **not yet uploaded** to a personal",
        "Dataverse (no DOI). Their metadata + metrics are public in the catalog/site, but a consumer cannot",
        f"`get()` their bytes until they are uploaded and a token-gated DOI is minted. {len(on_dv)} already on Dataverse._",
        "",
        "## Upload one",
        "```bash",
        "n4a-datasets publish <id> --collection <your-collection> --contact-email you@example.org",
        "```",
        "Needs a Dataverse token (see [PUBLISHING.md](PUBLISHING.md)); first publish mints the DOI, which is",
        "written back into `catalog/datasets/<id>.yaml` so this list shrinks automatically.",
        "",
        f"## Pending uploads ({len(pending)})",
        "| id | name | tier | license | origin(s) | samples | validation |",
        "|----|------|------|---------|-----------|--------:|------------|",
    ]
    for r in pending:
        d = yaml.safe_load((desc_dir / f"{r['id']}.yaml").read_text(encoding="utf-8")) or {}
        name = str(d.get("name") or r["id"])
        lic = str((d.get("governance") or {}).get("license") or "—")
        origins = ", ".join(sorted({str(o.get("kind")) for o in (d.get("origin_sources") or []) if isinstance(o, dict)})) or "—"
        lines.append(f"| `{r['id']}` | {name} | {r['tier']} | {lic} | {origins} | {r['n_samples'] if r['n_samples'] is not None else '—'} | {_VAL_ICON[r['validation']]} |")
    return "\n".join(lines) + "\n"


def build_reports(root: str | Path) -> dict[str, Path]:
    """Refresh the validation registry + write both status reports. Returns the written paths."""
    root = Path(root)
    init_validation(root)
    rows = collect(root)
    docs = root / "docs"
    docs.mkdir(parents=True, exist_ok=True)
    status_md = docs / "DATASET_STATUS.md"
    private_md = docs / "PRIVATE_DATASETS.md"
    status_md.write_text(render_status_md(rows), encoding="utf-8")
    private_md.write_text(render_private_md(root, rows), encoding="utf-8")
    return {"status": status_md, "private": private_md, "validation": validation_path(root)}
