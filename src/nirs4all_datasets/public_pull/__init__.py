"""Download public original data and materialize a locally readable dataset."""
from __future__ import annotations

import hashlib
import importlib
import json
import os
import tempfile
from pathlib import Path
from typing import Any

import pandas as pd
from filelock import FileLock

from nirs4all_datasets.public_pull.common import PullContext
from nirs4all_datasets.schema import AlignmentLevel, AxisUnit, ConversionStatus, DatasetDescriptor, Tier, Variable, VariableRole, VarType

_FAMILIES = ("ecosis", "dryad", "mendeley", "fairdata", "harvard_forage", "other")


def _recipe(dataset_id: str) -> Any:
    for name in _FAMILIES:
        try:
            module = importlib.import_module(f"nirs4all_datasets.public_pull.{name}")
        except ModuleNotFoundError as exc:
            if exc.name == f"nirs4all_datasets.public_pull.{name}":
                continue
            raise
        if module.supports(dataset_id):
            return module
    raise ValueError(f"{dataset_id!r} has no implemented public-origin loading recipe")


def available(dataset_id: str) -> bool:
    try:
        _recipe(dataset_id)
    except ValueError:
        return False
    return True


def pull(descriptor: DatasetDescriptor, *, cache_dir: str | Path | None = None, guestbook_response: dict[str, Any] | None = None, timeout_secs: int | None = None, max_total_bytes: int | None = None) -> tuple[Path, DatasetDescriptor]:
    """Materialize a public dataset, serializing concurrent writers to its cache."""
    base = Path(cache_dir) if cache_dir is not None else Path(os.environ.get("XDG_CACHE_HOME", str(Path.home() / ".cache"))) / "nirs4all-datasets"
    lock_dir = base / "public" / descriptor.id
    lock_dir.mkdir(parents=True, exist_ok=True)
    with FileLock(str(lock_dir / ".build.lock"), timeout=3600):
        return _pull(descriptor, cache_dir=base, guestbook_response=guestbook_response, timeout_secs=timeout_secs, max_total_bytes=max_total_bytes)


def _pull(descriptor: DatasetDescriptor, *, cache_dir: str | Path | None = None, guestbook_response: dict[str, Any] | None = None, timeout_secs: int | None = None, max_total_bytes: int | None = None) -> tuple[Path, DatasetDescriptor]:
    """Fetch original public bytes, apply a packaged recipe, and atomically cache canonical data.

    This is a fresh conversion of original data. Historical canonical hashes are
    not used to claim identity with a different upstream representation.
    """
    from nirs4all_datasets.bootstrap import _original_sample_alias, _sample_conflicts, _v2_numeric_columns
    from nirs4all_datasets.canonical import build_canonical
    from nirs4all_datasets.manifest import sha256_file

    if descriptor.tier is not Tier.PUBLIC:
        raise ValueError("automatic public-origin assembly is restricted to public datasets")
    module = _recipe(descriptor.id)
    base = Path(cache_dir) if cache_dir is not None else Path(os.environ.get("XDG_CACHE_HOME", str(Path.home() / ".cache"))) / "nirs4all-datasets"
    fingerprint = hashlib.sha256(descriptor.model_dump_json().encode())
    from nirs4all_datasets import __version__

    fingerprint.update(__version__.encode())
    module_path = Path(getattr(module, "__file__", __file__))
    package_root = Path(__file__).parent.parent
    paths = {Path(__file__), Path(__file__).with_name("common.py"), module_path, package_root / "canonical.py", package_root / "curation.py", package_root / "curation_contracts.json"}
    paths.update(module_path.parent.glob(module_path.stem + "*.json"))
    for path in sorted(paths):
        fingerprint.update(path.read_bytes())
    destination = base / "public" / descriptor.id / fingerprint.hexdigest()[:24]
    marker = destination / "origin-pull.json"
    if marker.exists():
        try:
            saved = json.loads(marker.read_text(encoding="utf-8"))
            files = saved["files"]
            canonical = (destination / "canonical").resolve()
            if isinstance(files, dict) and "canonical/dataset.json" in files and all(
                isinstance(rel, str)
                and isinstance(digest, str)
                and (destination / rel).resolve().is_relative_to(canonical)
                and (destination / rel).is_file()
                and sha256_file(destination / rel) == digest
                for rel, digest in files.items()
            ):
                config = json.loads((canonical / "dataset.json").read_text(encoding="utf-8"))
                entries = [*config.get("sources", []), *config.get("splits", [])]
                if config.get("variables"):
                    entries.append(config["variables"])
                if entries and all(isinstance(entry, dict) and entry.get("path") in files for entry in entries):
                    return destination, DatasetDescriptor(**saved["descriptor"])
        except (OSError, ValueError, TypeError, KeyError):
            # An incomplete/corrupt marker is a cache miss; rebuild under the lock.
            pass
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".pull-", dir=destination.parent) as work:
        directory = Path(work)
        context = PullContext(descriptor.id, directory, base, guestbook_response=guestbook_response, timeout=timeout_secs or 90,
                              max_total_bytes=max_total_bytes if max_total_bytes is not None else 20_000_000_000)
        try:
            leaf = Path(module.build(descriptor, context))
        finally:
            context.session.close()
        if not leaf.is_dir() or not list(leaf.glob("X*.csv")):
            raise ValueError(f"{descriptor.id}: recipe did not produce spectral tables")
        runtime = descriptor.model_copy(deep=True)
        # Historical standardized-table assumptions do not describe freshly joined originals.
        runtime.provenance.warnings = [w for w in runtime.provenance.warnings if not w.startswith(("Y.csv has no observation_id;", "Observation identity is used as the canonical join key because source sample_id"))]
        layout_path = leaf / "pull-layout.json"
        layout = json.loads(layout_path.read_text(encoding="utf-8")) if layout_path.is_file() else {}
        for source in runtime.sources:
            override = layout.get("sources", {}).get(source.source_id, {})
            if "axis_unit" in override:
                source.axis_unit = AxisUnit(override["axis_unit"])
                # Bounds describe the representation actually returned, not a historical transform.
                source.axis_min, source.axis_max, source.axis_resolution = None, None, None
        runtime.provenance.warnings.extend(layout.get("warnings", []))
        y_path = leaf / "Y.csv"
        y_cols = list(pd.read_csv(y_path, sep=";", nrows=0).columns) if y_path.is_file() else []
        missing = [v.name for v in runtime.targets if v.name not in y_cols]
        if missing:
            raise ValueError(f"{descriptor.id}: original-source assembly is missing target columns: {missing}")
        m_path = leaf / "M.csv"
        m_cols = list(pd.read_csv(m_path, sep=";", nrows=0).columns) if m_path.is_file() else []
        runtime.variables = [v for v in runtime.variables if v.name in set(y_cols + m_cols)]
        declared = {v.name for v in runtime.variables}
        numeric = _v2_numeric_columns(m_path, default_numeric=False)
        structural = {"dataset_id", "observation_id", "sample_id", "split_original", "split_source", "source_sample_index"}
        for name in m_cols:
            if name not in declared and name not in structural and not name.startswith("source_"):
                runtime.variables.append(Variable(name=name, role=VariableRole.METADATA, type=VarType.NUMERIC if numeric.get(name) else VarType.CATEGORICAL))
        from nirs4all_datasets.curation import identity_view

        metadata = pd.read_csv(m_path, sep=";", dtype=str, keep_default_na=False) if m_path.is_file() else pd.DataFrame(columns=["observation_id"])
        _, identity = identity_view(runtime.id, metadata)
        runtime.ids.sample_id = "sample_id"
        runtime.ids.sample_id_available = identity["sample_id_available"]
        if runtime.ids.sample_id_available:
            runtime.alignment_level = AlignmentLevel.SAMPLE
        output = directory / "output"
        result = build_canonical(leaf, runtime, output)
        if result.status is ConversionStatus.FAILED:
            raise ValueError(f"{descriptor.id}: original-source conversion failed: {result.warnings}")
        runtime.provenance.warnings = list(dict.fromkeys([*runtime.provenance.warnings, *result.warnings]))
        config = result.config
        for source in runtime.sources:
            actual = next((s for s in config["sources"] if s["source_id"] == source.source_id), None)
            if actual is None:
                raise ValueError(f"{descriptor.id}: original-source assembly omitted source {source.source_id!r}")
            source.n_observations, source.n_variables = actual["n_observations"], actual["n_variables"]
            source.axis_min, source.axis_max = actual.get("axis_min"), actual.get("axis_max")
        files = {p.relative_to(output).as_posix(): sha256_file(p) for p in sorted((output / "canonical").rglob("*")) if p.is_file()}
        info = {"schema": "nirs4all-datasets.public-origin.v1", "descriptor": runtime.model_dump(mode="json"), "downloads": context.downloads, "files": files, "conversion_warnings": result.warnings,
                "representation": layout.get("representation", "original-source-tables")}
        (output / "origin-pull.json").write_text(json.dumps(info, indent=2, sort_keys=True), encoding="utf-8")
        if destination.exists():
            import shutil

            shutil.rmtree(destination)
        output.rename(destination)
    return destination, runtime
