"""Ingest raw inputs into the canonical, nirs4all-loadable form.

Two routes, one canonical output:

* a **directory** of tabular files (the nirs4all ``Xcal/Ycal/...`` convention) is loaded
  with :class:`nirs4all.data.DatasetConfigs`;
* a **single instrument file** (OPUS/SPC/JCAMP/ASD/...) is read losslessly with
  ``nirs4all_io.open_recordset`` and projected via ``to_spectrodataset``.

Both yield a ``SpectroDataset`` written to ``<out>/canonical/`` as Parquet plus an explicit
``nirs4all_config.json`` (the dict :class:`DatasetConfigs` consumes; the ``.parquet`` files are
*not* auto-detected, so the config references them by relative path -- use :func:`resolve_config`
to turn it into an absolute, loadable config). Parquet is chosen because Dataverse does not
auto-ingest it, so the canonical bytes stay pristine.

Scope: single- and multi-source **regression and classification** datasets, with or without targets.
Regression targets are written as float64; classification targets are written as nirs4all's
**encoded numeric class indices** (string labels are encoded by nirs4all, so original class *names*
belong in the descriptor's ``Target.classes``). Multi-source datasets write one X file per source
(``train_x`` becomes a list); targetless datasets write no Y. The task type is recorded in
``nirs4all_config.json`` and can be forced via ``task_type`` (the descriptor's intent) to avoid an
integer-valued regression target being auto-detected as classification.
"""
from __future__ import annotations

import json
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq

from nirs4all_datasets.manifest import sha256_file
from nirs4all_datasets.schema import ConversionStatus

_CLASSIFICATION = {"binary_classification", "multiclass_classification"}


@dataclass
class IngestResult:
    """Outcome of an ingest: the dataset dir, loader config, and provenance."""

    dataset_dir: Path
    canonical_dir: Path
    config: dict[str, Any]
    converter_name: str
    converter_version: str
    converter_config: dict[str, str]
    status: ConversionStatus
    canonical_hashes: dict[str, str] = field(default_factory=dict)
    row_counts: dict[str, int] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)
    n_samples: int = 0
    n_features: int = 0


def _load_via_dataverse_io(path: Path, *, target: str | None, signal: str | None) -> tuple[Any, str, str, dict[str, str], list[str]]:
    """Instrument route: read a single file with nirs4all-io and project to a SpectroDataset."""
    import nirs4all_io as nio

    recordset = nio.open_recordset(str(path))
    available = recordset.signal_names()
    if not available:
        raise ValueError(f"{path}: no spectral signals found.")
    warnings: list[str] = []
    chosen = signal or available[0]
    if chosen not in available:
        raise ValueError(f"{path}: signal {chosen!r} not in available signals {available}.")
    if len(available) > 1 and signal is None:
        warnings.append(f"multiple signals {available}; using {chosen!r} (single-source canonical form). Pass signal=... to choose.")
    dataset = recordset.to_spectrodataset(name=path.stem, signals=[chosen], target=target)
    conv_config = {"signal": chosen, "available_signals": ",".join(available)}
    return dataset, "nirs4all-io", nio.__version__, conv_config, warnings


def _has_data_rows(path: Path) -> bool:
    """Whether a tabular file holds at least one data row (not missing / 0-byte / header-only)."""
    try:
        if not path.exists() or path.stat().st_size == 0:
            return False
    except OSError:
        return False
    with path.open("r", encoding="utf-8", errors="replace") as fh:
        non_empty = sum(1 for line in fh if line.strip())
        if non_empty > 1:  # short-circuit: a header + >=1 data row
            return True
    return False


def _build_folder_config(path: Path, *, header_unit: str | None, na_policy: str) -> tuple[dict[str, Any], list[str]]:
    """Build an explicit nirs4all config from a folder, robust to real-world data.

    Reuses nirs4all's ``FolderParser`` for the (case-insensitive) file→role mapping — this package
    never re-derives the naming rules — then augments it: ``na_policy`` on the X/Y loaders (``ignore``
    keeps NaN so the card can report it instead of the loader aborting), an explicit ``header_unit``
    for the spectral axis, and dropping ``*_group`` metadata files that are empty/header-only (which
    otherwise crash the loader). Returns ``(config, warnings)``.
    """
    from nirs4all.data.parsers.folder_parser import FolderParser

    result = FolderParser().parse(str(path))
    if not result.success:
        raise ValueError(f"{path}: could not parse folder: {'; '.join(result.errors)}")
    config: dict[str, Any] = {k: v for k, v in result.config.items() if v is not None}
    warnings: list[str] = list(result.warnings or [])

    def _params_for(value: Any, base: dict[str, str]) -> Any:
        return [dict(base) for _ in value] if isinstance(value, list) else dict(base)

    x_base = {"na_policy": na_policy} | ({"header_unit": header_unit} if header_unit else {})
    y_base = {"na_policy": na_policy}
    for side in ("train", "test"):
        if config.get(f"{side}_x") is not None:
            config[f"{side}_x_params"] = _params_for(config[f"{side}_x"], x_base)
        if config.get(f"{side}_y") is not None:
            config[f"{side}_y_params"] = _params_for(config[f"{side}_y"], y_base)

    for gkey in ("train_group", "test_group"):
        value = config.get(gkey)
        if isinstance(value, str) and not _has_data_rows(Path(value)):
            config.pop(gkey, None)
            config.pop(f"{gkey}_params", None)
            warnings.append(f"dropped empty/header-only metadata file for {gkey}")
    return config, warnings


def _load_via_dataset_configs(path: Path, *, header_unit: str | None, na_policy: str) -> tuple[Any, str, str, dict[str, str], list[str]]:
    """Tabular route: load a directory with nirs4all DatasetConfigs (robust explicit config)."""
    import nirs4all
    from nirs4all.data import DatasetConfigs

    config, warnings = _build_folder_config(path, header_unit=header_unit, na_policy=na_policy)
    dataset = DatasetConfigs(config).get_dataset_at(0)
    # Record the load knobs so the manifest/incrementality reacts if they change (not NIRS logic).
    conv_config = {"na_policy": na_policy, "header_unit": str(header_unit or "")}
    return dataset, "nirs4all-DatasetConfigs", nirs4all.__version__, conv_config, warnings


def load_dataset(source: str | Path, *, target: str | None = None, signal: str | None = None, header_unit: str | None = None, na_policy: str = "ignore") -> tuple[Any, str, str, dict[str, str], list[str]]:
    """Load any supported input into a ``SpectroDataset``.

    Args:
        source: A directory (tabular convention) or a single instrument file.
        target: For instrument files, the target key to attach (optional).
        signal: For multi-signal instrument files, the signal to use (optional).
        header_unit: Spectral axis unit for the X loader (e.g. ``"nm"``/``"cm-1"``; folder route only).
        na_policy: NA handling for the X/Y loaders (folder route); ``"ignore"`` keeps NaN in place.

    Returns:
        ``(dataset, converter_name, converter_version, converter_config, warnings)``.
    """
    path = Path(source)
    if path.is_dir():
        return _load_via_dataset_configs(path, header_unit=header_unit, na_policy=na_policy)
    if path.is_file():
        return _load_via_dataverse_io(path, target=target, signal=signal)
    raise FileNotFoundError(f"ingest source does not exist: {source}")


def _resolve_partitions(dataset: Any, n_samples: int) -> dict[str, np.ndarray]:
    """Map samples to partitions. Returns {'all'} or {'train','test'}; raises on unsupported sets."""
    try:
        parts = np.asarray([str(p) for p in dataset.index_column("partition")])
    except Exception:  # noqa: BLE001 - partition column may be absent
        parts = np.array([], dtype=str)
    if parts.shape[0] != n_samples:
        return {"all": np.ones(n_samples, dtype=bool)}
    labels = {p for p in parts.tolist() if p and p != "None"}
    if not labels or labels == {"train"}:
        return {"all": np.ones(n_samples, dtype=bool)}
    if labels == {"train", "test"}:
        return {"train": parts == "train", "test": parts == "test"}
    raise NotImplementedError(f"unsupported partition set {sorted(labels)}; the canonical writer supports train-only or train+test.")


def _write_table(array: np.ndarray, columns: list[str], path: Path) -> str:
    """Write a 2D array to Parquet with the given (unique) column names; return its sha256."""
    if len(columns) != array.shape[1]:
        raise ValueError(f"header count {len(columns)} != feature count {array.shape[1]}.")
    if len(set(columns)) != len(columns):
        raise ValueError("duplicate column headers in canonical table.")
    table = pa.table({col: array[:, i] for i, col in enumerate(columns)})
    pq.write_table(table, path, compression="zstd")
    return sha256_file(path)


def _source_blocks(dataset: Any) -> list[np.ndarray]:
    """Per-source 2D feature blocks (a single-source dataset yields a one-element list)."""
    x = dataset.x({}, layout="2d", concat_source=False)
    blocks = x if isinstance(x, list) else [x]
    return [np.asarray(block, dtype="float32") for block in blocks]


def write_canonical(dataset: Any, out_dir: Path, *, target_names: list[str] | None = None, task_type: str | None = None) -> tuple[dict[str, Any], dict[str, str], dict[str, int]]:
    """Write a ``SpectroDataset`` to ``out_dir/canonical`` as Parquet + ``nirs4all_config.json``.

    Handles single- and multi-source datasets (one X file per source; ``train_x`` becomes a list of
    paths with a matching list of ``train_x_params``), train-only / train+test splits, and targetless
    datasets (no Y written). Regression targets are float64; classification targets are encoded numeric
    class indices. ``task_type`` overrides nirs4all's auto-detected task (except the sentinel ``"auto"``).
    """
    blocks = _source_blocks(dataset)
    n_sources = len(blocks)
    n_samples = blocks[0].shape[0]

    y_raw = np.asarray(dataset.y({}))
    has_targets = y_raw.size > 0

    if task_type and task_type != "auto":
        task_value = task_type
    elif not has_targets:
        task_value = "auto"  # no targets -> do not assert a supervised task
    else:
        task_value = dataset.task_type.value if dataset.task_type is not None else "regression"
    is_classification = task_value in _CLASSIFICATION

    y_all = (y_raw.reshape(-1, 1) if y_raw.ndim == 1 else y_raw) if has_targets else y_raw
    if has_targets and not is_classification:
        y_all = y_all.astype("float64")
    if has_targets and target_names is not None and len(target_names) != y_all.shape[1]:
        raise ValueError(f"target_names has {len(target_names)} entries but y has {y_all.shape[1]} columns.")
    y_cols = (target_names or [f"y{i}" for i in range(y_all.shape[1])]) if has_targets else []

    headers = [[str(h) for h in (dataset.headers(src) or [str(i) for i in range(blocks[src].shape[1])])] for src in range(n_sources)]
    units = [dataset.header_unit(src) for src in range(n_sources)]

    canonical = out_dir / "canonical"
    if canonical.exists():
        shutil.rmtree(canonical)  # avoid stale artifacts when the layout changes
    canonical.mkdir(parents=True)
    masks = _resolve_partitions(dataset, n_samples)

    # Persist na_policy="ignore" in the canonical config so reloading the Parquet for the card never
    # re-aborts on NaN (ParquetLoader otherwise defaults to abort). Header unit is carried through too.
    na = "ignore"
    x_params: Any = {"header_unit": units[0], "na_policy": na} if n_sources == 1 else [{"header_unit": u, "na_policy": na} for u in units]
    config: dict[str, Any] = {"task_type": task_value, "train_x_params": x_params}
    if "test" in masks:
        config["test_x_params"] = x_params
    if has_targets:
        config["train_y_params"] = {"na_policy": na}
        if "test" in masks:
            config["test_y_params"] = {"na_policy": na}
    hashes: dict[str, str] = {}
    rows: dict[str, int] = {}

    def _write_partition(part: str, key_prefix: str) -> None:
        mask = masks[part]
        rows[part] = int(mask.sum())
        x_label = "X" if part == "all" else f"X{part}"
        x_paths = []
        for src in range(n_sources):
            filename = f"{x_label}.parquet" if n_sources == 1 else f"{x_label}_{src}.parquet"
            hashes[filename] = _write_table(blocks[src][mask], headers[src], canonical / filename)
            x_paths.append(f"canonical/{filename}")
        config[f"{key_prefix}_x"] = x_paths[0] if n_sources == 1 else x_paths
        if has_targets:
            y_filename = "Y.parquet" if part == "all" else f"Y{part}.parquet"
            hashes[y_filename] = _write_table(y_all[mask], y_cols, canonical / y_filename)
            config[f"{key_prefix}_y"] = f"canonical/{y_filename}"

    if "test" in masks:
        _write_partition("train", "train")
        _write_partition("test", "test")
    else:
        _write_partition("all", "train")

    (canonical / "nirs4all_config.json").write_text(json.dumps(config, indent=2, sort_keys=True), encoding="utf-8")
    return config, hashes, rows


def resolve_config(dataset_dir: str | Path) -> dict[str, Any]:
    """Read ``<dataset_dir>/canonical/nirs4all_config.json`` and resolve paths to absolute.

    The on-disk config stores portable relative paths; this returns a dict whose ``train_x``
    etc. are absolute, ready to pass to :class:`nirs4all.data.DatasetConfigs`.
    """
    root = Path(dataset_dir)
    config: dict[str, Any] = json.loads((root / "canonical" / "nirs4all_config.json").read_text(encoding="utf-8"))
    for key in ("train_x", "test_x"):  # may be a list of paths (multi-source) or a single path
        value = config.get(key)
        if isinstance(value, list):
            config[key] = [str((root / item).resolve()) for item in value]
        elif isinstance(value, str):
            config[key] = str((root / value).resolve())
    for key in ("train_y", "test_y", "folds"):  # single path if present (folds may be an inline spec -> leave it)
        if isinstance(config.get(key), str):
            config[key] = str((root / config[key]).resolve())
    return config


def ingest(source: str | Path, out_dir: str | Path, *, target: str | None = None, signal: str | None = None, target_names: list[str] | None = None, task_type: str | None = None, header_unit: str | None = None) -> IngestResult:
    """Ingest ``source`` into ``out_dir/canonical`` and report provenance.

    ``task_type`` forces the effective task (the descriptor's intent); ``header_unit`` sets the spectral
    axis unit for the folder route. Unsupported conversions are reported as ``ConversionStatus.FAILED``;
    unexpected I/O errors propagate.
    """
    out = Path(out_dir)
    dataset, converter, version, conv_config, warnings = load_dataset(source, target=target, signal=signal, header_unit=header_unit)
    try:
        config, hashes, rows = write_canonical(dataset, out, target_names=target_names, task_type=task_type)
    except NotImplementedError as exc:
        warnings.append(str(exc))
        return IngestResult(out, out / "canonical", {}, converter, version, conv_config, ConversionStatus.FAILED, warnings=warnings)

    status = ConversionStatus.PARTIAL if warnings else ConversionStatus.OK
    nfeat = dataset.num_features if isinstance(dataset.num_features, int) else dataset.num_features[0]
    return IngestResult(
        dataset_dir=out,
        canonical_dir=out / "canonical",
        config=config,
        converter_name=converter,
        converter_version=version,
        converter_config=conv_config,
        status=status,
        canonical_hashes=hashes,
        row_counts=rows,
        warnings=warnings,
        n_samples=dataset.num_samples,
        n_features=int(nfeat),
    )
