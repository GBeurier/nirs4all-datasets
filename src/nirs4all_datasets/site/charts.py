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
ACCENT_SOFT = "#0d9488"  # lighter teal companion for fills / hovers
INK = "#0f172a"
MUTED = "#64748b"
FAINT = "#94a3b8"
GRID = "#dde4ec"  # plot frame + axis ticks
GRID_SOFT = "#eef2f7"  # inner gridlines — kept lighter so the data reads first
PLOT_BG = "#ffffff"
RAMP = ["#0f766e", "#3f6f9f", "#b7791f", "#9c5b6a", "#5b6abf", "#6e8b5a", "#8a5a83", "#2f8f8a", "#a4713e", "#566b8c"]

# One type scale across every chart. Sizes are absolute px in the chart's own viewBox; since the SVG
# scales to its container, keeping them consistent (and ≥11) is what makes labels legible whether a
# chart sits in a wide bank panel or a narrow card.
FS_TICK = 11.0  # numeric axis ticks (tabular mono)
FS_AXIS = 11.5  # axis caption / footnote
FS_LABEL = 12.5  # category / row labels
FS_LEGEND = 11.5  # legend entries
FS_VALUE = 12.0  # inline value numbers


def _ramp(i: int) -> str:
    return RAMP[i % len(RAMP)]


def _svg(w: float, h: float, inner: str, *, title: str) -> str:
    return (
        f'<svg viewBox="0 0 {w:.0f} {h:.0f}" role="img" aria-label="{esc(title)}" '
        f'preserveAspectRatio="xMidYMid meet"><title>{esc(title)}</title>{inner}</svg>'
    )


def _empty(w: float, h: float, title: str, msg: str = "no data") -> str:
    pad = 10.0
    inner = (
        f'<rect x="{pad}" y="{pad}" width="{w - 2 * pad:.0f}" height="{h - 2 * pad:.0f}" rx="8" fill="{GRID_SOFT}" '
        f'fill-opacity="0.5" stroke="{GRID}" stroke-dasharray="4 4"></rect>'
        f'<text x="{w / 2:.0f}" y="{h / 2 + 4:.0f}" text-anchor="middle" font-size="{FS_AXIS}" fill="{FAINT}">{esc(msg)}</text>'
    )
    return _svg(w, h, inner, title=title)


def _clip(label: str, n: int) -> str:
    s = str(label)
    return s if len(s) <= n else s[: n - 1] + "…"


def _finite(seq: list[Any]) -> list[float]:
    return [float(v) for v in seq if v is not None and isinstance(v, bool) is False and (isinstance(v, (int, float)) and math.isfinite(v))]


def _ok(v: Any) -> bool:
    return v is not None and isinstance(v, bool) is False and isinstance(v, (int, float)) and math.isfinite(v)


def _finite_float(v: Any) -> float | None:
    return float(v) if _ok(v) else None


def _nice_step(raw: float) -> float:
    """Return a human-friendly step using the 1/2/2.5/5/10 progression."""
    if raw <= 0 or not math.isfinite(raw):
        return 1.0
    power = 10 ** math.floor(math.log10(raw))
    fraction = raw / power
    if fraction <= 1:
        nice = 1.0
    elif fraction <= 2:
        nice = 2.0
    elif fraction <= 2.5:
        nice = 2.5
    elif fraction <= 5:
        nice = 5.0
    else:
        nice = 10.0
    return float(nice * power)


def _linear_scale(lo: float, hi: float, *, target_ticks: int = 5, include_zero: bool = False) -> tuple[float, float, list[float], float]:
    """Nice linear domain + tick labels, so axes never expose raw min/max noise."""
    if not (math.isfinite(lo) and math.isfinite(hi)):
        return 0.0, 1.0, [0.0, 0.5, 1.0], 0.5
    if hi < lo:
        lo, hi = hi, lo
    if hi <= lo:
        pad = max(abs(lo) * 0.05, 0.5)
        lo, hi = lo - pad, hi + pad
    if include_zero:
        lo = min(lo, 0.0)
        hi = max(hi, 0.0)
    step = _nice_step((hi - lo) / max(target_ticks - 1, 1))
    start = math.floor(lo / step) * step
    end = math.ceil(hi / step) * step
    # Avoid domains made too loose by a single awkward endpoint.
    if start + step <= lo and (lo - start) > 0.92 * step:
        start += step
    if end - step >= hi and (end - hi) > 0.92 * step:
        end -= step
    if end <= start:
        end = start + step
    n = int(round((end - start) / step))
    ticks = [start + i * step for i in range(n + 1)]
    return start, end, ticks, step


def _looks_log_spaced(edges: list[float]) -> bool:
    vals = [float(v) for v in edges if _ok(v) and float(v) > 0]
    if len(vals) < 3 or len(vals) != len(edges):
        return False
    ratios = [vals[i + 1] / vals[i] for i in range(len(vals) - 1) if vals[i] > 0]
    if not ratios or max(ratios) <= 1.01:
        return False
    med = sorted(ratios)[len(ratios) // 2]
    return med > 1.01 and all(abs(r - med) / med < 0.08 for r in ratios)


def _log_scale(lo: float, hi: float, *, target_ticks: int = 6) -> tuple[float, float, list[float]]:
    """Nice log domain + ticks using 1/2/5 decades."""
    if lo <= 0 or hi <= 0 or not (math.isfinite(lo) and math.isfinite(hi)):
        return 1.0, 10.0, [1.0, 10.0]
    if hi < lo:
        lo, hi = hi, lo
    d0 = math.floor(math.log10(lo))
    d1 = math.ceil(math.log10(hi))
    start, end = 10 ** d0, 10 ** d1
    ticks: list[float] = []
    for exp in range(d0, d1 + 1):
        for mantissa in (1.0, 2.0, 5.0):
            v = mantissa * 10 ** exp
            if start <= v <= end:
                ticks.append(v)
    if len(ticks) > target_ticks + 2:
        ticks = [10 ** exp for exp in range(d0, d1 + 1)]
    return start, end, ticks


def _tick_label(value: float, *, step: float | None = None, integer: bool = False) -> str:
    """Format a tick with the decimals implied by the nice step."""
    if not math.isfinite(value):
        return "—"
    if integer:
        return f"{int(round(value)):,}"
    if step is None or step <= 0 or not math.isfinite(step):
        return num(value)
    if abs(value) < abs(step) * 1e-9:
        value = 0.0
    step_s = f"{abs(step):.12f}".rstrip("0").rstrip(".")
    decimals = len(step_s.split(".", 1)[1]) if "." in step_s else 0
    return f"{value:,.{decimals}f}"


def _x_tick_text(x: float, y: float, label: str, *, width: float, edge: float = 34.0) -> str:
    """Axis tick label that stays inside the SVG viewBox at the left/right edges."""
    anchor = "start" if x <= edge else "end" if x >= width - edge else "middle"
    return f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="{anchor}" font-size="{FS_TICK}" fill="{MUTED}" class="numt">{label}</text>'


def _legend_panel(entries: list[tuple[str, str, str]], *, right: float, top: float, opacity: float = 0.92) -> str:
    """A compact, self-sizing legend box whose top-right corner sits at ``(right, top)``.

    It measures its own width from the longest label so it never overflows the plot, and draws an
    opaque backdrop so swatches/text never collide with the data underneath. Each entry is
    ``(kind, color, label)`` where ``kind`` is ``line`` / ``dash`` / ``band`` / ``box``.
    """
    if not entries:
        return ""
    line_h, pad, swatch, gap = 17.0, 9.0, 18.0, 8.0
    longest = max(len(lbl) for _k, _c, lbl in entries)
    w = pad * 2 + swatch + gap + longest * (FS_LEGEND * 0.56)
    h = pad * 2 + len(entries) * line_h - (line_h - FS_LEGEND)
    x = right - w
    parts = [f'<rect x="{x:.1f}" y="{top:.1f}" width="{w:.1f}" height="{h:.1f}" rx="7" fill="#ffffff" fill-opacity="{opacity:.2f}" stroke="{GRID}"></rect>']
    sx = x + pad
    for i, (kind, color, label) in enumerate(entries):
        cy = top + pad + FS_LEGEND * 0.5 + i * line_h
        if kind == "box":
            parts.append(f'<rect x="{sx:.1f}" y="{cy - 5:.1f}" width="11" height="11" rx="2.5" fill="{color}"></rect>')
        elif kind == "band":
            parts.append(f'<rect x="{sx:.1f}" y="{cy - 5:.1f}" width="{swatch:.0f}" height="10" rx="2" fill="{color}" fill-opacity="0.32" stroke="{color}" stroke-opacity="0.55"></rect>')
        else:
            dash_attr = ' stroke-dasharray="3 2"' if kind == "dash" else ""
            parts.append(f'<line x1="{sx:.1f}" y1="{cy:.1f}" x2="{sx + swatch:.1f}" y2="{cy:.1f}" stroke="{color}" stroke-width="2.4"{dash_attr}></line>')
        parts.append(f'<text x="{sx + swatch + gap:.1f}" y="{cy + 3.5:.1f}" font-size="{FS_LEGEND}" fill="{MUTED}">{esc(label)}</text>')
    return "".join(parts)


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
        value_x = label_w + w + 7
        value_anchor = "start"
        if value_x > width - 6:
            value_x = width - 6
            value_anchor = "end"
        parts.append(
            f'<text x="{label_w - 10:.0f}" y="{y + row_h / 2 + 4:.0f}" text-anchor="end" font-size="{FS_LABEL}" fill="{INK}" class="lbl">{esc(_clip(label, 30))}</text>'
            f'<rect x="{label_w:.0f}" y="{y:.0f}" width="{bar_w:.1f}" height="{row_h}" rx="3.5" fill="{GRID_SOFT}"></rect>'
            f'<rect class="barm" x="{label_w:.0f}" y="{y:.0f}" width="{w:.1f}" height="{row_h}" rx="3.5" fill="{_ramp(i)}"><title>{esc(label)}: {num(value)}{esc(unit)}</title></rect>'
            f'<text x="{value_x:.1f}" y="{y + row_h / 2 + 4:.0f}" text-anchor="{value_anchor}" font-size="{FS_VALUE}" fill="{MUTED}" class="numt">{num(value)}{esc(unit)}</text>'
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
        f'<text x="{cx}" y="{cy + 17:.0f}" text-anchor="middle" font-size="10.5" letter-spacing="0.08em" fill="{MUTED}">TOTAL</text>'
    )
    legend = []
    lx = 2 * cx + 8
    for i, (label, value) in enumerate(rows):
        ly = (height - len(rows) * 24) / 2 + 16 + i * 24
        pct = value / total * 100
        legend.append(
            f'<rect x="{lx}" y="{ly - 11:.0f}" width="11" height="11" rx="2.5" fill="{_ramp(i)}"></rect>'
            f'<text x="{lx + 18}" y="{ly:.0f}" font-size="{FS_LABEL}" fill="{INK}" class="lbl">{esc(_clip(label, 22))}</text>'
            f'<text x="{width - 6:.0f}" y="{ly:.0f}" text-anchor="end" font-size="{FS_VALUE}" fill="{MUTED}" class="numt">{num(value)} · {pct:.0f}%</text>'
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
    pad_l, pad_b, pad_t, pad_r = 44, 30, 14, 14
    pw, ph = width - pad_l - pad_r, height - pad_b - pad_t
    # Count axis on nice, round, integer ticks — never raw cmax fractions (e.g. 0 / 1000 / 2001).
    _, y_top, y_ticks, _ = _linear_scale(0.0, float(cmax), target_ticks=4, include_zero=True)
    y_top = max(y_top, 1.0)
    edge_vals = [float(v) for v in edges]
    log_x = _looks_log_spaced(edge_vals)
    if log_x:
        x0, x1, x_ticks = _log_scale(edge_vals[0], edge_vals[-1])
        x_step = None

        def x_for(v: float) -> float:
            return pad_l + (math.log10(v) - math.log10(x0)) / (math.log10(x1) - math.log10(x0)) * pw

    else:
        x0, x1, x_ticks, x_step = _linear_scale(edge_vals[0], edge_vals[-1])

        def x_for(v: float) -> float:
            return pad_l + (v - x0) / (x1 - x0) * pw

    parts: list[str] = [f'<rect x="{pad_l}" y="{pad_t}" width="{pw:.0f}" height="{ph:.0f}" rx="3" fill="{PLOT_BG}" stroke="{GRID}" stroke-width="1"></rect>']
    for tick in y_ticks:
        if tick > y_top:
            continue
        y = pad_t + (1.0 - tick / y_top) * ph
        parts.append(f'<line x1="{pad_l}" y1="{y:.1f}" x2="{width - pad_r:.0f}" y2="{y:.1f}" stroke="{GRID_SOFT}"></line>')
        parts.append(f'<text x="{pad_l - 7}" y="{y + 3:.1f}" text-anchor="end" font-size="{FS_TICK}" fill="{MUTED}" class="numt">{num(int(round(tick)))}</text>')
    for i, c in enumerate(counts):
        h = (c / y_top) * ph
        x = x_for(edge_vals[i])
        x_next = x_for(edge_vals[i + 1])
        bw = x_next - x
        lo_txt = num(int(round(edges[i]))) if int_x else num(edges[i], nd=4)
        hi_txt = num(int(round(edges[i + 1]))) if int_x else num(edges[i + 1], nd=4)
        parts.append(
            f'<rect class="barm" x="{x + 0.6:.1f}" y="{pad_t + ph - h:.1f}" width="{max(0.8, bw - 1.2):.1f}" height="{h:.1f}" rx="1.5" fill="{ACCENT}">'
            f'<title>{lo_txt} – {hi_txt}{esc(unit)}: {c}</title></rect>'
        )
    for tick in x_ticks:
        if x0 <= tick <= x1:
            lbl = _tick_label(tick, step=x_step, integer=int_x)
            x = x_for(tick)
            parts.append(f'<line x1="{x:.0f}" y1="{pad_t + ph:.0f}" x2="{x:.0f}" y2="{pad_t + ph + 4:.0f}" stroke="{GRID}"></line>')
            parts.append(_x_tick_text(x, pad_t + ph + 18, lbl, width=width))
    if x_label:
        parts.append(f'<text x="{pad_l + pw / 2:.0f}" y="{height - 4:.0f}" text-anchor="middle" font-size="{FS_AXIS}" fill="{FAINT}">{esc(x_label)}</text>')
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
    height = 92
    pad = 16
    pw = width - pad * 2
    cy = 38
    x0, x1, ticks, step = _linear_scale(vmin, vmax)

    def x(v: float) -> float:
        return pad + (v - x0) / (x1 - x0) * pw

    parts = [
        f'<line x1="{x(vmin):.1f}" y1="{cy}" x2="{x(vmax):.1f}" y2="{cy}" stroke="{ACCENT}" stroke-width="1.3" opacity="0.6"></line>',
        f'<line x1="{x(vmin):.1f}" y1="{cy - 8}" x2="{x(vmin):.1f}" y2="{cy + 8}" stroke="{ACCENT}" stroke-width="1.3"></line>',
        f'<line x1="{x(vmax):.1f}" y1="{cy - 8}" x2="{x(vmax):.1f}" y2="{cy + 8}" stroke="{ACCENT}" stroke-width="1.3"></line>',
        f'<rect x="{x(q1):.1f}" y="{cy - 13}" width="{max(2.0, x(q3) - x(q1)):.1f}" height="26" rx="3" fill="{ACCENT}" fill-opacity="0.16" stroke="{ACCENT}" stroke-width="1.1"><title>q1 {num(q1, nd=4)} – q3 {num(q3, nd=4)}</title></rect>',
        f'<line x1="{x(med):.1f}" y1="{cy - 13}" x2="{x(med):.1f}" y2="{cy + 13}" stroke="{ACCENT}" stroke-width="2.2"><title>median {num(med, nd=4)}</title></line>',
    ]
    mean = stats.get("mean")
    if isinstance(mean, (int, float)) and not isinstance(mean, bool) and math.isfinite(mean):
        mx = x(float(mean))
        parts.append(f'<circle cx="{mx:.1f}" cy="{cy}" r="3.4" fill="#fff" stroke="#b7791f" stroke-width="2.2"><title>mean {num(float(mean), nd=4)}</title></circle>')
    for tick in ticks:
        parts.append(f'<line x1="{x(tick):.1f}" y1="{cy + 18}" x2="{x(tick):.1f}" y2="{cy + 22}" stroke="{GRID}"></line>')
        parts.append(_x_tick_text(x(tick), cy + 34, f"{_tick_label(tick, step=step)}{esc(unit)}", width=width))
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
    y0, y1, y_ticks, y_step = _linear_scale(min(ally), max(ally))
    amin_raw, amax_raw = float(axis[0]), float(axis[-1])
    amin, amax, x_ticks, x_step = _linear_scale(amin_raw, amax_raw)
    height = round(width * 0.42)
    pad_l, pad_r, pad_t, pad_b = 52, 16, 14, 34
    pw, ph = width - pad_l - pad_r, height - pad_t - pad_b

    def px(a: float) -> float:
        return pad_l + (a - amin) / (amax - amin) * pw

    def py(v: float) -> float:
        return pad_t + (1.0 - (v - y0) / (y1 - y0)) * ph

    def band(lower: list[float], upper: list[float]) -> str:
        up = " ".join(f"{px(axis[i]):.1f},{py(upper[i]):.1f}" for i in range(n) if _ok(upper[i]) and _ok(axis[i]))
        dn = " ".join(f"{px(axis[i]):.1f},{py(lower[i]):.1f}" for i in range(n - 1, -1, -1) if _ok(lower[i]) and _ok(axis[i]))
        return f"{up} {dn}"

    def line(values: list[float]) -> str:
        return " ".join(f"{px(axis[i]):.1f},{py(values[i]):.1f}" for i in range(n) if _ok(values[i]) and _ok(axis[i]))

    parts: list[str] = [
        f'<rect x="{pad_l}" y="{pad_t}" width="{pw:.0f}" height="{ph:.0f}" rx="3" fill="{PLOT_BG}" stroke="{GRID}" stroke-width="1"></rect>',
    ]
    for v in y_ticks:
        y = py(v)
        parts.append(f'<line x1="{pad_l}" y1="{y:.1f}" x2="{width - pad_r:.0f}" y2="{y:.1f}" stroke="{GRID_SOFT}"></line>')
        parts.append(f'<text x="{pad_l - 7}" y="{y + 3:.1f}" text-anchor="end" font-size="{FS_TICK}" fill="{MUTED}" class="numt">{_tick_label(v, step=y_step)}</text>')
    for a in x_ticks:
        parts.append(f'<line x1="{px(a):.0f}" y1="{pad_t}" x2="{px(a):.0f}" y2="{pad_t + ph:.0f}" stroke="{GRID_SOFT}"></line>')
        parts.append(_x_tick_text(px(a), height - 14, _tick_label(a, step=x_step), width=width))
    parts.extend([
        f'<polygon points="{band(q05, q95)}" fill="{ACCENT}" fill-opacity="0.12"><title>q05-q95 envelope</title></polygon>',
        f'<polygon points="{band(q25, q75)}" fill="{ACCENT}" fill-opacity="0.24"><title>q25-q75 envelope</title></polygon>',
        f'<polyline points="{line(med)}" fill="none" stroke="{ACCENT}" stroke-width="1.8" stroke-linejoin="round"><title>median spectrum</title></polyline>',
    ])
    parts.append(_legend_panel(
        [("line", ACCENT, "median"), ("band", ACCENT, "q25–q75"), ("band", ACCENT, "q05–q95")],
        right=width - pad_r - 8, top=pad_t + 8,
    ))
    parts.append(f'<text x="{pad_l + pw / 2:.0f}" y="{height - 1:.0f}" text-anchor="middle" font-size="{FS_AXIS}" fill="{FAINT}">{esc(axis_label)}{(" / " + esc(unit)) if unit else ""}</text>')
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
    vmax = 1.0
    parts = [f'<rect x="{pad_l}" y="{pad_t}" width="{pw:.0f}" height="{ph:.0f}" rx="3" fill="{PLOT_BG}" stroke="{GRID}" stroke-width="1"></rect>']
    for frac in (0.0, 0.25, 0.5, 0.75, 1.0):
        y = pad_t + (1.0 - frac) * ph
        parts.append(f'<line x1="{pad_l}" y1="{y:.1f}" x2="{width - pad_r:.0f}" y2="{y:.1f}" stroke="{GRID_SOFT}"></line>')
        parts.append(f'<text x="{pad_l - 6}" y="{y + 3:.1f}" text-anchor="end" font-size="{FS_TICK}" fill="{MUTED}" class="numt">{frac * 100:.0f}%</text>')
    cum = 0.0
    cumpts: list[tuple[float, float]] = []
    for i, v in enumerate(vals):
        h = (v / vmax) * ph
        x = pad_l + i * bw
        cum += v
        cumpts.append((x + bw / 2, pad_t + (1 - cum) * ph))
        parts.append(
            f'<rect class="barm" x="{x + 1.5:.1f}" y="{pad_t + ph - h:.1f}" width="{max(1.0, bw - 3):.1f}" height="{h:.1f}" rx="1.5" fill="{ACCENT}">'
            f'<title>PC{i + 1}: {v * 100:.1f}% (cumulative {cum * 100:.1f}%)</title></rect>'
            f'<text x="{x + bw / 2:.1f}" y="{pad_t + ph + 16:.0f}" text-anchor="middle" font-size="{FS_TICK}" fill="{MUTED}">{i + 1}</text>'
        )
    parts.append(f'<polyline points="{" ".join(f"{px:.1f},{py:.1f}" for px, py in cumpts)}" fill="none" stroke="{FAINT}" stroke-width="1.4" stroke-dasharray="3 2"><title>cumulative explained variance</title></polyline>')
    for px, py in cumpts:
        parts.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="1.9" fill="{FAINT}"></circle>')
    parts.append(_legend_panel([("box", ACCENT, "PC variance"), ("dash", FAINT, "cumulative")], right=width - pad_r - 6, top=pad_t + 6))
    parts.append(f'<text x="{pad_l + pw / 2:.0f}" y="{height - 2:.0f}" text-anchor="middle" font-size="{FS_AXIS}" fill="{FAINT}">principal component · cumulative (dashed)</text>')
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
    raw_min = min(lo for _, sp in fams for lo, _ in sp)
    raw_max = max(hi for _, sp in fams for _, hi in sp)
    gmin, gmax, ticks, step = _linear_scale(raw_min, raw_max)
    label_w, row_h, gap, pad_t, pad_b = 160, 28, 16, 8, 34
    pw = width - label_w - 18
    height = pad_t + len(fams) * (row_h + gap) + pad_b
    parts: list[str] = []
    for i, (fam, sp) in enumerate(fams):
        lo = min(a for a, _ in sp)
        hi = max(b for _, b in sp)
        y = pad_t + i * (row_h + gap)
        x0 = label_w + (lo - gmin) / (gmax - gmin) * pw
        x1 = label_w + (hi - gmin) / (gmax - gmin) * pw
        w = max(6.0, x1 - x0)
        label_text = f"{num(lo)}–{num(hi)} · {len(sp)}"
        value_inside = x1 > width - 180 and w > 130
        value_x = x1 - 8 if value_inside else min(x1 + 10, width - 6)
        value_anchor = "end" if value_inside or value_x >= width - 6 else "start"
        value_color = "#fff" if value_inside else MUTED
        parts.append(
            f'<text x="{label_w - 12}" y="{y + row_h / 2 + 4:.0f}" text-anchor="end" font-size="{FS_LABEL}" fill="{INK}" class="lbl">{esc(_clip(fam, 18))}</text>'
            f'<rect class="barm" x="{x0:.1f}" y="{y:.0f}" width="{w:.1f}" height="{row_h}" rx="4" fill="{_ramp(i)}" opacity="0.9">'
            f'<title>{esc(fam)}: {num(lo)}–{num(hi)} {esc(unit_label)} across {len(sp)} dataset(s)</title></rect>'
            f'<text x="{value_x:.1f}" y="{y + row_h / 2 + 4:.0f}" text-anchor="{value_anchor}" font-size="{FS_TICK}" fill="{value_color}" class="numt">{label_text}</text>'
        )
    axis_y = pad_t + len(fams) * (row_h + gap)
    parts.append(f'<line x1="{label_w}" y1="{axis_y:.0f}" x2="{label_w + pw:.0f}" y2="{axis_y:.0f}" stroke="{GRID}"></line>')
    for val in ticks:
        x = label_w + (val - gmin) / (gmax - gmin) * pw
        parts.append(f'<line x1="{x:.0f}" y1="{pad_t}" x2="{x:.0f}" y2="{axis_y:.0f}" stroke="{GRID_SOFT}"></line>')
        parts.append(_x_tick_text(x, axis_y + 18, _tick_label(val, step=step), width=width))
    parts.append(f'<text x="{label_w + pw / 2:.0f}" y="{height - 2:.0f}" text-anchor="middle" font-size="{FS_AXIS}" fill="{FAINT}">wavelength / {esc(unit_label)} · band = min–max coverage, then range · dataset count</text>')
    return _svg(width, height, "".join(parts), title=title)


# =============================================================================
# Dataset explorer charts: samples/features scatter + profile radar + diagnostics
# =============================================================================
def samples_features_scatter(points: list[dict[str, Any]], *, title: str = "Samples vs features", width: float = 1040) -> str:
    """Whole-bank scatter plot: each dataset positioned by sample count and feature count.

    Axes are log-scaled when the range spans more than one order of magnitude. Point size reflects
    the number of targets; color reflects the dataset's mean profile risk when available, else family.
    """
    rows = []
    for p in points:
        samples = _finite_float(p.get("samples"))
        features = _finite_float(p.get("features"))
        if samples is not None and features is not None and samples > 0 and features > 0:
            rows.append(p | {"samples": samples, "features": features})
    if len(rows) < 2:
        return _empty(width, 260, title, "not enough datasets")
    height = round(width * 0.46)
    pad_l, pad_r, pad_t, pad_b = 62, 24, 22, 48
    pw, ph = width - pad_l - pad_r, height - pad_t - pad_b
    xs = [r["samples"] for r in rows]
    ys = [r["features"] for r in rows]
    log_x = max(xs) / min(xs) >= 10
    log_y = max(ys) / min(ys) >= 10

    x_step: float | None = None
    y_step: float | None = None
    if log_x:
        x_min, x_max, x_ticks = _log_scale(min(xs), max(xs))
    else:
        x_min, x_max, x_ticks, x_step = _linear_scale(min(xs), max(xs))
    if log_y:
        y_min, y_max, y_ticks = _log_scale(min(ys), max(ys))
    else:
        y_min, y_max, y_ticks, y_step = _linear_scale(min(ys), max(ys))
    x0, x1 = (math.log10(x_min), math.log10(x_max)) if log_x else (x_min, x_max)
    y0, y1 = (math.log10(y_min), math.log10(y_max)) if log_y else (y_min, y_max)

    def tx(v: float) -> float:
        return math.log10(v) if log_x else v

    def ty(v: float) -> float:
        return math.log10(v) if log_y else v

    def px(v: float) -> float:
        return pad_l + (tx(v) - x0) / (x1 - x0) * pw

    def py(v: float) -> float:
        return pad_t + (1.0 - (ty(v) - y0) / (y1 - y0)) * ph

    parts: list[str] = [f'<rect x="{pad_l}" y="{pad_t}" width="{pw:.0f}" height="{ph:.0f}" rx="3" fill="{PLOT_BG}" stroke="{GRID}" stroke-width="1"></rect>']
    for tick in x_ticks:
        x = px(tick)
        parts.append(f'<line x1="{x:.0f}" y1="{pad_t}" x2="{x:.0f}" y2="{pad_t + ph:.0f}" stroke="{GRID_SOFT}"></line>')
        parts.append(_x_tick_text(x, height - 22, _tick_label(tick, step=x_step, integer=True), width=width))
    for tick in y_ticks:
        y = py(tick)
        parts.append(f'<line x1="{pad_l}" y1="{y:.0f}" x2="{pad_l + pw:.0f}" y2="{y:.0f}" stroke="{GRID_SOFT}"></line>')
        parts.append(f'<text x="{pad_l - 8}" y="{y + 4:.0f}" text-anchor="end" font-size="{FS_TICK}" fill="{MUTED}" class="numt">{_tick_label(tick, step=y_step, integer=True)}</text>')
    draw_rows = sorted(rows, key=lambda r: float(r.get("targets") or 0), reverse=True)
    for i, r in enumerate(draw_rows):
        risk = _finite_float(r.get("risk"))
        color = _risk_color(risk) if risk is not None else _ramp(i)
        targets = _finite_float(r.get("targets")) or 0.0
        radius = 3.3 + min(6.0, float(targets) ** 0.5 * 1.7)
        label = str(r.get("label") or r.get("id") or "dataset")
        family = str(r.get("family") or "unknown")
        tier = str(r.get("tier") or "")
        href = r.get("href")
        circle = (
            f'<circle class="pt" cx="{px(r["samples"]):.1f}" cy="{py(r["features"]):.1f}" r="{radius:.1f}" fill="{color}" fill-opacity="0.74" stroke="#fff" stroke-width="1.1">'
            f'<title>{esc(label)} · {num(r["samples"])} samples · {num(r["features"])} features · {esc(family)}{(" · " + esc(tier)) if tier else ""}</title></circle>'
        )
        parts.append(f'<a href="{esc(str(href))}">{circle}</a>' if href else circle)
    parts.append(f'<text x="{pad_l + pw / 2:.0f}" y="{height - 3:.0f}" text-anchor="middle" font-size="{FS_AXIS}" fill="{FAINT}">samples per dataset{" (log scale)" if log_x else ""}</text>')
    parts.append(f'<text transform="translate(16 {pad_t + ph / 2:.0f}) rotate(-90)" text-anchor="middle" font-size="{FS_AXIS}" fill="{FAINT}">features / wavelengths{" (log scale)" if log_y else ""}</text>')
    parts.append(_risk_legend(width - 232, 13))
    parts.append(f'<text x="{pad_l}" y="{pad_t - 8:.0f}" font-size="{FS_AXIS}" fill="{FAINT}">{len(rows)} datasets · colour = profile risk · size = #targets</text>')
    parts.append(
        f'<g transform="translate({width - 232:.0f} {height - 24:.0f})">'
        f'<circle cx="0" cy="0" r="4" fill="{FAINT}" fill-opacity=".55"></circle>'
        f'<circle cx="34" cy="0" r="8" fill="{FAINT}" fill-opacity=".35"></circle>'
        f'<text x="50" y="4" font-size="{FS_TICK}" fill="{MUTED}">more targets</text></g>'
    )
    return _svg(width, height, "".join(parts), title=title)


def _risk_color(risk: float) -> str:
    risk = max(0.0, min(1.0, risk))
    if risk < 0.34:
        return "#0f766e"
    if risk < 0.67:
        return "#b7791f"
    return "#9c3f4f"


def _risk_legend(x: float, y: float) -> str:
    return (
        f'<g transform="translate({x:.0f} {y:.0f})">'
        f'<circle cx="0" cy="0" r="5" fill="#0f766e"></circle><text x="10" y="4" font-size="{FS_LEGEND}" fill="{MUTED}">low profile risk</text>'
        f'<circle cx="108" cy="0" r="5" fill="#b7791f"></circle><text x="118" y="4" font-size="{FS_LEGEND}" fill="{MUTED}">mid</text>'
        f'<circle cx="160" cy="0" r="5" fill="#9c3f4f"></circle><text x="170" y="4" font-size="{FS_LEGEND}" fill="{MUTED}">high</text>'
        "</g>"
    )


def radar_profiles(profiles: list[dict[str, Any]], *, title: str = "Dataset profile radar", width: float = 520) -> str:
    """Radar/star chart for normalized dataset-property axes (0..1; outward = higher risk)."""
    axes = [
        ("integrity_risk", "integrity"),
        ("noise_risk", "noise"),
        ("local_artefact_risk", "artefacts"),
        ("shape_drift", "baseline"),
        ("outlier_pressure", "PCA outliers"),
        ("reference_spread", "reference"),
        ("repeatability_risk", "repeatability"),
        ("structure_complexity", "structure"),
    ]
    rows = []
    for p in profiles[:8]:
        scores = p.get("scores") or {}
        vals = [float(scores.get(k) or 0.0) for k, _ in axes]
        if any(v > 0 for v in vals):
            rows.append((str(p.get("label") or "dataset"), vals, str(p.get("color") or "")))
    if not rows:
        return _empty(width, 300, title, "profile unavailable")
    height = round(width * 0.80)
    cx, cy = width * 0.40, height * 0.5
    rmax = min(width * 0.24, height * 0.34)
    n_ax = len(axes)
    parts: list[str] = []

    def point(i: int, value: float) -> tuple[float, float]:
        ang = -math.pi / 2 + i * 2 * math.pi / n_ax
        r = rmax * max(0.0, min(1.0, value))
        return cx + r * math.cos(ang), cy + r * math.sin(ang)

    # Concentric rings: faint inside, the unit ring a touch stronger; fraction labels sit just left of
    # the vertical axis so they never overlap a spoke.
    for frac in (0.25, 0.5, 0.75, 1.0):
        pts = " ".join(f"{point(i, frac)[0]:.1f},{point(i, frac)[1]:.1f}" for i in range(n_ax))
        parts.append(f'<polygon points="{pts}" fill="none" stroke="{GRID if frac == 1.0 else GRID_SOFT}" stroke-width="1"></polygon>')
        parts.append(f'<text x="{cx - 5:.1f}" y="{point(0, frac)[1] + 3:.1f}" text-anchor="end" font-size="9.5" fill="{FAINT}" class="numt">{frac:g}</text>')
    for i, (_key, label) in enumerate(axes):
        ex, ey = point(i, 1.0)
        parts.append(f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{GRID_SOFT}"></line>')
        lx, ly = point(i, 1.13)
        anchor = "middle" if abs(lx - cx) <= 20 else ("end" if lx < cx else "start")
        parts.append(f'<text x="{lx:.1f}" y="{ly + 3:.1f}" text-anchor="{anchor}" font-size="{FS_AXIS}" fill="{MUTED}">{esc(label)}</text>')
    # Profiles: draw the secondary ones first so the primary (index 0) sits on top; vertex dots carry a
    # per-axis hover readout (all profiles when a single one is shown, else only the primary).
    single = len(rows) == 1
    for i in range(len(rows) - 1, -1, -1):
        label, vals, color = rows[i]
        color = color or _ramp(i)
        primary = i == 0
        pts = " ".join(f"{point(j, v)[0]:.1f},{point(j, v)[1]:.1f}" for j, v in enumerate(vals))
        parts.append(
            f'<polygon points="{pts}" fill="{color}" fill-opacity="{0.22 if primary else 0.09}" '
            f'stroke="{color}" stroke-width="{2.2 if primary else 1.3}" stroke-linejoin="round"><title>{esc(label)} profile</title></polygon>'
        )
        if single or primary:
            for j, (_k, axlabel) in enumerate(axes):
                vx, vy = point(j, vals[j])
                parts.append(f'<circle cx="{vx:.1f}" cy="{vy:.1f}" r="2.4" fill="{color}"><title>{esc(axlabel)}: {vals[j]:.2f}</title></circle>')
    parts.append(_legend_panel([("box", color or _ramp(i), _clip(label, 16)) for i, (label, _vals, color) in enumerate(rows)], right=width - 8, top=12))
    parts.append(f'<text x="{cx:.1f}" y="{height - 8:.0f}" text-anchor="middle" font-size="{FS_AXIS}" fill="{FAINT}">0 center · 1 outer ring · outward = stronger anomaly / heterogeneity signal</text>')
    return _svg(width, height, "".join(parts), title=title)


def diagnostic_bars(diagnostics: list[dict[str, Any]], *, title: str = "Diagnostic hypotheses", width: float = 520, top_n: int = 8) -> str:
    """Ranked diagnostic hypothesis bars, where score is 0..1."""
    rows = [(str(d.get("label") or d.get("key") or "diagnostic"), float(d.get("score") or 0.0)) for d in diagnostics[:top_n] if _ok(d.get("score"))]
    if not rows:
        return _empty(width, 180, title, "no diagnostic")
    height = 46 + len(rows) * 32
    label_w = min(width * 0.42, 220)
    bar_w = width - label_w - 56
    parts: list[str] = []
    axis_y = 26
    for tick in (0.0, 0.25, 0.5, 0.75, 1.0):
        x = label_w + tick * bar_w
        parts.append(f'<line x1="{x:.0f}" y1="{axis_y}" x2="{x:.0f}" y2="{height - 10:.0f}" stroke="{GRID_SOFT}"></line>')
        parts.append(f'<text x="{x:.0f}" y="13" text-anchor="middle" font-size="{FS_TICK}" fill="{MUTED}" class="numt">{tick:.2g}</text>')
    parts.append(f'<text x="{label_w + bar_w:.0f}" y="30" text-anchor="end" font-size="{FS_AXIS}" fill="{FAINT}">hypothesis score</text>')
    for i, (label, score) in enumerate(rows):
        y = 36 + i * 32
        w = max(2.0, max(0.0, min(1.0, score)) * bar_w)
        color = _risk_color(score)
        parts.append(
            f'<text x="{label_w - 10:.0f}" y="{y + 16:.0f}" text-anchor="end" font-size="{FS_LABEL}" fill="{INK}">{esc(_clip(label, 30))}</text>'
            f'<rect x="{label_w:.0f}" y="{y:.0f}" width="{bar_w:.0f}" height="20" rx="4" fill="{GRID_SOFT}" stroke="{GRID}" stroke-width="1"></rect>'
            f'<rect x="{label_w:.0f}" y="{y:.0f}" width="{w:.1f}" height="20" rx="4" fill="{color}"><title>{esc(label)}: {score:.2f}</title></rect>'
            f'<text x="{label_w + bar_w + 8:.0f}" y="{y + 15:.0f}" font-size="{FS_VALUE}" fill="{MUTED}" class="numt">{score:.2f}</text>'
        )
    return _svg(width, height, "".join(parts), title=title)


def pca_score_scatter(score_plot: dict[str, Any], *, title: str = "PCA score plot", width: float = 520) -> str:
    """PC1/PC2 scatter from precomputed card points."""
    pts = score_plot.get("points") or []
    rows: list[tuple[float, float]] = []
    for p in pts:
        if not isinstance(p, dict):
            continue
        x = _finite_float(p.get("x"))
        y = _finite_float(p.get("y"))
        if x is not None and y is not None:
            rows.append((x, y))
    if len(rows) < 3:
        return _empty(width, 240, title, "PCA scores unavailable")
    height = round(width * 0.62)
    pad_l, pad_r, pad_t, pad_b = 42, 18, 18, 34
    pw, ph = width - pad_l - pad_r, height - pad_t - pad_b
    xs, ys = [x for x, _y in rows], [y for _x, y in rows]
    x0, x1, x_ticks, x_step = _linear_scale(min(xs), max(xs), target_ticks=5, include_zero=True)
    y0, y1, y_ticks, y_step = _linear_scale(min(ys), max(ys), target_ticks=5, include_zero=True)

    def px(v: float) -> float:
        return pad_l + (v - x0) / (x1 - x0) * pw

    def py(v: float) -> float:
        return pad_t + (1.0 - (v - y0) / (y1 - y0)) * ph

    parts: list[str] = [f'<rect x="{pad_l}" y="{pad_t}" width="{pw:.0f}" height="{ph:.0f}" rx="3" fill="{PLOT_BG}" stroke="{GRID}" stroke-width="1"></rect>']
    for tick in x_ticks:
        x = px(tick)
        parts.append(f'<line x1="{x:.0f}" y1="{pad_t}" x2="{x:.0f}" y2="{pad_t + ph:.0f}" stroke="{GRID_SOFT}"></line>')
        parts.append(_x_tick_text(x, height - 18, _tick_label(tick, step=x_step), width=width))
    for tick in y_ticks:
        y = py(tick)
        parts.append(f'<line x1="{pad_l}" y1="{y:.0f}" x2="{pad_l + pw:.0f}" y2="{y:.0f}" stroke="{GRID_SOFT}"></line>')
        parts.append(f'<text x="{pad_l - 7}" y="{y + 3:.0f}" text-anchor="end" font-size="{FS_TICK}" fill="{MUTED}" class="numt">{_tick_label(tick, step=y_step)}</text>')
    if x0 < 0 < x1:
        parts.append(f'<line x1="{px(0):.1f}" y1="{pad_t}" x2="{px(0):.1f}" y2="{pad_t + ph:.0f}" stroke="{FAINT}" stroke-width="1.2"></line>')
    if y0 < 0 < y1:
        parts.append(f'<line x1="{pad_l}" y1="{py(0):.1f}" x2="{pad_l + pw:.0f}" y2="{py(0):.1f}" stroke="{FAINT}" stroke-width="1.2"></line>')
    # Radius + opacity scale down as the cloud gets denser, so a large dataset reads as structure
    # rather than an ink blob.
    n = len(rows)
    r = 2.2 if n > 800 else 2.7 if n > 250 else 3.2
    op = 0.42 if n > 800 else 0.55 if n > 250 else 0.66
    for x, y in rows:
        parts.append(f'<circle cx="{px(x):.1f}" cy="{py(y):.1f}" r="{r}" fill="{ACCENT}" fill-opacity="{op}"><title>PC1 {num(x, nd=4)} · PC2 {num(y, nd=4)}</title></circle>')
    evr = score_plot.get("explained_variance_ratio") or []
    xlab = f"PC1 ({float(evr[0]) * 100:.1f}%)" if len(evr) >= 1 and _ok(evr[0]) else "PC1"
    ylab = f"PC2 ({float(evr[1]) * 100:.1f}%)" if len(evr) >= 2 and _ok(evr[1]) else "PC2"
    parts.append(f'<text x="{pad_l + pw / 2:.0f}" y="{height - 3:.0f}" text-anchor="middle" font-size="{FS_AXIS}" fill="{FAINT}">{esc(xlab)}</text>')
    parts.append(f'<text transform="translate(13 {pad_t + ph / 2:.0f}) rotate(-90)" text-anchor="middle" font-size="{FS_AXIS}" fill="{FAINT}">{esc(ylab)}</text>')
    parts.append(f'<text x="{width - pad_r:.0f}" y="{pad_t + 12:.0f}" text-anchor="end" font-size="{FS_TICK}" fill="{FAINT}">{num(n)} scores</text>')
    return _svg(width, height, "".join(parts), title=title)


def xy_correlation_curve(xy: dict[str, Any], *, title: str = "X-Y spectral correlation", width: float = 520) -> str:
    """Line chart of signed and absolute per-wavelength correlation with one target."""
    curve = xy.get("curve") or {}
    axis = curve.get("axis") or []
    abs_corr = curve.get("abs_corr") or []
    corr = curve.get("corr") or []
    n = min(len(axis), len(abs_corr), len(corr))
    if n < 2:
        return _empty(width, 220, title, "correlation unavailable")
    height = round(width * 0.46)
    pad_l, pad_r, pad_t, pad_b = 42, 16, 14, 32
    pw, ph = width - pad_l - pad_r, height - pad_t - pad_b
    amin, amax, x_ticks, x_step = _linear_scale(float(axis[0]), float(axis[n - 1]))

    def px(a: float) -> float:
        return pad_l + (a - amin) / (amax - amin) * pw

    def py(v: float) -> float:
        return pad_t + (1.0 - (v + 1.0) / 2.0) * ph

    signed = " ".join(f"{px(float(axis[i])):.1f},{py(float(corr[i])):.1f}" for i in range(n) if _ok(axis[i]) and _ok(corr[i]))
    absolute = " ".join(f"{px(float(axis[i])):.1f},{py(float(abs_corr[i])):.1f}" for i in range(n) if _ok(axis[i]) and _ok(abs_corr[i]))
    abs_top = [(float(axis[i]), float(abs_corr[i])) for i in range(n) if _ok(axis[i]) and _ok(abs_corr[i])]
    abs_area = ""
    if abs_top:
        upper = " ".join(f"{px(a):.1f},{py(v):.1f}" for a, v in abs_top)
        lower = " ".join(f"{px(a):.1f},{py(0.0):.1f}" for a, _v in reversed(abs_top))
        abs_area = f"{upper} {lower}"
    parts: list[str] = [
        f'<rect x="{pad_l}" y="{pad_t}" width="{pw:.0f}" height="{ph:.0f}" rx="3" fill="{PLOT_BG}" stroke="{GRID}" stroke-width="1"></rect>',
    ]
    for tick in (-1.0, -0.5, 0.0, 0.5, 1.0):
        y = py(tick)
        parts.append(f'<line x1="{pad_l}" y1="{y:.1f}" x2="{pad_l + pw:.0f}" y2="{y:.1f}" stroke="{FAINT if tick == 0 else GRID_SOFT}" stroke-width="{1.3 if tick == 0 else 1}"></line>')
        parts.append(f'<text x="{pad_l - 7}" y="{y + 3:.1f}" text-anchor="end" font-size="{FS_TICK}" fill="{MUTED}" class="numt">{tick:g}</text>')
    if abs_area:
        parts.append(f'<polygon points="{abs_area}" fill="{ACCENT}" fill-opacity="0.10"><title>absolute correlation envelope</title></polygon>')
    parts.extend([
        f'<polyline points="{signed}" fill="none" stroke="{FAINT}" stroke-width="1.35" stroke-dasharray="4 3"><title>signed correlation</title></polyline>',
        f'<polyline points="{absolute}" fill="none" stroke="{ACCENT}" stroke-width="2.0"><title>absolute correlation</title></polyline>',
    ])
    for a in x_ticks:
        parts.append(f'<line x1="{px(a):.0f}" y1="{pad_t + ph:.0f}" x2="{px(a):.0f}" y2="{pad_t + ph + 4:.0f}" stroke="{GRID}"></line>')
        parts.append(_x_tick_text(px(a), height - 13, _tick_label(a, step=x_step), width=width))
    parts.append(_legend_panel([("line", ACCENT, "|r|"), ("dash", FAINT, "signed r")], right=width - pad_r - 6, top=pad_t + 6))
    parts.append(f'<text x="{pad_l + pw / 2:.0f}" y="{height - 1:.0f}" text-anchor="middle" font-size="{FS_AXIS}" fill="{FAINT}">axis · Pearson correlation scale</text>')
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
