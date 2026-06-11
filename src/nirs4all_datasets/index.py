"""The distributable, cross-language download contract: ``catalog/index.json`` (index schema 1.0).

One JSON file, derived from the git-tracked descriptors + manifests, that carries **everything a
resolver in any language needs** to turn a dataset id into a complete, version-pinned download
contract:

* ``tier`` and the Dataverse ``instance`` / ``doi`` / ``dataset_version`` pin;
* the per-file download list (``name``, ``relpath``, ``sha256``, ``size``, Dataverse ``file_id``,
  ``directory_label``) — the frozen integrity contract;
* the ``origins`` (where open bytes can be fetched: Dataverse / Zenodo / figshare / url / script);
* the **tier-sanitized public descriptor** (``public_descriptor``), so the bundled index can never
  leak an anonymized identity.

This is the single contract the Rust acquisition core (``nirs4all-datasets-core``) and every language
binding read; the Python :func:`nirs4all_datasets.get` path consumes it too, which is what lets a
plain ``pip install`` resolve datasets with no git checkout. It is small (JSON), so it is shipped
bundled into each binding's package and/or fetched from the GitHub raw URL on demand (ETag-cached),
and it is **version-pinned**: the committed file at a release tag — together with each entry's
``dataset_version`` and every file's ``sha256`` — re-fetches the exact bytes of that release.

The serialization is the canonical-JSON form shared across the bindings (UTF-8, keys sorted by code
point, two-space indent, ``\\n`` endings, exactly one trailing newline) so the Rust core and the
Python writer agree byte-for-byte.
"""
from __future__ import annotations

import json
from pathlib import Path, PurePosixPath
from typing import Any

import yaml

from nirs4all_datasets.manifest import read_manifest
from nirs4all_datasets.schema import DatasetDescriptor, FileRole, Manifest

# The index format version (independent of the package version and of the dataset schema version).
INDEX_SCHEMA = "1.0"


def _file_contract(manifest: Manifest) -> list[dict[str, Any]]:
    """The per-file download contract for a manifest's CANONICAL files (the only fetchable bytes).

    ``directory_label`` is the POSIX parent of the relative path — the Dataverse ``directoryLabel`` the
    upload used — so a resolver can match a file by directory label + name (never bare basename, which
    would collide across ``raw/`` and ``canonical/sources/``).
    """
    files: list[dict[str, Any]] = []
    for fe in manifest.files:
        if fe.role is not FileRole.CANONICAL:
            continue
        rel = PurePosixPath(fe.path.replace("\\", "/"))
        files.append(
            {
                "name": rel.name,
                "relpath": str(rel),
                "directory_label": str(rel.parent) if str(rel.parent) != "." else "",
                "sha256": fe.sha256,
                "size": fe.size,
                "file_id": fe.file_id,
            }
        )
    return sorted(files, key=lambda f: f["relpath"])


def _origins(descriptor: DatasetDescriptor) -> list[dict[str, Any]]:
    """The origin sources a resolver may try (kind/mode/locator/access), in authored order."""
    return [
        {"kind": o.kind.value, "mode": o.mode.value, "locator": o.locator, "access": o.access.value}
        for o in descriptor.origin_sources
    ]


def index_entry(root: str | Path, descriptor: DatasetDescriptor) -> dict[str, Any]:
    """Build one index entry from a descriptor + its manifest (sanitized to the public/anonymized view).

    Every field is derived from the **public** descriptor (``public_descriptor``): for the anonymized
    tier the variable names are masked and identifying free text is removed, so the bundled index leaks
    nothing. Private-tier descriptors are shown in full (private gates the *bytes*, not the metadata) —
    exactly the policy the catalog index and the static site already apply.
    """
    from nirs4all_datasets.qualify.anonymize import public_descriptor  # lazy: keep `import index` light
    from nirs4all_datasets.schema import Tier

    pub = public_descriptor(descriptor)
    manifest_path = Path(root) / "datasets" / descriptor.id / "manifest.json"
    manifest = read_manifest(manifest_path) if manifest_path.exists() else None

    dv = pub.dataverse
    doi = dv.doi or (manifest.doi if manifest else None)
    dataset_version = dv.dataset_version or (manifest.dataset_version if manifest else None)
    files = _file_contract(manifest) if manifest else []
    origins = _origins(pub)

    # The anonymized tier hides *what* a dataset is, so the PUBLIC index must not leak its
    # acquisition pointers either: a DOI / origin locator resolves to the named dataset, and a
    # Dataverse file id is tied to it. Strip them here (the file SHA-256 contract stays, for
    # display/integrity). Fetching an anonymized dataset is token-gated and uses the real,
    # locally-known descriptor (see access._resolved_contract), never this public index.
    if pub.tier is Tier.ANONYMIZED:
        doi = None
        dataset_version = None
        origins = []
        files = [{**f, "file_id": None} for f in files]

    return {
        "tier": pub.tier.value,
        "dataverse": {"instance": dv.instance, "doi": doi, "dataset_version": dataset_version},
        "files": files,
        "origins": origins,
        "descriptor": pub.model_dump(mode="json"),
    }


def build_index(root: str | Path, *, write: bool = True) -> dict[str, Any]:
    """Assemble (and optionally write) ``catalog/index.json`` — the cross-language download contract.

    One entry per descriptor under ``<root>/catalog/datasets``, keyed by dataset id, each enriched with
    its manifest's canonical-file contract. Deterministic and import-light (no numpy/pandas/nirs4all),
    so it regenerates in the green gate alongside ``catalog/datasets.yaml``.
    """
    from nirs4all_datasets.catalog import descriptor_paths

    root = Path(root)
    datasets: dict[str, Any] = {}
    for path in descriptor_paths(root):
        descriptor = DatasetDescriptor(**(yaml.safe_load(path.read_text(encoding="utf-8")) or {}))
        datasets[descriptor.id] = index_entry(root, descriptor)

    index = {"schema": INDEX_SCHEMA, "n_datasets": len(datasets), "datasets": datasets}
    if write:
        out = root / "catalog" / "index.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(index, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    return index


def load_index(source: str | Path) -> dict[str, Any]:
    """Read an assembled index from a ``catalog/index.json`` file or a registry root containing one."""
    path = Path(source)
    if path.is_dir():
        path = path / "catalog" / "index.json"
    data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    return data


def resolve(index: dict[str, Any], dataset_id: str) -> dict[str, Any]:
    """Return the download contract entry for ``dataset_id`` from a loaded index.

    Raises:
        KeyError: If the index has no entry for ``dataset_id``.
    """
    datasets = index.get("datasets", {})
    if dataset_id not in datasets:
        raise KeyError(f"dataset {dataset_id!r} is not in the index ({len(datasets)} datasets).")
    entry: dict[str, Any] = datasets[dataset_id]
    return entry
