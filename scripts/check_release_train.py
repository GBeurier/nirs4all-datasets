#!/usr/bin/env python3
"""Fail closed when Datasets manifests, locks, or upstream releases drift.

The normal check is offline and verifies that every tracked consumer surface is
consistent with the root Cargo manifest.  ``--release`` additionally enforces
the exact V1 train declared in ``release/train-v1.toml``.  ``--check-registry``
proves that each required upstream crate/version is actually on crates.io; it is
intended for publishing jobs, not ordinary development CI.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import tomllib
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

_REQ_RE = re.compile(r"^(?P<name>[A-Za-z0-9_.-]+)>=(?P<version>[0-9A-Za-z.+-]+)$")


@dataclass
class CheckResult:
    """Collected release-train diagnostics."""

    checked: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    def expect(self, label: str, actual: object, expected: object) -> None:
        """Record one exact-value assertion without aborting the whole audit."""
        self.checked.append(f"{label} = {actual!s}")
        if actual != expected:
            self.errors.append(f"{label}: found {actual!r}, expected {expected!r}")


def _toml(path: Path) -> dict[str, Any]:
    with path.open("rb") as handle:
        return tomllib.load(handle)


def _dependency_version(value: object, *, label: str) -> str:
    if not isinstance(value, dict) or not isinstance(value.get("version"), str):
        raise ValueError(f"{label} must be a dependency table with an explicit version")
    return value["version"]


def _package_version(lock: dict[str, Any], name: str, *, label: str) -> str:
    versions = {entry.get("version") for entry in lock.get("package", []) if entry.get("name") == name}
    versions.discard(None)
    if len(versions) != 1:
        rendered = ", ".join(sorted(str(version) for version in versions)) or "missing"
        raise ValueError(f"{label}: expected exactly one {name!r} package, found {rendered}")
    return str(versions.pop())


def _python_extra_versions(pyproject: dict[str, Any]) -> dict[str, str]:
    values = pyproject.get("project", {}).get("optional-dependencies", {}).get("io", [])
    parsed: dict[str, str] = {}
    for value in values:
        if not isinstance(value, str):
            continue
        match = _REQ_RE.fullmatch(value)
        if match:
            parsed[match.group("name").lower().replace("_", "-")] = match.group("version")
    return parsed


def check_tree(root: Path, *, enforce_contract: bool) -> tuple[CheckResult, dict[str, Any], dict[str, str]]:
    """Check tracked manifests and lockfiles, optionally against the V1 contract."""
    result = CheckResult()
    cargo = _toml(root / "Cargo.toml")
    pyproject = _toml(root / "pyproject.toml")
    contract = _toml(root / "release" / "train-v1.toml")

    workspace_version = str(cargo["workspace"]["package"]["version"])
    dependencies = cargo["workspace"]["dependencies"]
    upstream = {
        "nirs4all-formats": _dependency_version(dependencies["nirs4all-formats"], label="Cargo.toml nirs4all-formats"),
        "nirs4all-io": _dependency_version(dependencies["nirs4all-io"], label="Cargo.toml nirs4all-io"),
    }

    result.expect("pyproject.toml project.version", pyproject["project"]["version"], workspace_version)
    result.expect(
        "Cargo.toml nirs4all-datasets-core dependency",
        _dependency_version(dependencies["nirs4all-datasets-core"], label="Cargo.toml nirs4all-datasets-core"),
        workspace_version,
    )

    extra_versions = _python_extra_versions(pyproject)
    for name, version in upstream.items():
        result.expect(f"pyproject.toml io extra {name}", extra_versions.get(name), version)

    lock_specs = {
        "Cargo.lock": {
            "nirs4all-datasets-core": workspace_version,
            "nirs4all-formats": upstream["nirs4all-formats"],
            "nirs4all-formats-core": upstream["nirs4all-formats"],
            "nirs4all-io": upstream["nirs4all-io"],
            "nirs4all-io-core": upstream["nirs4all-io"],
        },
        "bindings/python/Cargo.lock": {
            "nirs4all-datasets-core": workspace_version,
            "nirs4all-datasets-py": workspace_version,
            "nirs4all-formats": upstream["nirs4all-formats"],
            "nirs4all-formats-core": upstream["nirs4all-formats"],
            "nirs4all-io": upstream["nirs4all-io"],
            "nirs4all-io-core": upstream["nirs4all-io"],
        },
        "bindings/wasm/Cargo.lock": {
            "nirs4all-datasets-core": workspace_version,
            "nirs4all-datasets-wasm": workspace_version,
        },
    }
    for relative, packages in lock_specs.items():
        lock = _toml(root / relative)
        for name, expected in packages.items():
            try:
                actual = _package_version(lock, name, label=relative)
            except ValueError as exc:
                result.errors.append(str(exc))
                continue
            result.expect(f"{relative} {name}", actual, expected)

    r_manifest = _toml(root / "bindings/r/nirs4alldatasets/src/rust/Cargo.toml")
    r_dependencies = r_manifest["workspace"]["dependencies"]
    result.expect("R vendored workspace version", r_manifest["workspace"]["package"]["version"], workspace_version)
    result.expect(
        "R vendored nirs4all-datasets-core",
        _dependency_version(r_dependencies["nirs4all-datasets-core"], label="R nirs4all-datasets-core"),
        workspace_version,
    )
    for name, version in upstream.items():
        result.expect(f"R vendored {name}", _dependency_version(r_dependencies[name], label=f"R {name}"), version)
        result.expect(f"R vendored {name}-core", _dependency_version(r_dependencies[f"{name}-core"], label=f"R {name}-core"), version)

    if enforce_contract:
        result.expect("release/train-v1.toml schema_version", contract.get("schema_version"), 1)
        result.expect("Cargo workspace release version", workspace_version, contract.get("release_version"))
        contract_dependencies = contract.get("dependencies", {})
        for name, version in upstream.items():
            result.expect(f"V1 train dependency {name}", version, contract_dependencies.get(name))

        tag = os.environ.get("GITHUB_REF_NAME", "")
        if tag.startswith("v"):
            result.expect("release tag", tag[1:], workspace_version)

    return result, contract, upstream


def check_crates_io(result: CheckResult, contract: dict[str, Any]) -> None:
    """Require an exact crates.io release for each contract registry package."""
    names = contract.get("registries", {}).get("crates_io", [])
    if not isinstance(names, list):
        result.errors.append("release/train-v1.toml registries.crates_io must be a list")
        return
    versions = {**contract.get("dependencies", {}), **contract.get("prerequisites", {})}
    for name in names:
        version = versions.get(name)
        if not isinstance(version, str):
            result.errors.append(f"release/train-v1.toml registry package {name!r} has no target version")
            continue
        encoded_name = urllib.parse.quote(name, safe="")
        encoded_version = urllib.parse.quote(version, safe="")
        url = f"https://crates.io/api/v1/crates/{encoded_name}/{encoded_version}"
        request = urllib.request.Request(url, headers={"User-Agent": "nirs4all-datasets-release-train/1"})
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                if response.status != 200:
                    raise OSError(f"HTTP {response.status}")
        except (OSError, urllib.error.URLError) as exc:
            result.errors.append(f"crates.io {name}@{version}: unavailable ({exc})")
        else:
            result.checked.append(f"crates.io {name}@{version} = published")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--release", action="store_true", help="enforce the exact release/train-v1.toml target")
    parser.add_argument("--check-registry", action="store_true", help="require exact upstream crates on crates.io")
    args = parser.parse_args(argv)

    try:
        result, contract, _ = check_tree(args.root.resolve(), enforce_contract=args.release)
        if args.check_registry:
            if not args.release:
                result.errors.append("--check-registry requires --release")
            else:
                check_crates_io(result, contract)
    except (KeyError, OSError, tomllib.TOMLDecodeError, TypeError, ValueError) as exc:
        print(f"FAIL: cannot inspect release train: {exc}", file=sys.stderr)
        return 2

    for line in result.checked:
        print(f"OK: {line}")
    if result.errors:
        print(f"HOLD: {len(result.errors)} release-train blocker(s):", file=sys.stderr)
        for error in result.errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    print("GO: release train is internally consistent" + (" and publishable" if args.release else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
