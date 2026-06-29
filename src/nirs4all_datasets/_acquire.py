"""Idiomatic wrapper over the embedded native acquisition core (``nirs4all_datasets._n4ds``).

The heavy *download* of a dataset — DOI/version-pinned resolution, redirect-safe
Dataverse / Zenodo / figshare fetch, streaming SHA-256 verification and the pooch-style
cache — lives in the Rust core (`crates/nirs4all-datasets-core`) behind a stable C ABI
(`n4ds_`) and is exposed here via pyo3. JSON crosses the boundary; dicts cross this API.

The scientific *analysis* layer (cards / qualify / site / health) stays in pure Python
in this package — this module only acquires bytes. :mod:`nirs4all_datasets.access`
builds on it.
"""
from __future__ import annotations

import json
from typing import Any

from nirs4all_datasets import _n4ds  # the compiled pyo3 extension (built by maturin)

__all__ = ["abi_version", "resolve", "fetch", "retrieve_raw", "prepare_raw", "verify_cached"]


def abi_version() -> str:
    """The version of the underlying native acquisition core."""
    return str(_n4ds.abi_version())


def _as_json(value: dict[str, Any] | str) -> str:
    return value if isinstance(value, str) else json.dumps(value)


def resolve(index: dict[str, Any] | str, dataset_id: str) -> dict[str, Any]:
    """Resolve ``dataset_id`` against a loaded index (dict or JSON) to its download contract.

    Returns ``{id, tier, instance, doi, dataset_version, files:[...], origins:[...]}``.

    Raises:
        KeyError: If the dataset id is not in the index.
        ValueError: If the index JSON is malformed.
    """
    result: dict[str, Any] = json.loads(_n4ds.resolve(_as_json(index), dataset_id))
    return result


def fetch(resolved: dict[str, Any] | str, opts: dict[str, Any] | None = None) -> dict[str, Any]:
    """Download + SHA-256-verify a resolved dataset into the cache.

    ``opts`` accepts ``{cache_dir?, token?, instance?, timeout_secs?}``. Returns
    ``{dir, files:[{name, relpath, path, status}]}`` (``status`` is ``cached`` or
    ``downloaded``).

    Raises:
        RuntimeError: A private/anonymized dataset needs a token that was not given, or
            a download / HTTP / checksum error occurred.
        ValueError: Nothing in the contract is auto-fetchable.
    """
    result: dict[str, Any] = json.loads(_n4ds.fetch(_as_json(resolved), json.dumps(opts or {})))
    return result


def retrieve_raw(request: dict[str, Any] | str, opts: dict[str, Any] | None = None) -> dict[str, Any]:
    """Retrieve raw origin resources into the native cache.

    ``request`` is ``{dataset_id, route}``, where ``route`` is one item from
    ``descriptor.retrieval.routes``. ``opts`` accepts ``{cache_dir?, timeout_secs?,
    max_total_bytes?}``. Returns ``{dir, ok, verified, route_id, resources:[...]}``.

    This is raw repatriation, not canonical verification. ``verified`` is true only
    when every retrieved resource had a SHA-256 pin and matched it.
    """
    result: dict[str, Any] = json.loads(_n4ds.retrieve_raw(_as_json(request), json.dumps(opts or {})))
    return result


def prepare_raw(request: dict[str, Any] | str, opts: dict[str, Any] | None = None) -> dict[str, Any]:
    """Prepare already-retrieved raw resources through the Rust reader stack.

    ``request`` is the same ``{dataset_id, route}`` payload as :func:`retrieve_raw`.
    ``opts`` accepts ``{cache_dir?}``. Returns
    ``{dir, ok, route_id, resources:[...]}``, where supported native resources
    have been decoded by ``nirs4all-formats`` and tabular resources summarized by
    ``nirs4all-io``.
    """
    result: dict[str, Any] = json.loads(_n4ds.prepare_raw(_as_json(request), json.dumps(opts or {})))
    return result


def verify_cached(resolved: dict[str, Any] | str, directory: str) -> dict[str, Any]:
    """Re-verify a cached dataset directory against the contract's SHA-256s (offline).

    Returns ``{dir, ok, files:[{name, relpath, status}]}`` with ``status`` in
    ``ok`` | ``missing`` | ``corrupt``.
    """
    result: dict[str, Any] = json.loads(_n4ds.verify_cached(_as_json(resolved), str(directory)))
    return result
