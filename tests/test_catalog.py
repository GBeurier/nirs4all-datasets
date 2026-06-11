"""Tests for catalog assembly and querying (schema 2.0).

Hermetic: a temp registry is built from synthetic v2.0 leaves via the real
bootstrap -> organize -> qualify pipeline, so every dataset has a real schema-2.0
descriptor YAML under ``catalog/datasets/<id>.yaml`` plus a real ``card.json`` +
``manifest.json``. No network. The fleet is three datasets:

* ``wheat`` — multi-source (X1+X2), public tier, one numeric target, native split.
* ``barley`` — single-source, private tier, one numeric target.
* ``soil`` — single-source, private tier, metadata-only (no declared target).
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
import yaml
from conftest import make_v2_leaf  # the shared synthetic-leaf factory

from nirs4all_datasets.bootstrap import build_descriptor_from_card
from nirs4all_datasets.catalog import (
    bank_summary,
    build_catalog,
    catalog_entry,
    get_card,
    load_catalog,
    search,
)
from nirs4all_datasets.manifest import metadata_hash, processing_hash
from nirs4all_datasets.organize import organize
from nirs4all_datasets.qualify.profile import qualify
from nirs4all_datasets.schema import DatasetDescriptor

# The documented per-dataset index entry contract (catalog_entry output).
_ENTRY_KEYS = {
    "id", "name", "domain", "tier", "license", "content_version", "schema_protocol",
    "spectro_family", "modalities", "n_sources", "source_ids", "n_features_total",
    "alignment_level", "n_targets", "targets", "n_metadata", "has_split", "splits",
    "n_samples", "doi", "origin_kinds", "origin_access", "n_publications",
    "card_protocol", "content_hash", "processing_hash", "has_card", "has_manifest",
    "is_stale", "publishable",
}


def _author(root: Path, name: str, **leaf_kwargs: Any) -> DatasetDescriptor:
    """Build one real dataset (descriptor YAML + canonical + card + manifest) under ``root``.

    Writes a synthetic v2.0 leaf, authors a schema-2.0 descriptor from its card, persists the
    descriptor to ``catalog/datasets/<id>.yaml``, then organizes (canonical + manifest) and
    qualifies (card.json) under ``datasets/<id>/`` — i.e. the on-disk layout the catalog reads.
    """
    leaf = make_v2_leaf(root / "src" / name, **leaf_kwargs)
    descriptor, _ = build_descriptor_from_card(leaf)

    desc_dir = root / "catalog" / "datasets"
    desc_dir.mkdir(parents=True, exist_ok=True)
    (desc_dir / f"{descriptor.id}.yaml").write_text(
        yaml.safe_dump(descriptor.model_dump(mode="json", exclude_none=True), sort_keys=False), encoding="utf-8"
    )

    organize(leaf, descriptor, root / "datasets")
    qualify(root / "datasets" / descriptor.id, descriptor, compute_assets=False, compute_pca=False)
    return descriptor


@pytest.fixture
def fleet(tmp_path: Path) -> tuple[Path, dict[str, DatasetDescriptor]]:
    """A temp registry with three real datasets: a multi-source public one, a private one, and a
    metadata-only one. Returns ``(root, {id: descriptor})``."""
    descriptors = {
        "wheat": _author(
            tmp_path, "wheat",
            blocks=("X1", "X2"), sample_of={"o1": "s1", "o2": "s2"},
            targets={"protein": "numeric"}, split={"o1": "calibration", "o2": "test"}, public=True,
        ),
        "barley": _author(
            tmp_path, "barley",
            sample_of={"o1": "s1", "o2": "s2"}, targets={"moisture": "numeric"},
        ),
        "soil": _author(tmp_path, "soil", targets={}),
    }
    return tmp_path, descriptors


# =============================================================================
# catalog_entry — per-dataset index entry
# =============================================================================
def test_catalog_entry_documented_keys_and_values(fleet: tuple[Path, dict[str, DatasetDescriptor]]) -> None:
    root, descriptors = fleet
    entry = catalog_entry(root, descriptors["wheat"])

    # exactly the documented key set.
    assert set(entry) == _ENTRY_KEYS

    # values derived from the descriptor.
    assert entry["id"] == "wheat"
    assert entry["tier"] == "public"
    assert entry["n_sources"] == 2
    assert entry["source_ids"] == ["X1", "X2"]
    assert entry["spectro_family"] == "NIR"
    assert entry["modalities"] == ["NIR"]
    assert entry["n_targets"] == 1
    assert entry["targets"] == ["protein"]
    assert entry["content_version"] == "1.0.0"
    assert entry["alignment_level"] == "sample"
    assert entry["has_split"] is True
    assert entry["splits"] == ["original"]
    assert entry["license"] == "CC-BY-4.0"
    assert entry["origin_kinds"] == ["zenodo"]
    assert entry["origin_access"] == ["open"]
    assert entry["n_features_total"] == 4  # 2 sources x 2 spectral variables

    # values from the fresh card / manifest.
    assert entry["n_samples"] == 2
    assert entry["has_card"] is True
    assert entry["has_manifest"] is True
    assert entry["is_stale"] is False
    assert entry["content_hash"]
    assert entry["card_protocol"]
    assert entry["processing_hash"] == processing_hash(descriptors["wheat"])
    assert entry["publishable"] is True


def test_catalog_entry_metadata_only(fleet: tuple[Path, dict[str, DatasetDescriptor]]) -> None:
    root, descriptors = fleet
    entry = catalog_entry(root, descriptors["soil"])
    assert entry["n_targets"] == 0
    assert entry["targets"] == []
    assert entry["tier"] == "private"
    assert entry["has_card"] is True
    assert entry["is_stale"] is False
    # publication_blockers only gates the public tier; private/anonymized descriptors are valid
    # catalog entries with no blockers (they are token-gated at fetch, never openly published).
    assert entry["publishable"] is True


def test_catalog_entry_health_passthrough(fleet: tuple[Path, dict[str, DatasetDescriptor]]) -> None:
    root, descriptors = fleet
    health = {"alive": True, "degraded": False, "origins": []}
    entry = catalog_entry(root, descriptors["wheat"], health=health)
    assert entry["health"] == health
    # omitted when not supplied.
    assert "health" not in catalog_entry(root, descriptors["wheat"])


# =============================================================================
# staleness
# =============================================================================
def test_metadata_edit_flags_stale_but_keeps_stats(fleet: tuple[Path, dict[str, DatasetDescriptor]]) -> None:
    # Editing keywords changes metadata_hash but NOT processing_hash, so the card's canonical-derived
    # stats stay trusted while the entry is flagged stale (the card no longer reflects the descriptor's
    # displayed metadata).
    root, descriptors = fleet
    wheat = descriptors["wheat"]
    edited = wheat.model_copy(update={"keywords": ["nir", "edited", "drift"]})

    assert processing_hash(edited) == processing_hash(wheat)
    assert metadata_hash(edited) != metadata_hash(wheat)

    entry = catalog_entry(root, edited)
    assert entry["is_stale"] is True
    assert entry["n_samples"] == 2  # processing_hash still matches -> stats not discarded


def test_processing_edit_drops_stale_stats(fleet: tuple[Path, dict[str, DatasetDescriptor]]) -> None:
    # Bumping the content version changes processing_hash, so the card is wholly stale and its
    # canonical-derived enrichment is dropped (n_samples falls back to the descriptor, which has none).
    root, descriptors = fleet
    wheat = descriptors["wheat"]
    bumped = wheat.model_copy(update={"versions": wheat.versions.model_copy(update={"content": "2.0.0"})})

    assert processing_hash(bumped) != processing_hash(wheat)

    entry = catalog_entry(root, bumped)
    assert entry["is_stale"] is True
    assert entry["n_samples"] is None
    assert entry["content_hash"] is None
    assert entry["card_protocol"] is None


# =============================================================================
# bank_summary — whole-bank aggregation
# =============================================================================
def test_bank_summary_aggregates(fleet: tuple[Path, dict[str, DatasetDescriptor]]) -> None:
    root, descriptors = fleet
    entries = [catalog_entry(root, d) for d in descriptors.values()]
    summary = bank_summary(entries)

    assert summary["n_datasets"] == 3
    assert summary["by_tier"] == {"private": 2, "public": 1}
    assert summary["n_multi_source"] == 1  # only wheat (X1+X2)
    assert summary["n_with_targets"] == 2  # wheat + barley
    assert summary["n_metadata_only"] == 1  # soil
    assert summary["n_with_split"] == 1  # wheat
    assert summary["by_spectro_family"] == {"NIR": 3}
    assert summary["by_domain"] == {"barley": 1, "soil": 1, "wheat": 1}
    assert summary["license_mix"]["CC-BY-4.0"] == 1
    assert summary["total_sources"] == 4  # 2 + 1 + 1

    # samples distribution: every dataset has 2 samples.
    assert summary["samples"] == {"min": 2, "median": 2, "max": 2, "total": 6}


def test_bank_summary_empty() -> None:
    summary = bank_summary([])
    assert summary["n_datasets"] == 0
    assert summary["samples"] is None
    assert summary["by_tier"] == {}


# =============================================================================
# build_catalog + load_catalog + search + get_card
# =============================================================================
def test_build_catalog_writes_index(fleet: tuple[Path, dict[str, DatasetDescriptor]]) -> None:
    root, _ = fleet
    catalog = build_catalog(root)

    assert catalog["schema_version"] == "2.0"
    assert catalog["n_datasets"] == 3
    assert "summary" in catalog
    assert {e["id"] for e in catalog["datasets"]} == {"wheat", "barley", "soil"}
    assert (root / "catalog" / "datasets.yaml").exists()

    # round-trips through the written index.
    loaded = load_catalog(root)
    assert len(loaded["datasets"]) == 3
    assert loaded["summary"]["n_datasets"] == 3


def test_build_catalog_no_write(fleet: tuple[Path, dict[str, DatasetDescriptor]]) -> None:
    root, _ = fleet
    (root / "catalog" / "datasets.yaml").unlink(missing_ok=True)
    catalog = build_catalog(root, write=False)
    assert catalog["n_datasets"] == 3
    assert not (root / "catalog" / "datasets.yaml").exists()


def test_search_filters(fleet: tuple[Path, dict[str, DatasetDescriptor]]) -> None:
    root, _ = fleet
    build_catalog(root)

    assert {e["id"] for e in search(root)} == {"wheat", "barley", "soil"}
    assert {e["id"] for e in search(root, tier="public")} == {"wheat"}
    assert {e["id"] for e in search(root, tier="private")} == {"barley", "soil"}
    assert {e["id"] for e in search(root, domain="wheat")} == {"wheat"}
    assert {e["id"] for e in search(root, spectro_family="NIR")} == {"wheat", "barley", "soil"}
    assert search(root, spectro_family="MIR") == []
    assert {e["id"] for e in search(root, has_target=True)} == {"wheat", "barley"}
    assert {e["id"] for e in search(root, has_target=False)} == {"soil"}
    # combined filters intersect.
    assert {e["id"] for e in search(root, tier="private", has_target=True)} == {"barley"}


def test_load_catalog_missing_index(tmp_path: Path) -> None:
    catalog = load_catalog(tmp_path)
    assert catalog["n_datasets"] == 0
    assert catalog["datasets"] == []


def test_get_card(fleet: tuple[Path, dict[str, DatasetDescriptor]]) -> None:
    root, _ = fleet
    card = get_card(root, "wheat")
    assert card is not None
    assert card["identity"]["id"] == "wheat"
    assert card["alignment"]["n_samples"] == 2
    assert get_card(root, "missing") is None
