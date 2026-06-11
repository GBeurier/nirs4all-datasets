"""Tests for catalog assembly and querying (no nirs4all)."""
from __future__ import annotations

import json
from pathlib import Path

from nirs4all_datasets.catalog import build_catalog, get_card, load_catalog, search


def test_build_catalog_enriches_from_card(registry: Path) -> None:
    catalog = build_catalog(registry)
    assert catalog["n_datasets"] == 1
    entry = catalog["datasets"][0]
    assert entry["id"] == "corn"
    assert entry["task_type"] == "regression"
    assert entry["n_samples"] == 80  # from the card
    assert entry["signal_type"] == "absorbance"
    assert entry["content_hash"] == "abc123"
    assert entry["has_card"] is True and entry["has_manifest"] is True
    assert entry["is_stale"] is False
    assert entry["publishable"] is True
    assert (registry / "catalog" / "datasets.yaml").exists()


def test_stale_card_is_flagged_and_ignored(registry: Path) -> None:
    card_path = registry / "datasets" / "corn" / "card.json"
    card = json.loads(card_path.read_text())
    card["integrity"]["descriptor_hash"] = "0" * 64  # no longer matches the descriptor
    card_path.write_text(json.dumps(card))
    entry = build_catalog(registry)["datasets"][0]
    assert entry["is_stale"] is True
    assert entry["signal_type"] is None  # stale enrichment ignored
    assert entry["n_samples"] is None  # falls back to the descriptor (which declares none)


def test_metadata_stale_card_is_flagged_but_stats_trusted(registry: Path) -> None:
    # Canonical is unchanged (descriptor_hash matches) but provenance was edited (metadata_hash differs):
    # the card must be flagged stale, yet its canonical-derived enrichment stays trusted.
    card_path = registry / "datasets" / "corn" / "card.json"
    card = json.loads(card_path.read_text())
    card["integrity"]["metadata_hash"] = "0" * 64
    card_path.write_text(json.dumps(card))
    entry = build_catalog(registry)["datasets"][0]
    assert entry["is_stale"] is True
    assert entry["n_samples"] == 80  # descriptor_hash still matches -> stats not discarded


def test_load_and_search(registry: Path) -> None:
    build_catalog(registry)
    assert len(load_catalog(registry)["datasets"]) == 1
    assert len(search(registry, task_type="regression")) == 1
    assert len(search(registry, task_type="classification")) == 0
    assert len(search(registry, visibility="public")) == 1
    assert len(search(registry, signal_type="reflectance")) == 0


def test_get_card(registry: Path) -> None:
    assert get_card(registry, "corn")["inventory"]["n_samples"] == 80
    assert get_card(registry, "missing") is None


def test_card_metadata_fresh_helper(tmp_path: Path, descriptor) -> None:  # noqa: ANN001 - fixture
    """The shared freshness check used by `add`/`build-all` to rebuild cards on metadata-only edits."""
    from nirs4all_datasets.manifest import metadata_hash
    from nirs4all_datasets.qualify.profile import card_metadata_fresh

    card_path = tmp_path / "card.json"
    assert card_metadata_fresh(card_path, descriptor) is False  # missing -> rebuild
    card_path.write_text(json.dumps({"integrity": {"metadata_hash": metadata_hash(descriptor)}}), encoding="utf-8")
    assert card_metadata_fresh(card_path, descriptor) is True
    card_path.write_text(json.dumps({"integrity": {"metadata_hash": "0" * 64}}), encoding="utf-8")
    assert card_metadata_fresh(card_path, descriptor) is False  # provenance edited
    card_path.write_text(json.dumps({"integrity": {}}), encoding="utf-8")
    assert card_metadata_fresh(card_path, descriptor) is False  # legacy card without it -> rebuild
