"""Tests for the schema-2.0 identity-card builder (``qualify.profile``).

Hermetic: every dataset is built by the ``canonical_dataset`` fixture (a real ``canonical/`` +
``manifest.json`` from a synthetic v2.0 leaf), so the card is derived from real canonical Parquet —
no network, no nirs4all-version dependence for the card shape itself.
"""
from __future__ import annotations

import json
from collections.abc import Iterable
from typing import Any

from nirs4all_datasets.qualify.profile import build_card, card_metadata_fresh, qualify

# The documented top-level card contract (build_card output).
_CARD_KEYS = {
    "schema_version",
    "protocol_version",
    "generated_at",
    "identity",
    "versions",
    "alignment",
    "sources",
    "variables",
    "splits",
    "provenance",
    "integrity",
    "governance",
    "assets",
    "warnings",
}

# Per-source spectral keys.
_SPECTRAL_KEYS = {"value_min", "value_max", "mean_min", "mean_max", "n_outliers", "pca"}

# Per-variable stats keys (by declared type).
_NUMERIC_STATS_KEYS = {"n", "n_missing", "min", "max", "mean", "std", "median", "q1", "q3"}
_CATEGORICAL_STATS_KEYS = {"n", "n_missing", "n_classes", "top_classes"}


def _vars_by_name(card: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {v["name"]: v for v in card["variables"]}


def _no_nonfinite_floats(obj: Any) -> Iterable[float]:
    """Yield every non-finite float reachable in ``obj`` (should be empty after sanitization)."""
    import math

    if isinstance(obj, bool):
        return
    if isinstance(obj, float):
        if not math.isfinite(obj):
            yield obj
        return
    if isinstance(obj, dict):
        for value in obj.values():
            yield from _no_nonfinite_floats(value)
    elif isinstance(obj, (list, tuple)):
        for value in obj:
            yield from _no_nonfinite_floats(value)


def test_build_card_multi_source_targets_and_metadata(canonical_dataset: Any) -> None:
    # corn: 3 spectral sources, sample-aligned; Moisture (numeric target) + variety (categorical
    # target) + a metadata var; a native train/test split.
    dataset_dir, descriptor = canonical_dataset(
        "corn",
        blocks=("X1", "X2", "X3"),
        sample_of={"o1": "s1", "o2": "s2"},
        targets={"Moisture": "numeric", "variety": "categorical"},
        extra_meta=("note_field",),
        split={"o1": "calibration", "o2": "test"},
    )
    card = build_card(dataset_dir, descriptor, compute_assets=False, compute_pca=True)

    # --- top-level contract: exactly the documented key set ---
    assert set(card) == _CARD_KEYS
    assert card["schema_version"] == "2.0"
    assert card["protocol_version"]
    assert card["identity"]["id"] == "corn"

    # --- sources: one per spectral block, finite spectral stats, pca present (dict or null) ---
    assert len(card["sources"]) == 3
    assert {s["source_id"] for s in card["sources"]} == {"X1", "X2", "X3"}
    for source in card["sources"]:
        spectral = source["spectral"]
        assert set(spectral) == _SPECTRAL_KEYS
        assert spectral["pca"] is None or isinstance(spectral["pca"], dict)

    # --- no NaN/Inf reaches JSON (recursively + via json.dumps allow_nan=False) ---
    assert not list(_no_nonfinite_floats(card))
    json.dumps(card, allow_nan=False)  # must not raise

    # --- variables: both targets + the metadata var, with the right stats shape ---
    variables = _vars_by_name(card)
    assert {"Moisture", "variety", "note_field"} <= set(variables)
    assert variables["Moisture"]["type"] == "numeric"
    assert variables["Moisture"]["role"] == "target"
    assert set(variables["Moisture"]["stats"]) == _NUMERIC_STATS_KEYS
    assert variables["variety"]["type"] == "categorical"
    assert variables["variety"]["role"] == "target"
    assert set(variables["variety"]["stats"]) == _CATEGORICAL_STATS_KEYS
    assert isinstance(variables["variety"]["stats"]["top_classes"], list)
    assert variables["note_field"]["role"] == "metadata"
    assert set(variables["note_field"]["stats"]) == _NUMERIC_STATS_KEYS

    # --- splits: native split partition counts ---
    assert len(card["splits"]) == 1
    split = card["splits"][0]
    assert split["name"] == "original"
    assert split["applied"] is False
    assert sum(split["partitions"].values()) == 2  # one calibration + one test sample

    # --- integrity: all three hashes present ---
    assert set(card["integrity"]) >= {"processing_hash", "metadata_hash", "content_hash"}
    assert card["integrity"]["processing_hash"]
    assert card["integrity"]["metadata_hash"]
    assert card["integrity"]["content_hash"]


def test_build_card_categorical_target(canonical_dataset: Any) -> None:
    # Categorical target only: variety is typed categorical, gets the categorical stats shape.
    dataset_dir, descriptor = canonical_dataset(
        "varieties",
        sample_of={"o1": "s1", "o2": "s2"},
        targets={"variety": "categorical"},
    )
    card = build_card(dataset_dir, descriptor, compute_assets=False, compute_pca=False)

    assert set(card) == _CARD_KEYS
    variables = _vars_by_name(card)
    assert variables["variety"]["type"] == "categorical"
    assert variables["variety"]["role"] == "target"
    stats = variables["variety"]["stats"]
    assert set(stats) == _CATEGORICAL_STATS_KEYS
    assert stats["n_classes"] >= 1
    assert all({"name", "count"} <= set(entry) for entry in stats["top_classes"])
    # compute_pca=False -> every source's pca is null.
    assert all(source["spectral"]["pca"] is None for source in card["sources"])
    json.dumps(card, allow_nan=False)


def test_build_card_x_only_has_no_variables(canonical_dataset: Any) -> None:
    # X-only dataset (no Y columns, no metadata): variables is empty, splits empty.
    dataset_dir, descriptor = canonical_dataset("xonly", sample_of=None, targets={})
    card = build_card(dataset_dir, descriptor, compute_assets=False)

    assert set(card) == _CARD_KEYS
    assert card["variables"] == []
    assert card["splits"] == []
    assert len(card["sources"]) == 1
    json.dumps(card, allow_nan=False)


def test_qualify_writes_artifacts_and_freshness(canonical_dataset: Any) -> None:
    dataset_dir, descriptor = canonical_dataset("corn", sample_of={"o1": "s1", "o2": "s2"})
    card = qualify(dataset_dir, descriptor, compute_assets=False, compute_pca=False)

    # qualify writes the full artifact set.
    assert (dataset_dir / "card.json").exists()
    assert (dataset_dir / "card.md").exists()  # Datasheets-for-Datasets
    assert (dataset_dir / "croissant.json").exists()  # MLCommons Croissant JSON-LD

    # the written card.json is finite, valid JSON.
    written = json.loads((dataset_dir / "card.json").read_text(encoding="utf-8"))
    assert written["identity"]["id"] == "corn"
    assert set(written) == _CARD_KEYS
    assert json.loads((dataset_dir / "croissant.json").read_text(encoding="utf-8"))["@type"] == "sc:Dataset"
    assert card["identity"]["id"] == "corn"

    # fresh right after qualify; stale after a metadata-only descriptor edit.
    assert card_metadata_fresh(dataset_dir, descriptor) is True
    edited = descriptor.model_copy(update={"keywords": ["nir", "edited", "metadata"]})
    assert card_metadata_fresh(dataset_dir, edited) is False
    # accepts the card.json path directly too.
    assert card_metadata_fresh(dataset_dir / "card.json", descriptor) is True
