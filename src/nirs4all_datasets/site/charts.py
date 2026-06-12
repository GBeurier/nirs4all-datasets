"""Inline-SVG charts for the catalog — a restrained, scientific datasheet aesthetic.

Each chart's ``viewBox`` width is set to its intended *display* width (passed by the caller), with
absolute ~12–13px type, so text renders at a legible, consistent size whether the chart sits in a
wide whole-bank panel or a narrow per-variable card (no upscaled-giant / downscaled-tiny fonts). One
restrained accent (spectral teal) carries quantitative charts; a muted sequential ramp is used only
where categories must be distinguished (donuts). Numbers are tabular monospace. Pure stdlib + the
escaping helpers — no nirs4all / pandas / matplotlib.
"""
from __future__ import annotations

import math
from typing import Any

from .escape import esc, num

# Spectral teal is the single-series accent (histograms / spectra / box / scree). A curated, MUTED
# multi-hue palette distinguishes categories (domains / families / donut slices) — varied + elegant,
# never a saturated rainbow.
ACCENT = "#0f766e"
INK = "#0f172a"
MUTED = "#64748b"
FAINT = "#94a3b8"
GRID = "#e6ebf1"
RAMP = ["#0f766e", "#3f6f9f", "#b7791f", "#9c5b6a", "#5b6abf", "#6e8b5a", "#8a5a83", "#2f8f8a", "#a4713e", "#566b8c"]


def _ramp(i: int) -> str:
    return RAMP[i % len(RAMP)]


def _svg(w: float, h: float, inner: str, *, title: str) -> str:
    return (
        f'<svg viewBox="0 0 {w:.0f} {h:.0f}" role="img" aria-label="{esc(title)}" '
        f'preserveAspectRatio="xMidYMid meet"><title>{esc(title)}</title>{inner}</svg>'
    )


def _empty(w: float, h: float, title: str, msg: str = "no data") -> str:
    return _svg(w, h, f'<text x="{w / 2:.0f}" y="{h / 2:.0f}" text-anchor="middle" font-size="13" fill="{FAINT}">{esc(msg)}</text>', title=title)


def _clip(label: str, n: int) -> str:
    s = str(label)
    return s if len(s) <= n else s[: n - 1] + "…"


def _finite(seq: list[Any]) -> list[float]:
    return [float(v) for v in seq if v is not None and isinstance(v, bool) is False and (isinstance(v, (int, float)) and math.isfinite(v))]


def _ok(v: Any) -> bool:
    return v is not None and isinstance(v, bool) is False and isinstance(v, (int, float)) and math.isfinite(v)


# =============================================================================
# Horizontal bar chart — single accent, consistent rows, readable labels
# =============================================================================
def bar_chart(items: list[tuple[str, float]], *, title: str, top_n: int | None = None, unit: str = "", width: float = 520) -> str:
    """Horizontal bars from ``(label, value)``, one accent colour, value labels in mono."""
    rows = [(str(k), float(v)) for k, v in items if _ok(v)]
    rows.sort(key=lambda kv: -kv[1])
    if top_n is not None and len(rows) > top_n:
        rest = sum(v for _, v in rows[top_n:])
        rows = rows[:top_n] + [(f"+{len(items) - top_n} more", rest)]
    if not rows:
        return _empty(width, 80, title)

    row_h, gap, pad_t = 26, 9, 6
    label_w = min(width * 0.36, 190)
    val_w = 56
    bar_w = width - label_w - val_w - 14
    height = pad_t * 2 + len(rows) * (row_h + gap)
    vmax = max(v for _, v in rows) or 1
    parts: list[str] = []
    for i, (label, value) in enumerate(rows):
        y = pad_t + i * (row_h + gap)
        w = max(3.0, (value / vmax) * bar_w)
        parts.append(
            f'<text x="{label_w - 10:.0f}" y="{y + row_h / 2 + 4:.0f}" text-anchor="end" font-size="12.5" fill="{INK}" class="lbl">{esc(_clip(label, 30))}</text>'
            f'<rect class="barm" x="{label_w:.0f}" y="{y:.0f}" width="{w:.1f}" height="{row_h}" rx="3" fill="{_ramp(i)}"></rect>'
            f'<text x="{label_w + w + 7:.1f}" y="{y + row_h / 2 + 4:.0f}" font-size="12" fill="{MUTED}" class="numt">{num(value)}{esc(unit)}</text>'
        )
    return _svg(width, height, "".join(parts), title=title)


# =============================================================================
# Donut — restrained ramp, centred total, side legend
# =============================================================================
def _polar(cx: float, cy: float, r: float, frac: float) -> tuple[float, float]:
    ang = frac * 2 * math.pi - math.pi / 2
    return cx + r * math.cos(ang), cy + r * math.sin(ang)


def donut_chart(items: list[tuple[str, float]], *, title: str, width: float = 500) -> str:
    """Donut from ``(label, value)`` with a restrained ramp, centred total + a legible legend."""
    rows = [(str(k), float(v)) for k, v in sorted(items, key=lambda kv: -kv[1]) if _ok(v) and v > 0]
    total = sum(v for _, v in rows)
    if total <= 0:
        return _empty(width, 200, title)
    height = max(210, 36 + len(rows) * 24)
    cx, cy, r, rin = 108, height / 2, 88, 56
    arcs: list[str] = []
    acc = 0.0
    for i, (label, value) in enumerate(rows):
        f0, f1 = acc / total, (acc + value) / total
        acc += value
        if f1 - f0 >= 0.9999:
            arcs.append(f'<circle cx="{cx}" cy="{cy:.0f}" r="{(r + rin) / 2:.0f}" fill="none" stroke="{_ramp(i)}" stroke-width="{r - rin}"><title>{esc(label)}: {num(value)}</title></circle>')
            continue
        x0, y0 = _polar(cx, cy, r, f0)
        x1, y1 = _polar(cx, cy, r, f1)
        xi0, yi0 = _polar(cx, cy, rin, f0)
        xi1, yi1 = _polar(cx, cy, rin, f1)
        large = 1 if (f1 - f0) > 0.5 else 0
        d = f"M{x0:.2f},{y0:.2f} A{r},{r} 0 {large} 1 {x1:.2f},{y1:.2f} L{xi1:.2f},{yi1:.2f} A{rin},{rin} 0 {large} 0 {xi0:.2f},{yi0:.2f} Z"
        arcs.append(f'<path class="seg" d="{d}" fill="{_ramp(i)}"><title>{esc(label)}: {num(value)} ({value / total * 100:.0f}%)</title></path>')
    center = (
        f'<text x="{cx}" y="{cy - 2:.0f}" text-anchor="middle" font-size="26" font-weight="700" fill="{INK}" class="numt">{num(int(total))}</text>'
        f'<text x="{cx}" y="{cy + 16:.0f}" text-anchor="middle" font-size="11" fill="{MUTED}">total</text>'
    )
    legend = []
    lx = 2 * cx + 8
    for i, (label, value) in enumerate(rows):
        ly = (height - len(rows) * 24) / 2 + 16 + i * 24
        legend.append(
            f'<rect x="{lx}" y="{ly - 11:.0f}" width="11" height="11" rx="2.5" fill="{_ramp(i)}"></rect>'
            f'<text x="{lx + 18}" y="{ly:.0f}" font-size="12.5" fill="{INK}" class="lbl">{esc(_clip(label, 22))}</text>'
            f'<text x="{width - 6:.0f}" y="{ly:.0f}" text-anchor="end" font-size="12" fill="{MUTED}" class="numt">{num(value)}</text>'
        )
    return _svg(width, height, f"{''.join(arcs)}{center}{''.join(legend)}", title=title)


# =============================================================================
# Histogram from precomputed bins (per-variable distribution)
# =============================================================================
def histogram_bins(edges: list[float], counts: list[int], *, title: str, x_label: str = "", unit: str = "", width: float = 440, int_x: bool = False) -> str:
    """Bar histogram from precomputed ``edges`` (n+1) + ``counts`` (n); per-bar range on hover.

    ``int_x`` rounds the x-axis tick labels to integers (for count distributions like samples /
    wavelengths, whose log-spaced bin edges are otherwise fractional)."""
    nb = len(counts)
    if nb < 1 or len(edges) != nb + 1:
        return _empty(width, 180, title, "not enough data")
    cmax = max(counts) or 1
    height = round(width * 0.52)
    pad_l, pad_b, pad_t, pad_r = 40, 30, 12, 12
    pw, ph = width - pad_l - pad_r, height - pad_b - pad_t
    bw = pw / nb
    parts: list[str] = [f'<line x1="{pad_l}" y1="{pad_t + ph:.0f}" x2="{width - pad_r:.0f}" y2="{pad_t + ph:.0f}" stroke="{GRID}"></line>']
    for i, c in enumerate(counts):
        h = (c / cmax) * ph
        x = pad_l + i * bw
        parts.append(
            f'<rect class="barm" x="{x + 0.6:.1f}" y="{pad_t + ph - h:.1f}" width="{max(0.8, bw - 1.2):.1f}" height="{h:.1f}" fill="{ACCENT}">'
            f'<title>{num(edges[i], nd=4)} – {num(edges[i + 1], nd=4)}{esc(unit)}: {c}</title></rect>'
        )
    for t in range(5):
        idx = round(t * nb / 4)
        lbl = num(int(round(edges[idx]))) if int_x else num(edges[idx], nd=4)
        parts.append(f'<text x="{pad_l + idx * bw:.0f}" y="{pad_t + ph + 18:.0f}" text-anchor="middle" font-size="11" fill="{MUTED}" class="numt">{lbl}</text>')
    parts.append(f'<text x="{pad_l - 6}" y="{pad_t + 10:.0f}" text-anchor="end" font-size="11" fill="{MUTED}" class="numt">{cmax}</text>')
    parts.append(f'<text x="{pad_l - 6}" y="{pad_t + ph:.0f}" text-anchor="end" font-size="11" fill="{MUTED}" class="numt">0</text>')
    if x_label:
        parts.append(f'<text x="{pad_l + pw / 2:.0f}" y="{height - 4:.0f}" text-anchor="middle" font-size="11" fill="{FAINT}">{esc(x_label)}</text>')
    return _svg(width, height, "".join(parts), title=title)


# =============================================================================
# Box-and-whisker (numeric 5-number summary)
# =============================================================================
def boxplot(stats: dict[str, Any], *, title: str, unit: str = "", width: float = 440) -> str:
    """Horizontal box-and-whisker from ``min,q1,median,q3,max`` + a mean marker."""
    vals = [stats.get(k) for k in ("min", "q1", "median", "q3", "max")]
    if not all(_ok(v) for v in vals) or vals[0] == vals[-1]:
        return _empty(width, 92, title, "no spread")
    vmin, q1, med, q3, vmax = (float(v) for v in vals)  # type: ignore[arg-type]
    span = (vmax - vmin) or 1.0
    height = 92
    pad = 16
    pw = width - pad * 2
    cy = 38

    def x(v: float) -> float:
        return pad + (v - vmin) / span * pw

    parts = [
        f'<line x1="{x(vmin):.1f}" y1="{cy}" x2="{x(vmax):.1f}" y2="{cy}" stroke="{ACCENT}" stroke-width="1.3" opacity="0.6"></line>',
        f'<line x1="{x(vmin):.1f}" y1="{cy - 8}" x2="{x(vmin):.1f}" y2="{cy + 8}" stroke="{ACCENT}" stroke-width="1.3"></line>',
        f'<line x1="{x(vmax):.1f}" y1="{cy - 8}" x2="{x(vmax):.1f}" y2="{cy + 8}" stroke="{ACCENT}" stroke-width="1.3"></line>',
        f'<rect x="{x(q1):.1f}" y="{cy - 13}" width="{max(2.0, x(q3) - x(q1)):.1f}" height="26" rx="3" fill="{ACCENT}" fill-opacity="0.16" stroke="{ACCENT}" stroke-width="1.1"><title>q1 {num(q1, nd=4)} – q3 {num(q3, nd=4)}</title></rect>',
        f'<line x1="{x(med):.1f}" y1="{cy - 13}" x2="{x(med):.1f}" y2="{cy + 13}" stroke="{ACCENT}" stroke-width="2.2"><title>median {num(med, nd=4)}</title></line>',
    ]
    mean = stats.get("mean")
    if isinstance(mean, (int, float)) and not isinstance(mean, bool) and math.isfinite(mean):
        parts.append(f'<circle cx="{x(float(mean)):.1f}" cy="{cy}" r="3.2" fill="#b08968"><title>mean {num(float(mean), nd=4)}</title></circle>')
    parts.append(f'<text x="{x(vmin):.1f}" y="{cy + 30}" text-anchor="start" font-size="11.5" fill="{MUTED}" class="numt">{num(vmin, nd=4)}{esc(unit)}</text>')
    parts.append(f'<text x="{x(vmax):.1f}" y="{cy + 30}" text-anchor="end" font-size="11.5" fill="{MUTED}" class="numt">{num(vmax, nd=4)}{esc(unit)}</text>')
    return _svg(width, height, "".join(parts), title=title)


# =============================================================================
# Spectra with quantile bands (per-source)
# =============================================================================
def spectra_quantile(curve: dict[str, list[float]], *, title: str, axis_label: str = "wavelength", unit: str = "", width: float = 860) -> str:
    """Mean spectrum with shaded q05–q95 / q25–q75 bands; per-wavelength hover readout."""
    axis = curve.get("axis") or []
    n = len(axis)
    if n < 2:
        return _empty(width, 300, title, "no spectral data")
    q05, q25, med, q75, q95 = (curve.get(k) or [] for k in ("q05", "q25", "median", "q75", "q95"))
    ally = _finite(q05) + _finite(q95) + _finite(med)
    if not ally:
        return _empty(width, 300, title, "no spectral data")
    lo, hi = min(ally), max(ally)
    if hi <= lo:
        hi = lo + 1.0
    amin, amax = float(axis[0]), float(axis[-1])
    aspan = (amax - amin) or 1.0
    height = round(width * 0.42)
    pad_l, pad_r, pad_t, pad_b = 52, 16, 14, 34
    pw, ph = width - pad_l - pad_r, height - pad_t - pad_b

    def px(a: float) -> float:
        return pad_l + (a - amin) / aspan * pw

    def py(v: float) -> float:
        return pad_t + (1.0 - (v - lo) / (hi - lo)) * ph

    def band(lower: list[float], upper: list[float]) -> str:
        up = " ".join(f"{px(axis[i]):.1f},{py(upper[i]):.1f}" for i in range(n) if _ok(upper[i]) and _ok(axis[i]))
        dn = " ".join(f"{px(axis[i]):.1f},{py(lower[i]):.1f}" for i in range(n - 1, -1, -1) if _ok(lower[i]) and _ok(axis[i]))
        return f"{up} {dn}"

    def line(values: list[float]) -> str:
        return " ".join(f"{px(axis[i]):.1f},{py(values[i]):.1f}" for i in range(n) if _ok(values[i]) and _ok(axis[i]))

    parts: list[str] = [
        f'<polygon points="{band(q05, q95)}" fill="{ACCENT}" fill-opacity="0.12"></polygon>',
        f'<polygon points="{band(q25, q75)}" fill="{ACCENT}" fill-opacity="0.24"></polygon>',
        f'<polyline points="{line(med)}" fill="none" stroke="{ACCENT}" stroke-width="1.8" stroke-linejoin="round"></polyline>',
    ]
    for t in range(3):
        v = lo + (hi - lo) * t / 2
        y = py(v)
        parts.append(f'<line x1="{pad_l}" y1="{y:.1f}" x2="{width - pad_r:.0f}" y2="{y:.1f}" stroke="{GRID}"></line>')
        parts.append(f'<text x="{pad_l - 7}" y="{y + 3:.1f}" text-anchor="end" font-size="11.5" fill="{MUTED}" class="numt">{num(v, nd=3)}</text>')
    for t in range(5):
        a = amin + aspan * t / 4
        parts.append(f'<text x="{px(a):.0f}" y="{height - 14:.0f}" text-anchor="middle" font-size="11.5" fill="{MUTED}" class="numt">{num(a, nd=4)}</text>')
    parts.append(f'<text x="{pad_l + pw / 2:.0f}" y="{height - 1:.0f}" text-anchor="middle" font-size="11.5" fill="{FAINT}">{esc(axis_label)}{(" / " + esc(unit)) if unit else ""}</text>')
    bw = pw / n
    for i in range(n):
        if not (_ok(med[i]) and _ok(q25[i]) and _ok(q75[i]) and _ok(axis[i])):
            continue
        parts.append(
            f'<rect x="{px(axis[i]) - bw / 2:.1f}" y="{pad_t}" width="{bw:.2f}" height="{ph:.0f}" fill="transparent">'
            f'<title>{num(axis[i], nd=5)}{esc(unit)} — median {num(med[i], nd=4)} (q25–q75 {num(q25[i], nd=4)}–{num(q75[i], nd=4)})</title></rect>'
        )
    return _svg(width, height, "".join(parts), title=title)


# =============================================================================
# PCA scree — variance per component (single accent)
# =============================================================================
def scree(evr: list[float], *, title: str = "PCA explained variance", width: float = 440, top: int = 10) -> str:
    """Explained-variance bars for the first ``top`` PCs (percent), single accent."""
    vals = _finite(list(evr))[:top]
    if not vals:
        return _empty(width, 180, title, "PCA unavailable")
    height = round(width * 0.5)
    pad_l, pad_b, pad_t, pad_r = 36, 28, 12, 10
    pw, ph = width - pad_l - pad_r, height - pad_b - pad_t
    n = len(vals)
    bw = pw / n
    vmax = max(vals) or 1
    parts = [f'<line x1="{pad_l}" y1="{pad_t + ph:.0f}" x2="{width - pad_r:.0f}" y2="{pad_t + ph:.0f}" stroke="{GRID}"></line>']
    cum = 0.0
    cumpts = []
    for i, v in enumerate(vals):
        h = (v / vmax) * ph
        x = pad_l + i * bw
        cum += v
        cumpts.append(f"{x + bw / 2:.1f},{pad_t + (1 - cum) * ph:.1f}")
        parts.append(
            f'<rect class="barm" x="{x + 1.5:.1f}" y="{pad_t + ph - h:.1f}" width="{max(1.0, bw - 3):.1f}" height="{h:.1f}" fill="{ACCENT}">'
            f'<title>PC{i + 1}: {v * 100:.1f}% (cumulative {cum * 100:.1f}%)</title></rect>'
            f'<text x="{x + bw / 2:.1f}" y="{pad_t + ph + 16:.0f}" text-anchor="middle" font-size="10.5" fill="{MUTED}">{i + 1}</text>'
        )
    parts.append(f'<polyline points="{" ".join(cumpts)}" fill="none" stroke="{FAINT}" stroke-width="1.3" stroke-dasharray="3 2"></polyline>')
    parts.append(f'<text x="{pad_l + pw / 2:.0f}" y="{height - 2:.0f}" text-anchor="middle" font-size="11" fill="{FAINT}">principal component · cumulative (dashed)</text>')
    return _svg(width, height, "".join(parts), title=title)


# =============================================================================
# Histogram of raw values (whole-bank distributions on the index)
# =============================================================================
def histogram(values: list[float], *, title: str, n_bins: int = 16, log: bool = False, x_label: str = "", width: float = 520, int_x: bool = False) -> str:
    """Histogram of ``values`` into ``n_bins`` (optionally log-spaced) — whole-bank index charts."""
    xs = _finite(values)
    xs = [v for v in xs if v > 0] if log else xs
    if len(xs) < 2:
        return _empty(width, 200, title, "not enough data")
    lo, hi = min(xs), max(xs)
    if hi <= lo:
        hi = lo + 1
    edges = [10 ** (math.log10(lo) + (math.log10(hi) - math.log10(lo)) * i / n_bins) for i in range(n_bins + 1)] if log else [lo + (hi - lo) * i / n_bins for i in range(n_bins + 1)]
    counts = [0] * n_bins
    for v in xs:
        j = min(n_bins - 1, next((b for b in range(n_bins) if v <= edges[b + 1]), n_bins - 1))
        counts[j] += 1
    return histogram_bins([float(e) for e in edges], counts, title=title, x_label=x_label, width=width, int_x=int_x)


# =============================================================================
# Wavelength coverage — one band per spectroscopy family (legible, with a legend)
# =============================================================================
def coverage_by_family(spans: list[dict[str, Any]], *, title: str, unit_label: str = "nm", width: float = 1040) -> str:
    """One band per spectroscopy *family*: the wavelength range it covers (min–max) + dataset count.

    ``spans`` must already be a single axis unit (the caller filters), so the shared x-axis is
    meaningful. Aggregating by family (≈6 rows) keeps every label legible — vs. one unreadable row per
    dataset. Bands have a visible minimum width.
    """
    from collections import defaultdict

    by_fam: dict[str, list[tuple[float, float]]] = defaultdict(list)
    for s in spans:
        if _ok(s.get("lo")) and _ok(s.get("hi")) and s["hi"] > s["lo"]:
            by_fam[str(s.get("family") or "other")].append((float(s["lo"]), float(s["hi"])))
    fams = sorted(by_fam.items(), key=lambda kv: -len(kv[1]))
    if not fams:
        return _empty(width, 120, title, "no wavelength axes")
    gmin = min(lo for _, sp in fams for lo, _ in sp)
    gmax = max(hi for _, sp in fams for _, hi in sp)
    span = (gmax - gmin) or 1.0
    label_w, row_h, gap, pad_t, pad_b = 160, 28, 16, 8, 34
    pw = width - label_w - 18
    height = pad_t + len(fams) * (row_h + gap) + pad_b
    parts: list[str] = []
    for i, (fam, sp) in enumerate(fams):
        lo = min(a for a, _ in sp)
        hi = max(b for _, b in sp)
        y = pad_t + i * (row_h + gap)
        x0 = label_w + (lo - gmin) / span * pw
        x1 = label_w + (hi - gmin) / span * pw
        w = max(6.0, x1 - x0)
        parts.append(
            f'<text x="{label_w - 12}" y="{y + row_h / 2 + 4:.0f}" text-anchor="end" font-size="13" fill="{INK}" class="lbl">{esc(_clip(fam, 18))}</text>'
            f'<rect class="barm" x="{x0:.1f}" y="{y:.0f}" width="{w:.1f}" height="{row_h}" rx="4" fill="{_ramp(i)}" opacity="0.88">'
            f'<title>{esc(fam)}: {num(lo)}–{num(hi)} {esc(unit_label)} across {len(sp)} dataset(s)</title></rect>'
            f'<text x="{label_w + x1 - x0 + 10 if (x1 - x0) > 6 else x0 + w + 10:.1f}" y="{y + row_h / 2 + 4:.0f}" font-size="11.5" fill="{MUTED}" class="numt">{num(lo)}–{num(hi)} · {len(sp)}</text>'
        )
    axis_y = pad_t + len(fams) * (row_h + gap)
    parts.append(f'<line x1="{label_w}" y1="{axis_y:.0f}" x2="{label_w + pw:.0f}" y2="{axis_y:.0f}" stroke="{GRID}"></line>')
    for t in range(5):
        val = gmin + span * t / 4
        x = label_w + pw * t / 4
        parts.append(f'<text x="{x:.0f}" y="{axis_y + 18:.0f}" text-anchor="middle" font-size="11.5" fill="{MUTED}" class="numt">{num(val)}</text>')
    parts.append(f'<text x="{label_w + pw / 2:.0f}" y="{height - 2:.0f}" text-anchor="middle" font-size="11.5" fill="{FAINT}">wavelength / {esc(unit_label)} · band = min–max coverage, then range · dataset count</text>')
    return _svg(width, height, "".join(parts), title=title)


# =============================================================================
# Stacked horizontal bars (structural mixes on the index)
# =============================================================================
def stacked_bars(rows: list[tuple[str, list[tuple[str, float]]]], *, title: str, width: float = 520) -> str:
    """A few labelled stacked bars; segment colours shared across rows via a legend."""
    seg_labels: list[str] = []
    for _, segs in rows:
        for label, _v in segs:
            if label not in seg_labels:
                seg_labels.append(label)
    color_for = {label: _ramp(i) for i, label in enumerate(seg_labels)}
    label_w, row_h, gap, pad_t = 96, 30, 20, 6
    bar_w = width - label_w - 14
    height = pad_t + len(rows) * (row_h + gap) + 24
    parts: list[str] = []
    for ri, (row_label, segs) in enumerate(rows):
        y = pad_t + ri * (row_h + gap)
        total = sum(v for _, v in segs if _ok(v)) or 1
        x = float(label_w)
        parts.append(f'<text x="{label_w - 10}" y="{y + row_h / 2 + 4:.0f}" text-anchor="end" font-size="12.5" fill="{INK}" class="lbl">{esc(row_label)}</text>')
        for label, value in segs:
            if not _ok(value) or value <= 0:
                continue
            w = (value / total) * bar_w
            cap = f'<text x="{x + w / 2:.1f}" y="{y + row_h / 2 + 4:.0f}" text-anchor="middle" font-size="11.5" fill="#fff" font-weight="600" class="numt">{num(value)}</text>' if w > 28 else ""
            parts.append(f'<rect x="{x:.1f}" y="{y:.0f}" width="{w:.1f}" height="{row_h}" fill="{color_for[label]}"><title>{esc(row_label)} · {esc(label)}: {num(value)}</title></rect>{cap}')
            x += w
    legend = "".join(f'<span><i style="background:{color_for[lbl]}"></i>{esc(lbl)}</span>' for lbl in seg_labels)
    return f'{_svg(width, height, "".join(parts), title=title)}<div class="legend">{legend}</div>'
