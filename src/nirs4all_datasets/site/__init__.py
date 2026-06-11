"""Static-site generator for the schema-2.0 catalog of raw NIRS reference datasets.

A striking, dependency-light (pyyaml + stdlib) static site that renders already-generated artifacts —
the catalog index, per-dataset identity cards, and their PNG assets — into a self-contained ``out/``
tree (``index.html`` + ``catalog.html`` + ``dataset/<id>.html``). Charts are inline SVG rendered at
build time; the only client-side JS is the catalog's filter/sort UI and the hero animation. No
nirs4all / pandas / matplotlib import. Tier gating (public / private / anonymized) is load-bearing and
enforced in :mod:`model` (which card to serve) and :mod:`build` (which assets to copy) — no dataset
bytes are ever written.

The public entry point is :func:`build_site`; ``cli.py`` imports it lazily as
``from nirs4all_datasets.site import build_site``.
"""
from __future__ import annotations

from .build import build_site

__all__ = ["build_site"]
