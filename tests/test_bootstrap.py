"""Tests for descriptor authoring from v2.0 dataset_card.json (schema 2.0)."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from nirs4all_datasets.bootstrap import bootstrap, build_descriptor_from_card, find_v2_leaves
from nirs4all_datasets.schema import AlignmentLevel, Tier, VariableRole, VarType


def test_descriptor_is_valid_and_multi_source(tmp_path: Path, v2_leaf: Any) -> None:
    leaf = v2_leaf(tmp_path / "corn", blocks=("X1", "X2", "X3"), sample_of={"o1": "s1", "o2": "s2"})
    desc, warns = build_descriptor_from_card(leaf)
    assert [s.source_id for s in desc.sources] == ["X1", "X2", "X3"]
    assert desc.alignment_level is AlignmentLevel.SAMPLE
    assert desc.ids.sample_id_available is True
    assert warns == []


def test_variable_roles_and_types(tmp_path: Path, v2_leaf: Any) -> None:
    leaf = v2_leaf(
        tmp_path / "ds",
        targets={"Moisture": "numeric", "variety": "categorical"},
        extra_meta=("region",),
        sample_of={"o1": "s1", "o2": "s2"},
    )
    desc, _ = build_descriptor_from_card(leaf)
    by_name = {v.name: v for v in desc.variables}
    assert by_name["Moisture"].role is VariableRole.TARGET and by_name["Moisture"].type is VarType.NUMERIC
    assert by_name["variety"].role is VariableRole.TARGET and by_name["variety"].type is VarType.CATEGORICAL  # name heuristic
    assert by_name["region"].role is VariableRole.METADATA  # m_field, not a target


def test_no_placeholder_target_when_none_declared(tmp_path: Path, v2_leaf: Any) -> None:
    leaf = v2_leaf(tmp_path / "xonly", targets={})  # X-only-ish: no declared targets
    desc, _ = build_descriptor_from_card(leaf)
    assert desc.targets == []  # never invent a target


def test_tier_public_only_when_open_and_cleared(tmp_path: Path, v2_leaf: Any) -> None:
    pub = v2_leaf(tmp_path / "pub", public=True, sample_of={"o1": "s1", "o2": "s2"})
    priv = v2_leaf(tmp_path / "priv", public=False, sample_of={"o1": "s1", "o2": "s2"})
    assert build_descriptor_from_card(pub)[0].tier is Tier.PUBLIC
    assert build_descriptor_from_card(priv)[0].tier is Tier.PRIVATE


def test_sample_id_availability(tmp_path: Path, v2_leaf: Any) -> None:
    with_sid = v2_leaf(tmp_path / "withsid", sample_of={"o1": "s1", "o2": "s2"})
    without = v2_leaf(tmp_path / "nosid", sample_of=None)  # no sample_id column in M
    assert build_descriptor_from_card(with_sid)[0].ids.sample_id_available is True
    assert build_descriptor_from_card(without)[0].ids.sample_id_available is False
    assert build_descriptor_from_card(without)[0].alignment_level is AlignmentLevel.OBSERVATION


def test_native_split_documented_not_applied(tmp_path: Path, v2_leaf: Any) -> None:
    leaf = v2_leaf(tmp_path / "ds", sample_of={"o1": "s1", "o2": "s2"}, split={"o1": "cal", "o2": "test"})
    desc, _ = build_descriptor_from_card(leaf)
    assert [sp.name for sp in desc.splits] == ["original"]
    assert desc.splits[0].applied is False


def test_origin_and_publication_routing(tmp_path: Path, v2_leaf: Any) -> None:
    leaf = v2_leaf(tmp_path / "ds", sample_of={"o1": "s1", "o2": "s2"})
    desc, _ = build_descriptor_from_card(leaf)
    assert any(src.kind.value == "zenodo" for src in desc.origin_sources)  # data DOI -> origin
    assert any(pub.doi == "10.1038/s41586-020-0" for pub in desc.publications)  # journal DOI -> publication


def test_bootstrap_idempotent_and_prune(tmp_path: Path, v2_leaf: Any) -> None:
    source = tmp_path / "source"
    v2_leaf(source / "v2.0" / "ds_a", sample_of={"o1": "s1", "o2": "s2"})
    v2_leaf(source / "v2.0" / "ds_b", sample_of={"o1": "s1", "o2": "s2"})
    assert {p.name for p in find_v2_leaves(source)} == {"ds_a", "ds_b"}

    catalog = tmp_path / "catalog_root"
    first = bootstrap(source, catalog)
    assert sorted(c["id"] for c in first["created"]) == ["ds_a", "ds_b"]
    second = bootstrap(source, catalog)
    assert second["created"] == [] and {s["reason"] for s in second["skipped"]} == {"unchanged"}

    # remove a source leaf -> its managed descriptor becomes an orphan, pruned with prune=True
    import shutil

    shutil.rmtree(source / "v2.0" / "ds_b")
    pruned = bootstrap(source, catalog, prune=True)
    assert pruned["removed"] == ["ds_b"]
    assert not (catalog / "catalog" / "datasets" / "ds_b.yaml").exists()
    assert (catalog / "catalog" / "datasets" / "ds_a.yaml").exists()
