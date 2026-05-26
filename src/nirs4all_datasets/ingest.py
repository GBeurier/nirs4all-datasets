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

Scope: single-source **regression and classification** datasets with targets. Regression targets
are written as float64; classification targets are written as nirs4all's **encoded numeric class
indices** (string labels are encoded by nirs4all, so original class *names* belong in the
descriptor's ``Target.classes``), and the task type is recorded in ``nirs4all_config.json``. The
effective task type can be forced via ``task_type`` (the descriptor's intent) to avoid an
integer-valued regression target being auto-detected as classification. Targetless and multi-source
export remain explicit ``NotImplementedError``.
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


def _load_via_dataset_configs(path: Path) -> tuple[Any, str, str, dict[str, str], list[str]]:
    """Tabular route: load a directory with nirs4all DatasetConfigs."""
    import nirs4all
    from nirs4all.data import DatasetConfigs

    dataset = DatasetConfigs(str(path)).get_dataset_at(0)
    return dataset, "nirs4all-DatasetConfigs", nirs4all.__version__, {}, []


def load_dataset(source: str | Path, *, target: str | None = None, signal: str | None = None) -> tuple[Any, str, str, dict[str, str], list[str]]:
    """Load any supported input into a ``SpectroDataset``.

    Args:
        source: A directory (tabular convention) or a single instrument file.
        target: For instrument files, the target key to attach (optional).
        signal: For multi-signal instrument files, the signal to use (optional).

    Returns:
        ``(dataset, converter_name, converter_version, converter_config, warnings)``.
    """
    path = Path(source)
    if path.is_dir():
        return _load_via_dataset_configs(path)
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


def write_canonical(dataset: Any, out_dir: Path, *, target_names: list[str] | None = None, task_type: str | None = None) -> tuple[dict[str, Any], dict[str, str], dict[str, int]]:
    """Write a ``SpectroDataset`` to ``out_dir/canonical`` as Parquet + ``nirs4all_config.json``.

    Regression targets are float64; classification targets are encoded numeric class indices.
    ``task_type`` (e.g. the descriptor's intent) overrides nirs4all's auto-detected task, except the
    sentinel ``"auto"``. Returns ``(config, canonical_hashes, row_counts)``. Raises
    ``NotImplementedError`` for multi-source or targetless datasets (deferred to a later phase).
    """
    if dataset.n_sources != 1:
        raise NotImplementedError(f"multi-source canonical export not supported yet (n_sources={dataset.n_sources}).")
    auto_task = dataset.task_type.value if dataset.task_type is not None else "regression"
    task_value = task_type if (task_type and task_type != "auto") else auto_task
    is_classification = task_value in _CLASSIFICATION

    x_obj = dataset.x({}, layout="2d", concat_source=False)
    x_all = np.asarray(x_obj[0] if isinstance(x_obj, list) else x_obj, dtype="float32")
    n_samples, n_features = x_all.shape

    y_all = np.asarray(dataset.y({}))
    if y_all.size == 0:
        raise NotImplementedError("targetless datasets not supported yet (no targets to export).")
    if y_all.ndim == 1:
        y_all = y_all.reshape(-1, 1)
    if not is_classification:
        y_all = y_all.astype("float64")  # regression: numeric; classification: preserve labels as-is
    if target_names is not None and len(target_names) != y_all.shape[1]:
        raise ValueError(f"target_names has {len(target_names)} entries but y has {y_all.shape[1]} columns.")
    y_cols = target_names or [f"y{i}" for i in range(y_all.shape[1])]

    headers = [str(h) for h in (dataset.headers(0) or [str(i) for i in range(n_features)])]
    header_unit = dataset.header_unit(0)

    canonical = out_dir / "canonical"
    if canonical.exists():
        shutil.rmtree(canonical)  # avoid stale artifacts when the layout changes (split <-> single)
    canonical.mkdir(parents=True)
    masks = _resolve_partitions(dataset, n_samples)
    x_params = {"header_unit": header_unit}
    config: dict[str, Any] = {"task_type": task_value, "train_x_params": x_params}
    hashes: dict[str, str] = {}
    rows: dict[str, int] = {}

    if "test" in masks:
        plan = {"train": ("Xtrain.parquet", "Ytrain.parquet"), "test": ("Xtest.parquet", "Ytest.parquet")}
        for part, (xf, yf) in plan.items():
            mask = masks[part]
            hashes[xf] = _write_table(x_all[mask], headers, canonical / xf)
            hashes[yf] = _write_table(y_all[mask], y_cols, canonical / yf)
            rows[part] = int(mask.sum())
        config |= {
            "train_x": "canonical/Xtrain.parquet", "train_y": "canonical/Ytrain.parquet",
            "test_x": "canonical/Xtest.parquet", "test_y": "canonical/Ytest.parquet",
            "test_x_params": x_params,
        }
    else:
        hashes["X.parquet"] = _write_table(x_all, headers, canonical / "X.parquet")
        hashes["Y.parquet"] = _write_table(y_all, y_cols, canonical / "Y.parquet")
        rows["all"] = n_samples
        config |= {"train_x": "canonical/X.parquet", "train_y": "canonical/Y.parquet"}

    (canonical / "nirs4all_config.json").write_text(json.dumps(config, indent=2, sort_keys=True), encoding="utf-8")
    return config, hashes, rows


def resolve_config(dataset_dir: str | Path) -> dict[str, Any]:
    """Read ``<dataset_dir>/canonical/nirs4all_config.json`` and resolve paths to absolute.

    The on-disk config stores portable relative paths; this returns a dict whose ``train_x``
    etc. are absolute, ready to pass to :class:`nirs4all.data.DatasetConfigs`.
    """
    root = Path(dataset_dir)
    config: dict[str, Any] = json.loads((root / "canonical" / "nirs4all_config.json").read_text(encoding="utf-8"))
    for key in ("train_x", "train_y", "test_x", "test_y", "folds"):
        if key in config:
            config[key] = str((root / config[key]).resolve())
    return config


def ingest(source: str | Path, out_dir: str | Path, *, target: str | None = None, signal: str | None = None, target_names: list[str] | None = None, task_type: str | None = None) -> IngestResult:
    """Ingest ``source`` into ``out_dir/canonical`` and report provenance.

    ``task_type`` forces the effective task (the descriptor's intent). Unsupported conversions
    (multi-source, targetless) are reported as ``ConversionStatus.FAILED``; unexpected I/O errors propagate.
    """
    out = Path(out_dir)
    dataset, converter, version, conv_config, warnings = load_dataset(source, target=target, signal=signal)
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
