"""nirs4all-datasets — store, qualify, and serve curated RAW NIRS reference datasets.

Data bytes live at each dataset's origin (a data Dataverse / Zenodo / vendor archive); descriptors and
generated metadata live in git; datasets are fetched on demand and cached locally (pooch-style). This
package reuses ``nirs4all`` (optional ``[nirs4all]`` extra) for the card metrics + the ``to_nirs4all``
bridge, and never re-implements NIRS or IO logic; the catalog, ``get()``/``NirsDataset`` readers and the
site work without it.

The consumer entry point is :func:`get`, which resolves a dataset (local-first, else fetch by DOI or
open origin) and returns a :class:`~nirs4all_datasets.dataset.NirsDataset` wrapping the local canonical
form. Heavy dependencies (numpy / pyarrow / nirs4all) are imported lazily, so ``import
nirs4all_datasets`` stays cheap.
"""
from __future__ import annotations

from collections.abc import Sequence
from importlib import import_module
from importlib.metadata import PackageNotFoundError, version
from typing import TYPE_CHECKING, Any

from nirs4all_datasets.config import Settings, get_settings

if TYPE_CHECKING:  # type hints only; runtime resolves these lazily to keep import light
    from pathlib import Path

    from nirs4all_datasets.dataset import NirsDataset

try:
    __version__ = version("nirs4all-datasets")
except PackageNotFoundError:  # running from a source checkout without install
    __version__ = "0.1.0.dev0"


def get(
    name: str,
    *,
    root: str | Path = ".",
    source: str | None = None,
    split: str | None = None,
    token: str | None = None,
    instance: str | None = None,
    cache_dir: str | Path | None = None,
    concat: bool = True,
) -> NirsDataset:
    """Resolve a catalog dataset and return it as a :class:`NirsDataset` (local-first, else fetch).

    Resolution order: local canonical -> the personal Dataverse DOI (public via pooch, private/
    anonymized via token) -> an OPEN origin source. Public datasets need no token. See
    :func:`nirs4all_datasets.access.get`.
    """
    from nirs4all_datasets.access import get as _get

    return _get(name, root=root, source=source, split=split, token=token, instance=instance, cache_dir=cache_dir, concat=concat)


def list(root: str | Path = ".", **filters: Any) -> Sequence[dict[str, Any]]:
    """List catalog datasets, forwarding any keyword filters to :func:`nirs4all_datasets.catalog.search`."""
    from nirs4all_datasets.catalog import search

    return search(root, **filters)


def card(name: str, root: str | Path = ".") -> dict[str, Any] | None:
    """Return a dataset's generated identity card (dict), or ``None`` if absent."""
    from nirs4all_datasets.catalog import get_card

    return get_card(root, name)


def __getattr__(name: str) -> Any:
    """Lazily expose ``NirsDataset`` and the ``metrics`` namespace without importing them eagerly."""
    if name == "NirsDataset":
        return import_module("nirs4all_datasets.dataset").NirsDataset
    if name == "metrics":
        return import_module("nirs4all_datasets.qualify.metrics")
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = ["Settings", "get_settings", "get", "NirsDataset", "list", "card", "metrics", "__version__"]
