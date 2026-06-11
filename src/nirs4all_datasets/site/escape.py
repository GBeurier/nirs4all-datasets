"""HTML/JSON escaping + small table/formatting primitives (pure stdlib).

Salvaged from the prior ``site.py``: ``_esc`` / ``_inline_json`` / ``_kv_rows`` / ``_table`` and the
numeric formatter. These are the shared, low-level rendering helpers every page/component builds on;
they never touch nirs4all, pandas, or the filesystem.
"""
from __future__ import annotations

import html
import json
import math
from typing import Any


def esc(value: Any) -> str:
    """HTML-escape a scalar for text/attribute context (``None`` -> empty string)."""
    if value is None:
        return ""
    return html.escape(str(value), quote=True)


def inline_json(obj: Any) -> str:
    """JSON for embedding inside a ``<script>`` tag (neutralizes ``</script>`` and HTML comments)."""
    return json.dumps(obj, allow_nan=False, ensure_ascii=False).replace("</", "<\\/").replace("<!--", "<\\!--")


def num(value: Any, nd: int = 4) -> str:
    """Compact, locale-free number formatting; em-dash for ``None``/non-finite; thousands for ints."""
    if isinstance(value, bool) or value is None:
        return "—"
    if isinstance(value, int):
        return f"{value:,}"
    if isinstance(value, float):
        if not math.isfinite(value):
            return "—"
        if value == int(value) and abs(value) < 1e15:
            return f"{int(value):,}"
        return f"{value:.{nd}g}"
    return esc(value)


def kv_rows(rows: list[tuple[str, Any]]) -> str:
    """Render a 2-column key/value table body, dropping rows whose value is ``None``/empty.

    A value that already starts with ``<`` is treated as trusted pre-rendered HTML (e.g. a link);
    every other value is HTML-escaped.
    """
    out: list[str] = []
    for key, value in rows:
        if value in (None, "", [], {}):
            continue
        rendered = value if (isinstance(value, str) and value.startswith("<")) else esc(value)
        out.append(f"<tr><th>{esc(key)}</th><td>{rendered}</td></tr>")
    return "".join(out)


def table(caption: str, body: str, *, css_class: str = "kv") -> str:
    """Wrap a key/value (or generic) table body in a captioned ``<table>``; empty body -> ``""``."""
    if not body:
        return ""
    return f'<table class="{esc(css_class)}"><caption>{esc(caption)}</caption><tbody>{body}</tbody></table>'


def locator_link(locator: Any) -> str:
    """Render a source/publication locator as a link (DOI -> doi.org, http(s) as-is, else plain text)."""
    loc = str(locator or "").strip()
    if not loc:
        return ""
    if loc.startswith("http"):
        return f'<a href="{esc(loc)}" target="_blank" rel="noopener">{esc(loc)}</a>'
    if loc.startswith("10."):
        return f'<a href="https://doi.org/{esc(loc)}" target="_blank" rel="noopener">{esc(loc)}</a>'
    return esc(loc)
