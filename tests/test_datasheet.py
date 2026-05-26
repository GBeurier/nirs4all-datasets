"""Tests for the Datasheets-for-Datasets renderer (pure, no nirs4all)."""
from __future__ import annotations

from nirs4all_datasets import schema as s
from nirs4all_datasets.qualify.datasheet import render_datasheet

_SECTIONS = ["## Motivation", "## Composition", "## Collection process", "## Preprocessing", "## Uses", "## Distribution", "## Maintenance"]


def test_render_datasheet_has_all_sections(descriptor: s.DatasetDescriptor) -> None:
    card = {"inventory": {"n_samples": 80, "n_features": 700}, "spectral": {"signal_type": "absorbance", "wavelength_unit": "nm"}, "quality": {"has_nan": False}}
    md = render_datasheet(descriptor, card)
    for section in _SECTIONS:
        assert section in md
    assert "80" in md
    assert "CC-BY-4.0" in md
    assert "10.70112/abc" in md


def test_datasheet_marks_missing_fields() -> None:
    minimal = s.DatasetDescriptor(
        id="bare", name="Bare", version="1.0.0", description="x",
        instrument={"modality": "NIR"}, targets=[{"name": "y", "task_type": "regression"}],
        provenance={"contributor": "Lab"}, governance={"license": "CC-BY-4.0"},
    )
    md = render_datasheet(minimal, {})
    assert "*Not specified.*" in md  # e.g. collection date, reference method, DOI
