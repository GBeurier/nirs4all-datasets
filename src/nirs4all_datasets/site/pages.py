"""Render the three page types: index (overview), catalog (filterable), dataset detail (identity card).

Pure formatting of the tier-aware view models (:mod:`model`) via :mod:`components` + :mod:`charts`.
Tier gating is enforced here at render time: no anonymized page prints an original name/description,
no non-public page exposes a byte download or a card/croissant link, and no PNG asset is referenced
for an anonymized dataset.
"""
from __future__ import annotations

import math
from typing import Any

from . import charts
from . import components as C
from .escape import esc, locator_link, num
from .model import Catalog, DatasetView
from .theme import page


# =============================================================================
# INDEX (overview)
# =============================================================================
def _index_kpis(summary: dict[str, Any], datasets: list[DatasetView]) -> list[tuple[str, str]]:
    n = summary.get("n_datasets") or len(datasets)
    samples = (summary.get("samples") or {}).get("total")
    domains = len(summary.get("by_domain") or {})
    n_public = (summary.get("by_tier") or {}).get("public", 0)
    return [
        (num(n), "datasets"),
        (num(samples) if samples else "—", "total samples"),
        (num(summary.get("total_sources") or 0), "spectral sources"),
        (num(domains), "domains"),
        (num(summary.get("n_multi_source") or 0), "multi-source"),
        (num(n_public), "public-tier"),
    ]


def _dataviz(summary: dict[str, Any], datasets: list[DatasetView]) -> str:
    """The whole-bank dataviz grid, built entirely from the index ``summary`` (+ axis ranges from views)."""
    by_domain = summary.get("by_domain") or {}
    by_family = summary.get("by_spectro_family") or {}
    by_tier = summary.get("by_tier") or {}
    license_mix = summary.get("license_mix") or {}
    origin_kinds = summary.get("origin_kinds") or {}
    samples = summary.get("samples") or {}
    features = summary.get("features") or {}

    # Whole-bank panels: wide charts get the full row (≈1040px), the rest sit two-up (≈500px). Each
    # chart's viewBox width matches that, so the type renders at a consistent ~12px everywhere.
    HALF, WIDE = 500, 1040
    cards: list[str] = []

    ranges = _axis_ranges(datasets)
    if ranges:
        # one shared axis is only meaningful within one unit (nm vs cm⁻¹ vs index) — show the dominant
        units: dict[str, int] = {}
        for r in ranges:
            units[r["unit"]] = units.get(r["unit"], 0) + 1
        unit = max(units, key=lambda u: units[u]) if units else "nm"
        same_unit = [r for r in ranges if r["unit"] == unit]
        other = len(ranges) - len(same_unit)
        sub = f"Spectral range each family covers, in {esc(unit)}" + (f" ({other} dataset(s) on another axis unit not shown)" if other else "")
        cards.append(C.viz_card(
            "Wavelength coverage", sub,
            charts.coverage_by_family(same_unit, title="Wavelength coverage by family", unit_label=unit, width=WIDE),
            wide=True,
        ))
    if by_domain:
        cards.append(C.viz_card(
            "Datasets by domain", "Application domains across the bank",
            charts.bar_chart(list(by_domain.items()), title="Datasets by domain", top_n=14, width=WIDE),
            wide=True,
        ))
    if by_family:
        cards.append(C.viz_card(
            "Spectroscopy family", "Single-modality family per dataset (mixed when heterogeneous)",
            charts.donut_chart(list(by_family.items()), title="Datasets by spectroscopy family", width=HALF),
        ))
    if by_tier:
        cards.append(C.viz_card(
            "Access tier", "Governance tier: public / private / anonymized",
            charts.donut_chart(list(by_tier.items()), title="Datasets by access tier", width=HALF),
        ))

    # targets-per-dataset distribution (datasets range from 0 to many tens of targets)
    target_vals: list[int] = [int(v.entry["n_targets"]) for v in datasets if isinstance(v.entry.get("n_targets"), int)]
    if len(target_vals) >= 2 and max(target_vals, default=0) > 1:
        cards.append(C.viz_card(
            "Targets per dataset", "How many prediction targets each dataset declares (0 = metadata-only)",
            charts.histogram([float(t) for t in target_vals], title="Distribution of target counts", n_bins=12, x_label="targets per dataset", width=HALF, int_x=True),
        ))

    sample_vals = [v.entry.get("n_samples") for v in datasets if isinstance(v.entry.get("n_samples"), int)]
    if len([v for v in sample_vals if v]) >= 2:
        cards.append(C.viz_card(
            "Sample-size distribution", f"#samples per dataset (log-spaced bins) · median {num(samples.get('median'))}",
            charts.histogram([float(v) for v in sample_vals if v], title="Distribution of dataset sample counts", log=True, x_label="samples per dataset", width=HALF, int_x=True),
        ))
    feature_vals = [v.entry.get("n_features_total") for v in datasets if isinstance(v.entry.get("n_features_total"), int)]
    if len([v for v in feature_vals if v]) >= 2:
        cards.append(C.viz_card(
            "Wavelength-count distribution", f"#wavelengths per dataset · median {num(features.get('median'))}",
            charts.histogram([float(v) for v in feature_vals if v], title="Distribution of wavelength counts", log=True, x_label="wavelengths per dataset", width=HALF, int_x=True),
        ))

    if license_mix:
        cards.append(C.viz_card(
            "License mix", "SPDX license per dataset across the bank",
            charts.bar_chart(list(license_mix.items()), title="License mix", top_n=10, width=HALF),
        ))
    if origin_kinds:
        cards.append(C.viz_card(
            "Origin kinds", "Where the bytes originate (zenodo / dataverse / url / …)",
            charts.donut_chart(list(origin_kinds.items()), title="Origin kinds", width=HALF),
        ))
    return f'<div class="viz-grid">{"".join(cards)}</div>'


def _axis_ranges(datasets: list[DatasetView]) -> list[dict[str, Any]]:
    """Pull one ``axis_min..axis_max`` span per dataset (its first card source) for the coverage chart."""
    out: list[dict[str, Any]] = []
    for v in datasets:
        card = v.card
        if not card:
            continue
        sources = card.get("sources") or []
        if not sources:
            continue
        src = sources[0]
        lo, hi = src.get("axis_min"), src.get("axis_max")
        try:
            lo_f, hi_f = float(lo), float(hi)
        except (TypeError, ValueError):
            continue
        out.append({"label": v.name, "family": v.entry.get("spectro_family") or "other", "unit": src.get("axis_unit") or "?", "lo": lo_f, "hi": hi_f})
    return out


def render_index(catalog: Catalog) -> str:
    summary = catalog.summary
    datasets = catalog.datasets
    sample_id = datasets[0].id if datasets else "corn_oil"
    get_title = 'One <em>call</em>, fully reproducible'
    body = f"""
{C.nav("", "index")}
{C.HERO_MARKUP}
<section class="section section-paper">
  <div class="container">
    {C.section_head("The bank at a glance", "Every dataset, <em>measured</em>")}
    {C.kpi_strip(_index_kpis(summary, datasets))}
  </div>
</section>
<section class="section section-aurora">
  <div class="container">
    {C.section_head("Whole-bank dataviz", "What's <em>inside</em> the bank", "Computed once at build time and rendered as inline SVG — no trackers, no runtime chart library.")}
    {_dataviz(summary, datasets)}
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    {C.section_head("Use it in one line", get_title, "Datasets download on demand by their pinned DOI, are checksum-verified, and cached locally.")}
    <div style="max-width:760px;margin:0 auto">
      {C.load_snippet(sample_id, "public")}
      <p class="dl-note" style="margin-top:16px">Public datasets fetch openly; private/anonymized datasets need a Dataverse token. The bytes always live at their licensed origin — this catalog never redistributes them.</p>
    </div>
  </div>
</section>
<section class="section">
  <div class="container" style="text-align:center">
    {C.section_head("Provenance &amp; citation", "Built to be <em>cited</em>", "Each dataset carries its DataCite provenance, origin sources, and publication DOIs. Cite the dataset DOI and its origin publications; respect each dataset's own license.")}
    <a class="btn btn-primary" href="catalog.html">Open the full catalog &rarr;</a>
  </div>
</section>
{C.footer("")}
"""
    return page(title="nirs4all-datasets — a citable, reproducible bank of raw NIRS reference datasets", rel="", body=body, scripts=C.HERO_SCRIPT, active="index")


# =============================================================================
# CATALOG (filterable / sortable / searchable)
# =============================================================================
def _filter_options(datasets: list[DatasetView], key: str) -> list[str]:
    return sorted({str(v.entry.get(key)) for v in datasets if v.entry.get(key)})


def render_catalog(catalog: Catalog) -> str:
    datasets = catalog.datasets
    cards = "".join(C.dataset_card(v) for v in datasets)
    families = sorted({str(v.entry.get("spectro_family")) for v in datasets if v.entry.get("spectro_family")})
    domains = sorted({str(v.entry.get("domain")) for v in datasets if v.entry.get("domain")})
    tiers = sorted({v.tier for v in datasets})

    def opts(values: list[str]) -> str:
        return "".join(f'<option value="{esc(x)}">{esc(x)}</option>' for x in values)

    body = f"""
{C.nav("", "catalog")}
<section class="section-tight section-paper" style="padding-top:84px">
  <div class="container">
    {C.section_head("Browse", "The <em>catalog</em>", "Filter, sort, and search every dataset in the bank. Open a card for the full identity sheet.")}
  </div>
</section>
<section class="section" style="padding-top:32px">
  <div class="container">
    <div class="controls">
      <input id="q" type="search" placeholder="Search name, id, domain, target…" aria-label="Search datasets">
      <select id="f-tier" aria-label="Filter by tier"><option value="">all tiers</option>{opts(tiers)}</select>
      <select id="f-family" aria-label="Filter by family"><option value="">all families</option>{opts(families)}</select>
      <select id="f-domain" aria-label="Filter by domain"><option value="">all domains</option>{opts(domains)}</select>
      <select id="f-target" aria-label="Filter by target"><option value="">target or not</option><option value="yes">has target</option><option value="no">metadata-only</option></select>
      <select id="f-multi" aria-label="Filter by sources"><option value="">any sources</option><option value="yes">multi-source</option><option value="no">single-source</option></select>
      <select id="f-sort" aria-label="Sort"><option value="name">A → Z</option><option value="samples">most samples</option><option value="features">most wavelengths</option></select>
      <button class="btn-reset" id="reset">reset</button>
      <span class="count" id="count"></span>
    </div>
    <div class="cards" id="cards">{cards}</div>
    <div class="empty hidden" id="empty">No dataset matches these filters.</div>
  </div>
</section>
{C.footer("")}
"""
    return page(title="Catalog — nirs4all-datasets", rel="", body=body, scripts=_CATALOG_JS, active="catalog")


# Small vanilla-JS filter/sort over the rendered cards (UI only, not a chart lib).
_CATALOG_JS = """
<script>
(function(){
  var cards=[].slice.call(document.querySelectorAll('.ds-card'));
  var q=document.getElementById('q'),count=document.getElementById('count'),empty=document.getElementById('empty'),grid=document.getElementById('cards');
  var f={tier:document.getElementById('f-tier'),family:document.getElementById('f-family'),domain:document.getElementById('f-domain'),target:document.getElementById('f-target'),multi:document.getElementById('f-multi')};
  var sort=document.getElementById('f-sort');
  function apply(){
    var t=(q.value||'').trim().toLowerCase();var n=0;
    cards.forEach(function(c){
      var ok=true;
      if(t&&c.getAttribute('data-name').indexOf(t)<0)ok=false;
      if(f.tier.value&&c.getAttribute('data-tier')!==f.tier.value)ok=false;
      if(f.family.value&&c.getAttribute('data-family')!==f.family.value)ok=false;
      if(f.domain.value&&c.getAttribute('data-domain')!==f.domain.value)ok=false;
      if(f.target.value&&c.getAttribute('data-target')!==f.target.value)ok=false;
      if(f.multi.value&&c.getAttribute('data-multi')!==f.multi.value)ok=false;
      c.classList.toggle('hidden',!ok);if(ok)n++;
    });
    count.textContent=n+' / '+cards.length+' datasets';
    empty.classList.toggle('hidden',n>0);
  }
  function resort(){
    var key=sort.value;
    var vis=cards.slice();
    vis.sort(function(a,b){
      if(key==='name')return a.querySelector('h3').textContent.localeCompare(b.querySelector('h3').textContent);
      return (+b.getAttribute('data-'+key))-(+a.getAttribute('data-'+key));
    });
    vis.forEach(function(c){grid.appendChild(c);});
  }
  q.addEventListener('input',apply);
  Object.keys(f).forEach(function(k){f[k].addEventListener('change',apply);});
  sort.addEventListener('change',function(){resort();apply();});
  document.getElementById('reset').addEventListener('click',function(){q.value='';Object.keys(f).forEach(function(k){f[k].value='';});sort.value='name';resort();apply();});
  resort();apply();
})();
</script>
"""


# =============================================================================
# DATASET DETAIL (tier-respecting identity card)
# =============================================================================
def _kv(rows: list[tuple[str, Any]]) -> str:
    from .escape import kv_rows, table
    return table("", kv_rows(rows), css_class="kv").replace("<caption></caption>", "")


def _isnum(v: Any) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)


def _f(v: Any, *, nd: int = 4, suffix: str = "") -> str | None:
    """Format a metric value for a stat table, or None to omit the row. Bools -> yes/no."""
    if isinstance(v, bool):
        return "yes" if v else "no"
    if _isnum(v):
        return f"{num(v, nd=nd)}{suffix}"
    if isinstance(v, str) and v.strip():
        return esc(v)
    return None


def _pct(v: Any, nd: int = 0) -> str | None:
    return f"{v * 100:.{nd}f}%" if _isnum(v) else None


def _stat_table(title: str, pairs: list[tuple[str, str | None]]) -> str:
    """A compact key→value stat panel; rows whose value is None are dropped."""
    rows = "".join(f'<tr><th>{esc(label)}</th><td>{value}</td></tr>' for label, value in pairs if value is not None)
    return f'<div class="stat-card"><h4>{esc(title)}</h4><table class="stat-table">{rows}</table></div>' if rows else ""


def _zoom(svg: str, *, cls: str = "", max_w: int | None = None) -> str:
    """Wrap a chart so a click opens it large in the lightbox; cap its width so it never upscales
    (a small viewBox stretched to a full-width panel is what made the scree/scrolls render giant)."""
    style = f' style="max-width:{max_w}px"' if max_w else ""
    return f'<div class="chart {cls}"{style} tabindex="0" role="button" aria-label="enlarge chart">{svg}</div>'


def _sources_panel(view: DatasetView, rel: str) -> str:
    """Per spectral source: the spectra chart + a real scientific stat sheet (sampling / signal &
    quality / dimensionality) + the PCA scree. The numbers are the qualification metrics."""
    card = view.card or {}
    sources = card.get("sources") or []
    if not sources:
        return ""
    blocks: list[str] = []
    for s in sources:
        spec = s.get("spectral") or {}
        unit = s.get("axis_unit") or ""
        qual = spec.get("quality") or {}
        spacing = spec.get("spacing") or {}
        dim = spec.get("dimensionality") or {}
        pca = spec.get("pca") or {}

        head = (
            f'<div class="source-head"><h3>{esc(s.get("name") or s.get("source_id"))}</h3>'
            f'<span class="src-meta">{esc(s.get("source_id"))} · {esc(s.get("modality") or "—")}'
            f'{(" · " + esc(s.get("instrument_name"))) if s.get("instrument_name") else ""}</span></div>'
        )
        curve = spec.get("curve")
        chart = ""
        if view.show_variable_plots and curve and curve.get("axis"):
            chart = _zoom(charts.spectra_quantile(curve, title=f'{s.get("name") or s.get("source_id")} spectra', unit=unit, width=860), cls="chart-spectra", max_w=860)

        rng = f'{num(s.get("axis_min"))}–{num(s.get("axis_max"))} {esc(unit)}' if (_isnum(s.get("axis_min")) and _isnum(s.get("axis_max"))) else None
        sampling = _stat_table("Sampling", [
            ("Wavelengths", _f(s.get("n_variables"))),
            ("Axis range", rng),
            ("Mean spacing", _f(spacing.get("mean"), nd=3, suffix=f" {unit}") if spacing.get("mean") is not None else None),
            ("Grid", "uniform" if spacing.get("is_uniform") else ("irregular" if spacing.get("is_uniform") is False else None)),
            ("Observations", _f(s.get("n_observations"))),
        ])
        signal = _stat_table("Signal & quality", [
            ("Value range", f'{_f(spec.get("value_min"), nd=3)} – {_f(spec.get("value_max"), nd=3)}' if _isnum(spec.get("value_min")) and view.show_value_stats else None),
            ("Mean range", f'{_f(spec.get("mean_min"), nd=3)} – {_f(spec.get("mean_max"), nd=3)}' if _isnum(spec.get("mean_min")) and view.show_value_stats else None),
            ("Noise SNR", _f(qual.get("noise_proxy_db"), nd=1, suffix=" dB")),
            ("Dynamic range", _f(qual.get("dynamic_range"), nd=3)),
            ("Smoothness", _f(qual.get("smoothness"), nd=4)),
            ("Saturated", _pct(qual.get("saturation_fraction"), nd=1)),
            ("X-outliers", _f(spec.get("n_outliers"))),
        ])
        dimensionality = _stat_table("Dimensionality (PCA)", [
            ("Effective rank", _f(dim.get("effective_rank"), nd=2)),
            ("PCs → 95% var", _f(dim.get("n_components_95"))),
            ("PCs → 99% var", _f(dim.get("n_components_99"))),
            ("Top-10 cum. var", _pct(dim.get("cumulative_top10"), nd=1)),
        ])
        scree = ""
        evr = pca.get("explained_variance_ratio") or []
        if view.show_variable_plots and evr:
            scree = _zoom(charts.scree([float(x) for x in evr if _isnum(x)], width=420), max_w=420)

        blocks.append(
            f'<div class="source-card">{head}{chart}'
            f'<div class="stat-grid">{sampling}{signal}{dimensionality}</div>{scree}</div>'
        )
    return f'<section class="panel wide"><h2>Spectral sources</h2><div class="panel-body">{"".join(blocks)}</div></section>'


def _var_has_data(v: dict[str, Any]) -> bool:
    """Whether a variable carries any usable values (drops all-missing / no-class columns)."""
    stats = v.get("stats") or {}
    n, missing = stats.get("n") or 0, stats.get("n_missing") or 0
    all_missing = bool(n) and missing >= n
    no_class = v.get("type") != "numeric" and (stats.get("n_classes") or 0) < 1
    return not (all_missing or no_class)


def _variable_card(view: DatasetView, v: dict[str, Any]) -> str:
    """One variable: a distribution chart (only when there is spread) + its real statistics."""
    stats = v.get("stats") or {}
    shape = v.get("shape") or {}
    balance = v.get("balance") or {}
    is_num = v.get("type") == "numeric"
    name = v.get("name") or "—"
    unit = v.get("unit")
    tag = " · ".join(filter(None, [v.get("role"), v.get("type"), unit]))

    chart = ""
    if view.show_variable_plots:
        if is_num and view.show_value_stats:
            hist = v.get("histogram") or {}
            if hist.get("counts") and len([c for c in hist["counts"] if c]) >= 2:
                chart = charts.histogram_bins(hist["edges"], hist["counts"], title=f"{name} distribution", unit=unit or "", width=440)
            elif _isnum(stats.get("min")) and stats.get("min") != stats.get("max"):
                chart = charts.boxplot(stats, title=f"{name} distribution", unit=unit or "", width=440)
        elif not is_num and (stats.get("n_classes") or 0) >= 2:
            tc = stats.get("top_classes") or []
            chart = charts.bar_chart([(str(c.get("name")), float(c.get("count") or 0)) for c in tc], title=f"{name} classes", top_n=10, width=440)

    if is_num and view.show_value_stats:
        rows = [
            ("n / missing", f'{num(stats.get("n"))} / {num(stats.get("n_missing"))}'),
            ("Mean ± SD", f'{_f(stats.get("mean"), nd=4)} ± {_f(stats.get("std"), nd=3)}' if _isnum(stats.get("mean")) else None),
            ("Median", _f(stats.get("median"), nd=4)),
            ("Range", f'{_f(stats.get("min"), nd=4)} – {_f(stats.get("max"), nd=4)}' if _isnum(stats.get("min")) else None),
            ("CV", _f(shape.get("cv"), nd=3)),
            ("Skew / kurtosis", f'{_f(shape.get("skewness"), nd=2)} / {_f(shape.get("kurtosis"), nd=2)}' if _isnum(shape.get("skewness")) else None),
            ("Normal?", _f(shape.get("is_normal")) if shape.get("is_normal") is not None else None),
        ]
    elif is_num:
        rows = [("n / missing", f'{num(stats.get("n"))} / {num(stats.get("n_missing"))}'), ("Values", "hidden (token-gated)")]
    else:
        top = (stats.get("top_classes") or [{}])[0]
        rows = [
            ("n / missing", f'{num(stats.get("n"))} / {num(stats.get("n_missing"))}'),
            ("Classes", _f(stats.get("n_classes"))),
            ("Balance (entropy)", _f(balance.get("normalized_entropy"), nd=2)),
            ("Imbalance ratio", _f(balance.get("imbalance_ratio"), nd=1)),
            ("Top class", f'{esc(top.get("name"))} ({num(top.get("count"))})' if top.get("name") is not None else None),
        ]

    body = "".join(f'<tr><th>{esc(label)}</th><td>{value}</td></tr>' for label, value in rows if value is not None)
    chart_html = _zoom(chart, cls="var-chart", max_w=440) if chart else ""
    return (
        f'<div class="var-card"><div class="var-card-head"><h4>{esc(name)}</h4>'
        f'<span class="var-tag">{esc(tag)}</span></div>{chart_html}<table class="stat-table">{body}</table></div>'
    )


def _variables_panel(view: DatasetView, rel: str) -> str:
    card = view.card or {}
    variables = card.get("variables") or []
    if not variables:
        note = "This dataset is metadata-only (no declared prediction targets)." if view.has_card else ""
        return f'<section class="panel"><h2>Variables</h2><div class="panel-body"><p class="dl-note">{esc(note or "No variables present.")}</p></div></section>' if note else ""

    usable = [v for v in variables if _var_has_data(v)]
    omitted = len(variables) - len(usable)
    targets = [v for v in usable if v.get("role") == "target"]
    meta_all = [v for v in usable if v.get("role") != "target"]
    # a single-valued metadata column (e.g. unit = "nanometer") is not a distribution — list it
    # compactly as key = value rather than a dataviz card with a pointless 1-bar chart.
    meta = [v for v in meta_all if not _is_constant(v)]
    constant = [v for v in meta_all if _is_constant(v)]
    blocks: list[str] = []
    if targets:
        blocks.append(f'<h3 class="var-group">Targets <span>{len(targets)}</span></h3>')
        blocks.append(f'<div class="var-grid">{"".join(_variable_card(view, v) for v in targets)}</div>')
    if meta:
        blocks.append(f'<h3 class="var-group">Metadata <span>{len(meta)}</span></h3>')
        blocks.append(f'<div class="var-grid">{"".join(_variable_card(view, v) for v in meta)}</div>')
    if constant:
        items = "".join(f'<li><span>{esc(v.get("name"))}</span><b>{_constant_value(view, v)}</b></li>' for v in constant)
        blocks.append(f'<details class="const-meta"><summary>Constant metadata <span>{len(constant)}</span></summary><ul>{items}</ul></details>')
    if omitted:
        blocks.append(f'<p class="dl-note">{omitted} variable(s) omitted (no recorded values).</p>')
    if not targets and not meta and not constant:
        blocks.append('<p class="dl-note">No variable carries recorded values.</p>')
    return f'<section class="panel wide"><h2>Variables</h2><div class="panel-body">{"".join(blocks)}</div></section>'


def _is_constant(v: dict[str, Any]) -> bool:
    """A variable with a single distinct value (a constant column — no distribution to plot)."""
    stats = v.get("stats") or {}
    if v.get("type") == "numeric":
        return _isnum(stats.get("min")) and stats.get("min") == stats.get("max")
    return (stats.get("n_classes") or 0) <= 1


def _constant_value(view: DatasetView, v: dict[str, Any]) -> str:
    """The single value of a constant column (or a token-gated placeholder)."""
    if not view.show_value_stats:
        return "—"
    stats = v.get("stats") or {}
    if v.get("type") == "numeric":
        return f'<span class="numt">{num(stats.get("min"))}{(" " + esc(v.get("unit"))) if v.get("unit") else ""}</span>'
    top = (stats.get("top_classes") or [{}])[0]
    return esc(top.get("name")) if top.get("name") is not None else "—"


def _alignment_panel(view: DatasetView) -> str:
    card = view.card or {}
    al = card.get("alignment") or {}
    if not al:
        return ""
    reps = al.get("reps_per_sample") or {}
    rows: list[tuple[str, Any]] = [
        ("Alignment level", al.get("level")),
        ("Sample id available", "yes" if al.get("sample_id_available") else "no"),
        ("Samples", num(al.get("n_samples"))),
        ("Observations (total)", num(al.get("n_observations_total"))),
    ]
    if reps:
        rows.append(("Reps per sample", f'min {num(reps.get("min"))} · mean {num(reps.get("mean"))} · max {num(reps.get("max"))}'))
    return f'<section class="panel"><h2>Alignment</h2><div class="panel-body">{_kv(rows)}</div></section>'


def _splits_panel(view: DatasetView) -> str:
    card = view.card or {}
    splits = card.get("splits") or []
    if not splits:
        return ""
    items: list[str] = []
    for s in splits:
        parts = s.get("partitions") or {}
        parts_str = ", ".join(f"{esc(k)}: {num(val)}" for k, val in parts.items()) or "—"
        items.append(f'<tr><th>{esc(s.get("name"))}</th><td>{parts_str} <span class="badge neutral" style="margin-left:6px">documented · not applied</span></td></tr>')
    return f'<section class="panel"><h2>Splits</h2><div class="panel-body"><table class="kv"><tbody>{"".join(items)}</tbody></table></div></section>'


def _provenance_panel(view: DatasetView) -> str:
    card = view.card or {}
    prov = card.get("provenance") or {}
    rows: list[str] = []
    if prov.get("contributor"):
        rows.append(f'<tr><th>Contributor</th><td>{esc(prov.get("contributor"))}</td></tr>')
    if prov.get("reference_method"):
        rows.append(f'<tr><th>Reference method</th><td>{esc(prov.get("reference_method"))}</td></tr>')
    if prov.get("conversion_status"):
        rows.append(f'<tr><th>Conversion status</th><td>{esc(prov.get("conversion_status"))}</td></tr>')
    for src in prov.get("origin_sources") or []:
        label = f'{src.get("kind")} [{src.get("access")}]'
        title = f' — {esc(src.get("title"))}' if src.get("title") else ""
        lic = f' <span class="badge neutral">{esc(src.get("license"))}</span>' if src.get("license") else ""
        rows.append(f'<tr><th>Origin · {esc(label)}</th><td>{locator_link(src.get("locator"))}{title}{lic}</td></tr>')
    for pub in prov.get("publications") or []:
        if pub.get("doi"):
            t = f' — {esc(pub.get("title"))}' if pub.get("title") else ""
            yr = f' ({esc(pub.get("year"))})' if pub.get("year") else ""
            rows.append(f'<tr><th>Publication</th><td>{locator_link(pub.get("doi"))}{t}{yr}</td></tr>')
    if not rows:
        return ""
    return f'<section class="panel wide"><h2>Provenance &amp; citation</h2><div class="panel-body"><table class="kv"><tbody>{"".join(rows)}</tbody></table></div></section>'


def _governance_integrity_panel(view: DatasetView) -> str:
    card = view.card or {}
    gov = card.get("governance") or {}
    integ = card.get("integrity") or {}
    versions = card.get("versions") or {}
    rows: list[tuple[str, Any]] = [
        ("Tier", gov.get("tier") or view.tier),
        ("License", gov.get("license")),
        ("Permitted use", gov.get("permitted_use")),
        ("Access policy", gov.get("access_policy")),
        ("Redistribution", gov.get("redistribution_rights")),
        ("Content version", versions.get("content")),
        ("Schema / protocol", versions.get("schema_protocol")),
    ]
    doi = view.entry.get("doi")
    if doi:
        rows.append(("DOI", locator_link(doi)))
    for label, key in (("Content hash", "content_hash"), ("Processing hash", "processing_hash"), ("Metadata hash", "metadata_hash")):
        val = integ.get(key)
        if val:
            rows.append((label, f'<code style="font-size:.78rem">{esc(str(val)[:16])}…</code>'))
    return f'<section class="panel"><h2>Governance &amp; integrity</h2><div class="panel-body">{_kv(rows)}</div></section>'


def _tier_note(view: DatasetView) -> str:
    if view.tier == "private":
        return (
            '<div class="tier-note private"><span class="ico">&#128274;</span><div>'
            "<strong>Private dataset.</strong> Full metadata and metrics are shown, but the bytes are not "
            "redistributed here — exporting the data requires a Dataverse token. The identity card carries "
            "no spectra, only descriptive statistics.</div></div>"
        )
    if view.tier == "anonymized":
        return (
            '<div class="tier-note anonymized"><span class="ico">&#127917;</span><div>'
            "<strong>Anonymized dataset.</strong> Variable names are masked (<code>var_NNN</code>) and numeric "
            "targets are normalized; the original description, keywords, and per-variable plots are withheld. "
            "Only the structure and normalized statistics are shown.</div></div>"
        )
    return ""


def _downloads(view: DatasetView, rel: str) -> str:
    """Metadata downloads — only for public datasets (the card itself holds no bytes; bytes never served)."""
    if not view.show_metadata_downloads or not view.has_card:
        if view.has_card:
            return '<p class="dl-note">Metadata downloads are available for public datasets only. The dataset bytes are never served here — fetch them from the origin / DOI above.</p>'
        return ""
    return (
        '<div class="dl-row">'
        f'<a class="dl-btn" href="{rel}data/{esc(view.id)}.card.json">card.json</a>'
        f'<a class="dl-btn" href="{rel}data/{esc(view.id)}.croissant.json">croissant.json</a>'
        '<span class="dl-note">Identity metadata only — the dataset bytes live at the origin / DOI.</span>'
        '</div>'
    )


def render_dataset(view: DatasetView) -> str:
    rel = "../"
    e = view.entry
    domain = e.get("domain") or ""
    family = e.get("spectro_family") or ""

    badges = [C.tier_badge(view.tier)]
    if (e.get("n_sources") or 0) > 1:
        badges.append(C.badge(f'{e.get("n_sources")} sources', "info"))
    if (e.get("n_targets") or 0) == 0:
        badges.append(C.badge("metadata-only", "neutral"))
    if e.get("has_split"):
        badges.append(C.badge("native split", "neutral"))
    if not view.has_card:
        badges.append(C.badge("card pending", "warn"))
    elif view.is_stale:
        badges.append(C.badge("stale card", "warn"))

    keywords = "".join(f'<span class="kw">{esc(k)}</span>' for k in view.keywords)
    desc = f'<p class="ds-sub">{esc(view.description)}</p>' if view.description else ""
    tags = f'<div class="ds-tags">{keywords}</div>' if keywords else ""

    if view.has_card:
        kpis = C.kpi_strip([
            (num(e.get("n_samples")) if e.get("n_samples") is not None else "—", "samples"),
            (num(e.get("n_features_total")) if e.get("n_features_total") is not None else "—", "wavelengths"),
            (num(e.get("n_sources") or 0), "sources"),
            (num(e.get("n_targets") or 0), "targets"),
            (num(e.get("n_metadata") or 0), "metadata"),
            (esc(family or "—"), "family"),
        ])
        panels = "".join([
            _sources_panel(view, rel),
            _variables_panel(view, rel),
            _alignment_panel(view),
            _splits_panel(view),
            _provenance_panel(view),
            _governance_integrity_panel(view),
        ])
        content = f'<div class="panel-grid">{panels}</div>'
    else:
        kpis = ""
        rows = _kv([
            ("Domain", domain),
            ("Family", family),
            ("License", e.get("license")),
            ("Tier", view.tier),
            ("Sources", num(e.get("n_sources") or 0)),
            ("Targets", num(e.get("n_targets") or 0)),
            ("DOI", locator_link(e.get("doi")) if e.get("doi") else None),
        ])
        content = (
            '<div class="panel-grid"><section class="panel wide"><h2>Identity card pending</h2>'
            '<div class="panel-body"><p class="dl-note">This dataset is cataloged with full provenance and '
            'governance, but its statistical identity card has not been computed yet. The descriptor metadata '
            f'below is authoritative.</p>{rows}</div></section></div>'
        )

    body = f"""
{C.nav(rel, "catalog")}
<section class="ds-hero section-paper">
  <div class="container">
    <a class="back" href="{rel}catalog.html">&larr; Back to the catalog</a>
    <div class="ds-tags" style="margin-bottom:12px">{"".join(badges)}</div>
    <h1 class="ds-title">{esc(view.name)}</h1>
    <div class="ds-domain" style="margin-top:8px;color:var(--teal-d);font-size:.8rem;text-transform:uppercase;letter-spacing:.06em;font-weight:600">{esc(domain)}{(" · " + esc(family)) if family else ""}</div>
    {desc}
    {tags}
    {_tier_note(view)}
  </div>
</section>
<section class="section" style="padding-top:36px">
  <div class="container">
    {kpis}
    <div style="margin-top:26px">{content}</div>
    <section class="panel wide" style="margin-top:20px"><h2>Load this dataset</h2><div class="panel-body">{C.load_snippet(view.id, view.tier)}<div style="margin-top:16px">{_downloads(view, rel)}</div></div></section>
  </div>
</section>
{C.footer(rel)}
"""
    return page(title=f"{esc(view.name)} — nirs4all-datasets", rel=rel, body=body, active="catalog")
