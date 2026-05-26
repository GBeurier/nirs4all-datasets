"""Tests for the Croissant (JSON-LD) renderer (pure, no nirs4all)."""
from __future__ import annotations

import json

from nirs4all_datasets import schema as s
from nirs4all_datasets.qualify.croissant import render_croissant


def test_render_croissant_structure(descriptor: s.DatasetDescriptor) -> None:
    croissant = render_croissant(
        descriptor,
        {"inventory": {"n_samples": 80}},
        files=[("X.parquet", "a" * 64, 11), ("Y.parquet", "b" * 64, 12)],
        instance="https://entrepot.recherche.data.gouv.fr",
    )

    assert croissant["@type"] == "sc:Dataset"
    assert croissant["conformsTo"] == "http://mlcommons.org/croissant/1.0"
    assert croissant["url"] == "https://doi.org/10.70112/abc"  # dataset landing page
    assert croissant["creator"][0]["sameAs"] == "https://orcid.org/0000-0002-1825-0097"

    distribution = {f["@id"]: f for f in croissant["distribution"]}
    assert distribution["X.parquet"]["sha256"] == "a" * 64
    assert distribution["X.parquet"]["contentUrl"] == "https://entrepot.recherche.data.gouv.fr/api/access/datafile/11"

    fields = {f["name"]: f for f in croissant["recordSet"][0]["field"]}
    assert fields["spectrum"]["repeated"] is True
    assert fields["spectrum"]["source"]["fileObject"]["@id"] == "X.parquet"
    assert fields["protein"]["dataType"] == "sc:Float"  # regression target
    assert fields["protein"]["source"]["extract"]["column"] == "protein"

    json.dumps(croissant)  # fully JSON-serializable


def test_croissant_without_doi_uses_instance() -> None:
    descriptor = s.DatasetDescriptor(
        id="bare", name="Bare", version="1.0.0", description="x",
        instrument={"modality": "NIR"}, targets=[{"name": "cls", "task_type": "multiclass_classification"}],
        provenance={"contributor": "Lab"}, governance={"license": "CC-BY-4.0"},
    )
    croissant = render_croissant(descriptor, {}, files=[])
    assert croissant["url"] == "https://entrepot.recherche.data.gouv.fr"
    fields = {f["name"]: f for f in croissant["recordSet"][0]["field"]}
    assert fields["cls"]["dataType"] == "sc:Integer"  # classification target
