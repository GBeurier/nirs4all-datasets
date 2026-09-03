"""Release-train manifest and lockfile guard."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from scripts import check_release_train as release_train

ROOT = Path(__file__).resolve().parents[1]


def test_tracked_dependency_surfaces_are_consistent() -> None:
    result, _, upstream = release_train.check_tree(ROOT, enforce_contract=False)
    assert result.errors == []
    assert upstream == {"nirs4all-formats": "0.2.8", "nirs4all-io": "0.1.12"}
    assert "pyproject.toml project.license = CECILL-2.1 OR AGPL-3.0-or-later" in result.checked
    assert "pyproject.toml commercial license packaging = True" in result.checked


def test_python_extra_parser_requires_explicit_minimums() -> None:
    pyproject = {"project": {"optional-dependencies": {"io": ["nirs4all-io>=0.1.12", "nirs4all-formats>=0.2.8", "other~=1.0"]}}}
    assert release_train._python_extra_versions(pyproject) == {"nirs4all-io": "0.1.12", "nirs4all-formats": "0.2.8"}


def test_result_reports_drift_without_short_circuiting() -> None:
    result = release_train.CheckResult()
    result.expect("first", "0.1.11", "0.1.12")
    result.expect("second", "0.2.8", "0.2.8")
    assert result.errors == ["first: found '0.1.11', expected '0.1.12'"]
    assert len(result.checked) == 2


def test_v1_contract_declares_final_dependency_train() -> None:
    result, contract, _ = release_train.check_tree(ROOT, enforce_contract=False)
    assert "release/train-v1.toml release_version = 0.3.9" in result.checked
    assert contract["release_version"] == "0.3.9"
    assert contract["dependencies"] == {"nirs4all-formats": "0.2.8", "nirs4all-io": "0.1.12"}
    assert contract["prerequisites"] == {"dag-ml-data": "0.2.10"}


def test_registry_probe_uses_target_contract_versions(monkeypatch: Any) -> None:
    seen: list[str] = []

    class Response:
        status = 200

        def __enter__(self) -> Response:
            return self

        def __exit__(self, *_args: object) -> None:
            return None

    def urlopen(request: Any, *, timeout: int) -> Response:
        seen.append(request.full_url)
        assert timeout == 20
        return Response()

    monkeypatch.setattr(release_train.urllib.request, "urlopen", urlopen)
    result = release_train.CheckResult()
    contract = {
        "dependencies": {"nirs4all-io": "0.1.12"},
        "prerequisites": {"dag-ml-data": "0.2.10"},
        "registries": {"crates_io": ["dag-ml-data", "nirs4all-io"]},
    }
    release_train.check_crates_io(result, contract)
    assert result.errors == []
    assert seen == [
        "https://crates.io/api/v1/crates/dag-ml-data/0.2.10",
        "https://crates.io/api/v1/crates/nirs4all-io/0.1.12",
    ]
