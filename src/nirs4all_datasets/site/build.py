"""Orchestrate the static-site build: load -> render -> write ``out/``.

Pure rendering: the only inputs are the committed artifacts (``catalog/datasets.yaml`` + per-dataset
``card.json``). All visuals are **inline SVG** rendered from the card's own data (spectral quantile
curves + per-variable histograms), so the site is self-contained — no PNG assets, no nirs4all/pandas/
matplotlib import, and **no dataset bytes are ever written** (the canonical Parquet is never touched).
"""
from __future__ import annotations

import shutil
from importlib.resources import files
from importlib.resources.abc import Traversable
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
    _copy_ui_assets(out)

    (out / "index.html").write_text(pages.render_index(catalog), encoding="utf-8")
    (out / "catalog.html").write_text(pages.render_catalog(catalog), encoding="utf-8")
    (out / "guide.html").write_text(pages.render_guide(), encoding="utf-8")

    for view in catalog.datasets:
        (out / "dataset" / f"{view.id}.html").write_text(pages.render_dataset(view), encoding="utf-8")
        _copy_metadata(view, root, out)

    _write_seo(catalog, out)
    _copy_brand(root, out)
    return out


def _copy_ui_assets(out: Path) -> None:
    """Copy bundled browser resources without Node, including from a non-filesystem package.

    Read Traversables directly: directory ``as_file`` support starts at Python 3.12, while
    this package supports Python 3.11. Missing assets are an installation/packaging defect.
    """
    source = files("nirs4all_datasets.site").joinpath("ui_assets/nirs4all-ui")
    required = ("nirs4all-ui-browser.iife.js", "browser.css", "LICENSE", "LICENSING.md", "THIRD_PARTY_NOTICES.md", "PROVENANCE.json")
    missing = [name for name in required if not source.joinpath(name).is_file()]
    if not source.joinpath("LICENSES").is_dir():
        missing.append("LICENSES/")
    if missing:
        raise FileNotFoundError(f"Missing bundled nirs4all-ui site resources: {', '.join(missing)}. Reinstall a package containing site/ui_assets/nirs4all-ui/.")

    def copy_tree(src: Traversable, dst: Path) -> None:
        dst.mkdir(parents=True, exist_ok=True)
        for child in src.iterdir():
            target = dst / child.name
            if child.is_dir():
                copy_tree(child, target)
            else:
                target.write_bytes(child.read_bytes())

    copy_tree(source, out / "vendor" / "nirs4all-ui")


def _write_seo(catalog: Catalog, out: Path) -> None:
    """Emit crawl-discovery files for the public catalog."""
    paths = ["", "catalog.html", "guide.html"] + [f"dataset/{view.id}.html" for view in catalog.datasets]
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
