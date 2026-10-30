"""Project task evidence already recorded in a card without loading dataset bytes."""
from __future__ import annotations

from copy import deepcopy
from typing import Any


def project_card_tasks(card: dict[str, Any]) -> dict[str, Any]:
    """Recover binary target evidence in legacy cards from exact curation cardinalities.

    Source-column mappings must be unambiguous. Histograms supply counts only after the
    exact two-value evidence and numeric endpoints establish the two possible values.
    """
    result = deepcopy(card)
    candidates: dict[str, list[dict[str, Any]]] = {}
    for item in (result.get("curation") or {}).get("variables", []):
        if item.get("view") != "Y":
            continue
        names = {item.get("name")}
        names.update(source.get("name") for source in item.get("source_columns", []) if source.get("resource") == "Y.csv")
        for name in names:
            if isinstance(name, str):
                candidates.setdefault(name, []).append(item)
    for variable in result.get("variables") or []:
        if variable.get("role") != "target" or variable.get("type") != "numeric" or variable.get("task_type") not in {None, "unavailable"}:
            continue
        matches = candidates.get(variable.get("name"), [])
        stats = variable.get("stats") or {}
        if len(matches) != 1:
            continue
        evidence = matches[0].get("stats") or {}
        if evidence.get("n_unique") != 2 or evidence.get("n_rows") != stats.get("n") or evidence.get("n_missing") != stats.get("n_missing") or stats.get("min") != 0 or stats.get("max") != 1:
            continue
        variable["task_type"] = "classification"
        histogram = variable.get("histogram") or {}
        counts, edges = histogram.get("counts") or [], histogram.get("edges") or []
        if len(counts) >= 2 and len(edges) == len(counts) + 1 and edges[0] == 0 and edges[-1] == 1 and not any(counts[1:-1]) and sum(counts) == (stats.get("n") or 0) - (stats.get("n_missing") or 0):
            variable["class_stats"] = {"n": stats.get("n"), "n_missing": stats.get("n_missing"), "n_classes": 2, "top_classes": [{"name": "0", "count": counts[0]}, {"name": "1", "count": counts[-1]}]}
    return result


def card_task_kinds(card: dict[str, Any], targets: list[str]) -> set[str] | None:
    """Return available tasks when every selected target exists; omit unavailable inferences."""
    variables = {v.get("name"): v for v in card.get("variables") or [] if v.get("role") == "target"}
    if any(name not in variables for name in targets):
        return None
    return {"classification" if variables[name].get("task_type") == "classification" or variables[name].get("type") in {"categorical", "text", "identifier"} else "regression" for name in targets if variables[name].get("task_type") != "unavailable"}
