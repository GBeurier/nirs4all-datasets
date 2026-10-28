"""Local standardized bundle import preserves the canonical data contract."""
from __future__ import annotations

import json

import pandas as pd
import pytest

from nirs4all_datasets.reproduce import import_standardized


def test_import_standardized_bundle(tmp_path, descriptor):
    leaf = tmp_path / "bundle"
    leaf.mkdir()
    (leaf / "dataset_card.json").write_text(json.dumps({"dataset_id": descriptor.id}))
    (leaf / "X1.csv").write_text("observation_id;1100;1200\no1;0.1;0.2\no2;0.3;0.4\n")
    (leaf / "Y.csv").write_text("observation_id;protein\no1;5\no2;6\n")
    (leaf / "M.csv").write_text("observation_id;sample_id;split_original;site\no1;s1;train;A\no2;s2;test;B\n")
    out = tmp_path / "output"
    result = import_standardized(leaf, descriptor, out)
    assert result.canonical_dir == out / "canonical"
    x = pd.read_parquet(out / "canonical/sources/X1.parquet")
    assert x["sample_id"].tolist() == ["s1", "s2"]
    variables = pd.read_parquet(out / "canonical/variables.parquet")
    assert variables["protein"].tolist() == [5, 6]
    assert variables["site"].tolist() == ["A", "B"]
    split = pd.read_parquet(out / "canonical/splits/original.parquet")
    assert split["partition"].tolist() == ["train", "test"]
    with pytest.raises(FileExistsError):
        import_standardized(leaf, descriptor, out)


def test_import_rejects_wrong_or_unusable_bundle_without_publishing(tmp_path, descriptor):
    leaf = tmp_path / "bundle"
    leaf.mkdir()
    card = leaf / "dataset_card.json"
    card.write_text(json.dumps({"dataset_id": "wrong"}))
    with pytest.raises(ValueError, match="dataset_id"):
        import_standardized(leaf, descriptor, tmp_path / "out")
    card.write_text(json.dumps({"dataset_id": descriptor.id}))
    with pytest.raises(ValueError, match="could not be imported"):
        import_standardized(leaf, descriptor, tmp_path / "out")
    assert not (tmp_path / "out/canonical").exists()


def test_import_keeps_asymmetric_sources_separate(tmp_path, descriptor):
    leaf = tmp_path / "bundle"
    leaf.mkdir()
    (leaf / "dataset_card.json").write_text(json.dumps({"dataset_id": descriptor.id}))
    (leaf / "X1.csv").write_text("observation_id;1100\no1;0.1\no2;0.2\n")
    (leaf / "X2.csv").write_text("observation_id;1500\no3;0.3\n")
    (leaf / "M.csv").write_text("observation_id;sample_id\no1;s1\no2;s2\no3;s1\n")
    result = import_standardized(leaf, descriptor, tmp_path / "out")
    x1 = pd.read_parquet(result.canonical_dir / "sources/X1.parquet")
    x2 = pd.read_parquet(result.canonical_dir / "sources/X2.parquet")
    assert x1["sample_id"].tolist() == ["s1", "s2"]
    assert x2["sample_id"].tolist() == ["s1"]
    assert any("declared sources" in warning for warning in result.warnings)


def test_cli_import_standardized_normalizes_bundle_id(tmp_path, descriptor, monkeypatch):
    from typer.testing import CliRunner

    from nirs4all_datasets import cli

    leaf = tmp_path / "bundle"
    leaf.mkdir()
    (leaf / "dataset_card.json").write_text(json.dumps({"dataset_id": descriptor.id.upper()}))
    (leaf / "X1.csv").write_text("observation_id;1100\no1;0.1\n")
    monkeypatch.setattr(cli, "_descriptor", lambda root, dataset_id: descriptor)
    out = tmp_path / "output"
    result = CliRunner().invoke(cli.app, ["import-standardized", str(leaf), descriptor.id, "--out", str(out)])
    assert result.exit_code == 0, result.output
    assert (out / "canonical/dataset.json").is_file()
    assert "import-standardized:" in result.output
