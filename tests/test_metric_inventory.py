"""Every local diagnostic has an explicit scientific definition and migration owner."""
from __future__ import annotations

import ast
import runpy
from pathlib import Path

from nirs4all_datasets.qualify import registry


def test_inventory_is_current_and_covers_every_public_metric_implementation():
    root = Path(__file__).resolve().parents[1]
    generator = runpy.run_path(str(root / "scripts/generate_metric_inventory.py"))
    inventory = registry.migration_inventory()
    assert inventory == generator["generate"]()
    keys = [row["metric_id"] for row in inventory["metrics"]]
    assert len(keys) == len(set(keys))
    assert {row["transition"] for row in inventory["metrics"]} == set(inventory["actions"])
    assert all(row["scientific_definition"] and row["target_owner"] for row in inventory["metrics"])
    source = root / "src/nirs4all_datasets/qualify/metrics.py"
    public_functions = {node.name for node in ast.parse(source.read_text()).body if isinstance(node, ast.FunctionDef) and not node.name.startswith("_")}
    inventoried = {item["symbol"] for item in inventory["definitions"].values()}
    assert public_functions <= inventoried | inventory["non_metric_public_helpers"].keys()
    assert all(item["implementation_sha256"] and item["local_helper_implementations"] for key, item in inventory["definitions"].items() if not key.startswith("native."))
    assert "native.preflight.integrity.missing_cells" in inventory["definitions"]


def test_false_lof_and_snr_names_are_only_explicit_compatibility_aliases():
    rows = {row["metric_id"]: row for row in registry.migration_inventory()["metrics"]}
    assert rows["structure.local_outlier_factor_p95"]["transition"] == "deprecated"
    assert rows["structure.local_outlier_factor_p95"]["replaced_by"] == "structure.knn_distance_ratio_p95"
    assert rows["noise.snr"]["replaced_by"] == "noise.roughness_signal_to_noise_proxy"
    assert rows["noise.roughness_signal_to_noise_proxy"]["native_equivalence"] == "not_assumed"
    assert rows["target_shift.wasserstein"]["scope"] == "task/split"
    assert rows["target_shift.wasserstein"]["target_owner"] == "Domains"
