"""Tests for the qualification metric registry (``qualify.registry``).

The registry is a thin scope-keyed index over the pure numerics in ``qualify.metrics``; it carries a
``PROTOCOL_VERSION`` so a card can be re-qualified without rebuilding canonical bytes. These tests
exercise the version stamp, the per-scope lookup, the ``register`` guards (unknown scope / duplicate
key), and that the registered callables run on a tiny array/series and return a dict.
"""
from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd
import pytest

from nirs4all_datasets.qualify import registry as r


def test_protocol_version_is_nonempty_str() -> None:
    assert isinstance(r.PROTOCOL_VERSION, str)
    assert r.PROTOCOL_VERSION.strip()


def test_metrics_for_returns_registered_metrics() -> None:
    source = r.metrics_for("source")
    variable = r.metrics_for("variable")
    dataset = r.metrics_for("dataset")

    assert {"value_range", "spectral_quality"} <= set(source)
    assert {"numeric_stats", "categorical_stats"} <= set(variable)
    assert {"reps_per_sample"} <= set(dataset)
    assert all(callable(fn) for fn in (*source.values(), *variable.values(), *dataset.values()))


def test_metrics_for_unknown_scope_raises() -> None:
    with pytest.raises(ValueError, match="unknown metric scope"):
        r.metrics_for("bogus")  # type: ignore[arg-type]


def test_metrics_for_returns_a_copy() -> None:
    # Mutating the returned mapping must not affect the live registry.
    snapshot = r.metrics_for("source")
    snapshot["__injected__"] = lambda *a, **k: None
    assert "__injected__" not in r.metrics_for("source")


def test_register_rejects_unknown_scope() -> None:
    with pytest.raises(ValueError, match="unknown metric scope"):
        r.register("anything", "not_a_scope")  # type: ignore[arg-type]


def test_register_rejects_duplicate_key() -> None:
    # 'value_range' is already registered in the 'source' scope; re-registering must raise (and the
    # raise happens before insertion, so this does not pollute the global registry).
    with pytest.raises(ValueError, match="already registered"):
        r.register("value_range", "source")(lambda spectra: {})


def test_register_success_path(monkeypatch: pytest.MonkeyPatch) -> None:
    # Swap the global registry for an isolated copy so registering a new key does not leak across
    # tests; the decorator must record the metric and return the function unchanged.
    isolated = {"source": {}, "variable": {}, "dataset": {}}
    monkeypatch.setattr(r, "_REGISTRY", isolated)

    def my_metric(values: Any) -> dict[str, Any]:
        return {"ok": True}

    returned = r.register("my_metric", "variable")(my_metric)
    assert returned is my_metric
    assert r.metrics_for("variable")["my_metric"] is my_metric


def test_source_metric_callable_on_tiny_array() -> None:
    value_range = r.metrics_for("source")["value_range"]
    out = value_range(np.array([[0.1, 0.2], [0.3, 0.4]], dtype="float64"))
    assert isinstance(out, dict)
    assert set(out) == {"value_min", "value_max", "mean_min", "mean_max"}


def test_variable_metrics_callable() -> None:
    numeric_stats = r.metrics_for("variable")["numeric_stats"]
    num = numeric_stats(np.array([1.0, 2.0, 3.0], dtype="float64"))
    assert isinstance(num, dict)
    assert num["n"] == 3 and num["min"] == 1.0 and num["max"] == 3.0

    categorical_stats = r.metrics_for("variable")["categorical_stats"]
    cat = categorical_stats(pd.Series(["a", "b", "a"]))
    assert isinstance(cat, dict)
    assert cat["n_classes"] == 2 and cat["n"] == 3


def test_dataset_metric_callable() -> None:
    reps_per_sample = r.metrics_for("dataset")["reps_per_sample"]
    out = reps_per_sample(np.array([1.0, 2.0, 3.0], dtype="float64"))
    assert isinstance(out, dict)
    assert out["min"] == 1 and out["max"] == 3 and out["mean"] == 2.0
