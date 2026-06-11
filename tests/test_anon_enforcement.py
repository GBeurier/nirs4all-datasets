"""End-to-end enforcement of the anonymized tier: no original name/text leaks through any public path.

Guards the fix for the Codex NO-GO — anonymization is TIER-DRIVEN (automatic), not an opt-in flag, so an
anonymized dataset cannot leak through the tracked card artifacts, the catalog index, or the plugin API.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from nirs4all_datasets import schema as s

_T = "MoistureSecret"  # a numeric target name that must never appear in any public artifact
_M = "ProvenanceSecret"  # a metadata name that must never leak
_NAME = "SecretGrassDataset"
_DESC = "Top secret grass description that must not leak."
_DOMAIN = "SecretDomainX"  # the domain reveals what the dataset is -> must be masked too
_SECRETS = (_T, _M, _NAME, _DESC, _DOMAIN, "secretword")


def _anon_dataset(canonical_dataset: Any) -> tuple[Path, s.DatasetDescriptor]:
    dataset_dir, descriptor = canonical_dataset("ds_secret", targets={_T: "numeric"}, extra_meta=(_M,), sample_of={"o1": "s1", "o2": "s2"})
    anon = descriptor.model_copy(update={"tier": s.Tier.ANONYMIZED, "name": _NAME, "description": _DESC, "keywords": ["secretword"], "domain": _DOMAIN})
    return dataset_dir, anon


def test_qualify_writes_anonymized_tracked_artifacts(tmp_path: Path, canonical_dataset: Any) -> None:
    pytest.importorskip("pyarrow")
    from nirs4all_datasets.qualify.profile import qualify

    dataset_dir, anon = _anon_dataset(canonical_dataset)
    card = qualify(dataset_dir, anon)
    blob = json.dumps(card)
    for path in ("card.json", "card.md", "croissant.json"):
        blob += (dataset_dir / path).read_text(encoding="utf-8")
    for secret in _SECRETS:
        assert secret not in blob, f"{secret!r} leaked into a tracked artifact"
    assert all(v["name"].startswith("var_") for v in card["variables"])  # masked names


def test_catalog_entry_masks_anonymized(tmp_path: Path, canonical_dataset: Any) -> None:
    pytest.importorskip("pyarrow")
    from nirs4all_datasets.catalog import catalog_entry
    from nirs4all_datasets.qualify.profile import qualify

    dataset_dir, anon = _anon_dataset(canonical_dataset)
    qualify(dataset_dir, anon)
    entry = catalog_entry(tmp_path, anon)
    assert _T not in entry["targets"] and all(t.startswith("var_") for t in entry["targets"])
    assert entry["name"] != _NAME and _NAME not in json.dumps(entry)
    assert entry["n_targets"] == 1  # the count is preserved, only the name is masked


def test_nirsdataset_public_surface_no_leak(tmp_path: Path, canonical_dataset: Any) -> None:
    pytest.importorskip("pyarrow")
    from nirs4all_datasets.dataset import NirsDataset
    from nirs4all_datasets.qualify.profile import qualify

    dataset_dir, anon = _anon_dataset(canonical_dataset)
    qualify(dataset_dir, anon)
    nd = NirsDataset(dataset_dir, anon)
    assert all(v.name.startswith("var_") for v in nd.variables())
    assert all(v.name.startswith("var_") for v in nd.descriptor.variables)
    assert nd.descriptor.name != _NAME and nd.descriptor.domain is None
    leak_surface = json.dumps(nd.card()) + json.dumps([v.name for v in nd.variables()]) + json.dumps(nd.descriptor.model_dump(mode="json"))
    for secret in _SECRETS:
        assert secret not in leak_surface
    y = nd.y()  # numeric target z-scored + column masked
    assert y is not None and all(c == "sample_id" or c.startswith("var_") for c in y.columns)


def test_public_tier_is_unchanged(tmp_path: Path, canonical_dataset: Any) -> None:
    """The enforcement is anonymized-only: a public dataset keeps its real names everywhere."""
    pytest.importorskip("pyarrow")
    from nirs4all_datasets.dataset import NirsDataset
    from nirs4all_datasets.qualify.profile import qualify

    dataset_dir, descriptor = canonical_dataset("ds_open", targets={"Moisture": "numeric"}, sample_of={"o1": "s1", "o2": "s2"})
    pub = descriptor.model_copy(update={"tier": s.Tier.PUBLIC})
    card = qualify(dataset_dir, pub)
    assert any(v["name"] == "Moisture" for v in card["variables"])
    assert any(v.name == "Moisture" for v in NirsDataset(dataset_dir, pub).variables())
