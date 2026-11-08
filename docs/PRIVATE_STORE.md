# Offline private store

`nirs4all_datasets.private_store` stores submitted descriptors and opaque private
files separately from the catalog and acquisition cache. Catalog and origin
retrieval policy is unchanged. No catalog, card, schema hash, qualification,
frontend, or generated artifact participates in this store.

This is an offline Python API with no authentication dependency. A separate
optional [project service](PROJECT_SERVICE.md) uses pure ASGI and the WORK-accepted
access leaf, authenticating before reading bodies. The offline API remains usable
without that extra. Independent final WORK review of Datasets remains required.

## Assertions and evidence

The store performs **no origin detection**. A SHA-256 digest proves integrity of
what was submitted, nothing about origin, ownership, redistribution rights, or
legal compliance. There is no public-hash denylist or generated hash artifact.

`DatasetDescriptor` validates metadata, but its output is discarded. The store
persists the submitted descriptor JSON without injected defaults or normalized
values: omitted tier, versions, origin access/mode, modality, and Dataverse instance
remain omitted. DOI citations, open origins, contributor prose, retrieval plans,
and reproduction notes are inert assertions. Nothing resolves a DOI, fetches a
URL, executes a recipe, opens a local locator, or parses submitted file contents.

Every record carries the fixed labels:

| Field | Value |
| --- | --- |
| `provenance_status` | `asserted_unverified` |
| `rights_status` | `asserted_unverified` |
| `content_validated` | `hash_only` |

Only streamed size/digest and operator-supplied server stamps are established by
this layer. Tiers and credentials are never evidence of origin or rights.
Free-text declarations remain assertions, even if they claim verification.

## Manifest contract

`PrivateSubmission` is separate from the existing `DatasetDescriptor`,
`Provenance`, and catalog `FileEntry`; those contracts are unchanged.

```json
{
  "descriptor": {
    "id": "private_example",
    "name": "Private example",
    "description": "Submitted measurements",
    "sources": [{"source_id": "X"}],
    "provenance": {"contributor": "Submitted contributor"},
    "governance": {"license": "NOASSERTION"}
  },
  "files": []
}
```

Both envelope keys are required. Each file declares `path`, `sha256`, `size`, and
`byte_source`, with an optional free-text `note`. Digests must exactly match
`[0-9a-f]{64}` using `re.fullmatch`; sizes are nonnegative JSON integers, excluding
booleans. Filenames are relative POSIX metadata only, never filesystem paths.
Absolute paths, empty/dot/parent components, backslashes, drive/ADS prefixes,
control/format characters, Windows device names, trailing dots/spaces, and Windows
reserved punctuation are refused. Names must be unique after NFC normalization
and case folding. One digest can have multiple logical names, but one size only.
No generic legal attestation is requested or accepted.

| Declaration or condition | Result |
| --- | --- |
| No files, any valid declared tier, with or without public-origin references | Commit metadata immediately |
| `byte_source: user_provided` | Accept as asserted, including when metadata cites open origins |
| `byte_source: unknown` | Accept as unverified; a derivative may use this with an asserted note |
| `byte_source: public_origin_download` | `public_origin_download_refused` |
| Missing `byte_source` | `byte_source_required` |
| Other `byte_source` values | `invalid_manifest` |
| Envelope/file `fetch`, `mirror`, `source_url`, `download_url`, or `locator` | `fetch_or_mirror_refused` |
| Descriptor top-level fetch/mirror request | `fetch_or_mirror_refused` |
| Files with explicit tier `public` or `anonymized` | `tier_unsupported_for_bytes` |
| Omitted tier with files | Accept, preserve omission |
| Client ownership/stamp/evidence fields, `generation`, origin `alive`/`last_checked` (including null) | `server_owned_field` |
| Other unknown fields | `unknown_field` |

Existing schema-defined fields inside descriptor retrieval plans and origin
locators remain inert metadata. Refusals above occur before a pending manifest,
directory, or payload is created. Intake requires strict UTF-8 without a BOM;
UTF-16, invalid JSON, duplicate JSON keys, nonfinite
numbers, non-JSON Python objects, and malformed descriptors are refused.

## Offline operations

The local operator constructs `StoreContext(project_id, principal_id)` from a
trusted source. This object supplies scope and stamps; **it does not authenticate
or authorize anyone**. Never construct it from unverified submission fields.
`provenance.contributor` is separate free-text metadata.

1. Construct `PrivateStore(absolute_store_path)` with an explicit location outside
   any Git working tree and outside `catalog`/`datasets` path components. Private
   payload sources must also be outside the repository. The store takes byte
   iterables, never source filesystem paths.
2. Call `begin(context, manifest_dict_or_json_bytes)`. Metadata-only submissions
   return `created` with a record immediately. File submissions return `pending`,
   a server-generated random `submission_id`, and a content-derived `record_id`.
3. Call `put_file(context, submission_id, declared_sha256, iterable_of_bytes)` for
   each distinct declared digest. Unknown/foreign submissions and undeclared
   digests do not consume the iterable. Size and digest are checked while
   streaming, including on deduplicated retries. There is no Content-Length to
   trust in this API; every chunk is counted.
4. Call `commit(context, submission_id)`. All blobs must be present and sound;
   the immutable record is written last. Missing pending blobs return
   `missing_blob` (409) and leave the submission pending.

`get_record`, `list_records`, and `read_file` operate only on committed records in
the supplied project. Pending submissions and unpublished temporary files are
never listed. Unknown/foreign resources return `not_found` (404). Read operations
and construction never create directories or locks. A committed record with
missing/damaged bytes or invalid metadata returns `corrupt_record` (409); it is
never served or silently repaired. Listing fails explicitly if a committed record
is corrupt. `read_file` returns opaque bytes in memory. The `open_file` context
manager verifies and opens an anchored inode for bounded-memory reads; callers
must close the context on every path. This is not an immutable snapshot: a local
writer can modify the inode after verification and change subsequently streamed
bytes. Clients must verify the declared digest for end-to-end integrity; a later
store read freshly detects any persistent damage. The HTTP service uses `open_file` and
never materializes the complete payload. Historical records remain
readable after intake limits are lowered or the descriptor intake schema changes:
stored data is checked by record structure, fixed evidence labels, ownership,
digest/size format, and recomputed content hash, without rerunning intake rules.
Optional `max_metadata_bytes`/`max_records` read bounds refuse oversized metadata
with `response_too_large` before collecting an unbounded list. They are response
limits, not intake rules or a corruption verdict; the default trusted API
remains unbounded. Each successful read freshly verifies unique referenced blobs;
aliases are deduplicated within the operation, never across requests.

Records contain the submitted `descriptor`/`files`, fixed evidence labels,
`record_id`, `project_id`, `principal_id`, and UTC `submitted_at`. The stamps come
from the first accepted manifest, even if another principal retries or commits it.

## Identity and persistence

`record_id` is SHA-256 of the UTF-8 canonical submission envelope: object keys
sorted, compact separators, Unicode preserved, no NaN/Infinity. The submitted
descriptor and ordered file list, including assertions and optional notes,
participate; server stamps do not. This serialization is the Python store
contract, not a claim of RFC 8785 numeric canonicalization.

Identical retries return `already_present` with the first record and stamps.
Identical pending retries reuse the first server-generated submission ID. The
same descriptor `id` and declared `versions.content` with different content
returns `record_id_conflict` (409) against committed records only. Pending variants
do not reserve unpublished identities: a mistyped digest can be corrected with
the same id/version. Two variants can receive bytes; the first commit wins, and
the second commit conflicts under the project lock.
An undeclared content version is a distinct identity represented internally by
null; no `1.0.0` is inferred. A schema-protocol change alone does not bypass a
conflict at the same declared content version.

Storage uses:

```text
<root>/projects/<sha256-of-project-id>/
    .lock
    blobs/sha256/<first-two-hex>/<digest>
    pending/<server-generated-submission-id>.json
    pending_index/<record-id>.json
    records/<record-id>.json
```

Client names and raw project IDs never reach filesystem paths. Projects have
separate blob inodes, records, pending manifests, and locks, even for identical
record IDs and bytes. Deduplication occurs only within a project.

Commit may succeed without an upload for the new pending submission when all its
declared digests/sizes already exist in the same project. It verifies those blobs
and retains the newly submitted assertions. This applies to add-only principals
too; it is not a provenance or rights verification. Bytes in another project
cannot satisfy a commit. HTTP add-only receipts expose status and record ID,
while the trusted offline API still returns the full record and first stamps.

Writes use per-project `filelock` locks, exclusive temporary files, fsync, atomic
`os.replace`, and directory fsync. The lock file is opened relative to an anchored
project descriptor with no-follow checks, never through a mutable absolute path.
Project-lock acquisition has a 30-second timeout (`store_busy`, 503).
Existing sound blobs keep their first inode;
retries still consume and verify their submitted stream. POSIX descriptor-relative
IO with `O_NOFOLLOW`, directory checks, and `lstat`/no-follow scans rejects symlinks,
nonregular files, and hardlinks. Newly created directories/files use 0700/0600.
The root and shared `projects/` component are validated without scanning other
projects. Only the addressed project's tree is scanned on writes, so an unsafe
entry in B cannot block construction, reads, or writes for A. A pre-existing
group/world-writable root is refused. The operator must control the root and
exclude hostile local filesystem writers.

File uploads stream to a temporary file **outside the project lock**. A lease
(`flock` on the open temporary inode) prevents recovery or concurrent writers
from removing a live upload. Creation and lease acquisition occur together inside
the initial short project lock, closing the open-before-flock cleanup race. No
client body is received until that lock has been released. Size and digest are checked during streaming, then
the visible directory/inode and complete digest are rechecked under the project
lock before atomic publication. Directory and temporary-file symlink swaps fail
closed and never redirect writes to another project.

On restart, call `recover(context)` to remove orphan `.tmp-<32 lowercase hex>`
files under the project lock. Every authorized write also performs recovery;
live leased files are skipped. Process death releases the lease, so orphan files
can then be reclaimed. In particular, SIGTERM during a service upload can kill
the process before cleanup and leave an orphan until recovery or the next
authorized write. It does not publish a partial blob or invalidate the pending
manifest; the upload can be retried and committed after restart.
Pending manifests remain resumable after restart and are retained after commit
to allow concurrent/repeated upload and commit calls to complete idempotently.
Deletion, pending expiration, and garbage collection are deferred; failed or
abandoned submissions can retain manifests and unreferenced blobs. Operator
removal of committed blobs makes the associated record corrupt.

The per-content pending index lets retries find only their own pending manifest.
A broken pending manifest affects only addressed/identical submissions; unrelated
writes continue. Corrupt committed metadata can block writes because it could
conceal an identity conflict. Pending submissions created before the index was
introduced remain resumable by submission ID, but an identical new `begin` may
create another pending ID until a record is committed.

## Limits and remaining gates

`StoreLimits` defaults to a 1 MiB canonical manifest, 128 logical files, 64 MiB
per file, and 256 MiB per submission. A required disk floor of 2,147,483,648 bytes
cannot be lowered. Intake limits do not retroactively invalidate stored records.
Size limits return `request_too_large` (413); declared size/hash
mismatches return `size_mismatch`/`digest_mismatch`. A pending commit that reuses
an intact known digest with an
incorrect declared size returns `size_mismatch`; genuine committed-record/blob
damage still returns `corrupt_record`. Free space is checked before
writes and each streamed chunk. Floor failures and ENOSPC/EDQUOT during store IO
return `insufficient_storage` (507). Independent processes/projects share the
physical filesystem: these checks are not global space reservations against
unrelated concurrent disk usage. Interrupted writes never publish partial blobs
or records; an error after an atomic rename can be retried idempotently.

The implementation is tested on Linux. Windows is explicitly unsupported and
fails closed (`platform_unsupported`); Windows lstat containment is unverified.
There is no encryption, retention/deletion API, global quota, or paginated index.
Writes scan stored manifests for identity conflicts, and reads hash files to
detect corruption; large-store performance is not qualified.

The [service contract](PROJECT_SERVICE.md) records ASGI authorization, transport,
and real-loopback qualification separately. No external network, installation,
native build, or hosting change is part of this batch. The earlier private-store
WORK review returned REQUEST_CHANGES; the fixes and passing counterexamples need
independent final review and are not an acceptance decision.

## Isolated verification

Use the existing repository venv. Set all BLAS/OpenMP implementations to one
thread, disable optional pytest plugins, and keep synthetic stores outside Git.
The local environment has a Git marker under `/tmp`; use an isolated directory
under `/var/tmp` for pytest instead.

```bash
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 BLIS_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
.venv/bin/python -m pytest -q -o addopts='' \
  --basetemp=/var/tmp/nirs4all-datasets-private-store-check tests/test_private_store.py tests/test_private_store_review.py
.venv/bin/python -m pytest -q -o addopts='' -m 'not network' \
  --basetemp=/var/tmp/nirs4all-datasets-private-store-regression tests/test_schema.py tests/test_manifest.py
.venv/bin/python -m ruff check src/nirs4all_datasets/private_store.py tests/test_private_store.py tests/test_private_store_review.py
.venv/bin/python -m mypy --config-file pyproject.toml --follow-imports=silent src/nirs4all_datasets/private_store.py
```

On 2026-11-04 the revised store passed **160 focused tests**, including all seven
requested WORK-review regression cases, the forced N3 temp-create/flock race,
and stalled-stream/symlink races. Together with the existing schema/manifest
cases the earlier storage run passed **203 tests**. The supplied independent
private-store probe was also executed with the same thread settings; W1–W5 and
W13 now show the corrected behavior, all four eight-process upload races produce
one record, and the 12-process cold-root probe succeeds. Its scratch roots are
removed by the probe. Permanent regression tests and exact commands/environment
are in the service document; volatile reviewer scripts are not test dependencies.
The full repository suite was not run.

Tests cover sparse metadata, inert public-origin/retrieval references, provenance
refusals, malformed manifests/paths/digests, size/digest mismatches, symlinks and
nonregular files, corruption, disk floor/full-disk failures, restart recovery,
atomic publication, project isolation, idempotence/conflicts, eight writers in
threads and independent processes, and cross-project concurrency. A cold import
blocks HTTP clients, numerical/native acquisition, web, and access modules;
socket guards permit numeric loopback only and forbid DNS. Stdlib socket is used
by Python's existing package-metadata imports; no store networking is performed.
