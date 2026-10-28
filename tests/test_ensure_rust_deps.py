"""The sibling checkout helper keeps CI on the declared release train."""
from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    ("ci", "ref", "expected_refs"),
    [
        (True, "main", ["v0.2.11", "v0.2.6"]),
        (True, "v0.3.12", ["v0.2.11", "v0.2.6"]),
        (True, "rc/test", ["rc/test", "rc/test"]),
        (False, "main", []),
        (False, "v0.3.12", []),
    ],
)
def test_sibling_checkout_selection(tmp_path: Path, ci: bool, ref: str, expected_refs: list[str]) -> None:
    checkout = tmp_path / "nirs4all-datasets"
    (checkout / "scripts").mkdir(parents=True)
    shutil.copy(ROOT / "scripts/ensure_rust_deps.sh", checkout / "scripts/ensure_rust_deps.sh")
    (checkout / "Cargo.toml").write_text(
        '[workspace.dependencies]\nnirs4all-formats = { version = "0.2.11" }\nnirs4all-io = { version = "0.2.6" }\n', encoding="utf-8"
    )
    for name, version in (("nirs4all-formats", "0.2.11"), ("nirs4all-io", "0.2.6")):
        repo = tmp_path / name
        (repo / ".git").mkdir(parents=True)
        (repo / "Cargo.toml").write_text(f'[workspace.package]\nversion = "{version}"\n', encoding="utf-8")
    bindir = tmp_path / "bin"
    bindir.mkdir()
    fake_git = bindir / "git"
    fake_git.write_text('#!/usr/bin/env bash\nprintf "%s\\n" "$*" >> "$N4DS_TEST_GIT_LOG"\n', encoding="utf-8")
    fake_git.chmod(0o755)
    log = tmp_path / "git.log"
    env = {k: v for k, v in os.environ.items() if k not in {"NIRS4ALL_SIBLING_REF", "GITHUB_HEAD_REF", "GITHUB_REF_NAME", "CI"}}
    env.update({"PATH": f"{bindir}:{env['PATH']}", "GITHUB_REF_NAME": ref, "N4DS_TEST_GIT_LOG": str(log)})
    if ci:
        env["CI"] = "true"
    subprocess.run(["bash", str(checkout / "scripts/ensure_rust_deps.sh")], env=env, check=True, capture_output=True, text=True)
    calls = log.read_text(encoding="utf-8").splitlines() if log.exists() else []
    fetches = [line.rsplit(" ", 1)[-1] for line in calls if " fetch " in line]
    assert fetches == expected_refs
