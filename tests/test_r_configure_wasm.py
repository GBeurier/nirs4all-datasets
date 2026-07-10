"""R binding configure guards for the R-universe WebAssembly tool wrappers."""
from __future__ import annotations

import os
import shutil
import stat
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIGURE = ROOT / "bindings" / "r" / "nirs4alldatasets" / "configure"
MAKEVARS = ROOT / "bindings" / "r" / "nirs4alldatasets" / "src" / "Makevars"


def _minimal_r_package(tmp_path: Path) -> Path:
    pkg = tmp_path / "nirs4alldatasets"
    pkg.mkdir()
    shutil.copy2(CONFIGURE, pkg / "configure")
    rust = pkg / "src" / "rust"
    (rust / "vendored" / "nirs4all-datasets-capi").mkdir(parents=True)
    (rust / "vendored" / "nirs4all-datasets-capi" / "Cargo.toml").write_text("[package]\nname = \"nirs4all-datasets-capi\"\n", encoding="utf-8")
    (rust / "vendor.tar.xz").write_bytes(b"placeholder")
    (pkg / "src" / "nirs4all_datasets.h").write_text("/* placeholder */\n", encoding="utf-8")
    (pkg / "inst").mkdir()
    (pkg / "inst" / "COPYRIGHTS").write_text("placeholder\n", encoding="utf-8")
    return pkg


def _rwasm_toolchain(tmp_path: Path) -> Path:
    bindir = tmp_path / "opt" / "R" / "library" / "rwasm" / "bin"
    bindir.mkdir(parents=True)
    script = "#!/bin/sh\nif [ \"${1:-}\" = \"--version\" ]; then exit 42; fi\nexit 0\n"
    for name in ("cargo", "rustc"):
        tool = bindir / name
        tool.write_text(script, encoding="utf-8")
        tool.chmod(tool.stat().st_mode | stat.S_IXUSR)
    return bindir


def _env(tmp_path: Path, bindir: Path) -> dict[str, str]:
    env = os.environ.copy()
    env["PATH"] = f"{bindir}:/usr/bin:/bin"
    env["HOME"] = str(tmp_path / "home")
    return env


def test_configure_accepts_rwasm_wrappers_without_version_in_wasm_mode(tmp_path: Path) -> None:
    pkg = _minimal_r_package(tmp_path)
    bindir = _rwasm_toolchain(tmp_path)

    result = subprocess.run(
        ["./configure", "--host=wasm32-unknown-emscripten"],
        cwd=pkg,
        env=_env(tmp_path, bindir),
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "accepting R-universe/rwasm cargo wrapper" in result.stderr
    assert "accepting R-universe/rwasm rustc wrapper" in result.stderr
    toolchain = (pkg / "src" / "n4ds-rust-toolchain.mk").read_text(encoding="utf-8")
    assert "N4DS_R_WASM = 1" in toolchain
    assert f"N4DS_CARGO = {bindir / 'cargo'}" in toolchain


def test_configure_rejects_unversioned_wrappers_in_native_mode(tmp_path: Path) -> None:
    pkg = _minimal_r_package(tmp_path)
    bindir = _rwasm_toolchain(tmp_path)

    result = subprocess.run(
        ["./configure"],
        cwd=pkg,
        env=_env(tmp_path, bindir),
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode != 0
    assert "Cargo >= 1.85.0 was not found" in result.stderr
    assert "accepting R-universe/rwasm" not in result.stderr


def test_makevars_reuses_configured_rwasm_wrappers_without_version(tmp_path: Path) -> None:
    src = tmp_path / "src"
    src.mkdir()
    shutil.copy2(MAKEVARS, src / "Makevars")
    (src / "rust").mkdir()
    bindir = _rwasm_toolchain(tmp_path)
    (src / "n4ds-rust-toolchain.mk").write_text(
        "\n".join(
            [
                f"N4DS_CARGO = {bindir / 'cargo'}",
                f"N4DS_RUSTC = {bindir / 'rustc'}",
                "N4DS_R_WASM = 1",
                "",
            ]
        ),
        encoding="utf-8",
    )

    statlib = tmp_path / "tmp" / "n4ds-r-target" / "release" / "libnirs4all_datasets_capi.a"
    result = subprocess.run(
        ["make", "-f", "Makevars", str(statlib)],
        cwd=src,
        env=_env(tmp_path, bindir) | {"TMPDIR": str(tmp_path / "tmp")},
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "accepting R-universe/rwasm cargo wrapper" in result.stderr
    assert "accepting R-universe/rwasm rustc wrapper" in result.stderr
    assert "cargo rwasm-wrapper" in result.stderr
    assert "rustc rwasm-wrapper" in result.stderr
