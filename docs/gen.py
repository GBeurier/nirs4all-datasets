#!/usr/bin/env python3
"""Generate MyST dataset pages for the static site from the catalog + per-dataset cards.

Run before ``sphinx-build``: reads ``catalog/datasets.yaml`` and each
``datasets/<id>/card.json``, writes ``docs/datasets/<id>.md`` + a filterable
``docs/datasets/index.md``, and copies the card's PNG assets next to the pages.
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = Path(__file__).resolve().parent


def _esc(value: object) -> str:
    """Escape a value for safe inclusion in a Markdown table cell."""
    return str(value).replace("|", "\\|").replace("\n", " ")


def _card(dataset_id: str) -> dict[str, Any]:
    path = ROOT / "datasets" / dataset_id / "card.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def _kpi_table(entry: dict[str, Any], card: dict[str, Any]) -> list[str]:
    inv = card.get("inventory", {})
    spec = card.get("spectral", {})
    rows = {
        "Task": entry.get("task_type"),
        "Samples": inv.get("n_samples", entry.get("n_samples")),
        "Features": inv.get("n_features", entry.get("n_features")),
        "Signal type": spec.get("signal_type", "—"),
        "Wavelength unit": spec.get("wavelength_unit", "—"),
        "License": entry.get("license"),
        "Visibility": entry.get("visibility"),
        "DOI": f"[{entry['doi']}](https://doi.org/{entry['doi']})" if entry.get("doi") else "—",
    }
    return ["| Field | Value |", "|---|---|", *[f"| {k} | {_esc(v)} |" for k, v in rows.items()], ""]


def _dataset_page(entry: dict[str, Any], card: dict[str, Any], out_dir: Path) -> None:
    dataset_id = entry["id"]
    lines = [f"# {entry['name']}", "", entry.get("domain") or "", "", *_kpi_table(entry, card)]

    src_dir = ROOT / "datasets" / dataset_id
    assets_src = src_dir / "assets"
    if assets_src.exists():
        dst = out_dir / dataset_id
        dst.mkdir(parents=True, exist_ok=True)
        for png in sorted(assets_src.glob("*.png")):
            shutil.copy2(png, dst / png.name)
            lines += [f"![{png.stem}]({dataset_id}/{png.name})", ""]

    croissant = src_dir / "croissant.json"
    if croissant.exists():
        dst = out_dir / dataset_id
        dst.mkdir(parents=True, exist_ok=True)
        shutil.copy2(croissant, dst / "croissant.json")
        lines += [f"**Metadata:** [Croissant (JSON-LD)]({dataset_id}/croissant.json)", ""]

    if card:
        # Colon-fence directive so the inner ```json fence cannot close the dropdown.
        lines += [":::{dropdown} Full card.json", "```json", json.dumps(card, indent=2), "```", ":::", ""]
    (out_dir / f"{dataset_id}.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    catalog_path = ROOT / "catalog" / "datasets.yaml"
    catalog = yaml.safe_load(catalog_path.read_text(encoding="utf-8")) if catalog_path.exists() else {"datasets": []}
    datasets: list[dict[str, Any]] = catalog.get("datasets", [])

    out_dir = DOCS / "datasets"
    if out_dir.exists():
        shutil.rmtree(out_dir)  # regenerate wholesale so removed datasets do not linger
    out_dir.mkdir(parents=True)

    rows: list[str] = []
    for entry in datasets:
        _dataset_page(entry, _card(entry["id"]), out_dir)
        doi = f"[{entry['doi']}](https://doi.org/{entry['doi']})" if entry.get("doi") else "—"
        rows.append(f"| [{_esc(entry['name'])}]({entry['id']}.md) | {entry.get('task_type')} | {entry.get('n_samples') or '?'} | {entry.get('signal_type') or '—'} | {entry.get('visibility')} | {doi} |")

    index = [
        "# Dataset catalog",
        "",
        "```{toctree}",
        ":hidden:",
        "",
        *[f"{e['id']}.md" for e in datasets],
        "```",
        "",
        "| Name | Task | N | Signal | Visibility | DOI |",
        "|---|---|---|---|---|---|",
        *rows,
        "",
    ]
    (out_dir / "index.md").write_text("\n".join(index), encoding="utf-8")
    print(f"generated {len(datasets)} dataset page(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
