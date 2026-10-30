"""Identity, scientific targets and source-specific missing-value regressions."""
from __future__ import annotations

import json

import pandas as pd
import pytest
from conftest import make_v2_leaf

from nirs4all_datasets.bootstrap import build_descriptor_from_card
from nirs4all_datasets.canonical import build_canonical
from nirs4all_datasets.curation import consumer_views, enrich_lucas_metadata, identity_frame, normalize_variable
from nirs4all_datasets.qualify import metrics
from nirs4all_datasets.schema import Variable


@pytest.mark.parametrize("bad", [None, float("nan"), float("inf"), "unknown", True])
def test_unavailable_diagnostic_evidence_never_becomes_zero_or_normal(bad):
    profile = {"outliers": {"pca_q_ratio": bad}}
    rows = metrics.diagnostic_hypotheses(profile)
    assert all(row["score"] is None for row in rows)
    assert all(row["confidence_status"] == "unvalidated" for row in rows)
    normal = next(row for row in rows if row["key"] == "normal")
    assert normal["strength"] == "unknown"
    assert normal["evidence_coverage"] == 0
    assert metrics._saturate(0.0) == 0.0


def test_partial_evidence_is_explicit_and_serializes_without_nan():
    rows = metrics.diagnostic_hypotheses({"outliers": {"pca_q_ratio": 8.0}})
    noisy = next(row for row in rows if row["key"] == "very_noisy")
    assert noisy["availability"] == "partial"
    assert 0 < noisy["evidence_coverage"] < 1
    assert noisy["score"] is None
    assert noisy["interpretation_kind"] == "possible_cause"
    assert noisy["reference_scope"] == "dataset_mean_not_independent_reference"
    json.dumps(rows, allow_nan=False)


def test_missing_rules_are_column_scoped_and_preserve_censoring_and_raw_tokens():
    codes = pd.Series(["NA", "none", "ND", "001", ""])
    kept, _ = normalize_variable(codes, Variable(name="code", type="categorical"))
    assert kept.iloc[:4].tolist() == ["NA", "none", "ND", "001"]
    values = pd.Series(["NA", "no data", "-999", "0", "-2", "<0,1", "inf", "1.234,5"])
    normalized, audit = normalize_variable(values, Variable(name="measured", missing_values=["NA", "no data"], numeric_sentinels=[-999], decimal_separator=",", thousands_separator="."))
    assert normalized.iloc[3:5].tolist() == [0.0, -2.0]
    assert normalized.iloc[7] == 1234.5
    assert (audit["missing"], audit["censored"], audit["invalid"]) == (3, 1, 1)
    assert audit["rows"][5]["raw"] == "<0,1"
    assert audit["rows"][5]["status"] == "censored"
    assert audit["rows"][5]["censoring"] == {"operator": "<", "bound": 0.1, "unit": None}
    assert values.iloc[2] == "-999"


def test_blank_ids_never_group_and_source_suffixes_are_not_globally_stripped():
    source = pd.DataFrame({"observation_id": ["o1", "o2", "o3"], "sample_id": ["001", "", "product.0"]})
    result, report = identity_frame("unknown_source", source)
    assert result["sample_id"].tolist() == ["001", "o2", "product.0"]
    assert report["sample_id_available"] is False
    assert report["n_units"] is None
    assert source["sample_id"].iloc[1] == ""


def test_source_specific_vial_and_subject_hierarchy():
    frame = pd.DataFrame({"observation_id": ["o1", "o2", "o3"], "sample_id": ["RH11_API02_RW1_v12.0", "RH11_API02_RW1_v12.1", "RH11_API02_RW1_v12.2"]})
    mapped, report = identity_frame("ucph_granules_ambient_moisture_api_nir", frame)
    assert mapped["sample_id"].nunique() == 1
    assert mapped["acquisition_index"].tolist() == ["0", "1", "2"]
    assert report["method"] == "granule_vial"
    assert report["unit"]  # reviewed source contract wording is preserved
    with pytest.raises(ValueError, match="documented"):
        identity_frame("ucph_granules_ambient_moisture_api_nir", frame.iloc[:2])
    muscle = pd.DataFrame({"observation_id": ["o1", "o2", "o3"], "subject_id": ["S1", "S1", "S1"], "arm_aspect_code": ["B", "B", "D"], "source_label": ["S1_B", "S1_B", "S1_D"]})
    _, report = identity_frame("mendeley_human_arm_muscle_vis_swir_reflectance", muscle)
    assert report["n_units"] == 2
    assert report["source_columns"] == ["source_label"]


def test_consumer_views_retain_scientific_api_reference_and_exclude_target_copies(tmp_path):
    leaf = make_v2_leaf(tmp_path / "ucph_granules_ambient_moisture_api_nir", targets={"api_reference_percent_w_w": "numeric"})
    descriptor, _ = build_descriptor_from_card(leaf)
    descriptor.variables.extend([Variable(name="license", type="text"), Variable(name="temperature"), Variable(name="raw_label", equivalent_to="api_reference_percent_w_w"), Variable(name="api_concentration_design_percent"), Variable(name="encoded", derived_from=["api_reference_percent_w_w"])])
    frame = pd.DataFrame({"sample_id": ["v1", "v2"], "api_reference_percent_w_w": [2.0, 5.25], "license": ["A", "B"], "temperature": [20, 22], "raw_label": [2.0, 5.25], "api_concentration_design_percent": [2.0, 5.25], "encoded": [0, 1]})
    view = consumer_views(frame, descriptor)
    assert list(view["Y"]) == ["sample_id", "api_reference_percent_w_w"]
    assert list(view["M"]) == ["sample_id", "temperature"]
    assert list(view["passport"]) == ["sample_id", "license"]
    assert frame.equals(view["original"])


def test_acquisition_values_are_preserved_when_vial_metadata_changes(tmp_path):
    leaf = make_v2_leaf(tmp_path / "ucph_granules_ambient_moisture_api_nir", block_obs={"X": ["o1", "o2", "o3"]}, sample_of={"o1": "RH_API02_RW1_v1.0", "o2": "RH_API02_RW1_v1.1", "o3": "RH_API02_RW1_v1.2"}, targets={"api_reference_percent_w_w": "numeric"}, extra_meta=["time"])
    m = pd.read_csv(leaf / "M.csv", sep=";")
    m["time"] = [1, 2, 3]
    m.to_csv(leaf / "M.csv", sep=";", index=False)
    y = pd.read_csv(leaf / "Y.csv", sep=";")
    y["api_reference_percent_w_w"] = 2.0
    y.to_csv(leaf / "Y.csv", sep=";", index=False)
    descriptor, _ = build_descriptor_from_card(leaf)
    out = tmp_path / "out"
    result = build_canonical(leaf, descriptor, out)
    variables = pd.read_parquet(out / "canonical/variables.parquet")
    observations = pd.read_parquet(out / "canonical/observations.parquet")
    assert len(variables) == 3
    assert variables["time"].tolist() == [1, 2, 3]
    assert result.config["variables"]["join_key"] == "observation_id"
    assert observations["time"].tolist() == [1, 2, 3]
    assert observations["sample_id"].nunique() == 1
    assert any("observation grain" in warning for warning in result.warnings)


def test_lucas_join_preserves_campaign_intervals_and_site_grouping(tmp_path):
    from nirs4all_datasets.curation import LUCAS_SOILSITE_FIELDS

    original = {name: ["site1", "site1"] if name.startswith("id.dataset") else ["2009-05-01", "2015-03-01"] if "begin" in name else ["2012-08-01", "2015-10-01"] if "end" in name else ["1000", "1000"] for name in LUCAS_SOILSITE_FIELDS}
    site = pd.DataFrame({"dataset.code_ascii_txt": ["LUCAS.SSL"] * 2, "id.layer_uuid_txt": ["a", "b"], **original})
    path = tmp_path / "soilsite.csv.gz"
    site.to_csv(path, index=False)
    metadata = pd.DataFrame({"observation_id": ["o2", "o1"], "ID_sample": ["b", "a"], "dataset_code": ["LUCAS.SSL"] * 2})
    enriched, report = enrich_lucas_metadata(metadata, str(path))
    assert enriched["campaign_year"].tolist() == ["2015", "2009"]
    assert enriched["campaign_end_date"].tolist() == ["2015-10-01", "2012-08-01"]
    assert enriched["site_id"].nunique() == 1
    assert report["n_sites"] == 1
    assert "individual collection date" in report["derived"]["campaign_year"]
    assert "site_id" not in metadata


def test_declared_name_mapping_and_missing_rule_survive_regeneration(tmp_path):
    from nirs4all_datasets.manifest import processing_hash

    leaf = make_v2_leaf(tmp_path / "mapped", targets={"original concentration": "numeric"})
    descriptor, _ = build_descriptor_from_card(leaf)
    descriptor.variables[0] = Variable(name="concentration", original_name="original concentration", role="target", missing_values=["ND"], decimal_separator=".")
    y = pd.read_csv(leaf / "Y.csv", sep=";")
    y["original concentration"] = ["ND", "2.5"]
    y.to_csv(leaf / "Y.csv", sep=";", index=False)
    out = tmp_path / "out"
    build_canonical(leaf, descriptor, out)
    first = pd.read_parquet(out / "canonical/variables.parquet")
    assert "concentration" in first and "original concentration" not in first
    assert first["concentration"].isna().sum() == 1
    build_canonical(leaf, descriptor, out)
    assert first.equals(pd.read_parquet(out / "canonical/variables.parquet"))
    changed = descriptor.model_copy(deep=True)
    changed.variables[0].missing_values = []
    assert processing_hash(changed) != processing_hash(descriptor)


def test_identical_vectors_are_reported_without_claiming_reacquisition(tmp_path):
    leaf = make_v2_leaf(tmp_path / "copies", targets={})
    descriptor, _ = build_descriptor_from_card(leaf)
    result = build_canonical(leaf, descriptor, tmp_path / "out")
    duplicates = result.config["sources"][0]["duplicate_vectors"]
    assert duplicates["distinct"] == 1
    assert duplicates["additional_copies"] == 1
    assert "not proof" in duplicates["semantics"]
    assert pd.read_parquet(tmp_path / "out/canonical/sources/X.parquet").shape[0] == 2


def test_unknown_profile_axes_are_not_plotted_at_zero():
    from nirs4all_datasets.site.charts import radar_profiles

    svg = radar_profiles([{"label": "partial", "scores": {"noise_risk": 0.8}}])
    assert "fewer than three profile axes available" in svg
    assert "partial profile" not in svg


def test_partial_profile_draws_only_available_axes():
    from nirs4all_datasets.site.charts import radar_profiles

    svg = radar_profiles([{"label": "partial", "scores": {"integrity_risk": 0.0, "noise_risk": 0.8, "shape_drift": 0.3}}])
    assert "partial — integrity: 0.00" in svg
    assert "partial — noise: 0.80" in svg
    assert "partial — repeatability" not in svg
    assert "partial profile</title>" not in svg  # no filled polygon across missing axes


def test_lucas_source_context_is_content_addressed_and_regenerated(tmp_path):
    from nirs4all_datasets.curation import LUCAS_SOILSITE_FIELDS
    from nirs4all_datasets.organize import organize

    leaf = make_v2_leaf(tmp_path / "ossl_lucas_visnir_soil_all_y", targets={}, extra_meta=["ID_sample", "dataset_code"])
    metadata = pd.read_csv(leaf / "M.csv", sep=";")
    metadata["ID_sample"] = ["layer_a", "layer_b"]
    metadata["dataset_code"] = "LUCAS.SSL"
    metadata.to_csv(leaf / "M.csv", sep=";", index=False)
    fields = {key: ["site_1", "site_1"] if key.startswith("id.dataset") else ["2009-05-01", "2015-03-01"] if "begin" in key else ["2012-08-01", "2015-10-01"] if "end" in key else ["1000", "1000"] for key in LUCAS_SOILSITE_FIELDS}
    site = pd.DataFrame({"dataset.code_ascii_txt": ["LUCAS.SSL"] * 2, "id.layer_uuid_txt": ["layer_a", "layer_b"], **fields})
    path = tmp_path / "soilsite.csv.gz"
    site.to_csv(path, index=False)
    descriptor, _ = build_descriptor_from_card(leaf)
    kwargs = {"source_context": {"soilsite": str(path)}}
    result = organize(leaf, descriptor, tmp_path / "datasets", **kwargs)
    assert not result.skipped
    assert organize(leaf, descriptor, tmp_path / "datasets", **kwargs).skipped
    variables = pd.read_parquet(result.dataset_dir / "canonical/variables.parquet")
    assert variables["site_id"].nunique() == 1
    assert variables["campaign_year"].tolist() == ["2009", "2015"]
    # A changed auxiliary source must invalidate the manifest even with X/Y/M unchanged.
    site["longitude.point_wgs84_dd"] = [11, 12]
    site.to_csv(path, index=False)
    assert not organize(leaf, descriptor, tmp_path / "datasets", **kwargs).skipped
    variables = pd.read_parquet(result.dataset_dir / "canonical/variables.parquet")
    assert variables["longitude"].tolist() == [11.0, 12.0]


def test_scientific_source_prefixed_covariate_survives_bootstrap_and_views(tmp_path):
    leaf = make_v2_leaf(tmp_path / "prefix", targets={}, extra_meta=["source_temperature", "source_file"])
    metadata = pd.read_csv(leaf / "M.csv", sep=";")
    metadata["source_temperature"] = [21.5, 23.5]
    metadata.to_csv(leaf / "M.csv", sep=";", index=False)
    descriptor, _ = build_descriptor_from_card(leaf)
    out = tmp_path / "out"
    build_canonical(leaf, descriptor, out)
    frame = pd.read_parquet(out / "canonical/variables.parquet")
    assert frame["source_temperature"].tolist() == [21.5, 23.5]
    assert "source_temperature" in consumer_views(frame, descriptor)["M"]
    assert "source_file" not in consumer_views(frame, descriptor)["M"]


def test_conflicting_identity_aliases_are_rejected_but_hierarchies_are_journaled():
    frame = pd.DataFrame({"observation_id": ["o1", "o2"], "sample_id": ["001", "002"], "ID_sample": ["A", "B"]})
    with pytest.raises(ValueError, match="ambiguous sample identity"):
        identity_frame("unknown_source", frame)
    frame = frame.drop(columns=["ID_sample"])
    frame["source_sample_id"] = ["batch_1", "batch_1"]
    mapped, report = identity_frame("unknown_source", frame)
    assert mapped["sample_id"].tolist() == ["001", "002"]
    assert mapped["source_sample_id"].tolist() == ["batch_1", "batch_1"]
    assert report["identity_columns"]["source_sample_id"]["role"] == "hierarchical_source_identifier"


def test_equal_values_alone_do_not_exclude_an_independent_scientific_covariate(tmp_path):
    leaf = make_v2_leaf(tmp_path / "unrelated", targets={"protein": "numeric"})
    descriptor, _ = build_descriptor_from_card(leaf)
    descriptor.variables.append(Variable(name="temperature"))
    frame = pd.DataFrame({"sample_id": ["a", "b"], "protein": [20., 22.], "temperature": [20., 22.]})
    assert consumer_views(frame, descriptor)["M"]["temperature"].tolist() == [20., 22.]


def test_card_variable_denominator_tracks_actual_observation_grain(tmp_path):
    from conftest import make_v2_leaf

    from nirs4all_datasets.bootstrap import build_descriptor_from_card
    from nirs4all_datasets.canonical import build_canonical
    from nirs4all_datasets.qualify.profile import build_card

    leaf = make_v2_leaf(tmp_path / "grain_fixture", block_obs={"X": ["o1", "o2", "o3"]}, sample_of={"o1": "s1", "o2": "s1", "o3": "s2"}, targets={"response": "numeric"})
    (leaf / "Y.csv").write_text("observation_id;response\no1;1\no2;2\no3;3\n")
    descriptor, _ = build_descriptor_from_card(leaf)
    out = tmp_path / "out"
    build_canonical(leaf, descriptor, out)
    card = build_card(out, descriptor, assessment_mode="shared", compute_assets=False, compute_pca=False)
    section = next(v for v in card["variables"] if v["name"] == "response")
    assert card["variable_join_key"] == "observation_id"
    assert section["denominator"] == "canonical_observations"
    assert section["normalization"]["total"] == 3
    assert card["alignment"]["n_samples"] == 2
