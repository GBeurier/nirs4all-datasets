"""Regression coverage for descriptor-driven curation cache identity."""
from __future__ import annotations

import pandas as pd
import pytest
from conftest import make_v2_leaf

from nirs4all_datasets.bootstrap import build_descriptor_from_card
from nirs4all_datasets.manifest import processing_hash
from nirs4all_datasets.organize import organize
from nirs4all_datasets.schema import Variable


def _with_variable(descriptor, **kwargs):
    return descriptor.model_copy(update={"variables": [Variable(name="protein", **kwargs)]})


def test_type_change_rebuilds_canonical_data(tmp_path):
    leaf = make_v2_leaf(tmp_path / "sample", targets={"protein": [1, 2]})
    descriptor, _ = build_descriptor_from_card(leaf)
    numeric = _with_variable(descriptor, role="target", type="numeric")
    categorical = _with_variable(descriptor, role="target", type="categorical")
    result = organize(leaf, numeric, tmp_path / "datasets")
    assert organize(leaf, numeric, tmp_path / "datasets").skipped
    numeric_values = pd.read_parquet(result.dataset_dir / "canonical/variables.parquet")["protein"]
    rebuilt = organize(leaf, categorical, tmp_path / "datasets")
    assert not rebuilt.skipped
    categorical_values = pd.read_parquet(result.dataset_dir / "canonical/variables.parquet")["protein"]
    assert pd.api.types.is_numeric_dtype(numeric_values.dtype)
    assert not pd.api.types.is_numeric_dtype(categorical_values.dtype)


@pytest.mark.parametrize("change", [
    {"role": "target"}, {"type": "categorical"}, {"semantic_role": "identifier"},
    {"equivalent_to": "other"}, {"derived_from": ["other"]}, {"original_name": "old"},
    {"missing_values": ["missing"]}, {"numeric_sentinels": [-999]},
    {"decimal_separator": "."}, {"thousands_separator": "."}, {"unit": "mg"},
])
def test_curation_directives_change_identity(tmp_path, change):
    leaf = make_v2_leaf(tmp_path / "sample", targets={"protein": [1, 2]})
    descriptor, _ = build_descriptor_from_card(leaf)
    assert processing_hash(_with_variable(descriptor)) != processing_hash(_with_variable(descriptor, **change))


def test_descriptive_dataset_edits_do_not_change_identity(tmp_path):
    leaf = make_v2_leaf(tmp_path / "sample", targets={"protein": [1, 2]})
    descriptor, _ = build_descriptor_from_card(leaf)
    descriptor = _with_variable(descriptor)
    assert processing_hash(descriptor) == processing_hash(descriptor.model_copy(update={"description": "New description"}))


def test_descriptor_roundtrip_preserves_source_overrides(tmp_path):
    import json

    import yaml

    from nirs4all_datasets.curation import curate_bundle
    from nirs4all_datasets.schema import DatasetDescriptor

    leaf = make_v2_leaf(tmp_path / "sample", targets={"protein": [1, 2]})
    descriptor, _ = build_descriptor_from_card(leaf)
    (leaf / "M.csv").write_text("observation_id;dose\na;1,000\nb;2,000\n", encoding="utf-8")
    (leaf / "datapackage.json").write_text(json.dumps({"resources": [{"path": "M.csv", "schema": {"fields": [
        {"name": "dose", "type": "number", "decimalChar": ".", "groupChar": ","},
    ]}}]}), encoding="utf-8")
    implicit = descriptor.model_copy(update={"variables": [Variable(name="dose")]})
    explicit = descriptor.model_copy(update={"variables": [Variable(name="dose", type="numeric", decimal_separator=",", thousands_separator=None, missing_values=[], numeric_sentinels=[])]})
    for original, expected in [(implicit, [1000., 2000.]), (explicit, [1., 2.])]:
        dumped = yaml.safe_load(yaml.safe_dump(original.model_dump(mode="json")))
        restored = DatasetDescriptor.model_validate(dumped)
        assert processing_hash(original) == processing_hash(restored)
        assert original.variables[0].model_fields_set & {"type", "decimal_separator", "thousands_separator", "missing_values", "numeric_sentinels"} == restored.variables[0].model_fields_set & {"type", "decimal_separator", "thousands_separator", "missing_values", "numeric_sentinels"}
        assert curate_bundle(leaf, "synthetic", variable_specs=restored.variables).metadata.dose.dropna().tolist() == expected
    assert processing_hash(implicit) != processing_hash(explicit)
