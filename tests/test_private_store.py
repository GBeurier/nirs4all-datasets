"""Offline contract and adversarial persistence tests for private submissions."""
from __future__ import annotations

import copy
import errno
import hashlib
import ipaddress
import json
import os
import socket
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from types import SimpleNamespace

import pytest

from nirs4all_datasets.private_store import DISK_FLOOR_BYTES, PrivateStore, PrivateStoreError, PrivateSubmission, StoreContext, StoreLimits

PAYLOAD = b"Opaque synthetic private bytes\x00\xff\n"
DIGEST = hashlib.sha256(PAYLOAD).hexdigest()
A = StoreContext("project A", "operator A")
B = StoreContext("project B", "operator B")


@pytest.fixture(autouse=True)
def no_external_network(monkeypatch):
    """A socket guard permits numeric loopback only; no test needs a socket."""
    connect = socket.socket.connect

    def guarded(sock, address):
        if not isinstance(address, tuple) or not ipaddress.ip_address(address[0]).is_loopback:
            raise AssertionError("External network forbidden")
        return connect(sock, address)

    def no_dns(*args, **kwargs):
        raise AssertionError("DNS resolution forbidden")

    monkeypatch.setattr(socket.socket, "connect", guarded)
    monkeypatch.setattr(socket, "getaddrinfo", no_dns)


@pytest.fixture
def manifest():
    return {
        "descriptor": {
            "id": "private_example", "name": "Private example", "description": "Synthetic submission",
            "sources": [{"source_id": "X"}], "provenance": {"contributor": "Asserted contributor"},
            "governance": {"license": "NOASSERTION"},
            "origin_sources": [{"kind": "zenodo", "locator": "https://zenodo.org/records/1"}],
            "dataverse": {"doi": "https://doi.org/10.1234/asserted"},
            "retrieval": {"notes": "Asserted instructions, never executed"},
        },
        "files": [],
    }


@pytest.fixture
def with_file(manifest):
    manifest["files"] = [{"path": "logical/input.bin", "sha256": DIGEST, "size": len(PAYLOAD), "byte_source": "user_provided"}]
    return manifest


@pytest.fixture
def store(tmp_path):
    return PrivateStore(tmp_path / "private-store")


def assert_code(code, call, status=None):
    with pytest.raises(PrivateStoreError) as caught:
        call()
    assert caught.value.code == code
    if status is not None:
        assert caught.value.status == status


def project_root(store, context=A):
    return store.root / "projects" / hashlib.sha256(context.project_id.encode()).hexdigest()


def upload(store, manifest, context=A):
    started = store.begin(context, manifest)
    if started["status"] == "already_present":
        return started
    store.put_file(context, started["submission_id"], DIGEST, [PAYLOAD[:5], PAYLOAD[5:]])
    return store.commit(context, started["submission_id"])


def test_metadata_only_preserves_sparse_assertions_without_defaults(store, manifest):
    original = copy.deepcopy(manifest)
    result = store.begin(A, manifest)
    record = result["record"]
    assert result["status"] == "created"
    assert record["descriptor"] == original["descriptor"]
    assert manifest == original
    assert not {"tier", "versions", "generation"}.intersection(record["descriptor"])
    assert record["descriptor"]["origin_sources"] == original["descriptor"]["origin_sources"]
    assert record["descriptor"]["dataverse"] == original["descriptor"]["dataverse"]
    assert record["descriptor"]["sources"] == [{"source_id": "X"}]
    assert record["provenance_status"] == record["rights_status"] == "asserted_unverified"
    assert record["content_validated"] == "hash_only"
    assert record["project_id"] == A.project_id
    assert record["principal_id"] == A.principal_id
    assert store.list_records(A) == [record]
    assert not list(store.root.rglob("blobs"))
    manifest["descriptor"]["name"] = "Changed outside the store"
    assert store.get_record(A, record["record_id"])["descriptor"] == original["descriptor"]


@pytest.mark.parametrize("tier", ["public", "private", "anonymized"])
def test_metadata_only_allows_declared_tiers_without_publication_or_transformation(store, manifest, tier):
    manifest["descriptor"]["tier"] = tier
    assert store.begin(A, manifest)["record"]["descriptor"]["tier"] == tier


def test_public_origin_and_retrieval_references_never_fetch(store, with_file):
    # Even private/internal/script locators remain inert assertions, not commands.
    with_file["descriptor"]["origin_sources"] += [
        {"kind": "url", "locator": "http://169.254.169.254/latest/meta-data/"},
        {"kind": "script", "locator": "../../never-execute.py"},
    ]
    with_file["descriptor"]["retrieval"]["routes"] = [{
        "id": "asserted-origin", "method": "raw_retrieve", "provider": "url",
        "locator": "http://169.254.169.254/never-resolve",
        "resources": [{"id": "asserted-resource", "selector": {"kind": "direct_url", "value": "file:///never-open"}, "sha256": DIGEST}],
    }]
    result = upload(store, with_file)
    assert result["record"]["descriptor"] == with_file["descriptor"]
    assert store.read_file(A, result["record"]["record_id"], DIGEST) == PAYLOAD


@pytest.mark.parametrize("byte_source", ["unknown", "user_provided"])
def test_unknown_and_user_bytes_are_asserted_unverified(store, with_file, byte_source):
    with_file["files"][0].update(byte_source=byte_source, note="Derivative asserted by submitter")
    record = upload(store, with_file)["record"]
    assert record["files"] == with_file["files"]
    assert record["provenance_status"] == record["rights_status"] == "asserted_unverified"
    assert '"verified"' not in json.dumps(record)
    assert record["content_validated"] == "hash_only"


@pytest.mark.parametrize(("change", "code"), [
    ({"byte_source": "public_origin_download"}, "public_origin_download_refused"),
    ({"byte_source": None}, "invalid_manifest"),
    ({"byte_source": "third_party_private"}, "invalid_manifest"),
    ({"fetch": False}, "fetch_or_mirror_refused"),
    ({"mirror": False}, "fetch_or_mirror_refused"),
    ({"source_url": "https://example.org/file"}, "fetch_or_mirror_refused"),
    ({"download_url": "https://example.org/file"}, "fetch_or_mirror_refused"),
    ({"locator": "file:///etc/passwd"}, "fetch_or_mirror_refused"),
    ({"legal_attestation": True}, "unknown_field"),
    ({"unexpected": "value"}, "unknown_field"),
    ({"size": True}, "invalid_manifest"),
    ({"size": "5"}, "invalid_manifest"),
    ({"size": -1}, "invalid_manifest"),
])
def test_file_refusals_write_nothing(store, with_file, change, code):
    with_file["files"][0].update(change)
    assert_code(code, lambda: store.begin(A, with_file))
    assert not store.root.exists()


def test_missing_byte_source_is_not_defaulted(store, with_file):
    del with_file["files"][0]["byte_source"]
    assert_code("byte_source_required", lambda: store.begin(A, with_file))
    assert not store.root.exists()


@pytest.mark.parametrize("tier", ["public", "anonymized"])
def test_tier_with_bytes_is_refused_before_root_creation(store, with_file, tier):
    with_file["descriptor"]["tier"] = tier
    assert_code("tier_unsupported_for_bytes", lambda: store.begin(A, with_file))
    assert not store.root.exists()


@pytest.mark.parametrize("field", ["project_id", "principal_id", "submitted_at", "provenance_status", "rights_status", "record_id"])
@pytest.mark.parametrize("location", ["envelope", "descriptor", "file"])
def test_server_ownership_cannot_be_submitted(store, with_file, field, location):
    target = with_file if location == "envelope" else with_file["descriptor"] if location == "descriptor" else with_file["files"][0]
    target[field] = "client claim"
    assert_code("server_owned_field", lambda: store.begin(A, with_file))
    assert not store.root.exists()


@pytest.mark.parametrize("field", ["alive", "last_checked"])
def test_origin_health_is_server_owned_even_when_null(store, manifest, field):
    manifest["descriptor"]["origin_sources"][0][field] = None
    assert_code("server_owned_field", lambda: store.begin(A, manifest))
    assert not store.root.exists()


def test_generation_is_server_owned(store, manifest):
    manifest["descriptor"]["generation"] = {"managed": False}
    assert_code("server_owned_field", lambda: store.begin(A, manifest))
    assert not store.root.exists()


@pytest.mark.parametrize("field", ["fetch", "mirror", "source_url", "download_url", "locator"])
def test_envelope_fetch_refused(store, manifest, field):
    manifest[field] = "https://example.org/file"
    assert_code("fetch_or_mirror_refused", lambda: store.begin(A, manifest))
    assert not store.root.exists()


def test_refused_file_never_exists_in_an_existing_project(store, with_file, manifest):
    store.begin(A, manifest)
    before = {p.relative_to(store.root): p.read_bytes() for p in store.root.rglob("*") if p.is_file()}
    with_file["files"][0]["byte_source"] = "public_origin_download"
    assert_code("public_origin_download_refused", lambda: store.begin(A, with_file))
    after = {p.relative_to(store.root): p.read_bytes() for p in store.root.rglob("*") if p.is_file()}
    assert after == before
    assert not list(store.root.rglob(DIGEST))


@pytest.mark.parametrize("path", ["", "/absolute", "../escape", "a/../b", "./a", "a//b", "a/", "a\\b", "C:/file", "C:file", "a\x00b", "a\nb", "con", "AUX.bin", "folder/LPT1.csv", "COM¹.bin", "a.", "a ", "a:b", "a?b", "a\u202eb"])
def test_unsafe_logical_names_are_rejected(store, with_file, path):
    with_file["files"][0]["path"] = path
    assert_code("invalid_filename", lambda: store.begin(A, with_file))
    assert not store.root.exists()


def test_casefold_and_unicode_name_collisions(store, with_file):
    with_file["files"] *= 2
    with_file["files"] = [dict(f, path=p) for f, p in zip(with_file["files"], ["A.bin", "a.BIN"], strict=True)]
    assert_code("filename_conflict", lambda: store.begin(A, with_file))
    with_file["files"][0]["path"] = "é.bin"
    with_file["files"][1]["path"] = "e\u0301.bin"
    assert_code("filename_conflict", lambda: store.begin(A, with_file))


@pytest.mark.parametrize("digest", ["A" * 64, "a" * 63, "a" * 65, "a" * 64 + "\n", "../x", "a" * 63 + "g"])
def test_digests_use_fullmatch_without_normalization(store, with_file, digest):
    with_file["files"][0]["sha256"] = digest
    assert_code("invalid_digest", lambda: store.begin(A, with_file))
    assert not store.root.exists()


@pytest.mark.parametrize("raw", [b"null", b"[]", b"{}", b'{"descriptor":{},"descriptor":{}}', b'{"value":NaN}', b"\xff", b"{"])
def test_malformed_json_writes_nothing(store, raw):
    assert_code("invalid_manifest", lambda: store.begin(A, raw))
    assert not store.root.exists()


def test_descriptor_unknown_fields_and_json_objects_are_rejected(store, manifest):
    manifest["descriptor"]["governance"]["made_up"] = True
    assert_code("unknown_field", lambda: store.begin(A, manifest))
    del manifest["descriptor"]["governance"]["made_up"]
    manifest["descriptor"]["citation"] = Path("not-json")
    assert_code("invalid_manifest", lambda: store.begin(A, manifest))
    assert not store.root.exists()


def test_manifest_first_pending_hidden_and_undeclared_upload_not_consumed(store, with_file):
    consumed = []

    def chunks():
        consumed.append(True)
        yield PAYLOAD

    assert_code("not_found", lambda: store.put_file(A, "a" * 32, DIGEST, chunks()), 404)
    assert not store.root.exists()
    started = store.begin(A, with_file)
    assert store.list_records(A) == []
    assert_code("undeclared_digest", lambda: store.put_file(A, started["submission_id"], "0" * 64, chunks()))
    assert consumed == []
    assert_code("missing_blob", lambda: store.commit(A, started["submission_id"]), 409)
    assert store.list_records(A) == []


@pytest.mark.parametrize(("chunks", "code"), [([PAYLOAD[:-1]], "size_mismatch"), ([PAYLOAD + b"x"], "size_mismatch"), ([b"x" * len(PAYLOAD)], "digest_mismatch"), (["text"], "invalid_chunk")])
def test_invalid_stream_never_publishes_a_blob_or_record(store, with_file, chunks, code):
    started = store.begin(A, with_file)
    assert_code(code, lambda: store.put_file(A, started["submission_id"], DIGEST, chunks))
    assert not list(store.root.rglob(DIGEST))
    assert not list(store.root.rglob(".tmp-*"))
    assert store.list_records(A) == []
    assert upload(store, with_file)["status"] == "created"


def test_interrupted_stream_cleans_temporary_then_retries(store, with_file):
    started = store.begin(A, with_file)

    def interrupted():
        yield PAYLOAD[:2]
        raise RuntimeError("interrupted stream")

    with pytest.raises(RuntimeError, match="interrupted stream"):
        store.put_file(A, started["submission_id"], DIGEST, interrupted())
    assert not list(store.root.rglob(".tmp-*"))
    assert not list(store.root.rglob(DIGEST))
    assert upload(store, with_file)["record"]["files"] == with_file["files"]


def test_empty_file_and_multiple_files_all_required(store, with_file):
    empty = hashlib.sha256(b"").hexdigest()
    with_file["files"].append({"path": "empty", "sha256": empty, "size": 0, "byte_source": "unknown"})
    started = store.begin(A, with_file)
    store.put_file(A, started["submission_id"], DIGEST, [PAYLOAD])
    assert_code("missing_blob", lambda: store.commit(A, started["submission_id"]))
    store.put_file(A, started["submission_id"], empty, [])
    record = store.commit(A, started["submission_id"])["record"]
    assert store.read_file(A, record["record_id"], empty) == b""


def test_same_digest_different_declared_sizes_refused(store, with_file):
    with_file["files"].append(dict(with_file["files"][0], path="other", size=1))
    assert_code("digest_size_conflict", lambda: store.begin(A, with_file))
    assert not store.root.exists()


def test_idempotent_canonical_identity_preserves_first_stamps(store, with_file):
    first = upload(store, with_file)
    reordered = {"files": with_file["files"], "descriptor": dict(reversed(list(with_file["descriptor"].items())))}
    second = store.begin(StoreContext(A.project_id, "another principal"), json.dumps(reordered).encode())
    assert second["status"] == "already_present"
    assert second["record"] == first["record"]
    assert len(store.list_records(A)) == 1
    assert len(list(project_root(store).rglob(DIGEST))) == 1


@pytest.mark.parametrize("committed", [False, True])
def test_same_id_version_content_conflict_precedes_bytes(store, with_file, committed):
    with_file["descriptor"]["versions"] = {"content": "1.2.3"}
    if committed:
        upload(store, with_file)
    else:
        store.begin(A, with_file)
    changed = copy.deepcopy(with_file)
    changed["descriptor"]["name"] = "Conflicting content"
    if committed:
        assert_code("record_id_conflict", lambda: store.begin(A, changed), 409)
        assert len(list(project_root(store).glob("pending/*.json"))) == 1
    else:
        assert store.begin(A, changed)["status"] == "pending"
        assert len(list(project_root(store).glob("pending/*.json"))) == 2
    changed["descriptor"]["versions"]["content"] = "1.2.4"
    assert store.begin(A, changed)["status"] == "pending"


def test_no_implicit_version_in_identity(store, manifest):
    store.begin(A, manifest)
    changed = copy.deepcopy(manifest)
    changed["descriptor"]["name"] = "Changed"
    assert_code("record_id_conflict", lambda: store.begin(A, changed), 409)
    changed["descriptor"]["versions"] = {"content": "1.0.0"}
    assert store.begin(A, changed)["status"] == "created"


def test_identical_ids_across_projects_have_separate_bytes_and_stamps(store, with_file):
    first = upload(store, with_file, A)["record"]
    assert store.list_records(B) == []
    assert_code("not_found", lambda: store.get_record(B, first["record_id"]), 404)
    assert not project_root(store, B).exists()
    second = upload(store, with_file, B)["record"]
    assert first["record_id"] == second["record_id"]
    assert second["project_id"] == B.project_id
    paths = [next(project_root(store, c).rglob(DIGEST)) for c in (A, B)]
    assert paths[0].stat().st_ino != paths[1].stat().st_ino
    paths[0].unlink()
    assert_code("corrupt_record", lambda: store.get_record(A, first["record_id"]), 409)
    assert store.read_file(B, second["record_id"], DIGEST) == PAYLOAD


def test_project_and_source_identifiers_never_become_paths(store, with_file):
    context = StoreContext("../../project:CON", "../principal")
    with_file["descriptor"]["sources"][0]["source_id"] = "../../not-a-path"
    record = upload(store, with_file, context)["record"]
    assert record["project_id"] == context.project_id
    assert store.read_file(context, record["record_id"], DIGEST) == PAYLOAD
    assert all(len(p.name) == 64 for p in (store.root / "projects").iterdir())


def test_foreign_pending_and_record_file_cannot_be_read_or_consumed(store, with_file):
    started = store.begin(A, with_file)
    assert_code("not_found", lambda: store.put_file(B, started["submission_id"], DIGEST, [PAYLOAD]), 404)
    assert_code("not_found", lambda: store.commit(B, started["submission_id"]), 404)
    assert not project_root(store, B).exists()
    record = upload(store, with_file)["record"]
    assert_code("not_found", lambda: store.read_file(B, record["record_id"], DIGEST), 404)
    assert_code("not_found", lambda: store.read_file(A, record["record_id"], "0" * 64), 404)


def test_restart_recovers_temps_and_preserves_pending_and_committed_state(store, with_file):
    started = store.begin(A, with_file)
    store.put_file(A, started["submission_id"], DIGEST, [PAYLOAD])
    orphan = project_root(store) / "pending" / (".tmp-" + "a" * 32)
    orphan.write_bytes(b"interrupted write")
    restarted = PrivateStore(store.root)
    assert restarted.recover(A) == 1
    assert not orphan.exists()
    record = restarted.commit(A, started["submission_id"])["record"]
    assert PrivateStore(store.root).get_record(A, record["record_id"]) == record
    assert PrivateStore(store.root).commit(A, started["submission_id"])["status"] == "already_present"


def test_first_write_after_restart_cleans_only_owned_temp_names(store, with_file):
    started = store.begin(A, with_file)
    orphan = project_root(store) / (".tmp-" + "a" * 32)
    unrelated = project_root(store) / ".tmp-operator-note"
    orphan.write_bytes(b"partial")
    unrelated.write_bytes(b"operator note")
    restarted = PrivateStore(store.root)
    restarted.put_file(A, started["submission_id"], DIGEST, [PAYLOAD])
    assert not orphan.exists()
    assert unrelated.read_bytes() == b"operator note"


@pytest.mark.parametrize("damage", ["missing", "size", "digest"])
def test_corrupt_committed_blobs_are_not_served_or_silently_repaired(store, with_file, damage):
    record = upload(store, with_file)["record"]
    blob = next(store.root.rglob(DIGEST))
    if damage == "missing":
        blob.unlink()
    else:
        blob.write_bytes(b"x" if damage == "size" else b"x" * len(PAYLOAD))
    restarted = PrivateStore(store.root)
    assert_code("corrupt_record", lambda: restarted.get_record(A, record["record_id"]), 409)
    assert_code("corrupt_record", lambda: restarted.list_records(A), 409)
    assert_code("corrupt_record", lambda: restarted.read_file(A, record["record_id"], DIGEST), 409)
    assert_code("corrupt_record", lambda: restarted.begin(A, with_file), 409)


@pytest.mark.parametrize("damage", ["json", "descriptor", "evidence", "ownership", "filename"])
def test_corrupt_record_envelopes_are_not_served(store, manifest, damage):
    record = store.begin(A, manifest)["record"]
    path = project_root(store) / "records" / (record["record_id"] + ".json")
    if damage == "json":
        path.write_text("{")
    elif damage == "filename":
        path.rename(path.with_name("0" * 64 + ".json"))
    else:
        changed = copy.deepcopy(record)
        if damage == "descriptor":
            changed["descriptor"]["name"] = "Tampered"
        elif damage == "evidence":
            changed["rights_status"] = "verified"
        else:
            changed["project_id"] = B.project_id
        path.write_text(json.dumps(changed))
    assert_code("corrupt_record", lambda: store.list_records(A), 409)


def test_failed_record_publication_is_atomic_and_retryable(store, with_file, monkeypatch):
    started = store.begin(A, with_file)
    store.put_file(A, started["submission_id"], DIGEST, [PAYLOAD])
    replace = os.replace

    def fail_record(src, dst, **kwargs):
        if dst.endswith(".json"):
            raise OSError("simulated publication failure")
        return replace(src, dst, **kwargs)

    with monkeypatch.context() as patch:
        patch.setattr(os, "replace", fail_record)
        with pytest.raises(OSError, match="publication failure"):
            store.commit(A, started["submission_id"])
    assert store.list_records(A) == []
    assert not list(store.root.rglob(".tmp-*"))
    assert store.commit(A, started["submission_id"])["status"] == "created"


def test_readers_never_see_unpublished_record_temporary_files(store, with_file, monkeypatch):
    started = store.begin(A, with_file)
    store.put_file(A, started["submission_id"], DIGEST, [PAYLOAD])
    replace = os.replace
    observed = []

    def observe_before_publication(src, dst, **kwargs):
        if dst.endswith(".json"):
            observed.append(store.list_records(A))
        return replace(src, dst, **kwargs)

    with monkeypatch.context() as patch:
        patch.setattr(os, "replace", observe_before_publication)
        record = store.commit(A, started["submission_id"])["record"]
    assert observed == [[]]
    assert store.list_records(A) == [record]


def test_deduplicated_upload_checks_bytes_and_preserves_original_inode(store, with_file):
    started = store.begin(A, with_file)
    record = upload(store, with_file)["record"]
    blob = next(store.root.rglob(DIGEST))
    inode = blob.stat().st_ino
    store.put_file(A, started["submission_id"], DIGEST, [PAYLOAD])
    assert blob.stat().st_ino == inode
    assert_code("digest_mismatch", lambda: store.put_file(A, started["submission_id"], DIGEST, [b"x" * len(PAYLOAD)]))
    assert store.read_file(A, record["record_id"], DIGEST) == PAYLOAD
    blob.unlink()
    assert_code("corrupt_record", lambda: store.put_file(A, started["submission_id"], DIGEST, [PAYLOAD]), 409)
    assert not blob.exists()


def test_disk_full_during_fsync_returns_507_without_publishing(store, with_file, monkeypatch):
    started = store.begin(A, with_file)
    fsync = os.fsync

    def disk_full(fd):
        if os.path.isfile(f"/proc/self/fd/{fd}"):
            raise OSError(errno.ENOSPC, "simulated full disk")
        return fsync(fd)

    with monkeypatch.context() as patch:
        patch.setattr(os, "fsync", disk_full)
        assert_code("insufficient_storage", lambda: store.put_file(A, started["submission_id"], DIGEST, [PAYLOAD]), 507)
    assert not list(store.root.rglob(DIGEST))
    assert not list(store.root.rglob(".tmp-*"))
    assert store.list_records(A) == []


def test_stream_disk_floor_is_rechecked_after_earlier_chunks(store, with_file, monkeypatch):
    started = store.begin(A, with_file)

    def chunks():
        yield PAYLOAD[:2]
        monkeypatch.setattr(os, "fstatvfs", lambda _: SimpleNamespace(f_bavail=DISK_FLOOR_BYTES, f_frsize=1))
        yield PAYLOAD[2:]

    assert_code("insufficient_storage", lambda: store.put_file(A, started["submission_id"], DIGEST, chunks()), 507)
    assert not list(store.root.rglob(DIGEST))
    assert not list(store.root.rglob(".tmp-*"))


def test_multiple_logical_names_deduplicate_only_within_project(store, with_file):
    with_file["files"].append(dict(with_file["files"][0], path="second-name.bin", byte_source="unknown"))
    record = upload(store, with_file)["record"]
    assert record["files"] == with_file["files"]
    assert len(list(store.root.rglob(DIGEST))) == 1
    assert store.read_file(A, record["record_id"], DIGEST) == PAYLOAD


def test_mutated_envelope_is_revalidated_before_writing(store, with_file):
    parsed = PrivateSubmission.parse(with_file)
    parsed.descriptor["generation"] = {"managed": True}
    assert_code("server_owned_field", lambda: store.begin(A, parsed))
    assert not store.root.exists()


def test_file_count_and_submission_caps_refuse_manifests(store, with_file):
    with_file["files"].append(dict(with_file["files"][0], path="other.bin"))
    for limits in (StoreLimits(max_files=1), StoreLimits(max_submission_bytes=len(PAYLOAD))):
        limited = PrivateStore(store.root, limits=limits)
        assert_code("request_too_large", lambda: limited.begin(A, with_file), 413)
        assert not store.root.exists()


def test_concurrent_pending_variants_do_not_reserve_unpublished_identity(store, with_file):
    changed = copy.deepcopy(with_file)
    changed["descriptor"]["name"] = "Conflict"

    def writer(manifest):
        try:
            return PrivateStore(store.root).begin(A, manifest)["status"]
        except PrivateStoreError as exc:
            return exc.code

    with ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(writer, [with_file, changed]))
    assert results == ["pending", "pending"]
    assert len(list(project_root(store).glob("pending/*.json"))) == 2
    assert not list(store.root.rglob(DIGEST))


@pytest.mark.parametrize("with_bytes", [False, True])
def test_eight_concurrent_identical_writers_have_one_first_record(store, manifest, with_file, with_bytes):
    submitted = copy.deepcopy(with_file if with_bytes else manifest)
    if not with_bytes:
        submitted["files"] = []

    def writer(_):
        independent = PrivateStore(store.root)
        return upload(independent, submitted) if with_bytes else independent.begin(A, submitted)

    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(writer, range(8)))
    assert [r["status"] for r in results].count("created") == 1
    assert [r["status"] for r in results].count("already_present") == 7
    assert all(r["record"] == results[0]["record"] for r in results)
    assert len(store.list_records(A)) == 1


def test_cross_project_concurrent_writes_do_not_deduplicate(store, with_file):
    contexts = [StoreContext(f"project {i}", f"operator {i}") for i in range(8)]
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(lambda c: upload(PrivateStore(store.root), with_file, c), contexts))
    assert all(r["status"] == "created" for r in results)
    assert len({next(project_root(store, c).rglob(DIGEST)).stat().st_ino for c in contexts}) == 8
    assert [store.list_records(c)[0]["project_id"] for c in contexts] == [c.project_id for c in contexts]


def test_independent_processes_serialize_same_project(store, with_file):
    script = """
import json, sys
from nirs4all_datasets.private_store import PrivateStore, StoreContext
root, manifest, payload = json.load(sys.stdin)
store = PrivateStore(root)
context = StoreContext('project A', 'operator A')
result = store.begin(context, manifest)
if result['status'] == 'pending':
    sid = result['submission_id']
    store.put_file(context, sid, manifest['files'][0]['sha256'], [bytes.fromhex(payload)])
    result = store.commit(context, sid)
print(json.dumps(result))
"""
    processes = [subprocess.Popen([sys.executable, "-c", script], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) for _ in range(8)]
    data = json.dumps([str(store.root), with_file, PAYLOAD.hex()])
    for process in processes:
        process.stdin.write(data)
        process.stdin.close()
        process.stdin = None
    results = []
    try:
        for process in processes:
            stdout, stderr = process.communicate(timeout=30)
            assert process.returncode == 0, stderr
            results.append(json.loads(stdout))
    finally:
        for process in processes:
            if process.poll() is None:
                process.kill()
                process.wait()
    assert [r["status"] for r in results].count("created") == 1
    assert all(r["record"] == results[0]["record"] for r in results)


def test_read_and_recovery_of_absent_store_create_nothing(store):
    assert store.list_records(A) == []
    assert store.recover(A) == 0
    assert_code("not_found", lambda: store.get_record(A, "0" * 64), 404)
    assert not store.root.exists()


def test_root_must_be_explicit_absolute_outside_git_and_catalog(tmp_path):
    with pytest.raises(TypeError):
        PrivateStore()
    for path in (Path("relative"), tmp_path / "catalog" / "store", tmp_path / "datasets" / "store", Path(__file__).resolve().parents[1] / "private-store"):
        assert_code("unsafe_store_root", lambda p=path: PrivateStore(p))
    repository = tmp_path / "worktree"
    repository.mkdir()
    (repository / ".git").write_text("gitdir: /not/resolved")
    assert_code("unsafe_store_root", lambda: PrivateStore(repository / "store"))


def test_root_or_ancestor_symlinks_are_refused(tmp_path):
    target = tmp_path / "target"
    target.mkdir()
    link = tmp_path / "link"
    link.symlink_to(target, target_is_directory=True)
    assert_code("symlink_refused", lambda: PrivateStore(link))
    assert_code("symlink_refused", lambda: PrivateStore(link / "child"))


def test_root_changed_to_symlink_after_construction_is_refused(store, manifest, tmp_path):
    external = tmp_path / "external"
    external.mkdir()
    store.root.symlink_to(external, target_is_directory=True)
    assert_code("symlink_refused", lambda: store.begin(A, manifest))
    assert list(external.iterdir()) == []


def test_existing_store_only_checks_the_addressed_project(store, manifest, tmp_path):
    store.begin(A, manifest)
    store.begin(B, manifest)
    target = tmp_path / "external-file"
    target.write_bytes(b"untouched")
    (project_root(store, B) / "link").symlink_to(target)
    reopened = PrivateStore(store.root)
    changed = copy.deepcopy(manifest)
    changed["descriptor"]["id"] = "another"
    assert reopened.begin(A, changed)["status"] == "created"
    assert_code("symlink_refused", lambda: reopened.begin(B, changed))
    assert len(reopened.list_records(A)) == 2
    assert target.read_bytes() == b"untouched"


def test_shared_projects_component_symlink_is_refused_at_open(tmp_path):
    root = tmp_path / "private-store"
    root.mkdir()
    target = tmp_path / "external"
    target.mkdir()
    (root / "projects").symlink_to(target, target_is_directory=True)
    assert_code("symlink_or_path_refused", lambda: PrivateStore(root))
    assert list(target.iterdir()) == []


def test_non_regular_payload_is_refused_without_blocking(store, with_file):
    record = upload(store, with_file)["record"]
    blob = next(store.root.rglob(DIGEST))
    blob.unlink()
    os.mkfifo(blob)
    assert_code("unsafe_store_file", lambda: store.read_file(A, record["record_id"], DIGEST))


@pytest.mark.parametrize("target_kind", ["project", "records", "pending", "blob", "lock", "unrelated"])
def test_symlinks_below_root_are_refused_and_targets_untouched(store, with_file, tmp_path, target_kind):
    started = store.begin(A, with_file)
    record = upload(store, with_file)["record"]
    external = tmp_path / "external"
    external.mkdir()
    sentinel = external / "sentinel"
    sentinel.write_bytes(b"must not change")
    if target_kind == "blob":
        target = next(store.root.rglob(DIGEST))
        target.unlink()
        target.symlink_to(sentinel)
    elif target_kind == "lock":
        target = project_root(store) / ".lock"
        target.unlink()
        target.symlink_to(sentinel)
    elif target_kind == "unrelated":
        (project_root(store) / "unrelated").symlink_to(external, target_is_directory=True)
    else:
        target = project_root(store) if target_kind == "project" else project_root(store) / target_kind
        target.rename(target.with_name(target.name + "-saved"))
        target.symlink_to(external, target_is_directory=True)
    with pytest.raises(PrivateStoreError) as caught:
        store.commit(A, started["submission_id"])
    assert caught.value.code in {"symlink_refused", "symlink_or_path_refused"}
    assert sentinel.read_bytes() == b"must not change"
    if target_kind in {"records", "blob", "project"}:
        with pytest.raises(PrivateStoreError):
            store.get_record(A, record["record_id"])


def test_hardlinked_blob_refused(store, with_file, tmp_path):
    record = upload(store, with_file)["record"]
    blob = next(store.root.rglob(DIGEST))
    os.link(blob, tmp_path / "external-hardlink")
    assert_code("unsafe_store_file", lambda: store.read_file(A, record["record_id"], DIGEST))


def test_store_limits_floor_and_actual_chunk_count(store, with_file, monkeypatch):
    with pytest.raises(ValueError):
        StoreLimits(disk_floor_bytes=DISK_FLOOR_BYTES - 1)
    limited = PrivateStore(store.root, limits=StoreLimits(max_file_bytes=1))
    assert_code("request_too_large", lambda: limited.begin(A, with_file), 413)
    assert not store.root.exists()
    limited = PrivateStore(store.root, limits=StoreLimits(max_manifest_bytes=10))
    assert_code("request_too_large", lambda: limited.begin(A, json.dumps(with_file).encode()), 413)
    assert not store.root.exists()
    with monkeypatch.context() as patch:
        patch.setattr(os, "fstatvfs", lambda _: SimpleNamespace(f_bavail=DISK_FLOOR_BYTES - 1, f_frsize=1))
        assert_code("insufficient_storage", lambda: store.begin(A, with_file), 507)
    assert not store.root.exists()
    started = store.begin(A, with_file)
    with monkeypatch.context() as patch:
        patch.setattr(os, "fstatvfs", lambda _: SimpleNamespace(f_bavail=DISK_FLOOR_BYTES - 1, f_frsize=1))
        assert_code("insufficient_storage", lambda: store.put_file(A, started["submission_id"], DIGEST, [PAYLOAD]), 507)
    assert not list(store.root.rglob(DIGEST))
    assert not list(store.root.rglob(".tmp-*"))
    # No Content-Length exists in this API; actual streamed bytes enforce the cap.
    at_cap = PrivateStore(store.root, limits=StoreLimits(max_file_bytes=len(PAYLOAD)))
    assert_code("request_too_large", lambda: at_cap.put_file(A, started["submission_id"], DIGEST, [PAYLOAD, b"excess"]), 413)


def test_import_and_metadata_submission_need_no_network_native_or_web_modules(tmp_path, manifest):
    script = """
import importlib.abc, ipaddress, json, socket, sys
# The existing package imports stdlib socket through importlib.metadata/email.
# Block HTTP/native/web clients and guard sockets, including during imports.
def guarded_connect(sock, address):
    if not isinstance(address, tuple) or not ipaddress.ip_address(address[0]).is_loopback:
        raise AssertionError('External network forbidden')
    return original_connect(sock, address)
def no_dns(*args, **kwargs):
    raise AssertionError('DNS forbidden')
original_connect = socket.socket.connect
socket.socket.connect = guarded_connect
socket.getaddrinfo = no_dns
blocked = {'requests', 'http.client', 'urllib.request', 'pandas', 'numpy', 'pyarrow',
           'nirs4all_access', 'fastapi', 'starlette', 'uvicorn', 'httpx',
           'nirs4all_datasets._n4ds', 'nirs4all_datasets.access', 'nirs4all_datasets.retrieval'}
class Blocker(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if any(fullname == name or fullname.startswith(name + '.') for name in blocked):
            raise AssertionError('Forbidden import: ' + fullname)
sys.meta_path.insert(0, Blocker())
from nirs4all_datasets.private_store import PrivateStore, StoreContext
root, manifest = json.load(sys.stdin)
record = PrivateStore(root).begin(StoreContext('project', 'principal'), manifest)['record']
assert record['descriptor'] == manifest['descriptor']
assert not blocked.intersection(sys.modules)
"""
    result = subprocess.run([sys.executable, "-c", script], input=json.dumps([str(tmp_path / "cold-store"), manifest]), capture_output=True, text=True, timeout=30)
    assert result.returncode == 0, result.stderr
