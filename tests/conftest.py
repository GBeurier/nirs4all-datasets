"""Shared test fixtures."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
import yaml

from nirs4all_datasets.manifest import descriptor_hash, metadata_hash
from nirs4all_datasets.schema import DatasetDescriptor

_DESCRIPTOR: dict[str, Any] = {
    "id": "corn",
    "name": "Corn",
    "version": "1.0.0",
    "description": "example",
    "domain": "agriculture",
    "instrument": {"modality": "NIR", "axis_unit": "nm", "signal_type": "absorbance"},
    "targets": [{"name": "protein", "task_type": "regression"}],
    "provenance": {"contributor": "Lab"},
    "governance": {
        "license": "CC-BY-4.0", "visibility": "public", "confidentiality_class": "public",
        "owner_steward": "Lab", "redistribution_rights": "CC-BY-4.0", "consent_ethics_status": "n/a",
        "anonymization_status": "n/a", "permitted_use": "research", "access_policy": "open",
    },
}


@pytest.fixture
def descriptor() -> DatasetDescriptor:
    """A fully-populated, publishable descriptor (with DataCite authors + DOI)."""
    data = dict(_DESCRIPTOR)
    data["citation"] = "Doe et al. (2024)"
    data["datacite"] = {"authors": [{"name": "Doe", "orcid": "0000-0002-1825-0097", "affiliation": "CIRAD"}]}
    data["dataverse"] = {"doi": "10.70112/abc"}
    return DatasetDescriptor(**data)


@pytest.fixture
def registry(tmp_path: Path) -> Path:
    """A minimal registry root with one descriptor + a generated card and manifest."""
    descriptors = tmp_path / "catalog" / "datasets"
    descriptors.mkdir(parents=True)
    (descriptors / "corn.yaml").write_text(yaml.safe_dump(_DESCRIPTOR), encoding="utf-8")

    dhash = descriptor_hash(DatasetDescriptor(**_DESCRIPTOR))
    mhash = metadata_hash(DatasetDescriptor(**_DESCRIPTOR))
    data_dir = tmp_path / "datasets" / "corn"
    data_dir.mkdir(parents=True)
    (data_dir / "card.json").write_text(
        json.dumps({
            "identity": {"id": "corn"},
            "inventory": {"n_samples": 80, "n_features": 700},
            "spectral": {"signal_type": "absorbance"},
            "integrity": {"content_hash": "abc123", "descriptor_hash": dhash, "metadata_hash": mhash},
        }),
        encoding="utf-8",
    )
    (data_dir / "manifest.json").write_text(json.dumps({"descriptor_hash": dhash}), encoding="utf-8")
    return tmp_path
