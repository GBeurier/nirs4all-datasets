"""Scientific naming and explicit protocol migration preserve historical evidence."""
from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

import pytest

from nirs4all_datasets.qualify import metrics


def test_heuristic_strength_is_never_a_causal_probability_and_mean_is_explicit():
    rows = metrics.diagnostic_hypotheses({})
    assert rows
    assert all(row["confidence_status"] == "unvalidated" for row in rows)
    assert all(row["score_kind"] == "heuristic_signature" for row in rows)
    assert all("0.78" in row["score_explanation"] and "78%" in row["score_explanation"] for row in rows)
    assert all(row["recommended_verifications"] for row in rows)
    assert "RMS/SAM référence" not in json.dumps(rows, ensure_ascii=False)
    assert all(row["score"] is None for row in rows)


def test_domain_specific_vera25_is_opt_in_and_still_unvalidated():
    assert "vera25_like" not in {row["key"] for row in metrics.diagnostic_hypotheses({})}
    rows = metrics.diagnostic_hypotheses({}, domain_context="VERA25")
    vera = next(row for row in rows if row["key"] == "vera25_like")
    assert vera["domain_context"] == "VERA25"
    assert vera["specificity_status"] == vera["confidence_status"] == "unvalidated"
    with pytest.raises(ValueError, match="domain_context"):
        metrics.diagnostic_hypotheses({}, domain_context="unvalidated-new-domain")


def test_protocol_golden_keeps_old_raw_values_and_uses_truthful_proxy_ids():
    golden = json.loads((Path(__file__).parent / "goldens/qualification_protocol_6_7.json").read_text())
    old = golden["protocol6_profile"]
    original = deepcopy(old)
    migrated = metrics.migrate_profile_metadata(old, from_protocol="6")
    assert old == original
    for dotted, expected in golden["protocol7_proxy_values"].items():
        section, field = dotted.split(".")
        assert migrated[section][field] == expected
    for section in ["noise", "structure"]:
        for name, value in original[section].items():
            assert migrated[section][name] == value
    assert migrated["signature_metadata"] == golden["protocol7_metadata"]
    assert metrics.migrate_profile_metadata(migrated, from_protocol="7") == migrated
    catalog = metrics.metric_catalog()
    assert next(item for item in catalog if item["key"] == "structure.knn_distance_ratio_p95")["metric"] == "kNN distance ratio (not LOF)"
    assert next(item for item in catalog if item["key"] == "noise.roughness_signal_to_noise_proxy")["legacy_key"] == "noise.snr"
    # An old card is still readable, with the value bound to its original definition.
    rows = metrics.metric_score_rows(old)
    assert next(row for row in rows if row["key"] == "structure.knn_distance_ratio_p95")["value"] == 1.4
    assert next(row for row in rows if row["key"] == "noise.roughness_signal_to_noise_proxy")["value"] == 8.0


def test_legacy_alias_never_overwrites_a_distinct_producer_value():
    profile = {"noise": {"snr": 8.0, "roughness_signal_to_noise_proxy": 11.0}}
    assert metrics.with_metric_semantics(profile)["noise"]["roughness_signal_to_noise_proxy"] == 11.0
    with pytest.raises(ValueError, match="explicit protocol"):
        metrics.migrate_profile_metadata(profile, from_protocol="unknown")


def test_unavailable_or_empty_ids_never_form_a_repeat_group():
    import numpy as np
    import pandas as pd

    x = np.ones((8, 4))
    x[:5] *= np.arange(1, 6)[:, None]
    result = metrics.repeatability_metrics(x, [None, float("nan"), pd.NA, "", "  ", "NA", "NA", "one"])
    assert result["n_repeat_groups"] == 1  # Literal scientific ID "NA" is valid.
    assert result["rms_intra_id"] == 0.0
    assert metrics.repeatability_metrics(x[:2], [None, None])["n_repeat_groups"] == 0


def test_old_card_display_preserves_score_and_hides_domain_hypothesis_by_default():
    from nirs4all_datasets.site.pages import _combined_diagnostics

    old = {"diagnostics": [
        {"key": "white_calibration", "label": "Erreur calibration", "score": 0.78, "evidence": [{"signal": "RMS/SAM référence", "level": 0.5}]},
        {"key": "vera25_like", "label": "VERA25-like", "score": 0.9},
    ]}
    original = deepcopy(old)
    presented = _combined_diagnostics([("X", old)])
    assert old == original
    assert len(presented) == 1
    assert presented[0]["score"] == 0.78
    assert "compatible" in presented[0]["label"]
    assert presented[0]["confidence_status"] == "unvalidated"
    assert presented[0]["evidence"][0]["signal"] == "RMS/SAM to mean spectrum"
    assert len(_combined_diagnostics([("X", old)], domain_context="VERA25")) == 2


def test_anonymized_card_hides_domain_context_and_specific_suggestions():
    from nirs4all_datasets.qualify.anonymize import anonymize_card

    original = {"qualification_provenance": {"diagnostic_domain": "VERA25"}, "sources": [{"source_id": "X", "spectral": {"profile": {
        "diagnostics": [{"key": "vera25_like", "domain_context": "VERA25"}], "signature_metadata": {"domain_context": "VERA25"},
    }}}]}
    assert "VERA25" not in json.dumps(anonymize_card(original))
    assert original["qualification_provenance"]["diagnostic_domain"] == "VERA25"


def test_knn_proxy_matches_its_population_median_definition_not_local_reachability():
    import numpy as np

    result = metrics.dataset_structure_metrics(np.zeros((4, 2)), pca={"scores": np.array([[0.], [1.], [2.], [10.]])})
    # k=3 gives mean distances 13/3, 11/3, 11/3, 9 and population median 4.
    assert result["knn_distance_ratio_p95"] == pytest.approx(2.075, abs=1e-14)
    assert result["local_outlier_factor_p95"] == result["knn_distance_ratio_p95"]
    row = next(item for item in metrics.metric_catalog() if item["key"] == "structure.knn_distance_ratio_p95")
    assert "median population" in row["formula"] and "not LOF" in row["formula"]
