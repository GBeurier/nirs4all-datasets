"""Optional, versioned external assessments; scientific kernels stay with their producer.

The sidecar is distinct from the legacy card and canonical content. It binds reports
by content hash and context; task/split-dependent findings never become intrinsic QC.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

from nirs4all_datasets.manifest import sha256_file


class AssessmentMetric(BaseModel):
    """A producer-owned observation with explicit availability and protocol."""

    model_config = ConfigDict(extra="forbid", allow_inf_nan=False)
    metric_id: str = Field(min_length=1)
    protocol_version: str = Field(min_length=1)
    value: float | None = None
    unit: str | None = None
    availability: Literal["available", "unavailable", "not_applicable"]
    reason_code: str | None = None
    kind: Literal["measured_observation", "heuristic_signature", "possible_cause"] = "measured_observation"
    confidence_status: Literal["unvalidated", "unknown", "validated"] = "unknown"
    native_status: str | None = None
    native_metric: dict[str, Any] | None = None
    view_id: str = "native"
    evidence_coverage: float | None = Field(default=None, ge=0, le=1)
    signal_strength: float | None = Field(default=None, ge=0, le=1)

    @model_validator(mode="after")
    def check_availability(self) -> AssessmentMetric:
        if self.availability == "available" and self.value is None:
            raise ValueError("available metrics require a finite value")
        if self.availability != "available" and (self.value is not None or not self.reason_code):
            raise ValueError("unavailable metrics require a reason_code and null value")
        return self


class Assessment(BaseModel):
    """One immutable assessment context, separate from canonical dataset identity."""

    model_config = ConfigDict(extra="forbid", allow_inf_nan=False)
    schema_version: Literal["1"] = "1"
    dataset_id: str = Field(min_length=1)
    content_hash: str = Field(pattern=r"^(?:sha256:)?[0-9a-f]{64}$")
    producer: Literal["nirs4all-preflight", "nirs4all-domains", "nirs4all-methods"]
    engine_version: str = Field(min_length=1)
    protocol_version: str = Field(min_length=1)
    source_id: str = Field(min_length=1)
    population_id: str = Field(min_length=1)
    context_id: str = Field(min_length=1)
    scope: Literal["intrinsic", "task"]
    target_id: str | None = None
    split_id: str | None = None
    fit_population_id: str | None = None
    evaluation_population_id: str | None = None
    metrics: list[AssessmentMetric] = Field(default_factory=list)
    report: dict[str, Any] | None = None

    @model_validator(mode="after")
    def check_context(self) -> Assessment:
        if self.scope == "intrinsic" and any((self.target_id, self.split_id, self.fit_population_id, self.evaluation_population_id)):
            raise ValueError("intrinsic assessments cannot contain target/split/evaluation context")
        if self.scope == "task" and not all((self.target_id, self.split_id, self.fit_population_id, self.evaluation_population_id)):
            raise ValueError("task assessments require target, split and fit/evaluation populations")
        keys = [(m.metric_id, m.protocol_version, m.view_id) for m in self.metrics]
        if len(keys) != len(set(keys)):
            raise ValueError("duplicate metric/protocol identity")
        json.dumps(self.model_dump(mode="json"), allow_nan=False)
        return self


def canonical_content_hash(dataset_dir: str | Path) -> str:
    """Hash canonical relative paths and bytes, excluding every optional assessment."""
    canonical = Path(dataset_dir) / "canonical"
    if not (canonical / "dataset.json").is_file():
        raise FileNotFoundError("canonical/dataset.json is required")
    records = [(str(p.relative_to(canonical)), sha256_file(p)) for p in sorted(canonical.rglob("*")) if p.is_file()]
    return hashlib.sha256(json.dumps(records, separators=(",", ":")).encode()).hexdigest()


def validate_assessments(reports: list[dict[str, Any]], dataset_dir: str | Path, dataset_id: str) -> list[dict[str, Any]]:
    """Reject stale, wrong-dataset or colliding contexts; never silently rebind reports."""
    expected = canonical_content_hash(dataset_dir)
    result = []
    contexts = set()
    config = json.loads((Path(dataset_dir) / "canonical/dataset.json").read_text(encoding="utf-8"))
    sources = {s["source_id"] for s in config.get("sources", [])}
    for raw in reports:
        report = Assessment.model_validate(raw)
        if report.dataset_id != dataset_id or report.content_hash.removeprefix("sha256:") != expected:
            raise ValueError("assessment dataset/content identity does not match canonical bytes")
        if report.source_id not in sources:
            raise ValueError("assessment source is absent from canonical data")
        key = (report.producer, report.source_id, report.target_id, report.split_id, report.population_id, report.context_id, report.protocol_version)
        if key in contexts:
            raise ValueError("duplicate assessment context")
        contexts.add(key)
        result.append(report.model_dump(mode="json"))
    return result


def write_assessments(dataset_dir: str | Path, dataset_id: str, reports: list[dict[str, Any]]) -> None:
    """Atomically cache validated reports without changing cards or canonical bytes."""
    checked = validate_assessments(reports, dataset_dir, dataset_id)
    path = Path(dataset_dir) / "assessments.json"
    temporary = path.with_suffix(".json.tmp")
    temporary.write_text(json.dumps({"schema_version": "1", "reports": checked}, indent=2, allow_nan=False), encoding="utf-8")
    os.replace(temporary, path)


def read_assessments(dataset_dir: str | Path, dataset_id: str) -> list[dict[str, Any]]:
    """Read the optional sidecar; absence preserves every legacy card/API behavior."""
    path = Path(dataset_dir) / "assessments.json"
    if not path.exists():
        return []
    value = json.loads(path.read_text(encoding="utf-8"))
    if value.get("schema_version") != "1" or not isinstance(value.get("reports"), list):
        raise ValueError("unsupported assessment sidecar")
    return validate_assessments(value["reports"], dataset_dir, dataset_id)


def public_assessments(reports: list[dict[str, Any]], *, anonymized: bool) -> list[dict[str, Any]]:
    """Suppress report identifiers, free text and detailed values for anonymized data."""
    if not anonymized:
        return reports
    return [{"schema_version": "1", "producer": r["producer"], "engine_version": r["engine_version"], "protocol_version": r["protocol_version"], "scope": r["scope"], "availability": "redacted", "reason_code": "anonymized_tier"} for r in reports]


def intrinsic_profile(report: dict[str, Any], *, view_id: str = "native") -> dict[str, Any]:
    """Project versioned producer metrics into legacy display slots, without kernels.

    Only exact documented legacy slot IDs are consumed. Unknown additive metric IDs
    remain in the assessment rather than being guessed or recomputed.
    """
    parsed = Assessment.model_validate(report)
    if parsed.scope != "intrinsic":
        raise ValueError("task-scoped reports cannot populate intrinsic source profiles")
    from nirs4all_datasets.qualify import metrics

    sections = {"integrity", "amplitude", "noise", "artefacts", "shape", "outliers", "reference", "repeatability", "structure"}
    profile: dict[str, Any] = {key: {} for key in sections}
    for metric in parsed.metrics:
        if metric.view_id != view_id:
            continue
        section, separator, key = metric.metric_id.partition(".")
        if separator and section in sections:
            profile[section][key] = metric.value if metric.availability == "available" else None
    profile["profile_scores"] = metrics._profile_scores(profile)
    profile["diagnostics"] = metrics.diagnostic_hypotheses(profile, top_k=8)
    profile["producer"] = {"name": parsed.producer, "engine_version": parsed.engine_version, "protocol_version": parsed.protocol_version}
    return profile
