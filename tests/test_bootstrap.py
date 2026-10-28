"""Tests for descriptor authoring from v2.0 dataset_card.json (schema 2.0)."""
from __future__ import annotations

import json
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


def test_x_only_discovery_and_unlisted_metadata(tmp_path: Path, v2_leaf: Any) -> None:
    leaf = v2_leaf(tmp_path / "v2.0" / "xonly", targets={}, extra_meta=("region",))
    (leaf / "Y.csv").unlink()
    card_path = leaf / "dataset_card.json"
    card = json.loads(card_path.read_text())
    card["metadata_fields_summary"]["m_fields"] = []
    card_path.write_text(json.dumps(card))
    assert find_v2_leaves(tmp_path) == [leaf]
    desc, _ = build_descriptor_from_card(leaf)
    assert not desc.targets
    assert any(v.name == "region" and v.role is VariableRole.METADATA for v in desc.variables)


def test_metadata_header_preserves_trailing_space(tmp_path: Path, v2_leaf: Any) -> None:
    leaf = v2_leaf(tmp_path / "ds", extra_meta=("measurement ",))
    desc, _ = build_descriptor_from_card(leaf)
    assert any(v.name == "measurement " for v in desc.metadata_variables)


def test_declared_signal_and_wavenumber(tmp_path: Path, v2_leaf: Any) -> None:
    leaf = v2_leaf(tmp_path / "ds")
    path = leaf / "dataset_card.json"
    card = json.loads(path.read_text())
    card["spectral_blocks"][0].update(axis_unit="cm^-1", signal_type="Reflectance (percent)")
    path.write_text(json.dumps(card))
    source = build_descriptor_from_card(leaf)[0].sources[0]
    assert source.axis_unit.value == "cm-1"
    assert source.signal_type.value == "reflectance%"


def test_micrometer_axis_preserves_native_unit_warning(tmp_path: Path, v2_leaf: Any) -> None:
    leaf = v2_leaf(tmp_path / "ds")
    path = leaf / "dataset_card.json"
    card = json.loads(path.read_text())
    card["spectral_blocks"][0].update(axis_unit="Wavelength (micrometers)", axis_min="0.4", axis_max="2.5")
    path.write_text(json.dumps(card))
    desc, warnings = build_descriptor_from_card(leaf)
    assert desc.sources[0].axis_unit.value == "none"
    assert desc.sources[0].axis_min == 0.4
    assert any("Wavelength (micrometers)" in w and "Multiply by 1000" in w for w in warnings)
    assert warnings == desc.provenance.warnings


def test_text_summary_fields_are_accepted(tmp_path: Path, v2_leaf: Any) -> None:
    leaf = v2_leaf(tmp_path / "ds", extra_meta=("region",))
    path = leaf / "dataset_card.json"
    card = json.loads(path.read_text())
    card.update(metadata_fields_summary="see metadata", split_summary="none", source_summary="Example source", reproducibility_assessment="manual")
    path.write_text(json.dumps(card))
    desc, _ = build_descriptor_from_card(leaf)
    assert any(v.name == "region" for v in desc.variables)
    assert desc.reproducibility == {"assessment": "manual"}


def test_tier_public_only_when_open_and_cleared(tmp_path: Path, v2_leaf: Any) -> None:
    pub = v2_leaf(tmp_path / "pub", public=True, sample_of={"o1": "s1", "o2": "s2"})
    priv = v2_leaf(tmp_path / "priv", public=False, sample_of={"o1": "s1", "o2": "s2"})
    assert build_descriptor_from_card(pub)[0].tier is Tier.PUBLIC
    assert build_descriptor_from_card(priv)[0].tier is Tier.PRIVATE


def test_restricted_creative_commons_is_not_open(tmp_path: Path, v2_leaf: Any) -> None:
    leaf = v2_leaf(tmp_path / "restricted", public=True)
    path = leaf / "dataset_card.json"
    card = json.loads(path.read_text())
    card["license_summary"] = {"public_release_allowed": True, "license_name": "CC-BY-NC-4.0"}
    path.write_text(json.dumps(card))
    assert build_descriptor_from_card(leaf)[0].tier is Tier.PRIVATE


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


def test_refresh_preserves_curated_retrieval_and_pins(tmp_path: Path, v2_leaf: Any) -> None:
    import yaml

    source = tmp_path / "source"
    v2_leaf(source / "v2.0" / "ds")
    root = tmp_path / "catalog_root"
    bootstrap(source, root)
    path = root / "catalog" / "datasets" / "ds.yaml"
    data = yaml.safe_load(path.read_text())
    data["retrieval"]["routes"] = [{"id": "curated", "locator": "https://example.org/data"}]
    data["dataverse"]["doi"] = "10.1234/example"
    data["dataverse"]["dataset_version"] = "2.0"
    data["versions"]["content"] = "2.1.0"
    data["reproducibility"]["notes"] = "Curated conversion notes"
    path.write_text(yaml.safe_dump(data))
    bootstrap(source, root, force=True)
    refreshed = yaml.safe_load(path.read_text())
    assert refreshed["retrieval"]["routes"][0]["id"] == "curated"
    assert refreshed["dataverse"]["doi"] == "10.1234/example"
    assert refreshed["dataverse"]["dataset_version"] == "2.0"
    assert refreshed["versions"]["content"] == "2.1.0"
    assert refreshed["reproducibility"]["notes"] == "Curated conversion notes"
