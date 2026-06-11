"""Fetch datasets on demand (cached) and load them as nirs4all ``DatasetConfigs``.

Local-first: an already-organized dataset directory loads directly. Otherwise public datasets
are fetched **by pinned DOI** via pooch (download + checksum-verify + OS cache), and
private/restricted ones via the Dataverse access API with the token. Downloads are verified
against the manifest's local SHA-256 -- which matches only because files are uploaded with
``tabIngest=false`` (pristine bytes). Cached files are reused on subsequent calls.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from nirs4all_datasets.ingest import resolve_config
from nirs4all_datasets.manifest import Manifest, sha256_file
from nirs4all_datasets.schema import _DOI_RE, DatasetDescriptor, FileRole, SourceAccess, SourceKind, SourceMode


def default_cache_dir() -> Path:
    """OS-specific cache directory for downloaded datasets."""
    import pooch

    return Path(pooch.os_cache("nirs4all-datasets"))


def load_local(dataset_dir: str | Path) -> Any:
    """Load an already-present dataset directory as a nirs4all ``DatasetConfigs``."""
    from nirs4all.data import DatasetConfigs

    return DatasetConfigs(resolve_config(dataset_dir))


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


def fetch_and_load(dataset_id: str, doi: str, manifest: Manifest, *, cache_dir: str | Path | None = None, instance: str | None = None, token: str | None = None) -> Any:
    """Fetch a dataset's canonical files into the cache and load them as ``DatasetConfigs``.

    Public datasets (``token is None``) are fetched by DOI via pooch; otherwise the Dataverse
    access API is used. Returns a nirs4all ``DatasetConfigs`` ready for ``nirs4all.run``.
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
    return load_local(cache_root / dataset_id)


# Origin kinds pooch can resolve by DOI (Zenodo / figshare / Dataverse). url / manual / script sources
# are never auto-fetched in the consumer path: scripts are maintainer-only (no code execution on load),
# and url/manual need a human (click-through licence, registration, raw scraping).
_FETCHABLE_KINDS = frozenset({SourceKind.DATAVERSE, SourceKind.ZENODO, SourceKind.FIGSHARE})


def _origin_sources_message(name: str, descriptor: DatasetDescriptor) -> str:
    """Actionable error when nothing can be auto-fetched: say exactly where the data lives."""
    if not descriptor.sources:
        return f"{name!r} is not published (no DOI) and has no local canonical data to load"
    lines = [f"  - {s.kind.value} [{s.access.value}/{s.mode.value}]: {s.locator}" + (f"  ({s.title})" if s.title else "") for s in descriptor.sources]
    hint = "\n(open DOI sources can be auto-reproduced with reproduce=True)" if any(s.access is SourceAccess.OPEN and s.kind in _FETCHABLE_KINDS for s in descriptor.sources) else ""
    return f"{name!r} has no local data and no minted DOI. Fetch it from one of its original sources:\n" + "\n".join(lines) + hint


def fetch_from_origin(name: str, descriptor: DatasetDescriptor, manifest: Manifest, *, cache_dir: str | Path | None = None, reproduce: bool = False) -> Any | None:
    """Load a dataset from one of its OPEN original sources, or return ``None`` if none is auto-fetchable.

    A ``canonical``-mode source is fetched by DOI and verified against the manifest's canonical SHA-256
    (byte-pinned). A ``raw``-mode source is attempted only when ``reproduce`` is set: its raw files are
    fetched, verified against the manifest's raw SHA-256, then **re-ingested locally** -- the result is a
    *reproduced* canonical (NOT byte-identical to a published Parquet, due to float32/zstd/version drift),
    the honest best obtainable from upstream vendor files. Script/manual/token/url sources are never
    auto-fetched here.
    """
    cache_root = Path(cache_dir) if cache_dir is not None else default_cache_dir()
    for src in descriptor.sources:
        if src.access is not SourceAccess.OPEN or src.kind not in _FETCHABLE_KINDS or not _DOI_RE.match(src.locator):
            continue
        if src.mode is SourceMode.CANONICAL:
            canonical = cache_root / name / "canonical"
            try:
                fetch_public(src.locator, canonical_registry(manifest), canonical)
            except Exception:  # noqa: BLE001 - byte mismatch / rot: try the next source
                continue
            return load_local(cache_root / name)
        if reproduce:
            raw_registry = {Path(fe.path).name: fe.sha256 for fe in manifest.files if fe.role is FileRole.RAW}
            if not raw_registry:
                continue
            staging = cache_root / name / "_origin_raw"
            try:
                fetch_public(src.locator, raw_registry, staging)
            except Exception:  # noqa: BLE001
                continue
            from nirs4all_datasets.ingest import ingest

            out = cache_root / name
            ingest(staging, out, task_type=descriptor.targets[0].task_type.value, target_names=[t.name for t in descriptor.targets])
            return load_local(out)
    return None


def load(name: str, *, root: str | Path = ".", token: str | None = None, instance: str | None = None, cache_dir: str | Path | None = None, reproduce: bool = False) -> Any:
    """Load a catalog dataset by ``name`` as a nirs4all ``DatasetConfigs``.

    Local-first: if ``<root>/datasets/<name>/canonical`` is present it loads directly (no network).
    Otherwise it fetches by the dataset's pinned DOI -- **public** datasets via pooch (download +
    checksum-verify + cache), **restricted** ones via the Dataverse access API with a token (passed
    explicitly, or, for a non-public dataset, resolved from settings: env / config.toml / ``.env``).

    Args:
        name: Dataset id (a ``catalog/datasets/<name>.yaml`` descriptor under ``root``).
        root: Registry root (defaults to the current directory).
        token: Dataverse API token for private downloads; auto-resolved from settings if omitted.
        instance: Dataverse instance override (else the descriptor's instance).
        cache_dir: Download cache (defaults to pooch's OS cache).

    Returns:
        A nirs4all ``DatasetConfigs`` ready for ``nirs4all.run``.
    """
    import yaml

    from nirs4all_datasets.manifest import read_manifest
    from nirs4all_datasets.schema import Visibility

    root = Path(root)
    dataset_dir = root / "datasets" / name
    if (dataset_dir / "canonical" / "nirs4all_config.json").exists():
        return load_local(dataset_dir)  # already present locally -> no download

    descriptor_path = root / "catalog" / "datasets" / f"{name}.yaml"
    if not descriptor_path.exists():
        raise FileNotFoundError(f"unknown dataset {name!r}: no local canonical data and no descriptor at {descriptor_path}")
    descriptor = DatasetDescriptor(**(yaml.safe_load(descriptor_path.read_text(encoding="utf-8")) or {}))
    manifest_path = dataset_dir / "manifest.json"
    if not manifest_path.exists():
        raise FileNotFoundError(f"no manifest for {name!r} at {manifest_path}; build it before remote access")
    manifest = read_manifest(manifest_path)

    doi = descriptor.dataverse.doi or manifest.doi
    if doi:
        resolved_instance = instance or descriptor.dataverse.instance
        resolved_token = token
        if resolved_token is None and descriptor.governance.visibility is not Visibility.PUBLIC:
            from nirs4all_datasets.config import get_settings

            settings = get_settings(instance=resolved_instance)
            resolved_token = settings.token.get_secret_value() if settings.token else None
        return fetch_and_load(name, doi, manifest, cache_dir=cache_dir, instance=resolved_instance, token=resolved_token)

    # No minted DOI: fall back to the original open sources (or guide the user to a manual source).
    origin = fetch_from_origin(name, descriptor, manifest, cache_dir=cache_dir, reproduce=reproduce)
    if origin is not None:
        return origin
    raise ValueError(_origin_sources_message(name, descriptor))
