"""Guard a presentation-only migration against accidental data requalification."""
from __future__ import annotations

import copy
import csv
import importlib.util
import json
from pathlib import Path
from typing import Any

import pytest
import yaml

from nirs4all_datasets.manifest import metadata_hash, processing_hash
from nirs4all_datasets.qualify.profile import qualify
from nirs4all_datasets.schema import DatasetDescriptor

SPEC = importlib.util.spec_from_file_location("rename_dataset_displays", Path(__file__).resolve().parents[1] / "scripts/rename_dataset_displays.py")
assert SPEC and SPEC.loader
RENAME = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RENAME)


def descriptor_file(root: Path, descriptor: DatasetDescriptor) -> Path:
    path = root / "catalog/datasets" / f"{descriptor.id}.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(descriptor.model_dump(mode="json"), sort_keys=False), encoding="utf-8")
    return path


def test_rename_retains_qualification_and_is_idempotent(canonical_dataset: Any) -> None:
    directory, descriptor = canonical_dataset("display_names", blocks=("X1", "X2"), sample_of={"o1": "s1", "o2": "s1"}, targets={"Moisture": "numeric"})
    before = qualify(directory, descriptor, compute_assets=False, compute_pca=False)
    manifest = (directory / "manifest.json").read_bytes()
    path = descriptor_file(directory.parents[1], descriptor)
    changes = RENAME.plan_rename(path, descriptor.name, "Corn — two instruments", directory)
    after = json.loads(changes[directory / "card.json"])
    expected = copy.deepcopy(before)
    expected["identity"]["name"] = "Corn — two instruments"
    renamed = descriptor.model_copy(update={"name": expected["identity"]["name"]})
    expected["integrity"]["metadata_hash"] = metadata_hash(renamed)
    assert after == expected
    assert before["generated_at"] == after["generated_at"]
    assert processing_hash(descriptor) == processing_hash(renamed)
    assert json.loads((directory / "croissant.json").read_text())["name"] == descriptor.id
    for output, text in changes.items():
        output.write_text(text, encoding="utf-8")
    assert RENAME.plan_rename(path, descriptor.name, renamed.name, directory) == {}
    assert (directory / "manifest.json").read_bytes() == manifest
    assert path.read_text().startswith("schema_version:")
    assert DatasetDescriptor(**yaml.safe_load(path.read_text())) == renamed
    assert renamed.name in (directory / "card.md").read_text(encoding="utf-8")


@pytest.mark.parametrize("drift", ["metadata", "processing", "card_identity", "unexpected_name"])
def test_rename_rejects_stale_inputs_without_writing(canonical_dataset: Any, drift: str) -> None:
    directory, descriptor = canonical_dataset("stale_names")
    qualify(directory, descriptor, compute_assets=False, compute_pca=False)
    path = descriptor_file(directory.parents[1], descriptor)
    if drift == "metadata":
        changed = descriptor.model_copy(update={"description": "Changed outside this migration"})
        path = descriptor_file(directory.parents[1], changed)
    elif drift in {"processing", "card_identity"}:
        card_path = directory / "card.json"
        card = json.loads(card_path.read_text())
        if drift == "processing":
            card["integrity"]["processing_hash"] = "0" * 64
        else:
            card["identity"]["id"] = "another_dataset"
        card_path.write_text(json.dumps(card), encoding="utf-8")
    before = {p: p.read_bytes() for p in [path, directory / "card.json", directory / "manifest.json"]}
    with pytest.raises(ValueError):
        RENAME.plan_rename(path, "unreviewed old name" if drift == "unexpected_name" else descriptor.name, "New display name", directory)
    assert all(p.read_bytes() == payload for p, payload in before.items())


def test_crosswalk_validates_every_row_before_any_write(tmp_path: Path, descriptor: DatasetDescriptor) -> None:
    first = descriptor_file(tmp_path, descriptor)
    second = descriptor_file(tmp_path, descriptor.model_copy(update={"id": "second", "name": "Second original"}))
    mapping = tmp_path / "names.csv"
    with mapping.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["dataset_id", "previous_display_name", "display_name"])
        writer.writeheader()
        writer.writerows([
            {"dataset_id": descriptor.id, "previous_display_name": descriptor.name, "display_name": "First renamed"},
            {"dataset_id": "second", "previous_display_name": "Wrong previous name", "display_name": "Second renamed"},
        ])
    original = first.read_bytes()
    with pytest.raises(ValueError, match="current name"):
        RENAME.apply_crosswalk(tmp_path, mapping, write=True)
    assert first.read_bytes() == original
    assert yaml.safe_load(second.read_text())["name"] == "Second original"


def test_crosswalk_rejects_collision_with_unmapped_dataset(tmp_path: Path, descriptor: DatasetDescriptor) -> None:
    descriptor_file(tmp_path, descriptor)
    descriptor_file(tmp_path, descriptor.model_copy(update={"id": "second", "name": "Existing NAME"}))
    mapping = tmp_path / "names.csv"
    mapping.write_text(f'dataset_id,previous_display_name,display_name\n{descriptor.id},{descriptor.name},existing name\n', encoding="utf-8")
    with pytest.raises(ValueError, match="not unique"):
        RENAME.apply_crosswalk(tmp_path, mapping, write=True)
