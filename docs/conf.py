"""Sphinx configuration for the nirs4all-datasets static site (MyST + Furo)."""
from __future__ import annotations

project = "nirs4all-datasets"
author = "CIRAD"
extensions = ["myst_parser", "sphinx_design", "sphinx_copybutton"]
myst_enable_extensions = ["colon_fence", "deflist"]
html_theme = "furo"
html_title = "nirs4all datasets"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
source_suffix = {".md": "markdown", ".rst": "restructuredtext"}
