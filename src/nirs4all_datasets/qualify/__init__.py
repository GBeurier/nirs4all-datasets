"""Dataset qualification public API.

The exports are loaded lazily so the static-site renderer can import lightweight metric
documentation without pulling in the full qualification stack (pandas / canonical readers).
"""
from __future__ import annotations

from importlib import import_module
from typing import Any

_EXPORTS = {
    "PROTOCOL_VERSION": "nirs4all_datasets.qualify.registry",
    "build_card": "nirs4all_datasets.qualify.profile",
    "bug_method_catalog": "nirs4all_datasets.qualify.metrics",
    "card_metadata_fresh": "nirs4all_datasets.qualify.profile",
    "class_balance": "nirs4all_datasets.qualify.metrics",
    "diagnostic_hypotheses": "nirs4all_datasets.qualify.metrics",
    "distribution_shape": "nirs4all_datasets.qualify.metrics",
    "metric_catalog": "nirs4all_datasets.qualify.metrics",
    "metric_score_rows": "nirs4all_datasets.qualify.metrics",
    "metrics_for": "nirs4all_datasets.qualify.registry",
    "profile_score_labels": "nirs4all_datasets.qualify.metrics",
    "qualify": "nirs4all_datasets.qualify.profile",
    "register": "nirs4all_datasets.qualify.registry",
    "spectral_profile": "nirs4all_datasets.qualify.metrics",
    "spectral_quality": "nirs4all_datasets.qualify.metrics",
    "technology_guidance": "nirs4all_datasets.qualify.metrics",
    "wavelength_spacing": "nirs4all_datasets.qualify.metrics",
    "write_card": "nirs4all_datasets.qualify.profile",
}

__all__ = list(_EXPORTS)


def __getattr__(name: str) -> Any:
    if name not in _EXPORTS:
        raise AttributeError(name)
    module = import_module(_EXPORTS[name])
    value = getattr(module, name)
    globals()[name] = value
    return value
