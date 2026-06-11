"""End-to-end tests for the ``n4a-datasets`` CLI (schema 2.0).

Drives the real command flow over a synthetic v2.0 source tree built with the ``v2_leaf`` factory:
``bootstrap`` -> ``build-all`` -> ``catalog`` / ``list`` / ``card`` / ``get`` / ``qualify`` /
``health-check``. No real network: ``health-check`` runs against a fake injected HTTP session.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from typer.testing import CliRunner

import nirs4all_datasets.health as health
from nirs4all_datasets.cli import app

runner = CliRunner()


def _source_tree(tmp_path: Path, v2_leaf: Any) -> Path:
    """Build a two-leaf v2.0 source tree under ``<tmp>/source`` (one private, one public)."""
    source = tmp_path / "source"
    v2_leaf(source / "v2.0" / "ds_a", sample_of={"o1": "s1", "o2": "s2"})
    v2_leaf(source / "v2.0" / "ds_pub", public=True, sample_of={"o1": "s1", "o2": "s2"})
    return source


class _FakeResponse:
    status_code = 200


class _FakeSession:
    """Duck-typed ``HttpSession`` returning a live (200) status — keeps health-check off the network."""

    def head(self, url: str, *, timeout: float, allow_redirects: bool) -> _FakeResponse:
        return _FakeResponse()

    def get(self, url: str, *, timeout: float, allow_redirects: bool, stream: bool) -> _FakeResponse:
        return _FakeResponse()


def test_full_cli_flow(tmp_path: Path, v2_leaf: Any, monkeypatch: Any) -> None:
    """bootstrap -> build-all -> catalog -> list -> card -> get -> qualify -> health-check, all green."""
    source = _source_tree(tmp_path, v2_leaf)
    reg = tmp_path / "reg"

    # bootstrap: one schema-2.0 descriptor per v2.0 leaf + the assembled index.
    result = runner.invoke(app, ["bootstrap", str(source), "--root", str(reg)])
    assert result.exit_code == 0, result.output
    assert "created=2" in result.output
    assert (reg / "catalog" / "datasets" / "ds_a.yaml").exists()
    assert (reg / "catalog" / "datasets" / "ds_pub.yaml").exists()
    assert (reg / "catalog" / "datasets.yaml").exists()

    # build-all: parallel organize + qualify (no site), failure-isolated bulk report + cards.
    result = runner.invoke(app, ["build-all", "--source-tree", str(source), "--root", str(reg)])
    assert result.exit_code == 0, result.output
    assert "build-all:" in result.output
    assert (reg / "bulk_report.json").exists()
    assert (reg / "datasets" / "ds_a" / "card.json").exists()
    assert (reg / "datasets" / "ds_pub" / "card.json").exists()

    # catalog: re-assemble the index from descriptors + cards.
    result = runner.invoke(app, ["catalog", "--root", str(reg)])
    assert result.exit_code == 0, result.output
    assert "2 dataset(s)" in result.output

    # list: both datasets; filtered by tier shows only the public one.
    result = runner.invoke(app, ["list", "--root", str(reg)])
    assert result.exit_code == 0, result.output
    assert "ds_a" in result.output and "ds_pub" in result.output

    result = runner.invoke(app, ["list", "--root", str(reg), "--tier", "public"])
    assert result.exit_code == 0, result.output
    assert "ds_pub" in result.output and "ds_a" not in result.output

    # card: prints the generated identity card JSON.
    result = runner.invoke(app, ["card", "ds_a", "--root", str(reg)])
    assert result.exit_code == 0, result.output
    assert "identity" in result.output and "ds_a" in result.output

    # get: local-first resolution prints a one-line summary.
    result = runner.invoke(app, ["get", "ds_a", "--root", str(reg)])
    assert result.exit_code == 0, result.output
    assert "loaded ds_a: 1 source(s)" in result.output

    # qualify --anonymize: rebuild the card and emit the anonymized variant.
    result = runner.invoke(app, ["qualify", "ds_a", "--root", str(reg), "--anonymize"])
    assert result.exit_code == 0, result.output
    assert "card: datasets/ds_a/card.json" in result.output
    assert (reg / "datasets" / "ds_a" / "card.anon.json").exists()

    # health-check: no network — feed run_health_check a fake session via _default_session.
    monkeypatch.setattr(health, "_default_session", lambda: _FakeSession())
    result = runner.invoke(app, ["health-check", "--root", str(reg)])
    assert result.exit_code == 0, result.output
    assert "health-check:" in result.output
    assert (reg / "catalog" / "health.json").exists()


def test_get_unknown_id_exits_nonzero(tmp_path: Path, v2_leaf: Any) -> None:
    """get on an id with no descriptor and no local data fails (CliRunner surfaces the exception)."""
    source = _source_tree(tmp_path, v2_leaf)
    reg = tmp_path / "reg"
    assert runner.invoke(app, ["bootstrap", str(source), "--root", str(reg)]).exit_code == 0

    result = runner.invoke(app, ["get", "ghost", "--root", str(reg)])
    assert result.exit_code != 0


def test_bootstrap_without_v2_tree_creates_nothing(tmp_path: Path, v2_leaf: Any) -> None:
    """A source tree with no ``v2.0/`` directory yields ``created=0`` (still exits 0)."""
    bad_source = tmp_path / "bad_source"
    v2_leaf(bad_source / "not_v2" / "ds_x", sample_of={"o1": "s1", "o2": "s2"})
    reg = tmp_path / "reg"

    result = runner.invoke(app, ["bootstrap", str(bad_source), "--root", str(reg)])
    assert result.exit_code == 0, result.output
    assert "created=0" in result.output


def test_help_lists_commands() -> None:
    """``--help`` works with no heavy deps and advertises the key commands."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "qualify" in result.output and "publish" in result.output and "health-check" in result.output
