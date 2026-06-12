"""Inline line-art SVG icons for the catalog cards — task type + detected spectral signal type.

Each value is a self-contained ``<svg>`` (24×24 viewBox, ``currentColor`` strokes, no fills, no text),
so the icon inherits its size + colour from CSS. The catalog renders a small legend (``ICON_LABELS``)
above the grid and one icon per card; ``icon(key)`` falls back to the neutral ``spectra`` glyph.
"""
from __future__ import annotations

_A = 'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"'

ICONS: dict[str, str] = {
    # ── task type ─────────────────────────────────────────────────────────────
    # scatter of points with a best-fit trend line → continuous prediction
    "regression": f'<svg {_A}><path d="M4 20 L20 6"/><circle cx="6" cy="17" r="1.1"/><circle cx="10" cy="15" r="1.1"/><circle cx="14" cy="9.5" r="1.1"/><circle cx="18" cy="9" r="1.1"/></svg>',
    # two separated clusters split by a boundary → discrete classes
    "classification": f'<svg {_A}><path d="M14 4 L9 20"/><circle cx="6" cy="8" r="1.1"/><circle cx="8.5" cy="11" r="1.1"/><circle cx="5.5" cy="13" r="1.1"/><circle cx="16" cy="10" r="1.1"/><circle cx="18.5" cy="14" r="1.1"/><circle cx="15" cy="16" r="1.1"/></svg>',
    # ── detected signal type ──────────────────────────────────────────────────
    # baseline with an upward absorption peak
    "absorbance": f'<svg {_A}><path d="M3 18 H8 C10 18 10 7 12 7 C14 7 14 18 16 18 H21"/></svg>',
    # ray hitting a surface and bouncing off (incidence + reflection)
    "reflectance": f'<svg {_A}><path d="M4 19 H20"/><path d="M7 5 L12 19 L17 5"/><path d="M14.5 8 L17 5 L14 4.5"/></svg>',
    # ray passing through a slab and out the far side
    "transmittance": f'<svg {_A}><path d="M9 6 V18"/><path d="M15 6 V18"/><path d="M3 12 H21"/><path d="M18 9.5 L21 12 L18 14.5"/></svg>',
    # concave log-shaped response (log(1/R))
    "log1r": f'<svg {_A}><path d="M4 19 C8 19 9 6 20 5"/><path d="M4 19 V5"/><path d="M4 19 H20"/></svg>',
    # two opposing flux arrows between scattering layers (Kubelka–Munk two-flux)
    "kubelka_munk": f'<svg {_A}><path d="M3 6 H21"/><path d="M3 18 H21"/><path d="M9 7 V17"/><path d="M7 9 L9 7 L11 9"/><path d="M15 7 V17"/><path d="M13 15 L15 17 L17 15"/></svg>',
    # neutral spectrum squiggle (auto / undetermined)
    "spectra": f'<svg {_A}><path d="M3 14 C6 14 6 9 9 9 C12 9 11 16 14 16 C17 16 17 8 21 11"/></svg>',
}

# Human labels for the legend (only the signal-type + task glyphs are explained there).
ICON_LABELS: dict[str, str] = {
    "regression": "regression",
    "classification": "classification",
    "absorbance": "absorbance",
    "reflectance": "reflectance",
    "transmittance": "transmittance",
    "log1r": "log(1/R)",
    "kubelka_munk": "Kubelka–Munk",
}

# Map a detected nirs4all signal-type value to an icon key.
_SIGNAL_KEY: dict[str, str] = {
    "absorbance": "absorbance",
    "reflectance": "reflectance",
    "reflectance%": "reflectance",
    "transmittance": "transmittance",
    "transmittance%": "transmittance",
    "log(1/r)": "log1r",
    "kubelka-munk": "kubelka_munk",
}


def icon(key: str) -> str:
    """The SVG for ``key`` (a task or icon key), or the neutral spectrum glyph if unknown."""
    return ICONS.get(key, ICONS["spectra"])


def signal_icon_key(signal_type: str) -> str:
    """Map a detected signal-type string to its icon key (neutral ``spectra`` when unrecognized)."""
    return _SIGNAL_KEY.get(str(signal_type).strip().lower(), "spectra")
