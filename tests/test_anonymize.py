"""Tests for the anonymized-tier transform (opaque names + z-scored numeric targets; no nirs4all in the
asserts, but the card is built from a real canonical dataset)."""
from __future__ import annotations

import json
import math
from typing import Any

import pandas as pd

from nirs4all_datasets.qualify.anonymize import anonymize_card, anonymize_variables
from nirs4all_datasets.qualify.profile import qualify


def test_anonymize_variables_zscores_numeric_targets_and_renames(canonical_dataset: Any) -> None:
    """Numeric TARGET columns are z-scored (mean ~0, std ~1); columns are renamed to ``var_NNN`` in
    order; the ``sample_id`` join key is kept verbatim and not numbered."""
    _, desc = canonical_dataset("corn", blocks=("X1",), sample_of={"o1": "s1", "o2": "s2"})
    # `Moisture` is a numeric target, `variety` a categorical target (from the v2_leaf default targets).
    df = pd.DataFrame(
        {
            "sample_id": ["s1", "s2", "s3", "s4"],
            "Moisture": [1.0, 2.0, 3.0, 4.0],
            "variety": ["a", "b", "a", "c"],
        }
    )
    out, name_map = anonymize_variables(df, desc)

    # Rename: every variable column -> a generic slot, left-to-right order preserved; sample_id kept.
    assert name_map == {"Moisture": "var_001", "variety": "var_002"}
    assert list(out.columns) == ["sample_id", "var_001", "var_002"]
    assert list(out["sample_id"]) == ["s1", "s2", "s3", "s4"]  # join key verbatim

    # Numeric target is z-scored over finite values (population std): mean ~ 0, std ~ 1.
    z = out["var_001"].astype("float64")
    assert math.isclose(float(z.mean()), 0.0, abs_tol=1e-9)
    assert math.isclose(float(z.std(ddof=0)), 1.0, abs_tol=1e-9)

    # Categorical target is left untouched (only numeric targets are z-scored).
    assert list(out["var_002"]) == ["a", "b", "a", "c"]

    # The input frame is not mutated.
    assert list(df.columns) == ["sample_id", "Moisture", "variety"]


def test_anonymize_variables_constant_numeric_is_all_zero_no_nan(canonical_dataset: Any) -> None:
    """A constant numeric target (std == 0) becomes all-zeros — no NaN, no leaked location."""
    _, desc = canonical_dataset("corn", blocks=("X1",), sample_of={"o1": "s1", "o2": "s2"})
    df = pd.DataFrame({"sample_id": ["s1", "s2", "s3"], "Moisture": [5.0, 5.0, 5.0], "variety": ["a", "a", "a"]})
    out, _ = anonymize_variables(df, desc)
    z = out["var_001"].astype("float64")
    assert list(z) == [0.0, 0.0, 0.0]
    assert not z.isna().any()


def test_anonymize_variables_deterministic(canonical_dataset: Any) -> None:
    """The transform is pure/deterministic — the same input yields an identical output twice."""
    _, desc = canonical_dataset("corn", blocks=("X1",), sample_of={"o1": "s1", "o2": "s2"})
    df = pd.DataFrame(
        {"sample_id": ["s1", "s2", "s3"], "Moisture": [1.5, float("nan"), 4.5], "variety": ["a", "b", "a"]}
    )
    out1, map1 = anonymize_variables(df, desc)
    out2, map2 = anonymize_variables(df, desc)
    assert map1 == map2
    pd.testing.assert_frame_equal(out1, out2)


def test_anonymize_card_leaks_no_identifying_text(canonical_dataset: Any) -> None:
    """No original variable name, no dataset name, and no identifying free text survives anywhere in the
    serialized anonymized card."""
    dataset_dir, desc = canonical_dataset("corn", blocks=("X1", "X2"), sample_of={"o1": "s1", "o2": "s2"})
    card = qualify(dataset_dir, desc, compute_assets=False, compute_pca=False)

    anon = anonymize_card(card)
    serialized = json.dumps(anon)

    # Original variable names must be gone (replaced by var_NNN slots).
    for var in desc.variables:
        assert var.name not in serialized

    # The dataset display name + other identifying free text must be gone. (The opaque slug ``id`` is
    # intentionally kept and reused as the display name — it is the public Dataverse/URL identity.)
    leakage = [desc.name, desc.description, desc.provenance.contributor]
    leakage.extend(src.instrument_name for src in desc.sources if src.instrument_name)
    leakage.extend(o.title for o in desc.origin_sources if o.title)
    leakage.extend(p.title for p in desc.publications if p.title)
    for needle in leakage:
        assert needle and needle not in serialized, f"identifying text leaked: {needle!r}"

    # The free-text identity is masked structurally: description masked, keywords dropped, name == id.
    assert anon["identity"]["description"] != desc.description
    assert anon["identity"]["keywords"] == []
    assert anon["identity"]["name"] == anon["identity"]["id"]

    # Variable columns are renamed to opaque slots in order; the input card is not mutated.
    assert [v["name"] for v in anon["variables"]] == ["var_001", "var_002"]
    assert [v["name"] for v in card["variables"]] == ["Moisture", "variety"]


def test_anonymize_card_numeric_stats_are_range_free(canonical_dataset: Any) -> None:
    """A numeric variable's anonymized stats expose no location/scale — only normalized mean0/std1."""
    dataset_dir, desc = canonical_dataset("corn", blocks=("X1",), sample_of={"o1": "s1", "o2": "s2"})
    card = qualify(dataset_dir, desc, compute_assets=False, compute_pca=False)
    anon = anonymize_card(card)

    numeric = next(v for v in anon["variables"] if v["type"] == "numeric")
    stats = numeric["stats"]
    # Location/scale fields are dropped (None); mean/std are either null (no data) or normalized.
    for field in ("min", "max", "median", "q1", "q3"):
        assert stats[field] is None
    assert stats["mean"] in (None, 0.0)
    assert stats["std"] in (None, 1.0)
