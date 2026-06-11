"""Resolve a catalog dataset to a local canonical directory and wrap it as a :class:`NirsDataset`.

Resolution order for :func:`get`:

1. **local** — ``<root>/datasets/<name>/canonical`` is present: load it directly (no network);
2. **personal Dataverse DOI** — fetch the canonical Parquet by the descriptor's pinned DOI; public via
   pooch, private/anonymized via the Dataverse access API with a token;
3. **open origin source** — fetch the canonical bytes from an OPEN ``origin_sources`` entry by DOI.

Every download is SHA-256-verified against the manifest's recorded hashes — which match only because
canonical files are uploaded with ``tabIngest=false`` (pristine bytes). Verified files are cached and
reused. A token is required to fetch the bytes of a ``private`` or ``anonymized`` dataset that is not
already local; an actionable error is raised otherwise.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from nirs4all_datasets.dataset import NirsDataset
from nirs4all_datasets.manifest import Manifest, sha256_file
from nirs4all_datasets.schema import _DOI_RE, DatasetDescriptor, FileRole, SourceAccess, SourceKind, SourceMode, Tier


def default_cache_dir() -> Path:
    """OS-specific cache directory for downloaded datasets."""
    import pooch

    return Path(pooch.os_cache("nirs4all-datasets"))


def canonical_registry(manifest: Manifest) -> dict[str, str]:
    """Map canonical filename -> local SHA-256 (the frozen, pinned download registry)."""
    return {Path(fe.path).name: fe.sha256 for fe in manifest.files if fe.role is FileRole.CANONICAL}


def canonical_file_ids(manifest: Manifest) -> dict[str, int]:
    """Map canonical filename -> Dataverse file id (for the private access API)."""
    return {Path(fe.path).name: fe.file_id for fe in manifest.files if fe.role is FileRole.CANONICAL and fe.file_id is not None}


def fetch_public(doi: str, registry: dict[str, str], cache_dir: str | Path) -> dict[str, Path]:
    """Download canonical files of a public dataset by DOI via pooch (verified + cached).

    The SHA-256 registry guarantees byte identity even though pooch resolves files by basename
    from the DOI's latest version (canonical filenames are unique within a dataset).
    """
    import pooch

    bare_doi = doi[4:] if doi.lower().startswith("doi:") else doi
    pup = pooch.create(path=str(cache_dir), base_url=f"doi:{bare_doi}/", registry={name: f"sha256:{sha}" for name, sha in registry.items()})
    return {name: Path(pup.fetch(name)) for name in registry}


def fetch_private(
    file_ids: dict[str, int],
    registry: dict[str, str],
    cache_dir: str | Path,
    *,
    instance: str,
    token: str,
    session: Any | None = None,
) -> dict[str, Path]:
    """Download canonical files via the Dataverse access API (token), verify SHA-256, cache."""
    import os

    import requests

    sess = session if session is not None else requests.Session()
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    out: dict[str, Path] = {}
    for name, expected in registry.items():
        dest = cache_dir / name
        if dest.exists() and sha256_file(dest) == expected:
            out[name] = dest
            continue
        if name not in file_ids:
            raise RuntimeError(f"no Dataverse file id for {name!r} (cannot download privately).")
        # Do not follow redirects with the token: signed S3 storage must not receive the key.
        resp = sess.get(f"{instance}/api/access/datafile/{file_ids[name]}", headers={"X-Dataverse-key": token}, timeout=120, allow_redirects=False)
        if getattr(resp, "is_redirect", False):
            location = resp.headers.get("Location")
            if not location:
                raise RuntimeError(f"download {name} redirected without a Location header.")
            resp = sess.get(location, timeout=300)  # follow to storage host WITHOUT the Dataverse key
        if not resp.ok:
            raise RuntimeError(f"download {name} failed: HTTP {resp.status_code} {resp.reason}")
        tmp = dest.with_name(dest.name + ".tmp")
        tmp.write_bytes(resp.content)
        if sha256_file(tmp) != expected:
            tmp.unlink(missing_ok=True)
            raise RuntimeError(f"checksum mismatch for {name} after download.")
        os.replace(tmp, dest)
        out[name] = dest
    return out


def fetch_by_doi(dataset_id: str, doi: str, manifest: Manifest, *, cache_dir: str | Path | None = None, instance: str | None = None, token: str | None = None) -> Path:
    """Fetch a dataset's canonical files (by its pinned DOI) into the cache and return its directory.

    Public datasets (``token is None``) are fetched by DOI via pooch; otherwise the Dataverse access
    API is used. Returns the dataset directory (whose ``canonical/`` now holds the verified files).
    """
    cache_root = Path(cache_dir) if cache_dir is not None else default_cache_dir()
    canonical = cache_root / dataset_id / "canonical"
    registry = canonical_registry(manifest)
    if token is None:
        fetch_public(doi, registry, canonical)
    else:
        if instance is None:
            raise ValueError("instance is required for private downloads.")
        fetch_private(canonical_file_ids(manifest), registry, canonical, instance=instance, token=token)
    return cache_root / dataset_id


# Origin kinds pooch can resolve by DOI (Dataverse / Zenodo / figshare). url / manual / script sources
# are never auto-fetched in the consumer path: scripts are maintainer-only (no code execution on get),
# and url/manual need a human (click-through licence, registration, raw scraping).
_FETCHABLE_KINDS = frozenset({SourceKind.DATAVERSE, SourceKind.ZENODO, SourceKind.FIGSHARE})


def fetch_from_origin(name: str, descriptor: DatasetDescriptor, manifest: Manifest, *, cache_dir: str | Path | None = None) -> Path | None:
    """Fetch canonical bytes from an OPEN ``origin_sources`` entry, or ``None`` if none is auto-fetchable.

    Only ``canonical``-mode open DOI origins are auto-fetched here: the bytes are verified against the
    manifest's canonical SHA-256, so they are byte-identical to a published dataset. Raw-mode origins
    would require local re-ingestion (a *reproduction*, not byte-identical) and are not fetched on the
    consumer path. Returns the dataset directory on success, else ``None``.
    """
    cache_root = Path(cache_dir) if cache_dir is not None else default_cache_dir()
    for src in descriptor.origin_sources:
        if src.access is not SourceAccess.OPEN or src.kind not in _FETCHABLE_KINDS or src.mode is not SourceMode.CANONICAL or not _DOI_RE.match(src.locator):
            continue
        canonical = cache_root / name / "canonical"
        try:
            fetch_public(src.locator, canonical_registry(manifest), canonical)
        except Exception:  # noqa: BLE001 - byte mismatch / link rot: try the next origin
            continue
        return cache_root / name
    return None


def _origin_message(name: str, descriptor: DatasetDescriptor) -> str:
    """Actionable error when nothing can be auto-fetched: say exactly where the bytes live."""
    if not descriptor.origin_sources:
        return f"{name!r} has no local canonical data, no minted DOI, and no documented origin source."
    lines = [f"  - {s.kind.value} [{s.access.value}/{s.mode.value}]: {s.locator}" + (f"  ({s.title})" if s.title else "") for s in descriptor.origin_sources]
    return f"{name!r} has no local data and no minted DOI. Fetch it from one of its origin sources:\n" + "\n".join(lines)


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
    """Resolve a catalog dataset by ``name`` and return it as a :class:`NirsDataset`.

    Resolution order: local ``<root>/datasets/<name>/canonical`` -> the descriptor's personal Dataverse
    DOI (public via pooch, private/anonymized via token) -> an OPEN ``origin_sources`` entry. The first
    that yields verified canonical bytes wins.

    Args:
        name: Dataset id (a ``catalog/datasets/<name>.yaml`` descriptor under ``root``).
        root: Registry root holding ``catalog/`` and ``datasets/`` (defaults to the current directory).
        source: Forwarded to the returned dataset's accessors (recorded for the consumer's convenience).
        split: Forwarded similarly (the named native split to apply downstream).
        token: Dataverse API token for private/anonymized downloads; auto-resolved from settings if
            omitted for a non-public dataset.
        instance: Dataverse instance override (else the descriptor's instance).
        cache_dir: Download cache (defaults to pooch's OS cache).
        concat: Default ``x()`` concat behaviour recorded on the returned dataset (informational).

    Returns:
        A :class:`NirsDataset` bound to the resolved local/cached canonical directory.

    Raises:
        FileNotFoundError: If there is no descriptor and no local data for ``name``.
        RuntimeError: If a private/anonymized dataset must be fetched but no token is available.
        ValueError: If nothing can be auto-fetched (guides the user to the origin sources).
    """
    from nirs4all_datasets.manifest import read_manifest

    root = Path(root)
    dataset_dir = root / "datasets" / name

    # 1. Local-first: a present canonical directory loads with no network and no descriptor lookup.
    if (dataset_dir / "canonical" / "dataset.json").exists():
        return _wrap(dataset_dir, _read_descriptor(root, name), source=source, split=split, concat=concat)

    descriptor = _read_descriptor(root, name)
    manifest_path = dataset_dir / "manifest.json"
    if not manifest_path.exists():
        raise FileNotFoundError(f"no manifest for {name!r} at {manifest_path}; build it before remote access.")
    manifest = read_manifest(manifest_path)

    resolved_token = token
    needs_token = descriptor.tier is not Tier.PUBLIC
    resolved_instance = instance or descriptor.dataverse.instance
    if needs_token and resolved_token is None:
        from nirs4all_datasets.config import get_settings

        settings = get_settings(instance=resolved_instance)
        resolved_token = settings.token.get_secret_value() if settings.token else None

    # 2. Personal Dataverse DOI (public via pooch, private/anonymized via token).
    doi = descriptor.dataverse.doi or manifest.doi
    if doi:
        if needs_token and resolved_token is None:
            raise RuntimeError(
                f"{name!r} is tier {descriptor.tier.value!r}: a Dataverse token is required to fetch it. "
                f"Pass token=..., set NIRS4ALL_DATAVERSE_TOKEN, or configure ~/.config/nirs4all-datasets/config.toml."
            )
        fetched = fetch_by_doi(name, doi, manifest, cache_dir=cache_dir, instance=resolved_instance, token=resolved_token if needs_token else None)
        return _wrap(fetched, descriptor, source=source, split=split, concat=concat)

    # 3. No minted DOI: fall back to an OPEN origin source (private/anonymized never have an open origin).
    if not needs_token:
        from_origin = fetch_from_origin(name, descriptor, manifest, cache_dir=cache_dir)
        if from_origin is not None:
            return _wrap(from_origin, descriptor, source=source, split=split, concat=concat)
    raise ValueError(_origin_message(name, descriptor))


def _read_descriptor(root: Path, name: str) -> DatasetDescriptor:
    """Load and validate ``<root>/catalog/datasets/<name>.yaml``."""
    import yaml

    descriptor_path = root / "catalog" / "datasets" / f"{name}.yaml"
    if not descriptor_path.exists():
        raise FileNotFoundError(f"unknown dataset {name!r}: no local canonical data and no descriptor at {descriptor_path}.")
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
