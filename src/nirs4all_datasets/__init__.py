"""nirs4all-datasets — store, qualify, and organize NIRS reference datasets.

Data lives on Recherche Data Gouv / Dataverse (DOI-citable, FAIR); code lives on
GitHub; datasets are fetched on demand and cached locally (pooch-style). This
package reuses ``nirs4all`` for qualification and ``nirs4all-io`` for reading
instrument formats.
"""
from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

from nirs4all_datasets.config import Settings, get_settings

try:
    __version__ = version("nirs4all-datasets")
except PackageNotFoundError:  # running from a source checkout without install
    __version__ = "0.1.0.dev0"

__all__ = ["Settings", "get_settings", "__version__"]
