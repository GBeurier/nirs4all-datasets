"""Shared test fixtures (schema 2.0)."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
import yaml

from nirs4all_datasets.manifest import metadata_hash, processing_hash
from nirs4all_datasets.schema import DatasetDescriptor

_DESCRIPTOR: dict[str, Any] = {
    "id": "corn",
    "name": "Corn",
    "description": "example",
    "domain": "agriculture",
    "sources": [{"source_id": "X1", "instrument_name": "m5", "axis_unit": "nm", "signal_type": "absorbance", "n_observations": 80, "n_variables": 700}],
    "variables": [{"name": "protein", "role": "target", "type": "numeric", "unit": "%"}],
    "provenance": {"contributor": "Lab"},
    "governance": {
        "license": "CC-BY-4.0", "owner_steward": "Lab", "redistribution_rights": "open under CC-BY-4.0",
        "consent_ethics_status": "n/a", "anonymization_status": "n/a", "permitted_use": "research", "access_policy": "open",
    },
    "tier": "public",
}


@pytest.fixture
def descriptor() -> DatasetDescriptor:
    """A fully-populated, public-tier descriptor (with DataCite authors + an open origin source)."""
    data = dict(_DESCRIPTOR)
    data["citation"] = "Doe et al. (2024)"
    data["datacite"] = {"authors": [{"name": "Doe", "orcid": "0000-0002-1825-0097", "affiliation": "CIRAD"}]}
    data["publications"] = [{"doi": "10.1038/s41586-020-0", "title": "Doe et al."}]
    data["origin_sources"] = [{"kind": "zenodo", "locator": "10.5281/zenodo.1", "access": "open", "license": "CC-BY-4.0"}]
    return DatasetDescriptor(**data)


@pytest.fixture
def registry(tmp_path: Path) -> Path:
    """A minimal registry root with one descriptor + a generated card and manifest (schema 2.0)."""
    descriptors = tmp_path / "catalog" / "datasets"
    descriptors.mkdir(parents=True)
    (descriptors / "corn.yaml").write_text(yaml.safe_dump(_DESCRIPTOR), encoding="utf-8")

    desc = DatasetDescriptor(**_DESCRIPTOR)
    phash, mhash = processing_hash(desc), metadata_hash(desc)
    data_dir = tmp_path / "datasets" / "corn"
    data_dir.mkdir(parents=True)
    (data_dir / "card.json").write_text(
        json.dumps({
            "identity": {"id": "corn"},
            "inventory": {"n_samples": 80, "n_features": 700, "n_sources": 1},
            "integrity": {"content_hash": "abc123", "processing_hash": phash, "metadata_hash": mhash},
        }),
        encoding="utf-8",
    )
    (data_dir / "manifest.json").write_text(
        json.dumps({"schema_version": "2.0", "dataset_id": "corn", "processing_hash": phash, "converter_name": "c", "converter_version": "1"}),
        encoding="utf-8",
    )
    return tmp_path
