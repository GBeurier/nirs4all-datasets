"""Opt-in real owner executable → versioned sidecar → card integration, with no mock kernels."""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
from conftest import make_v2_leaf

from nirs4all_datasets.bootstrap import build_descriptor_from_card
from nirs4all_datasets.canonical import build_canonical
from nirs4all_datasets.dataset import NirsDataset
from nirs4all_datasets.qualify.assessments import canonical_content_hash, read_assessments, write_assessments
from nirs4all_datasets.qualify.profile import build_card


@pytest.mark.skipif(not os.environ.get("NIRS4ALL_PREFLIGHT_CLI"), reason="optional owner executable: set NIRS4ALL_PREFLIGHT_CLI to run native conformance")
def test_real_preflight_count_and_mask_are_served_without_legacy_substitution(tmp_path, monkeypatch):
    binary = Path(os.environ["NIRS4ALL_PREFLIGHT_CLI"]).resolve()
    binary_hash = hashlib.sha256(binary.read_bytes()).hexdigest()
    ids = [f"o{i}" for i in range(6)]
    samples = {observation: f"s{i}" for i, observation in enumerate(ids)}
    leaf = make_v2_leaf(tmp_path / "analytic_fixture", block_obs={"X": ids}, sample_of=samples, targets={})
    matrix = np.array([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9]], dtype=float)
    matrix[1, 1] = np.nan
    matrix[4, 3] = np.nan
    pd.DataFrame({"observation_id": ids, **{str(1100 + 2 * column): matrix[:, column] for column in range(4)}}).to_csv(leaf / "X.csv", sep=";", index=False)
    raw_card = json.loads((leaf / "dataset_card.json").read_text())
    raw_card["spectral_blocks"][0].update(n_spectral_variables=4, axis_max="1106")
    (leaf / "dataset_card.json").write_text(json.dumps(raw_card))
    descriptor, _ = build_descriptor_from_card(leaf)
    out = tmp_path / "canonical_fixture"
    build_canonical(leaf, descriptor, out)
    frame = pd.read_parquet(out / "canonical/sources/X.parquet")
    feature_names = [name for name in frame if name not in {"observation_id", "sample_id"}]
    values = frame[feature_names].to_numpy(dtype=float)
    assert values.shape == (6, 4) and np.isnan(values).sum() == 2
    valid = np.isfinite(values)
    valid[0, 0] = False  # A finite but explicitly excluded cell: distinct from legacy NaN ratio.
    view = {"source_id": "X", "view_id": "native", "valid_mask": valid.tolist(), "meaning": "synthetic conformance validity mask; no benchmark or physical-independence claim"}
    view_path = out / "canonical/assessment_views/native.json"
    view_path.parent.mkdir()
    view_path.write_text(json.dumps(view, sort_keys=True))
    digest = canonical_content_hash(out)  # Includes the actual mask artifact.
    payload = {"schema_version": 1, "data_origin": "synthetic", "sources": [{
        "source_id": "X", "observation_ids": frame.observation_id.tolist(), "sample_ids": frame.sample_id.tolist(),
        "x": [[float(value) if np.isfinite(value) else None for value in row] for row in values],
        "valid_mask": view["valid_mask"], "axis": [float(name) for name in feature_names],
        "axis_unit": "nm", "signal_unit": "arbitrary", "signal_type": "unknown",
    }], "samples": [{"sample_id": sample, "partition": "development"} for sample in frame.sample_id], "targets": []}
    input_path = tmp_path / "native-input.json"
    input_path.write_text(json.dumps(payload, allow_nan=False))
    report_path = tmp_path / "native-report.json"
    context_path = tmp_path / "context.json"
    context_path.write_text(json.dumps({"dataset_id": descriptor.id, "content_hash": digest, "producer": "nirs4all-preflight", "source_id": "X", "population_id": "development_real", "context_id": "intrinsic/masked-conformance/v1", "scope": "intrinsic", "semantics": {}}))
    receipts = []
    for command, output in [([str(binary), "analyze", str(input_path)], report_path), ([str(binary), "extract-assessment", str(report_path), str(context_path)], tmp_path / "assessment.json")]:
        result = subprocess.run(command, capture_output=True, check=False)
        output.write_bytes(result.stdout)
        output.with_suffix(output.suffix + ".stderr.log").write_bytes(result.stderr)
        receipts.append({"command": command, "exit": result.returncode, "stdout_sha256": hashlib.sha256(result.stdout).hexdigest(), "stderr_sha256": hashlib.sha256(result.stderr).hexdigest()})
        assert result.returncode == 0, result.stderr.decode(errors="replace")
    assessment = json.loads((tmp_path / "assessment.json").read_text())
    metric = next(item for item in assessment["metrics"] if item["metric_id"] == "integrity.missing_cells")
    assert metric["availability"] == "available" and metric["value"] == 3
    assert metric["native_metric"]["denominators"]["n_cells"] == 24
    old_card = {"protocol_version": "6", "legacy": "unchanged"}
    (out / "card.json").write_text(json.dumps(old_card))
    write_assessments(out, descriptor.id, [assessment])
    assert read_assessments(out, descriptor.id)[0]["report"] == assessment["report"]
    from nirs4all_datasets.qualify import metrics

    def forbidden(*args, **kwargs):
        raise AssertionError("shared owner evidence must not invoke a legacy scientific kernel")
    for name in ["_basic_pca", "spectral_quality", "spectral_noise", "reference_similarity", "dataset_structure_metrics"]:
        monkeypatch.setattr(metrics, name, forbidden)
    card = build_card(out, descriptor, assessment_mode="shared", compute_assets=False, compute_pca=False)
    profile = card["sources"][0]["spectral"]["profile"]
    assert profile["integrity"]["missing_cells"] == 3
    assert profile["integrity"].get("nan_ratio") is None  # Do not invent 3/24 as legacy NaN ratio.
    assert profile["producer"]["population_id"] == "development_real"
    assert all(row["score"] is None for row in profile["diagnostics"])
    assert NirsDataset(out, descriptor).card() == old_card
    assert canonical_content_hash(out) == digest
    assert hashlib.sha256(binary.read_bytes()).hexdigest() == binary_hash
    (tmp_path / "native-integration-receipt.json").write_text(json.dumps({"status": "PASS", "producer_executable": str(binary), "producer_sha256": binary_hash, "input_sha256": hashlib.sha256(input_path.read_bytes()).hexdigest(), "canonical_content_hash": digest, "expected_missing_cells": 3, "expected_n_cells": 24, "raw_nan_cells": 2, "finite_masked_cells": 1, "engine_version": assessment["engine_version"], "protocol_version": assessment["protocol_version"], "native_report_lossless": True, "legacy_card_unchanged": True, "canonical_content_unchanged": True, "legacy_kernels_forbidden": True, "commands": receipts}, indent=2))
