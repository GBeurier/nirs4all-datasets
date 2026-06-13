"""Sphinx configuration for the nirs4all-datasets documentation.

Built on ReadTheDocs (ubuntu-24.04, Python 3.12) from ``docs/requirements.txt``. MyST-Markdown is the
authoring format; the furo theme renders the site. Maintainer-only worklists (e.g. the private-dataset
upload backlog) are excluded from the published build.
"""
from __future__ import annotations

# -- Project information -----------------------------------------------------
project = "nirs4all-datasets"
author = "G. Beurier"
copyright = "2026, G. Beurier"

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.mathjax",
]

source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext",
}

root_doc = "index"

# Files that must never reach the published site:
#   - PRIVATE_DATASETS.md: a maintainer worklist of private/embargoed datasets pending Dataverse
#     upload (dataset names + governance state). Not for a public RTD site.
#   - docs/datasets/: machine-generated per-dataset pages (gitignored build artefacts).
#   - dev/: maintainer-only release-process notes.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "PRIVATE_DATASETS.md",
    "datasets",
    "dev",
]

# -- MyST configuration ------------------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "substitution",
    "tasklist",
    "attrs_inline",
    "dollarmath",
]
myst_heading_anchors = 3

# -- autosectionlabel --------------------------------------------------------
autosectionlabel_prefix_document = True

# -- HTML output -------------------------------------------------------------
html_theme = "furo"
html_title = "nirs4all-datasets"
