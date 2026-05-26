"""Dataset qualification: descriptive metrics, plots, and the identity ``card.json``."""
from __future__ import annotations

from nirs4all_datasets.qualify.metrics import class_balance, distribution_shape, spectral_quality, wavelength_spacing

__all__ = ["class_balance", "distribution_shape", "spectral_quality", "wavelength_spacing"]
