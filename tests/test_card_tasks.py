"""Task inference uses individual targets and exact legacy cardinality evidence."""
from __future__ import annotations

import copy
import json
from pathlib import Path

import pandas as pd
import pytest

from nirs4all_datasets.card_tasks import card_task_kinds, project_card_tasks
from nirs4all_datasets.catalog import catalog_entry
from nirs4all_datasets.qualify.anonymize import anonymize_card
from nirs4all_datasets.qualify.profile import _variable_section, build_card
from nirs4all_datasets.schema import Variable
from nirs4all_datasets.site.model import _dataset_view
from nirs4all_datasets.site.pages import _variable_card


def test_many_mixed_targets_in_real_card(canonical_dataset, tmp_path: Path) -> None:
    pytest.importorskip("nirs4all_io.infer.detectors")
    targets = {**{f"trait_{i}": "numeric" for i in range(12)}, "continuous": "numeric", "category": "categorical"}
    dataset_dir, descriptor = canonical_dataset("mixed_targets", targets=targets)
    path = dataset_dir / "canonical" / "variables.parquet"
    frame = pd.read_parquet(path)
    # Exercise a rare positive while keeping many independently inferred targets.
    frame = pd.concat([frame.iloc[[0]]] * 19 + [frame.iloc[[1]]], ignore_index=True)
    frame["sample_id"] = [f"s{i}" for i in range(len(frame))]
    for i in range(12):
        frame[f"trait_{i}"] = [0] * 19 + [1]
    frame["continuous"] = [i / 19 for i in range(20)]
    frame["category"] = ["a", "b"] * 10
    frame.to_parquet(path, index=False)
    card = build_card(dataset_dir, descriptor, compute_assets=False, compute_pca=False)
    variables = {v["name"]: v for v in card["variables"]}
    assert all(variables[f"trait_{i}"]["task_type"] == "classification" for i in range(12))
    assert variables["trait_0"]["class_stats"]["top_classes"] == [{"name": "0", "count": 19}, {"name": "1", "count": 1}]
    assert "task_type" not in variables["continuous"]
    assert variables["category"]["type"] == "categorical"
    assert card_task_kinds(card, list(targets)) == {"classification", "regression"}
    (dataset_dir / "card.json").write_text(json.dumps(card), encoding="utf-8")
    assert catalog_entry(dataset_dir.parent.parent, descriptor)["task"] == "classification+regression"
    redacted = anonymize_card(card)
    assert all("class_stats" not in v for v in redacted["variables"] if v["type"] == "numeric")


def test_existing_many_target_card_and_ambiguous_evidence() -> None:
    root = Path(__file__).resolve().parents[1]
    dataset_id = "dryad_grassland_hyspex_species_manual"
    original = json.loads((root / "datasets" / dataset_id / "card.json").read_text(encoding="utf-8"))
    projected = project_card_tasks(original)
    variables = [v for v in projected["variables"] if v["role"] == "target"]
    assert len(variables) == 100
    assert all(v.get("task_type") == "classification" for v in variables)
    assert variables[0]["class_stats"]["top_classes"] == [{"name": "1", "count": 81}, {"name": "0", "count": 23}]
    for variable in variables:
        class_counts = [item["count"] for item in variable["class_stats"]["top_classes"]]
        assert class_counts == sorted(class_counts, reverse=True)
    assert "task_type" not in original["variables"][0]
    unavailable = copy.deepcopy(original)
    unavailable["variables"][0]["task_type"] = "unavailable"
    assert project_card_tasks(unavailable)["variables"][0]["task_type"] == "classification"
    entry = {"id": dataset_id, "tier": "public", "has_card": True, "targets": [v["name"] for v in variables], "task": "regression"}
    view = _dataset_view(root, entry)
    assert view.entry["task"] == "classification"
    html = _variable_card(view, view.card["variables"][0])
    assert "classification" in html and "Classes" in html
    top_class_row = html.split("Top class", 1)[1].split("</tr>", 1)[0]
    assert "<td>1 (81)</td>" in top_class_row

    uncertain = copy.deepcopy(original)
    uncertain["curation"]["variables"] = []
    assert "task_type" not in project_card_tasks(uncertain)["variables"][0]
    uncertain = copy.deepcopy(original)
    matching = next(v for v in uncertain["curation"]["variables"] if any(s.get("name") == original["variables"][0]["name"] for s in v.get("source_columns", [])))
    matching["stats"]["n_unique"] = 3
    assert "task_type" not in project_card_tasks(uncertain)["variables"][0]
    matching["stats"]["n_unique"] = 2
    uncertain["curation"]["variables"].append(copy.deepcopy(matching))
    assert "task_type" not in project_card_tasks(uncertain)["variables"][0]


def test_small_numeric_samples_and_optional_detector(monkeypatch) -> None:
    import builtins

    variable = Variable(name="measurement", role="target", type="numeric")
    for values in ([0.0, 0.5, 1.0], [1, 2, 1], [0, 1]):
        assert "task_type" not in _variable_section(variable, pd.Series(values), [])
    assert "task_type" not in _variable_section(Variable(name="context", role="metadata", type="numeric"), pd.Series([0, 0, 1]), [])
    original_import = builtins.__import__

    def without_io(name, *args, **kwargs):
        if name == "nirs4all_io.infer.detectors":
            raise ImportError("optional IO unavailable")
        return original_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", without_io)
    warnings: list[str] = []
    section = _variable_section(variable, pd.Series([0, 0, 1]), warnings)
    assert section["task_type"] == "unavailable"
    assert section["type"] == "numeric"
    assert card_task_kinds({"variables": [section]}, [variable.name]) == set()
    assert any("task inference unavailable" in message for message in warnings)
    continuous = _variable_section(variable, pd.Series([0.0, 0.5, 1.0]), [])
    assert card_task_kinds({"variables": [continuous]}, [variable.name]) == {"regression"}


def test_unavailable_task_is_not_presented_as_regression(monkeypatch, canonical_dataset) -> None:
    import builtins

    dataset_dir, descriptor = canonical_dataset("binary_without_io", targets={"presence": "numeric"})
    path = dataset_dir / "canonical" / "variables.parquet"
    frame = pd.read_parquet(path).iloc[[0, 0, 1]].reset_index(drop=True)
    frame["sample_id"] = ["s0", "s1", "s2"]
    frame["presence"] = [0, 0, 1]
    frame.to_parquet(path, index=False)
    original_import = builtins.__import__

    def without_io(name, *args, **kwargs):
        if name == "nirs4all_io.infer.detectors":
            raise ImportError("optional IO unavailable")
        return original_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", without_io)
    card = build_card(dataset_dir, descriptor, compute_assets=False, compute_pca=False)
    (dataset_dir / "card.json").write_text(json.dumps(card), encoding="utf-8")
    entry = catalog_entry(dataset_dir.parent.parent, descriptor)
    assert entry["task"] is None
    # Loading a saved legacy index must also discard its obsolete regression label.
    view = _dataset_view(dataset_dir.parent.parent, {**entry, "task": "regression"})
    assert view.entry["task"] is None
    html = _variable_card(view, view.card["variables"][0])
    assert "Task inference is unavailable" in html
    assert "numeric storage does not establish a regression task" in html
    assert "Requalify with nirs4all-io installed" in html

    redacted = anonymize_card(card)
    (dataset_dir / "card.json").write_text(json.dumps(redacted), encoding="utf-8")
    anon_entry = {**entry, "tier": "anonymized", "targets": [v["name"] for v in redacted["variables"]], "task": "regression"}
    anon_view = _dataset_view(dataset_dir.parent.parent, anon_entry)
    assert anon_view.entry["task"] is None
    assert "Task inference is unavailable" in _variable_card(anon_view, anon_view.card["variables"][0])
