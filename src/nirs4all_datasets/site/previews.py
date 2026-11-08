"""Project public catalogue entries into the shared browser preview's presentation contract.

Only the already public/anonymized entry and named presentation flags are consumed. Cards,
descriptors, origins, axes and scientific inference do not belong in this projection.
"""
from __future__ import annotations

from typing import Any

from .model import DatasetView


def _declared_int(value: Any) -> int | None:
    """Return a declared integer count, preserving zero and excluding booleans."""
    return value if isinstance(value, int) and not isinstance(value, bool) else None


def preview_view(view: DatasetView) -> dict[str, Any]:
    """Whitelist a public entry into a data-only ``DatasetPreviewView`` without UI inference."""
    entry = view.entry
    samples = _declared_int(entry.get("n_samples"))
    features = _declared_int(entry.get("n_features_total"))
    targets = _declared_int(entry.get("n_targets"))
    sources = _declared_int(entry.get("n_sources"))
    tier_label = {"public": "Open redistribution", "private": "Restricted redistribution", "anonymized": "Anonymized"}.get(view.tier, view.tier)
    badges = [{"id": f"tier-{view.tier}", "label": tier_label, "tone": "default"}]
    if view.has_open_retrieval:
        badges.append({"id": "open-access", "label": "Open source access", "tone": "default"})
    retrieval = {
        "canonical_verified": ("canonical verified", "default"),
        "raw_reproducible": ("raw reproducible", "default"),
        "token_required": ("token access / hosting pending", "warning"),
        "manual": ("manual retrieval", "warning"),
        "delegate": ("delegate", "muted"),
        "missing_delegate": ("raw source available · assembly incomplete", "warning"),
        "blocked_parser": ("source available · parser needed", "warning"),
        "manual_only": ("manual source access", "warning"),
        "documented_only": ("retrieval not implemented", "muted"),
    }.get(str(entry.get("retrieval_status") or ""))
    if retrieval:
        badges.append({"id": f"retrieval-{entry['retrieval_status']}", "label": retrieval[0], "tone": retrieval[1]})
    if sources is not None:
        badges.append({"id": "sources", "label": f"{sources:,} {'source' if sources == 1 else 'sources'}", "tone": "default"})
    if targets == 0:
        badges.append({"id": "metadata-only", "label": "metadata-only", "tone": "muted"})
    if entry.get("has_split"):
        badges.append({"id": "native-split", "label": "native split", "tone": "muted"})
    if not view.has_card:
        badges.append({"id": "card-pending", "label": "card pending", "tone": "warning"})
    elif view.is_stale:
        badges.append({"id": "card-stale", "label": "stale card", "tone": "warning"})
    if (entry.get("health") or {}).get("degraded"):
        badges.append({"id": "origin-degraded", "label": "origin degraded", "tone": "warning"})
    stats = [
        {
            "id": key,
            "label": label,
            "value": f"{value:,}" if value is not None else "—",
            "detail": "total across sources" if key == "features" and sources is not None and sources > 1 else None,
            "tone": "default" if value is not None else "muted",
        }
        for key, label, value in (("samples", "Samples", samples), ("features", "Spectral variables", features), ("targets", "Targets", targets))
    ]
    return {
        "id": str(entry["id"]),
        "title": f"{entry.get('domain') or '—'} · {entry.get('spectro_family') or '—'}",
        "description": None,
        "taskKind": "unknown",
        "taskLabel": entry.get("task") or "",
        "sampleCount": samples,
        "sampleCountLabel": None,
        "featureCount": features,
        "featureCountLabel": None,
        "targetCount": targets,
        "targetCountLabel": None,
        "classCount": None,
        "classCountLabel": None,
        "spectralRangeLabel": None,
        "splitCounts": [],
        "splitSummaryLabel": None,
        "tags": [],
        "badges": badges,
        "stats": stats,
    }
