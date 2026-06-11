"""Tests for dataset discovery and descriptor auto-generation."""
from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from nirs4all_datasets import discover
from nirs4all_datasets.schema import DatasetDescriptor


# --- pure helpers (no nirs4all) ---------------------------------------------
def test_slugify_and_id_dedup() -> None:
    assert discover.slugify("Corn_Oil 80 (m5)") == "corn_oil_80_m5"
    assert discover.dataset_id("ALPINE", "ALPINE_C_424_KS") == "alpine_c_424_ks"  # family prefix collapsed
    assert discover.dataset_id("CORN", "Corn_Oil_80_WangStyle_m5spec") == "corn_oil_80_wangstyle_m5spec"
    assert discover.dataset_id("ARABIDOPSIS_CEFE", "Genotype10_250") == "arabidopsis_cefe_genotype10_250"


def test_generic_header_detection() -> None:
    assert discover._is_generic_header("x") and discover._is_generic_header("y_cal") and discover._is_generic_header("Ycal")
    assert not discover._is_generic_header("CoffeeType") and not discover._is_generic_header("oil")


def test_axis_unit_inference(tmp_path: Path) -> None:
    def unit(header: str) -> str:
        p = tmp_path / "X.csv"
        p.write_text(header + "\n0;0;0\n", encoding="utf-8")
        return discover._infer_axis_unit(p)

    assert unit("1100;1102;1104") == "nm"
    assert unit("350;1000;2500") == "nm"
    assert unit("4000;8000;12000") == "cm-1"
    assert unit("852.78_nm;853.34_nm") == "nm"
    assert unit("a;b;c") == "index"


def test_read_column_not_truncated(tmp_path: Path) -> None:
    # The csv sniffer would split "CoffeeType" on an interior char; the delimiter-aware reader must not.
    p = tmp_path / "Y.csv"
    p.write_text("CoffeeType\nReggio\nRenzo\nLa Spezia\n", encoding="utf-8")
    header, values = discover._read_column(p)
    assert header == "CoffeeType"
    assert list(values) == ["Reggio", "Renzo", "La Spezia"]


def test_spdx_mapping() -> None:
    assert discover._spdx("CC0 1.0") == "CC0-1.0"
    assert discover._spdx("CC BY 4.0") == "CC-BY-4.0"
    assert discover._spdx("GPL (>= 2)") == "GPL-2.0-or-later"
    assert discover._spdx("none") is None and discover._spdx(None) is None
    assert discover._spdx("some custom thing").startswith("LicenseRef-")


# --- bootstrap over a synthetic source tree (needs nirs4all FolderParser) ---
pytest.importorskip("nirs4all")


def _make_leaf(path: Path, *, clf: bool = False, empty_meta: bool = False) -> None:
    path.mkdir(parents=True)
    (path / "Xtrain.csv").write_text("1100;1102;1104\n0.1;0.2;0.3\n0.2;0.3;0.4\n", encoding="utf-8")
    (path / "Xtest.csv").write_text("1100;1102;1104\n0.15;0.25;0.35\n", encoding="utf-8")
    if clf:
        (path / "Ytrain.csv").write_text("Species\nAlpha\nBeta\n", encoding="utf-8")
        (path / "Ytest.csv").write_text("Species\nAlpha\n", encoding="utf-8")
    else:
        (path / "Ytrain.csv").write_text("Brix\n3.1\n3.2\n", encoding="utf-8")
        (path / "Ytest.csv").write_text("Brix\n3.15\n", encoding="utf-8")
    if empty_meta:
        (path / "Mtrain.csv").write_text("", encoding="utf-8")


@pytest.fixture
def source_tree(tmp_path: Path) -> Path:
    src = tmp_path / "src"
    _make_leaf(src / "regression" / "BERRY" / "brix_split", empty_meta=True)
    _make_leaf(src / "classification" / "COFFEE" / "species_split", clf=True)
    return src


def test_bootstrap_creates_valid_descriptors(source_tree: Path, tmp_path: Path) -> None:
    root = tmp_path / "registry"
    report = discover.bootstrap(source_tree, root)
    assert len(report["created"]) == 2 and not report["errors"]

    files = sorted((root / "catalog" / "datasets").glob("*.yaml"))
    descriptors = {f.stem: DatasetDescriptor(**(yaml.safe_load(f.read_text()) or {})) for f in files}
    berry = descriptors["berry_brix_split"]
    assert berry.targets[0].task_type.value == "regression"
    assert berry.targets[0].name == "Brix"
    assert berry.instrument.axis_unit.value == "nm"
    assert berry.generation and berry.generation.managed and berry.generation.source_relpath.endswith("brix_split")

    coffee = descriptors["coffee_species_split"]
    assert coffee.targets[0].task_type.value == "binary_classification"
    assert coffee.targets[0].classes == ["Alpha", "Beta"]  # sorted union of train+test labels


def test_bootstrap_is_idempotent_and_protects_human_edits(source_tree: Path, tmp_path: Path) -> None:
    root = tmp_path / "registry"
    discover.bootstrap(source_tree, root)
    again = discover.bootstrap(source_tree, root)
    assert len(again["skipped"]) == 2 and not again["created"] and not again["updated"]  # unchanged

    forced = discover.bootstrap(source_tree, root, force=True)
    assert len(forced["updated"]) == 2

    # Mark one descriptor as human-managed -> never overwritten without force.
    path = root / "catalog" / "datasets" / "berry_brix_split.yaml"
    data = yaml.safe_load(path.read_text())
    data["generation"]["managed"] = False
    data["description"] = "Hand-edited; keep me."
    path.write_text(yaml.safe_dump(data), encoding="utf-8")
    discover.bootstrap(source_tree, root)
    assert "Hand-edited" in path.read_text()


def test_bootstrap_detects_metadata_only_change(source_tree: Path, tmp_path: Path) -> None:
    """A provenance-only edit (excluded from descriptor_hash) must still be re-bootstrapped."""
    from nirs4all_datasets.manifest import descriptor_hash, metadata_hash

    root = tmp_path / "registry"
    discover.bootstrap(source_tree, root)
    path = root / "catalog" / "datasets" / "berry_brix_split.yaml"
    data = yaml.safe_load(path.read_text())
    before = DatasetDescriptor(**data)
    data["sources"] = [{"kind": "zenodo", "mode": "raw", "locator": "10.5281/zenodo.123", "access": "open"}]  # sources excluded from descriptor_hash
    path.write_text(yaml.safe_dump(data), encoding="utf-8")
    after = DatasetDescriptor(**data)
    assert descriptor_hash(before) == descriptor_hash(after)  # canonical bytes unaffected by sources
    assert metadata_hash(before) != metadata_hash(after)  # but the card/catalog must notice
    again = discover.bootstrap(source_tree, root)  # non-force
    assert any(u["id"] == "berry_brix_split" for u in again["updated"])  # rewritten, not skipped as "unchanged"
