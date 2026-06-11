"""nirs4all-datasets — store, qualify, and organize NIRS reference datasets.

Data lives on Recherche Data Gouv / Dataverse (DOI-citable, FAIR); code lives on
GitHub; datasets are fetched on demand and cached locally (pooch-style). This
package reuses ``nirs4all`` for qualification and ``nirs4all-io`` for reading
instrument formats.
"""
from __future__ import annotations

from collections.abc import Sequence
from importlib.metadata import PackageNotFoundError, version
from typing import TYPE_CHECKING, Any

from nirs4all_datasets.config import Settings, get_settings

if TYPE_CHECKING:  # type hints only; the runtime functions lazy-import to keep this module light
    from pathlib import Path

try:
    __version__ = version("nirs4all-datasets")
except PackageNotFoundError:  # running from a source checkout without install
    __version__ = "0.1.0.dev0"


# Public API. These are thin lazy wrappers: the heavy modules (numpy/pyarrow/nirs4all) are imported
# only when a function is actually called, so ``import nirs4all_datasets`` stays cheap.
def load(name: str, *, root: str | Path = ".", token: str | None = None, instance: str | None = None, cache_dir: str | Path | None = None, reproduce: bool = False) -> Any:
    """Load a catalog dataset as a nirs4all ``DatasetConfigs`` (local-first, else fetch).

    Resolution order: local canonical -> the personal Dataverse DOI (public via pooch, restricted via
    token) -> an OPEN original source (``reproduce=True`` re-ingests a raw source into a *reproduced*
    canonical). Public datasets need no token. See :func:`nirs4all_datasets.access.load`.
    """
    from nirs4all_datasets.access import load as _load

    return _load(name, root=root, token=token, instance=instance, cache_dir=cache_dir, reproduce=reproduce)


def load_local(dataset_dir: str | Path) -> Any:
    """Load an already-present dataset directory as a nirs4all ``DatasetConfigs``."""
    from nirs4all_datasets.access import load_local as _load_local

    return _load_local(dataset_dir)


def list(root: str | Path = ".", *, task_type: str | None = None, visibility: str | None = None, signal_type: str | None = None) -> Sequence[dict[str, Any]]:
    """List catalog datasets (optionally filtered by task / visibility / signal type)."""
    from nirs4all_datasets.catalog import search

    return search(root, task_type=task_type, visibility=visibility, signal_type=signal_type)


def card(name: str, root: str | Path = ".") -> dict[str, Any] | None:
    """Return a dataset's generated identity card (dict), or ``None`` if absent."""
    from nirs4all_datasets.catalog import get_card

    return get_card(root, name)


__all__ = ["Settings", "get_settings", "load", "load_local", "list", "card", "__version__"]
