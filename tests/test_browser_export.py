"""Tests for the offline public browser exporter (:mod:`nirs4all_datasets.browser_export`)."""

from __future__ import annotations

import hashlib
import json
import sys
import types
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import pytest
import yaml

from nirs4all_datasets import browser_export
from nirs4all_datasets.browser_export import CATALOG_SCHEMA, SOURCE_SCHEMA, BrowserExportError, export, main
from nirs4all_datasets.schema import Tier


def _governed(desc: Any, *, tier: Tier = Tier.PUBLIC) -> Any:
    gov = desc.governance.model_copy(update={
        "license": "CC-BY-4.0", "owner_steward": "Lab", "redistribution_rights": "open", "consent_ethics_status": "n/a",
        "anonymization_status": "n/a", "permitted_use": "research", "access_policy": "open",
    })
    return desc.model_copy(update={"governance": gov, "tier": tier})


def _registry(canonical_dataset: Any, tmp_path: Path, name: str = "pub", *, tier: Tier = Tier.PUBLIC, **kwargs: Any) -> tuple[Path, Any]:
    """A catalog root whose descriptor + local canonical data resolve offline through ``get()``."""
    dataset_dir, desc = canonical_dataset(name, public=True, **kwargs)
    desc = _governed(desc, tier=tier)
    catalog = tmp_path / "catalog" / "datasets"
    catalog.mkdir(parents=True, exist_ok=True)
    (catalog / f"{desc.id}.yaml").write_text(yaml.safe_dump(desc.model_dump(mode="json")), encoding="utf-8")
    assert dataset_dir == tmp_path / "datasets" / desc.id
    return tmp_path, desc


class _FakeIO:
    """A recording stand-in for native IO, mirroring a minimal assembled_full schema-3 result."""

    __version__ = "0.0.test"

    def __init__(self) -> None:
        self.calls: list[tuple[dict[str, Any], Any, Any]] = []
        self.rows: int | None = None
        self.schema = 3
        self.extra: dict[str, Any] = {}

    def assembled_full(self, spec: dict[str, Any], conventions: Any, name: Any) -> dict[str, Any]:
        self.calls.append((spec, conventions, name))
        n = self.rows if self.rows is not None else len(pd.read_parquet(spec["sources"][0]["input"]))
        precision = {"dtype": "float32", "origin": "source-declared", "source_dtype": "float32", "requested_dtype": None, "consumer": None}
        x = {"dtype": "float32", "n_rows": n, "n_cols": 1, "data_bytes_hex": np.zeros(n, "<f4").tobytes().hex(), "validity": [True] * n, "precision": precision}
        block = {"n_samples": n, "source_ids": [spec["sources"][0]["id"]], "x": [x], "feature_headers": [["1100"]], "header_units": ["nm"],
                 "y": None, "y_headers": [], "y_categorical": {}, "metadata": {"n_rows": n, "columns": []}}
        return {"assembled_schema_version": self.schema, "name": name, "partition_order": ["train"], "blocks": {"train": block}, "warnings": [], **self.extra}


def _install_io(monkeypatch: pytest.MonkeyPatch, *, profile: int | None, assembled_full: Any = None) -> None:
    module = types.ModuleType("nirs4all_io")
    module.__version__ = _FakeIO.__version__  # type: ignore[attr-defined]
    if assembled_full is not None:
        module.assembled_full = assembled_full  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, "nirs4all_io", module)
    if profile is None:  # a build that declares no wire profile: checked per native result
        monkeypatch.delitem(sys.modules, "nirs4all_io._assembled", raising=False)
        monkeypatch.setattr(browser_export, "_assembled_profile", lambda _module: None)
        return
    assembled = types.ModuleType("nirs4all_io._assembled")
    assembled.ASSEMBLED_DATASET_VERSION = profile  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, "nirs4all_io._assembled", assembled)


@pytest.fixture
def fake_io(monkeypatch: pytest.MonkeyPatch) -> _FakeIO:
    fake = _FakeIO()
    _install_io(monkeypatch, profile=3, assembled_full=fake.assembled_full)
    return fake


def _no_acquisition(monkeypatch: pytest.MonkeyPatch) -> None:
    def forbidden(*_: Any, **__: Any) -> None:
        raise AssertionError("acquisition must not start")

    monkeypatch.setattr("nirs4all_datasets.access.get", forbidden)


def test_exports_catalog_and_one_asset_per_explicit_source(canonical_dataset: Any, tmp_path: Path, fake_io: _FakeIO) -> None:
    root, desc = _registry(canonical_dataset, tmp_path, blocks=("X1", "X2"), sample_of={"o1": "s1", "o2": "s2"}, split={"o1": "cal", "o2": "val"})
    out = tmp_path / "export"

    catalog = export([desc.id], out, root=root)

    assert json.loads((out / "catalog.json").read_text(encoding="utf-8")) == catalog
    assert catalog["schema"] == CATALOG_SCHEMA
    [entry] = catalog["datasets"]
    assert entry["id"] == desc.id and entry["tier"] == "public" and entry["license"] == "CC-BY-4.0"
    assert [s["id"] for s in entry["sources"]] == ["X1", "X2"]
    for source in entry["sources"]:
        data = (out / source["url"]).read_bytes()
        assert source["url"] == f"sources/{desc.id}/{source['id']}.json"
        assert source["sha256"] == hashlib.sha256(data).hexdigest() and source["size_bytes"] == len(data)
        asset = json.loads(data)
        assert asset["schema"] == SOURCE_SCHEMA and asset["dataset_id"] == desc.id and asset["source_id"] == source["id"]
        assert asset["assembled"]["blocks"]["train"]["n_samples"] == 2
        provenance = asset["provenance"]
        assert provenance["materialization"]["operation"] == "nirs4all_io.assembled_full"
        assert provenance["native_splits"] == {"exposed_as_metadata": ["split_original"], "applied": False, "note": provenance["native_splits"]["note"]}
        assert all(not Path(item["path"]).is_absolute() for item in provenance["materialization"]["inputs"])
        assert str(root) not in data.decode("utf-8")
    # Each native call selects exactly one spectral source; variables and the split are joined to it.
    selected = [[s["id"] for s in spec["sources"] if s.get("modality") == "spectroscopy"] for spec, _, _ in fake_io.calls]
    assert selected == [["X1"], ["X2"]]
    assert all(name == desc.id for _, _, name in fake_io.calls)
    # The owner bridge spec is passed as-is, plus only the declared raw-export NA policy on every source.
    from nirs4all_datasets.access import get

    bridge = get(desc.id, root=root).to_io_spec(source="X1")
    sent = fake_io.calls[0][0]
    assert all(s["params"]["na"] == {"policy": "ignore"} for s in sent["sources"])
    stripped = [{k: v for k, v in s.items() if k != "params"} for s in sent["sources"]]
    assert stripped == [{k: v for k, v in s.items() if k != "params"} for s in bridge["sources"]]
    assert [{k: v for k, v in s.get("params", {}).items() if k != "na"} for s in sent["sources"]] == [s.get("params", {}) for s in bridge["sources"]]


@pytest.mark.parametrize("tier", [Tier.PRIVATE, Tier.ANONYMIZED])
def test_refuses_non_public_tier_before_acquisition(canonical_dataset: Any, tmp_path: Path, fake_io: _FakeIO, monkeypatch: pytest.MonkeyPatch, tier: Tier) -> None:
    root, desc = _registry(canonical_dataset, tmp_path, tier=tier)
    _no_acquisition(monkeypatch)
    with pytest.raises(BrowserExportError, match="not exportable"):
        export([desc.id], tmp_path / "export", root=root)
    assert not (tmp_path / "export").exists() and fake_io.calls == []


def test_refuses_public_descriptor_with_publication_blockers(canonical_dataset: Any, tmp_path: Path, fake_io: _FakeIO, monkeypatch: pytest.MonkeyPatch) -> None:
    root, desc = _registry(canonical_dataset, tmp_path)
    data = desc.model_dump(mode="json")
    data["governance"]["license"] = "CC-BY-NC-4.0"
    (root / "catalog" / "datasets" / f"{desc.id}.yaml").write_text(yaml.safe_dump(data), encoding="utf-8")
    _no_acquisition(monkeypatch)
    with pytest.raises(BrowserExportError, match="open license"):
        export([desc.id], tmp_path / "export", root=root)


def test_refuses_missing_native_operation(canonical_dataset: Any, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    root, desc = _registry(canonical_dataset, tmp_path)
    _install_io(monkeypatch, profile=None)
    _no_acquisition(monkeypatch)
    with pytest.raises(BrowserExportError, match="does not expose the native assembled_full"):
        export([desc.id], tmp_path / "export", root=root)


@pytest.mark.parametrize("profile", [2, 4, 5])
def test_refuses_unsupported_io_profile_before_acquisition(canonical_dataset: Any, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, profile: int) -> None:
    root, desc = _registry(canonical_dataset, tmp_path)
    fake = _FakeIO()
    _install_io(monkeypatch, profile=profile, assembled_full=fake.assembled_full)
    _no_acquisition(monkeypatch)
    with pytest.raises(BrowserExportError, match=rf"assembled_schema_version={profile}.*require one of \[3\]"):
        export([desc.id], tmp_path / "export", root=root)
    assert fake.calls == [] and not (tmp_path / "export").exists()


def test_refuses_unsupported_result_schema_without_writing(canonical_dataset: Any, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    root, desc = _registry(canonical_dataset, tmp_path)
    fake = _FakeIO()
    fake.schema = 2
    _install_io(monkeypatch, profile=None, assembled_full=fake.assembled_full)
    with pytest.raises(BrowserExportError, match="assembled_schema_version=2"):
        export([desc.id], tmp_path / "export", root=root)
    assert len(fake.calls) == 1 and not (tmp_path / "export").exists() and not list(tmp_path.glob(".browser-export-*"))


def test_raw_export_spec_declares_na_ignore_and_refuses_conflicts() -> None:
    spec = {"sources": [{"id": "X", "params": {"header_unit": "nm"}}, {"id": "variables"}]}
    declared = browser_export.raw_export_spec(spec)
    assert declared["sources"] == [{"id": "X", "params": {"header_unit": "nm", "na": {"policy": "ignore"}}}, {"id": "variables", "params": {"na": {"policy": "ignore"}}}]
    assert "na" not in spec["sources"][0]["params"]  # the owner spec is not mutated
    with pytest.raises(BrowserExportError, match="NA handling"):
        browser_export.raw_export_spec({"sources": [{"id": "X", "params": {"na": {"policy": "remove_sample"}}}]})


@pytest.mark.parametrize("ids", [[], [""], ["a", "a"], ["../escape"]])
def test_requires_explicit_valid_unique_ids(tmp_path: Path, fake_io: _FakeIO, ids: list[str]) -> None:
    with pytest.raises(BrowserExportError):
        export(ids, tmp_path / "export")


def test_cli_requires_ids(capsys: pytest.CaptureFixture[str], tmp_path: Path) -> None:
    with pytest.raises(SystemExit):
        main(["--out", str(tmp_path / "export")])
    assert "--ids" in capsys.readouterr().err


def test_output_must_be_empty_and_outside_git(canonical_dataset: Any, tmp_path: Path, fake_io: _FakeIO) -> None:
    root, desc = _registry(canonical_dataset, tmp_path)
    occupied = tmp_path / "occupied"
    occupied.mkdir()
    (occupied / "keep.txt").write_text("x", encoding="utf-8")
    with pytest.raises(BrowserExportError, match="never overwritten"):
        export([desc.id], occupied, root=root)
    repo = tmp_path / "repo"
    (repo / ".git").mkdir(parents=True)
    with pytest.raises(BrowserExportError, match="outside Git"):
        export([desc.id], repo / "public" / "browser", root=root)
    assert (occupied / "keep.txt").read_text(encoding="utf-8") == "x" and fake_io.calls == []


def test_refuses_row_loss_and_leaves_nothing(canonical_dataset: Any, tmp_path: Path, fake_io: _FakeIO) -> None:
    root, desc = _registry(canonical_dataset, tmp_path)
    fake_io.rows = 1
    with pytest.raises(BrowserExportError, match="refusing a subset"):
        export([desc.id], tmp_path / "export", root=root)
    assert not (tmp_path / "export").exists()
    assert not list(tmp_path.glob(".browser-export-*"))


def test_refuses_non_strict_json(canonical_dataset: Any, tmp_path: Path, fake_io: _FakeIO) -> None:
    root, desc = _registry(canonical_dataset, tmp_path)
    fake_io.extra = {"audits": [{"value": float("nan")}]}
    with pytest.raises(BrowserExportError, match="strict JSON"):
        export([desc.id], tmp_path / "export", root=root)


def test_default_root_is_isolated_from_cwd(canonical_dataset: Any, tmp_path: Path, fake_io: _FakeIO, monkeypatch: pytest.MonkeyPatch) -> None:
    # A cwd registry declaring a non-public dataset as public must not be consulted by default.
    root, desc = _registry(canonical_dataset, tmp_path)
    monkeypatch.chdir(root)
    seen: list[Path] = []

    def read_descriptor(catalog_root: Path, name: str) -> Any:
        seen.append(catalog_root)
        raise FileNotFoundError(f"unknown dataset {name!r}")

    monkeypatch.setattr("nirs4all_datasets.access._read_descriptor", read_descriptor)
    with pytest.raises(BrowserExportError, match="unknown dataset"):
        export([desc.id], tmp_path / "export")
    assert seen and seen[0] != root.resolve() and not seen[0].exists()


def test_cli_exports_with_comma_separated_ids(canonical_dataset: Any, tmp_path: Path, fake_io: _FakeIO, capsys: pytest.CaptureFixture[str]) -> None:
    root, desc = _registry(canonical_dataset, tmp_path)
    assert main(["--ids", f"{desc.id},", "--out", str(tmp_path / "export"), "--root", str(root)]) == 0
    summary = json.loads(capsys.readouterr().out)
    assert summary["datasets"] == [{"id": desc.id, "sources": [f"sources/{desc.id}/X.json"]}]


def _decode(block: dict[str, Any]) -> np.ndarray:
    dtype = {"float32": "<f4", "float64": "<f8"}[block["dtype"]]
    return np.frombuffer(bytes.fromhex(block["data_bytes_hex"]), dtype=dtype).reshape(block["n_rows"], block["n_cols"])


def test_real_native_io_preserves_values_names_identity_and_missing_rows(canonical_dataset: Any, tmp_path: Path) -> None:
    nirs4all_io = pytest.importorskip("nirs4all_io")
    if not callable(getattr(nirs4all_io, "assembled_full", None)):
        pytest.skip("installed nirs4all_io does not expose the native assembled_full operation")
    profile = browser_export._assembled_profile(nirs4all_io)
    if profile not in browser_export.SUPPORTED_ASSEMBLED_SCHEMAS:
        pytest.skip(f"installed nirs4all_io {nirs4all_io.__version__} emits assembled schema {profile}; the browser wire needs 3")
    root, desc = _registry(canonical_dataset, tmp_path, name="native", block_obs={"X": ["o1", "o2", "o3"]}, sample_of={"o1": "s1", "o2": "s2", "o3": "s3"},
                           targets={"Moisture": "numeric", "variety": "categorical"}, extra_meta=("site",))
    canonical = root / "datasets" / desc.id / "canonical"
    variables = pd.read_parquet(canonical / "variables.parquet")
    variables.loc[variables["sample_id"] == "s2", "Moisture"] = np.nan  # missing numeric target
    variables.loc[variables["sample_id"] == "s3", "variety"] = None  # missing categorical target
    variables.to_parquet(canonical / "variables.parquet", index=False)
    spectra = pd.read_parquet(canonical / "sources" / "X.parquet")
    spectra.loc[spectra["observation_id"] == "o2", "1102"] = np.nan  # missing spectral cell
    spectra.to_parquet(canonical / "sources" / "X.parquet", index=False)

    from nirs4all_datasets.access import get

    dataset = get(desc.id, root=root)
    expected_x = np.asarray(dataset.x("X"), dtype=np.float32)

    export([desc.id], tmp_path / "export", root=root)

    asset = json.loads((tmp_path / "export" / "sources" / desc.id / "X.json").read_text(encoding="utf-8"))
    native = nirs4all_io.assembled_full(browser_export.raw_export_spec(dataset.to_io_spec(source="X")), None, desc.id)
    assert asset["assembled"] == json.loads(json.dumps(native))  # the native result, unmodified
    assert asset["assembled"]["assembled_schema_version"] in browser_export.SUPPORTED_ASSEMBLED_SCHEMAS
    [block] = asset["assembled"]["blocks"].values()
    assert block["n_samples"] == 3  # no row dropped for a missing X cell or missing targets
    [x] = block["x"]
    assert x["validity"] == np.isfinite(expected_x).ravel().tolist()
    decoded = _decode(x)
    assert np.array_equal(decoded[np.isfinite(expected_x)], expected_x[np.isfinite(expected_x)])
    assert block["feature_headers"][0] == ["1100", "1102"] and block["header_units"] == ["nm"]
    columns = {c["name"]: c["values"] for c in block["metadata"]["columns"]}
    assert columns["observation_id"] == ["o1", "o2", "o3"] and columns["sample_id"] == ["s1", "s2", "s3"] and "site" in columns
    targets = {c["name"]: c for c in block["y"]["columns"]}
    assert set(targets) == {"Moisture", "variety"}
    assert targets["Moisture"]["block"]["validity"] == [True, False, True]
    assert _decode(targets["Moisture"]["block"])[[0, 2], 0].tolist() == [1.0, 2.0]
    assert targets["variety"]["block"]["validity"] == [True, True, False]
    assert block["y_categorical"]["variety"]["categories"] == ["class_0", "class_1"]  # missing is not a class
    assert asset["provenance"]["materialization"]["io_spec"]["sources"][0]["params"]["na"] == {"policy": "ignore"}
    assert browser_export.public_refusals(dataset.descriptor) == []
