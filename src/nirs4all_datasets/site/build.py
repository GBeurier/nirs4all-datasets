"""Orchestrate the static-site build: load -> render -> copy tier-permitted assets -> write ``out/``.

Pure rendering: the only inputs are the committed artifacts (``catalog/datasets.yaml``, per-dataset
``card.json`` / ``card.anon.json``, and the PNG assets under ``datasets/<id>/assets/``). No nirs4all,
pandas, or matplotlib import. Tier gating is enforced by the view model: only ``view.asset_dataset_id``
(set for public/private, empty for anonymized and cardless) is ever copied, and **no dataset bytes are
ever written** — the canonical Parquet under ``datasets/<id>/canonical/`` is never touched.
"""
from __future__ import annotations

import shutil
from pathlib import Path

from . import pages
from .model import Catalog, DatasetView, load_catalog


def _copy_assets(view: DatasetView, root: Path, out: Path) -> None:
    """Copy a dataset's tier-permitted PNG assets into ``out/assets/<id>/`` (PNGs only; never bytes).

    Anonymized + cardless datasets have ``asset_dataset_id == ""`` and copy nothing. Even for the
    permitted tiers we copy only ``*.png`` so a stray Parquet/CSV in the assets tree can never leak.
    """
    if not view.asset_dataset_id:
        return
    src = root / "datasets" / view.asset_dataset_id / "assets"
    if not src.is_dir():
        return
    dst = out / "assets" / view.id
    for png in src.rglob("*.png"):
        target = dst / png.relative_to(src)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(png, target)


def _copy_metadata(view: DatasetView, root: Path, out: Path) -> None:
    """Copy ``card.json`` / ``croissant.json`` for public datasets only (byte-free metadata downloads)."""
    if not view.show_metadata_downloads or not view.has_card:
        return
    data_dir = out / "data"
    for suffix in ("card.json", "croissant.json"):
        src = root / "datasets" / view.id / suffix
        if src.exists():
            data_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, data_dir / f"{view.id}.{suffix}")


def build_site(root: str | Path, out: str | Path) -> Path:
    """Build the catalog static site from ``root`` into ``out`` (regenerated wholesale); return ``out``.

    Writes ``index.html``, ``catalog.html``, one ``dataset/<id>.html`` per dataset, the public-tier
    metadata downloads under ``data/``, and the tier-permitted PNG assets under ``assets/``.
    """
    root = Path(root)
    out = Path(out)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    (out / "dataset").mkdir()

    catalog: Catalog = load_catalog(root)

    (out / "index.html").write_text(pages.render_index(catalog), encoding="utf-8")
    (out / "catalog.html").write_text(pages.render_catalog(catalog), encoding="utf-8")

    for view in catalog.datasets:
        (out / "dataset" / f"{view.id}.html").write_text(pages.render_dataset(view), encoding="utf-8")
        _copy_assets(view, root, out)
        _copy_metadata(view, root, out)

    return out
