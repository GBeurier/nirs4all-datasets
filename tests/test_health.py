"""Tests for the origin-liveness health probe (``health.py``) — no real network.

Every probe goes through an injected fake HTTP session (duck-typed: ``.head``/``.get`` returning an
object with ``.status_code``), so the suite never touches the network. Covers:

* :func:`probe_origin` — open repo/URL origins resolve to alive True/False by HTTP status; non-probeable
  origins (script/manual/token-gated/no-URL) report ``alive=None``; a HEAD refused (403/405/501) retries
  with a streamed GET.
* :func:`check_dataset` — a PUBLIC dataset whose every open origin is dead is ``degraded``; a private one
  never is.
* :func:`run_health_check` — writes ``catalog/health.json`` with ``n_degraded`` and a per-id entry, and
  honours ``only=[...]``.
"""
from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

import yaml

from nirs4all_datasets.health import check_dataset, probe_origin, run_health_check
from nirs4all_datasets.schema import (
    DatasetDescriptor,
    Governance,
    OriginSource,
    Provenance,
    Source,
    SourceAccess,
    SourceKind,
    Tier,
)

_NOW = datetime(2026, 6, 11, 12, 0, 0, tzinfo=UTC)


class _Resp:
    """Minimal HTTP response stand-in (only ``.status_code`` is consulted)."""

    def __init__(self, status_code: int) -> None:
        self.status_code = status_code


class FakeSession:
    """Duck-typed HTTP session: maps url -> status_code per method, records every call.

    Defaults to 200; a per-url override in ``head_map``/``get_map`` wins. A url present in ``raise_on``
    raises from the matching method (to exercise the transport-error path).
    """

    def __init__(
        self,
        *,
        default: int = 200,
        head_map: dict[str, int] | None = None,
        get_map: dict[str, int] | None = None,
        raise_on: set[str] | None = None,
    ) -> None:
        self.default = default
        self.head_map = head_map or {}
        self.get_map = get_map or {}
        self.raise_on = raise_on or set()
        self.head_calls: list[str] = []
        self.get_calls: list[str] = []

    def head(self, url: str, *, timeout: float, allow_redirects: bool):  # noqa: ANN201
        self.head_calls.append(url)
        if url in self.raise_on:
            raise ConnectionError("boom")
        return _Resp(self.head_map.get(url, self.default))

    def get(self, url: str, *, timeout: float, allow_redirects: bool, stream: bool):  # noqa: ANN201
        self.get_calls.append(url)
        if url in self.raise_on:
            raise ConnectionError("boom")
        return _Resp(self.get_map.get(url, self.default))


def _origin(kind: SourceKind, locator: str, access: SourceAccess = SourceAccess.OPEN, **kw) -> OriginSource:  # noqa: ANN003
    return OriginSource(kind=kind, locator=locator, access=access, **kw)


def _descriptor(name: str, tier: Tier, origins: list[OriginSource]) -> DatasetDescriptor:
    return DatasetDescriptor(
        id=name,
        name=name.title(),
        description="synthetic",
        sources=[Source(source_id="X")],
        variables=[],
        provenance=Provenance(contributor="Lab"),
        governance=Governance(license="CC-BY-4.0"),
        tier=tier,
        origin_sources=origins,
    )


# =============================================================================
# probe_origin
# =============================================================================
def test_probe_open_zenodo_alive() -> None:
    origin = _origin(SourceKind.ZENODO, "10.5281/zenodo.1")
    result = probe_origin(origin, session=FakeSession(default=200), now=_NOW)
    assert result["alive"] is True
    assert result["http_status"] == 200
    assert result["reason"] is None
    assert result["kind"] == "zenodo"
    assert result["access"] == "open"
    assert result["checked_at"] == _NOW.isoformat()


def test_probe_open_url_dead() -> None:
    origin = _origin(SourceKind.URL, "https://example.org/dataset")
    result = probe_origin(origin, session=FakeSession(default=404), now=_NOW)
    assert result["alive"] is False
    assert result["http_status"] == 404
    assert result["reason"] == "HTTP 404"


def test_probe_bare_doi_resolved_through_doi_org() -> None:
    origin = _origin(SourceKind.DATAVERSE, "10.18167/abc")
    session = FakeSession(default=200)
    probe_origin(origin, session=session, now=_NOW)
    assert session.head_calls == ["https://doi.org/10.18167/abc"]


def test_probe_script_origin_not_probed() -> None:
    origin = _origin(SourceKind.SCRIPT, "scripts/build.py", access=SourceAccess.MANUAL)
    session = FakeSession()
    result = probe_origin(origin, session=session, now=_NOW)
    assert result["alive"] is None
    assert result["http_status"] is None
    assert "not probed" in result["reason"]
    assert session.head_calls == [] and session.get_calls == []  # never touched


def test_probe_manual_origin_not_probed() -> None:
    origin = _origin(SourceKind.URL, "https://esdac.jrc.ec.europa.eu/x", access=SourceAccess.MANUAL)
    result = probe_origin(origin, session=FakeSession(), now=_NOW)
    assert result["alive"] is None


def test_probe_token_origin_not_probed() -> None:
    origin = _origin(SourceKind.DATAVERSE, "10.18167/private", access=SourceAccess.TOKEN)
    result = probe_origin(origin, session=FakeSession(), now=_NOW)
    assert result["alive"] is None
    assert "not probed" in result["reason"]


def test_probe_no_probeable_url() -> None:
    # An OPEN script-style locator (not http, not a DOI) has no URL to hit.
    origin = _origin(SourceKind.URL, "not-a-url-or-doi")
    result = probe_origin(origin, session=FakeSession(), now=_NOW)
    assert result["alive"] is None
    assert result["reason"] == "no probeable URL"


def test_probe_head_refused_retries_get() -> None:
    url = "https://example.org/head-refused"
    origin = _origin(SourceKind.URL, url)
    session = FakeSession(head_map={url: 403}, get_map={url: 200})
    result = probe_origin(origin, session=session, now=_NOW)
    assert result["alive"] is True
    assert result["http_status"] == 200
    assert session.head_calls == [url]  # HEAD attempted once
    assert session.get_calls == [url]  # then a streamed GET


def test_probe_head_refused_then_get_also_dead() -> None:
    url = "https://example.org/gone"
    origin = _origin(SourceKind.URL, url)
    session = FakeSession(head_map={url: 405}, get_map={url: 404})
    result = probe_origin(origin, session=session, now=_NOW)
    assert result["alive"] is False
    assert result["http_status"] == 404


def test_probe_transport_error_is_not_alive() -> None:
    url = "https://example.org/timeout"
    origin = _origin(SourceKind.URL, url)
    result = probe_origin(origin, session=FakeSession(raise_on={url}), now=_NOW)
    assert result["alive"] is False
    assert result["http_status"] is None
    assert "ConnectionError" in result["reason"]


# =============================================================================
# check_dataset
# =============================================================================
def test_check_dataset_public_all_open_dead_is_degraded() -> None:
    descriptor = _descriptor("wheat", Tier.PUBLIC, [_origin(SourceKind.ZENODO, "10.5281/zenodo.9")])
    result = check_dataset(descriptor, session=FakeSession(default=404), now=_NOW)
    assert result["degraded"] is True
    assert result["alive"] is False
    assert len(result["origins"]) == 1


def test_check_dataset_public_alive_not_degraded() -> None:
    descriptor = _descriptor("wheat", Tier.PUBLIC, [_origin(SourceKind.ZENODO, "10.5281/zenodo.9")])
    result = check_dataset(descriptor, session=FakeSession(default=200), now=_NOW)
    assert result["degraded"] is False
    assert result["alive"] is True


def test_check_dataset_private_dead_not_degraded() -> None:
    # A private dataset is token-gated; a dead open origin does not degrade it.
    descriptor = _descriptor("barley", Tier.PRIVATE, [_origin(SourceKind.ZENODO, "10.5281/zenodo.9")])
    result = check_dataset(descriptor, session=FakeSession(default=404), now=_NOW)
    assert result["degraded"] is False


def test_check_dataset_no_probeable_origin_not_degraded() -> None:
    # A public dataset whose only origin is token-gated has nothing to probe -> not degraded, alive None.
    descriptor = _descriptor("rye", Tier.PUBLIC, [_origin(SourceKind.DATAVERSE, "10.18167/p", access=SourceAccess.TOKEN)])
    result = check_dataset(descriptor, session=FakeSession(default=404), now=_NOW)
    assert result["degraded"] is False
    assert result["alive"] is None


# =============================================================================
# run_health_check — writes catalog/health.json
# =============================================================================
def _write_descriptor(root: Path, descriptor: DatasetDescriptor) -> None:
    desc_dir = root / "catalog" / "datasets"
    desc_dir.mkdir(parents=True, exist_ok=True)
    (desc_dir / f"{descriptor.id}.yaml").write_text(
        yaml.safe_dump(descriptor.model_dump(mode="json", exclude_none=True), sort_keys=False), encoding="utf-8"
    )


def test_run_health_check_writes_report(tmp_path: Path) -> None:
    _write_descriptor(tmp_path, _descriptor("wheat", Tier.PUBLIC, [_origin(SourceKind.ZENODO, "10.5281/zenodo.9")]))
    _write_descriptor(tmp_path, _descriptor("barley", Tier.PRIVATE, [_origin(SourceKind.ZENODO, "10.5281/zenodo.8")]))

    report = run_health_check(tmp_path, session=FakeSession(default=404), now=_NOW)

    assert report["checked_at"] == _NOW.isoformat()
    assert report["n_datasets"] == 2
    assert report["n_degraded"] == 1  # only the public dataset degrades on a dead origin
    assert set(report["datasets"]) == {"wheat", "barley"}
    assert report["datasets"]["wheat"]["degraded"] is True
    assert report["datasets"]["barley"]["degraded"] is False

    written = json.loads((tmp_path / "catalog" / "health.json").read_text(encoding="utf-8"))
    assert written["n_degraded"] == 1
    assert written["datasets"]["wheat"]["degraded"] is True


def test_run_health_check_only_limits_probe(tmp_path: Path) -> None:
    _write_descriptor(tmp_path, _descriptor("wheat", Tier.PUBLIC, [_origin(SourceKind.ZENODO, "10.5281/zenodo.9")]))
    _write_descriptor(tmp_path, _descriptor("barley", Tier.PUBLIC, [_origin(SourceKind.ZENODO, "10.5281/zenodo.8")]))

    report = run_health_check(tmp_path, session=FakeSession(default=200), only=["wheat"], now=_NOW)

    assert report["n_datasets"] == 1
    assert set(report["datasets"]) == {"wheat"}
