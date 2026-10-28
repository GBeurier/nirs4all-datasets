"""Resolve a catalog dataset to a local canonical directory and wrap it as a :class:`NirsDataset`.

Resolution order for :func:`get`:

1. **local** — ``<root>/datasets/<name>/canonical`` is present: load it directly (no network);
2. **packaged public-origin recipe** — download original files and assemble locally;
3. **personal Dataverse DOI** — fetch the canonical Parquet by the descriptor's pinned DOI (public
   without a token; private/anonymized with one);
4. **open origin source** — fetch the canonical bytes from an OPEN ``origin_sources`` entry by DOI.

The download itself — DOI/version-pinned resolution, the redirect-safe Dataverse fetch (the
``X-Dataverse-key`` never reaches signed storage), streaming SHA-256 verification against the manifest
and the pooch-style cache — lives in the native acquisition core (Rust, ``crates/nirs4all-datasets-core``)
behind the ``n4ds_`` C ABI and is reached here through :mod:`nirs4all_datasets._acquire`. This module
owns only the *policy* around it: local-first short-circuit, the token gate, the actionable
"where do the bytes live" error, and wrapping the result as a :class:`NirsDataset`.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from nirs4all_datasets.dataset import NirsDataset
from nirs4all_datasets.schema import _DOI_RE, DatasetDescriptor, SourceAccess, SourceKind, SourceMode, Tier

# Origin kinds the acquisition core can resolve by DOI (Dataverse / Zenodo / figshare). url / manual /
# script sources are never auto-fetched on the consumer path: scripts are maintainer-only (no code
# execution on get), and url/manual need a human (click-through licence, registration, raw scraping).
_FETCHABLE_KINDS = frozenset({SourceKind.DATAVERSE, SourceKind.ZENODO, SourceKind.FIGSHARE})


def _has_fetchable_origin(descriptor: DatasetDescriptor) -> bool:
    """Whether any origin is an OPEN canonical DOI the core can auto-fetch + verify byte-for-byte."""
    return any(
        src.access is SourceAccess.OPEN and src.mode is SourceMode.CANONICAL and src.kind in _FETCHABLE_KINDS and bool(_DOI_RE.match(src.locator))
        for src in descriptor.origin_sources
    )


def _resolved_contract(root: Path, descriptor: DatasetDescriptor) -> dict[str, Any]:
    """Build the resolved download contract the native core consumes (from descriptor + manifest).

    This uses the **real** local descriptor (DOI, origins, file ids) — unlike the public
    ``catalog/index.json``, which sanitizes anonymized-tier acquisition pointers. The maintainer's
    local checkout is trusted, so an anonymized dataset is still fetchable here (token-gated).
    """
    from nirs4all_datasets.index import _file_contract, _origins
    from nirs4all_datasets.manifest import read_manifest

    manifest_path = root / "datasets" / descriptor.id / "manifest.json"
    manifest = read_manifest(manifest_path) if manifest_path.exists() else None
    dv = descriptor.dataverse
    return {
        "id": descriptor.id,
        "tier": descriptor.tier.value,
        "instance": dv.instance,
        "doi": dv.doi or (manifest.doi if manifest else None),
        "dataset_version": dv.dataset_version or (manifest.dataset_version if manifest else None),
        "files": _file_contract(manifest) if manifest else [],
        "origins": _origins(descriptor),
    }


def _origin_link(locator: str) -> str:
    """A resolvable URL for an origin locator: a DOI -> doi.org, an http(s) URL as-is, else verbatim."""
    loc = str(locator).strip()
    if bool(_DOI_RE.match(loc)):
        return f"https://doi.org/{loc}"
    return loc


def _origin_message(name: str, descriptor: DatasetDescriptor) -> str:
    """Actionable error when nothing can be auto-fetched: a resolvable download link per origin.

    The bank's origins are mostly ``raw`` (the original vendor data) — fetching one yields raw files
    that must be re-ingested locally (a reproduction), so it is not the verified-canonical ``get()``
    path. The message therefore points at *where to download*, with a usable link.
    """
    if not descriptor.origin_sources:
        return f"{name!r} has no local canonical data, no published canonical DOI, and no documented origin source."
    lines: list[str] = []
    for s in descriptor.origin_sources:
        what = "canonical bytes" if s.mode is SourceMode.CANONICAL else "raw data (re-ingest locally)"
        note = f"  — {s.title}" if s.title else ""
        access = "" if s.access is SourceAccess.OPEN else f" [{s.access.value} access]"
        lines.append(f"  • {s.kind.value}{access}, {what}: {_origin_link(s.locator)}{note}")
    return (
        f"{name!r} is not auto-fetchable: it has no local canonical data and no published canonical DOI yet. "
        f"Download it from one of its origin sources:\n" + "\n".join(lines)
    )


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
    reproduce: bool = False,
    guestbook_response: dict[str, Any] | None = None,
) -> NirsDataset:
    """Resolve a catalog dataset by ``name`` and return it as a :class:`NirsDataset`.

    Load current local canonical data when present. Public datasets with a packaged recipe
    are assembled from their original public resources using packaged recipes; no checkout is needed.
    These results carry their own provenance and hashes, rather than claiming byte identity with
    historical canonical exports. Hosted canonical downloads retain manifest SHA-256 verification.
    Private/anonymized datasets require a Dataverse token.

    Args:
        name: Dataset id from the bundled catalog, optionally overridden by a local descriptor.
        root: Optional registry/local data root; the installed catalog is used outside a checkout.
        source: Forwarded to the returned dataset's accessors (validated against the dataset's sources).
        split: Forwarded similarly (the named native split to apply downstream).
        token: Dataverse API token for private/anonymized downloads; auto-resolved from settings if
            omitted for a non-public dataset.
        instance: Dataverse instance override (else the descriptor's instance).
        cache_dir: Download cache (defaults to the native core's OS cache).
        guestbook_response: Optional explicit Harvard guestbook answers, required for the two malaria
            datasets. No identity is supplied or submitted by default.
        concat: Default ``x()`` concat behaviour recorded on the returned dataset (informational).
        reproduce: When nothing is canonically fetchable, re-ingest from an OPEN origin's RAW bytes by
            delegating to nirs4all-io (a *reproduction*, not byte-pinned; needs the ``[io]`` extra).
            Returns a nirs4all ``SpectroDataset`` instead of a cached :class:`NirsDataset`.

    Returns:
        A :class:`NirsDataset` bound to the resolved local/cached canonical directory.

    Raises:
        FileNotFoundError: If there is no descriptor and no local data for ``name``.
        RuntimeError: If a private/anonymized dataset must be fetched but no token is available.
        ValueError: If nothing can be auto-fetched (guides the user to the origin sources).
    """
    root = Path(root)
    dataset_dir = root / "datasets" / name

    # 1. Local-first: a present canonical directory loads with no network and no descriptor lookup.
    if (dataset_dir / "canonical" / "dataset.json").exists():
        local_descriptor = _read_descriptor(root, name)
        current = True
        if local_descriptor.tier is Tier.PUBLIC:
            from nirs4all_datasets.public_pull import available

            if available(name):
                from nirs4all_datasets.manifest import processing_hash, read_manifest

                try:
                    manifest = dataset_dir / "manifest.json"
                    current = manifest.exists() and read_manifest(manifest).processing_hash == processing_hash(local_descriptor)
                    local_config = json.loads((dataset_dir / "canonical" / "dataset.json").read_text(encoding="utf-8"))
                    entries = [*local_config.get("sources", []), *local_config.get("splits", [])]
                    variables = local_config.get("variables")
                    if variables:
                        entries.append(variables)
                    current = current and bool(local_config.get("sources")) and all((dataset_dir / entry["path"]).is_file() for entry in entries)
                    if local_descriptor.targets:
                        import pyarrow.parquet as pq

                        variable_path = dataset_dir / variables["path"] if variables else None
                        columns = set(pq.read_schema(variable_path).names) if variable_path and variable_path.is_file() else set()
                        current = current and all(v.name in columns for v in local_descriptor.targets)
                except (OSError, ValueError, KeyError, TypeError):
                    current = False
        if current:
            return _wrap(dataset_dir, local_descriptor, source=source, split=split, concat=concat)

    descriptor = _read_descriptor(root, name)
    if descriptor.tier is Tier.PUBLIC:
        from nirs4all_datasets.public_pull import available, pull

        if available(name):
            directory, runtime_descriptor = pull(descriptor, cache_dir=cache_dir, guestbook_response=guestbook_response)
            return _wrap(directory, runtime_descriptor, source=source, split=split, concat=concat)

    manifest_path = dataset_dir / "manifest.json"
    if manifest_path.exists():
        contract = _resolved_contract(root, descriptor)
    else:
        from nirs4all_datasets.index import load_index, resolve

        try:
            entry = resolve(load_index(root), name)
        except (FileNotFoundError, KeyError):
            entry = {}
        dv = entry.get("dataverse") or {}
        contract = {"id": name, "tier": descriptor.tier.value, "instance": dv.get("instance") or descriptor.dataverse.instance,
                    "doi": dv.get("doi") or descriptor.dataverse.doi, "dataset_version": dv.get("dataset_version"),
                    "files": entry.get("files") or [], "origins": entry.get("origins") or []}
    fetchable = bool(contract["doi"]) or _has_fetchable_origin(descriptor)
    if not fetchable:
        if reproduce:
            from nirs4all_datasets.reproduce import reproduce_from_origin

            ds = reproduce_from_origin(descriptor, cache_dir=cache_dir)
            if ds is not None:
                return ds  # type: ignore[no-any-return]  # a nirs4all SpectroDataset (reproduction, not byte-pinned)
        raise ValueError(_origin_message(name, descriptor))

    # 2. Token gate (private/anonymized): resolve a token, and refuse before any network without one.
    needs_token = descriptor.tier is not Tier.PUBLIC
    resolved_instance = instance or descriptor.dataverse.instance
    resolved_token = token
    if needs_token and resolved_token is None:
        from nirs4all_datasets.config import get_settings

        settings = get_settings(instance=resolved_instance)
        resolved_token = settings.token.get_secret_value() if settings.token else None
    if needs_token and resolved_token is None:
        raise RuntimeError(
            f"{name!r} is tier {descriptor.tier.value!r}: a Dataverse token is required to fetch it. "
            f"Pass token=..., set NIRS4ALL_DATAVERSE_TOKEN, or configure ~/.config/nirs4all-datasets/config.toml."
        )

    # 3. Hand the resolved contract to the native core: download + verify + cache.
    opts: dict[str, Any] = {}
    if cache_dir is not None:
        opts["cache_dir"] = str(cache_dir)
    if instance is not None:
        opts["instance"] = instance
    if needs_token and resolved_token:
        opts["token"] = resolved_token

    from nirs4all_datasets import _acquire

    try:
        result = _acquire.fetch(contract, opts)
    except ValueError:  # the core found nothing auto-fetchable: guide to the origin sources
        raise ValueError(_origin_message(name, descriptor)) from None
    return _wrap(result["dir"], descriptor, source=source, split=split, concat=concat)


def _read_descriptor(root: Path, name: str) -> DatasetDescriptor:
    """Load and validate ``<root>/catalog/datasets/<name>.yaml``."""
    import yaml

    descriptor_path = root / "catalog" / "datasets" / f"{name}.yaml"
    if not descriptor_path.exists():
        from nirs4all_datasets.index import load_index, resolve

        try:
            entry = resolve(load_index(root), name)
        except (KeyError, FileNotFoundError):
            raise FileNotFoundError(f"unknown dataset {name!r}: no local or bundled descriptor.") from None
        return DatasetDescriptor(**entry["descriptor"])
    return DatasetDescriptor(**(yaml.safe_load(descriptor_path.read_text(encoding="utf-8")) or {}))


def _wrap(dataset_dir: str | Path, descriptor: DatasetDescriptor, *, source: str | None, split: str | None, concat: bool) -> NirsDataset:
    """Bind a resolved canonical directory to a :class:`NirsDataset`, validating ``source``/``split``."""
    dataset = NirsDataset(dataset_dir, descriptor)
    if source is not None and source not in dataset.sources():
        raise KeyError(f"unknown source {source!r} for {dataset.id!r}; available: {dataset.sources()}")
    if split is not None and dataset.split(split) is None:
        available = [str(s["name"]) for s in dataset._config.get("splits", [])]
        raise KeyError(f"unknown split {split!r} for {dataset.id!r}; available: {available}")
    return dataset
