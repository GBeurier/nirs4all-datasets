"""Execute R recipes through a pinned rwasm wrapper and inspect the linked path."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tarfile
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[3]
MAKEVARS = REPO / "bindings/r/nirs4alldatasets/src/Makevars"
FIXTURE = Path(__file__).parent / "fixtures/rwasm"
TRIPLE = "wasm32-unknown-emscripten"
LIBRARY = "libnirs4all_datasets_capi.a"

HOST_CARGO = r"""#!__PYTHON__
import json, os, sys
from pathlib import Path
if '--version' in sys.argv:
    print('cargo 1.88.0')
    raise SystemExit(0)
if os.environ.get('FAIL_CARGO'):
    raise SystemExit(17)
target = next((x.split('=', 1)[1] for x in sys.argv if x.startswith('--target=')), os.environ.get('CARGO_BUILD_TARGET'))
root = Path(os.environ['CARGO_TARGET_DIR'])
artifact = root / target / 'release' if target else root / 'release'
artifact.mkdir(parents=True, exist_ok=True)
(artifact / 'libnirs4all_datasets_capi.a').write_bytes(b'recording Cargo artifact; not compiled code')
Path(os.environ['CARGO_RECORD']).write_text(json.dumps({'args': sys.argv[1:], 'target': target, 'artifact': str(artifact), 'cargo_home': os.environ['CARGO_HOME']}))
"""


def prepare(tmp_path: Path, *, wasm: bool, fail: bool = False, makevars: Path = MAKEVARS):
    source = tmp_path / "src"
    (source / "rust").mkdir(parents=True)
    tools = tmp_path / "tools"
    tools.mkdir()
    cargo = tools / "cargo"
    cargo.write_text(HOST_CARGO.replace("__PYTHON__", sys.executable))
    cargo.chmod(0o755)
    rustc = tools / "rustc"
    rustc.write_text("#!/bin/sh\necho 'rustc 1.88.0'\n")
    rustc.chmod(0o755)
    rustup = tools / "rustup"
    rustup.write_text("#!/bin/sh\necho 'recording rustup; no toolchain install'\n")
    rustup.chmod(0o755)
    vendor = tmp_path / "vendor"
    vendor.mkdir()
    (vendor / "marker").write_text("offline fixture")
    with tarfile.open(source / "rust/vendor.tar.xz", "w:xz") as archive:
        archive.add(vendor, arcname="vendor")
    shim = tmp_path / "rwasm/bin/cargo"
    shim.parent.mkdir(parents=True)
    shutil.copyfile(FIXTURE / "cargo", shim)
    shim.chmod(0o755)
    makefile = source / "witness.mk"
    makefile.write_text(f"SHLIB = package.so\ninclude {makevars}\n.PHONY: witness\nwitness: $(STATLIB)\n\t@test -f \"$(STATLIB)\"\n\t@printf '%s\\n' \"$(STATLIB)\"\n")
    env = os.environ.copy()
    for key in ["CARGO_BUILD_TARGET", "CARGO_TARGET_DIR", "EM_HOST_CARGO", "MAKEFLAGS"]:
        env.pop(key, None)
    env.update(PATH=str(tools) + os.pathsep + env["PATH"], CARGO_RECORD=str(tmp_path / "cargo.json"), EM_HOST_CARGO=str(cargo))
    if fail:
        env["FAIL_CARGO"] = "1"
    command = [
        "make", "--no-print-directory", "-f", str(makefile), "witness",
        f"N4DS_R_WASM={int(wasm)}", f"N4DS_CARGO={shim if wasm else cargo}",
        f"N4DS_RUSTC={rustc}", f"TARGET_DIR={tmp_path / 'private/target'}",
        f"CARGOTMP={tmp_path / 'private/cargo-home'}", f"VENDOR_ROOT={tmp_path / 'private/vendor-root'}",
    ]
    return source, env, command


@pytest.mark.parametrize("wasm", [False, True])
def test_library_path_matches_the_actual_cargo_target(tmp_path: Path, wasm: bool):
    source, env, command = prepare(tmp_path, wasm=wasm)
    result = subprocess.run(command, cwd=source, env=env, capture_output=True, text=True, check=False)
    assert result.returncode == 0, result.stdout + result.stderr
    record = json.loads((tmp_path / "cargo.json").read_text())
    assert "--offline" in record["args"]
    assert record["cargo_home"] == str(tmp_path / "private/cargo-home")
    expected = tmp_path / "private/target"
    if wasm:
        assert f"--target={TRIPLE}" in record["args"]
        assert record["target"] == TRIPLE
        expected /= TRIPLE
        assert "Copying wasm32" not in result.stdout
    else:
        assert not any(x.startswith("--target") for x in record["args"])
        assert record["target"] is None
    artifact = expected / "release" / LIBRARY
    assert artifact.is_file()
    assert result.stdout.rstrip().endswith(str(artifact))
    assert not (source / "rust/target").exists()


def test_wrapper_fixture_is_the_pinned_upstream_file():
    provenance = json.loads((FIXTURE / "PROVENANCE.json").read_text())
    assert hashlib.sha256((FIXTURE / "cargo").read_bytes()).hexdigest() == provenance["file_sha256"]


def test_failed_cargo_cannot_produce_a_successful_r_library(tmp_path: Path):
    source, env, command = prepare(tmp_path, wasm=True, fail=True)
    result = subprocess.run(command, cwd=source, env=env, capture_output=True, text=True, check=False)
    assert result.returncode != 0
    assert not (tmp_path / "cargo.json").exists()
