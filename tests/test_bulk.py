"""Bulk conversion outcomes survive qualification and incremental runs."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from nirs4all_datasets.bootstrap import build_descriptor_from_card
from nirs4all_datasets.bulk import process_one


def _registry(tmp_path: Path, v2_leaf: Any) -> tuple[Path, Path]:
    root = tmp_path / "registry"
    source = tmp_path / "source"
    leaf = v2_leaf(source / "v2.0" / "demo", sample_of={"o1": "s1", "o2": "s2"})
    descriptor, _ = build_descriptor_from_card(leaf)
    path = root / "catalog" / "datasets" / "demo.yaml"
    path.parent.mkdir(parents=True)
    path.write_text(yaml.safe_dump(descriptor.model_dump(mode="json")), encoding="utf-8")
    return root, leaf


def test_conversion_warnings_survive_fresh_and_incremental_bulk(tmp_path: Path, v2_leaf: Any) -> None:
    root, leaf = _registry(tmp_path, v2_leaf)
    # An unjoinable target file is intentionally skipped by canonical conversion.
    (leaf / "Y.csv").write_text("wrong;Moisture\n1;3\n", encoding="utf-8")
    for i in range(1, 9):
        (leaf / f"X{i}.csv").write_text("wrong;1100\n1;0.1\n", encoding="utf-8")
    first = process_one(str(root), str(leaf.parent.parent), "demo", skip_assets=True, force=False)
    assert first["status"] == "partial"
    assert any("skipping targets" in warning for warning in first["warnings"])
    assert len(first["warnings"]) > 6
    card = json.loads((root / "datasets/demo/card.json").read_text())
    assert any("skipping targets" in warning for warning in card["warnings"])
    manifest = json.loads((root / "datasets/demo/manifest.json").read_text())
    assert manifest["conversion_status"] == "partial"
    assert any("skipping targets" in warning for warning in manifest["conversion_warnings"])
    second = process_one(str(root), str(leaf.parent.parent), "demo", skip_assets=True, force=False)
    assert second["status"] == "partial"
    assert any("skipping targets" in warning for warning in second["warnings"])
    assert second["warnings"] == first["warnings"]


def test_failed_conversion_never_reported_success_even_on_rerun(tmp_path: Path, v2_leaf: Any) -> None:
    root, leaf = _registry(tmp_path, v2_leaf)
    (leaf / "X.csv").write_text("bad;1100\n1;0.1\n", encoding="utf-8")
    for _ in range(2):
        result = process_one(str(root), str(leaf.parent.parent), "demo", skip_assets=True, force=False)
        assert result["status"] == "failed"
        assert any("nothing converted" in warning for warning in result["warnings"])
