"""Tests for the CLI commands that do not need nirs4all (catalog/list/card)."""
from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from nirs4all_datasets.cli import app

runner = CliRunner()


def test_catalog_list_card(registry: Path) -> None:
    result = runner.invoke(app, ["catalog", "--root", str(registry)])
    assert result.exit_code == 0
    assert "1 dataset" in result.output

    result = runner.invoke(app, ["list", "--root", str(registry)])
    assert result.exit_code == 0
    assert "corn" in result.output

    result = runner.invoke(app, ["list", "--root", str(registry), "--task", "classification"])
    assert result.exit_code == 0
    assert "(no datasets)" in result.output

    result = runner.invoke(app, ["card", "corn", "--root", str(registry)])
    assert result.exit_code == 0
    assert "inventory" in result.output


def test_card_missing_exits_nonzero(registry: Path) -> None:
    result = runner.invoke(app, ["card", "ghost", "--root", str(registry)])
    assert result.exit_code == 1


def test_help_works_without_heavy_deps() -> None:
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "qualify" in result.output and "publish" in result.output
