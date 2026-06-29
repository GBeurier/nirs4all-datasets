"""User-facing retrieval helper."""
from __future__ import annotations

import json

import pytest

from nirs4all_datasets.retrieval import retrieve


def _write_index(root, entry):
    path = root / "catalog" / "index.json"
    path.parent.mkdir(parents=True)
    path.write_text(
        json.dumps({"schema": "1.0", "n_datasets": 1, "datasets": {"demo": entry}}),
        encoding="utf-8",
    )


def test_retrieve_uses_first_open_raw_route(tmp_path, monkeypatch):
    route = {
        "id": "raw",
        "priority": 100,
        "method": "raw_retrieve",
        "provider": "url",
        "access": "open",
        "locator": "https://example.test/raw.csv",
        "resources": [{"id": "raw", "selector": {"kind": "direct_url", "value": "https://example.test/raw.csv"}}],
    }
    entry = {
        "tier": "public",
        "dataverse": {"instance": "https://dv.example", "doi": None, "dataset_version": None},
        "files": [],
        "origins": [],
        "retrieval": {"status": "raw_reproducible", "routes": [route]},
        "descriptor": {"id": "demo"},
    }
    _write_index(tmp_path, entry)

    from nirs4all_datasets import _acquire

    monkeypatch.setattr(_acquire, "resolve", lambda index, dataset_id: {"id": dataset_id, "doi": None, **index["datasets"][dataset_id]})

    def fake_retrieve_raw(request, opts):
        assert request == {"dataset_id": "demo", "route": route}
        assert opts["cache_dir"] == str(tmp_path / "cache")
        return {"dir": "/cache/demo/raw", "ok": True, "verified": False, "route_id": "raw", "resources": []}

    def fake_prepare_raw(request, opts):
        assert request == {"dataset_id": "demo", "route": route}
        assert opts["cache_dir"] == str(tmp_path / "cache")
        return {"dir": "/cache/demo/raw/prepared", "ok": True, "route_id": "raw", "resources": []}

    monkeypatch.setattr(_acquire, "retrieve_raw", fake_retrieve_raw)
    monkeypatch.setattr(_acquire, "prepare_raw", fake_prepare_raw)
    result = retrieve("demo", root=tmp_path, cache_dir=tmp_path / "cache")

    assert result["dataset_id"] == "demo"
    assert result["kind"] == "raw"
    assert result["ok"] is True
    assert result["preparation"]["ok"] is True


def test_retrieve_token_pending_without_dataverse_doi_is_actionable(tmp_path, monkeypatch):
    entry = {
        "tier": "private",
        "dataverse": {"instance": "https://dv.example", "doi": None, "dataset_version": None},
        "files": [],
        "origins": [],
        "retrieval": {"status": "token_required", "routes": [], "blockers": ["upload pending"]},
        "descriptor": {"id": "demo"},
    }
    _write_index(tmp_path, entry)

    from nirs4all_datasets import _acquire

    monkeypatch.setattr(_acquire, "resolve", lambda index, dataset_id: {"id": dataset_id, "doi": None, **index["datasets"][dataset_id]})

    with pytest.raises(RuntimeError, match="pending token-gated Dataverse hosting"):
        retrieve("demo", root=tmp_path)
