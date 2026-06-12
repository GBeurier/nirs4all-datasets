"""Reusable HTML fragments: nav, footer, hero (spectral-wave), KPI strip, chips, tables, dataset card.

The hero markup + the spectral-wave animation script are lifted from ``nirs4all-webpage/index.html``
(adapted copy). Everything else is authored for this site. All fragments are pure string builders over
the escaping helpers + view models; none touch nirs4all/pandas/the filesystem.
"""
from __future__ import annotations

from typing import Any

from .escape import esc, num
from .icons import icon, signal_icon_key
from .model import DatasetView

_TIERS = ("public", "private", "anonymized")
_TIER_LABEL = {"public": "Public", "private": "Private", "anonymized": "Anonymized"}


# =============================================================================
# Nav + footer
# =============================================================================
def nav(rel: str, active: str = "") -> str:
    """The sticky glassmorphic top nav. ``active`` highlights ``index``/``catalog``."""
    def cls(name: str) -> str:
        return ' class="active"' if name == active else ""
    return f"""
<nav id="nav"><div class="container nav-inner">
  <a class="nav-logo" href="{rel}index.html"><span class="mark"></span>&nbsp;<b>nirs4all</b>-datasets&nbsp;<span>v2.0</span></a>
  <div class="nav-links">
    <a href="{rel}index.html"{cls('index')}>Overview</a>
    <a href="{rel}catalog.html"{cls('catalog')}>Catalog</a>
    <a href="https://nirs4all.org" target="_blank" rel="noopener">nirs4all.org</a>
    <a href="https://github.com/GBeurier/nirs4all-datasets" target="_blank" rel="noopener">GitHub</a>
  </div>
</div></nav>
"""


def footer(rel: str) -> str:
    """Dark footer with brand, links, and the provenance/license note."""
    return f"""
<footer><div class="container">
  <div>
    <div class="f-brand">nirs4all-datasets</div>
    <p class="f-meta">A citable, reproducible bank of <strong>raw</strong> NIRS reference datasets.
    Bytes live at their licensed origin / on Dataverse (DOI-pinned, checksum-verified); this catalog
    serves only descriptors, metrics, and identity cards.</p>
  </div>
  <div class="f-links">
    <a href="{rel}index.html">Overview</a>
    <a href="{rel}catalog.html">Catalog</a>
    <a href="https://github.com/GBeurier/nirs4all-datasets" target="_blank" rel="noopener">Source &amp; issues</a>
    <a href="https://nirs4all.org" target="_blank" rel="noopener">nirs4all ecosystem</a>
  </div>
  <p class="f-note">Built with the nirs4all-datasets static-site generator — pure rendering over committed
  artifacts. Each dataset retains its own license; cite the dataset DOI and its origin publications.</p>
</div></footer>
"""


# =============================================================================
# Hero (spectral-wave) — lifted markup + animation
# =============================================================================
HERO_MARKUP = """
<section id="hero">
  <div class="hero-dots"></div>
  <div class="hero-grain"></div>
  <svg class="hero-spectra" viewBox="0 0 1440 400" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="sg1" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0d9488" stop-opacity="0.28"/><stop offset="100%" stop-color="#0d9488" stop-opacity="0"/></linearGradient>
      <linearGradient id="sg2" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#06b6d4" stop-opacity="0.22"/><stop offset="100%" stop-color="#06b6d4" stop-opacity="0"/></linearGradient>
      <linearGradient id="sg3" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#10b981" stop-opacity="0.15"/><stop offset="100%" stop-color="#10b981" stop-opacity="0"/></linearGradient>
    </defs>
    <path class="spectrum-area" id="area0" fill="url(#sg1)" opacity="0.7"/>
    <path class="spectrum-area" id="area1" fill="url(#sg2)" opacity="0.55"/>
    <path class="spectrum-area" id="area2" fill="url(#sg3)" opacity="0.35"/>
    <path class="spectrum-line" id="line0" stroke="#0f766e" stroke-width="1.3" opacity="0.75"/>
    <path class="spectrum-line" id="line1" stroke="#0891b2" stroke-width="1.0" opacity="0.55"/>
    <path class="spectrum-line" id="line2" stroke="#059669" stroke-width="0.8" opacity="0.35"/>
    <g id="wave-dots"></g>
  </svg>
  <div class="container hero-content">
    <div class="hero-badge"><span class="dot"></span> DOI-pinned · checksum-verified · pooch-style on-demand</div>
    <h1 class="hero-tagline">A reproducible bank of <em>raw NIRS</em> reference datasets</h1>
    <p class="hero-sub">Curated near-infrared spectroscopy datasets — provenance-rich, license-aware, and
    citable. Each is described by a full identity card; the bytes stay at their licensed origin and are
    fetched on demand, verified, and cached.</p>
    <div class="hero-ctas">
      <a class="btn btn-primary" href="catalog.html">Browse the catalog &rarr;</a>
      <button class="btn-pip" id="copy-pip" title="Click to copy"><code>pip install nirs4all-datasets</code></button>
    </div>
  </div>
</section>
"""

# Spectral-wave animation, lifted from nirs4all.org (self-contained; degrades gracefully if absent).
HERO_SCRIPT = """
<script>
(function(){
  var pip=document.getElementById('copy-pip');
  if(pip){pip.addEventListener('click',function(){var t=pip.querySelector('code').textContent;
    if(navigator.clipboard)navigator.clipboard.writeText(t);
    var o=pip.querySelector('code').textContent;pip.querySelector('code').textContent='copied!';
    setTimeout(function(){pip.querySelector('code').textContent=o;},1100);});}
  var W=1440,H=400,STEP=4;
  var lines=[document.getElementById('line0'),document.getElementById('line1'),document.getElementById('line2')];
  var areas=[document.getElementById('area0'),document.getElementById('area1'),document.getElementById('area2')];
  var dotsGroup=document.getElementById('wave-dots');
  if(!lines[0]||!dotsGroup)return;
  var waves=[
    {baseY:260,amp:50,freq:0.0044,phase:0,speed:0.00035,color:'#0f766e',dotColor:'rgba(15,118,110,0.95)'},
    {baseY:290,amp:38,freq:0.0038,phase:2.1,speed:0.00028,color:'#0891b2',dotColor:'rgba(8,145,178,0.85)'},
    {baseY:230,amp:30,freq:0.0052,phase:4.2,speed:0.00022,color:'#059669',dotColor:'rgba(5,150,105,0.75)'}
  ];
  var MAX_DOTS=18,dots=[],DOT_LIFETIME=2400,DOT_SPAWN_INTERVAL=320,lastSpawn=0;
  var svgEl=lines[0].ownerSVGElement,invSx=1,invSy=1;
  function updateScale(){var r=svgEl.getBoundingClientRect();if(r.width>0&&r.height>0){invSx=W/r.width;invSy=H/r.height;}}
  updateScale();window.addEventListener('resize',updateScale);
  function getY(wave,x,now){return wave.baseY+Math.sin(x*wave.freq+wave.phase+now*wave.speed)*wave.amp+Math.sin(x*wave.freq*1.7+wave.phase*0.6+now*wave.speed*0.7)*wave.amp*0.2;}
  function buildSinePath(wave,now){var d='';for(var x=0;x<=W;x+=STEP){var y=getY(wave,x,now);d+=(x===0?'M':'L')+x.toFixed(1)+','+y.toFixed(1);}return d;}
  function spawnDot(now){if(dots.length>=MAX_DOTS)return;var wi=Math.floor(Math.random()*waves.length),wave=waves[wi];
    var x=60+Math.random()*(W-120),y=getY(wave,x,now);
    var el=document.createElementNS('http://www.w3.org/2000/svg','ellipse');
    el.setAttribute('cx',x.toFixed(1));el.setAttribute('cy',y.toFixed(1));
    el.setAttribute('rx',(3*invSx).toFixed(2));el.setAttribute('ry',(3*invSy).toFixed(2));
    el.setAttribute('fill',wave.dotColor);el.setAttribute('opacity','0');el.classList.add('wave-dot');el.style.color=wave.color;
    dotsGroup.appendChild(el);dots.push({el:el,waveIdx:wi,x:x,born:now,lifetime:DOT_LIFETIME+Math.random()*800,connectors:[]});}
  var MAX_CONN_DX=220;
  function updateConnectors(now){
    dots.forEach(function(d){d.connectors.forEach(function(c){c.remove();});d.connectors=[];});
    var pos=dots.map(function(d){return {d:d,op:parseFloat(d.el.getAttribute('opacity')||'0'),y:getY(waves[d.waveIdx],d.x,now)};});
    var seen={};
    for(var i=0;i<pos.length;i++){var a=pos[i];if(a.op<0.18)continue;var best=null;
      for(var j=0;j<pos.length;j++){if(i===j)continue;var b=pos[j];if(b.d.waveIdx===a.d.waveIdx)continue;if(b.op<0.18)continue;
        var dx=Math.abs(a.d.x-b.d.x);if(dx>MAX_CONN_DX)continue;if(!best||dx<best.dx)best={b:b,j:j,dx:dx};}
      if(!best)continue;var key=i<best.j?i+':'+best.j:best.j+':'+i;if(seen[key])continue;seen[key]=1;
      var b2=best.b,prox=1-best.dx/MAX_CONN_DX,op=Math.min(a.op,b2.op)*0.55*(0.35+0.65*prox);if(op<0.03)continue;
      var line=document.createElementNS('http://www.w3.org/2000/svg','path');
      line.setAttribute('d','M'+a.d.x.toFixed(1)+','+a.y.toFixed(1)+' L'+b2.d.x.toFixed(1)+','+b2.y.toFixed(1));
      line.setAttribute('stroke',waves[a.d.waveIdx].color);line.setAttribute('stroke-width','0.75');
      line.setAttribute('opacity',op.toFixed(3));line.classList.add('wave-connector');
      dotsGroup.insertBefore(line,dotsGroup.firstChild);a.d.connectors.push(line);}}
  function updateDots(now){for(var i=dots.length-1;i>=0;i--){var dot=dots[i],age=now-dot.born,p=age/dot.lifetime;
    if(p>=1){dot.el.remove();dot.connectors.forEach(function(c){c.remove();});dots.splice(i,1);continue;}
    var y=getY(waves[dot.waveIdx],dot.x,now);dot.el.setAttribute('cy',y.toFixed(1));
    var op;if(p<0.15)op=p/0.15;else if(p<0.7)op=1;else op=1-(p-0.7)/0.3;
    dot.el.setAttribute('opacity',(op*0.9).toFixed(3));var r=2.5+op*1.5;
    dot.el.setAttribute('rx',(r*invSx).toFixed(2));dot.el.setAttribute('ry',(r*invSy).toFixed(2));}}
  var frameId=0;
  function animate(now){waves.forEach(function(wave,i){var d=buildSinePath(wave,now);lines[i].setAttribute('d',d);
    areas[i].setAttribute('d',d+' L'+W+','+H+' L0,'+H+' Z');});
    if(now-lastSpawn>DOT_SPAWN_INTERVAL){spawnDot(now);lastSpawn=now;}
    updateDots(now);updateConnectors(now);frameId=requestAnimationFrame(animate);}
  frameId=requestAnimationFrame(animate);
  window.addEventListener('pagehide',function(){cancelAnimationFrame(frameId);},{once:true});
})();
</script>
"""


# =============================================================================
# Small chips / KPIs / section heads
# =============================================================================
def kpi(value: str, label: str) -> str:
    return f'<div class="kpi"><div class="kpi-v">{value}</div><div class="kpi-l">{esc(label)}</div></div>'


def kpi_strip(kpis: list[tuple[str, str]]) -> str:
    return f'<div class="kpis">{"".join(kpi(value, label) for value, label in kpis)}</div>'


def tier_badge(tier: str) -> str:
    t = tier if tier in _TIERS else "public"
    return f'<span class="badge tier-{t}"><span class="b-dot"></span>{esc(_TIER_LABEL.get(t, t))}</span>'


def badge(text: str, kind: str = "neutral") -> str:
    return f'<span class="badge {esc(kind)}">{esc(text)}</span>'


def section_head(eyebrow: str, title_html: str, sub: str = "", *, centered: bool = True) -> str:
    wrap = ' class="eyebrow-wrap"' if centered else ""
    sub_html = f'<p class="section-sub">{esc(sub)}</p>' if sub else ""
    return f'<div{wrap}><span class="eyebrow">{esc(eyebrow)}</span></div><h2 class="section-title">{title_html}</h2>{sub_html}'


def viz_card(title: str, sub: str, svg: str, *, wide: bool = False) -> str:
    return (
        f'<div class="viz-card{" wide" if wide else ""}">'
        f'<div class="viz-h">{esc(title)}</div><div class="viz-sub">{esc(sub)}</div>{svg}</div>'
    )


# =============================================================================
# Dataset card (catalog page)
# =============================================================================
def dataset_card(view: DatasetView) -> str:
    """A catalog card with the tier accent stripe, KPIs, and badges. Carries ``data-*`` for JS filters."""
    e = view.entry
    tier = view.tier
    tier_var = {"public": "var(--tier-public)", "private": "var(--tier-private)", "anonymized": "var(--tier-anonymized)"}.get(tier, "var(--teal)")
    n_samples = e.get("n_samples")
    n_features = e.get("n_features_total")
    n_targets = e.get("n_targets") or 0
    n_sources = e.get("n_sources") or 0
    family = e.get("spectro_family") or "—"
    domain = e.get("domain") or "—"

    # task-type + detected signal-type glyphs (legend on the catalog page)
    glyphs: list[str] = []
    for kind in (e.get("task") or "").split("+"):
        if kind:
            glyphs.append(f'<span class="ds-ic task" title="{esc(kind)}">{icon(kind)}<i>{esc(kind)}</i></span>')
    for st in e.get("signal_types") or []:
        glyphs.append(f'<span class="ds-ic signal" title="signal type: {esc(st)}">{icon(signal_icon_key(st))}<i>{esc(st)}</i></span>')
    icons_html = f'<div class="ds-icons">{"".join(glyphs)}</div>' if glyphs else ""

    badges = [tier_badge(tier)]
    if n_sources > 1:
        badges.append(badge(f"{n_sources} sources", "info"))
    if n_targets == 0:
        badges.append(badge("metadata-only", "neutral"))
    if e.get("has_split"):
        badges.append(badge("native split", "neutral"))
    if not view.has_card:
        badges.append(badge("card pending", "warn"))
    elif view.is_stale:
        badges.append(badge("stale card", "warn"))
    if (e.get("health") or {}).get("degraded"):
        badges.append(badge("origin degraded", "warn"))

    data_attrs = (
        f'data-name="{esc(view.name.lower())} {esc(view.id)} {esc(domain.lower())} {esc(" ".join(str(t).lower() for t in e.get("targets") or []))}" '
        f'data-tier="{esc(tier)}" data-family="{esc(family)}" data-domain="{esc(domain)}" '
        f'data-target="{"yes" if n_targets > 0 else "no"}" data-multi="{"yes" if n_sources > 1 else "no"}" '
        f'data-samples="{n_samples if isinstance(n_samples, int) else 0}" '
        f'data-features="{n_features if isinstance(n_features, int) else 0}"'
    )
    return f"""
<article class="ds-card" style="--tier:{tier_var}" {data_attrs}>
  <h3><a href="dataset/{esc(view.id)}.html">{esc(view.name)}</a></h3>
  <div class="ds-domain">{esc(domain)} &middot; {esc(family)}</div>
  {icons_html}
  <div class="ds-meta">
    <div>Samples <b>{num(n_samples) if n_samples is not None else "—"}</b></div>
    <div>Wavelengths <b>{num(n_features) if n_features is not None else "—"}</b></div>
    <div>Targets <b>{num(n_targets)}</b></div>
    <div>Sources <b>{num(n_sources)}</b></div>
  </div>
  <div class="ds-badges">{"".join(badges)}</div>
</article>
"""


# =============================================================================
# Code block (how-to-load snippet)
# =============================================================================
def code_block(lines: list[tuple[str, str]]) -> str:
    """A terminal-styled code block. Each line is ``(css_class, text)`` (``""`` => plain)."""
    rendered = []
    for cls, text in lines:
        span = f'<span class="{cls}">{esc(text)}</span>' if cls else esc(text)
        rendered.append(span)
    return f'<div class="codeblock"><div class="topbar"><i></i><i></i><i></i></div><pre>{chr(10).join(rendered)}</pre></div>'


def load_snippet(dataset_id: str, tier: str) -> str:
    """A ``get("<id>")`` python snippet, with a token hint for non-public tiers."""
    lines: list[tuple[str, str]] = [
        ("c", "# pip install nirs4all-datasets"),
        ("", "from nirs4all_datasets import get"),
        ("", ""),
    ]
    if tier == "public":
        lines.append(("", f'ds = get("{dataset_id}")            # DOI-pinned, checksum-verified, cached'))
    else:
        lines.append(("c", f"# {tier} dataset — export requires a Dataverse token"))
        lines.append(("", f'ds = get("{dataset_id}", token="…")'))
    lines += [
        ("", "X, y = ds.x(), ds.y()"),
        ("", "print(X.shape, y.shape)"),
    ]
    return code_block(lines)


# =============================================================================
# Generic table helpers (for the dataset detail page)
# =============================================================================
def data_table(caption: str, headers: list[str], rows: list[list[Any]], *, num_cols: set[int] | None = None) -> str:
    """A multi-column data table (sources / variables / splits)."""
    if not rows:
        return ""
    num_cols = num_cols or set()
    head = "".join(f'<th class="num">{esc(h)}</th>' if i in num_cols else f"<th>{esc(h)}</th>" for i, h in enumerate(headers))
    body = []
    for row in rows:
        cells = "".join(
            (f'<td class="num">{c}</td>' if i in num_cols else f"<td>{c}</td>")
            if (isinstance(c, str) and c.startswith("<"))
            else (f'<td class="num">{esc(c)}</td>' if i in num_cols else f"<td>{esc(c)}</td>")
            for i, c in enumerate(row)
        )
        body.append(f"<tr>{cells}</tr>")
    return (
        f'<div class="table-scroll"><table class="data"><caption>{esc(caption)}</caption>'
        f"<thead><tr>{head}</tr></thead><tbody>{''.join(body)}</tbody></table></div>"
    )
