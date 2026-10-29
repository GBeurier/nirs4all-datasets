"""Release-train manifest and lockfile guard."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from scripts import check_release_train as release_train

ROOT = Path(__file__).resolve().parents[1]


def test_tracked_dependency_surfaces_are_consistent() -> None:
    result, _, upstream = release_train.check_tree(ROOT, enforce_contract=False)
    assert result.errors == []
    assert upstream == {"nirs4all-formats": "0.2.13", "nirs4all-io": "0.2.11"}
    assert "pyproject.toml project.license = CECILL-2.1 OR AGPL-3.0-or-later" in result.checked
    assert "pyproject.toml commercial license packaging = True" in result.checked



def test_r_vendor_default_zip_features_are_rejected(monkeypatch: Any) -> None:
    original = release_train._toml

    def changed_manifest(path: Path) -> dict[str, Any]:
        value = original(path)
        if path == ROOT / "bindings/r/nirs4alldatasets/src/rust/Cargo.toml":
            value["workspace"]["dependencies"]["zip"] = "2"
        return value

    monkeypatch.setattr(release_train, "_toml", changed_manifest)
    result, _, _ = release_train.check_tree(ROOT, enforce_contract=False)
    assert len(result.errors) == 1
    assert result.errors[0].startswith("R vendored zip dependency/features:")


def test_python_extra_parser_requires_explicit_minimums() -> None:
    pyproject = {"project": {"optional-dependencies": {"io": ["nirs4all-io>=0.1.12", "nirs4all-formats>=0.2.9", "other~=1.0"]}}}
    assert release_train._python_extra_versions(pyproject) == {"nirs4all-io": "0.1.12", "nirs4all-formats": "0.2.9"}


def test_result_reports_drift_without_short_circuiting() -> None:
    result = release_train.CheckResult()
    result.expect("first", "0.1.11", "0.1.12")
    result.expect("second", "0.2.8", "0.2.8")
    assert result.errors == ["first: found '0.1.11', expected '0.1.12'"]
    assert len(result.checked) == 2


def test_v1_contract_declares_final_dependency_train() -> None:
    result, contract, _ = release_train.check_tree(ROOT, enforce_contract=False)
    workspace_version = release_train._toml(ROOT / "Cargo.toml")["workspace"]["package"]["version"]
    assert result.errors == []
    assert f"release/train-v1.toml release_version = {workspace_version}" in result.checked
    assert contract["release_version"] == workspace_version
    assert contract["dependencies"] == {"nirs4all-formats": "0.2.13", "nirs4all-io": "0.2.11"}
    assert contract["prerequisites"] == {"dag-ml-data": "0.2.13"}


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


def test_capi_release_archive_preserves_the_actual_project_licenses(tmp_path: Path) -> None:
    """Exercise the real CI assembler; a dual license must never be labeled MIT."""
    import shutil
    import subprocess
    import tarfile

    import yaml

    workflow = yaml.safe_load((ROOT / ".github/workflows/release-python.yml").read_text())
    assemble = next(step["run"] for step in workflow["jobs"]["c-abi-archive"]["steps"] if step.get("name") == "Assemble archive")
    shutil.copyfile(ROOT / "LICENSE", tmp_path / "LICENSE")
    shutil.copytree(ROOT / "LICENSES", tmp_path / "LICENSES")
    header = Path("crates/nirs4all-datasets-capi/include/nirs4all_datasets.h")
    (tmp_path / header).parent.mkdir(parents=True)
    shutil.copyfile(ROOT / header, tmp_path / header)
    (tmp_path / "target/release").mkdir(parents=True)
    binary = tmp_path / "target/release/libnirs4all_datasets_capi.so"
    binary.write_bytes(b"fixture binary for archive-assembly coverage")
    subprocess.run(["bash", "-eu", "-c", assemble.replace("${{ matrix.os }}", "linux")], cwd=tmp_path, check=True)
    with tarfile.open(tmp_path / "nirs4all-datasets-capi-linux.tar.gz") as archive:
        assert "nirs4all-datasets-capi/licenses/MIT.txt" not in archive.getnames()
        base = "nirs4all-datasets-capi/licenses/"
        assert archive.extractfile(base + "LICENSE").read() == (ROOT / "LICENSE").read_bytes()
        for notice in (ROOT / "LICENSES").iterdir():
            if notice.is_file():
                assert archive.extractfile(base + "LICENSES/" + notice.name).read() == notice.read_bytes()
        assert archive.extractfile("nirs4all-datasets-capi/lib/" + binary.name).read() == binary.read_bytes()


def test_matlab_release_archive_includes_exact_notices_reproducibly(tmp_path: Path) -> None:
    """The independently downloadable binding archive carries its own notices."""
    import os
    import shutil
    import subprocess
    import zipfile

    import yaml

    workflow = yaml.safe_load((ROOT / ".github/workflows/release-matlab.yml").read_text())
    assemble = next(step["run"] for step in workflow["jobs"]["matlab-package"]["steps"] if step.get("name") == "Build the MATLAB/Octave package (deterministic git archive)")
    shutil.copyfile(ROOT / "LICENSE", tmp_path / "LICENSE")
    shutil.copytree(ROOT / "LICENSES", tmp_path / "LICENSES")
    prefix = "nirs4all-datasets-matlab-octave-fixture"
    command = assemble.replace("${{ steps.meta.outputs.prefix }}", prefix)
    git_dir = subprocess.check_output(["git", "rev-parse", "--absolute-git-dir"], cwd=ROOT, text=True).strip()
    env = {**os.environ, "GIT_DIR": git_dir, "GIT_WORK_TREE": str(ROOT), "PACKAGE_PREFIX": prefix}
    subprocess.run(["bash", "-eu", "-c", command], cwd=tmp_path, env=env, check=True)
    path = tmp_path / "dist" / f"{prefix}.zip"
    first = path.read_bytes()
    with zipfile.ZipFile(path) as archive:
        assert archive.read(f"{prefix}/LICENSE") == (ROOT / "LICENSE").read_bytes()
        for notice in (ROOT / "LICENSES").iterdir():
            if notice.is_file():
                assert archive.read(f"{prefix}/LICENSES/{notice.name}") == notice.read_bytes()
        assert archive.read(f"{prefix}/build.m") == (ROOT / "bindings/matlab/build.m").read_bytes()
        import time

        epoch = int(subprocess.check_output(["git", "log", "-1", "--format=%ct"], cwd=ROOT, text=True))
        expected_time = list(time.gmtime(epoch)[:6])
        expected_time[-1] -= expected_time[-1] % 2  # ZIP's DOS timestamp resolution
        assert {entry.date_time for entry in archive.infolist()} == {tuple(expected_time)}
    subprocess.run(["bash", "-eu", "-c", command], cwd=tmp_path, env=env, check=True)
    assert path.read_bytes() == first
