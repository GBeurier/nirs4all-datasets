"""Tests for idempotent local organization (uses sample_data; skipped if absent)."""
from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any

import pytest

from nirs4all_datasets import schema as s
from nirs4all_datasets.organize import organize

pytest.importorskip("nirs4all")


def _sample_regression() -> Path | None:
    candidates: list[Path] = []
    spec = importlib.util.find_spec("nirs4all")
    if spec and spec.origin:
        pkg = Path(spec.origin).parent
        candidates += [pkg.parent / "examples" / "sample_data" / "regression", pkg / "examples" / "sample_data" / "regression"]
    candidates.append(Path("/home/delete/nirs4all/nirs4all/examples/sample_data/regression"))
    return next((c for c in candidates if c.is_dir()), None)


def _descriptor() -> s.DatasetDescriptor:
    return s.DatasetDescriptor(
        id="corn_reg", name="Corn", version="1.0.0", description="x",
        instrument={"modality": "NIR", "axis_unit": "cm-1"},
        targets=[{"name": "y", "task_type": "regression"}],
        provenance={"contributor": "Lab"}, governance={"license": "CC-BY-4.0"},
    )


def test_organize_is_idempotent(tmp_path: Path) -> None:
    sample = _sample_regression()
    if sample is None:
        pytest.skip("sample_data/regression not found")
    descriptor = _descriptor()

    first = organize(sample, descriptor, tmp_path)
    assert first.skipped is False
    assert first.manifest_path.exists()
    assert (first.dataset_dir / "raw").exists()
    canonical = first.dataset_dir / "canonical"
    assert (canonical / "Xtrain.parquet").exists() or (canonical / "X.parquet").exists()

    second = organize(sample, descriptor, tmp_path)
    assert second.skipped is True

    forced = organize(sample, descriptor, tmp_path, force=True)
    assert forced.skipped is False
