"""Tests for the per-dataset status + the human-validation registry."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from nirs4all_datasets import status


def _entry(**over: Any) -> dict[str, Any]:
    base = {"id": "d", "tier": "public", "has_card": True, "is_stale": False, "has_manifest": True, "doi": None, "health": {"alive": True, "degraded": False}, "n_samples": 10}
    base.update(over)
    return base


def test_state_origin_distribution() -> None:
    assert status._state(_entry()) == "qualified"
    assert status._state(_entry(has_card=False)) == "canonical"
    assert status._state(_entry(has_card=False, has_manifest=False)) == "described"
    assert status._state(_entry(is_stale=True)) == "canonical"  # stale card -> not "qualified"

    assert status._origin(_entry()) == "verified"
    assert status._origin(_entry(health={"alive": None})) == "unverified"
    assert status._origin(_entry(health={"alive": False})) == "unreachable"
    assert status._origin(_entry(health={"alive": False, "degraded": True})) == "degraded"

    assert status._distribution(_entry(tier="public")) == "open"
    assert status._distribution(_entry(tier="private", doi=None)) == "upload_pending"
    assert status._distribution(_entry(tier="private", doi="10.70112/x")) == "on_dataverse"
    assert status._distribution(_entry(tier="anonymized", doi=None)) == "upload_pending"


def test_dataset_status_combines_state_and_validation() -> None:
    s = status.dataset_status(_entry(tier="private"), {"validation": "approved"})
    assert s["state"] == "qualified" and s["materialized"] is True and s["origin"] == "verified"
    assert s["distribution"] == "upload_pending" and s["validation"] == "approved"
    # default validation when no record
    assert status.dataset_status(_entry(), None)["validation"] == "pending"


def test_validation_registry_init_and_preserve(registry: Path) -> None:
    reg = status.init_validation(registry)
    assert reg["corn"]["validation"] == "pending"
    assert status.validation_path(registry).exists()

    # a human sign-off survives a re-init (e.g. after a bootstrap regeneration)
    path = status.validation_path(registry)
    data = yaml.safe_load(path.read_text())
    data["datasets"]["corn"]["validation"] = "approved"
    data["datasets"]["corn"]["reviewed_by"] = "alice"
    path.write_text(yaml.safe_dump(data))
    reg2 = status.init_validation(registry)
    assert reg2["corn"]["validation"] == "approved" and reg2["corn"]["reviewed_by"] == "alice"

    # an invalid validation value falls back to pending
    data["datasets"]["corn"]["validation"] = "bogus"
    path.write_text(yaml.safe_dump(data))
    assert status.init_validation(registry)["corn"]["validation"] == "pending"


def test_build_reports(registry: Path) -> None:
    from nirs4all_datasets.catalog import build_catalog

    build_catalog(registry)  # corn is public-tier in the fixture
    paths = status.build_reports(registry)
    assert paths["status"].exists() and paths["private"].exists()
    status_md = paths["status"].read_text(encoding="utf-8")
    assert "# Dataset status" in status_md and "`corn`" in status_md and "qualified" in status_md
    # corn is public -> it appears in the status report but NOT in the upload-pending list
    assert "`corn`" not in paths["private"].read_text(encoding="utf-8")
