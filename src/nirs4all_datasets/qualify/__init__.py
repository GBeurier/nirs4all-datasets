"""Dataset qualification: descriptive metrics, an extensible metric registry, plots, and the
schema-2.0 identity ``card.json`` (built directly from the canonical Parquet)."""
from __future__ import annotations

from nirs4all_datasets.qualify.metrics import (
    bug_method_catalog,
    class_balance,
    diagnostic_hypotheses,
    distribution_shape,
    metric_catalog,
    metric_score_rows,
    profile_score_labels,
    spectral_profile,
    spectral_quality,
    technology_guidance,
    wavelength_spacing,
)
from nirs4all_datasets.qualify.profile import build_card, card_metadata_fresh, qualify, write_card
from nirs4all_datasets.qualify.registry import PROTOCOL_VERSION, metrics_for, register

__all__ = [
    "PROTOCOL_VERSION",
    "build_card",
    "bug_method_catalog",
    "card_metadata_fresh",
    "class_balance",
    "diagnostic_hypotheses",
    "distribution_shape",
    "metric_catalog",
    "metric_score_rows",
    "metrics_for",
    "profile_score_labels",
    "qualify",
    "register",
    "spectral_profile",
    "spectral_quality",
    "technology_guidance",
    "wavelength_spacing",
    "write_card",
]
