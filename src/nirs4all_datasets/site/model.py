"""Tier-aware view models: load ``catalog/datasets.yaml`` + per-dataset cards (pure reads).

This is the load-bearing tier-gating layer. It reads the already-generated artifacts and decides,
per dataset, *which* card to serve and *what* may be shown:

* ``public``  -> the full ``card.json``; per-source/per-variable plots, value stats, and byte-free
  metadata downloads (``card.json`` / ``croissant.json``) are exposed.
* ``private`` -> the full ``card.json`` (it holds no bytes), plots, and stats — but **no** byte
  download, and no card/croissant download buttons that imply open bytes.
* ``anonymized`` -> ``card.anon.json`` (masked ``var_NNN`` names, normalized Y). Per-variable PNG
  assets are **never** served (their filenames embed real names) and the description/keywords/
  contributor are never printed; only structure + normalized stats.

No tier ever serves the dataset bytes — the site links to origins/DOI. The catalog index summary is
passed through verbatim (it is whole-bank aggregate, computed upstream by ``catalog.bank_summary``).
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

PUBLIC, PRIVATE, ANONYMIZED = "public", "private", "anonymized"


@dataclass
class DatasetView:
    """A tier-resolved view of one dataset: the index entry + the card the tier permits + flags."""

    entry: dict[str, Any]
    tier: str
    card: dict[str, Any] | None  # the card chosen for this tier (anon for anonymized), or None if cardless
    has_card: bool
    # tier-gated affordances
    show_value_stats: bool
    show_variable_plots: bool
    show_byte_download: bool  # always False — bytes never served
    show_metadata_downloads: bool  # card.json / croissant.json links (public only)
    asset_dataset_id: str  # which datasets/<id>/assets to copy from (empty => copy none)

    @property
    def id(self) -> str:
        return str(self.entry["id"])

    @property
    def name(self) -> str:
        if self.card and self.card.get("identity", {}).get("name"):
            return str(self.card["identity"]["name"])
        return str(self.entry.get("name") or self.entry["id"])

    @property
    def is_stale(self) -> bool:
        return bool(self.entry.get("is_stale"))

    @property
    def description(self) -> str:
        """Description, gated: anonymized never prints the original description."""
        if self.tier == ANONYMIZED or not self.card:
            return ""
        return str(self.card.get("identity", {}).get("description") or "")

    @property
    def keywords(self) -> list[str]:
        if self.tier == ANONYMIZED or not self.card:
            return []
        return list(self.card.get("identity", {}).get("keywords") or [])


@dataclass
class Catalog:
    """The whole-bank view model: the verbatim index summary + a tier-resolved view per dataset."""

    root: Path
    schema_version: str
    summary: dict[str, Any]
    datasets: list[DatasetView] = field(default_factory=list)


def _read_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
    return data


def _dataset_view(root: Path, entry: dict[str, Any]) -> DatasetView:
    """Resolve one catalog entry into its tier-gated view (choose card.anon for anonymized)."""
    dataset_id = str(entry["id"])
    tier = str(entry.get("tier") or PUBLIC)
    dataset_dir = root / "datasets" / dataset_id

    # A stale card holds wrong stats for the current descriptor; treat it as no card (render the
    # descriptor-only "card pending" state) so the site never advertises outdated facts.
    fresh_card = bool(entry.get("has_card")) and not entry.get("is_stale")

    card: dict[str, Any] | None = None
    asset_id = ""
    if fresh_card:
        if tier == ANONYMIZED:
            card = _read_json(dataset_dir / "card.anon.json")
            # anonymized never serves per-variable PNGs (filenames embed real names); we copy no assets
            asset_id = ""
        else:
            card = _read_json(dataset_dir / "card.json")
            asset_id = dataset_id if card is not None else ""

    return DatasetView(
        entry=entry,
        tier=tier,
        card=card,
        has_card=card is not None,
        show_value_stats=(tier != ANONYMIZED),
        show_variable_plots=(tier != ANONYMIZED),
        show_byte_download=False,
        show_metadata_downloads=(tier == PUBLIC),
        asset_dataset_id=asset_id,
    )


def load_catalog(root: str | Path) -> Catalog:
    """Load the catalog index + resolve a tier-aware view per dataset (pure reads; no recomputation)."""
    root = Path(root)
    raw = yaml.safe_load((root / "catalog" / "datasets.yaml").read_text(encoding="utf-8")) if (root / "catalog" / "datasets.yaml").exists() else {}
    raw = raw or {}
    entries: list[dict[str, Any]] = raw.get("datasets") or []
    views = [_dataset_view(root, e) for e in entries]
    return Catalog(
        root=root,
        schema_version=str(raw.get("schema_version") or "2.0"),
        summary=raw.get("summary") or {},
        datasets=views,
    )
