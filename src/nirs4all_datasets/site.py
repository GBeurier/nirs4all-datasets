"""Generate a self-contained interactive static site for the dataset catalog.

Reads ``catalog/datasets.yaml`` + each ``datasets/<id>/card.json`` (and the descriptor for
provenance/governance), and writes a standalone ``site/``:

* ``index.html`` — a summary header plus a client-side **searchable / filterable / sortable** table
  of every dataset. The row data is embedded inline (no ``fetch``) so the page works from ``file://``
  as well as under ``python -m http.server``.
* ``dataset/<id>.html`` — the full identity card: KPIs, plots, statistics tables (spectral,
  dimensionality, train↔test shift, targets, quality), provenance & governance, and downloads.
* ``assets/<id>/*.png`` and ``data/<id>.{card,croissant}.json`` — copied per dataset.

Pure rendering: no nirs4all import, no recomputation — it only formats already-generated artifacts.
"""
from __future__ import annotations

import html
import json
import math
import shutil
from pathlib import Path
from typing import Any

import yaml

_ACCENT = "#0b7285"


# --------------------------------------------------------------------------- helpers
def _esc(value: Any) -> str:
    """HTML-escape a scalar for text/attribute context."""
    if value is None:
        return ""
    return html.escape(str(value), quote=True)


def _inline_json(obj: Any) -> str:
    """JSON for embedding inside a ``<script>`` tag (neutralizes ``</script>`` and HTML comments)."""
    return json.dumps(obj, allow_nan=False).replace("</", "<\\/").replace("<!--", "<\\!--")


def _num(value: Any, nd: int = 4) -> str:
    if isinstance(value, bool) or value is None:
        return "—"
    if isinstance(value, int):
        return f"{value:,}"
    if isinstance(value, float):
        return "—" if not math.isfinite(value) else f"{value:.{nd}g}"
    return _esc(value)


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def _kv_rows(rows: list[tuple[str, Any]]) -> str:
    """Render a 2-column key/value table body, dropping rows whose value is None/empty."""
    out = []
    for key, value in rows:
        if value in (None, "", [], {}):
            continue
        rendered = value if (isinstance(value, str) and value.startswith("<")) else _esc(value)
        out.append(f"<tr><th>{_esc(key)}</th><td>{rendered}</td></tr>")
    return "".join(out)


def _table(caption: str, body: str) -> str:
    return f'<table class="kv"><caption>{_esc(caption)}</caption><tbody>{body}</tbody></table>' if body else ""


# --------------------------------------------------------------------------- summary record (index)
def _summary_record(entry: dict[str, Any], card: dict[str, Any]) -> dict[str, Any]:
    inv = card.get("inventory") or {}
    spec = card.get("spectral") or {}
    dim = card.get("dimensionality") or {}
    qual = card.get("quality") or {}
    wl = spec.get("wavelength_range")
    return {
        "id": entry["id"],
        "name": entry.get("name") or entry["id"],
        "version": entry.get("version") or "",
        "domain": entry.get("domain") or "",
        "task": entry.get("task_type") or (card.get("targets") or {}).get("task_type") or "",
        "targets": ", ".join(entry.get("targets") or []),
        "n_samples": inv.get("n_samples") if inv.get("n_samples") is not None else entry.get("n_samples"),
        "n_features": inv.get("n_features") if inv.get("n_features") is not None else entry.get("n_features"),
        "n_classes": inv.get("num_classes"),
        "signal": spec.get("signal_type") or "",
        "unit": spec.get("wavelength_unit") or "",
        "wl": f"{wl[0]:.0f}–{wl[1]:.0f}" if isinstance(wl, list) and len(wl) == 2 else "",
        "eff_rank": dim.get("effective_rank"),
        "has_nan": bool(qual.get("has_nan")),
        "license": entry.get("license") or "",
        "visibility": entry.get("visibility") or "",
        "stale": bool(entry.get("is_stale")),
    }


# --------------------------------------------------------------------------- per-dataset page
def _kpi(label: str, value: str) -> str:
    return f'<div class="kpi"><div class="kpi-v">{value}</div><div class="kpi-l">{_esc(label)}</div></div>'


def _plots_html(dataset_id: str, assets: dict[str, str]) -> str:
    titles = {
        "spectra_envelope": "Mean spectrum ± std",
        "target_distribution": "Target distribution",
        "pca_scatter": "PCA projection",
        "class_spectra": "Per-class / per-quartile spectra",
        "train_test_overlay": "Train vs test mean",
    }
    cards = []
    for key, title in titles.items():
        if key in assets:
            cards.append(f'<figure><img loading="lazy" src="../assets/{_esc(dataset_id)}/{key}.png" alt="{_esc(title)}"><figcaption>{_esc(title)}</figcaption></figure>')
    return f'<div class="plots">{"".join(cards)}</div>' if cards else ""


def _shift_html(shift: dict[str, Any]) -> str:
    if not shift:
        return ""
    target = shift.get("target") or {}
    cov = shift.get("covariate") or {}
    rows: list[tuple[str, Any]] = []
    if "standardized_mean_diff" in target:
        rows += [
            ("Target std. mean diff", _num(target.get("standardized_mean_diff"))),
            ("Target KS (p)", f"{_num(target.get('ks_statistic'))} ({_num(target.get('ks_p'))})"),
            ("Target Wasserstein", _num(target.get("wasserstein"))),
        ]
    elif "jensen_shannon" in target:
        rows += [
            ("Class Jensen–Shannon", _num(target.get("jensen_shannon"))),
            ("Max class-proportion Δ", _num(target.get("max_abs_proportion_delta"))),
            ("Unseen in test", ", ".join(target.get("unseen_in_test") or []) or "—"),
            ("Unseen in train", ", ".join(target.get("unseen_in_train") or []) or "—"),
        ]
    if cov:
        rows += [
            ("Covariate centroid dist. (σ)", _num(cov.get("pc_space_centroid_distance_std"))),
            ("PC1 KS (p)", f"{_num(cov.get('pc1_ks_statistic'))} ({_num(cov.get('pc1_ks_p'))})"),
        ]
    return _table("Train ↔ test shift", _kv_rows(rows))


def _targets_html(targets: dict[str, Any]) -> str:
    if not targets or targets.get("note"):
        note = (targets or {}).get("note")
        return _table("Targets", _kv_rows([("Note", note)])) if note else ""
    rows: list[tuple[str, Any]] = [("Task", targets.get("task_type"))]
    stats = targets.get("stats") or {}
    for key in ("mean", "std", "min", "max", "cv"):
        if key in stats:
            rows.append((f"Target {key}", _num(stats.get(key))))
    shape = targets.get("shape") or {}
    if shape:
        rows += [("Skewness", _num(shape.get("skewness"))), ("Kurtosis", _num(shape.get("kurtosis"))), ("Normal?", shape.get("is_normal"))]
    dist = targets.get("class_distribution") or {}
    if dist:
        rows.append(("Class distribution", _esc(", ".join(f"{k}:{v}" for k, v in dist.items()))))
    bal = targets.get("balance") or {}
    if bal:
        rows += [("Classes", bal.get("n_classes")), ("Normalized entropy", _num(bal.get("normalized_entropy"))), ("Imbalance ratio", _num(bal.get("imbalance_ratio")))]
    parts = targets.get("partitions") or {}
    if isinstance(parts, dict) and parts:
        summary = []
        for name, val in parts.items():
            if isinstance(val, dict) and "mean" in val:
                summary.append(f"{name}: μ={_num(val.get('mean'))} σ={_num(val.get('sd') or val.get('std'))} n={val.get('nsample') or val.get('n')}")
            elif isinstance(val, dict):
                summary.append(f"{name}: " + ", ".join(f"{k}={v}" for k, v in val.items()))
        rows.append(("Per partition", "<br>".join(_esc(s) for s in summary)))
    return _table("Targets", _kv_rows(rows))


def _locator_link(locator: Any) -> str:
    """Render a source/publication locator as a link (DOI -> doi.org, http(s) as-is, else plain)."""
    loc = str(locator or "")
    if loc.startswith("http"):
        return f'<a href="{_esc(loc)}">{_esc(loc)}</a>'
    if loc.startswith("10."):
        return f'<a href="https://doi.org/{_esc(loc)}">{_esc(loc)}</a>'
    return _esc(loc)


def _origin_html(descriptor: dict[str, Any], card: dict[str, Any]) -> str:
    """Where the data actually lives + how to cite it (origin sources, papers, provenance chain).

    Metadata only -- it points to each dataset's licensed home, it never serves the bytes, so it is
    license-respecting for restricted datasets too.
    """
    sources = descriptor.get("sources") or []
    pubs = ((descriptor.get("datacite") or {}).get("related_publications")) or []
    citation = descriptor.get("citation")
    if not sources and not pubs and not citation:
        return ""
    rows: list[str] = []
    for src in sources:
        label = f"{src.get('kind')} [{src.get('access')}/{src.get('mode')}]" + (f" — {src.get('title')}" if src.get("title") else "")
        rows.append(f"<tr><th>{_esc(label)}</th><td>{_locator_link(src.get('locator'))}</td></tr>")
    for pub in pubs:
        if pub.get("doi"):
            rows.append(f"<tr><th>Publication</th><td>{_locator_link(pub['doi'])}</td></tr>")
    if citation and not pubs:
        rows.append(f"<tr><th>Citation</th><td>{_esc(citation)}</td></tr>")
    chain = ((card.get("integrity") or {}).get("traceability")) or {}
    if chain:
        summary = f"{len(chain.get('origin_locators') or [])} origin → {len(chain.get('raw_sha256') or [])} raw → {len(chain.get('canonical_sha256') or {})} canonical → card"
        rows.append(f"<tr><th>Provenance chain</th><td>{_esc(summary)}</td></tr>")
    return _table("Origin &amp; citation", "".join(rows))


def _dataset_page(entry: dict[str, Any], card: dict[str, Any], descriptor: dict[str, Any]) -> str:
    did = entry["id"]
    ident = card.get("identity") or {}
    inv = card.get("inventory") or {}
    spec = card.get("spectral") or {}
    dim = card.get("dimensionality") or {}
    qual = card.get("quality") or {}
    gov = descriptor.get("governance") or {}
    prov = descriptor.get("provenance") or {}
    inst = descriptor.get("instrument") or {}
    name = ident.get("name") or entry.get("name") or did
    version = ident.get("version") or entry.get("version")
    dataverse_version = (descriptor.get("dataverse") or {}).get("dataset_version")

    badges = "".join(
        f'<span class="badge">{_esc(b)}</span>'
        for b in [(f"v{version}" if version else None), entry.get("task_type"), entry.get("visibility"), entry.get("license")]
        if b
    )
    if entry.get("is_stale"):
        badges += '<span class="badge warn">stale card</span>'
    if not card:
        badges += '<span class="badge warn">card pending</span>'

    wl = spec.get("wavelength_range")
    kpis = "".join([
        _kpi("samples", _num(inv.get("n_samples"))),
        _kpi("wavelengths", _num(inv.get("n_features"))),
        _kpi("sources", _num(inv.get("n_sources"))),
        _kpi("classes" if inv.get("num_classes") else "CV folds", _num(inv.get("num_classes") if inv.get("num_classes") else inv.get("n_folds"))),
        _kpi("signal", _esc(spec.get("signal_type") or "—")),
        _kpi("axis", _esc(f"{wl[0]:.0f}–{wl[1]:.0f} {spec.get('wavelength_unit')}" if isinstance(wl, list) and len(wl) == 2 else (spec.get("wavelength_unit") or "—"))),
    ])

    spacing = spec.get("spacing") or {}
    spectral_tbl = _table("Spectral", _kv_rows([
        ("Wavelengths", inv.get("n_features")),
        ("Range", f"{wl[0]:.1f}–{wl[1]:.1f} {spec.get('wavelength_unit')}" if isinstance(wl, list) and len(wl) == 2 else None),
        ("Mean spacing", f"{_num(spacing.get('mean'))} {spec.get('spacing_unit') or ''}" if spacing.get("mean") is not None else None),
        ("Uniform grid", spacing.get("is_uniform")),
        ("Signal type", spec.get("signal_type")),
        ("Signal confidence", _num(spec.get("signal_type_confidence"))),
        ("Detection note", spec.get("signal_type_reason")),
    ]))
    dim_tbl = _table("Dimensionality (PCA)", _kv_rows([
        ("Effective rank", _num(dim.get("effective_rank"))),
        ("PCs → 95% var", dim.get("n_components_95")),
        ("PCs → 99% var", dim.get("n_components_99")),
        ("Top-10 cumulative var", _num(dim.get("cumulative_variance_top10"))),
        ("PC1 explained var", _num((dim.get("explained_variance_ratio") or [None])[0])),
        ("Rows / components used", f"{dim.get('n_rows_used')} / {dim.get('n_components_computed')}" if dim.get("n_rows_used") else None),
    ])) if dim else ""
    outl = qual.get("x_outliers") or {}
    quality_tbl = _table("Quality", _kv_rows([
        ("Contains NaN", qual.get("has_nan")),
        ("Noise proxy (dB)", _num((qual.get("spectral") or {}).get("noise_proxy_db"))),
        ("Dynamic range", _num((qual.get("spectral") or {}).get("dynamic_range"))),
        ("X-outliers", f"{outl.get('n_excluded')}/{outl.get('n_samples')} ({_num(outl.get('exclusion_rate'))}) via {outl.get('method')}" if outl else None),
    ]))
    gov_tbl = _table("Provenance & governance", _kv_rows([
        ("Contributor", prov.get("contributor")),
        ("Reference method", prov.get("reference_method")),
        ("Instrument", " ".join(str(x) for x in [inst.get("vendor"), inst.get("model")] if x) or None),
        ("Modality", inst.get("modality")),
        ("License", gov.get("license")),
        ("Visibility", gov.get("visibility")),
        ("Confidentiality", gov.get("confidentiality_class")),
        ("Redistribution", gov.get("redistribution_rights")),
        ("Catalog version", version),
        ("DOI", f'<a href="https://doi.org/{_esc(ident.get("doi"))}">{_esc(ident.get("doi"))}</a>' if ident.get("doi") else None),
        ("Dataverse version", dataverse_version),
        ("Citation", descriptor.get("citation")),
    ]))

    warnings = card.get("warnings") or []
    warn_html = f'<div class="warnings"><strong>Warnings:</strong> {_esc("; ".join(warnings))}</div>' if warnings else ""
    keywords = " ".join(f'<span class="kw">{_esc(k)}</span>' for k in (descriptor.get("keywords") or []))
    downloads_html = (
        f'<div class="downloads"><strong>Downloads:</strong> <a href="../data/{_esc(did)}.card.json">card.json</a>'
        f' <a href="../data/{_esc(did)}.croissant.json">croissant.json</a></div>'
        if card
        else '<div class="downloads"><em>Identity card pending — dataset cataloged with full provenance; statistical diagnostics not yet computed.</em></div>'
    )

    return _PAGE_TMPL.format(
        title=_esc(name),
        accent=_ACCENT,
        rel="../",
        body=f"""
<a class="back" href="../index.html">← catalog</a>
<h1>{_esc(name)}</h1>
<p class="domain">{_esc(entry.get('domain') or '')}</p>
<div class="badges">{badges}</div>
<p class="desc">{_esc(ident.get('description') or descriptor.get('description') or '')}</p>
<div class="keywords">{keywords}</div>
{warn_html}
<div class="kpis">{kpis}</div>
{_plots_html(did, card.get('assets') or {})}
<div class="grid">{spectral_tbl}{dim_tbl}{_shift_html(card.get('shift') or {})}{_targets_html(card.get('targets') or {})}{quality_tbl}{gov_tbl}{_origin_html(descriptor, card)}</div>
{downloads_html}
""",
    )


# --------------------------------------------------------------------------- index page
def _index_page(records: list[dict[str, Any]]) -> str:
    n = len(records)
    n_reg = sum(1 for r in records if r["task"] == "regression")
    n_clf = n - n_reg
    total_samples = sum(int(r["n_samples"]) for r in records if isinstance(r.get("n_samples"), int))
    n_families = len({r["domain"] for r in records if r["domain"]})
    summary = "".join([
        _kpi("datasets", _num(n)),
        _kpi("regression", _num(n_reg)),
        _kpi("classification", _num(n_clf)),
        _kpi("families", _num(n_families)),
        _kpi("total spectra", _num(total_samples)),
    ])
    return _PAGE_TMPL.format(
        title="nirs4all datasets",
        accent=_ACCENT,
        rel="",
        body=f"""
<h1>nirs4all datasets</h1>
<p class="desc">Curated NIRS reference datasets — statistical identity cards for benchmarking and publication.</p>
<div class="kpis">{summary}</div>
<div class="controls">
  <input id="q" type="search" placeholder="Search name, domain, target…" aria-label="search">
  <select id="f-task"><option value="">all tasks</option></select>
  <select id="f-domain"><option value="">all families</option></select>
  <select id="f-signal"><option value="">all signals</option></select>
  <select id="f-unit"><option value="">all units</option></select>
  <button id="reset">reset</button>
  <span id="count" class="count"></span>
</div>
<div class="top-scroll" id="topScroll"><div class="top-scroll-inner" id="topScrollInner"></div></div>
<div class="table-wrap" id="tableWrap">
<table id="catalog">
<colgroup><col style="width:19%"><col style="width:8%"><col style="width:8%"><col style="width:5%"><col style="width:6%"><col style="width:5%"><col style="width:8%"><col style="width:5%"><col style="width:8%"><col style="width:4%"><col style="width:6%"><col style="width:4%"><col style="width:8%"><col style="width:6%"></colgroup>
<thead><tr>
  <th data-k="name" class="col-name">Dataset</th><th data-k="domain">Family</th><th data-k="task">Task</th><th data-k="version">Ver.</th>
  <th data-k="n_samples" class="num">Samples</th><th data-k="n_features" class="num">λ</th>
  <th data-k="wl">Range</th><th data-k="unit">Unit</th><th data-k="signal">Signal</th>
  <th data-k="n_classes" class="num">Cls</th><th data-k="eff_rank" class="num">Eff.rank</th>
  <th data-k="has_nan">NaN</th><th data-k="license">License</th><th data-k="visibility">Vis.</th>
</tr></thead><tbody id="rows"></tbody></table>
</div>
<script>const DATA = {_inline_json(records)};</script>
<script src="app.js"></script>
""",
    )


# --------------------------------------------------------------------------- build
def build_site(root: str | Path, out_dir: str | Path) -> Path:
    """Build the static site from the catalog + cards into ``out_dir`` (regenerated wholesale)."""
    root = Path(root)
    out = Path(out_dir)
    if out.exists():
        shutil.rmtree(out)
    (out / "dataset").mkdir(parents=True)
    (out / "assets").mkdir()
    (out / "data").mkdir()

    catalog = yaml.safe_load((root / "catalog" / "datasets.yaml").read_text(encoding="utf-8")) if (root / "catalog" / "datasets.yaml").exists() else {"datasets": []}
    records: list[dict[str, Any]] = []
    for entry in catalog.get("datasets", []):
        dataset_dir = root / "datasets" / entry["id"]
        descriptor_path = root / "catalog" / "datasets" / f"{entry['id']}.yaml"
        descriptor = (yaml.safe_load(descriptor_path.read_text(encoding="utf-8")) or {}) if descriptor_path.exists() else {}
        # Use the card only when present AND fresh: a stale card holds wrong stats for the current
        # descriptor, and a cardless dataset (e.g. v2.0 cataloged, diagnostics not yet computed) has
        # none. Both render descriptor-driven (the page flags "card pending"); never show wrong stats.
        card = _read_json(dataset_dir / "card.json") if (entry.get("has_card") and not entry.get("is_stale")) else None
        card = card or {}
        if card:
            assets_src = dataset_dir / "assets"
            if assets_src.exists():
                shutil.copytree(assets_src, out / "assets" / entry["id"])
            for suffix in ("card.json", "croissant.json"):
                src = dataset_dir / suffix
                if src.exists():
                    shutil.copy2(src, out / "data" / f"{entry['id']}.{suffix}")
        (out / "dataset" / f"{entry['id']}.html").write_text(_dataset_page(entry, card, descriptor), encoding="utf-8")
        records.append(_summary_record(entry, card))

    records.sort(key=lambda r: r["name"].lower())
    (out / "index.html").write_text(_index_page(records), encoding="utf-8")
    (out / "style.css").write_text(_CSS, encoding="utf-8")
    (out / "app.js").write_text(_APP_JS, encoding="utf-8")
    return out


# --------------------------------------------------------------------------- templates
_PAGE_TMPL = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="{rel}style.css">
</head><body><main>{body}</main></body></html>
"""

_CSS = """
:root{--accent:#0b7285;--accent2:#0c8599;--bg:#f7fafb;--card:#fff;--line:#e3e8ea;--ink:#1a2326;--mut:#5b6b70}
*{box-sizing:border-box}
body{margin:0;font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--ink);background:var(--bg)}
main{max-width:1180px;margin:0 auto;padding:28px 20px 64px}
h1{font-size:1.7rem;margin:.2em 0 .1em;letter-spacing:-.01em}
a{color:var(--accent2);text-decoration:none}a:hover{text-decoration:underline}
.desc{color:var(--mut);max-width:70ch}.domain{color:var(--accent);font-weight:600;margin:.1em 0 .4em;text-transform:capitalize}
.back{display:inline-block;margin-bottom:10px;font-size:.9rem}
.badges{margin:.3em 0}.badge{display:inline-block;background:var(--accent);color:#fff;border-radius:999px;padding:2px 10px;font-size:.74rem;margin-right:6px;text-transform:capitalize}
.badge.warn{background:#e8590c}
.keywords{margin:.3em 0}.kw{display:inline-block;background:#e7f3f5;color:var(--accent);border-radius:4px;padding:1px 7px;font-size:.74rem;margin:0 5px 5px 0}
.warnings{background:#fff4e6;border:1px solid #ffd8a8;border-radius:8px;padding:8px 12px;margin:12px 0;font-size:.85rem;color:#a8580c}
.kpis{display:flex;flex-wrap:wrap;gap:12px;margin:18px 0}
.kpi{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 16px;min-width:96px}
.kpi-v{font-size:1.35rem;font-weight:700;color:var(--accent)}.kpi-l{font-size:.74rem;color:var(--mut);text-transform:uppercase;letter-spacing:.04em}
.plots{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px;margin:18px 0}
figure{margin:0;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px}
figure img{width:100%;height:auto;display:block}figcaption{font-size:.8rem;color:var(--mut);text-align:center;margin-top:6px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));gap:14px;margin:18px 0}
table.kv{width:100%;background:var(--card);border:1px solid var(--line);border-radius:10px;border-collapse:collapse;overflow:hidden}
table.kv caption{text-align:left;font-weight:700;padding:10px 12px;background:var(--accent);color:#fff}
table.kv th,table.kv td{text-align:left;padding:7px 12px;border-top:1px solid var(--line);vertical-align:top;font-size:.88rem}
table.kv th{color:var(--mut);font-weight:600;width:46%}
.downloads{margin-top:18px;font-size:.9rem}.downloads a{margin-right:12px}
.controls{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:18px 0 10px}
.controls input,.controls select,.controls button{font:inherit;padding:7px 10px;border:1px solid var(--line);border-radius:8px;background:#fff}
.controls input[type=search]{min-width:240px;flex:1}
.controls button{cursor:pointer}.count{color:var(--mut);font-size:.85rem;margin-left:auto}
/* Synced horizontal scrollbar shown ABOVE the table (mirrors the table's own bottom scroll). */
.top-scroll{overflow-x:auto;overflow-y:hidden;height:14px;background:var(--card);border:1px solid var(--line);border-bottom:none;border-radius:10px 10px 0 0}
.top-scroll-inner{height:1px}
.table-wrap{overflow-x:auto;background:var(--card);border:1px solid var(--line);border-radius:0 0 10px 10px}
/* Fixed layout + a percentage colgroup => the table fits its container (no runaway-wide columns);
   overflowing cell text is ellipsized, with the full value available in the title tooltip. */
#catalog{width:100%;border-collapse:collapse;font-size:.86rem;table-layout:fixed}
#catalog th,#catalog td{padding:8px 10px;border-top:1px solid var(--line);text-align:left;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#catalog thead th{position:sticky;top:0;background:#eef4f5;cursor:pointer;user-select:none;border-top:none;z-index:1}
#catalog thead th:hover{background:#e1edee}
#catalog th.num,#catalog td.num{text-align:right;font-variant-numeric:tabular-nums}
#catalog tbody tr:hover{background:#f0f7f8}
#catalog tbody td a{display:block;overflow:hidden;text-overflow:ellipsis}
.nan-y{color:#e8590c;font-weight:700}.pill{font-size:.72rem;color:var(--mut)}
"""

_APP_JS = """
(function(){
  const rows=document.getElementById('rows'),q=document.getElementById('q'),count=document.getElementById('count');
  const sel={task:document.getElementById('f-task'),domain:document.getElementById('f-domain'),signal:document.getElementById('f-signal'),unit:document.getElementById('f-unit')};
  const keys={task:'task',domain:'domain',signal:'signal',unit:'unit'};
  for(const k in sel){const vals=[...new Set(DATA.map(d=>d[keys[k]]).filter(Boolean))].sort();
    for(const v of vals){const o=document.createElement('option');o.value=v;o.textContent=v;sel[k].appendChild(o);}}
  let sortK='name',sortDir=1;
  const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  function fmt(v){return v==null?'':(typeof v==='number'&&!Number.isInteger(v)?(+v.toPrecision(4)):v);}
  function match(d){
    const t=q.value.trim().toLowerCase();
    if(t&&!((d.name+' '+d.domain+' '+d.targets+' '+d.id).toLowerCase().includes(t)))return false;
    for(const k in sel){if(sel[k].value&&String(d[keys[k]])!==sel[k].value)return false;}
    return true;
  }
  function render(){
    let list=DATA.filter(match);
    list.sort((a,b)=>{let x=a[sortK],y=b[sortK];if(x==null)x='';if(y==null)y='';
      if(typeof x==='number'&&typeof y==='number')return (x-y)*sortDir;
      return String(x).localeCompare(String(y),undefined,{numeric:true})*sortDir;});
    rows.innerHTML=list.map(d=>`<tr>
      <td class="col-name"><a href="dataset/${esc(d.id)}.html" title="${esc(d.name)}">${esc(d.name)}</a></td>
      <td title="${esc(d.domain)}">${esc(d.domain)}</td><td>${esc(d.task)}</td><td>${esc(d.version)}</td>
      <td class="num">${fmt(d.n_samples)}</td><td class="num">${fmt(d.n_features)}</td>
      <td title="${esc(d.wl)}">${esc(d.wl)}</td><td>${esc(d.unit)}</td><td title="${esc(d.signal)}">${esc(d.signal)}</td>
      <td class="num">${d.n_classes==null?'':d.n_classes}</td>
      <td class="num">${d.eff_rank==null?'':(+d.eff_rank).toPrecision(3)}</td>
      <td>${d.has_nan?'<span class="nan-y">yes</span>':''}</td>
      <td title="${esc(d.license)}"><span class="pill">${esc(d.license)}</span></td><td>${esc(d.visibility)}</td></tr>`).join('');
    count.textContent=list.length+' / '+DATA.length+' datasets';
    syncWidth();
  }
  // Top scrollbar mirrors the table's own (bottom) horizontal scroll, both ways.
  const wrap=document.getElementById('tableWrap'),topbar=document.getElementById('topScroll'),inner=document.getElementById('topScrollInner'),table=document.getElementById('catalog');
  function syncWidth(){ if(!inner||!table||!wrap||!topbar) return; inner.style.width=table.scrollWidth+'px'; topbar.style.display=(table.scrollWidth>wrap.clientWidth+1)?'block':'none'; }
  let lock=false;
  if(topbar&&wrap){
    topbar.addEventListener('scroll',()=>{if(lock)return;lock=true;wrap.scrollLeft=topbar.scrollLeft;lock=false;});
    wrap.addEventListener('scroll',()=>{if(lock)return;lock=true;topbar.scrollLeft=wrap.scrollLeft;lock=false;});
  }
  window.addEventListener('resize',syncWidth);
  document.querySelectorAll('#catalog thead th').forEach(th=>th.addEventListener('click',()=>{
    const k=th.dataset.k;if(!k)return;sortDir=(sortK===k)?-sortDir:1;sortK=k;render();}));
  q.addEventListener('input',render);for(const k in sel)sel[k].addEventListener('change',render);
  document.getElementById('reset').addEventListener('click',()=>{q.value='';for(const k in sel)sel[k].value='';sortK='name';sortDir=1;render();});
  render();
})();
"""
