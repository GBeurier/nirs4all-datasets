<!-- SPDX-License-Identifier: CECILL-2.1 OR AGPL-3.0-or-later -->
# nirs4all-datasets binding specification (normative)

This is the binding contract for the Rust **dataset-acquisition core** of
`nirs4all-datasets`. It is adapted from
[`nirs4all-io/bindings/SPEC.md`](../../nirs4all-io/bindings/SPEC.md) (the C-ABI
discipline) and `nirs4all-formats` (the pyo3/maturin model), and is scoped by the
feasibility report [`migration_ABI_C.md`](../migration_ABI_C.md) (§§2, 5, 6).
PRs that violate a **MUST** here are rejected.

## 1. Scope and layers

This core does **only dataset *acquisition*** — it is not the analysis package.
Given the distributable catalog index, it: resolves a dataset id → its tier-sanitized
descriptor + pinned origin / DOI / `dataset_version` + per-file SHA-256 + Dataverse file-ids; fetches
the canonical Parquet (Dataverse / Zenodo / figshare / URL), redirect-safe;
retrieves declared raw origin resources when the catalog exposes an open route;
SHA-256-verifies pinned bytes; and caches them in the native platform cache. The scientific
*analysis* layer (`qualify`/card/site/`health`/`anonymize`/the catalog assembler)
stays in **pure Python** and is **never** ported across the ABI — it depends on
nirs4all + numpy/scipy/sklearn/matplotlib and runs once on the maintainer's
machine (`migration_ABI_C.md` §§2, 9).

The acquisition core exposes one engine through several language bindings. Two
layers:

- **Raw layer** — the stable C ABI (`n4ds_` prefix,
  [`crates/nirs4all-datasets-capi`](../crates/nirs4all-datasets-capi)) + the pyo3
  native module (`nirs4all_datasets._n4ds`, [`bindings/python`](python)).
  Hand-written FFI plumbing; conformance-tested. The cbindgen header is committed.
- **Idiomatic layer** — per-language ergonomics (Python dicts /
  R `list` / typed classes). Hand-written, shared, conformance-tested. No per-call
  codegen.

The C ABI surface is **strings (JSON) + filesystem paths**:
`resolve`, `fetch`, `retrieve_raw`, `prepare_raw`, `verify_cached`. **No opaque
scientific handles cross the C ABI** (`migration_ABI_C.md` §5, the nirs4all-io
`D-R7` rule): the host reads the verified Parquet **natively** with its own reader
(`pyarrow` / R `arrow` / MATLAB `parquetread` / `parquet-wasm`). Raw preparation
may write portable JSON artifacts decoded by Rust `nirs4all-formats` or summarized
by Rust `nirs4all-io`; dataset-specific canonical assembly remains recipe-owned. The returned
paths are **relative canonical paths** (including `canonical/dataset.json`) and the
returned `descriptor` is the neutral schema-2.0 metadata view (`sources`,
`variables`, `ids`, `splits`, `retrieval`) so the host can present and load the
dataset without importing `nirs4all_providers` or the Python `nirs4all_datasets`
analysis layer. This keeps the ABI tiny, stable, and binding-cheap.

## 2. Canonical-JSON contract (the wire format)

Every JSON that crosses any binding boundary — the index in, the resolved
contract / fetch status / verify report out — and every golden, MUST be the
canonical form. It is produced by the Rust core (`serde_json`) and mirrored by the
Python writer in
[`src/nirs4all_datasets/index.py`](../src/nirs4all_datasets/index.py)
(`build_index` → `catalog/index.json`):

- UTF-8, no BOM; non-ASCII emitted verbatim (NOT `\uXXXX`-escaped;
  `ensure_ascii=False`).
- Object keys sorted lexicographically by Unicode code point (`sort_keys=True`).
- Two-space pretty indent, `": "` after keys, one element per line.
- `\n` line endings; exactly one trailing `\n`.
- Finite numbers only — NaN/Inf never appear (the index carries only sizes,
  hashes, and string locators; the IR never emits non-finite numbers).

The workspace enables serde_json's `preserve_order` + `float_roundtrip` so *input*
object order is preserved on the way in, while the canonical *output* sorts keys
EXPLICITLY rather than relying on the map type. The index is **version-pinned**:
the committed `catalog/index.json` at a release tag — together with each entry's
`dataset_version` and every file's `sha256` — re-fetches the exact bytes of that
release. The bundled index MUST carry only the **tier-sanitized public
descriptor** (`public_descriptor`): anonymized variable names masked, identifying
free text removed — the index leaks nothing (`index.py`, `migration_ABI_C.md` §7).

### Index schema (the resolver contract)

`catalog/index.json` is `index` schema **1.0** (independent of the package version
and the dataset schema version). One entry per dataset id carries everything a
resolver in any language needs: `tier`; the Dataverse `instance` / `doi` /
`dataset_version` pin; the per-file download list (`name`, `relpath`,
`directory_label`, `sha256`, `size`, `file_id` — files matched by directory label
+ name, never bare basename, which would collide across `raw/` and
`canonical/sources/`); the `origins` a resolver may try
(`kind`/`mode`/`locator`/`access`); the first-class `retrieval` plan for open
raw repatriation or token/manual fallbacks; and the sanitized `descriptor`. `resolve`
MUST copy that descriptor into the resolved JSON unchanged. This is the non-Python
provider contract: R/WASM/Rust clients consume `catalog/index.json` directly rather
than linking to the Python provider package.

### Descriptor → IO package bridge

The resolved contract is also the neutral hand-off to `nirs4all-io` for hosts that
want an assembled `DatasetPackage` without importing the Python provider:

1. Call `resolve(index_json, dataset_id)` and `fetch(...)` / `verify_cached(...)`.
2. Treat the fetch result's dataset directory as the IO `base_dir`; every payload
   path comes from `files[].relpath`, not from hard-coded absolute paths.
3. Use `descriptor.ids`, `descriptor.sources`, `descriptor.variables`, and
   `descriptor.splits` for sample identity, source ids, target/metadata roles, and
   native split labels.
4. Read exact feature column labels from the verified Parquet schemas with the
   host's native Parquet reader (`arrow`, `parquet-wasm`, `parquet2`, MATLAB
   `parquetread`, etc.). The descriptor intentionally records source identity and
   roles, while the payload schema records the spectral axis labels.
5. Build a normal `nirs4all-io` `DatasetSpec` and materialize through that binding
   (`n4io_load_summary`, `assembleDataset`, Rust `nirs4all-io`, or pyo3
   `to_dataset_package`). Datasets does not own joins or package assembly.

The bounded fixture in
[`tests/goldens/nonpython_bridge`](../tests/goldens/nonpython_bridge) pins this:
Rust and WASM resolve the same descriptor-rich contract, and the Python contract
test derives the expected IO `DatasetSpec` from only the resolved JSON plus
host-read Parquet schemas.

## 3. Status and error model (C ABI)

- Every fallible C ABI call returns an `n4ds_status_t` (a `#[repr(C)]` enum;
  `N4DS_OK == 0`). Callers MUST check it. The non-OK codes are stable and
  semantic: `N4DS_ERR_INVALID_ARGUMENT (2)`, `N4DS_ERR_NOT_FOUND (3)` (id not in
  the index), `N4DS_ERR_TOKEN_REQUIRED (4)` (private/anonymized needs a Dataverse
  token), `N4DS_ERR_NOT_FETCHABLE (5)` (no DOI / no open canonical origin),
  `N4DS_ERR_CHECKSUM (6)` (download ≠ pinned SHA-256), `N4DS_ERR_HTTP (7)`,
  `N4DS_ERR_IO (8)`, `N4DS_ERR_ABI_MISMATCH (12)`,
  `N4DS_ERR_VERSION_INCOMPATIBLE (15)`, `N4DS_ERR_INTERNAL (255)`.
- On a non-OK status, the human-readable message lives in a **per-context error
  buffer**. Bindings copy it out **before** the next call on the same context.
- `n4ds_context_last_error(ctx)` returns a context-owned `const char*` (never
  NULL; empty string when no error or a NULL ctx). Bindings MUST NOT free it.
- On any fallible call the `*out` JSON pointer is set to NULL before work begins
  and is written only on `N4DS_OK`, so a caller that checks the status never reads
  a stale or partial pointer.

## 4. Memory ownership (never free across the boundary)

Ownership is symmetric: the caller frees what it allocated; the core frees what it
allocated. The only core-allocated outputs a caller receives ownership of are the
JSON strings returned by value (`n4ds_abi_version`, and the `*out` of `n4ds_resolve`
/ `n4ds_fetch` / `n4ds_retrieve_raw` / `n4ds_prepare_raw` / `n4ds_verify_cached`) and the opaque context. Each such string
MUST be released with `n4ds_string_free`; the context with `n4ds_context_destroy`.
The `const char*` from `n4ds_context_last_error` is context-owned and MUST NOT be
freed. **Never free a core pointer with the host allocator.**

## 5. Opaque handles

`n4ds_context_t` is a forward-declared opaque struct (it carries the per-context
error buffer). `n4ds_context_create` returns `N4DS_OK` and sets `*out`; on a NULL
`out` it returns `N4DS_ERR_INVALID_ARGUMENT`. `n4ds_context_destroy` is void and
no-ops on NULL. v0 exposes this one handle. No result handles (resolved/plan) and
**no scientific handles** are exposed — v0 returns canonical JSON by value, and
the host reads the verified Parquet natively (§1).

## 6. ABI versioning

- `n4ds_abi_version()` returns the ABI version string (owned; free with
  `n4ds_string_free`). The ABI version (`N4DS_ABI_VERSION` in
  [`crates/nirs4all-datasets-capi/src/lib.rs`](../crates/nirs4all-datasets-capi/src/lib.rs),
  currently `0.3.0`) is **independent of the crate semver** (`0.2.3`) —
  bump it only on an ABI change.
- Bindings MUST call `n4ds_check_abi_compatibility(header_major, header_minor)`
  before any other call and fail loudly on skew: the header MAJOR MUST equal the
  library MAJOR (`N4DS_ERR_ABI_MISMATCH`); the library MINOR MUST be `>=` the
  header MINOR (forward-compatible additive changes; otherwise
  `N4DS_ERR_VERSION_INCOMPATIBLE`).

## 7. Symbol governance

- The cbindgen header
  ([`crates/nirs4all-datasets-capi/include/nirs4all_datasets.h`](../crates/nirs4all-datasets-capi/include/nirs4all_datasets.h))
  is committed and regenerated by the capi `build.rs`.
- [`crates/nirs4all-datasets-capi/abi/expected_symbols_{linux,macos,windows}.txt`](../crates/nirs4all-datasets-capi/abi)
  snapshot the exported symbol set (the eleven `n4ds_*` symbols); the ABI-check CI
  ([`.github/workflows/abi-check.yml`](../.github/workflows/abi-check.yml)) diffs
  the *built* cdylib's actual symbols vs expected and **fails on drift**. Every
  exported symbol MUST start with `n4ds_`: enforced on Linux by a GNU ld version
  script
  ([`abi/version_script.map`](../crates/nirs4all-datasets-capi/abi/version_script.map),
  nodes `N4DS_1`/`N4DS_2`/`N4DS_3`, wired in `build.rs`) that makes everything else `local`, on
  macOS/Windows by Rust's default `#[no_mangle]`-only export, and on all three by
  a CI grep.
- A `cargo test` drift guard
  ([`crates/nirs4all-datasets-capi/tests/abi_surface.rs`](../crates/nirs4all-datasets-capi/tests/abi_surface.rs))
  cross-checks the canonical surface ↔ the three snapshots ↔ the generated header
  (every symbol declared, every symbol `n4ds_`-prefixed).
- A **forbidden-runtime-dependency audit** (CI `ldd`) ensures the cdylib does not
  link Python/R/BLAS/etc.
- **Windows**: Rust auto-exports `#[no_mangle]` symbols (no `.def` needed); a
  dumpbin-based MSVC CI leg diffs the surface.

The canonical C ABI surface is exactly these eleven symbols:

```
n4ds_abi_version            n4ds_check_abi_compatibility
n4ds_context_create         n4ds_context_destroy         n4ds_context_last_error
n4ds_string_free
n4ds_resolve                n4ds_fetch                   n4ds_verify_cached
n4ds_retrieve_raw           n4ds_prepare_raw
```

## 8. Per-language FFI policy (NOT one-size-fits-all)

The bindings mirror the feasibility report's per-binding rating
(`migration_ABI_C.md` §6); native bindings are **C-ABI-first**, Python is
**pyo3-native**, WASM is **wasm-bindgen-native**.

- **Python = pyo3-native** and **embedded** (formats/io model). The pyo3 extension
  ([`bindings/python/src/lib.rs`](python/src/lib.rs), crate
  `nirs4all-datasets-py`, lib `_n4ds`) is built by maturin **into** the
  `nirs4all-datasets` package as module `nirs4all_datasets._n4ds` — there is **no
  separate Python distribution**. It links the core crate directly and exposes
  `abi_version` / `resolve` / `fetch` / `retrieve_raw` / `prepare_raw` /
  `verify_cached`; `fetch` and `retrieve_raw` release the GIL for blocking network duration.
  `prepare_raw` releases the GIL for filesystem/decoder work. Its idiomatic layer
  ([`src/nirs4all_datasets/_acquire.py`](../src/nirs4all_datasets/_acquire.py))
  parses dicts ↔ JSON; errors map to the exceptions the legacy `access.py` raised
  (`KeyError` for an unknown id, `RuntimeError` for a missing token, `ValueError`
  for a not-fetchable contract).
- **R = C-ABI-first** (`extendr`/C shim over the C ABI; CRAN target — see
  `docs/dev/release_process.md`). v0 scope: the C-ABI JSON surface
  (`resolve`/`fetch`/`retrieve_raw`/`prepare_raw`/`verify_cached`); `resolve` returns
  the descriptor JSON so R code can inspect `sources`/`variables` before reading
  verified Parquet with R-native tooling. Rated *medium* (native-lib packaging,
  TLS/cert store, CRAN policy).
- **Octave / MATLAB = C-ABI-first** (MEX/oct over the C ABI; GitHub-Release zip).
  Rated *medium* (per-platform binary distribution).
- **WASM / JS = wasm-bindgen-native** over the core's `resolve` descriptor+download surface, plus
  fetch of **metadata + small public datasets only** (npm
  `@nirs4all/datasets-wasm`). **Caveat (`migration_ABI_C.md` §4):** Dataverse
  emits CORS only when the instance is configured to, the S3/CDN that serves the
  bytes needs its own bucket CORS, there is no real filesystem (→ OPFS/IndexedDB,
  bounded), and large files are impractical. WASM is realistic for metadata + small
  public datasets, or behind a first-party app/proxy that owns CORS + storage.

## 9. Token hygiene (load-bearing across every binding)

The Dataverse API token travels **only** in the `X-Dataverse-key` header — never
as a query param, never logged. A private/anonymized fetch does **not** replay the
token onto a cross-host signed S3/Swift redirect (the redirect is followed without
the key). This mirrors the policy the Python `access.py` and `config.py` already
enforce; every binding inherits it from the core. A token is only ever needed to
fetch a `private` / `anonymized` dataset; `public` datasets fetch open from the
origin with no token.

## 10. Conformance gates

- **Per-crate:** `cargo fmt --check`, `cargo clippy --workspace --all-targets -D
  warnings`, `cargo test --workspace`.
- **Python ≡ Rust JSON parity:** the Python `index.py` writer and the Rust core
  emit **byte-identical** canonical JSON for the same input (the index, and the
  resolved-contract round-trip).
- **Cross-binding behavioral parity:** the `n4ds` CLI is the **oracle** — native
  bindings (Python / R / Octave-MATLAB) MUST `resolve` / `verify_cached`
  identically to `n4ds` on the golden vectors. The WASM binding MUST match
  `n4ds resolve` and the shared SHA-256 vectors; it has no `verify_cached`
  surface because the browser target has no portable filesystem contract.
  Network `fetch` / `retrieve_raw` parity runs against the RDG/CIRAD **sandbox** under the
  `network` gate, with the injected-session fakes for the offline default
  (mirroring the Python tests' no-network policy).
- **ABI:** the symbol-snapshot diff + version script + forbidden-dep audit + the
  `n4ds_check_abi_compatibility` probe on load; an MSVC/Windows leg.
- **Import-boundary (load-bearing):** importing the Python acquisition path
  (`nirs4all_datasets._acquire` / `_n4ds`) MUST NOT import `nirs4all`. Acquisition
  is self-contained native code; only the *analysis* layer (qualify/card) lazily
  touches nirs4all, and that touch MUST stay lazy.
