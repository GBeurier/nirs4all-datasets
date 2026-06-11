"""Tests for the Croissant (JSON-LD) renderer (pure card+descriptor -> dict, no nirs4all in the asserts)."""
from __future__ import annotations

import json
from typing import Any

from nirs4all_datasets.qualify.croissant import render_croissant
from nirs4all_datasets.qualify.profile import qualify


def test_render_croissant_is_valid_json_ld(canonical_dataset: Any) -> None:
    """A built card renders to valid Croissant JSON-LD: ``@context`` + ``@type``, a FileObject per
    source (+ a variables FileObject), and a RecordSet per source plus a variables RecordSet."""
    dataset_dir, desc = canonical_dataset("corn", blocks=("X1", "X2"), sample_of={"o1": "s1", "o2": "s2"})
    card = qualify(dataset_dir, desc, compute_assets=False, compute_pca=False)

    croissant = render_croissant(card, desc, hashes={}, file_ids={}, instance="https://x")

    # JSON-LD envelope.
    assert isinstance(croissant["@context"], dict)
    assert "@vocab" in croissant["@context"]
    assert croissant["@type"] == "sc:Dataset"
    assert croissant["conformsTo"] == "http://mlcommons.org/croissant/1.0"

    # One FileObject per source Parquet, plus a variables FileObject.
    distribution = {obj["@id"]: obj for obj in croissant["distribution"]}
    assert distribution["file/X1.parquet"]["@type"] == "cr:FileObject"
    assert "file/X2.parquet" in distribution
    assert "file/variables.parquet" in distribution

    # One RecordSet per source (array-valued spectrum field) + a variables RecordSet (one field/variable).
    record_sets = {rs["@id"]: rs for rs in croissant["recordSet"]}
    assert {"X1", "X2", "variables"} <= set(record_sets)
    x1_fields = {f["name"]: f for f in record_sets["X1"]["field"]}
    assert x1_fields["spectrum"]["repeated"] is True
    var_fields = {f["name"] for f in record_sets["variables"]["field"]}
    assert {"sample_id", "Moisture", "variety"} <= var_fields

    # Fully JSON-serializable.
    json.dumps(croissant)


def test_render_croissant_stamps_hashes_and_file_ids(canonical_dataset: Any) -> None:
    """Optional ``hashes`` / ``file_ids`` stamp ``sha256`` / ``contentUrl`` onto the matching FileObject."""
    dataset_dir, desc = canonical_dataset("corn", blocks=("X1",), sample_of={"o1": "s1", "o2": "s2"})
    card = qualify(dataset_dir, desc, compute_assets=False, compute_pca=False)

    croissant = render_croissant(
        card,
        desc,
        hashes={"X1.parquet": "a" * 64},
        file_ids={"X1.parquet": 11},
        instance="https://entrepot.recherche.data.gouv.fr",
    )
    x1 = next(obj for obj in croissant["distribution"] if obj["@id"] == "file/X1.parquet")
    assert x1["sha256"] == "a" * 64
    assert x1["contentUrl"] == "https://entrepot.recherche.data.gouv.fr/api/access/datafile/11"


def test_render_croissant_variable_datatypes(canonical_dataset: Any) -> None:
    """Variable fields are typed by their declared type: numeric -> Float, categorical -> Integer."""
    dataset_dir, desc = canonical_dataset("corn", blocks=("X1",), sample_of={"o1": "s1", "o2": "s2"})
    card = qualify(dataset_dir, desc, compute_assets=False, compute_pca=False)

    croissant = render_croissant(card, desc, hashes={}, file_ids={}, instance="https://x")
    variables_rs = next(rs for rs in croissant["recordSet"] if rs["@id"] == "variables")
    fields = {f["name"]: f for f in variables_rs["field"]}
    assert fields["Moisture"]["dataType"] == "sc:Float"  # numeric target
    assert fields["variety"]["dataType"] == "sc:Integer"  # categorical target
    assert fields["Moisture"]["source"]["extract"]["column"] == "Moisture"
