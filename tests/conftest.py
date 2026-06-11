"""Shared test fixtures (schema 2.0)."""
from __future__ import annotations

import json
from collections.abc import Sequence
from pathlib import Path
from typing import Any

import pytest
import yaml

from nirs4all_datasets.manifest import metadata_hash, processing_hash
from nirs4all_datasets.schema import DatasetDescriptor


def make_v2_leaf(
    leaf: Path,
    *,
    blocks: Sequence[str] = ("X",),
    block_obs: dict[str, list[str]] | None = None,
    sample_of: dict[str, str] | None = None,
    targets: dict[str, str] | None = None,
    extra_meta: Sequence[str] = (),
    split: dict[str, str] | None = None,
    public: bool = False,
) -> Path:
    """Write a synthetic v2.0 Frictionless leaf (dataset_card.json + X*/Y/M.csv) for hermetic tests.

    ``block_obs`` maps a block id -> its observation ids (lets a test build ASYMMETRIC sources);
    defaults to two shared observations. ``sample_of`` maps observation_id -> sample_id (omit -> no
    ``sample_id`` column, i.e. identity fallback). ``targets`` maps name -> 'numeric'|'categorical'.
    """
    leaf.mkdir(parents=True, exist_ok=True)
    block_obs = block_obs or {b: ["o1", "o2"] for b in blocks}
    targets = {"Moisture": "numeric", "variety": "categorical"} if targets is None else targets
    all_obs = sorted({o for obs in block_obs.values() for o in obs})

    spectral_blocks = []
    for b in blocks:
        obs = block_obs[b]
        rows = [f"{o};0.1;0.2" for o in obs]
        (leaf / f"{b}.csv").write_text("observation_id;1100;1102\n" + "\n".join(rows) + "\n", encoding="utf-8")
        spectral_blocks.append({"block_id": b, "x_file": f"{b}.csv", "instrument_name": f"inst_{b}", "axis_unit": "nm", "axis_min": "1100", "axis_max": "1102", "n_rows": len(obs), "n_spectral_variables": 2})

    # Y.csv (per observation, like the real corpus). Omit target columns -> X-only-ish (header only).
    yhead = ["observation_id", *targets]
    yrows = [";".join([o, *["3.1" if t == "numeric" else "a" for t in targets]]) for o in all_obs]
    (leaf / "Y.csv").write_text(";".join(yhead) + "\n" + "\n".join(yrows) + "\n", encoding="utf-8")

    # M.csv
    mcols = ["dataset_id", "observation_id"]
    if sample_of is not None:
        mcols.append("sample_id")
    if split is not None:
        mcols.append("split_original")
    mcols.extend(extra_meta)
    mrows = []
    for o in all_obs:
        cells = [leaf.name, o]
        if sample_of is not None:
            cells.append(sample_of.get(o, o))
        if split is not None:
            cells.append(split.get(o, ""))
        cells.extend(["meta"] * len(extra_meta))
        mrows.append(";".join(cells))
    (leaf / "M.csv").write_text(";".join(mcols) + "\n" + "\n".join(mrows) + "\n", encoding="utf-8")

    card = {
        "dataset_id": leaf.name,
        "dataset_name": leaf.name.replace("_", " ").title(),
        "spectral_organization": {"organization_type": "multi_block" if len(blocks) > 1 else "single_block", "alignment_level": "sample" if sample_of is not None else "observation", "n_blocks": len(blocks)},
        "spectral_blocks": spectral_blocks,
        "target_summary": {"target_variables": list(targets), "target_types": {k: ("regression" if v == "numeric" else "classification") for k, v in targets.items()}},
        "metadata_fields_summary": {"m_fields": mcols},
        "split_summary": {"original_split_available": split is not None, "split_should_be_preserved_not_applied": True},
        "license_summary": {"public_release_allowed": public, "rights_notes": "synthetic", **({"license_name": "CC-BY-4.0"} if public else {})},
        "source_summary": {"source_name": "Synthetic", "source_url": "https://doi.org/10.5281/zenodo.1"},
        "detected_sources": [{"url": "https://doi.org/10.5281/zenodo.1"}],
        "associated_publications": [{"doi": "10.1038/s41586-020-0"}],
    }
    (leaf / "dataset_card.json").write_text(json.dumps(card), encoding="utf-8")
    return leaf

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
def v2_leaf():  # noqa: ANN201 - factory fixture
    """Factory returning :func:`make_v2_leaf` (build a synthetic v2.0 package in a tmp dir)."""
    return make_v2_leaf


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
