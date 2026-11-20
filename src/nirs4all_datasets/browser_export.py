"""Offline export of explicitly selected PUBLIC datasets as static browser assets.

This module is a maintainer preparation step for browser hosts (for example the nirs4all web
app) that have no Python runtime or backend. It writes, outside Git:

* ``catalog.json`` (schema ``nirs4all.datasets.public-browser.v1``) listing every exported
  dataset and one entry per spectral source, with a relative ``url``, ``sha256`` and
  ``size_bytes`` for each source asset;
* ``sources/<dataset_id>/<source_id>.json`` (schema ``nirs4all.datasets.browser-dataset.v1``),
  one asset per source, carrying the dataset provenance and the unmodified output of the native
  ``nirs4all_io.assembled_full`` operation.

Ownership stays where it belongs: :func:`nirs4all_datasets.get` resolves and caches the public
dataset, :meth:`NirsDataset.to_io_spec` publishes the canonical paths/roles/units/join keys with
exactly one explicitly selected spectral source, and native ``nirs4all-io`` materializes it. This
module adds no loader, join, encoding, filling, subsetting, split or target selection; it only
refuses what must not be exported and serializes the native result as strict JSON.

Only explicitly named datasets are exported (there is no "whole catalog" mode). Non-public tiers
and public descriptors with publication blockers are refused before any acquisition. Nothing is
uploaded; hosting the produced directory is a separate, explicitly authorized release step (see
``docs/BROWSER_EXPORT.md``).

Example:
    ``python -m nirs4all_datasets.browser_export --ids barley_moisture_perten --out /srv/stage/browser``
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import shutil
import sys
import tempfile
from collections.abc import Callable, Iterator, Sequence
from contextlib import contextmanager
from pathlib import Path
from typing import Any

from nirs4all_datasets.schema import _ID_RE, DatasetDescriptor, Tier

CATALOG_SCHEMA = "nirs4all.datasets.public-browser.v1"
SOURCE_SCHEMA = "nirs4all.datasets.browser-dataset.v1"
IO_OPERATION = "nirs4all_io.assembled_full"
CATALOG_FILENAME = "catalog.json"
SOURCES_DIRNAME = "sources"
SUPPORTED_ASSEMBLED_SCHEMAS = frozenset({3})
"""Native ``assembled_schema_version`` values the browser decoder (nirs4all-io ``decodeAssembledFull``)
accepts. Older wires lack declared numeric bytes and validity masks and are refused, never migrated."""
RAW_NA_POLICY = {"policy": "ignore"}
"""Declared raw-export NA policy for every spec source: IO keeps missing cells as invalid entries
(validity masks), removes no row or feature and fills nothing. IO's default policy aborts on any NA."""

_SAFE_SEGMENT = frozenset("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-")


class BrowserExportError(RuntimeError):
    """An export precondition failed; nothing is written to the requested output."""


# -- preconditions ---------------------------------------------------------------------------------
def native_assembled_full() -> Callable[..., Any]:
    """Return the native ``nirs4all_io.assembled_full`` operation, or refuse.

    Raises:
        BrowserExportError: If ``nirs4all_io`` is absent or does not expose the native operation
            (for example a Python-only MVP build), or if its declared wire profile is not in
            :data:`SUPPORTED_ASSEMBLED_SCHEMAS`. No substitute materialization is attempted. Builds
            without a declared profile are checked on each native result instead.
    """
    try:
        import nirs4all_io
    except ImportError as exc:
        raise BrowserExportError("browser export needs nirs4all-io with its native binding (install the 'nirs4all-datasets[io]' extra).") from exc
    operation = getattr(nirs4all_io, "assembled_full", None)
    if not callable(operation):
        version = getattr(nirs4all_io, "__version__", "unknown")
        raise BrowserExportError(
            f"the installed nirs4all_io ({version}) does not expose the native assembled_full operation; "
            "install a nirs4all-io build with the native binding. No fallback materialization is used."
        )
    profile = _assembled_profile(nirs4all_io)
    if profile is not None and profile not in SUPPORTED_ASSEMBLED_SCHEMAS:
        raise BrowserExportError(_schema_message(profile, nirs4all_io))
    return operation  # type: ignore[no-any-return]


def _assembled_profile(nirs4all_io: Any) -> int | None:
    """The installed IO wire profile (``_assembled.ASSEMBLED_DATASET_VERSION``), when it declares one."""
    try:
        from importlib import import_module

        value = getattr(import_module(f"{nirs4all_io.__name__}._assembled"), "ASSEMBLED_DATASET_VERSION", None)
    except ImportError:
        return None
    return value if type(value) is int else None


def _schema_message(version: Any, nirs4all_io: Any) -> str:
    return (
        f"nirs4all_io {getattr(nirs4all_io, '__version__', 'unknown')} emits assembled_schema_version={version!r}; "
        f"browser assets require one of {sorted(SUPPORTED_ASSEMBLED_SCHEMAS)} (declared numeric bytes + validity masks). "
        "Install a nirs4all-io release whose native profile emits a supported wire. No migration or fallback is applied."
    )


def raw_export_spec(spec: dict[str, Any]) -> dict[str, Any]:
    """Return ``spec`` with the declared raw-export NA policy on every source; roles/joins are unchanged."""
    declared = copy.deepcopy(spec)
    for source in declared.get("sources", []):
        params = source.setdefault("params", {})
        current = params.setdefault("na", dict(RAW_NA_POLICY))
        if current != RAW_NA_POLICY:
            raise BrowserExportError(f"spec source {source.get('id')!r} declares NA handling {current!r}; raw export requires {RAW_NA_POLICY!r}.")
    return declared


def public_refusals(descriptor: DatasetDescriptor) -> list[str]:
    """Return the reasons ``descriptor`` must not be exported as an open browser asset.

    Only the ``public`` tier is exportable, and it must pass the owner publication policy
    (:meth:`DatasetDescriptor.publication_blockers`: open SPDX licence, open origins and the
    responsible-release governance fields).
    """
    if descriptor.tier is not Tier.PUBLIC:
        return [f"tier {descriptor.tier.value!r} is not exportable; only the public tier is."]
    return list(descriptor.publication_blockers())


def _check_ids(ids: Sequence[str]) -> list[str]:
    selected = [str(item).strip() for item in ids]
    if not selected or any(not item for item in selected):
        raise BrowserExportError("explicit dataset ids are required; the whole catalog is never exported by default.")
    duplicates = sorted({item for item in selected if selected.count(item) > 1})
    if duplicates:
        raise BrowserExportError(f"duplicate dataset ids: {duplicates}")
    invalid = [item for item in selected if not _ID_RE.match(item)]
    if invalid:
        raise BrowserExportError(f"invalid dataset ids: {invalid}")
    return selected


def _git_worktree(path: Path) -> Path | None:
    for candidate in (path, *path.parents):
        if (candidate / ".git").exists():
            return candidate
    return None


def _check_out(out: Path) -> Path:
    resolved = out.expanduser().resolve()
    if resolved.exists() and (not resolved.is_dir() or any(resolved.iterdir())):
        raise BrowserExportError(f"output {resolved} must be absent or an empty directory; existing exports are never overwritten.")
    worktree = _git_worktree(resolved)
    if worktree is not None:
        raise BrowserExportError(f"output {resolved} is inside the Git work tree {worktree}; browser payloads stay outside Git.")
    return resolved


def _safe_segment(value: str, what: str) -> str:
    if not value or value in {".", ".."} or any(ch not in _SAFE_SEGMENT for ch in value):
        raise BrowserExportError(f"{what} {value!r} is not a safe asset path segment.")
    return value


@contextmanager
def _catalog_root(root: str | Path | None) -> Iterator[Path]:
    """Yield the explicit catalog root, or a fresh empty one so no cwd data can shadow the catalog."""
    if root is not None:
        yield Path(root).expanduser().resolve()
        return
    with tempfile.TemporaryDirectory(prefix="n4ds-browser-root-") as empty:
        yield Path(empty)


# -- export ----------------------------------------------------------------------------------------
def _relative_spec(spec: dict[str, Any], dataset_dir: Path) -> dict[str, Any]:
    """Copy the IO spec with its local inputs made relative to the dataset directory."""
    relative = copy.deepcopy(spec)
    for source in relative.get("sources", []):
        path = Path(source["input"]).resolve()
        try:
            source["input"] = path.relative_to(dataset_dir).as_posix()
        except ValueError:
            raise BrowserExportError(f"IO spec input {path} is outside the dataset directory.") from None
    return relative


def _file_digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _provenance(dataset: Any, source_id: str, spec: dict[str, Any], full: dict[str, Any], dataset_dir: Path) -> dict[str, Any]:
    import nirs4all_io

    from nirs4all_datasets import __version__

    descriptor: DatasetDescriptor = dataset.descriptor  # the public view (identical for the public tier)
    source = next((s for s in descriptor.sources if s.source_id == source_id), None)
    split_ids = [s["id"] for s in spec["sources"] if str(s.get("id", "")).startswith("split_")]
    return {
        "dataset": {
            "id": descriptor.id,
            "name": descriptor.name,
            "tier": descriptor.tier.value,
            "ids": descriptor.ids.model_dump(mode="json"),
            "alignment_level": descriptor.alignment_level.value,
            "license": descriptor.governance.license,
            "citation": descriptor.citation,
            "doi": descriptor.dataverse.doi,
            "permitted_use": descriptor.governance.permitted_use,
            "access_policy": descriptor.governance.access_policy,
        },
        "origin_sources": [
            {"kind": o.kind.value, "mode": o.mode.value, "locator": o.locator, "access": o.access.value, "license": o.license, "title": o.title}
            for o in descriptor.origin_sources
        ],
        "publications": [p.model_dump(mode="json", exclude_none=True) for p in descriptor.publications],
        "source": None if source is None else {
            "source_id": source.source_id,
            "name": source.name,
            "instrument_name": source.instrument_name,
            "modality": source.modality.value,
            "axis_unit": source.axis_unit.value,
            "signal_type": source.signal_type.value,
        },
        "materialization": {
            "operation": IO_OPERATION,
            "nirs4all_io_version": getattr(nirs4all_io, "__version__", None),
            "nirs4all_datasets_version": __version__,
            "assembled_schema_version": full.get("assembled_schema_version"),
            "io_spec": _relative_spec(spec, dataset_dir),
            "inputs": [
                {"path": Path(s["input"]).resolve().relative_to(dataset_dir).as_posix(), "sha256": _file_digest(Path(s["input"])),
                 "size_bytes": Path(s["input"]).stat().st_size}
                for s in spec["sources"]
            ],
        },
        "native_splits": {
            "exposed_as_metadata": split_ids,
            "applied": False,
            "note": "Native splits are documented as a metadata column; all rows are exported and no split is applied or invented.",
        },
        "warnings": list(descriptor.provenance.warnings),
    }


def _source_asset(dataset: Any, source_id: str, assembled_full: Callable[..., Any]) -> bytes:
    """Materialize one explicitly selected source through native IO and encode the asset."""
    dataset_dir = Path(dataset._dir).resolve()
    spec = raw_export_spec(dataset.to_io_spec(source=source_id))
    spectral = [s for s in spec["sources"] if s.get("id") == source_id]
    if len(spectral) != 1 or any(s.get("modality") == "spectroscopy" and s.get("id") != source_id for s in spec["sources"]):
        raise BrowserExportError(f"{dataset.id}/{source_id}: the IO spec does not select exactly this one spectral source.")
    full = assembled_full(spec, None, dataset.id)
    if not isinstance(full, dict) or type(full.get("assembled_schema_version")) is not int or not isinstance(full.get("blocks"), dict):
        raise BrowserExportError(f"{dataset.id}/{source_id}: native assembled_full returned an unversioned or malformed result.")
    if full["assembled_schema_version"] not in SUPPORTED_ASSEMBLED_SCHEMAS:
        import nirs4all_io

        raise BrowserExportError(f"{dataset.id}/{source_id}: " + _schema_message(full["assembled_schema_version"], nirs4all_io))
    rows = sum(int(block.get("n_samples") or 0) for block in full["blocks"].values())
    expected = len(dataset.observation_ids(source_id))
    if rows != expected:
        raise BrowserExportError(f"{dataset.id}/{source_id}: native assembly returned {rows} rows for {expected} canonical observations; refusing a subset.")
    payload = {
        "schema": SOURCE_SCHEMA,
        "dataset_id": dataset.id,
        "source_id": source_id,
        "provenance": _provenance(dataset, source_id, spec, full, dataset_dir),
        "assembled": full,
    }
    try:
        text = json.dumps(payload, allow_nan=False, ensure_ascii=False, separators=(",", ":"))
    except ValueError as exc:
        raise BrowserExportError(f"{dataset.id}/{source_id}: native output is not strict JSON ({exc}).") from None
    if str(dataset_dir) in text:
        raise BrowserExportError(f"{dataset.id}/{source_id}: the asset would expose the local dataset path.")
    return text.encode("utf-8")


def export(ids: Sequence[str], out: str | Path, *, root: str | Path | None = None, cache_dir: str | Path | None = None) -> dict[str, Any]:
    """Export explicitly selected public datasets as a static browser catalog and per-source assets.

    Args:
        ids: Explicit dataset ids. There is no implicit whole-catalog export.
        out: Output directory, absent or empty and outside any Git work tree. It is created
            atomically: on failure nothing is left at ``out``.
        root: Catalog root. Defaults to a fresh empty directory so the packaged catalog is used and
            no ``catalog/`` or ``datasets/`` directory under the current working directory can
            shadow it. Pass a checkout root explicitly to use its descriptors/local canonical data.
        cache_dir: Download cache forwarded to :func:`nirs4all_datasets.get`.

    Returns:
        The written catalog document.

    Raises:
        BrowserExportError: On any refused precondition (tier/policy, native IO, output location,
            row loss, non-strict JSON, path leakage).
    """
    from nirs4all_datasets.access import _read_descriptor, get
    from nirs4all_datasets.dataset import NirsDataset

    selected = _check_ids(ids)
    destination = _check_out(Path(out))
    assembled_full = native_assembled_full()
    with _catalog_root(root) as catalog_root:
        refusals: dict[str, list[str]] = {}
        for dataset_id in selected:
            try:
                reasons = public_refusals(_read_descriptor(catalog_root, dataset_id))
            except FileNotFoundError as exc:
                reasons = [str(exc)]
            if reasons:
                refusals[dataset_id] = reasons
        if refusals:  # refused before any acquisition
            raise BrowserExportError("refused before acquisition: " + json.dumps(refusals, ensure_ascii=False))

        destination.parent.mkdir(parents=True, exist_ok=True)
        staging = Path(tempfile.mkdtemp(prefix=".browser-export-", dir=destination.parent))
        try:
            staging.chmod(0o755)  # mkdtemp is owner-only; the export is a static-hosting directory
            entries: list[dict[str, Any]] = []
            for dataset_id in selected:
                dataset = get(dataset_id, root=catalog_root, cache_dir=cache_dir)
                if not isinstance(dataset, NirsDataset):
                    raise BrowserExportError(f"{dataset_id}: resolution did not return a canonical public dataset.")
                reasons = public_refusals(dataset._descriptor)  # the runtime descriptor actually served
                if reasons:
                    raise BrowserExportError(f"{dataset_id}: {reasons}")
                descriptor = dataset.descriptor
                names = {s.source_id: s.name for s in descriptor.sources}
                sources: list[dict[str, Any]] = []
                for source_id in dataset.sources():
                    relative = f"{SOURCES_DIRNAME}/{_safe_segment(dataset_id, 'dataset id')}/{_safe_segment(source_id, 'source id')}.json"
                    data = _source_asset(dataset, source_id, assembled_full)
                    target = staging / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    with target.open("xb") as handle:
                        handle.write(data)
                    source_entry: dict[str, Any] = {"id": source_id}
                    if names.get(source_id):
                        source_entry["name"] = names[source_id]
                    source_entry.update({"url": relative, "sha256": hashlib.sha256(data).hexdigest(), "size_bytes": len(data)})
                    sources.append(source_entry)
                entry: dict[str, Any] = {"id": dataset_id, "name": descriptor.name, "tier": Tier.PUBLIC.value, "license": descriptor.governance.license}
                if descriptor.description.strip():
                    entry["description"] = descriptor.description
                entry["sources"] = sources
                entries.append(entry)
            catalog = {"schema": CATALOG_SCHEMA, "datasets": entries}
            with (staging / CATALOG_FILENAME).open("x", encoding="utf-8") as handle:
                json.dump(catalog, handle, ensure_ascii=False, indent=2, allow_nan=False)
                handle.write("\n")
            if destination.exists():
                destination.rmdir()  # verified empty above
            os.replace(staging, destination)
        except BaseException:
            shutil.rmtree(staging, ignore_errors=True)
            raise
    return catalog


# -- CLI -------------------------------------------------------------------------------------------
def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m nirs4all_datasets.browser_export",
        description="Export explicitly selected PUBLIC datasets as static browser JSON (catalog + one asset per source). Nothing is uploaded.",
    )
    parser.add_argument("--ids", nargs="+", required=True, help="Dataset ids (space- or comma-separated). Required: no whole-catalog export.")
    parser.add_argument("--out", required=True, type=Path, help="Absent or empty output directory outside any Git work tree.")
    parser.add_argument("--cache-dir", type=Path, default=None, help="Download cache (default: the package cache).")
    parser.add_argument("--root", type=Path, default=None, help="Catalog root (default: a fresh empty directory, i.e. the packaged catalog).")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Command-line entry point; returns the process exit status."""
    args = _parser().parse_args(argv)
    ids = [item for value in args.ids for item in str(value).split(",") if item.strip()]
    try:
        catalog = export(ids, args.out, root=args.root, cache_dir=args.cache_dir)
    except BrowserExportError as exc:
        print(f"browser export refused: {exc}", file=sys.stderr)
        return 2
    summary = {
        "catalog": str(Path(args.out).expanduser().resolve() / CATALOG_FILENAME),
        "datasets": [{"id": d["id"], "sources": [s["url"] for s in d["sources"]]} for d in catalog["datasets"]],
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":  # pragma: no cover - exercised through main()
    raise SystemExit(main())
