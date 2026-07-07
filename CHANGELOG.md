<!-- SPDX-License-Identifier: MIT -->
# Changelog

All notable changes to **nirs4all-datasets** are documented here. The format
follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); the public
surface is stable in shape but may still change before `1.0`.

## [0.3.5] - 2026-07-07

### Added
- Cover the dataset assembled bridge to `nirs4all-io` with a focused regression test.

### Changed
- Require `nirs4all-io >=0.1.7` for the optional IO bridge so published builds follow the current IO release train.
- Align WASM binding lock metadata with the current release train.
- Refresh the Dataverse retrieval audit while the seven pending datasets remain intentionally absent.

## [0.3.4] - 2026-07-06

### Fixed
- Harden R-universe source builds by vendoring the dataset reader workspaces and making fallback
  clone/fetch cleanup deterministic.

## [0.3.2] - 2026-07-03

Consolidates the 0.3.0 (2026-06-29) → 0.3.2 (2026-07-03) releases. Headline: reference datasets
now flow through `nirs4all-io` instead of being re-read here.

### Added
- Bridge reference datasets to `nirs4all-io`; expose a neutral descriptor in native `resolve`.
- Cross-language raw acquisition with CI-reproducible raw manifests.

### Fixed
- Drop native bzip2 from the C ABI surface.
- Guard the dataset package bridge; add canonical dataset SEO metadata on the site.

### Tests
- Cover IO loading of reference datasets; anonymized IO spec guard; non-python IO bridge contract;
  R-binding datasets↔io smoke + delimiter coverage; hermetic acquire stub.

## [0.2.3] - 2026-06-23

### Fixed

- **R binding (`nirs4alldatasets`) — macOS CRAN install failure.** The published
  `0.2.0` failed `R CMD check` with *"Installation failed"* on all four macOS
  flavors (r-release / r-oldrel × macOS-arm64 / x86_64) while Linux and Windows
  were OK. Cause: CRAN's macOS builders run `R CMD INSTALL` with a `PATH` that
  excludes the rustup `~/.cargo/bin`, so the `command -v cargo` guard in
  `src/Makevars` failed and aborted the install before any compilation (the
  Linux/Windows farms — and the GitHub Actions runners — have cargo on `PATH`, so
  the regression was invisible to CI). `src/Makevars` now appends
  `$(HOME)/.cargo/bin` to `PATH`, the pattern the sibling `dag-ml-data` R binding
  already uses. Resubmitted to CRAN as `0.2.3` to clear the 0.2.0 check ERRORs
  before their 2026-07-03 fix-by deadline.

## [0.2.2] - 2026-06-16

### Fixed

- **Packaging (PEP 639).** Declare `license-files` so the sdist bundles `LICENSE`.

## [0.2.1] - 2026-06-16

### Added

- Interactive dataset **property explorer** on the static site (fixed chart axes,
  Pages build).
- **ReadTheDocs / Sphinx** documentation set (getting-started, catalog,
  installation, ecosystem cross-links).

### Changed

- Adopt the new **nirs4all brand kit** (icon, logo, favicon, social/OG card).
- **R binding:** correct the CRAN maintainer email to `gregory.beurier@cirad.fr`
  and apply the Windows CRAN install fix (empty `CARGO_LINKER`).

## [0.2.0] - 2026-06-12

First release cut (from the `0.2.0-alpha.1` line). Version synced across every
binding manifest by `scripts/bump_version.sh --bump 0.2.0`.

### Changed

- **R binding (`nirs4alldatasets`) is now CRAN-self-contained.** Reworked from a
  C shim over a **prebuilt** `libnirs4all_datasets_capi` cdylib (linked via
  `N4DS_INCLUDE` / `N4DS_CAPI_DIR`, not installable on CRAN's farm) into a
  vendored, offline-compiled static-library build mirroring the proven
  `nirs4all-io` / `nirs4all-formats` pattern:
  - a `configure` (`N4DS_R_VENDOR=1`) copies the workspace crates
    (`nirs4all-datasets-core`, `nirs4all-datasets-capi`) into `src/rust/vendored/`,
    emits a self-contained `src/rust/Cargo.toml`, copies the committed C ABI header
    next to the shim, and `cargo vendor`s the crates.io closure into
    `src/rust/vendor.tar.xz` — dropping the test-only / `cbindgen` build deps and
    pruning the never-linked Windows import-library blobs (~76 MB) to keep the
    source tarball at ~9.4 MB (under CRAN's 10 MB cap);
  - `src/Makevars(.win)` extract the vendor archive and `cargo build -p
    nirs4all-datasets-capi --release --offline` the staticlib, then link it into
    `nirs4alldatasets.{so,dll}` by exact path, with a build-local `CARGO_HOME` /
    `CARGO_TARGET_DIR` (never `~/.cargo`), `-j 2`, a post-link `rust_clean`, and —
    on Windows — relocation of the cargo dirs to a short `$TMPDIR` path to dodge the
    260-char `MAX_PATH` limit and a `-lgcc` (staticlib-only) link;
  - `DESCRIPTION` declares `SystemRequirements: Cargo (Rust toolchain), rustc`,
    `License: MIT + file LICENSE`, ships `man/*.Rd`, and `release-r.yml` runs the
    full `R CMD check --as-cran` matrix (Linux release/devel, macOS arm64, Windows).
  `R CMD check --as-cran` is clean (0 ERRORs / 0 WARNINGs).

## [0.2.0-alpha.1] - 2026-06-12

The dataset *download* moves into a Rust acquisition core behind a stable `n4ds_`
C ABI, published like the rest of the nirs4all ecosystem (Rust / Python / R /
Octave-MATLAB / WASM). The scientific *analysis* layer (qualify / card / site /
health) stays in pure Python. See [`migration_ABI_C.md`](migration_ABI_C.md) for
the feasibility report this implements and [`bindings/SPEC.md`](bindings/SPEC.md)
for the normative binding contract.

### Added

- **Distributable catalog index (`catalog/index.json`, index schema 1.0).** One
  JSON file, derived from the git-tracked descriptors + manifests, carrying
  everything a resolver in any language needs to turn a dataset id into a
  complete, version-pinned download contract: `tier`; the Dataverse `instance` /
  `doi` / `dataset_version` pin; the per-file list (`name`, `relpath`,
  `directory_label`, `sha256`, `size`, `file_id`); the `origins`; and the
  **tier-sanitized public descriptor** (so the bundled index can never leak an
  anonymized identity). Serialized in the cross-binding canonical-JSON form (UTF-8,
  keys sorted by code point, two-space indent, `\n` endings, one trailing newline)
  so the Rust core and the Python writer agree byte-for-byte
  (`src/nirs4all_datasets/index.py`). It is version-pinned — the committed file at
  a release tag re-fetches the exact bytes of that release — and independently
  fixes standalone `pip install` use of `get()`.
- **Rust dataset-acquisition core** (`crates/nirs4all-datasets-core`,
  `nirs4all-datasets-capi`, `nirs4all-datasets-cli` — workspace at
  `0.2.0-alpha.1`, MIT). Pure-Rust I/O + integrity (no scientific stack): resolve
  a dataset id against the index → DOI/version-pinned origin resolution (Dataverse
  / Zenodo / figshare / URL) → redirect-safe download (the `X-Dataverse-key` never
  follows a cross-host signed-storage redirect) → streaming SHA-256 verification
  against the index → atomic write + pooch-style OS cache. The `n4ds` CLI binary is
  the cross-binding parity oracle.
- **`n4ds_` C ABI (v0, JSON in / JSON out).** `n4ds_resolve` (index + id → resolved
  contract), `n4ds_fetch` (resolved + opts → fetch status), `n4ds_verify_cached`
  (offline re-verify of a cached dir → report), plus `n4ds_abi_version`,
  `n4ds_check_abi_compatibility`, `n4ds_context_create` / `_destroy` /
  `_last_error`, and `n4ds_string_free`. A `#[repr(C)]` `n4ds_status_t`
  (`N4DS_OK == 0`) with semantic codes (not-found / token-required /
  not-fetchable / checksum / http / io / abi-mismatch). Per-context error buffer;
  the caller frees core strings with `n4ds_string_free` and never frees a core
  pointer with the host allocator. **No arrays and no scientific handles cross the
  boundary** — only JSON + relative canonical paths (including
  `canonical/dataset.json`); the host reads the verified Parquet natively. The ABI
  version (`0.1.0`) is independent of the crate semver.
- **Symbol governance.** A committed cbindgen header
  (`crates/nirs4all-datasets-capi/include/nirs4all_datasets.h`), per-platform ABI
  snapshots (`abi/expected_symbols_{linux,macos,windows}.txt`), a GNU ld version
  script (`abi/version_script.map`, node `N4DS_1`) that localizes everything but
  `n4ds_*`, a `cargo test` drift guard (`tests/abi_surface.rs`) cross-checking
  surface ↔ snapshots ↔ header, and the `abi-check` / `version-sync` CI plumbing.
- **Embedded Python native core.** A pyo3 extension (`bindings/python`, crate
  `nirs4all-datasets-py`, lib `_n4ds`) built by maturin **into** the
  `nirs4all-datasets` package as `nirs4all_datasets._n4ds` — there is **no separate
  Python distribution**. `pip install nirs4all-datasets` now ships the pure-Python
  analysis layer **and** the native acquisition core together (the bundled
  `catalog/index.json` rides in the wheel). `fetch` releases the GIL for the
  blocking network duration; errors map to the exceptions the old `access.py`
  raised. A thin `nirs4all_datasets._acquire` wraps the JSON boundary as dicts.
- **R / Octave-MATLAB / WASM bindings.** R (`nirs4alldatasets`, C shim over the C
  ABI, R-universe + GitHub Release; CRAN is a deferred self-containment follow-up).
  Octave/MATLAB (MEX/oct over the C ABI, GitHub-Release zip). WASM/JS
  (`@nirs4all/datasets-wasm`, wasm-bindgen over the core's resolve surface) —
  **scoped to metadata + small public datasets** per the feasibility report
  (Dataverse per-instance CORS, no real browser filesystem, large files
  impractical).
- **Release + governance docs.** [`bindings/SPEC.md`](bindings/SPEC.md) (the
  normative binding contract) and [`docs/dev/release_process.md`](docs/dev/release_process.md)
  (the maintainer release guide: version SoT table, binding→registry table,
  pre-release gates, the tag→workflow flow, and the PyPI / npm / CRAN one-time
  setup).

### Changed

- **`access.py` is now a thin façade over the native core.** It owns only the
  *policy* around acquisition — the local-first short-circuit, the token gate (a
  private/anonymized fetch is refused before any network without a token), the
  actionable "where do the bytes live" error, and wrapping the result as a
  `NirsDataset`. The download itself (DOI/version-pinned resolution, the
  redirect-safe Dataverse fetch, streaming SHA-256 verification, the pooch-style
  cache) is delegated to the Rust core through `_acquire`.

### Removed

- **The `pooch` / `requests`-based dataset download path.** The pure-Python public
  DOI→URL resolution + cache (previously delegated to `pooch`) and the manual
  `requests` Dataverse Access fetch are gone from the consumer `get()` path;
  acquisition is the native core. `requests` remains a dependency only for the
  maintainer-side Dataverse **publish** path and the origin **health** probe — not
  for downloading datasets.
