"""Opt-in *reproduce from origin* acquisition (``get(name, reproduce=True)``).

Download an OPEN origin's raw bytes and **assemble a dataset by delegating to nirs4all-io** (which pulls
nirs4all-formats for vendor decoders). This package re-implements **no** reading or assembly — it only
acquires bytes and hands a directory to :func:`nirs4all_io.load`.

This is a **reproduction**, not the checksum-pinned canonical download: the bytes are re-read and
re-assembled, so the result is *not* guaranteed byte-identical to the published canonical (the
manifest SHA-256 does not apply). It works only when the origin actually hosts the spectral data in a
layout nirs4all-io can infer — for much of the bank the DOI points at a *publication/project* (a thesis
PDF, a code repo, a multi-GB database) and the vendor→structure mapping is bespoke per dataset (the
``source_to_standard.py`` scripts); those are not reproducible this way and need the published
canonical (Dataverse) instead. Needs the ``[io]`` extra (``pip install nirs4all-datasets[io]``).
"""
from __future__ import annotations

import zipfile
from pathlib import Path
from typing import Any

from nirs4all_datasets.schema import DatasetDescriptor, OriginSource, SourceAccess, SourceKind

# Origin kinds whose bytes can be auto-downloaded (resolved to direct file URLs).
_DOWNLOADABLE = frozenset({SourceKind.ZENODO, SourceKind.FIGSHARE, SourceKind.URL})
_DEFAULT_MAX_BYTES = 1_000_000_000  # 1 GB guard — a thesis PDF / multi-GB DB is not a dataset to pull
_SKIP_EXT = frozenset({".pdf", ".docx", ".pptx", ".db", ".sqlite"})  # clearly-not-spectra payloads


def _zenodo_record(locator: str) -> str | None:
    i = locator.rfind("zenodo.")
    return locator[i + len("zenodo.") :].strip("/") if i >= 0 else None


def _figshare_article(locator: str) -> str | None:
    i = locator.rfind("figshare.")
    if i < 0:
        return None
    token = locator[i + len("figshare.") :].split(".")[0].split("/")[0]
    return token if token.isdigit() else None


def _origin_files(origin: OriginSource, session: Any) -> list[tuple[str, str]]:
    """Resolve an open origin to ``[(filename, download_url), …]`` (empty if not resolvable)."""
    loc = origin.locator.strip()
    if origin.kind is SourceKind.ZENODO:
        rec = _zenodo_record(loc)
        if not rec:
            return []
        data = session.get(f"https://zenodo.org/api/records/{rec}", timeout=60).json()
        return [(f["key"], f["links"]["self"]) for f in data.get("files", []) if f.get("key") and f.get("links")]
    if origin.kind is SourceKind.FIGSHARE:
        art = _figshare_article(loc)
        if not art:
            return []
        data = session.get(f"https://api.figshare.com/v2/articles/{art}", timeout=60).json()
        return [(f["name"], f["download_url"]) for f in data.get("files", []) if f.get("name") and f.get("download_url")]
    if origin.kind is SourceKind.URL and loc.startswith("http"):
        return [(loc.rsplit("/", 1)[-1] or "download", loc)]
    return []


def _download(session: Any, url: str, dest: Path, max_bytes: int) -> None:
    """Stream a URL to ``dest`` with a size guard (raises if it exceeds ``max_bytes``)."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    with session.get(url, stream=True, timeout=300) as resp:
        resp.raise_for_status()
        size = 0
        with open(dest, "wb") as fh:
            for chunk in resp.iter_content(chunk_size=1 << 20):
                size += len(chunk)
                if size > max_bytes:
                    fh.close()
                    dest.unlink(missing_ok=True)
                    raise RuntimeError(f"{url} exceeds the {max_bytes / 1e9:.1f} GB reproduce guard; publish its canonical instead.")
                fh.write(chunk)


def assemble(directory: str | Path, *, name: str | None = None) -> Any:
    """Assemble a local directory of (vendor or tabular) files into a dataset via nirs4all-io.

    The single delegation point: nirs4all-io owns inference + materialization and pulls nirs4all-formats
    for vendor decoders. Returns a nirs4all ``SpectroDataset``.
    """
    try:
        import nirs4all_io as nio
    except ImportError as exc:  # pragma: no cover - exercised only without the extra
        raise RuntimeError("reproduce/assemble needs the 'nirs4all-datasets[io]' extra (nirs4all-io + nirs4all-formats).") from exc
    return nio.load(str(directory), target="spectrodataset", name=name)


def reproduce_from_origin(descriptor: DatasetDescriptor, *, cache_dir: str | Path | None = None, session: Any | None = None, max_bytes: int = _DEFAULT_MAX_BYTES) -> Any | None:
    """Download an OPEN origin's bytes and assemble a dataset via nirs4all-io (or ``None`` if none work).

    Tries each open downloadable origin in turn: resolves it to files, downloads them (skipping clearly
    non-spectral payloads and anything over ``max_bytes``), unpacks zips, then hands the directory to
    :func:`assemble`. A **reproduction** (not byte-pinned).
    """
    import requests

    sess = session if session is not None else requests.Session()
    root = Path(cache_dir) if cache_dir is not None else _default_reproduce_dir()
    for origin in descriptor.origin_sources:
        if origin.access is not SourceAccess.OPEN or origin.kind not in _DOWNLOADABLE:
            continue
        try:
            files = _origin_files(origin, sess)
        except Exception:  # noqa: BLE001 - API/link rot: try the next origin
            continue
        files = [(n, u) for n, u in files if Path(n).suffix.lower() not in _SKIP_EXT]
        if not files:
            continue
        dest = root / descriptor.id / "origin"
        try:
            for fname, url in files:
                target = dest / fname
                _download(sess, url, target, max_bytes)
                if target.suffix.lower() == ".zip":
                    with zipfile.ZipFile(target) as zf:
                        zf.extractall(dest)
            return assemble(dest, name=descriptor.id)
        except Exception:  # noqa: BLE001 - download/format/inference failure: try the next origin
            continue
    return None


def _default_reproduce_dir() -> Path:
    """Cache root for reproduced (re-ingested) datasets — kept apart from the verified canonical cache."""
    import os

    base = os.environ.get("XDG_CACHE_HOME") or str(Path.home() / ".cache")
    return Path(base) / "nirs4all-datasets" / "_reproduced"
