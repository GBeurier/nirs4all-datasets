"""Keep declared variable contracts consistent across canonical and curated accessors."""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import pytest
from conftest import make_v2_leaf

from nirs4all_datasets.bootstrap import build_descriptor_from_card
from nirs4all_datasets.canonical import build_canonical
from nirs4all_datasets.curation import consumer_views
from nirs4all_datasets.schema import Variable


def test_declared_missing_tokens_sentinels_and_name_apply_to_both_views(tmp_path: Path) -> None:
    leaf = make_v2_leaf(tmp_path / "contract", targets={"Original concentration": "numeric"}, block_obs={"X": [f"o{i}" for i in range(5)]})
    target = pd.read_csv(leaf / "Y.csv", sep=";")
    target["Original concentration"] = ["-999", "ND", "1.5", "2.5", "3.5"]
    target.to_csv(leaf / "Y.csv", sep=";", index=False)
    descriptor, _ = build_descriptor_from_card(leaf)
    descriptor.variables = [Variable(name="Assay concentration", original_name="Original concentration", type="numeric", role="target", decimal_separator=".", missing_values=["ND"], numeric_sentinels=[-999])]
    out = tmp_path / "out"
    build_canonical(leaf, descriptor, out)
    canonical = pd.read_parquet(out / "canonical/variables.parquet")
    curated = pd.read_parquet(out / "canonical/curation/Y.parquet")
    assert canonical["Assay concentration"].isna().tolist() == [True, True, False, False, False]
    pd.testing.assert_series_equal(canonical["Assay concentration"], curated["Assay concentration"], check_dtype=False)
    original = pd.read_parquet(out / "canonical/curation/original_Y.parquet")
    assert original["Original concentration"].tolist() == ["-999", "ND", "1.5", "2.5", "3.5"]
    report = json.loads((out / "canonical/curation/mapping.json").read_text())
    field = next(row for row in report["mapping"] if row["original_name"] == "Original concentration")
    assert field["canonical_name"] == "Assay concentration"
    assert field["stats"]["n_missing"] == 2
    assert field["stats"]["min"] == 1.5


@pytest.mark.parametrize("reverse", [False, True])
def test_target_descendants_are_excluded_independently_of_descriptor_order(tmp_path: Path, reverse: bool) -> None:
    leaf = make_v2_leaf(tmp_path / "dependencies", targets={"response": "numeric"})
    descriptor, _ = build_descriptor_from_card(leaf)
    variables = [
        Variable(name="first", derived_from=["response"]),
        Variable(name="second", derived_from=["first"]),
        Variable(name="third", equivalent_to="second"),
        Variable(name="unrelated", derived_from=["instrument_temperature"]),
    ]
    descriptor.variables.extend(reversed(variables) if reverse else variables)
    frame = pd.DataFrame({"sample_id": ["s1", "s2"], "response": [1, 2], "first": [2, 4], "second": [3, 5], "third": [3, 5], "unrelated": [20, 21]})
    views = consumer_views(frame, descriptor)
    assert list(views["M"]) == ["sample_id", "unrelated"]
    excluded = {row["name"] for row in views["decisions"] if row["reason"] == "target_copy_or_declared_derivation"}
    assert excluded == {"first", "second", "third"}
    pd.testing.assert_frame_equal(views["original"], frame)


def test_static_curated_metadata_also_excludes_indirect_target_derivations(tmp_path: Path) -> None:
    leaf = make_v2_leaf(tmp_path / "derived", targets={"response": "numeric"}, extra_meta=["first", "second", "temperature"])
    metadata = pd.read_csv(leaf / "M.csv", sep=";")
    metadata["first"], metadata["second"], metadata["temperature"] = [2, 4], [3, 5], [20, 21]
    metadata.to_csv(leaf / "M.csv", sep=";", index=False)
    descriptor, _ = build_descriptor_from_card(leaf)
    for variable in descriptor.variables:
        if variable.name == "first":
            variable.derived_from = ["response"]
        elif variable.name == "second":
            variable.derived_from = ["first"]
    out = tmp_path / "out"
    build_canonical(leaf, descriptor, out)
    columns = pd.read_parquet(out / "canonical/curation/M.parquet").columns
    assert "first" not in columns and "second" not in columns
    assert "temperature" in columns


def test_dependency_cycles_terminate_without_excluding_unrelated_columns(tmp_path: Path) -> None:
    leaf = make_v2_leaf(tmp_path / "cycles", targets={"response": "numeric"})
    descriptor, _ = build_descriptor_from_card(leaf)
    descriptor.variables.extend([Variable(name="a", derived_from=["b"]), Variable(name="b", derived_from=["a"])])
    frame = pd.DataFrame({"response": [1, 2], "a": [3, 4], "b": [5, 6]})
    assert list(consumer_views(frame, descriptor)["M"]) == ["a", "b"]


def test_equivalent_response_is_excluded_when_declared_from_the_target_side(tmp_path: Path) -> None:
    leaf = make_v2_leaf(tmp_path / "equivalent", targets={"response": "numeric"})
    descriptor, _ = build_descriptor_from_card(leaf)
    descriptor.variables[0].equivalent_to = "raw_code"
    descriptor.variables.extend([Variable(name="raw_code"), Variable(name="encoded", derived_from=["raw_code"])])
    frame = pd.DataFrame({"response": [1, 2], "raw_code": [1, 2], "encoded": [10, 20]})
    views = consumer_views(frame, descriptor)
    assert list(views["M"]) == []


def test_homonymous_original_metadata_does_not_rename_or_taint_target(tmp_path: Path) -> None:
    leaf = make_v2_leaf(tmp_path / "homonyms", targets={"treatment": "categorical"}, extra_meta=["treatment"])
    (leaf / "Y.csv").write_text("observation_id;treatment\no1;0\no2;1\n")
    metadata = pd.read_csv(leaf / "M.csv", sep=";")
    metadata["treatment"] = ["control", "treated"]
    metadata.to_csv(leaf / "M.csv", sep=";", index=False)
    descriptor, _ = build_descriptor_from_card(leaf)
    for variable in descriptor.variables:
        if variable.name == "metadata_treatment":
            variable.original_name = "treatment"
    out = tmp_path / "out"
    build_canonical(leaf, descriptor, out)
    target = pd.read_parquet(out / "canonical/curation/Y.parquet")
    context = pd.read_parquet(out / "canonical/curation/M.parquet")
    assert target["treatment"].tolist() == ["0", "1"]
    assert context["metadata_treatment"].tolist() == ["control", "treated"]
