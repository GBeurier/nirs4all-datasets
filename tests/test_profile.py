"""Tests for the identity card builder (build_card) — self-contained via a tiny dataset."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

from nirs4all_datasets import schema as s
from nirs4all_datasets.ingest import write_canonical
from nirs4all_datasets.qualify.profile import build_card

pytest.importorskip("nirs4all")
from nirs4all.data import SpectroDataset  # noqa: E402


def _descriptor() -> s.DatasetDescriptor:
    return s.DatasetDescriptor(
        id="tiny", name="Tiny", version="1.0.0", description="x",
        instrument={"modality": "NIR", "axis_unit": "nm"},
        targets=[{"name": "y", "task_type": "regression"}],
        keywords=["nir"], provenance={"contributor": "Lab"},
        governance={"license": "CC-BY-4.0", "visibility": "public", "confidentiality_class": "public"},
    )


def _write_tiny_canonical(tmp_path: Path) -> None:
    ds = SpectroDataset("tiny")
    rng = np.random.RandomState(0)
    ds.add_samples(rng.rand(40, 8).astype("float32"), headers=[str(1000 + 10 * i) for i in range(8)], header_unit="nm")
    ds.add_targets(np.linspace(0.0, 1.0, 40))
    write_canonical(ds, tmp_path)


def test_build_card(tmp_path: Path) -> None:
    _write_tiny_canonical(tmp_path)
    try:
        card = build_card(tmp_path, _descriptor())
    except Exception as exc:  # noqa: BLE001
        if "categorical_mode" in str(exc):
            pytest.skip("requires the nirs4all ParquetLoader fix")
        raise

    assert set(card) >= {"identity", "inventory", "spectral", "targets", "quality", "integrity", "assets"}
    assert card["identity"]["id"] == "tiny"
    assert card["inventory"]["n_samples"] == 40
    assert card["inventory"]["n_features"] == 8
    assert card["targets"]["task_type"] == "regression"
    assert "shape" in card["targets"] and card["targets"]["shape"]["n"] == 40
    assert "spectral" in card["quality"]
    assert card["quality"]["has_nan"] is False
    assert card["integrity"]["content_hash"]
    assert "warnings" in card
    assert card["spectral"]["spacing_unit"] == "nm"
    assert (tmp_path / "card.json").exists()
    assert (tmp_path / "card.md").exists()  # datasheet
    assert (tmp_path / "croissant.json").exists()  # Croissant metadata
    assert (tmp_path / "assets" / "spectra_envelope.png").exists()
    assert (tmp_path / "assets" / "target_distribution.png").exists()
    # card.json is finite, valid JSON (no NaN/Inf); croissant is valid JSON
    loaded = json.loads((tmp_path / "card.json").read_text())
    assert loaded["inventory"]["n_samples"] == 40
    assert json.loads((tmp_path / "croissant.json").read_text())["@type"] == "sc:Dataset"


def _clf_descriptor() -> s.DatasetDescriptor:
    return s.DatasetDescriptor(
        id="clf", name="Clf", version="1.0.0", description="x",
        instrument={"modality": "NIR", "axis_unit": "nm"},
        targets=[{"name": "variety", "task_type": "multiclass_classification"}],
        provenance={"contributor": "Lab"},
        governance={"license": "CC-BY-4.0", "visibility": "public", "confidentiality_class": "public"},
    )


def test_build_card_classification(tmp_path: Path) -> None:
    ds = SpectroDataset("clf")
    rng = np.random.RandomState(0)
    ds.add_samples(rng.rand(30, 6).astype("float32"), headers=[str(1000 + 10 * i) for i in range(6)], header_unit="nm")
    ds.add_targets(np.array([0, 1, 2] * 10))
    write_canonical(ds, tmp_path)
    try:
        card = build_card(tmp_path, _clf_descriptor())
    except Exception as exc:  # noqa: BLE001
        if "categorical_mode" in str(exc):
            pytest.skip("requires the nirs4all ParquetLoader fix")
        raise
    assert card["targets"]["task_type"] == "classification"
    assert card["targets"]["balance"]["n_classes"] == 3
    assert (tmp_path / "assets" / "target_distribution.png").exists()
