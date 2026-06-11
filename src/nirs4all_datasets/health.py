"""Origin liveness probe -> ``catalog/health.json``.

Probes each dataset's open ``origin_sources`` (where we point users to fetch the bytes) and records
whether they still resolve. Script/manual/token-gated origins are not probed (``alive = None``). A
**public** dataset whose every open origin has died is flagged ``degraded`` — the catalog/site surface
it and the maintainer can fall back to a personal Dataverse copy. The HTTP session is injectable so the
probe is unit-testable with no network (the live probe is opt-in via the CLI).
"""
from __future__ import annotations

import json
import re
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Protocol, cast

import yaml

from nirs4all_datasets.schema import DatasetDescriptor, OriginSource, SourceAccess, SourceKind, Tier

_PROBE_KINDS = frozenset({SourceKind.DATAVERSE, SourceKind.ZENODO, SourceKind.FIGSHARE, SourceKind.URL})
_BARE_DOI = re.compile(r"^10\.\d{4,9}/\S+$")


class HttpSession(Protocol):
    """The minimal HTTP surface :func:`probe_origin` needs (satisfied by ``requests.Session``)."""

    def head(self, url: str, *, timeout: float, allow_redirects: bool) -> Any: ...
    def get(self, url: str, *, timeout: float, allow_redirects: bool, stream: bool) -> Any: ...


def _default_session() -> HttpSession:
    import requests

    return cast(HttpSession, requests.Session())


def _locator_url(origin: OriginSource) -> str | None:
    """The probeable URL for an origin: its http(s) locator, or a bare DOI resolved through doi.org."""
    loc = origin.locator.strip()
    if loc.startswith("http"):
        return loc
    if _BARE_DOI.match(loc):
        return f"https://doi.org/{loc}"
    return None


def probe_origin(origin: OriginSource, *, session: HttpSession, timeout: float = 10.0, now: datetime | None = None) -> dict[str, Any]:
    """Probe one origin's liveness. ``alive`` is ``None`` when the origin is not probeable (script /
    manual / token-gated / no URL), ``True``/``False`` from the HTTP status otherwise."""
    checked_at = (now or datetime.now(UTC)).isoformat()
    base = {"locator": origin.locator, "kind": origin.kind.value, "access": origin.access.value, "checked_at": checked_at}
    if origin.kind not in _PROBE_KINDS or origin.access is not SourceAccess.OPEN:
        return {**base, "alive": None, "http_status": None, "reason": "not probed (script/manual/token-gated origin)"}
    url = _locator_url(origin)
    if url is None:
        return {**base, "alive": None, "http_status": None, "reason": "no probeable URL"}
    try:
        resp = session.head(url, timeout=timeout, allow_redirects=True)
        status = int(resp.status_code)
        if status in (403, 405, 501):  # HEAD refused -> retry with a streamed GET
            resp = session.get(url, timeout=timeout, allow_redirects=True, stream=True)
            status = int(resp.status_code)
        alive = 200 <= status < 400
        return {**base, "alive": alive, "http_status": status, "reason": None if alive else f"HTTP {status}"}
    except Exception as exc:  # noqa: BLE001 - any network/transport error means "not reachable now"
        return {**base, "alive": False, "http_status": None, "reason": f"{type(exc).__name__}: {exc}"}


def check_dataset(descriptor: DatasetDescriptor, *, session: HttpSession, timeout: float = 10.0, now: datetime | None = None) -> dict[str, Any]:
    """Probe all of a dataset's origins; flag ``degraded`` when a PUBLIC dataset's open origins are all dead."""
    origins = [probe_origin(o, session=session, timeout=timeout, now=now) for o in descriptor.origin_sources]
    probed = [o for o in origins if o["alive"] is not None]
    all_open_dead = bool(probed) and all(not o["alive"] for o in probed)
    any_alive: bool | None = any(o["alive"] for o in probed) if probed else None
    return {"origins": origins, "alive": any_alive, "degraded": descriptor.tier is Tier.PUBLIC and all_open_dead}


def run_health_check(root: str | Path, *, session: HttpSession | None = None, timeout: float = 10.0, only: list[str] | None = None, now: datetime | None = None) -> dict[str, Any]:
    """Probe every (or ``only``) descriptor's origins and write ``catalog/health.json``.

    Returns ``{checked_at, n_datasets, n_degraded, datasets: {id: check_dataset(...)}}``.
    """
    root = Path(root)
    session = session or _default_session()
    checked_at = (now or datetime.now(UTC)).isoformat()
    paths = sorted((root / "catalog" / "datasets").glob("*.yaml"))
    if only is not None:
        wanted = set(only)
        paths = [p for p in paths if p.stem in wanted]
    datasets: dict[str, Any] = {}
    for path in paths:
        descriptor = DatasetDescriptor(**(yaml.safe_load(path.read_text(encoding="utf-8")) or {}))
        datasets[descriptor.id] = check_dataset(descriptor, session=session, timeout=timeout, now=now)
    report = {
        "checked_at": checked_at,
        "n_datasets": len(datasets),
        "n_degraded": sum(1 for d in datasets.values() if d["degraded"]),
        "datasets": datasets,
    }
    (root / "catalog").mkdir(parents=True, exist_ok=True)
    (root / "catalog" / "health.json").write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    return report
