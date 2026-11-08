# Private project service

The optional `nirs4all_datasets.project_service` is a pure-ASGI adapter over
`private_store`, with no FastAPI, catalog, acquisition, IO, frontend, or hosting
integration. It performs no origin detection. Public-origin references and
retrieval plans remain inert assertions; integrity hashes establish nothing
about origin or rights. The [private-store contract](PRIVATE_STORE.md) applies.

The access leaf's WORK review accepts wheel SHA-256
`99a4a95b431d9afab3e6ef56e574607bf6d7864f487aae789fa7a80dd1e8e25c`.
The installed `nirs4all_access/__init__.py` was checked against the review's
`0eb5c21ee85b10de7cc36c1cc2af12fba52194d2e12441046082f30700540d90` pin.
Independent re-review verified N1–N5 and real CLI logging. The subsequent N6
requalification closed the admission and response-bounds findings but returned
REQUEST_CHANGES for N8: Ctrl-C during a stuck download. This revision fixes that
cancellation path and prevents error recovery from attempting a second HTTP
response after headers. Independent targeted recheck is required.
Passing tests here are implementation evidence, not final acceptance.

## Authentication and routes

The application lazily imports the shared leaf and loads a credential snapshot
using `load_credential_store`. It refuses startup with no active, unexpired
credential granting `datasets.read` or `datasets.add`, and calls
`require_secure_transport` at startup. Every protected request uses the leaf's
`parse_bearer` and `ProjectTokenVerifier.verify(service="datasets",
required_rights=[...])` before invoking ASGI `receive` or any store operation.

| Method | Route | Right |
| --- | --- | --- |
| GET | `/healthz` | Public, fixed `{"status":"ok"}` only |
| POST | `/v1/submissions` | `datasets.add` |
| PUT | `/v1/submissions/<submission_id>/files/<sha256>` | `datasets.add` |
| POST | `/v1/submissions/<submission_id>/commit` | `datasets.add` |
| GET | `/v1/records` | `datasets.read` |
| GET | `/v1/records/<record_id>` | `datasets.read` |
| GET | `/v1/records/<record_id>/files/<sha256>` | `datasets.read` |

Routes and methods are closed. Submission IDs match `[0-9a-f]{32}` and digests
match `[0-9a-f]{64}` with fullmatch. Unknown routes require a valid datasets
credential and then return 404; missing/revoked/expired credentials return 401,
wrong service or insufficient rights return 403, all before reading a body.
401 includes `WWW-Authenticate: Bearer`. WebSockets are refused. There is no
CORS, static-file route, administrative route, or arbitrary path endpoint.

Only one `Authorization: Bearer ...` header is accepted. Query parameters are
not accepted, including query tokens, and `X-*-Project` selectors are refused.
Ownership and the hashed project storage directory come only from the verified
principal. The same resource ID requested from another project returns 404;
listing returns only the caller's project. No endpoint accepts a store path.
At capacity the pre-lookup response is 503 for unknown and known resources alike;
authorization still runs first and returns 401/403 independently of load.

Clients must use project credentials sourced from `NIRS4ALL_PROJECT_TOKEN` or
a protected client `--token-file`, distinct from `NIRS4ALL_DATAVERSE_TOKEN`.
This batch provides the HTTP server, not a packaged client transport or client
CLI; existing HTTP clients supply the bearer header themselves. Raw client
tokens are never server command-line arguments. Credential issuance/storage is
owned by the shared leaf, not reimplemented here.

The verifier is a snapshot. Credential revocation/replacement takes effect when
the app restarts; expiry is checked on every request. The service returns access
error codes only, not leaf error details containing principal information.
It does not log authorization headers or enable Uvicorn access logs. Health and
errors expose no server paths, tokens, or tracebacks. Responses containing
submitted descriptors preserve their asserted strings as required by M1.

The actual CLI configures null handlers for the Uvicorn logger namespace before
protocol handlers are constructed, disables access logs, and sets `ws="none"`.
This suppresses raw HTTP/WebSocket request-URL diagnostics, including arbitrary
query values containing tokens. Rejecting query parameters inside ASGI alone is
not a logging safeguard. Real CLI tests send a valid bearer token as both a
literal and percent-encoded arbitrary query value in HTTP and WebSocket upgrade
attempts and require empty captured stdout/stderr. CLI protocol diagnostics are
deliberately discarded; an embedding server needs equivalent pre-app logging
configuration. The ASGI factory alone cannot configure its host's logging.

An add-only credential receives only `status` and `record_id` on create or
already-present record receipts. It never receives another principal's stamps
through these write responses. Returning full records requires `datasets.read`;
the offline trusted store API continues returning its full record.

## Manifest-first protocol and limits

1. POST an `application/json` manifest to `/v1/submissions`. Intake is strict
   UTF-8 without a BOM. All declaration/refusal rules run before a pending
   manifest or any payload is stored. Metadata-only submissions commit here.
2. For an accepted pending submission, PUT opaque raw bytes to the declared
   digest route. Foreign/unknown submissions and undeclared digests do not read
   the request body. No multipart staging or file-locator import exists.
3. POST an empty body to the commit route. All declared blobs must be sound;
   the immutable record is written last. Pending entries are not records.

If identical declared bytes already exist within this project, step 2 can be
omitted: commit revalidates the blobs and deduplicates them. This asserts neither
origin nor rights. Another project's bytes cannot satisfy the manifest.

`created` responses use 201, `pending` uses 202, and `already_present`/stored/read
responses use 200. Store refusals retain their stable codes and statuses. Missing
pending blobs and immutable identity conflicts return 409. Reads of corrupt
committed records return 409. EIO and other OS errors map to `storage_failure`
(500); ENOSPC/EDQUOT or the required 2,147,483,648-byte disk floor map to
`insufficient_storage` (507), without filesystem messages.
An intact known blob with an incorrect newly declared size returns 400
`size_mismatch`; it does not mark a sound committed record as corrupt.

### Admission for all store operations

Every authorized store route first acquires immediate global/per-project
admission, before receiving a body or submitting executor work. Defaults are
**16 operations globally, 4 per project**. Metadata creation, record reads,
listing, and commits use a dedicated **18-worker store executor**; uploads and
downloads retain their separate executors and additional budgets below. No store
operation uses asyncio's unbounded default-executor queue. Each admitted request
has at most one executor job in flight. Per-project limits leave global capacity
for other projects, and admitted jobs remain strictly below executor capacity.

Admission lasts through the response send. Excess gets immediate 503
`store_busy` with `Retry-After: 1`, before body consumption. Resets and repeated
ASGI cancellation cannot release a slot while its admitted thread still runs;
the worker is drained first. One project's stalled, heavy or resetting requests
therefore cannot create an unbounded queue of detached store jobs. Several
projects can jointly fill the global budget; this is bounded concurrent work,
not a distributed scheduler or a request-rate quota.

Fresh blob verification remains enabled on metadata reads and commits. There is
no cross-request verification cache and no skipped-integrity label presented as
verification. Repeated logical file aliases to the same physical digest are
hashed once within an operation; subsequent operations recheck bytes. The probe
at the default 256 MiB submission ceiling qualifies this admission behavior, not
general large-store throughput.

Actual body bytes are counted for every accepted frame, independent of absent
or incorrect Content-Length. An oversized advertised length is an early 413;
duplicate/malformed lengths are refused. Compressed request bodies are refused.
Manifest buffering is bounded by `max_manifest_bytes`; upload input is passed in
at most 64 KiB chunks through a worker-driven iterator, with no second disk spool.
The store checks digest and size, streams outside its project lock, and verifies
and publishes under the lock. The default total body-read deadline is 30 seconds
(408); disconnects and ASGI cancellation clean up upload temporaries and leases.
Upload bodies use a dedicated executor, separate from the store executor.
Their additional admission checks run after authentication and header checks, before
any body is read or executor job is submitted. Defaults are **8 global uploads,
2 per project**, with 10 dedicated workers. There is no admission queue: excess
requests immediately return 503 `store_busy`, without soliciting a body or
`100 Continue`. Per-project limits must stay below the global limit, which stays
below the executor's worker count. Uploads cannot consume store-executor threads;
the all-operation budget also bounds reads, writes and commits. Several
projects together can exhaust global admission and receive 503; clients retry
later. This is concurrent-transfer admission, not a request-rate quota.

Downloads use independent admission (**4 global, 1 per project**) and a separate
6-worker file-IO executor. The store verifies the record and anchored inode before
headers, then the service reads and sends one 64 KiB chunk at a time. It does not
call the materializing `read_file()` API. While awaiting a slow socket, it holds
neither an executor thread nor a whole-file buffer. A total **15-second send
deadline** includes preparation time; deadline/disconnect/cancellation closes the
file and releases admission. Failure after response start closes the partial
response rather than sending another status. A deadline before headers returns
408. Blocking filesystem calls must finish before their resources are released;
the send deadline cannot forcibly interrupt kernel IO.

The anchored inode is verified before headers, not snapshotted or continuously
rehashed while streaming. A local operator modifying that inode in place after
verification can change bytes delivered with status 200; the next store read
detects the damage. Clients needing end-to-end integrity must verify the declared
SHA-256. Excluding hostile local filesystem writers remains a storage prerequisite.

### JSON response bounds

All JSON replies have the same configurable **15-second send deadline** and are
emitted in at most 64 KiB chunks. Store-route replies retain operation admission
until sending ends, including slow JSON readers. The default response ceiling
is **2 MiB**, and listing additionally permits at most **100 records**. Listings
are not paginated: an over-limit list returns 413 `response_too_large`; request
individual known record IDs or configure a larger bounded ceiling. The store
checks record file sizes and cumulative bytes while reading, before loading an
unbounded list, and JSON encoding itself also enforces the ceiling.
Encoding runs on the event loop and can delay other requests with dense metadata;
the deadline bounds asynchronous sends, not synchronous JSON encoding. There is
no discovery of IDs beyond the list cap without raising the configured ceiling.

An oversized individual metadata response returns the same 413, not
`corrupt_record`. If a write has already succeeded but its full receipt would
exceed the JSON ceiling, it retains its success status and returns `status` and
`record_id` only. Limits never turn a committed write into a reported intake
failure. Authentication and overload errors are fixed small replies and also
have send deadlines. Historical files remain readable after intake limits are
reduced. Cache-Control is `no-store`; no range requests are implemented.
HTTP framing is enforced by the ASGI server: bytes beyond a falsely short HTTP
Content-Length are outside that framed request and cannot be counted by the app.

## Explicit local entrypoint

The optional `project-service` extra declares `nirs4all-access>=0.1,<0.2` and
`uvicorn>=0.30,<1` on the existing Python >=3.11 package. Base imports and the
offline store do not require either dependency. There is no editable-source
override for the access leaf: qualification uses the accepted installed wheel.
Dependency installation, lock refresh, wheel build, and publication were not run.

```bash
python -m nirs4all_datasets.project_service serve \
  --store /absolute/private/store \
  --credentials /absolute/private/project-credentials.json \
  --host 127.0.0.1 --port 8046
```

The console entrypoint is `n4a-datasets-project serve` when the updated package is
installed. Both paths call the same function. `--store` and `--credentials` are
required; no repository-relative default is used. CLI binding is restricted to
127.0.0.1, ::1, or localhost. `--body-timeout`, `--max-file-bytes`, and
`--max-manifest-bytes` configure request limits. Proxy headers are disabled.
`--upload-limit`, `--project-upload-limit`, `--download-limit`, and
`--project-download-limit` configure immediate admission; `--send-timeout`
configures the download deadline. Transfer executors are shut down at ASGI
lifespan shutdown; programmatic owners call `app.close()` after draining requests.
`--operation-limit` and `--project-operation-limit` configure all-operation
admission; `--max-json-bytes` and `--max-list-records` configure response bounds.
`--send-timeout` applies to JSON as well as file responses. The CLI sets
`timeout_graceful_shutdown` to **2 seconds**, configurable through
`--shutdown-timeout`. On cancellation, already-drained read handles close inline
even after executor shutdown, and cleanup failures cannot replace cancellation.
Response-start tracking prevents error recovery from sending a second status.
This bounds the tested stuck-client shutdown path independently of the send
timeout; it does not interrupt blocked kernel IO or external file locks.
SIGTERM can terminate the process before upload cleanup and leave an orphan
temporary file. A later authorized write or offline recovery reclaims it once
its lease is released; the pending manifest remains resumable.
Startup failures such as a port collision or invalid `WEB_CONCURRENCY` produce
only the fixed, path-free
`Unable to start project service.` message and a nonzero exit code. Runtime
protocol/access logging remains suppressed before the app.
The app factory also enforces the shared leaf's transport rule for externally
managed TLS/proxy configurations, but remote/TLS deployment was not exercised.
This batch provisions no host and starts no persistent service after tests.

## Exact qualification environment and commands

All tests use existing installations, one thread for every BLAS/OpenMP backend,
synthetic data outside Git, and no external network. Python is 3.11; Uvicorn
0.49.0 is already installed under `/home/delete/.local/lib/python3.11/site-packages`.
The accepted leaf comes from
`/tmp/n4access-fix-wheel.gwg6ngpa/env311/lib/python3.11/site-packages`;
Pydantic 2.13.4, filelock 4.2.4, and pytest 9.0.3 come from this repo's existing
venv. No other repository is placed on the import path.

```bash
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 BLIS_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
export PYTHONPATH=/home/delete/nirs4all/nirs4all-datasets/src:/tmp/n4access-fix-wheel.gwg6ngpa/env311/lib/python3.11/site-packages:/home/delete/nirs4all/nirs4all-datasets/.venv/lib/python3.11/site-packages
/usr/bin/python3.11 -B -m pytest -q -o addopts='' \
  --basetemp=/var/tmp/nirs4all-datasets-fairness-final \
  tests/test_project_service.py tests/test_project_service_admission.py tests/test_project_service_fairness.py
.venv/bin/python -m pytest -q -o addopts='' -m 'not network' \
  --basetemp=/var/tmp/nirs4all-datasets-final-storage-check \
  tests/test_private_store.py tests/test_private_store_review.py tests/test_schema.py tests/test_manifest.py
.venv/bin/python -m ruff check src/nirs4all_datasets/private_store.py \
  src/nirs4all_datasets/project_service.py tests/test_private_store.py \
  tests/test_private_store_review.py tests/test_project_service.py \
  tests/test_project_service_admission.py tests/test_project_service_fairness.py \
  tests/test_project_service_shutdown.py
.venv/bin/python -m mypy --config-file pyproject.toml --follow-imports=silent \
  src/nirs4all_datasets/private_store.py src/nirs4all_datasets/project_service.py
```

Service tests include direct-ASGI pre-body 401/403 probes on every route, inert
public origins, manifest refusals, strict project isolation, actual-body caps,
stream integrity/deadlines/disconnect/cancellation, safe storage-error handling,
revocation snapshots, and missing/inactive/nonregular credential stores. Real
Uvicorn loopback tests cover raw pre-body responses, chunked uploads and caps,
eight simultaneous writers, a stalled upload alongside a same-project write,
and a new CLI process after restart/revocation. Cold-import tests block access
and web dependencies while committing metadata offline.

Permanent regression coverage lives in the repository tests above. The fairness
suite drives 112 admitted/rejected reads, lists, commits and resets with controlled
heavy work; B reads/writes/uploads must finish within one second, and excess A
work must never enter an executor. It also covers non-reading JSON clients,
response refusal before loading a full list, JSON deadlines/cancellation, fresh
integrity checks, known-blob size mismatch, a port collision, and real CLI
shutdown with JSON/download/upload clients still alive. The raw CLI HTTP/WS
query-token test and the 64 MiB streaming/RSS regression remain included.

The independent reviewer's unchanged `p12b_readstarve.py` was also executed on
the actual CLI with A's 256 MiB record. Results (seconds):

| 112-request attack | B list | B write | B upload |
| --- | --- | --- | --- |
| Read-only GET record | 0.01 | 0.01 | 0.08 |
| Read-only GET list | 0.03 | 0.05 | 0.12 |
| Read-only GET record with immediate RST | 0.01 | 0.06 | 0.04 |
| Existing-record commit | 0.02 | 0.02 | 0.10 |

The non-reset bursts admitted 4 A requests and refused 108 with 503. The
unchanged shutdown probe measured SIGTERM exit in **2.21 s** with a stuck
download client still alive; JSON-list refusal exited in 0.2 s. Both probes
captured empty stdout/stderr. These supplied reviewer harnesses are supplemental
evidence, not repository test dependencies or permanent reproduction commands.
Implementation tests do not establish independent WORK acceptance.

## Constrained finalization after the shared ENOSPC pause

The shared filesystem briefly exhausted space during concurrent workspace work.
Source syntax and diff integrity were checked after space was restored. The
resume preserved all existing changes; its only subsequent edits were a source
comment correction and documentation cleanup. No network or broad stress replay,
installation, native build, subagent, or other-repository edit was performed.

Only one focused suite ran at a time, with BLAS/OpenMP at one thread, optional
pytest plugins and pytest cache writes disabled, fresh isolated basetemps, and explicit
guards rejecting IPv4/IPv6 socket operations and DNS. The guards permit only
local asyncio socketpairs. Execution used `pytest.main` in that guarded process:

| Post-resume check | Exact selection | Result |
| --- | --- | --- |
| Offline service | `tests/test_project_service.py tests/test_project_service_admission.py tests/test_project_service_fairness.py`, `-k 'not real'`, basetemp `/var/tmp/nirs4all-datasets-n6-resume-offline` | 105 passed, 15 deselected |
| Store regressions | `tests/test_private_store_review.py tests/test_schema.py tests/test_manifest.py`, basetemp `/var/tmp/nirs4all-datasets-n6-resume-storage` | 63 passed |
| Ruff | Both implementation modules and all five private-store/service test files | Passed |
| mypy | Both implementation modules, `--follow-imports=silent --cache-dir=/dev/null` | Passed |

Both pytest calls also used `-q -o addopts='' -p no:cacheprovider`. Namespaced task
scratch grew from 336,850,944 to 343,920,640 bytes, below the 1 GiB scratch limit.
Post-test free space was 7,746,629,632 bytes, above the 2,147,483,648-byte floor.
Including the existing repository mypy/pytest/Ruff caches, measured task scratch
was 362,770,432 bytes. No existing scratch or dirty work was removed.

Implementation SHA-256 pins (service updated by the targeted N8 fix below):

| File | SHA-256 |
| --- | --- |
| `private_store.py` | `b9b43f9cacb4e47f5b98e10c76b38d68850732aff99f65a229b2538d563bc499` |
| `project_service.py` | `98e8bfac410ecd105ad7e631430130b4b499a02c4ed466cc1d3189d74bb760e3` |

Before this pause, the full focused service selection passed **120 tests** and
the supplied p12b/shutdown probes produced the measurements recorded above. Those
real-network results are earlier evidence and were **not** revalidated during
this resume; the 15 real-network tests were deliberately deselected. The full
repository suite remains unrun. Independent final re-review is required.

## Targeted N8 Ctrl-C fix, 2026-11-04

The independent N6 requalification confirmed the admission, JSON bounds,
integrity and logging fixes, but reproduced Ctrl-C waiting for the send deadline.
Download cleanup had submitted a close operation after executor shutdown,
replacing cancellation with `RuntimeError` and attempting a second response.
Cleanup now closes the drained read handle inline, preserves cancellation even
if close fails, and tracks response start across both error handlers.
Invalid `WEB_CONCURRENCY=abc` now returns the fixed startup diagnostic, without
a traceback. The private-store implementation is unchanged in this revision.

Using the environment above, run these two suites **sequentially**:

```bash
/usr/bin/python3.11 -B -m pytest -q -s -o addopts='' -p no:cacheprovider \
  --basetemp=/var/tmp/nirs4all-datasets-n8-sigint-final \
  tests/test_project_service_shutdown.py
/usr/bin/python3.11 -B -m pytest -q -o addopts='' -p no:cacheprovider \
  --basetemp=/var/tmp/nirs4all-datasets-n8-regression \
  tests/test_project_service.py::test_authentication_and_rights_refuse_before_every_body \
  tests/test_project_service.py::test_foreign_resources_are_404_and_ids_are_independent \
  tests/test_project_service.py::test_response_disconnect_does_not_start_a_second_response \
  tests/test_project_service.py::test_total_body_deadline_cleans_upload \
  tests/test_project_service.py::test_cancelled_asgi_upload_releases_temp_lease_and_worker \
  tests/test_project_service.py::test_health_has_no_paths_tokens_or_body_reads \
  tests/test_project_service_admission.py::test_n2_streaming_deadline_admission_and_cleanup \
  tests/test_project_service_admission.py::test_n2_failed_download_start_never_attempts_second_start \
  tests/test_project_service_admission.py::test_real_cli_http_and_websocket_arbitrary_query_values_never_log_bearer \
  tests/test_project_service_fairness.py::test_n7_json_admission_send_deadline_and_cleanup \
  tests/test_project_service_fairness.py::test_n8_real_cli_graceful_shutdown_is_bounded_with_client_alive \
  tests/test_project_service_fairness.py::test_n9_real_cli_port_collision_reports_fixed_path_free_failure
```

Results: **7 passed in 4.92 s**, then **45 passed in 6.27 s**. The first suite
uses an 8 MiB fixture and real CLI subprocesses. With `--send-timeout 60`, one
SIGINT and a client still not reading, exit took **0.72 s** for a 0.5-second
shutdown limit and **2.22 s** for the default 2-second limit. Both captured
stdout/stderr pairs were empty. Unit probes preserve the original cancellation
after pool shutdown (including injected close failure), release admission and
file handles, and prohibit a second response on cleanup or JSON-send failure.
The second suite repeats the real CLI arbitrary-query bearer-token HTTP/WS log
test, deadline/cancellation, project isolation and existing shutdown regressions.

Ruff passed with `--no-cache` on both implementation modules and all six
private-store/service test files. Mypy passed on both modules with
`--follow-imports=silent --cache-dir=/dev/null`. The same accepted wheel pin above
was rechecked. No broad stress probes, native builds, installations, external
network or full repository suite were run for this narrow revision.
Namespaced synthetic scratch plus existing repository tool caches measured
411,512,832 bytes; sampled free space remained above the required 2,684,354,560
bytes (latest sample 7,174,246,400 bytes). Existing work was preserved.
Independent targeted recheck remains required; these results do not establish
WORK acceptance.

## Remaining limits

Independent final WORK review is required. Full repository tests, Windows,
remote/TLS/proxy deployment, wheel packaging/installation, and other dependency
versions were not qualified. IPv6/localhost binding, slow headers, and multi-worker
coordination are not qualified. Admission is per app instance/process; it is not
a distributed limit. Deletion, pending expiration, garbage collection,
encryption, global disk reservations, rate limiting, and large-store performance
remain deferred. The storage root must be controlled by the operator. Limits
are not reservations against unrelated concurrent filesystem use. Server stamps
are outside the content hash and are not tamper-evident against local operators.
No origin or legal-rights verification is claimed.

In-progress filesystem IO and external file locks cannot be forcibly interrupted
by an ASGI timeout; admitted work is drained rather than detached. The graceful
limit bounds waiting for clients/tasks, not arbitrary stuck kernel IO. The
shutdown probe still observed transport sockets outliving a send deadline (8
descriptors before 12 stopped readers, 19 afterward, returning to 7 after peers
closed). Application response buffers/files are released, but TCP/transport
buffers and descriptors can persist until the peer or server closes. A 64 MiB
download below roughly 4.3 MiB/s cannot finish within the default 15-second total
deadline; configure `--send-timeout` for slower readers. There is no range resume.
