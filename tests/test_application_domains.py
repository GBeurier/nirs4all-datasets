"""Curated application domains: complete catalog coverage, closed list and summary aggregation."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from nirs4all_datasets.catalog import APPLICATION_DOMAINS_FILE, UNDISCLOSED, _application_domain, application_domain_errors, descriptor_paths, load_application_domains

REPO = Path(__file__).resolve().parents[1]


def test_every_catalog_dataset_has_a_curated_domain() -> None:
    mapping = load_application_domains(REPO)
    assert mapping is not None, f"{APPLICATION_DOMAINS_FILE} is missing"
    ids = {path.stem for path in descriptor_paths(REPO)}
    assert application_domain_errors(mapping, ids) == []  # new datasets must be curated in catalog/application_domains.yaml


def test_domain_errors_report_missing_unknown_and_out_of_list_entries() -> None:
    mapping: dict[str, Any] = {
        "domains": ["Soil science"],
        "datasets": {"soil": {"primary": "Soil science", "evidence": "name"}, "ghost": {"primary": "Astrology", "evidence": "name"}},
    }
    errors = application_domain_errors(mapping, {"soil", "wheat"})
    assert "wheat: no curated application domain." in errors
    assert "ghost: curated application domain for an unknown dataset." in errors
    assert "ghost: domain 'Astrology' is not in the closed list." in errors


def test_anonymized_datasets_do_not_disclose_their_domain() -> None:
    mapping = {"domains": ["Soil science"], "datasets": {"soil": {"primary": "Soil science", "evidence": "name"}}}
    assert _application_domain(mapping, {"id": "soil", "tier": "anonymized"}) == UNDISCLOSED
    assert _application_domain(mapping, {"id": "soil", "tier": "public"}) == "Soil science"
