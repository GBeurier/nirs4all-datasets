"""The site theme: lifted nirs4all.org palette/fonts/hero CSS + the base HTML shell.

The ``:root`` palette, the Google Fonts link (IBM Plex Sans + Inter + JetBrains Mono), the
``.section-paper`` / ``.section-aurora`` backdrops, the glassmorphic nav, ``.btn-primary``, and the
HERO (``.hero-dots`` / ``.hero-grain`` / ``.hero-spectra`` markup + the spectral-wave animation CSS)
are lifted verbatim from ``nirs4all-webpage/index.html`` so the catalog "claque" the same way. The
catalog/dataviz/identity-card styles below are authored here for this site. Self-contained: a single
inline ``<style>`` + the Google Fonts link; everything works from ``file://``.
"""
from __future__ import annotations

FONTS_LINK = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;0,700;1,500;1,600'
    "&family=Inter:wght@400;500;600;700;800"
    '&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'
)

# Lifted verbatim from nirs4all.org (palette, fonts vars, sections, nav, buttons, hero) + authored
# catalog/dataviz/card styles. Kept as one string so the page is fully self-contained.
CSS = """
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --teal:    #0d9488;
  --teal-d:  #0f766e;
  --teal-l:  #2dd4bf;
  --cyan:    #06b6d4;
  --cyan-d:  #0891b2;
  --indigo:  #4f46e5;
  --indigo-d:#4338ca;
  --green:   #10b981;
  --amber:   #d97706;

  --paper:    #faf7f0;
  --paper-2:  #f3efe5;
  --bg:       #ffffff;
  --bg-alt:   #f5f7fa;
  --bg-grid:  #f7f5ef;
  --bg-code:  #0b1220;
  --surface:  #ffffff;
  --border:   #e2e8f0;
  --border-warm: #e8e2d3;
  --text:     #0f172a;
  --text-2:   #475569;
  --text-3:   #64748b;

  --shadow:   0 4px 16px -4px rgba(17,24,39,0.08), 0 2px 4px -2px rgba(17,24,39,0.04);
  --shadow-lg: 0 20px 40px -12px rgba(17,24,39,0.10);
  --shadow-warm: 0 18px 38px -14px rgba(120,85,30,0.16), 0 3px 8px -4px rgba(120,85,30,0.10);
  --radius:   16px;
  --radius-sm: 10px;

  --font:    'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
  --display: 'IBM Plex Sans', 'Inter', -apple-system, system-ui, sans-serif;
  --mono:    'JetBrains Mono', 'Fira Code', 'Cascadia Code', Consolas, monospace;

  /* tier accents (authored) */
  --tier-public:     #10b981;
  --tier-private:    #d97706;
  --tier-anonymized: #4f46e5;
}

body {
  font-family: var(--font); background: var(--bg); color: var(--text);
  line-height: 1.7; overflow-x: hidden; -webkit-font-smoothing: antialiased;
}
a { color: var(--teal); text-decoration: none; transition: color .2s; }
a:hover { color: var(--teal-d); }
img { max-width: 100%; display: block; }
code, pre { font-family: var(--mono); }

.container { max-width: 1200px; margin: 0 auto; padding: 0 24px; }
.section { padding: 96px 0; position: relative; }
.section-tight { padding: 64px 0; }
.section-alt { background: var(--bg-alt); }

.section-paper {
  background: var(--paper);
  background-image:
    linear-gradient(rgba(20,50,48,0.035) 1px, transparent 1px),
    linear-gradient(90deg, rgba(20,50,48,0.035) 1px, transparent 1px);
  background-size: 52px 52px;
  border-top: 1px solid var(--border-warm);
  border-bottom: 1px solid var(--border-warm);
}
.section-paper::before {
  content: ''; position: absolute; inset: 0; pointer-events: none;
  background: radial-gradient(ellipse 90% 60% at 50% 0%, rgba(13,148,136,0.08), transparent 70%);
}

.section-aurora {
  background: #fcfdff; position: relative; overflow: hidden;
  border-top: 1px solid var(--border);
}
.section-aurora::before {
  content: ''; position: absolute; inset: -20%; pointer-events: none; z-index: 0;
  background:
    radial-gradient(ellipse 40% 35% at 15% 20%, rgba(13,148,136,0.22), transparent 70%),
    radial-gradient(ellipse 35% 30% at 85% 30%, rgba(6,182,212,0.18), transparent 70%),
    radial-gradient(ellipse 45% 35% at 50% 95%, rgba(16,185,129,0.14), transparent 72%),
    radial-gradient(ellipse 25% 25% at 90% 85%, rgba(217,119,6,0.12), transparent 75%);
  filter: blur(20px);
}
.section-aurora .container { position: relative; z-index: 1; }

.eyebrow {
  display: inline-flex; align-items: center; gap: 10px; font-family: var(--font);
  font-size: .72rem; font-weight: 600; letter-spacing: .18em; text-transform: uppercase;
  color: var(--teal-d); margin-bottom: 18px;
}
.eyebrow::before { content: ''; width: 28px; height: 1px; background: currentColor; }
.eyebrow-wrap { text-align: center; }
.eyebrow-wrap .eyebrow { justify-content: center; }
.section-title {
  font-family: var(--display); font-size: clamp(1.8rem, 4vw, 2.6rem); font-weight: 600;
  text-align: center; margin-bottom: 16px; letter-spacing: -.018em; line-height: 1.12;
}
.section-title em {
  font-style: italic; font-weight: 500;
  background: linear-gradient(120deg, var(--teal-d) 0%, var(--cyan) 60%, var(--green) 100%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.section-sub {
  color: var(--text-2); text-align: center; max-width: 680px; margin: 0 auto 56px;
  font-size: 1.05rem; line-height: 1.8;
}

/* ── Navigation (glassmorphic) ──────────────────────────────────── */
#nav {
  position: sticky; top: 0; left: 0; right: 0; z-index: 100;
  backdrop-filter: blur(20px) saturate(180%); -webkit-backdrop-filter: blur(20px) saturate(180%);
  background: rgba(255,255,255,0.82);
  border-bottom: 1px solid rgba(15,23,42,0.06);
}
.nav-inner { display: flex; align-items: center; gap: 8px; height: 62px; }
.nav-logo {
  display: flex; align-items: center; gap: 10px;
  font-family: var(--display); font-weight: 600; font-size: 1.12rem; color: var(--text); margin-right: auto;
}
.nav-logo .mark {
  width: 26px; height: 26px; border-radius: 7px;
  background: linear-gradient(135deg, var(--teal) 0%, var(--cyan-d) 100%);
  box-shadow: 0 4px 12px -3px rgba(13,148,136,.5);
}
.nav-logo b { font-weight: 700; }
.nav-logo span { color: var(--text-3); font-weight: 500; font-family: var(--mono); font-size: .72rem; }
.nav-links { display: flex; gap: 2px; align-items: center; }
.nav-links a { padding: 7px 14px; border-radius: 8px; color: var(--text-2); font-size: .88rem; font-weight: 500; transition: all .2s; }
.nav-links a:hover, .nav-links a.active { color: var(--text); background: rgba(15,23,42,0.05); }

/* ── Buttons ───────────────────────────────────────────────────── */
.btn {
  display: inline-flex; align-items: center; gap: 8px; padding: 11px 22px; border-radius: var(--radius-sm);
  font-weight: 600; font-size: .9rem; cursor: pointer; transition: all .2s; border: none; font-family: var(--font);
}
.btn-primary { background: var(--teal); color: #fff; }
.btn-primary:hover { background: var(--teal-d); color: #fff; transform: translateY(-1px); box-shadow: 0 4px 16px rgba(13,148,136,.35); }
.btn-outline { background: rgba(255,255,255,.7); color: var(--text); border: 1px solid var(--border); }
.btn-outline:hover { border-color: var(--teal); background: rgba(13,148,136,.05); }

/* ── Hero (LIGHT) ───────────────────────────────────────────────── */
#hero {
  position: relative;
  background:
    radial-gradient(ellipse 60% 55% at 85% 10%, rgba(13,148,136,0.14), transparent 70%),
    radial-gradient(ellipse 55% 50% at 12% 90%, rgba(6,182,212,0.16), transparent 72%),
    radial-gradient(ellipse 45% 40% at 50% 100%, rgba(16,185,129,0.10), transparent 75%),
    linear-gradient(180deg, #fbf9f3 0%, #f6f3ea 40%, #eef6f5 100%);
  min-height: 72vh; display: flex; align-items: center; overflow: hidden; isolation: isolate;
}
.hero-dots {
  position: absolute; inset: 0; z-index: 0; opacity: .6;
  background-image: radial-gradient(rgba(20,50,48,0.09) 1px, transparent 1px);
  background-size: 52px 52px;
  mask-image: radial-gradient(ellipse 80% 70% at 50% 40%, black 30%, transparent 90%);
  -webkit-mask-image: radial-gradient(ellipse 80% 70% at 50% 40%, black 30%, transparent 90%);
}
.hero-grain {
  position: absolute; inset: 0; z-index: 0; pointer-events: none; opacity: .25; mix-blend-mode: multiply;
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='220' height='220'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.92' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0.3  0 0 0 0 0.25  0 0 0 0 0.15  0 0 0 .35 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>");
  background-size: 220px 220px;
}
.hero-spectra { position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); width: calc(100% - 48px); max-width: 1200px; height: 40%; z-index: 1; pointer-events: none; }
.spectrum-line { fill: none; stroke-linecap: round; stroke-linejoin: round; }
.wave-dot { fill: currentColor; filter: drop-shadow(0 0 6px currentColor); }
.wave-connector { fill: none; stroke-dasharray: 1.5 4; stroke-linecap: round; mix-blend-mode: multiply; }

.hero-content { position: relative; z-index: 20; text-align: center; padding: 80px 0 64px; isolation: isolate; }
.hero-content > * { position: relative; z-index: 1; }
.hero-badge {
  display: inline-flex; align-items: center; gap: 8px;
  background: rgba(255,255,255,0.85); border: 1px solid rgba(13,148,136,0.18);
  border-radius: 100px; padding: 6px 18px; font-size: .78rem; color: var(--text-2); margin-bottom: 28px;
  backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
  box-shadow: 0 8px 24px -10px rgba(13,148,136,0.25); font-weight: 500; letter-spacing: .02em;
}
.hero-badge .dot { width: 8px; height: 8px; background: var(--green); border-radius: 50%; animation: pulse 2s infinite; box-shadow: 0 0 0 3px rgba(16,185,129,0.18); }
@keyframes pulse { 0%,100% { opacity: 1; } 50% { opacity: .4; } }
.hero-tagline {
  font-family: var(--display); font-size: clamp(1.9rem, 5.2vw, 3.2rem); font-weight: 600;
  color: var(--text); margin-bottom: 14px; letter-spacing: -.025em; line-height: 1.05;
}
.hero-tagline em {
  font-style: italic; font-weight: 500;
  background: linear-gradient(120deg, var(--teal-d) 0%, var(--cyan) 55%, var(--green) 100%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.hero-sub { font-size: clamp(.98rem, 2.2vw, 1.14rem); color: var(--text-2); max-width: 640px; margin: 0 auto 28px; line-height: 1.7; }
.hero-ctas { display: flex; flex-wrap: wrap; gap: 12px; justify-content: center; margin-bottom: 12px; position: relative; z-index: 12; }
.btn-pip {
  display: inline-flex; align-items: center; gap: 10px; background: rgba(11,18,32,0.92);
  border: 1px solid rgba(15,23,42,0.9); border-radius: var(--radius-sm); padding: 12px 20px; font-size: .88rem;
  cursor: pointer; transition: all .2s; color: rgba(255,255,255,0.95); font-family: var(--font);
  box-shadow: 0 10px 26px -10px rgba(11,18,32,0.5);
}
.btn-pip:hover { border-color: var(--teal); transform: translateY(-1px); box-shadow: 0 14px 32px -10px rgba(13,148,136,.5); }
.btn-pip code { color: #5eead4; font-size: .88rem; font-weight: 500; }

/* ── KPI strip ─────────────────────────────────────────────────── */
.kpis { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 14px; margin: 8px 0; }
.kpi {
  background: rgba(255,255,255,0.78); border: 1px solid var(--border-warm); border-radius: 14px;
  padding: 18px 20px; text-align: center; backdrop-filter: blur(8px);
  box-shadow: var(--shadow); transition: transform .2s, box-shadow .2s;
}
.kpi:hover { transform: translateY(-2px); box-shadow: var(--shadow-lg); }
.kpi-v {
  font-family: var(--display); font-size: 1.85rem; font-weight: 700; line-height: 1;
  background: linear-gradient(120deg, var(--teal-d), var(--cyan)); -webkit-background-clip: text; background-clip: text; color: transparent;
}
.kpi-l { font-size: .72rem; color: var(--text-3); text-transform: uppercase; letter-spacing: .08em; margin-top: 8px; font-weight: 600; }

/* ── Dataviz grid ──────────────────────────────────────────────── */
.viz-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 20px; }
@media (max-width: 760px) { .viz-grid { grid-template-columns: 1fr; } }
.viz-card {
  background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius);
  padding: 22px 22px 18px; box-shadow: var(--shadow); transition: box-shadow .2s, transform .2s;
}
.viz-card:hover { box-shadow: var(--shadow-lg); transform: translateY(-2px); }
.viz-card.wide { grid-column: 1 / -1; }
.viz-h { font-family: var(--display); font-size: 1.02rem; font-weight: 600; margin-bottom: 4px; }
.viz-sub { font-size: .8rem; color: var(--text-3); margin-bottom: 16px; }
.viz-card svg { width: 100%; height: auto; display: block; }
.viz-canvas { width: 100%; }
/* charts size their own viewBox to the display width; numbers are tabular monospace */
svg text { font-family: var(--font); }
svg text.numt { font-family: var(--mono); font-variant-numeric: tabular-nums; }
svg .barm, svg .seg, svg .pt { transition: opacity .15s, filter .15s; }
svg .barm:hover, svg .seg:hover, svg .pt:hover { opacity: .86; filter: drop-shadow(0 2px 4px rgba(15,23,42,.16)); }
.legend { display: flex; flex-wrap: wrap; justify-content: center; gap: 8px 16px; margin-top: 14px; font-size: .78rem; color: var(--text-2); }
.legend i { display: inline-block; width: 11px; height: 11px; border-radius: 3px; margin-right: 6px; vertical-align: -1px; }

/* ── How-to-load code block ─────────────────────────────────────── */
.codeblock {
  background: var(--bg-code); border-radius: var(--radius); padding: 22px 24px; overflow-x: auto;
  box-shadow: var(--shadow-lg); position: relative;
}
.codeblock pre { margin: 0; font-size: .86rem; line-height: 1.7; color: #e2e8f0; }
.codeblock .c { color: #64748b; }
.codeblock .k { color: #5eead4; }
.codeblock .s { color: #fbbf24; }
.codeblock .topbar { display: flex; gap: 7px; margin-bottom: 14px; }
.codeblock .topbar i { width: 11px; height: 11px; border-radius: 50%; background: #334155; }

/* ── Catalog page (table + cards + filters) ─────────────────────── */
.controls {
  display: flex; flex-wrap: wrap; gap: 10px; align-items: center; margin: 0 0 22px;
  background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius);
  padding: 16px 18px; box-shadow: var(--shadow);
}
.controls input, .controls select {
  font: inherit; font-size: .88rem; padding: 9px 12px; border: 1px solid var(--border); border-radius: 9px;
  background: #fff; color: var(--text);
}
.controls input[type=search] { min-width: 260px; flex: 1; }
.controls input:focus, .controls select:focus { outline: none; border-color: var(--teal); box-shadow: 0 0 0 3px rgba(13,148,136,.14); }
.controls .btn-reset { font: inherit; font-size: .85rem; padding: 9px 16px; border: 1px solid var(--border); border-radius: 9px; background: #fff; cursor: pointer; color: var(--text-2); }
.controls .btn-reset:hover { border-color: var(--teal); color: var(--teal-d); }
.controls .count { color: var(--text-3); font-size: .85rem; margin-left: auto; font-variant-numeric: tabular-nums; }

.cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 18px; }
.ds-card {
  display: flex; flex-direction: column; background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 20px; box-shadow: var(--shadow);
  transition: transform .2s, box-shadow .2s, border-color .2s; position: relative; overflow: hidden;
}
.ds-card::before {
  content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 4px; background: var(--tier, var(--teal));
}
.ds-card:hover { transform: translateY(-3px); box-shadow: var(--shadow-lg); border-color: var(--teal-l); }
.ds-card h3 { font-family: var(--display); font-size: 1.06rem; font-weight: 600; line-height: 1.3; margin-bottom: 4px; }
.ds-card h3 a { color: var(--text); }
.ds-card h3 a:hover { color: var(--teal-d); }
.ds-card .ds-domain { font-size: .76rem; color: var(--teal-d); text-transform: uppercase; letter-spacing: .06em; font-weight: 600; margin-bottom: 12px; }
.ds-meta { display: grid; grid-template-columns: 1fr 1fr; gap: 8px 14px; margin: 10px 0 14px; font-size: .82rem; }
.ds-meta div { color: var(--text-3); }
.ds-meta b { color: var(--text); font-weight: 600; font-variant-numeric: tabular-nums; }
.ds-badges { display: flex; flex-wrap: wrap; gap: 6px; margin-top: auto; }

/* ── Task / signal-type glyphs on cards + the catalog legend ── */
.ds-icons { display: flex; flex-wrap: wrap; gap: 6px 8px; margin: 0 0 12px; }
.ds-ic { display: inline-flex; align-items: center; gap: 5px; font-size: .72rem; padding: 3px 9px 3px 7px;
  border-radius: 999px; border: 1px solid var(--border); background: var(--bg-alt); white-space: nowrap; }
.ds-ic svg { width: 15px; height: 15px; }
.ds-ic i { font-style: normal; }
.ds-ic.task { color: var(--teal-d); border-color: rgba(15,118,110,.28); background: rgba(15,118,110,.07); }
.ds-ic.signal { color: #9c5b6a; border-color: rgba(156,91,106,.28); background: rgba(156,91,106,.07); }
.icon-legend { display: flex; flex-wrap: wrap; align-items: center; gap: 8px 16px; margin-bottom: 22px;
  padding: 12px 18px; border: 1px solid var(--border); border-radius: 12px; background: var(--bg-alt); font-size: .8rem; color: var(--text-2); }
.icon-legend .leg-title { font-family: var(--display); font-weight: 600; color: var(--text-3); text-transform: uppercase; letter-spacing: .06em; font-size: .7rem; }
.leg-item { display: inline-flex; align-items: center; gap: 6px; }
.leg-ic { display: inline-flex; }
.leg-ic svg { width: 16px; height: 16px; }
.leg-ic.task { color: var(--teal-d); }
.leg-ic.signal { color: #9c5b6a; }

/* ── Tier / status badges ──────────────────────────────────────── */
.badge {
  display: inline-flex; align-items: center; gap: 5px; border-radius: 999px; padding: 3px 11px;
  font-size: .72rem; font-weight: 600; letter-spacing: .01em; border: 1px solid transparent;
}
.badge .b-dot { width: 7px; height: 7px; border-radius: 50%; background: currentColor; }
.badge.tier-public { color: #047857; background: rgba(16,185,129,.12); border-color: rgba(16,185,129,.3); }
.badge.tier-private { color: #b45309; background: rgba(217,119,6,.12); border-color: rgba(217,119,6,.3); }
.badge.tier-anonymized { color: #4338ca; background: rgba(79,70,229,.12); border-color: rgba(79,70,229,.3); }
.badge.neutral { color: var(--text-2); background: var(--bg-alt); border-color: var(--border); }
.badge.warn { color: #b45309; background: rgba(217,119,6,.1); border-color: rgba(217,119,6,.3); }
.badge.info { color: var(--cyan-d); background: rgba(6,182,212,.1); border-color: rgba(6,182,212,.28); }

.hidden { display: none !important; }
.empty { padding: 48px; text-align: center; color: var(--text-3); }

/* ── Dataset detail page ───────────────────────────────────────── */
.ds-hero { padding: 56px 0 28px; }
.back { display: inline-flex; align-items: center; gap: 6px; font-size: .85rem; color: var(--text-3); margin-bottom: 18px; }
.back:hover { color: var(--teal-d); }
.ds-title { font-family: var(--display); font-size: clamp(1.7rem, 4vw, 2.5rem); font-weight: 600; letter-spacing: -.02em; line-height: 1.1; }
.ds-sub { color: var(--text-2); max-width: 72ch; margin: 12px 0 0; }
.ds-tags { display: flex; flex-wrap: wrap; gap: 7px; margin: 16px 0 0; }
.kw { display: inline-block; background: rgba(13,148,136,.08); color: var(--teal-d); border-radius: 6px; padding: 2px 10px; font-size: .76rem; }
.tier-note {
  display: flex; gap: 12px; align-items: flex-start; margin: 22px 0 0; padding: 14px 18px; border-radius: 12px;
  border: 1px solid; font-size: .88rem; line-height: 1.55;
}
.tier-note.private { background: rgba(217,119,6,.07); border-color: rgba(217,119,6,.28); color: #92500a; }
.tier-note.anonymized { background: rgba(79,70,229,.07); border-color: rgba(79,70,229,.26); color: #3730a3; }
.tier-note .ico { font-size: 1.1rem; line-height: 1.3; }

.panel-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 20px; }
.panel {
  background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius);
  box-shadow: var(--shadow); overflow: hidden;
}
.panel.wide { grid-column: 1 / -1; }
.panel > h2 {
  font-family: var(--display); font-size: 1.04rem; font-weight: 600; padding: 16px 20px;
  border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 10px;
}
.panel-body { padding: 18px 20px; }

table.kv, table.data { width: 100%; border-collapse: separate; border-spacing: 0; font-size: .87rem; }
table.kv caption, table.data caption {
  text-align: left; font-family: var(--display); font-weight: 600; padding: 14px 18px;
  border-bottom: 1px solid var(--border); color: var(--text);
}
table.kv th, table.kv td, table.data th, table.data td { text-align: left; padding: 8px 18px; border-top: 1px solid var(--border); vertical-align: top; }
table.kv tr:first-child th, table.kv tr:first-child td { border-top: none; }
table.kv th { color: var(--text-3); font-weight: 600; width: 40%; }
/* keep long values (DOIs, descriptions, numbers) inside the key/value table */
table.kv td { word-break: break-word; overflow-wrap: anywhere; }
table.data thead th { background: var(--bg-alt); color: var(--text-3); font-size: .74rem; text-transform: uppercase; letter-spacing: .05em; border-top: none; position: sticky; top: 0; }
table.data tbody tr:hover { background: var(--bg-alt); }
table.data td.num, table.data th.num { text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }
table.data tbody th { color: var(--text-2); font-weight: 600; }
table.data td { overflow-wrap: anywhere; }
.table-scroll { overflow-x: auto; border: 1px solid var(--border); border-radius: 10px; background: #fff; }
.table-scroll table.data { min-width: 720px; }
.table-scroll table.data thead th:first-child, .table-scroll table.data tbody th:first-child, .table-scroll table.data tbody td:first-child {
  position: sticky; left: 0; z-index: 2; background: inherit;
}
.table-scroll table.data thead th:first-child { z-index: 3; background: var(--bg-alt); }

/* ── Charts: enlarge on click ── */
.chart { cursor: zoom-in; position: relative; }
.chart svg { width: 100%; height: auto; display: block; }
.chart::after {
  content: "⤢"; position: absolute; top: 8px; right: 8px; width: 22px; height: 22px;
  display: grid; place-items: center; border-radius: 6px; background: rgba(255,255,255,.9);
  border: 1px solid var(--border); color: var(--text-3); font-size: .82rem; opacity: 0; transition: opacity .15s;
}
.chart:hover::after, .chart:focus::after { opacity: 1; }

/* ── Dataset-page: spectral source cards + per-variable cards ── */
.source-card {
  background: var(--bg-alt); border: 1px solid var(--border); border-radius: var(--radius);
  padding: 18px 20px; margin-bottom: 18px;
}
.source-head { display: flex; align-items: baseline; gap: 12px; margin-bottom: 12px; flex-wrap: wrap; }
.source-head h3 { font-family: var(--display); font-size: 1.05rem; margin: 0; }
.src-meta { font-size: .76rem; color: var(--text-3); font-family: var(--mono); }
.chart-spectra { background: linear-gradient(180deg, #fff, #fbfdff); border: 1px solid var(--border); border-radius: 12px; padding: 8px 10px; margin-bottom: 14px; box-shadow: inset 0 1px 0 rgba(255,255,255,.85); }

.explorer-grid { display: grid; grid-template-columns: minmax(300px, 520px) minmax(300px, 1fr); gap: 18px; align-items: start; margin-bottom: 18px; }
@media (max-width: 860px) { .explorer-grid { grid-template-columns: 1fr; } }
.profile-summary { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 10px; margin-bottom: 16px; }
.profile-summary div { border: 1px solid var(--border); border-radius: 10px; background: linear-gradient(180deg, #fff, var(--bg-alt)); padding: 10px 12px; min-width: 0; }
.profile-summary span { display: block; color: var(--text-3); font-size: .68rem; text-transform: uppercase; letter-spacing: .06em; font-weight: 600; margin-bottom: 4px; }
.profile-summary b { display: block; color: var(--text); font-family: var(--mono); font-size: .86rem; font-weight: 600; overflow-wrap: anywhere; }
@media (max-width: 760px) { .profile-summary { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (max-width: 460px) { .profile-summary { grid-template-columns: 1fr; } }
.profile-radar, .diag-chart, .pca-score-chart, .xy-corr-chart { background: linear-gradient(180deg, #fff, #fbfdff); border: 1px solid var(--border); border-radius: 12px; padding: 8px 10px; margin-bottom: 12px; box-shadow: inset 0 1px 0 rgba(255,255,255,.85); }
.source-viz-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr)); gap: 12px; align-items: start; margin-top: 14px; }
.diag-table { min-width: 820px; }
.diag-table th:first-child { min-width: 190px; }
.diag-table th small { display: block; color: var(--text-3); font-family: var(--mono); font-size: .7rem; font-weight: 500; margin-top: 2px; }
.diag-table td:nth-child(2), .diag-table td:nth-child(3) { white-space: nowrap; }
.diag-table td:last-child { min-width: 260px; }
.metric-ref { min-width: 1080px; }
.metric-ref td:first-child { font-weight: 600; color: var(--text-2); min-width: 150px; }
.metric-ref code { color: var(--teal-d); background: rgba(13,148,136,.07); border: 1px solid rgba(13,148,136,.18); border-radius: 6px; padding: 2px 6px; white-space: nowrap; }
.metric-scores { margin-top: 14px; border: 1px solid var(--border); border-radius: 12px; background: #fff; padding: 4px 14px 14px; }
.metric-scores summary { cursor: pointer; font-family: var(--display); font-size: .92rem; font-weight: 600; padding: 10px 0; display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }
.metric-scores summary span { font-size: .7rem; font-family: var(--mono); background: var(--bg-alt); border: 1px solid var(--border); border-radius: 20px; padding: 2px 10px; color: var(--text-2); }
.metric-scores summary em { font-style: normal; font-family: var(--mono); font-size: .72rem; color: var(--text-3); margin-left: auto; }
.metric-score-table table.data { min-width: 1120px; }
.metric-score-table td:first-child { min-width: 150px; font-weight: 600; color: var(--text-2); }
.metric-score-table code { color: var(--teal-d); background: rgba(13,148,136,.07); border: 1px solid rgba(13,148,136,.18); border-radius: 6px; padding: 2px 6px; white-space: nowrap; }
.metric-score-table td small, .formula-cell small { display: block; color: var(--text-3); font-size: .72rem; line-height: 1.35; margin-top: 3px; }
.metric-score-table tbody tr { background: #fff; }
.metric-score-table tbody tr:nth-child(odd) { background: #fcfdff; }
.metric-score-table td:nth-child(3), .metric-score-table td:nth-child(4) { font-variant-numeric: tabular-nums; }
.formula-cell { min-width: 260px; color: var(--text-2); }
.formula-cell span { font-family: var(--mono); font-size: .76rem; color: var(--text); }
.score-col { text-align: right; white-space: nowrap; }
.score-pill { display: inline-flex; align-items: center; justify-content: center; min-width: 42px; height: 23px; border-radius: 999px; border: 1px solid var(--border); font-family: var(--mono); font-size: .74rem; font-weight: 600; }
.score-low { color: #0f766e; background: rgba(15,118,110,.08); border-color: rgba(15,118,110,.20); }
.score-mid { color: #9a5b00; background: rgba(217,119,6,.10); border-color: rgba(217,119,6,.24); }
.score-high { color: #9f1239; background: rgba(159,18,57,.09); border-color: rgba(159,18,57,.22); }
.score-na { color: var(--text-3); background: var(--bg-alt); }
.metric-score-table tbody tr.score-row-high { background: rgba(159,18,57,.035); }
.metric-score-table tbody tr.score-row-mid { background: rgba(217,119,6,.035); }
.metric-score-table tbody tr.score-row-low { background: rgba(15,118,110,.025); }
.reference-guidance, .tech-guidance { margin-top: 14px; border: 1px solid var(--border); border-radius: 12px; background: var(--bg-alt); padding: 4px 14px 12px; }
.reference-guidance:first-child, .tech-guidance:first-child { margin-top: 0; }
.reference-guidance summary, .tech-guidance summary { cursor: pointer; font-family: var(--display); font-weight: 600; font-size: .92rem; padding: 10px 0; color: var(--text); display: flex; align-items: center; gap: 10px; }
.reference-guidance summary span { font-size: .7rem; font-family: var(--mono); background: #fff; border: 1px solid var(--border); border-radius: 20px; padding: 2px 10px; color: var(--text-2); }
.xy-panel { margin-top: 14px; border: 1px solid var(--border); border-radius: 12px; background: #fff; padding: 4px 14px 14px; }
.xy-panel summary { cursor: pointer; font-family: var(--display); font-size: .92rem; font-weight: 600; padding: 10px 0; display: flex; align-items: center; gap: 10px; }
.xy-panel summary span { font-size: .7rem; font-family: var(--mono); background: var(--bg-alt); border: 1px solid var(--border); border-radius: 20px; padding: 2px 10px; color: var(--text-2); }
.xy-charts { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 12px; }
.xy-table { margin-top: 6px; }

.stat-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }
.stat-card { background: #fff; border: 1px solid var(--border); border-radius: 12px; padding: 12px 15px; }
.stat-card h4 { font-family: var(--display); font-size: .68rem; text-transform: uppercase; letter-spacing: .07em; color: var(--text-3); margin: 0 0 8px; }
table.stat-table { width: 100%; border-collapse: collapse; font-size: .83rem; }
table.stat-table th { text-align: left; font-weight: 500; color: var(--text-2); padding: 3px 0; white-space: nowrap; vertical-align: top; }
table.stat-table td { text-align: right; font-family: var(--mono); color: var(--text); padding: 3px 0 3px 12px; font-variant-numeric: tabular-nums; word-break: break-word; }

.var-group { font-family: var(--display); font-size: 1rem; margin: 24px 0 12px; display: flex; align-items: center; gap: 10px; }
.var-group span { font-size: .7rem; font-family: var(--mono); background: var(--bg-alt); border: 1px solid var(--border); border-radius: 20px; padding: 2px 10px; color: var(--text-2); }
.var-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 360px), 1fr)); gap: 16px; }
.var-card { background: var(--bg-alt); border: 1px solid var(--border); border-radius: var(--radius); padding: 14px 16px; display: flex; flex-direction: column; gap: 10px; }
.var-card-head { display: flex; align-items: baseline; justify-content: space-between; gap: 10px; }
.var-card-head h4 { margin: 0; font-family: var(--display); font-size: .92rem; word-break: break-word; }
.var-tag { font-size: .66rem; color: var(--text-3); font-family: var(--mono); white-space: nowrap; }
.var-chart { background: #fff; border: 1px solid var(--border); border-radius: 10px; padding: 6px 8px; }
.var-card .stat-table { font-size: .8rem; }

.const-meta { margin-top: 18px; border: 1px solid var(--border); border-radius: 12px; background: var(--bg-alt); padding: 2px 16px; }
.const-meta summary { cursor: pointer; font-family: var(--display); font-size: .9rem; padding: 10px 0; display: flex; align-items: center; gap: 10px; }
.const-meta summary span { font-size: .7rem; font-family: var(--mono); background: var(--bg); border: 1px solid var(--border); border-radius: 20px; padding: 2px 10px; color: var(--text-2); }
.const-meta ul { list-style: none; padding: 2px 0 14px; columns: 2; column-gap: 30px; }
@media (max-width: 640px) { .const-meta ul { columns: 1; } }
.const-meta li { display: flex; justify-content: space-between; gap: 14px; padding: 5px 0; border-bottom: 1px dotted var(--border); break-inside: avoid; font-size: .84rem; }
.const-meta li span { color: var(--text-2); word-break: break-word; }
.const-meta li b { font-family: var(--mono); font-weight: 500; color: var(--text); text-align: right; }

/* ── Lightbox (chart zoom popup) ── */
.lightbox { position: fixed; inset: 0; z-index: 999; display: none; place-items: center; background: rgba(8,15,26,.72); backdrop-filter: blur(3px); padding: 5vh 5vw; }
.lightbox.open { display: grid; }
.lightbox .lb-panel { background: #fff; border-radius: 18px; padding: 26px 28px; max-width: 1120px; width: 100%; max-height: 90vh; overflow: auto; box-shadow: var(--shadow-lg); }
.lightbox .lb-panel svg { width: 100%; height: auto; }
.lightbox .lb-close { position: absolute; top: 18px; right: 26px; font-size: 2rem; color: #fff; cursor: pointer; line-height: 1; }

.dl-row { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }
.dl-btn {
  display: inline-flex; align-items: center; gap: 7px; padding: 9px 16px; border-radius: 9px;
  border: 1px solid var(--border); background: #fff; font-size: .84rem; font-weight: 600; color: var(--text);
}
.dl-btn:hover { border-color: var(--teal); color: var(--teal-d); background: rgba(13,148,136,.04); }
.dl-note { font-size: .84rem; color: var(--text-3); }

/* ── Footer ────────────────────────────────────────────────────── */
footer { background: radial-gradient(ellipse 120% 80% at 50% -10%, #10233a 0%, #0b1626 60%, #070e1a 100%); color: rgba(255,255,255,0.7); padding: 56px 0 40px; }
footer .container { display: flex; flex-wrap: wrap; gap: 28px; justify-content: space-between; align-items: flex-start; }
footer a { color: var(--teal-l); }
footer a:hover { color: #fff; }
footer .f-brand { font-family: var(--display); font-weight: 600; font-size: 1.15rem; color: #fff; margin-bottom: 8px; }
footer .f-meta { font-size: .82rem; line-height: 1.8; max-width: 42ch; }
footer .f-links { display: flex; flex-direction: column; gap: 6px; font-size: .85rem; }
footer .f-note { width: 100%; border-top: 1px solid rgba(255,255,255,.08); margin-top: 32px; padding-top: 20px; font-size: .76rem; color: rgba(255,255,255,.45); }

/* Wide / tall charts bake their labels at a desktop size; on a phone, letting them shrink to fit makes
   the text illegible. Instead the widest charts scroll horizontally (keeping a legible minimum), and the
   tap-to-zoom lightbox opens any chart large enough to pan. */
@media (max-width: 720px) {
  .viz-card.wide .viz-canvas, .chart-spectra { overflow-x: auto; -webkit-overflow-scrolling: touch; }
  .viz-card.wide .viz-canvas svg { min-width: 600px; }
  .chart-spectra svg { min-width: 560px; }
  .lightbox { padding: 3vh 3vw; }
  .lightbox .lb-panel { padding: 16px 18px; }
  .lightbox .lb-panel svg { min-width: 520px; }
}

@media (max-width: 640px) {
  .nav-links a:not(.active) { display: none; }
  .ds-meta { grid-template-columns: 1fr; }
}
"""


def page(*, title: str, rel: str, body: str, scripts: str = "", active: str = "") -> str:
    """The base HTML shell: ``<head>`` (fonts + inline CSS) + ``<body>`` with ``body`` and ``scripts``.

    ``rel`` is the relative prefix to the site root (``""`` for top-level pages, ``"../"`` for
    ``dataset/<id>.html``); it is interpolated into nav/footer links so the page works from ``file://``.
    """
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="A citable, reproducible bank of raw NIRS reference datasets.">
<meta name="theme-color" content="#0d9488">
{FONTS_LINK}
<style>{CSS}</style>
</head>
<body>
{body}
{scripts}
{LIGHTBOX}
{GOATCOUNTER}
</body>
</html>
"""


# GoatCounter privacy-friendly analytics (no cookies), aggregated as one ecosystem page.
GOATCOUNTER = """<script data-goatcounter="https://nirs4all.goatcounter.com/count" data-goatcounter-settings='{"path": "/datasets"}' async src="//gc.zgo.at/count.js"></script>"""


# Chart zoom: clicking any `.chart` clones its SVG into a centred lightbox (Esc / backdrop to close).
LIGHTBOX = """<div id="lb" class="lightbox" aria-hidden="true"><span class="lb-close" aria-label="close">×</span><div class="lb-panel"></div></div>
<script>(function(){var lb=document.getElementById('lb'),p=lb.querySelector('.lb-panel');
function close(){lb.classList.remove('open');p.innerHTML='';}
document.addEventListener('click',function(e){var c=e.target.closest('.chart');
  if(c){var s=c.querySelector('svg');if(s){p.innerHTML=s.outerHTML;lb.classList.add('open');}return;}
  if(e.target===lb||e.target.closest('.lb-close'))close();});
document.addEventListener('keydown',function(e){if(e.key==='Escape')close();});})();</script>"""
