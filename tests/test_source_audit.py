"""Source inventory does not expose table values or execute source scripts."""
from __future__ import annotations

import json
import runpy
from pathlib import Path


def test_source_inventory(tmp_path):
    audit = runpy.run_path(str(Path(__file__).resolve().parents[1] / "catalog/scripts/source_audit.py"))["audit"]
    leaf = tmp_path / "v2.0" / "Example"
    leaf.mkdir(parents=True)
    (leaf / "dataset_card.json").write_text(json.dumps({"dataset_id": "Example_ID"}))
    (leaf / "source_to_standard.py").write_text('raise RuntimeError("must not execute")\n# convert_absent.py\n')
    (leaf / "X.csv").write_text("observation_id;1100\nsecret-sample;1.5\n")
    report = audit(tmp_path, set(), baseline="revision")
    assert report["summary"]["datasets"] == 1
    assert report["summary"]["with_missing_shared_converters"] == 1
    entry = report["datasets"][0]
    assert entry["id"] == "example_id"
    assert entry["missing_shared_converters"] == ["convert_absent.py"]
    assert entry["standardized_tables"][0]["layout"]["column_count"] == 2
    assert "secret-sample" not in json.dumps(report)
    assert str(tmp_path) not in json.dumps(report)
