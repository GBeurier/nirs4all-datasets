"""Fresh-install public-origin access, integrity-aware caching, and staging safety."""
from __future__ import annotations

import json
import types
import zipfile
from pathlib import Path
from typing import Any

import pandas as pd
import pytest

from nirs4all_datasets import access, catalog, public_pull
from nirs4all_datasets.public_pull.common import PullContext
from nirs4all_datasets.schema import DatasetDescriptor, Tier


def _descriptor() -> DatasetDescriptor:
    return DatasetDescriptor(id="origin_demo", name="Origin demo", description="An original public table.", tier="public",
                             sources=[{"source_id": "X", "axis_unit": "nm"}], variables=[{"name": "protein", "role": "target", "type": "numeric"}],
                             provenance={"contributor": "Origin"}, governance={"license": "CC-BY-4.0"},
                             origin_sources=[{"kind": "url", "mode": "raw", "access": "open", "locator": "https://origin.example/data.csv"}])


def test_get_from_bundled_descriptor_downloads_origin_and_reuses_verified_cache(tmp_path: Path, monkeypatch: Any) -> None:
    from nirs4all_datasets import _acquire, index

    original = tmp_path / "original.csv"
    original.write_text("observation_id,1100,1200,protein,site\na,0.1,0.2,4.5,field\nb,0.3,0.4,6.5,glasshouse\n")
    desc = _descriptor()
    calls = []

    def retrieve(request: dict[str, Any], opts: dict[str, Any]) -> dict[str, Any]:
        calls.append(request)
        assert request["route"]["resources"][0]["selector"]["value"] == "https://origin.example/data.csv"
        return {"ok": True, "resources": [{"path": str(original), "status": "downloaded", "sha256": None, "bytes": original.stat().st_size}]}

    def build(descriptor: DatasetDescriptor, context: PullContext) -> Path:
        frame = pd.read_csv(context.download("https://origin.example/data.csv"))
        return context.write_tables({"X": frame[["observation_id", "1100", "1200"]]}, frame[["observation_id", "protein"]], frame[["observation_id", "site"]])

    monkeypatch.setattr(_acquire, "retrieve_raw", retrieve)
    monkeypatch.setattr(public_pull, "_recipe", lambda _: types.SimpleNamespace(build=build))
    monkeypatch.setattr(index, "load_index", lambda _: {"datasets": {desc.id: {"descriptor": desc.model_dump(mode="json"), "tier": "public"}}})
    fresh = tmp_path / "no-registry"
    first = access.get(desc.id, root=fresh, cache_dir=tmp_path / "cache")
    assert first.x().shape == (2, 2)
    assert first.y()["protein"].tolist() == [4.5, 6.5]
    assert first.metadata()["site"].tolist() == ["field", "glasshouse"]
    second = access.get(desc.id, root=fresh, cache_dir=tmp_path / "cache")
    assert second.x().shape == (2, 2)
    assert len(calls) == 1
    # Corrupted local outputs must trigger reconstruction, never stale-data success.
    source = next((tmp_path / "cache" / "public").rglob("X.parquet"))
    source.write_bytes(b"corrupt")
    assert access.get(desc.id, root=fresh, cache_dir=tmp_path / "cache").x().shape == (2, 2)
    assert len(calls) == 2


def test_public_pull_refuses_private_before_download(tmp_path: Path) -> None:
    desc = _descriptor().model_copy(update={"tier": Tier.PRIVATE})
    with pytest.raises(ValueError, match="restricted to public"):
        public_pull.pull(desc, cache_dir=tmp_path)


def test_public_recipe_missing_target_cannot_publish_cache(tmp_path: Path, monkeypatch: Any) -> None:
    def build(descriptor: DatasetDescriptor, context: PullContext) -> Path:
        return context.write_tables({"X": pd.DataFrame({"observation_id": ["a"], "1100": [0.1]})})

    monkeypatch.setattr(public_pull, "_recipe", lambda _: types.SimpleNamespace(build=build))
    with pytest.raises(ValueError, match="missing target"):
        public_pull.pull(_descriptor(), cache_dir=tmp_path)
    assert not list(tmp_path.rglob("origin-pull.json"))


def test_archive_cannot_escape_staging(tmp_path: Path) -> None:
    archive = tmp_path / "unsafe.zip"
    with zipfile.ZipFile(archive, "w") as output:
        output.writestr("../../outside.csv", "no")
    context = PullContext("demo", tmp_path / "work", tmp_path / "cache")
    try:
        with pytest.raises(ValueError, match="unsafe archive"):
            context.extract(archive)
    finally:
        context.session.close()
    assert not (tmp_path / "outside.csv").exists()


def test_listing_without_checkout_uses_packaged_index(tmp_path: Path, monkeypatch: Any) -> None:
    from nirs4all_datasets import index

    desc = _descriptor()
    monkeypatch.setattr(index, "load_index", lambda _: {"datasets": {desc.id: {"descriptor": desc.model_dump(mode="json"), "tier": "public"}}})
    assert [x["id"] for x in catalog.search(tmp_path)] == [desc.id]


@pytest.mark.parametrize("damage", ["invalid_json", "empty_files", "omitted_source"])
def test_corrupt_cache_marker_rebuilds(tmp_path: Path, monkeypatch: Any, damage: str) -> None:
    calls = []

    def build(descriptor: DatasetDescriptor, context: PullContext) -> Path:
        calls.append(descriptor.id)
        return context.write_tables(
            {"X": pd.DataFrame({"observation_id": ["a"], "1100": [0.5]})},
            pd.DataFrame({"observation_id": ["a"], "protein": [2.0]}),
        )

    monkeypatch.setattr(public_pull, "_recipe", lambda _: types.SimpleNamespace(build=build))
    dest, _ = public_pull.pull(_descriptor(), cache_dir=tmp_path)
    marker = dest / "origin-pull.json"
    saved = json.loads(marker.read_text())
    if damage == "invalid_json":
        marker.write_text("{")
    else:
        if damage == "empty_files":
            saved["files"] = {}
        else:
            saved["files"].pop("canonical/sources/X.parquet")
        marker.write_text(json.dumps(saved))
    rebuilt, _ = public_pull.pull(_descriptor(), cache_dir=tmp_path)
    assert rebuilt == dest
    assert len(calls) == 2
    assert "canonical/sources/X.parquet" in json.loads(marker.read_text())["files"]


def test_download_budget_counts_new_bytes_across_resources(tmp_path: Path, monkeypatch: Any) -> None:
    from nirs4all_datasets import _acquire

    context = PullContext("demo", tmp_path / "stage", tmp_path / "cache", max_total_bytes=10)
    data = tmp_path / "result.csv"
    data.write_bytes(b"abcd")
    budgets = []

    def retrieve(request, opts):
        budgets.append(opts["max_total_bytes"])
        return {"ok": True, "resources": [{"path": str(data), "status": "downloaded", "bytes": 4}]}

    monkeypatch.setattr(_acquire, "retrieve_raw", retrieve)
    context.download("https://example.org/a.csv")
    context.download("https://example.org/b.csv")
    assert budgets == [10, 6]
    assert context.downloaded_bytes == 8
    class Response:
        def iter_content(self, size):
            return iter([b"x", b"yz"])
    iterator = context.iter_bytes(Response())
    assert next(iterator) == b"x"
    with pytest.raises(ValueError, match="max_total_bytes"):
        next(iterator)
    context.session.close()


def test_guestbook_profile_and_signed_url_do_not_enter_provenance(tmp_path: Path, monkeypatch: Any) -> None:
    from nirs4all_datasets import _acquire

    profile = {"name": "Test Person", "email": "person@example.test", "answers": [{"id": 8, "value": "Research"}]}
    context = PullContext("demo", tmp_path / "stage", tmp_path / "cache", guestbook_response=profile)
    monkeypatch.setattr(context, "get_json", lambda *_a, **_k: {"data": {"nameRequired": True, "emailRequired": True, "customQuestions": [{"id": 8, "question": "purpose", "required": True}]}})
    signed = "https://store.example/data?X-Amz-Credential=secret-credential&X-Amz-Security-Token=secret-token&X-Amz-Signature=secret-signature"

    class Response:
        def raise_for_status(self):
            pass
        def json(self):
            return {"data": {"signedUrl": signed}}

    def post(url, *, params, json, timeout):
        assert json == {"guestbookResponse": profile}
        return Response()

    original = tmp_path / "original.csv"
    original.write_text("data")
    monkeypatch.setattr(context.session, "post", post)
    monkeypatch.setattr(_acquire, "retrieve_raw", lambda *_a, **_k: {"ok": True, "resources": [{"path": str(original), "status": "downloaded", "bytes": 4}]})
    assert context.dataverse_file(42, "original.csv", guestbook_id=7) == original
    provenance = json.dumps(context.downloads)
    assert "person@example.test" not in provenance
    assert "secret-credential" not in provenance and "secret-token" not in provenance and "secret-signature" not in provenance
    assert context.downloads[0]["url"] == "https://dataverse.harvard.edu/api/access/datafile/42?format=original"
    context.session.close()


def test_download_error_removes_url_credentials_and_signed_query(tmp_path: Path, monkeypatch: Any) -> None:
    from nirs4all_datasets import _acquire

    context = PullContext("demo", tmp_path / "stage", tmp_path / "cache")
    signed = "https://user:secretpass@example.org/file?X-Amz-Credential=key123&X-Amz-Security-Token=token123&X-Amz-Signature=sig123#fragment"
    monkeypatch.setattr(_acquire, "retrieve_raw", lambda *_a, **_k: {"ok": False, "resources": [{"status": "failed", "reason": f"request failed for {signed}"}]})
    with pytest.raises(RuntimeError) as error:
        context.download(signed)
    message = str(error.value)
    for secret in ("secretpass", "key123", "token123", "sig123", "fragment"):
        assert secret not in message
    context.session.close()


def test_downloads_of_same_origin_are_serialized(tmp_path: Path, monkeypatch: Any) -> None:
    import concurrent.futures
    import threading
    import time

    from nirs4all_datasets import _acquire

    data = tmp_path / "file.csv"
    data.write_bytes(b"a")
    lock = threading.Lock()
    active = 0
    peak = 0

    def retrieve(request, opts):
        nonlocal active, peak
        with lock:
            active += 1
            peak = max(peak, active)
        time.sleep(0.05)
        with lock:
            active -= 1
        return {"ok": True, "resources": [{"path": str(data), "status": "cached_unverified", "bytes": 1}]}

    monkeypatch.setattr(_acquire, "retrieve_raw", retrieve)
    contexts = [PullContext("demo", tmp_path / f"stage-{i}", tmp_path / "cache") for i in range(2)]
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            paths = list(pool.map(lambda ctx: ctx.download("https://example.test/data.csv"), contexts))
        assert paths == [data, data]
        assert peak == 1
    finally:
        for context in contexts:
            context.session.close()


def test_concurrent_pulls_share_one_build(tmp_path: Path, monkeypatch: Any) -> None:
    import concurrent.futures
    import time

    builds = []

    def build(descriptor: DatasetDescriptor, context: PullContext) -> Path:
        builds.append(descriptor.id)
        time.sleep(0.05)
        return context.write_tables(
            {"X": pd.DataFrame({"observation_id": ["a"], "1100": [0.5]})},
            pd.DataFrame({"observation_id": ["a"], "protein": [2.0]}),
        )

    monkeypatch.setattr(public_pull, "_recipe", lambda _: types.SimpleNamespace(build=build))
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(lambda _: public_pull.pull(_descriptor(), cache_dir=tmp_path), range(2)))
    assert len(builds) == 1
    assert results[0][0] == results[1][0]


def _local_canonical(root: Path, descriptor: DatasetDescriptor, *, spectrum: float, target: float, with_manifest: bool = True, stale: bool = False) -> Path:
    from nirs4all_datasets.canonical import build_canonical
    from nirs4all_datasets.manifest import processing_hash, write_manifest
    from nirs4all_datasets.schema import Manifest

    leaf = root / "fixture-leaf"
    leaf.mkdir(parents=True, exist_ok=True)
    pd.DataFrame({"observation_id": ["sample-1"], "1100": [spectrum]}).to_csv(leaf / "X.csv", sep=";", index=False)
    pd.DataFrame({"observation_id": ["sample-1"], "protein": [target]}).to_csv(leaf / "Y.csv", sep=";", index=False)
    directory = root / "datasets" / descriptor.id
    result = build_canonical(leaf, descriptor, directory)
    assert result.config["variables"]["path"] == "canonical/variables.parquet"
    if with_manifest:
        manifest = Manifest(dataset_id=descriptor.id, processing_hash="0" * 64 if stale else processing_hash(descriptor), converter_name="test", converter_version="1")
        write_manifest(manifest, directory / "manifest.json")
    return directory


def test_public_local_current_manifest_and_targets_load_without_recipe(tmp_path: Path, monkeypatch: Any) -> None:
    desc = _descriptor()
    directory = _local_canonical(tmp_path, desc, spectrum=0.25, target=4.5)
    monkeypatch.setattr(access, "_read_descriptor", lambda _root, _name: desc)
    monkeypatch.setattr(public_pull, "available", lambda _id: True)
    monkeypatch.setattr(public_pull, "pull", lambda *_a, **_k: (_ for _ in ()).throw(AssertionError("unexpected public origin pull")))
    dataset = access.get(desc.id, root=tmp_path, cache_dir=tmp_path / "cache")
    assert dataset._dir == directory
    assert dataset.x()[0, 0] == pytest.approx(0.25)
    assert dataset.y()["protein"].tolist() == [4.5]


@pytest.mark.parametrize("invalid", ["manifest_missing", "manifest_stale", "target_missing", "variables_missing", "manifest_and_variables_missing", "source_missing", "manifest_invalid", "variables_corrupt"])
def test_public_local_invalid_cache_uses_recipe(tmp_path: Path, monkeypatch: Any, invalid: str) -> None:
    desc = _descriptor()
    local = _local_canonical(tmp_path, desc, spectrum=0.25, target=4.5, with_manifest=invalid not in {"manifest_missing", "manifest_and_variables_missing"}, stale=invalid == "manifest_stale")
    if invalid == "target_missing":
        variables = local / "canonical" / "variables.parquet"
        frame = pd.read_parquet(variables).drop(columns="protein")
        frame.to_parquet(variables)
    if invalid == "manifest_invalid":
        (local / "manifest.json").write_text("{")
    if invalid == "variables_corrupt":
        (local / "canonical" / "variables.parquet").write_bytes(b"broken")
    if invalid in {"variables_missing", "manifest_and_variables_missing"}:
        (local / "canonical" / "variables.parquet").unlink()
    if invalid == "source_missing":
        (local / "canonical" / "sources" / "X.parquet").unlink()
    remote = _local_canonical(tmp_path / "prepared", desc, spectrum=0.75, target=8.5, with_manifest=False)
    calls = []

    def pull(descriptor: DatasetDescriptor, **kwargs: Any) -> tuple[Path, DatasetDescriptor]:
        calls.append(descriptor.id)
        return remote, descriptor

    monkeypatch.setattr(access, "_read_descriptor", lambda _root, _name: desc)
    monkeypatch.setattr(public_pull, "available", lambda _id: True)
    monkeypatch.setattr(public_pull, "pull", pull)
    dataset = access.get(desc.id, root=tmp_path, cache_dir=tmp_path / "cache")
    assert calls == [desc.id]
    assert dataset._dir == remote
    assert dataset.x()[0, 0] == pytest.approx(0.75)
    assert dataset.y()["protein"].tolist() == [8.5]
