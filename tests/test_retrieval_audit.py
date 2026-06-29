"""Static retrieval audit generation."""
from __future__ import annotations

import yaml

from nirs4all_datasets.retrieval_audit import build_retrieval_audit


def _descriptor(**over):
    data = {
        "schema_version": "2.0",
        "id": "demo",
        "name": "Demo",
        "description": "Demo dataset.",
        "sources": [{"source_id": "X", "axis_unit": "nm"}],
        "variables": [{"name": "Moisture", "role": "target", "type": "numeric"}],
        "tier": "public",
        "provenance": {"contributor": "Lab"},
        "governance": {
            "license": "CC-BY-4.0",
            "owner_steward": "Lab",
            "redistribution_rights": "open",
            "consent_ethics_status": "n/a",
            "anonymization_status": "n/a",
            "permitted_use": "research",
            "access_policy": "open",
        },
        "origin_sources": [{"kind": "url", "mode": "raw", "locator": "https://example.test/raw.csv", "access": "open"}],
    }
    data.update(over)
    return data


def _write_descriptor(root, data):
    path = root / "catalog" / "datasets" / f"{data['id']}.yaml"
    path.parent.mkdir(parents=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")


def test_retrieval_audit_detects_nirs_db_script_without_executing_it(tmp_path):
    _write_descriptor(tmp_path, _descriptor())
    script = tmp_path / "NIRS DB" / "v2.0" / "demo" / "source_to_standard.py"
    script.parent.mkdir(parents=True)
    script.write_text("import requests\nURL = 'https://example.test/raw.csv'\n", encoding="utf-8")

    report = build_retrieval_audit(tmp_path)
    row = report["datasets"][0]

    assert report["summary"]["n_with_script"] == 1
    assert row["dataset_id"] == "demo"
    assert row["script"]["sha256"]
    assert row["script"]["urls"] == ["https://example.test/raw.csv"]
    assert row["proposed_route_type"] == "raw_retrieve"


def test_retrieval_audit_marks_private_without_open_source_as_token_required(tmp_path):
    _write_descriptor(tmp_path, _descriptor(id="private_demo", tier="private", origin_sources=[]))

    report = build_retrieval_audit(tmp_path)
    row = report["datasets"][0]

    assert row["proposed_route_type"] == "token_required"
    assert "requires token-gated hosted fallback or source credential" in row["blockers"]
    pending = tmp_path / "docs" / "DATAVERSE_PENDING.md"
    assert pending.exists()
    assert "private_demo" in pending.read_text(encoding="utf-8")
