"""Independent-review counterexamples B1–B3 and W5, including upload races."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import threading
from concurrent.futures import ThreadPoolExecutor
from types import SimpleNamespace

import pytest

import nirs4all_datasets.private_store as module
from nirs4all_datasets.private_store import PrivateStore, PrivateStoreError, StoreContext, StoreLimits

A = StoreContext("review-a", "alice")
B = StoreContext("review-b", "bob")
DATA = b"good-bytes"
DIGEST = hashlib.sha256(DATA).hexdigest()


@pytest.fixture
def store(tmp_path):
    return PrivateStore(tmp_path / "private-store")


@pytest.fixture
def manifest():
    return {"descriptor": {"id": "review", "name": "Review", "description": "Synthetic review probe",
                           "sources": [{"source_id": "X"}], "provenance": {"contributor": "Asserted"}, "governance": {"license": "NOASSERTION"}},
            "files": [{"path": "opaque.bin", "sha256": DIGEST, "size": len(DATA), "byte_source": "unknown"}]}


def project(store, context=A):
    return store.root / "projects" / hashlib.sha256(context.project_id.encode()).hexdigest()


def code(expected, fn, status=None):
    with pytest.raises(PrivateStoreError) as caught:
        fn()
    assert caught.value.code == expected
    if status is not None:
        assert caught.value.status == status


def publish(store, manifest, context=A):
    pending = store.begin(context, manifest)
    store.put_file(context, pending["submission_id"], DIGEST, [DATA])
    return store.commit(context, pending["submission_id"])["record"]


def test_b1_wrong_digest_then_corrected_same_identity_succeeds(store, manifest):
    wrong = copy.deepcopy(manifest)
    typo = hashlib.sha256(b"typo").hexdigest()
    wrong["files"][0]["sha256"] = typo
    pending = store.begin(A, wrong)
    code("digest_mismatch", lambda: store.put_file(A, pending["submission_id"], typo, [DATA]))
    assert publish(store, manifest)["files"] == manifest["files"]


def test_b1_abandoned_pending_does_not_block_metadata_only(store, manifest):
    store.begin(A, manifest)
    manifest["files"] = []
    assert store.begin(A, manifest)["status"] == "created"


def test_b1_two_pending_variants_conflict_only_on_second_commit(store, manifest):
    first = store.begin(A, manifest)
    variant = copy.deepcopy(manifest)
    variant["descriptor"]["description"] = "Another asserted variant"
    second = store.begin(A, variant)
    for pending in (first, second):
        store.put_file(A, pending["submission_id"], DIGEST, [DATA])
    assert store.commit(A, first["submission_id"])["status"] == "created"
    code("record_id_conflict", lambda: store.commit(A, second["submission_id"]), 409)
    assert len(store.list_records(A)) == 1


def test_b2_lower_limits_leave_records_readable_but_restrict_intake(store, manifest):
    record = publish(store, manifest)
    reopened = PrivateStore(store.root, limits=StoreLimits(max_file_bytes=1, max_manifest_bytes=10, max_files=1, max_submission_bytes=1))
    assert reopened.get_record(A, record["record_id"]) == record
    assert reopened.list_records(A) == [record]
    assert reopened.read_file(A, record["record_id"], DIGEST) == DATA
    code("request_too_large", lambda: reopened.begin(A, manifest), 413)
    other = copy.deepcopy(manifest)
    other["descriptor"]["id"] = "unrelated"
    other["files"] = []
    lower_file_cap = PrivateStore(store.root, limits=StoreLimits(max_file_bytes=1))
    assert lower_file_cap.begin(A, other)["status"] == "created"


def test_b2_tighter_descriptor_schema_does_not_revalidate_stored_data(store, manifest, monkeypatch):
    record = publish(store, manifest)

    def reject(*args, **kwargs):
        raise ValueError("simulated tighter intake schema")

    monkeypatch.setattr(module, "DatasetDescriptor", SimpleNamespace(model_validate=reject))
    reopened = PrivateStore(store.root)
    assert reopened.get_record(A, record["record_id"]) == record
    assert reopened.list_records(A) == [record]
    assert reopened.read_file(A, record["record_id"], DIGEST) == DATA
    code("invalid_manifest", lambda: reopened.begin(A, manifest))


@pytest.mark.parametrize("target", ["record", "blob", "evidence", "file_size", "file_digest"])
def test_b2_structural_and_integrity_tampering_still_corrupt(store, manifest, target):
    record = publish(store, manifest)
    path = project(store) / "records" / (record["record_id"] + ".json")
    if target == "blob":
        next(project(store).rglob(DIGEST)).write_bytes(b"x" * len(DATA))
    else:
        modified = copy.deepcopy(record)
        if target == "record":
            modified["descriptor"]["description"] = "tampered"
        elif target == "evidence":
            modified["rights_status"] = "verified"
        elif target == "file_size":
            modified["files"][0]["size"] = True
        else:
            modified["files"][0]["sha256"] += "\n"
        path.write_text(json.dumps(modified))
    code("corrupt_record", lambda: PrivateStore(store.root).get_record(A, record["record_id"]), 409)


def test_b3_unsafe_b_does_not_block_a_or_store_construction(store, manifest, tmp_path):
    publish(store, manifest, A)
    publish(store, manifest, B)
    sentinel = tmp_path / "external"
    sentinel.write_bytes(b"untouched")
    (project(store, B) / "evil").symlink_to(sentinel)
    reopened = PrivateStore(store.root)
    other = copy.deepcopy(manifest)
    other["descriptor"]["id"] = "unrelated"
    other["files"] = []
    assert reopened.begin(A, other)["status"] == "created"
    code("symlink_refused", lambda: reopened.begin(B, other))
    assert sentinel.read_bytes() == b"untouched"


def test_corrupt_pending_only_blocks_addressed_or_identical_submission(store, manifest):
    pending = store.begin(A, manifest)
    path = project(store) / "pending" / (pending["submission_id"] + ".json")
    path.write_bytes(b"{broken")
    other = copy.deepcopy(manifest)
    other["descriptor"]["id"] = "unrelated"
    other["files"] = []
    assert store.begin(A, other)["status"] == "created"
    code("corrupt_record", lambda: store.put_file(A, pending["submission_id"], DIGEST, [DATA]), 409)
    code("corrupt_record", lambda: store.commit(A, pending["submission_id"]), 409)
    code("corrupt_record", lambda: store.begin(A, manifest), 409)


def test_w5_stalled_stream_does_not_lock_project_or_lose_live_temp(store, manifest):
    pending = store.begin(A, manifest)
    entered, release = threading.Event(), threading.Event()

    def stalled():
        entered.set()
        assert release.wait(10)
        yield DATA

    other = copy.deepcopy(manifest)
    other["descriptor"]["id"] = "unrelated"
    other["files"] = []
    with ThreadPoolExecutor(max_workers=2) as pool:
        uploading = pool.submit(store.put_file, A, pending["submission_id"], DIGEST, stalled())
        try:
            assert entered.wait(5)
            assert pool.submit(store.begin, A, other).result(timeout=2)["status"] == "created"
            assert store.recover(A) == 0
            assert len(list(project(store).rglob(".tmp-*"))) == 1
        finally:
            release.set()
        assert uploading.result(timeout=5)["status"] == "stored"
    assert store.commit(A, pending["submission_id"])["status"] == "created"


@pytest.mark.parametrize("swap", ["bucket", "temporary", "project"])
def test_w5_mid_stream_symlink_swaps_do_not_touch_other_project(store, manifest, swap):
    publish(store, manifest, B)
    pending = store.begin(A, manifest)
    target = next(project(store, B).rglob(DIGEST))
    before = (target.stat().st_ino, target.read_bytes())

    def swapped():
        yield DATA[:2]
        bucket = project(store) / "blobs" / "sha256" / DIGEST[:2]
        path = bucket if swap == "bucket" else project(store) if swap == "project" else next(bucket.glob(".tmp-*"))
        path.rename(path.with_name(path.name + "-saved"))
        path.symlink_to(target.parent if swap == "bucket" else project(store, B) if swap == "project" else target)
        yield DATA[2:]

    with pytest.raises(PrivateStoreError) as caught:
        store.put_file(A, pending["submission_id"], DIGEST, swapped())
    assert caught.value.code in {"symlink_refused", "symlink_or_path_refused", "store_path_changed"}
    assert (target.stat().st_ino, target.read_bytes()) == before


@pytest.mark.parametrize("encoding", ["utf-16", "utf-8-sig"])
def test_manifest_transport_is_strict_utf8(store, manifest, encoding):
    code("invalid_manifest", lambda: store.begin(A, json.dumps(manifest).encode(encoding)))
    assert not store.root.exists()


def test_world_writable_root_is_refused(tmp_path):
    root = tmp_path / "private-store"
    root.mkdir()
    os.chmod(root, 0o777)
    code("unsafe_store_root", lambda: PrivateStore(root))


def test_n3_temp_creation_and_flock_are_atomic_against_cleaners(store, manifest, monkeypatch):
    pending = store.begin(A, manifest)
    opened, release, writer_started = threading.Event(), threading.Event(), threading.Event()
    flock = module.fcntl.flock
    outcome = []

    def paused(fd, operation):
        if operation == module.fcntl.LOCK_EX and threading.current_thread().name == "n3-uploader":
            opened.set()
            assert release.wait(5)
        return flock(fd, operation)

    monkeypatch.setattr(module.fcntl, "flock", paused)

    def uploading():
        outcome.append(store.put_file(A, pending["submission_id"], DIGEST, [DATA]))

    other = copy.deepcopy(manifest)
    other["descriptor"]["id"] = "cleaner"
    other["files"] = []

    def writing():
        writer_started.set()
        return store.begin(A, other)

    uploader = threading.Thread(target=uploading, name="n3-uploader")
    uploader.start()
    with ThreadPoolExecutor(max_workers=1) as pool:
        try:
            assert opened.wait(2)
            writer = pool.submit(writing)
            assert writer_started.wait(2)
            with pytest.raises(TimeoutError):
                writer.result(timeout=0.1)
            assert len(list(project(store).rglob(".tmp-*"))) == 1
        finally:
            release.set()
        assert writer.result(timeout=3)["status"] == "created"
        uploader.join(3)
    assert not uploader.is_alive()
    assert outcome == [{"status": "stored", "sha256": DIGEST, "size": len(DATA), "content_validated": "hash_only"}]
    assert store.commit(A, pending["submission_id"])["status"] == "created"
    assert not list(project(store).rglob(".tmp-*"))
