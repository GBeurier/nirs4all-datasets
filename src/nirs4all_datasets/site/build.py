"""Orchestrate the static-site build: load -> render -> write ``out/``.

Pure rendering: the only inputs are the committed artifacts (``catalog/datasets.yaml`` + per-dataset
``card.json``). All visuals are **inline SVG** rendered from the card's own data (spectral quantile
curves + per-variable histograms), so the site is self-contained — no PNG assets, no nirs4all/pandas/
matplotlib import, and **no dataset bytes are ever written** (the canonical Parquet is never touched).
"""
from __future__ import annotations

import shutil
from pathlib import Path

from . import pages
from .model import Catalog, DatasetView, load_catalog
from .theme import SITE_URL


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

    Writes ``index.html``, ``catalog.html``, one ``dataset/<id>.html`` per dataset, and the public-tier
    metadata downloads under ``data/``. All charts are inline SVG (no asset files).
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
        _copy_metadata(view, root, out)

    _write_seo(catalog, out)
    _copy_brand(root, out)
    return out


def _write_seo(catalog: Catalog, out: Path) -> None:
    """Emit crawl-discovery files for the public catalog."""
    paths = ["", "catalog.html"] + [f"dataset/{view.id}.html" for view in catalog.datasets]
    urls = "\n".join(
        "  <url>\n"
        f"    <loc>{SITE_URL}/{path}</loc>\n"
        "    <lastmod>2026-07-01</lastmod>\n"
        "  </url>"
        if path
        else "  <url>\n"
        f"    <loc>{SITE_URL}/</loc>\n"
        "    <lastmod>2026-07-01</lastmod>\n"
        "  </url>"
        for path in paths
    )
    (out / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n"
        "</urlset>\n",
        encoding="utf-8",
    )
    (out / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n",
        encoding="utf-8",
    )
    (out / "CNAME").write_text("datasets.nirs4all.org\n", encoding="utf-8")
    (out / ".nojekyll").write_text("", encoding="utf-8")


def _copy_brand(root: Path, out: Path) -> None:
    """Ship the site chrome (favicon, app icon, social card) under ``out/brand/``."""
    brand_src = root / "assets" / "brand"
    if not brand_src.is_dir():
        return
    brand_out = out / "brand"
    brand_out.mkdir(parents=True, exist_ok=True)
    for name in ("favicon.ico", "icon.svg", "icon-180.png", "og.png"):
        src = brand_src / name
        if src.exists():
            shutil.copy2(src, brand_out / name)
