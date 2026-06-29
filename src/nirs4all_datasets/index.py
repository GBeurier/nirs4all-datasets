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

import csv
import json
import re
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import quote, unquote, urlparse

import yaml

from nirs4all_datasets.manifest import read_manifest
from nirs4all_datasets.schema import DatasetDescriptor, FileRole, Manifest

# The index format version (independent of the package version and of the dataset schema version).
INDEX_SCHEMA = "1.0"
_DIRECT_FORMATS = {
    ".csv.gz": "csv_gz",
    ".csv": "csv",
    ".xlsx": "xlsx",
    ".xls": "xlsx",
    ".zip": "zip",
    ".mat": "mat",
    ".rda": "rda",
    ".rdata": "rda",
    ".rds": "rds",
    ".sqlite": "sqlite",
    ".db": "sqlite",
    ".spc": "spc",
    ".parquet": "parquet",
    ".json": "json",
    ".txt": "txt",
    ".jcamp": "jcamp_dx",
    ".jcm": "jcamp_dx",
    ".jdx": "jcamp_dx",
    ".dx": "jcamp_dx",
}

# JPL ECOSTRESS spectral library (https://speclib.jpl.nasa.gov). Its public "download" page serves
# one bundle per material category through a server-side ``orderall('<category>')`` action; the
# dataset id's second token is exactly that category token. We map the family to a structured
# ``jpl_ecostress`` route so resolvers stop seeing an opaque ``missing_delegate`` and instead get the
# provider, the verified category selector, and the public landing page.
_ECOSTRESS_DOWNLOAD_URL = "https://speclib.jpl.nasa.gov/download"
_ECOSTRESS_DATA_URL = "https://speclib.jpl.nasa.gov/ecospeclibdata"
_ECOSTRESS_HOST = "speclib.jpl.nasa.gov"
_ECOSTRESS_CATEGORIES = frozenset(
    {
        "lunar",
        "manmade",
        "meteorites",
        "mineral",
        "nonphotosyntheticvegetation",
        "rock",
        "soil",
        "vegetation",
        "water",
    }
)


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


def _retrieval(root: str | Path, descriptor: DatasetDescriptor) -> dict[str, Any]:
    """The explicit user-side retrieval plan, separate from raw provenance origins."""
    data = descriptor.retrieval.model_dump(mode="json")
    if data["routes"]:
        return data

    routes = _synthetic_raw_routes(root, descriptor)
    if routes:
        return {
            **data,
            "status": "raw_reproducible",
            "public_retrievable": True,
            "public_redistributable": False,
            "canonical_hosted": False,
            "routes": routes,
            "blockers": [],
            "notes": data.get("notes") or "Generated from open raw origin_sources; retrieved bytes still need canonicalization.",
        }

    has_open_raw = any(
        origin.access.value == "open" and origin.mode.value == "raw" and origin.kind.value != "script"
        for origin in descriptor.origin_sources
    )
    has_script = any(origin.kind.value == "script" for origin in descriptor.origin_sources)
    if has_open_raw:
        eco_routes = _ecostress_routes(descriptor)
        if eco_routes:
            category = eco_routes[0]["resources"][0]["selector"]["value"]
            return {
                **data,
                "status": "missing_delegate",
                "public_retrievable": True,
                "public_redistributable": False,
                "canonical_hosted": False,
                "routes": eco_routes,
                "blockers": [
                    f"JPL ECOSTRESS category bundle route identified (provider=jpl_ecostress, category={category}); blocked on "
                    "confirming the public bulk-order endpoint and adding the ECOSTRESS canonicalization recipe before automatic retrieval",
                ],
                "notes": data.get("notes") or "ECOSTRESS spectra are publicly reachable per material category; redistribution rights are not cleared.",
            }
        return {
            **data,
            "status": "missing_delegate" if has_script else "blocked_parser",
            "public_retrievable": True,
            "public_redistributable": False,
            "blockers": ["open raw origin exists, but it needs a curated adapter/delegate before automatic retrieval"],
        }

    if descriptor.tier.value in {"private", "anonymized"}:
        return {
            **data,
            "status": "token_required",
            "public_retrievable": False,
            "public_redistributable": False,
            "blockers": ["no open machine-actionable raw route; use token-gated Dataverse fallback"],
        }

    if any(origin.access.value == "manual" for origin in descriptor.origin_sources):
        return {
            **data,
            "status": "manual_only",
            "public_retrievable": False,
            "public_redistributable": False,
            "blockers": ["only manual/click-through origins are declared"],
        }

    return data


def _ecostress_category(descriptor: DatasetDescriptor) -> str | None:
    """Return the JPL ECOSTRESS material category for a descriptor, or ``None`` if it is not one.

    A descriptor qualifies only when it declares an open raw ``url`` origin on the JPL ECOSTRESS host
    *and* its id's second token is a known category (e.g. ``ecostress_lunar_tir_2124points`` -> ``lunar``).
    Both conditions must hold, so this never fires for non-ECOSTRESS datasets.
    """
    on_jpl_host = any(
        origin.access.value == "open"
        and origin.mode.value == "raw"
        and origin.kind.value == "url"
        and urlparse(origin.locator).netloc.endswith(_ECOSTRESS_HOST)
        for origin in descriptor.origin_sources
    )
    if not on_jpl_host:
        return None
    parts = descriptor.id.split("_")
    category = parts[1] if len(parts) > 1 else ""
    return category if category in _ECOSTRESS_CATEGORIES else None


def _ecostress_routes(descriptor: DatasetDescriptor) -> list[dict[str, Any]]:
    """Build the structured ``jpl_ecostress`` retrieval route for an ECOSTRESS descriptor.

    The route pins the provider, the verified per-material category selector, and the public download
    landing page. The bundle is one ZIP of per-sample spectrum ``.txt`` files; turning those into the
    descriptor's specific per-axis matrix is the ECOSTRESS family recipe and stays a ``delegate``.
    """
    category = _ecostress_category(descriptor)
    if category is None:
        return []
    script = next((origin.locator for origin in descriptor.origin_sources if origin.kind.value == "script"), None)
    citation = next((pub.doi for pub in descriptor.publications if pub.doi), None) or descriptor.citation
    route: dict[str, Any] = {
        "id": "jpl_ecostress",
        "priority": 40,
        "access": "open",
        "method": "raw_retrieve",
        "provider": "jpl_ecostress",
        "locator": _ECOSTRESS_DOWNLOAD_URL,
        "landing_url": _ECOSTRESS_DOWNLOAD_URL,
        "automated_download_allowed": False,
        "redistribution_allowed": False,
        "citation": citation,
        "resources": [
            {
                "id": f"{category}_bundle",
                "role": "archive",
                "required": True,
                "selector": {"kind": "api_file_name", "value": category},
                "file_name": f"ecostress_{category}.zip",
                "format": "zip",
                "unpack": {"archive": True, "members": []},
            }
        ],
        "canonicalization": {
            "engine": "delegate",
            "delegate": script or "source_to_standard.py",
            "notes": "ECOSTRESS category bundle (per-sample spectrum .txt files) -> per-axis matrix is the ECOSTRESS family recipe; not executed by raw retrieval.",
        },
        "notes": (
            f"JPL ECOSTRESS spectral library bundle for the '{category}' material category "
            f"(orderall('{category}') on {_ECOSTRESS_DOWNLOAD_URL}). The exact bulk-order endpoint "
            "must be confirmed before automatic fetch."
        ),
    }
    return [route]


def _synthetic_raw_routes(root: str | Path, descriptor: DatasetDescriptor) -> list[dict[str, Any]]:
    """Generate safe raw-retrieval routes from open origins until descriptors are curated."""
    manifest_routes = _raw_manifest_routes(root, descriptor)
    if manifest_routes:
        return manifest_routes
    script = next((origin.locator for origin in descriptor.origin_sources if origin.kind.value == "script"), None)
    routes: list[dict[str, Any]] = []
    for i, origin in enumerate(descriptor.origin_sources, start=1):
        if origin.access.value != "open" or origin.mode.value != "raw":
            continue
        provider = origin.kind.value
        if provider == "url":
            resource = _direct_url_resource(origin.locator)
            if resource is None:
                continue
            resources = [resource]
        elif provider in {"zenodo", "figshare", "dataverse"}:
            resources = []  # the Rust retriever enumerates provider files at runtime.
        else:
            continue
        route: dict[str, Any] = {
            "id": f"origin_{i:03d}",
            "priority": 100 + i,
            "access": "open",
            "method": "raw_retrieve",
            "provider": provider,
            "locator": origin.locator,
            "landing_url": origin.locator if provider == "url" and not resources else None,
            "automated_download_allowed": True,
            "redistribution_allowed": False,
            "resources": resources,
        }
        canonicalization = _canonicalization_for_resources(resources, script)
        if canonicalization is not None:
            route["canonicalization"] = canonicalization
        routes.append(route)
    return routes


def _raw_manifest_routes(root: str | Path, descriptor: DatasetDescriptor) -> list[dict[str, Any]]:
    """Generate direct raw routes from NIRS DB raw_manifest.csv without executing scripts."""
    if not any(
        origin.access.value == "open" and origin.mode.value == "raw" and origin.kind.value != "script"
        for origin in descriptor.origin_sources
    ):
        return []
    path = Path(root) / "NIRS DB" / "v2.0" / descriptor.id / "raw_manifest.csv"
    if not path.exists():
        return []
    resources: list[dict[str, Any]] = []
    seen: set[str] = set()
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        for row in csv.DictReader(handle, delimiter=";"):
            raw_url = (row.get("source_path_or_url") or row.get("source_file") or "").strip()
            name = (row.get("file_name") or "").strip() or unquote(PurePosixPath(urlparse(raw_url).path).name) or f"resource_{len(resources) + 1:03d}"
            url = _raw_manifest_resource_url(descriptor, raw_url, name)
            if url is None or url in seen:
                continue
            seen.add(url)
            fmt = _raw_manifest_format(descriptor, name) or "unknown"
            resource: dict[str, Any] = {
                "id": _resource_id(name, len(resources) + 1),
                "role": "spectra" if fmt == "ecostress_spectrum_txt" else _resource_role(row),
                "required": (row.get("used_for_conversion") or "").lower() != "no",
                "selector": {"kind": "direct_url", "value": url},
                "file_name": name,
                "format": fmt,
            }
            size = _int_or_none(row.get("file_size_bytes"))
            if size is not None:
                resource["size"] = size
            sha = (row.get("sha256_or_partial_hash") or "").strip().lower()
            if re.fullmatch(r"[0-9a-f]{64}", sha):
                resource["sha256"] = sha
            resources.append(resource)
    if not resources:
        return []
    script = next((origin.locator for origin in descriptor.origin_sources if origin.kind.value == "script"), None)
    route: dict[str, Any] = {
        "id": "nirs_db_raw_manifest",
        "priority": 50,
        "access": "open",
        "method": "raw_retrieve",
        "provider": "url",
        "locator": resources[0]["selector"]["value"],
        "automated_download_allowed": True,
        "redistribution_allowed": False,
        "resources": resources,
        "notes": "Generated from NIRS DB raw_manifest.csv; scripts are not executed.",
    }
    canonicalization = _canonicalization_for_resources(resources, script)
    if canonicalization is not None:
        route["canonicalization"] = canonicalization
    return [route]


def _raw_manifest_resource_url(descriptor: DatasetDescriptor, raw_url: str, file_name: str) -> str | None:
    """Return a machine-downloadable URL for a raw_manifest row."""
    if raw_url.startswith(("http://", "https://")):
        return raw_url
    if _ecostress_category(descriptor) is not None and file_name.endswith(".spectrum.txt"):
        return f"{_ECOSTRESS_DATA_URL}/{quote(file_name)}"
    return None


def _raw_manifest_format(descriptor: DatasetDescriptor, file_name: str) -> str | None:
    if _ecostress_category(descriptor) is not None and file_name.endswith(".spectrum.txt"):
        return "ecostress_spectrum_txt"
    return _format_from_name(file_name)


def _canonicalization_for_resources(resources: list[dict[str, Any]], script: str | None) -> dict[str, Any] | None:
    """Pick the Rust preparation engine declared for a synthetic raw route."""
    formats = {str(r.get("format") or "unknown") for r in resources}
    native = formats & {"jcamp_dx", "spc", "mat", "rda", "rds", "openspecy_rds"}
    tabular = formats & {"csv", "csv_gz", "txt"}
    if "ecostress_spectrum_txt" in formats:
        notes = (
            "Rust preparation parses ECOSTRESS spectrum text headers and X/Y values "
            "and assembles a dataset-level canonical payload."
        )
        engine = "rust_recipe"
        recipe_id = "jpl_ecostress_spectrum_txt_v1"
    elif native:
        notes = "Rust preparation decodes native spectra with nirs4all-formats."
        engine = "nirs4all_formats"
        recipe_id = None
    elif tabular:
        notes = "Rust preparation reads tabular resources with nirs4all-io."
        engine = "nirs4all_io"
        recipe_id = None
    elif script is None:
        return None
    else:
        notes = "NIRS DB compatibility script; not executed by raw retrieval."
        engine = "delegate"
        recipe_id = None
    out: dict[str, Any] = {"engine": engine, "notes": notes}
    if recipe_id is not None:
        out["recipe_id"] = recipe_id
        out["recipe_version"] = "1.0.0"
    if script is not None:
        out["delegate"] = script
        if engine == "rust_recipe" and recipe_id == "jpl_ecostress_spectrum_txt_v1":
            out["notes"] += " The NIRS DB script is retained as provenance/fallback, not as the active assembler."
        elif engine != "delegate":
            out["notes"] += (
                " Dataset-specific assembly remains delegated until a Rust recipe is curated; "
                "the NIRS DB script is retained as provenance/fallback."
            )
    return out


def _resource_id(file_name: str, n: int) -> str:
    stem = PurePosixPath(file_name).name.rsplit(".", 1)[0].lower()
    slug = re.sub(r"[^a-z0-9]+", "_", stem).strip("_")
    return slug or f"resource_{n:03d}"


def _resource_role(row: dict[str, str | None]) -> str:
    role = (row.get("file_role") or row.get("category") or "").lower()
    if "metadata" in role:
        return "metadata"
    if "license" in role:
        return "license"
    if "readme" in role:
        return "readme"
    if "split" in role:
        return "split"
    return "raw"


def _int_or_none(value: str | None) -> int | None:
    if value is None or value.strip() == "":
        return None
    try:
        return int(value)
    except ValueError:
        return None


def _direct_url_resource(locator: str) -> dict[str, Any] | None:
    parsed = urlparse(locator)
    if parsed.scheme not in {"http", "https"}:
        return None
    name = unquote(PurePosixPath(parsed.path).name)
    fmt = _format_from_name(name)
    if name == "" or fmt is None:
        return None
    return {
        "id": "resource",
        "role": "raw",
        "required": True,
        "selector": {"kind": "direct_url", "value": locator},
        "file_name": name,
        "format": fmt,
    }


def _format_from_name(name: str) -> str | None:
    lower = name.lower()
    for suffix, fmt in _DIRECT_FORMATS.items():
        if lower.endswith(suffix):
            return fmt
    return None


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
    retrieval = _retrieval(root, pub)

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
        retrieval = {
            "schema_version": "1.0",
            "status": "token_required",
            "canonical_hosted": False,
            "routes": [],
            "blockers": ["anonymized acquisition pointers are hidden in the public index"],
            "public_retrievable": False,
            "public_redistributable": False,
            "notes": None,
        }

    descriptor_dump = pub.model_dump(mode="json")
    descriptor_dump["retrieval"] = retrieval

    return {
        "tier": pub.tier.value,
        "dataverse": {"instance": dv.instance, "doi": doi, "dataset_version": dataset_version},
        "files": files,
        "origins": origins,
        "retrieval": retrieval,
        "descriptor": descriptor_dump,
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
