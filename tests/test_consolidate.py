"""Composition of upstream per-target / per-instrument leaves into one database leaf."""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import pytest

from nirs4all_datasets import consolidate
from nirs4all_datasets.bootstrap import build_descriptor_from_card, find_v2_leaves


def _leaf(path: Path, rows: dict[str, tuple[str | None, list[float]]], *, y: dict[str, list[str]], m: dict[str, list[str]] | None = None, keyless_y: bool = False, license_name: str = "CC BY 4.0") -> Path:
    """Write one standardized leaf: ``rows`` maps observation_id -> (sample_id, spectrum)."""
    path.mkdir(parents=True)
    ids = list(rows)
    (path / "X.csv").write_text("observation_id;1100;1102\n" + "".join(f"{o};{';'.join(map(str, rows[o][1]))}\n" for o in ids), encoding="utf-8")
    metadata = pd.DataFrame({"dataset_id": path.name, "observation_id": ids, **({"sample_id": [rows[o][0] or "" for o in ids]} if any(rows[o][0] for o in ids) else {}), "task_type": "regression", **(m or {})})
    metadata.to_csv(path / "M.csv", sep=";", index=False)
    targets = pd.DataFrame(y) if keyless_y else pd.DataFrame({"observation_id": ids, **y})
    targets.to_csv(path / "Y.csv", sep=";", index=False)
    card = {
        "dataset_id": path.name, "dataset_name": path.name,
        "license_summary": {"license_name": license_name, "license_url": "https://creativecommons.org/licenses/by/4.0/", "public_release_allowed": True},
        "rights": {"public_release_allowed": True},
        "spectral_blocks": [{"block_id": "X", "x_file": "X.csv", "instrument_name": f"{path.name} instrument", "axis_unit": "nm", "axis_min": "1100", "axis_max": "1102", "n_rows": len(ids), "n_spectral_variables": 2}],
        "target_summary": {"target_variables": list(y), "target_types": dict.fromkeys(y, "regression")},
        "detected_sources": [{"url": "https://zenodo.org/records/1"}],
    }
    (path / "dataset_card.json").write_text(json.dumps(card), encoding="utf-8")
    return path


@pytest.fixture
def declare(monkeypatch):
    def apply(databases: dict, superseded: dict | None = None) -> None:
        monkeypatch.setattr(consolidate, "spec", lambda: {"databases": databases, "superseded": superseded or {}})
    return apply


def test_target_split_leaves_become_one_database_with_all_targets(tmp_path, declare):
    base = tmp_path / "tree" / "v2.0"
    spectra = {"a1": ("s1", [0.1, 0.2]), "a2": ("s2", [0.3, 0.4]), "a3": ("s3", [0.5, 0.6])}
    _leaf(base / "trait_a", spectra, y={"lma": ["1.0", "2.0", "3.0"]}, keyless_y=True)
    # The second export kept only the spectra with a measured trait, spelled numbers differently and
    # recorded its own (passport) source file.
    _leaf(base / "trait_b", {"b1": ("s3", [0.5, 0.6]), "b2": ("s1", [0.1, 0.2])}, y={"nitrogen": ["7", "5"]}, m={"lma": ["3.00", "1"], "source_file": ["b.csv", "b.csv"]})
    declare({"db": {"name": "Database", "blocks": {"X": {"members": ["trait_a", "trait_b"]}}}})

    report = consolidate.consolidate_tree(tmp_path / "tree")
    assert report["composed"] == ["db"] and not report["errors"]
    leaf = tmp_path / "tree" / "consolidated" / "db"
    x = pd.read_csv(leaf / "X.csv", sep=";")
    y = pd.read_csv(leaf / "Y.csv", sep=";", dtype=str, keep_default_na=False)
    m = pd.read_csv(leaf / "M.csv", sep=";", dtype=str, keep_default_na=False)
    assert len(x) == 3 and x["observation_id"].tolist() == ["db_000001", "db_000002", "db_000003"]
    assert list(y.columns) == ["observation_id", "lma", "nitrogen"]
    assert y["nitrogen"].tolist() == ["5", "", "7"]
    assert m["sample_id"].tolist() == ["s1", "s2", "s3"]
    assert "task_type" not in m  # per-task plumbing of the retired views
    card = json.loads((leaf / "dataset_card.json").read_text())
    assert card["target_summary"]["target_variables"] == ["lma", "nitrogen"]
    assert card["consolidation"]["members"]["trait_b"] == {"block": "X", "observations": 2, "matched_existing": 2}
    descriptor, _ = build_descriptor_from_card(leaf)
    assert descriptor.id == "db" and [v.name for v in descriptor.targets] == ["lma", "nitrogen"]

    assert consolidate.consolidate_tree(tmp_path / "tree")["unchanged"] == ["db"]
    assert [p.name for p in find_v2_leaves(tmp_path / "tree")] == ["db"]


def test_conflicting_measurements_abort_instead_of_choosing_one(tmp_path, declare):
    base = tmp_path / "tree" / "v2.0"
    _leaf(base / "a", {"a1": ("s1", [0.1, 0.2])}, y={"lma": ["1.0"]})
    _leaf(base / "b", {"b1": ("s1", [0.1, 0.2])}, y={"lma": ["9.0"]})
    declare({"db": {"blocks": {"X": {"members": ["a", "b"]}}}})
    report = consolidate.consolidate_tree(tmp_path / "tree")
    assert "lma='9.0' conflicts with '1.0'" in report["errors"]["db"]
    assert not (tmp_path / "tree" / "consolidated" / "db" / "consolidation.json").exists()


def test_identical_spectra_of_different_samples_stay_distinct(tmp_path, declare):
    base = tmp_path / "tree" / "v2.0"
    _leaf(base / "a", {"a1": ("s1", [0.1, 0.2])}, y={"lma": ["1.0"]})
    _leaf(base / "b", {"b1": ("s2", [0.1, 0.2])}, y={"n": ["4"]})
    declare({"db": {"blocks": {"X": {"members": ["a", "b"]}}}})
    consolidate.consolidate_tree(tmp_path / "tree")
    m = pd.read_csv(tmp_path / "tree" / "consolidated" / "db" / "M.csv", sep=";", dtype=str)
    assert m["sample_id"].tolist() == ["s1", "s2"]


def test_stacked_campaigns_keep_every_observation_and_their_label(tmp_path, declare):
    base = tmp_path / "tree" / "v2.0"
    _leaf(base / "t1", {"p1": ("plant1", [0.1, 0.2])}, y={"strain": ["NO"]})
    _leaf(base / "t2", {"p1": ("plant1", [0.1, 0.2])}, y={"strain": ["NO"]})
    declare({"db": {"blocks": {"X": {"mode": "stack", "members": ["t1", "t2"]}}, "label": {"column": "measurement_time", "values": {"t1": "time1", "t2": "time2"}}}})
    consolidate.consolidate_tree(tmp_path / "tree")
    m = pd.read_csv(tmp_path / "tree" / "consolidated" / "db" / "M.csv", sep=";", dtype=str)
    assert m["sample_id"].tolist() == ["plant1", "plant1"]
    assert m["measurement_time"].tolist() == ["time1", "time2"]


def test_instruments_become_sources_linked_by_sample_identity(tmp_path, declare):
    base = tmp_path / "tree" / "v2.0"
    _leaf(base / "asd", {"x1": ("c1", [0.1, 0.2]), "x2": ("c2", [0.3, 0.4])}, y={"component": ["a", "b"]})
    _leaf(base / "scio", {"y1": ("c2", [0.7, 0.8])}, y={"component": ["b"]})
    declare({"db": {"blocks": {"X_asd": {"members": ["asd"]}, "X_scio": {"members": ["scio"]}}}})
    consolidate.consolidate_tree(tmp_path / "tree")
    leaf = tmp_path / "tree" / "consolidated" / "db"
    assert pd.read_csv(leaf / "X_scio.csv", sep=";")["observation_id"].tolist() == ["db_000003"]
    descriptor, _ = build_descriptor_from_card(leaf)
    assert [s.source_id for s in descriptor.sources] == ["X_asd", "X_scio"]
    assert [s.n_observations for s in descriptor.sources] == [2, 1]
    assert pd.read_csv(leaf / "M.csv", sep=";")["sample_id"].tolist() == ["c1", "c2", "c2"]


def test_members_with_different_rights_are_never_merged(tmp_path, declare):
    base = tmp_path / "tree" / "v2.0"
    _leaf(base / "open", {"a1": ("s1", [0.1, 0.2])}, y={"lma": ["1"]})
    _leaf(base / "local", {"b1": ("s1", [0.1, 0.2])}, y={"lma": ["1"]}, license_name="NOASSERTION")
    declare({"db": {"blocks": {"X": {"members": ["open"]}, "X_copy": {"members": ["local"]}}}})
    assert "different licenses" in consolidate.consolidate_tree(tmp_path / "tree")["errors"]["db"]


def test_superseded_leaves_are_not_catalog_datasets(tmp_path, declare):
    base = tmp_path / "tree" / "v2.0"
    _leaf(base / "database", {"a1": ("s1", [0.1, 0.2])}, y={"lma": ["1"], "n": ["2"]})
    _leaf(base / "lma_view", {"a1": ("s1", [0.1, 0.2])}, y={"lma": ["1"]})
    declare({}, {"lma_view": "database"})
    assert [p.name for p in find_v2_leaves(tmp_path / "tree")] == ["database"]


def test_the_committed_specification_is_consistent():
    entries = consolidate.spec()["databases"]
    consumed = consolidate.consumed_ids()
    for database, entry in entries.items():
        assert database == database.lower() and entry["blocks"]
        for block_id, block in entry["blocks"].items():
            assert block_id == "X" or block_id.startswith("X_")
            assert block.get("mode", "union") in {"union", "stack"}
        if "label" in entry:
            members = {consolidate._member_ref(r)[0] for b in entry["blocks"].values() for r in b["members"]}
            assert set(entry["label"]["values"]) == members
    for retired, database in consolidate.spec()["superseded"].items():
        assert retired not in entries and (database not in consumed or database in entries)
