"""Source metadata corrections preserve scientific coordinates, samples and measurements."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import pytest

from nirs4all_datasets.bootstrap import _build_sources, _v2_modality, build_descriptor_from_card
from nirs4all_datasets.organize import organize
from nirs4all_datasets.schema import Modality
from nirs4all_datasets.spectroscopy import spectroscopy_family, wavelength_range_nm


@pytest.mark.parametrize("native", ["um", "µm", "μm", "Wavelength (micrometers)", "Wavelength (micrometer)", "Wavelength (µm)", "wavelength_um"])
def test_native_micrometer_axis_roundtrip(tmp_path: Path, v2_leaf: Any, native: str) -> None:
    leaf = v2_leaf(tmp_path / "source")
    original = "observation_id;2.5;0.4\no1;0.1;0.2\no2;0.3;0.4\n"
    (leaf / "X.csv").write_text(original)
    path = leaf / "dataset_card.json"
    raw = json.loads(path.read_text())
    raw["spectral_blocks"][0].update(axis_unit=native, axis_min="2.5", axis_max="0.4", axis_resolution="0.1", spectroscopy_type="ECOSTRESS spectral library")
    path.write_text(json.dumps(raw))
    descriptor, _ = build_descriptor_from_card(leaf)
    assert descriptor.sources[0].axis_resolution == 100
    result = organize(leaf, descriptor, tmp_path / "output")
    source = result.canonical_result.config["sources"][0]
    assert (source["axis_unit"], source["axis_min"], source["axis_max"]) == ("nm", 400, 2500)
    assert source["axis_conversion"] == {"native_unit": "um", "unit": "nm", "scale": 1000}
    frame = pd.read_parquet(result.dataset_dir / source["path"])
    assert list(frame.columns) == ["observation_id", "sample_id", "2500.0", "400.0"]
    np.testing.assert_allclose(frame.iloc[:, 2:], [[0.1, 0.2], [0.3, 0.4]])
    assert (result.dataset_dir / "raw/X.csv").read_text() == original
    assert frame["observation_id"].tolist() == ["o1", "o2"]
    assert spectroscopy_family([descriptor.sources[0].model_dump(mode="json")]) == "NIR"


def test_ossl_mir_and_visnir_declarations_override_exporter_defaults() -> None:
    card = {"dataset_id": "ossl_afsis2_soil_all_y", "spectral_blocks": [
        {"block_id": "X_visnir", "axis_unit": "source_column", "axis_min": "350", "axis_max": "2500", "n_spectral_variables": 1076, "spectroscopy_type": "NIR"},
        {"block_id": "X_mir", "axis_unit": "source_column", "axis_min": "600", "axis_max": "4000", "n_spectral_variables": 1701, "spectroscopy_type": "NIR"},
    ]}
    sources = _build_sources(card, [])
    assert [(s.source_id, s.axis_unit.value, s.modality.value) for s in sources] == [("X_visnir", "nm", "NIR"), ("X_mir", "cm-1", "MIR")]
    assert spectroscopy_family([s.model_dump(mode="json") for s in sources]) == "mixed"
    card["spectral_blocks"][1]["axis_max"] = "3500"
    with pytest.raises(ValueError, match="reviewed spectral metadata no longer matches axis_max"):
        _build_sources(card, [])
    card["spectral_blocks"][1].update(axis_max="4000", axis_unit="cm-1", spectroscopy_type="Raman")
    with pytest.raises(ValueError, match="reviewed spectral metadata no longer matches spectroscopy_type"):
        _build_sources(card, [])


@pytest.mark.parametrize(("declaration", "expected"), [(None, Modality.OTHER), ("spectral_1d_or_unknown", Modality.OTHER), ("Vis-SWIR", Modality.VSWIR), ("NIT", Modality.NIR), ("IR", Modality.MIR), ("FT-NIR", Modality.NIR), ("unit", Modality.OTHER), ("monitoring", Modality.OTHER), ("entire", Modality.OTHER), ("FT-IR", Modality.MIR), ("ATR-IR", Modality.MIR)])
def test_technique_mapping_has_no_implicit_nir_or_ir_substring_guess(declaration: Any, expected: Modality) -> None:
    assert _v2_modality(declaration) is expected


def test_raman_shift_and_absolute_wavenumber_have_different_meanings() -> None:
    axis = {"axis_min": 400, "axis_max": 4000, "axis_unit": "cm-1"}
    assert wavelength_range_nm({**axis, "modality": "Raman"}) is None
    assert wavelength_range_nm({**axis, "modality": "MIR"}) == (2500, 25000)
    assert spectroscopy_family([{**axis, "modality": "Raman"}]) == "Raman"


def test_family_and_coverage_remain_distinct_for_instrument_edges() -> None:
    source = {"modality": "NIR", "axis_unit": "nm", "axis_min": 1350, "axis_max": 2550}
    assert spectroscopy_family([source]) == "NIR"
    # The same source's physical coverage crosses the declared 2500 nm boundary.
    from nirs4all_datasets.spectroscopy import optical_bands

    assert optical_bands(source) == {"NIR", "MIR"}


def test_repair_preserves_a_reviewed_index_representation() -> None:
    from nirs4all_datasets.schema import DatasetDescriptor
    from scripts.repair_spectral_metadata import corrected_descriptor

    descriptor = DatasetDescriptor(id="chembl_ir_raman_multiblock", name="Molecular modes", description="Indexed native peak lists", sources=[{"source_id": "X1", "modality": "MIR", "axis_unit": "index"}], provenance={"contributor": "Source"}, governance={"license": "CC0-1.0"})
    card = {"dataset_id": descriptor.id, "spectral_blocks": [{"block_id": "X1", "axis_unit": "cm-1", "spectroscopy_type": "NIR"}]}
    assert corrected_descriptor(descriptor, card) == descriptor


def test_ucr_technique_evidence_does_not_calibrate_exporter_coordinates() -> None:
    card = {"dataset_id": "timeseries_puree_fraise_authenticite_ts", "spectral_blocks": [
        {"block_id": "X", "axis_unit": "source_column", "axis_min": "4000", "axis_max": "400", "n_spectral_variables": 235, "spectroscopy_type": "spectral_1d_or_unknown"},
    ]}
    source = _build_sources(card, [])[0]
    assert source.modality.value == "MIR"
    assert source.axis_unit.value == "none"
    assert wavelength_range_nm(source.model_dump(mode="json")) is None
    assert spectroscopy_family([source.model_dump(mode="json")]) == "MIR"


def test_legacy_ecosis_wrong_nm_label_uses_reviewed_native_micrometers() -> None:
    card = {"dataset_id": "leaf_sample_category_fresh_dry_ecosis", "spectral_blocks": [
        {"block_id": "X", "axis_unit": "nm", "axis_min": "0.4", "axis_max": "2.5", "n_spectral_variables": 826, "spectroscopy_type": "NIR/VIS-NIR"},
    ]}
    source = _build_sources(card, [])[0]
    assert (source.axis_min, source.axis_max, source.axis_unit.value) == (400, 2500, "nm")


def test_micrometer_repair_is_idempotent_with_existing_evidence(tmp_path, v2_leaf):
    import importlib.util

    spec = importlib.util.spec_from_file_location("repair_spectral_metadata", Path(__file__).parents[1] / "scripts/repair_spectral_metadata.py")
    repair = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(repair)
    leaf = v2_leaf(tmp_path / "source")
    card = json.loads((leaf / "dataset_card.json").read_text())
    card["spectral_blocks"][0].update(axis_unit="um", axis_min="0.4", axis_max="2.5")
    (leaf / "dataset_card.json").write_text(json.dumps(card))
    descriptor, _ = build_descriptor_from_card(leaf)
    descriptor.provenance.warnings.append("Spectral declaration for X1: existing reviewed evidence")
    updated = repair.corrected_descriptor(descriptor, card)
    assert updated == descriptor
    assert repair.corrected_descriptor(updated, card) == updated


@pytest.mark.parametrize(("dataset_id", "index_start", "count", "first", "last"), [
    ("nirpy_coffee_classification_nir", 1, 601, 1100, 2300),
    ("nirpy_peach_brix_nir", 1, 600, 1100, 2298),
    ("nirpy_plums_brix_firmness_nir", 0, 600, 1102, 2300),
])
def test_source_verified_nirpy_axis_mapping(tmp_path, dataset_id, index_start, count, first, last):
    from nirs4all_datasets.bootstrap import _spectral_metadata
    from nirs4all_datasets.canonical import _convert_source
    from nirs4all_datasets.manifest import sha256_file
    from nirs4all_datasets.schema import DatasetDescriptor
    from scripts.repair_spectral_metadata import corrected_descriptor

    metadata = _spectral_metadata()
    correction = metadata[dataset_id]["X"]
    card = {"dataset_id": dataset_id, "spectral_blocks": [{"block_id": "X", **correction["expected"]}]}
    source = _build_sources(card, [])[0]
    assert (source.axis_unit.value, source.axis_min, source.axis_max, source.axis_resolution) == ("nm", first, last, 2)
    descriptor = DatasetDescriptor(id=dataset_id, name="Indexed source", description="Source-backed wavelength recovery", sources=[{"source_id": "X", "axis_unit": "index", "axis_min": index_start, "axis_max": index_start + count - 1}], provenance={"contributor": "Source"}, governance={"license": "CC0-1.0"})
    updated = corrected_descriptor(descriptor, card)
    assert (updated.sources[0].axis_unit.value, updated.sources[0].axis_min, updated.sources[0].axis_max) == ("nm", first, last)
    assert corrected_descriptor(updated, card) == updated

    raw = tmp_path / "X.csv"
    headers = [str(index_start + i) for i in range(count)]
    values = np.arange(count, dtype=np.float32) / 10
    pd.DataFrame({"observation_id": ["o1"], **{header: [value] for header, value in zip(headers, values, strict=True)}}).to_csv(raw, sep=";", index=False)
    original = raw.read_bytes()
    canonical = tmp_path / "canonical"
    (canonical / "sources").mkdir(parents=True)
    # Production pins the real standardized source bytes. Bind only this synthetic fixture here.
    mapping = {**correction["axis_mapping"], "raw_sha256": sha256_file(raw)}
    result = _convert_source(raw, "X", None, False, "sample_id", canonical, axis_mapping=mapping)
    frame = pd.read_parquet(canonical / "sources/X.parquet")
    assert list(frame.columns[2:]) == [str(value) for value in range(first, last + 1, 2)]
    np.testing.assert_array_equal(frame.iloc[0, 2:].to_numpy(dtype=np.float32), values)
    assert frame["observation_id"].tolist() == frame["sample_id"].tolist() == ["o1"]
    assert raw.read_bytes() == original
    assert (result[0]["axis_min"], result[0]["axis_max"]) == (first, last)
    with raw.open("a") as stream:
        stream.write("\n")
    with pytest.raises(ValueError, match="verified original raw bytes"):
        _convert_source(raw, "X", None, False, "sample_id", canonical, axis_mapping=mapping)
    changed = original.decode().replace(f";{index_start};", ";wrong_channel;", 1)
    raw.write_text(changed)
    mapping = {**mapping, "raw_sha256": sha256_file(raw)}
    with pytest.raises(ValueError, match="ordered channel headers"):
        _convert_source(raw, "X", None, False, "sample_id", canonical, axis_mapping=mapping)
