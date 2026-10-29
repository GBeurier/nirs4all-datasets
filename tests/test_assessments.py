"""Optional owner-produced assessments preserve identity, context and legacy cards."""
from __future__ import annotations

import json

import pytest
from conftest import make_v2_leaf
from pydantic import ValidationError

from nirs4all_datasets.bootstrap import build_descriptor_from_card
from nirs4all_datasets.canonical import build_canonical
from nirs4all_datasets.dataset import NirsDataset
from nirs4all_datasets.qualify.assessments import (
    Assessment,
    canonical_content_hash,
    intrinsic_profile,
    public_assessments,
    read_assessments,
    write_assessments,
)
from nirs4all_datasets.qualify.profile import build_card


def prepared(tmp_path):
    leaf = make_v2_leaf(tmp_path / "source", targets={"API_reference": "numeric"})
    descriptor, _ = build_descriptor_from_card(leaf)
    out = tmp_path / "out"
    build_canonical(leaf, descriptor, out)
    report = {
        "schema_version": "1", "dataset_id": descriptor.id,
        "content_hash": canonical_content_hash(out), "producer": "nirs4all-preflight",
        "engine_version": "0.1.0", "protocol_version": "1", "source_id": "X",
        "population_id": "all_samples", "context_id": "intrinsic", "scope": "intrinsic",
        "metrics": [{"metric_id": "outliers.pca_q_ratio", "protocol_version": "2", "value": None, "availability": "unavailable", "reason_code": "insufficient_samples"}],
    }
    return out, descriptor, report


def test_sidecar_does_not_change_legacy_card_or_canonical_identity(tmp_path):
    out, descriptor, report = prepared(tmp_path)
    card = {"legacy": "unchanged"}
    (out / "card.json").write_text(json.dumps(card))
    digest = canonical_content_hash(out)
    ds = NirsDataset(out, descriptor)
    assert ds.assessments() == []
    write_assessments(out, descriptor.id, [report])
    assert canonical_content_hash(out) == digest
    assert ds.card() == card
    assert read_assessments(out, descriptor.id)[0]["metrics"][0]["value"] is None
    assert ds.assessments()[0]["population_id"] == "all_samples"


def test_wrong_content_and_source_are_rejected(tmp_path):
    out, descriptor, report = prepared(tmp_path)
    with pytest.raises(ValueError, match="content identity"):
        write_assessments(out, descriptor.id, [report | {"content_hash": "0" * 64}])
    with pytest.raises(ValueError, match="source"):
        write_assessments(out, descriptor.id, [report | {"source_id": "missing"}])
    with pytest.raises(ValueError, match="duplicate assessment"):
        write_assessments(out, descriptor.id, [report, report])
    write_assessments(out, descriptor.id, [report])
    (out / "canonical/dataset.json").write_text((out / "canonical/dataset.json").read_text() + "\n")
    with pytest.raises(ValueError, match="content identity"):
        read_assessments(out, descriptor.id)


def test_context_and_nonfinite_values_are_not_silently_repaired(tmp_path):
    _, _, report = prepared(tmp_path)
    with pytest.raises(ValidationError, match="intrinsic"):
        Assessment.model_validate(report | {"target_id": "Y_test"})
    with pytest.raises(ValidationError, match="task assessments require"):
        Assessment.model_validate(report | {"scope": "task"})
    with pytest.raises(ValidationError):
        Assessment.model_validate(report | {"metrics": [{"metric_id": "noise.snr_db", "protocol_version": "1", "availability": "available", "value": float("inf")}]})
    task = report | {"scope": "task", "target_id": "API_reference", "split_id": "test", "fit_population_id": "train", "evaluation_population_id": "test"}
    with pytest.raises(ValueError, match="task-scoped"):
        intrinsic_profile(task)


def test_shared_mode_never_refits_or_falls_back_to_legacy_kernels(tmp_path, monkeypatch):
    from nirs4all_datasets.qualify import metrics, profile

    out, descriptor, report = prepared(tmp_path)
    write_assessments(out, descriptor.id, [report])
    def forbidden(*args, **kwargs):
        raise AssertionError("legacy scientific kernel was recomputed")
    monkeypatch.setattr(metrics, "_basic_pca", forbidden)
    monkeypatch.setattr(metrics, "spectral_quality", forbidden)
    monkeypatch.setattr(profile, "_source_pca", forbidden)
    monkeypatch.setattr(profile, "_x_outliers", forbidden)
    card = build_card(out, descriptor, assessment_mode="shared")
    assert card["sources"][0]["spectral"]["profile"]["outliers"]["pca_q_ratio"] is None
    assert card["sources"][0]["spectral"]["pca"] is None
    assert card["assessments"][0]["producer"] == "nirs4all-preflight"
    assert all(d["score"] is None for d in card["sources"][0]["spectral"]["profile"]["diagnostics"])


def test_anonymized_sidecars_drop_identifiers_and_detailed_values(tmp_path):
    _, _, report = prepared(tmp_path)
    report["population_id"] = "private population name"
    report["target_id"] = None
    safe = public_assessments([report], anonymized=True)
    text = json.dumps(safe)
    assert "private population name" not in text
    assert "content_hash" not in text
    assert "metrics" not in text
    assert safe[0]["availability"] == "redacted"


def test_actual_preflight_cli_report_is_accepted_losslessly():
    """Fixture generated by Preflight's actual Rust extract-assessment CLI, schema 1."""
    from pathlib import Path

    raw = json.loads((Path(__file__).parent / "fixtures/preflight-assessment-v1.json").read_text())
    parsed = Assessment.model_validate(raw)
    assert parsed.producer == "nirs4all-preflight"
    assert parsed.report == raw["report"]
    for original, metric in zip(raw["metrics"], parsed.metrics, strict=True):
        assert metric.native_metric == original["native_metric"]
        assert metric.native_status == original["native_status"]
        if metric.availability != "available":
            assert metric.value is None
            assert metric.reason_code


def test_metric_identity_includes_the_view(tmp_path):
    _, _, report = prepared(tmp_path)
    metric = report["metrics"][0]
    two_views = report | {"metrics": [metric | {"view_id": "raw"}, metric | {"view_id": "processed"}]}
    assert len(Assessment.model_validate(two_views).metrics) == 2
    with pytest.raises(ValidationError, match="duplicate metric"):
        Assessment.model_validate(report | {"metrics": [metric, metric]})
