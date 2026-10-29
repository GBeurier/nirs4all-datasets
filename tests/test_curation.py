"""Scientific regressions for issue #23/#24; fixtures contain no real dataset bytes."""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import pytest

from nirs4all_datasets.curation import curate_bundle, curate_tables, identity_view, normalize_missing


def test_passport_constant_empty_and_target_copies_leave_m_but_remain_traceable():
    m = pd.DataFrame({"observation_id": ["o1", "o2", "o3"], "sample_id": ["001", "001", "002"], "Site": ["A", "B", "B"], "license": ["a", "b", "b"], "constant": ["x"] * 3, "empty": ["", "null", "NaN"], "protein": ["1", "2", "3"]})
    y = pd.DataFrame({"observation_id": ["o3", "o1", "o2"], "protein": ["3", "1", "2"]})
    before = m.copy(deep=True)
    result = curate_tables("synthetic", m, y)
    assert result.metadata.columns.tolist() == ["observation_id", "sample_id", "site"]
    assert result.targets["protein"].tolist() == [1.0, 2.0, 3.0]  # keyed to M order, not a positional zip
    assert result.metadata["site"].tolist() == ["A", "B", "B"]
    assert result.structure["sample_id"].tolist() == ["001", "001", "002"]
    assert set(result.report["views"]["passport"]) >= {"license", "m_constant", "m_empty", "protein"}
    assert {(e["source_resource"], e["original_name"]) for e in result.report["mapping"]} == {("M.csv", c) for c in m} | {("Y.csv", c) for c in y}
    pd.testing.assert_frame_equal(m, before)


def test_aliases_coalesce_before_completeness_and_constants_are_evaluated():
    m = pd.DataFrame({"observation_id": ["a", "b", "c"], "Site": ["A", "", ""], "site": ["", "B", "B"]})
    result = curate_tables("synthetic", m)
    assert result.metadata["site"].tolist() == ["A", "B", "B"]
    stats = next(v["stats"] for v in result.report["variables"] if v["name"] == "site")
    assert stats["completeness_pct"] == 100
    assert stats["n_unique"] == 2 and stats["imbalance_ratio"] == 2
    m["Site"] = ["A", "C", "C"]
    m["site"] = ["D", "B", "E"]
    result = curate_tables("synthetic", m)
    assert result.metadata[["site", "site_2"]].shape == (3, 2)
    assert any(e["operation"] == "keep_conflicting_homonyms_separate" for e in result.report["mapping"])


def test_missing_tokens_are_contextual_and_censoring_is_not_imputed():
    values = pd.Series(["", "\u00a0", "NaN", "NULL", "not_available_reason", "none", "NA", "ND", "-999", "<0.1", "0", "-2"])
    clean = normalize_missing(values)
    assert clean.iloc[:5].isna().all()
    assert clean.iloc[5:].tolist() == ["none", "NA", "ND", "-999", "<0.1", "0", "-2"]
    m = pd.DataFrame({"observation_id": ["a", "b", "c"], "treatment": ["none", "salt", "salt"]})
    y = pd.DataFrame({"observation_id": ["a", "b", "c"], "concentration": ["<0.1", "2.5", "-999"]})
    with pytest.raises(ValueError, match="source confirmation"):
        curate_tables("synthetic", m, y, missing_rules={"Y:concentration": {"sentinels": ["-999"]}})
    result = curate_tables("synthetic", m, y, numeric_names={"concentration"}, missing_rules={"Y:concentration": {"sentinels": ["-999"], "confirmed": True, "evidence": "fixture source dictionary"}})
    stats = next(v["stats"] for v in result.report["variables"] if v["name"] == "concentration")
    assert stats["n_censored"] == 1 and stats["n_missing"] == 1
    assert stats["min"] == stats["max"] == 2.5
    assert result.targets["concentration"].iloc[0] == "<0.1"
    assert result.metadata["treatment"].iloc[0] == "none"


@pytest.mark.parametrize("dataset", ["ucph_granules_ambient_moisture_api_nir", "ucph_granules_moisture_controlled_api_nir"])
def test_granules_api_is_a_reference_target_and_scans_group_by_vial(dataset):
    ids = [f"o{i}" for i in range(6)]
    labels = [f"lot_v{vial}.{scan}" for vial in [1, 2] for scan in [0, 1, 2]]
    m = pd.DataFrame({"observation_id": ids, "sample_id": labels, "api_concentration_design_percent": ["2"] * 3 + ["15"] * 3, "riblet_mass_g": ["1"] * 3 + ["2"] * 3})
    y = pd.DataFrame({"observation_id": ids, "api_reference_percent_w_w": ["2"] * 3 + ["15"] * 3})
    result = curate_tables(dataset, m, y)
    assert "api_reference_percent_w_w" in result.targets
    assert "api_concentration_design_percent" not in result.metadata
    assert result.report["identity"]["n_samples"] == 2
    assert result.report["identity"]["observations_per_unit"] == {"3": 2}
    assert result.report["identity"]["technical_repetitions"] == 3
    assert next(v for v in result.report["variables"] if v["name"] == "api_reference_percent_w_w")["unit"] == "% w/w"
    m.loc[0, "sample_id"] = "invalid_suffix"
    with pytest.raises(ValueError, match="vial.scan"):
        curate_tables(dataset, m, y)


def test_muscle_groups_subject_aspect_and_keeps_subject_level():
    m = pd.DataFrame({"observation_id": ["a", "b", "c", "d"], "sample_id": ["S1B_rep1", "S1B_rep2", "S1D_rep1", "S1D_rep2"], "source_label": ["S1B", "S1B", "S1D", "S1D"], "subject_id": ["S1"] * 4})
    structure, report = identity_view("mendeley_human_arm_muscle_vis_swir_reflectance", m)
    assert structure["sample_id"].tolist() == ["S1B", "S1B", "S1D", "S1D"]
    assert structure["subject_id"].nunique() == 1
    assert report["n_samples"] == 2


@pytest.mark.parametrize("dataset", ["canopy_treatment_2009_2016_to_cedar_ecosis", "soil_elevation_2024_lake_fire_ecosis", "nirpy_milk_nir", "nirpy_milk_powder_nir"])
def test_improper_experiment_dates_or_class_reused_labels_do_not_become_samples(dataset):
    structure, report = identity_view(dataset, pd.DataFrame({"observation_id": ["a", "b"], "sample_id": ["2009", "2009"]}))
    assert structure["sample_id"].isna().all()
    assert report["n_samples"] is None and not report["sample_id_available"]
    assert report["technical_repetitions"] is None


def test_file_local_rice_ids_have_collision_free_composite_identity():
    m = pd.DataFrame({"observation_id": ["a", "b", "c"], "variety": ["A", "B", "A|B"], "source_sample_id": ["001", "001", "|001"]})
    structure, report = identity_view("dryad_rice_leaf_reflectance_manual", m)
    assert report["n_samples"] == 3
    assert structure["sample_id"].is_unique
    assert json.loads(structure["sample_id"].iloc[0]) == ["A", "001"]


def test_lucas_enrichment_is_keyed_complete_and_preserves_periods_and_location_error(tmp_path):
    m = pd.DataFrame({"observation_id": ["o15", "o09", "other"], "ID_sample": ["uuid15", "uuid09", "uuid3"], "dataset_code": ["LUCAS.SSL"] * 3})
    site = pd.DataFrame({"dataset.code_ascii_txt": ["LUCAS.SSL"] * 3, "id.layer_uuid_txt": ["uuid09", "uuid15", "uuid3"], "id.dataset.site_ascii_txt": ["001", "001", "002"], "longitude.point_wgs84_dd": ["1", "1.1", "2"], "latitude.point_wgs84_dd": ["45", "45.1", "46"], "observation.date.begin_iso.8601_yyyy.mm.dd": ["2009-05-01", "2015-03-01", "2015-03-01"], "observation.date.end_iso.8601_yyyy.mm.dd": ["2012-08-01", "2015-10-01", "2015-10-01"], "location.point.error_any_m": ["1000"] * 3})
    path = tmp_path / "soilsite.csv.gz"
    site.to_csv(path, index=False, compression="gzip")
    result = curate_tables("ossl_lucas_visnir_soil_all_y", m, soilsite=path)
    assert result.enriched_metadata["campaign_year"].tolist() == ["2015", "2009", "2015"]
    assert result.structure["site_id"].tolist() == ["001", "001", "002"]
    assert result.enriched_metadata["campaign_date_end"].iloc[1] == "2012-08-01"
    assert result.enriched_metadata["location_error_m"].eq("1000").all()
    assert all(entry["sha256"] for entry in result.report["enrichments"])
    assert not result.warnings
    site = pd.concat([site, site.iloc[[0]]])
    site.to_csv(path, index=False, compression="gzip")
    with pytest.raises(ValueError, match="not unique"):
        curate_tables("ossl_lucas_visnir_soil_all_y", m, soilsite=path)


def test_keyless_y_requires_an_explicit_pairing_contract(tmp_path):
    (tmp_path / "M.csv").write_text("observation_id;sample_id\na;001\nb;002\n")
    (tmp_path / "Y.csv").write_text("api_reference_percent_w_w\n2\n15\n")
    with pytest.raises(ValueError, match="explicit source pairing"):
        curate_bundle(tmp_path, "synthetic")
    result = curate_bundle(tmp_path, "synthetic", assume_paired_y=True)
    assert any("not independently verified" in warning for warning in result.warnings)
    assert result.report["source_hashes"].keys() == {"M.csv", "Y.csv"}
    assert result.original_targets.columns.tolist() == ["api_reference_percent_w_w"]
    assert any(entry.get("operation") == "assumed_row_pairing_to_Y" and entry["source_resource"] == "M.csv" for entry in result.report["mapping"])


def test_units_prevent_alias_merging_and_source_missing_tokens_are_respected(tmp_path):
    (tmp_path / "M.csv").write_text("observation_id;Temperature;temperature\na;1;1\nb;2;2\nc;NA;3\n")
    (tmp_path / "datapackage.json").write_text(json.dumps({"resources": [{"path": "M.csv", "schema": {"fields": [{"name": "Temperature", "unit": "degC", "missingValues": ["", "NA"]}, {"name": "temperature", "unit": "K"}]}}]}))
    result = curate_bundle(tmp_path, "synthetic")
    assert result.metadata["temperature"].isna().sum() == 1
    assert result.metadata["temperature_2"].tolist() == [1.0, 2.0, 3.0]
    assert {v["unit"] for v in result.report["variables"]} == {"K", "degC"}
    assert any("different source units" in str(entry.get("reasons", [])) for entry in result.report["mapping"])


def test_numeric_category_codes_remain_categories():
    m = pd.DataFrame({"observation_id": ["a", "b", "c"], "treatment": ["001", "002", "002"]})
    result = curate_tables("synthetic", m, categorical_names={"treatment"})
    assert result.metadata["treatment"].tolist() == ["001", "002", "002"]
    stats = result.report["variables"][0]["stats"]
    assert stats["type"] == "categorical" and stats["imbalance_ratio"] == 2


def test_numeric_spellings_do_not_create_false_variability():
    m = pd.DataFrame({"observation_id": ["a", "b", "c"], "constant_measure": ["1", "1.0", "1,0"]})
    result = curate_tables("synthetic", m, numeric_names={"constant_measure"})
    assert result.metadata.columns.tolist() == ["observation_id", "sample_id"]
    assert next(entry["stats"]["n_unique"] for entry in result.report["mapping"] if entry["original_name"] == "constant_measure") == 1


def test_observation_ids_are_opaque_and_preserve_significant_source_spelling():
    m = pd.DataFrame({"observation_id": ["FeSi0043 ", "FeSi0043"], "sample_id": ["001", "002"]})
    result = curate_tables("synthetic", m)
    assert result.structure["observation_id"].tolist() == ["FeSi0043 ", "FeSi0043"]
    assert result.report["identity"]["n_samples"] == 2
