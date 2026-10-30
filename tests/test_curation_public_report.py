"""Tracked curation summaries do not publish per-observation issue values."""
from copy import deepcopy

from nirs4all_datasets.curation import catalog_curation_report


def test_public_report_summarizes_issues_without_mutating_local_report():
    report = {
        "schema_version": "1.1", "dataset_id": "sample", "views": {"M": ["dose"], "Y": []},
        "mapping": [{"original_name": "dose", "stats": {"n_invalid": 2}, "value_issues": [
            {"observation_id": "private-observation", "raw": "private-value", "status": "invalid"},
            {"observation_id": "another", "raw": "<5", "status": "censored"},
            {"observation_id": "third", "raw": "bad", "status": "invalid"},
        ]}],
    }
    original = deepcopy(report)
    public = catalog_curation_report(report)
    assert report == original
    entry = public["mapping"][0]
    assert entry["value_issue_counts"] == {"censored": 1, "invalid": 2}
    assert entry["value_issue_detail"] == "Retained in local canonical/curation/mapping.json"
    assert "value_issues" not in entry
    assert "private-observation" not in str(public) and "private-value" not in str(public)
    assert entry["stats"] == {"n_invalid": 2}
    assert catalog_curation_report(report, anonymized=True) == {
        "schema_version": "1.1", "dataset_id": "sample", "view_counts": {"M": 1, "Y": 0}, "mapping": "withheld for anonymized tier",
    }
