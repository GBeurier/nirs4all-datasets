"""Explicit fleet migration does not turn historical raw values into fresh calculations."""
from __future__ import annotations

import json
import runpy
from copy import deepcopy
from pathlib import Path

import pytest


def test_metadata_card_migration_preserves_raw_values_and_is_idempotent(monkeypatch):
    from nirs4all_datasets.qualify import metrics

    migrate = runpy.run_path(str(Path(__file__).parents[1] / "scripts/migrate_card_protocol7.py"))["migrate_card"]
    old = {"protocol_version": "6", "generated_at": "historical", "integrity": {"content_hash": "unaltered"}, "sources": [{"source_id": "X", "spectral": {"profile": {"noise": {"snr": 8.0}, "structure": {"local_outlier_factor_p95": 1.4}, "diagnostics": [{"key": "vera25_like", "score": .8}]}}}]}
    original = deepcopy(old)
    def forbidden(*a, **k):
        raise AssertionError("metadata migration cannot recompute a scientific kernel")
    for name in ["_basic_pca", "spectral_noise", "reference_similarity", "dataset_structure_metrics"]:
        monkeypatch.setattr(metrics, name, forbidden)
    new = migrate(old)
    assert old == original and new["generated_at"] == "historical" and new["integrity"] == old["integrity"]
    profile = new["sources"][0]["spectral"]["profile"]
    assert profile["noise"]["snr"] == profile["noise"]["roughness_signal_to_noise_proxy"] == 8.0
    assert profile["structure"]["local_outlier_factor_p95"] == profile["structure"]["knn_distance_ratio_p95"] == 1.4
    assert profile["signature_metadata"]["source_protocol"] == "6" and "vera25_like" not in json.dumps(profile["diagnostics"])
    assert new["qualification_provenance"]["legacy_calculation_protocol"] == "6"
    assert migrate(new) == new


def test_migration_refuses_unknown_or_shared_source_protocols():
    migrate = runpy.run_path(str(Path(__file__).parents[1] / "scripts/migrate_card_protocol7.py"))["migrate_card"]
    with pytest.raises(ValueError, match="protocol 6 or 7"):
        migrate({"protocol_version": "unknown"})
    with pytest.raises(ValueError, match="shared assessment"):
        migrate({"protocol_version": "6", "assessment_mode": "shared"})
