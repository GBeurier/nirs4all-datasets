"""Tests for :class:`nirs4all_datasets.dataset.NirsDataset` (schema 2.0, real canonical data)."""

from __future__ import annotations

from typing import Any

import numpy as np
import pytest

from nirs4all_datasets.dataset import NirsDataset
from nirs4all_datasets.schema import Tier, Variable, VariableRole


def test_sources_lists_block_ids_in_order(canonical_dataset: Any) -> None:
    dataset_dir, desc = canonical_dataset("corn", blocks=("X1", "X2", "X3"), sample_of={"o1": "s1", "o2": "s2"})
    ds = NirsDataset(dataset_dir, desc)
    assert ds.sources() == ["X1", "X2", "X3"]
    assert ds.id == "corn"


def test_x_single_source_drops_id_columns(canonical_dataset: Any) -> None:
    # The leaf has 2 observations and 2 wavelength columns (1100, 1102) per block.
    dataset_dir, desc = canonical_dataset("corn", blocks=("X1", "X2"), sample_of={"o1": "s1", "o2": "s2"})
    ds = NirsDataset(dataset_dir, desc)
    x1 = ds.x("X1")
    assert isinstance(x1, np.ndarray)
    assert x1.ndim == 2
    assert x1.shape == (2, 2)  # rows = observations, cols = wavelengths (observation_id/sample_id dropped)
    assert x1.dtype == np.float32
    assert ds.wavelengths("X1").tolist() == [1100.0, 1102.0]


def test_x_concat_false_returns_dict_of_arrays(canonical_dataset: Any) -> None:
    dataset_dir, desc = canonical_dataset("corn", blocks=("X1", "X2", "X3"), sample_of={"o1": "s1", "o2": "s2"})
    ds = NirsDataset(dataset_dir, desc)
    out = ds.x(concat=False)
    assert isinstance(out, dict)
    assert set(out) == {"X1", "X2", "X3"}
    for sid, arr in out.items():
        assert isinstance(arr, np.ndarray)
        assert arr.shape == (2, 2)


def test_x_multi_sample_aligned_sources_raises_actionable_error(canonical_dataset: Any) -> None:
    # 3 sample-aligned sources cannot be safely row-concatenated; x() must refuse and guide the user.
    dataset_dir, desc = canonical_dataset("corn", blocks=("X1", "X2", "X3"), sample_of={"o1": "s1", "o2": "s2"})
    ds = NirsDataset(dataset_dir, desc)
    with pytest.raises(ValueError) as excinfo:
        ds.x()
    message = str(excinfo.value)
    assert "source=" in message
    assert "concat=False" in message


def test_x_single_observation_aligned_source_returns_2d_array(canonical_dataset: Any) -> None:
    # A single observation-aligned source (no sample_id mapping) -> x() yields one 2D array.
    dataset_dir, desc = canonical_dataset("mono", blocks=("X",), sample_of=None)
    ds = NirsDataset(dataset_dir, desc)
    x = ds.x()
    assert isinstance(x, np.ndarray)
    assert x.ndim == 2
    assert x.shape == (2, 2)


def test_y_returns_targets_keyed_by_sample(canonical_dataset: Any) -> None:
    dataset_dir, desc = canonical_dataset("corn", blocks=("X1",), sample_of={"o1": "s1", "o2": "s2"}, targets={"Moisture": "numeric", "variety": "categorical"})
    ds = NirsDataset(dataset_dir, desc)
    y = ds.y()
    assert y is not None
    assert "sample_id" in y.columns
    assert {"Moisture", "variety"} <= set(y.columns)
    assert sorted(y["sample_id"].astype(str)) == ["s1", "s2"]

    one = ds.y("Moisture")
    assert one is not None
    assert list(one.columns) == ["sample_id", "Moisture"]


def test_metadata_returns_only_metadata_role_columns(canonical_dataset: Any) -> None:
    dataset_dir, desc = canonical_dataset("corn", blocks=("X1",), sample_of={"o1": "s1", "o2": "s2"}, extra_meta=("site",))
    ds = NirsDataset(dataset_dir, desc)
    meta_names = {v.name for v in desc.variables if v.role is VariableRole.METADATA}
    assert "site" in meta_names

    meta = ds.metadata()
    assert meta is not None
    assert "sample_id" in meta.columns
    # only role==metadata columns are exposed, never the targets.
    target_names = {v.name for v in desc.variables if v.role is VariableRole.TARGET}
    assert set(meta.columns) - {"sample_id"} <= meta_names
    assert not (set(meta.columns) & target_names)


def test_split_returns_labels_when_native_split_exists(canonical_dataset: Any) -> None:
    dataset_dir, desc = canonical_dataset("mono", blocks=("X",), sample_of=None, split={"o1": "cal", "o2": "val"})
    ds = NirsDataset(dataset_dir, desc)
    split = ds.split("original")
    assert split is not None
    assert "partition" in split.columns
    assert sorted(split["partition"].astype(str)) == ["cal", "val"]


def test_split_absent_returns_none(canonical_dataset: Any) -> None:
    dataset_dir, desc = canonical_dataset("mono", blocks=("X",), sample_of=None)
    ds = NirsDataset(dataset_dir, desc)
    assert ds.split("original") is None
    assert ds.split("does_not_exist") is None


def test_tier_and_variables_and_card(canonical_dataset: Any) -> None:
    dataset_dir, desc = canonical_dataset("mono", blocks=("X",), sample_of=None)
    ds = NirsDataset(dataset_dir, desc)
    assert ds.tier is Tier.PRIVATE  # synthetic non-public leaf -> private tier
    variables = ds.variables()
    assert variables and all(isinstance(v, Variable) for v in variables)
    assert ds.card() is None  # no card.json built by the canonical_dataset fixture


def test_public_leaf_has_public_tier(canonical_dataset: Any) -> None:
    dataset_dir, desc = canonical_dataset("pub", blocks=("X",), sample_of=None, public=True)
    ds = NirsDataset(dataset_dir, desc)
    assert ds.tier is Tier.PUBLIC


def test_observation_and_sample_ids(canonical_dataset: Any) -> None:
    dataset_dir, desc = canonical_dataset("corn", blocks=("X1",), sample_of={"o1": "s1", "o2": "s2"})
    ds = NirsDataset(dataset_dir, desc)
    assert ds.observation_ids("X1").tolist() == ["o1", "o2"]
    assert sorted(ds.sample_ids().tolist()) == ["s1", "s2"]


def test_to_nirs4all_builds_a_spectrodataset(canonical_dataset: Any) -> None:
    pytest.importorskip("nirs4all")  # the nirs4all constructor is environment-dependent
    dataset_dir, desc = canonical_dataset("mono", blocks=("X",), sample_of=None)
    ds = NirsDataset(dataset_dir, desc)
    spectro = ds.to_nirs4all()
    assert spectro is not None
    assert spectro.num_samples == 2


def test_to_io_spec_exposes_canonical_parquet_bridge(canonical_dataset: Any) -> None:
    dataset_dir, desc = canonical_dataset(
        "bridge",
        blocks=("X",),
        sample_of={"o1": "s1", "o2": "s2"},
        targets={"Moisture": "numeric"},
        extra_meta=("site",),
        split={"o1": "cal", "o2": "val"},
    )
    ds = NirsDataset(dataset_dir, desc)

    spec = ds.to_io_spec()

    assert spec["name"] == "bridge"
    assert spec["sample_index"] == {"by": "id", "key": "sample_id", "observation_id": "observation_id"}
    by_id = {source["id"]: source for source in spec["sources"]}
    assert set(by_id) == {"X", "variables", "split_original"}
    assert by_id["X"]["input"].endswith("canonical/sources/X.parquet")
    assert by_id["X"]["columns"] == [
        {"role": "ignore", "select": ["observation_id", "sample_id"]},
        {"role": "features", "select": ["1100", "1102"]},
    ]
    assert by_id["variables"]["join"] == {"to": "X", "on": "sample_id", "how": "m:1", "coverage": "warn"}
    assert {"role": "targets", "select": ["Moisture"]} in by_id["variables"]["columns"]
    assert {"role": "metadata", "select": ["site"]} in by_id["variables"]["columns"]
    assert by_id["split_original"]["columns"] == [{"role": "metadata", "select": ["partition"]}]


def test_to_dataset_package_delegates_to_nirs4all_io(canonical_dataset: Any) -> None:
    pytest.importorskip("nirs4all_io")
    dataset_dir, desc = canonical_dataset(
        "bridge_pkg",
        blocks=("X",),
        sample_of={"o1": "s1", "o2": "s2"},
        targets={"Moisture": "numeric"},
        extra_meta=("site",),
    )
    ds = NirsDataset(dataset_dir, desc)

    package = ds.to_dataset_package()

    assert package.name == "bridge_pkg"
    block = package.to_assembled().blocks["train"]
    np.testing.assert_allclose(block.X[0], [[0.1, 0.2], [0.1, 0.2]], rtol=1e-6)
    np.testing.assert_allclose(block.y, [[1.0], [1.5]], rtol=1e-6)
    assert "site" in block.metadata.columns


def test_to_io_spec_refuses_ambiguous_multisource_repetitions(canonical_dataset: Any) -> None:
    dataset_dir, desc = canonical_dataset(
        "asym",
        blocks=("X1", "X2"),
        block_obs={"X1": ["o1", "o2", "o3"], "X2": ["p1", "p2"]},
        sample_of={"o1": "s1", "o2": "s1", "o3": "s2", "p1": "s1", "p2": "s2"},
    )
    ds = NirsDataset(dataset_dir, desc)

    with pytest.raises(ValueError, match="many-to-many join"):
        ds.to_io_spec()

    one = ds.to_io_spec(source="X1")
    assert [source["id"] for source in one["sources"] if source["id"].startswith("X")] == ["X1"]
