"""Catalog spectroscopy labels and optical coverage over explicitly declared axes.

Raman shifts describe an energy difference, not an absolute optical wavenumber.
Technique labels and wavelength coverage therefore remain separate summaries.
"""
from __future__ import annotations

import math
from typing import Any


def wavelength_range_nm(source: dict[str, Any]) -> tuple[float, float] | None:
    """Convert a declared optical range to nm; never interpret Raman shifts as light wavelengths."""
    if str(source.get("modality") or "").strip().lower() == "raman":
        return None
    try:
        raw_lo, raw_hi = source.get("axis_min"), source.get("axis_max")
        if raw_lo is None or raw_hi is None or isinstance(raw_lo, bool) or isinstance(raw_hi, bool):
            return None
        lo, hi = sorted((float(raw_lo), float(raw_hi)))
    except (TypeError, ValueError):
        return None
    if not (math.isfinite(lo) and math.isfinite(hi) and lo > 0):
        return None
    unit = str(source.get("axis_unit") or "").strip().lower()
    if unit == "nm":
        return lo, hi
    if unit in {"cm-1", "cm^-1", "cm⁻¹", "1/cm"}:
        result = (1e7 / hi, 1e7 / lo)
        return result if all(math.isfinite(value) for value in result) else None
    return None


def optical_bands(source: dict[str, Any]) -> set[str]:
    """NIR/MIR bands overlapped by a known absolute axis; empty for unknown/non-overlapping axes."""
    span = wavelength_range_nm(source)
    if span is None:
        return set()
    lo, hi = span
    bands = set()
    if hi >= 780 and (lo < 2500 or lo == hi == 2500):
        bands.add("NIR")
    if hi > 2500 and lo <= 25000:
        bands.add("MIR")
    return bands


def spectroscopy_family(sources: list[dict[str, Any]]) -> str:
    """Group declared techniques, refining broad/unspecified labels only with a known optical axis."""
    families: set[str] = set()
    for source in sources:
        modality = str(source.get("modality") or "other")
        if modality in {"NIR", "MIR", "Raman", "UV-Vis"}:
            families.add(modality)
        elif modality == "VSWIR":
            families.add("NIR")
        elif modality == "TIR":
            families.add("MIR")
        else:
            families.update(optical_bands(source) or {"other"})
    return next(iter(families)) if len(families) == 1 else "mixed" if families else "other"
