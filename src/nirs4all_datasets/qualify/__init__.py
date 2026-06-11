"""Dataset qualification: descriptive metrics, an extensible metric registry, plots, and the
schema-2.0 identity ``card.json`` (built directly from the canonical Parquet)."""
from __future__ import annotations

from nirs4all_datasets.qualify.metrics import class_balance, distribution_shape, spectral_quality, wavelength_spacing
from nirs4all_datasets.qualify.profile import build_card, card_metadata_fresh, qualify, write_card
from nirs4all_datasets.qualify.registry import PROTOCOL_VERSION, metrics_for, register

__all__ = [
    "PROTOCOL_VERSION",
    "build_card",
    "card_metadata_fresh",
    "class_balance",
    "distribution_shape",
    "metrics_for",
    "qualify",
    "register",
    "spectral_quality",
    "wavelength_spacing",
    "write_card",
]
