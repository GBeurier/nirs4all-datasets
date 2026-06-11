"""Inline-SVG chart functions, rendered at build time (no runtime JS chart lib).

Each function returns a self-contained ``<svg>`` string sized by a ``viewBox`` so it scales fluidly
to its container. Charts are on-palette, labelled, and accessible (``role="img"`` + ``<title>`` +
``aria-label``). Pure stdlib + the escaping helpers — no nirs4all, pandas, or matplotlib.
"""
from __future__ import annotations

import math
from typing import Any

from .escape import esc, num

# On-palette sequential ramp reused across donuts/segments (teal -> cyan -> green -> indigo -> amber ...).
PALETTE = [
    "#0d9488", "#06b6d4", "#10b981", "#4f46e5", "#d97706",
    "#0f766e", "#0891b2", "#059669", "#6366f1", "#b45309",
    "#14b8a6", "#22d3ee", "#34d399", "#818cf8", "#f59e0b",
]


def _color(i: int) -> str:
    return PALETTE[i % len(PALETTE)]


# A reusable vertical-tint gradient per palette colour gives bars depth without any runtime cost.
# The id is colour-derived so identical fills share one def and ids never collide across charts.
def _grad_id(color: str) -> str:
    return "g" + color.lstrip("#")


def _grad_defs(colors: list[str]) -> str:
    """One ``<linearGradient>`` per distinct colour: a light top tint fading to the solid colour."""
    seen: list[str] = []
    for c in colors:
        if c not in seen:
            seen.append(c)
    stops = "".join(
        f'<linearGradient id="{_grad_id(c)}" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0%" stop-color="{c}" stop-opacity="1"></stop>'
        f'<stop offset="100%" stop-color="{c}" stop-opacity="0.74"></stop></linearGradient>'
        for c in seen
    )
    return f"<defs>{stops}</defs>"


def _fill(color: str) -> str:
    """Reference the colour's gradient fill (depth) rather than the flat colour."""
    return f"url(#{_grad_id(color)})"


def _svg(viewbox_w: int, viewbox_h: int, inner: str, *, title: str) -> str:
    return (
        f'<svg viewBox="0 0 {viewbox_w} {viewbox_h}" role="img" aria-label="{esc(title)}" '
        f'preserveAspectRatio="xMidYMid meet"><title>{esc(title)}</title>{inner}</svg>'
    )


def _polar(cx: float, cy: float, r: float, frac: float) -> tuple[float, float]:
    """Point on a circle for ``frac`` of a full turn, starting at 12 o'clock, clockwise."""
    ang = frac * 2 * math.pi - math.pi / 2
    return cx + r * math.cos(ang), cy + r * math.sin(ang)


# =============================================================================
# Horizontal bar chart
# =============================================================================
def bar_chart(items: list[tuple[str, float]], *, title: str, top_n: int | None = None, unit: str = "") -> str:
    """Horizontal bar chart from ``(label, value)`` pairs, sorted by value, optionally capped at ``top_n``."""
    rows = sorted(items, key=lambda kv: -kv[1])
    if top_n is not None and len(rows) > top_n:
        head = rows[:top_n]
        rest = sum(v for _, v in rows[top_n:])
        rows = head + [(f"+{len(items) - top_n} more", rest)]
    if not rows:
        return _svg(600, 80, '<text x="300" y="44" text-anchor="middle">no data</text>', title=title)

    label_w, bar_w, row_h, gap = 168, 360, 26, 8
    height = len(rows) * (row_h + gap) + 8
    width = label_w + bar_w + 56
    vmax = max((v for _, v in rows), default=1) or 1
    colors = [_color(i) for i in range(len(rows))]
    parts: list[str] = [_grad_defs(colors)]
    for i, (label, value) in enumerate(rows):
        y = 4 + i * (row_h + gap)
        w = max(2.0, (value / vmax) * bar_w)
        parts.append(
            f'<g class="bar-row">'
            f'<text x="{label_w - 10}" y="{y + row_h / 2 + 4}" text-anchor="end" font-size="12">{esc(label)}</text>'
            f'<rect x="{label_w}" y="{y}" width="{w:.1f}" height="{row_h}" rx="5" fill="{_fill(colors[i])}"></rect>'
            f'<text x="{label_w + w + 8:.1f}" y="{y + row_h / 2 + 4}" font-size="12" class="barlabel">{num(value)}{esc(unit)}</text>'
            f'</g>'
        )
    return _svg(width, height, "".join(parts), title=title)


# =============================================================================
# Donut chart
# =============================================================================
def donut_chart(items: list[tuple[str, float]], *, title: str) -> str:
    """Donut chart from ``(label, value)`` pairs, with a centred total and an external legend."""
    rows = [(k, v) for k, v in sorted(items, key=lambda kv: -kv[1]) if v > 0]
    total = sum(v for _, v in rows)
    if total <= 0:
        return _svg(420, 240, '<text x="210" y="124" text-anchor="middle">no data</text>', title=title)

    cx, cy, r, rin = 120, 120, 100, 62
    arcs: list[str] = []
    acc = 0.0
    for i, (label, value) in enumerate(rows):
        f0 = acc / total
        acc += value
        f1 = acc / total
        x0, y0 = _polar(cx, cy, r, f0)
        x1, y1 = _polar(cx, cy, r, f1)
        xi0, yi0 = _polar(cx, cy, rin, f0)
        xi1, yi1 = _polar(cx, cy, rin, f1)
        large = 1 if (f1 - f0) > 0.5 else 0
        if (f1 - f0) >= 0.9999:  # single full slice -> draw as a full ring, arcs can't span 360°
            arcs.append(f'<circle cx="{cx}" cy="{cy}" r="{(r + rin) / 2:.1f}" fill="none" stroke="{_color(i)}" stroke-width="{r - rin}"><title>{esc(label)}: {num(value)}</title></circle>')
            continue
        d = (
            f'M{x0:.2f},{y0:.2f} A{r},{r} 0 {large} 1 {x1:.2f},{y1:.2f} '
            f'L{xi1:.2f},{yi1:.2f} A{rin},{rin} 0 {large} 0 {xi0:.2f},{yi0:.2f} Z'
        )
        arcs.append(f'<path class="arc" d="{d}" fill="{_color(i)}"><title>{esc(label)}: {num(value)} ({value / total * 100:.0f}%)</title></path>')
    center = (
        f'<text x="{cx}" y="{cy - 4}" text-anchor="middle" font-size="30" font-weight="700" fill="#0f172a">{num(int(total))}</text>'
        f'<text x="{cx}" y="{cy + 18}" text-anchor="middle" font-size="11" fill="#64748b">total</text>'
    )
    legend = []
    for i, (label, value) in enumerate(rows):
        ly = 26 + i * 22
        legend.append(
            f'<g><rect x="252" y="{ly - 11}" width="12" height="12" rx="3" fill="{_color(i)}"></rect>'
            f'<text x="270" y="{ly}" font-size="12">{esc(label)} · {num(value)}</text></g>'
        )
    rows_h = 26 + len(rows) * 22 + 8
    height = max(240, rows_h)
    return _svg(560, height, f'<g>{"".join(arcs)}{center}</g><g>{"".join(legend)}</g>', title=title)


# =============================================================================
# Stacked horizontal bars (structural mixes)
# =============================================================================
def stacked_bars(rows: list[tuple[str, list[tuple[str, float]]]], *, title: str) -> str:
    """Several labelled stacked bars; each row is ``(row_label, [(segment_label, value), ...])``.

    Segment colours are assigned per distinct segment label across rows, so a shared legend reads.
    """
    seg_labels: list[str] = []
    for _, segs in rows:
        for label, _v in segs:
            if label not in seg_labels:
                seg_labels.append(label)
    color_for = {label: _color(i) for i, label in enumerate(seg_labels)}

    label_w, bar_w, row_h, gap = 132, 380, 30, 18
    height = len(rows) * (row_h + gap) + 8
    width = label_w + bar_w + 16
    parts: list[str] = []
    for ri, (row_label, segs) in enumerate(rows):
        y = 4 + ri * (row_h + gap)
        total = sum(v for _, v in segs) or 1
        x = float(label_w)
        parts.append(f'<text x="{label_w - 12}" y="{y + row_h / 2 + 4}" text-anchor="end" font-size="12">{esc(row_label)}</text>')
        for label, value in segs:
            w = (value / total) * bar_w
            if w <= 0:
                continue
            cap = ""
            if w > 30:
                cap = f'<text x="{x + w / 2:.1f}" y="{y + row_h / 2 + 4}" text-anchor="middle" font-size="11" fill="#fff" font-weight="600">{num(value)}</text>'
            parts.append(
                f'<g class="seg"><rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{row_h}" fill="{color_for[label]}">'
                f'<title>{esc(row_label)} · {esc(label)}: {num(value)}</title></rect>{cap}</g>'
            )
            x += w
    legend = []
    for label in seg_labels:
        legend.append(f'<i style="background:{color_for[label]}"></i>{esc(label)}')
    body = _svg(width, height, "".join(parts), title=title)
    leg_html = "".join(f'<span>{seg}</span>' for seg in legend)
    return f'{body}<div class="legend">{leg_html}</div>'


# =============================================================================
# Histogram (distribution of counts)
# =============================================================================
def histogram(values: list[float], *, title: str, n_bins: int = 12, log: bool = False, x_label: str = "") -> str:
    """Histogram of ``values`` into ``n_bins`` (optionally log-spaced bins for skewed counts)."""
    xs = [float(v) for v in values if v is not None and (isinstance(v, bool) is False) and math.isfinite(float(v))]
    xs = [v for v in xs if v > 0] if log else xs
    if len(xs) < 2:
        return _svg(600, 200, '<text x="300" y="104" text-anchor="middle">not enough data</text>', title=title)

    lo, hi = min(xs), max(xs)
    if hi <= lo:
        hi = lo + 1
    if log:
        e0, e1 = math.log10(lo), math.log10(hi)
        edges = [10 ** (e0 + (e1 - e0) * i / n_bins) for i in range(n_bins + 1)]
    else:
        edges = [lo + (hi - lo) * i / n_bins for i in range(n_bins + 1)]
    counts = [0] * n_bins
    for v in xs:
        j = n_bins - 1
        for b in range(n_bins):
            if v <= edges[b + 1]:
                j = b
                break
        counts[j] += 1
    cmax = max(counts) or 1

    W, H = 620, 240
    pad_l, pad_b, pad_t, pad_r = 40, 34, 12, 12
    plot_w, plot_h = W - pad_l - pad_r, H - pad_b - pad_t
    bw = plot_w / n_bins
    parts: list[str] = [
        _grad_defs([_color(0)]),
        f'<line class="axis" x1="{pad_l}" y1="{pad_t + plot_h}" x2="{W - pad_r}" y2="{pad_t + plot_h}"></line>',
    ]
    for i, c in enumerate(counts):
        h = (c / cmax) * plot_h
        x = pad_l + i * bw
        y = pad_t + plot_h - h
        parts.append(
            f'<g class="bar-row"><rect x="{x + 1:.1f}" y="{y:.1f}" width="{bw - 2:.1f}" height="{h:.1f}" rx="2" fill="{_fill(_color(0))}">'
            f'<title>{num(edges[i])}–{num(edges[i + 1])}: {c}</title></rect></g>'
        )
    # x ticks: a handful, formatted on the original scale
    n_ticks = min(6, n_bins)
    for t in range(n_ticks + 1):
        idx = round(t * n_bins / n_ticks)
        x = pad_l + idx * bw
        parts.append(f'<text x="{x:.1f}" y="{pad_t + plot_h + 22}" text-anchor="middle" font-size="10">{num(edges[idx])}</text>')
    parts.append(f'<text x="{pad_l - 6}" y="{pad_t + 10}" text-anchor="end" font-size="10">{cmax}</text>')
    parts.append(f'<text x="{pad_l - 6}" y="{pad_t + plot_h}" text-anchor="end" font-size="10">0</text>')
    if x_label:
        parts.append(f'<text x="{pad_l + plot_w / 2:.1f}" y="{H - 2}" text-anchor="middle" font-size="10" fill="#64748b">{esc(x_label)}</text>')
    return _svg(W, H, "".join(parts), title=title)


# =============================================================================
# Wavelength-coverage range chart
# =============================================================================
def range_chart(items: list[dict[str, Any]], *, title: str, unit_label: str = "nm", max_rows: int = 40) -> str:
    """Each dataset a horizontal bar over ``axis_min..axis_max``, grouped (sorted) by ``family``.

    ``items`` = ``[{label, family, lo, hi, color?}, ...]``. Bars share one global axis so coverage and
    overlap read at a glance; rows are capped at ``max_rows`` (a footer notes any elided rows).
    """
    rows = [it for it in items if it.get("lo") is not None and it.get("hi") is not None and it["hi"] > it["lo"]]
    rows.sort(key=lambda it: (str(it.get("family") or ""), it["lo"]))
    elided = max(0, len(rows) - max_rows)
    rows = rows[:max_rows]
    if not rows:
        return _svg(640, 120, '<text x="320" y="64" text-anchor="middle">no axis ranges available</text>', title=title)

    gmin = min(it["lo"] for it in rows)
    gmax = max(it["hi"] for it in rows)
    span = (gmax - gmin) or 1
    label_w, plot_w, row_h, gap = 150, 420, 13, 5
    pad_t, pad_b = 8, 28
    height = pad_t + len(rows) * (row_h + gap) + pad_b
    width = label_w + plot_w + 16

    fam_color: dict[str, str] = {}
    parts: list[str] = []
    for i, it in enumerate(rows):
        fam = str(it.get("family") or "other")
        if fam not in fam_color:
            fam_color[fam] = _color(len(fam_color))
        color = it.get("color") or fam_color[fam]
        y = pad_t + i * (row_h + gap)
        x0 = label_w + (it["lo"] - gmin) / span * plot_w
        x1 = label_w + (it["hi"] - gmin) / span * plot_w
        parts.append(
            f'<g class="bar-row"><text x="{label_w - 8}" y="{y + row_h - 2}" text-anchor="end" font-size="10">{esc(it["label"])}</text>'
            f'<rect x="{x0:.1f}" y="{y}" width="{max(2.0, x1 - x0):.1f}" height="{row_h}" rx="3" fill="{color}" opacity="0.85">'
            f'<title>{esc(it["label"])} ({esc(fam)}): {num(it["lo"])}–{num(it["hi"])} {esc(unit_label)}</title></rect></g>'
        )
    # axis ticks (bottom)
    axis_y = pad_t + len(rows) * (row_h + gap) + 2
    parts.append(f'<line class="axis" x1="{label_w}" y1="{axis_y}" x2="{label_w + plot_w}" y2="{axis_y}"></line>')
    for t in range(5):
        val = gmin + span * t / 4
        x = label_w + plot_w * t / 4
        parts.append(f'<line class="axis" x1="{x:.1f}" y1="{axis_y}" x2="{x:.1f}" y2="{axis_y + 4}"></line>')
        parts.append(f'<text x="{x:.1f}" y="{axis_y + 16}" text-anchor="middle" font-size="10">{num(val)}</text>')
    body = _svg(width, height, "".join(parts), title=title)
    leg = "".join(f'<span><i style="background:{c}"></i>{esc(f)}</span>' for f, c in fam_color.items())
    footer = f'<div class="legend">{leg}</div>'
    if elided:
        footer += f'<p class="viz-sub" style="margin-top:8px">+{elided} more dataset(s) not shown — see the catalog.</p>'
    return f'{body}{footer}'


# =============================================================================
# Coverage / health gauge (a simple proportion bar)
# =============================================================================
def coverage_bar(parts: list[tuple[str, float]], *, title: str, total: float) -> str:
    """A single proportion bar (``[(label, value), ...]`` summing to <= ``total``) with inline captions."""
    total = total or 1
    W, H = 600, 64
    x = 0.0
    out: list[str] = []
    for i, (label, value) in enumerate(parts):
        w = (value / total) * W
        if w <= 0:
            continue
        cap = f'<text x="{x + w / 2:.1f}" y="40" text-anchor="middle" font-size="12" fill="#fff" font-weight="600">{esc(label)} {num(value)}</text>' if w > 70 else ""
        out.append(f'<g class="seg"><rect x="{x:.1f}" y="16" width="{w:.1f}" height="32" fill="{_color(i)}" rx="4"><title>{esc(label)}: {num(value)}</title></rect>{cap}</g>')
        x += w
    return _svg(W, H, "".join(out), title=title)
