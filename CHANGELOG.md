<!-- SPDX-License-Identifier: CECILL-2.1 OR AGPL-3.0-or-later -->
# Changelog

All notable changes to **nirs4all-datasets** are documented here. The format
follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); the public
surface is stable in shape but may still change before `1.0`.

## [Unreleased]

- Manage the catalog by origin database: a dataset is now the samples of one
  published record with all their variables. Upstream per-target leaves (the same
  spectra, one target each) and per-instrument leaves (the same samples, one block
  each) are composed by `consolidate.py` from the committed `consolidation.json`;
  `bootstrap` describes the composed leaf and skips its members. Spectra are matched
  only by their stored values and sources only by declared sample identity; conflicting
  measurements abort the composition, and members with different licences are never
  merged. This retires 72 task-view and duplicate entries and adds 16 databases, among
  them multi-source databases (UvA illicit drugs, five instruments; Recherche Data Gouv
  grapevine, three instruments; OSSL collections with vis-NIR and MIR; CABO v2
  reflectance and transmittance). EcoSIS databases gain the trait joins that only
  their per-target views carried (NGEE Arctic canopy, UW-BNL, NGEE Tropics Panama,
  Belgian dune grassland), and their origin recipes join every trait table.
- Fix the CABO 2018-2019 v2 reflectance resource being labelled absorbance, and the
  malaria target named `x` (it is the parasite load; the infection stage is now a
  variable of one database instead of two dataset ids).
- Cards report per-source sample coverage (`alignment.source_coverage`); dataset pages
  of multi-source databases show the coverage and one tab per source.
- `health-check --only` keeps the other datasets' probes instead of rewriting
  `catalog/health.json` with the selected ids alone.
- A keyless `Y.csv` paired to `M.csv` by row, with M's order confirmed by an X block,
  is the normal upstream layout and no longer emits a conversion or curation warning.
- Remove stale variable declarations that no data carries: `original_sample_id` from
  20 descriptors whose identity moved to `sample_id`, and the empty source columns
  (country, date, species…) of the five EcoSIS databases enriched in place.

## [0.3.18] - 2026-11-03

- Licensing metadata only, no code change: every published surface now declares the
  ecosystem dual license `CECILL-2.1 OR AGPL-3.0-or-later`. The Python extension and
  WASM binding crates (and so the npm `@nirs4all/datasets-wasm` package, previously
  published as MIT) carry the dual SPDX expression and ship the AGPL-3.0-or-later and
  CeCILL-2.1 texts; the R package declares `CeCILL-2.1 | AGPL (>= 3)` instead of
  `AGPL-3`; the MATLAB/MEX sources and the generated C header drop their stale MIT
  SPDX headers. `scripts/check_release_train.py` now fails on license drift in the
  binding and R manifests.

## [0.3.17] - 2026-11-03

- Align curated variable contracts with the descriptors: declared missing tokens,
  numeric sentinels and renamed source columns now reach the curated views, and
  predictors derived (transitively) from a declared target are excluded from the
  curated and consumer views. The processing hash covers the variable curation
  directives (type, role, unit, dependencies, explicit dialect overrides), so a
  changed contract invalidates the affected caches. Published curation mappings
  summarize invalid and censored values; per-observation detail stays in the local
  canonical mappings. A declared derivation resolves descriptor names before
  source-column aliases and is followed through variables that have no source
  column and from targets stored outside Y; the `curate` command writes the same
  sanitized reports, and anonymized cards mask the alignment identity narrative
  and key columns.
- Rebuild the 297 canonical caches and qualification cards from the verified
  inputs under the updated contracts, with English provenance and identity
  narratives. The 0.3.16 cards carried protocol-6 diagnostics migrated to
  protocol 7 without recomputing the raw kernels; every card now holds protocol-7
  values computed from the canonical data, so many PCA-based and shape metrics
  differ from 0.3.16.
- Delegate second-difference MAD roughness to nirs4all-methods
  (`SpectralNoiseProxy` through the generic C ABI, no Python numerical fallback).
  The new `methods` extra requires `nirs4all-methods>=1.3.11` (the first release
  with the bandwise outputs) and scikit-learn; without it the roughness metrics
  stay null with an explicit reason. The committed roughness profiles reproduce
  exactly from the published Methods 1.3.11 and 1.3.13 artifacts (319 source
  profiles, no mismatch); they still name the development library that produced
  them.
- Make the MATLAB/Octave release archive reproducible: the extended timestamps that
  `git archive` writes from the wall clock are dropped.
- Site: explain metrics (question-mark help in a responsive dialog), PCA and score
  interpretation, and the difference between source access and the redistribution
  tier; correct the spectral profiles, rank binary target classes by frequency and
  escape the home provenance heading once.
- Consume nirs4all-formats 0.2.14, which keeps delimited spectra with missing
  cells as NaN gaps, and nirs4all-io 0.2.14 (native spreadsheet reader, missing
  targets kept lossless as NaN). The raw-table summary uses IO only for delimited
  text, which is unchanged.

## [0.3.16] - 2026-10-29

- Honor explicitly reviewed numeric/categorical descriptor types over CSV storage
  schemas in curated views. UCPH API references remain numeric; categorical codes
  retain their spelling and immutable source tables remain available.
- Preserve underscore-containing numeric source codes as invalid tokens instead
  of treating Python digit separators as measured values.
- Advance the unified package and converter version so rebuilding detects the
  corrected curation recipe. Preserve the 0.3.15 tag and published artifacts.
- Include the Windows ARM64 and WebR build fixes merged after 0.3.15: honor the
  target triple, use LLVM unwind libraries for gnullvm, and link the actual
  Emscripten target output while retaining offline builds.
- Keep UCPH keyless Y row pairing explicitly assumed. The supplied converted
  source archive adds no independent original-MAT alignment proof.

## [0.3.11] - 2026-10-06

- Integrate the published 0.3.10 release history with main maintenance fixes.
- Align source builds with the published IO 0.2.6 / Formats 0.2.11 train and
  Data 0.2.13 prerequisite, preserving the IO 0.2 compatibility update.
- Seed self-contained R vendoring from the reviewed Cargo lock, retain the
  strict Rust 1.88 MSRV guard, and mirror deflate-only ZIP features.
- Run CI pytest as a Python module so source release-contract tests are collected.
- Preserve dataset content/catalogue versions and the C ABI 0.3.0. Existing
  0.3.10 tags and artifacts remain immutable.

## [0.3.10] - 2026-09-03

### Security

- Repin the optional raw-origin preparation path to nirs4all-formats 0.2.9,
  eliminating the vulnerable `quick-xml` dependency lines reported by
  `RUSTSEC-2026-0194` and `RUSTSEC-2026-0195` without changing runtime
  behavior or the IO 0.1.12 release-train pin.
- Synchronize the Python extra, Rust lockfiles, release contract, and R source
  package metadata with the secured Formats release.
- Upgrade the embedded Python binding to PyO3 0.29.2 and require maturin 1.14.1
  or newer, resolving `RUSTSEC-2025-0020` and `RUSTSEC-2026-0177` while
  preserving its JSON-string API and stable `abi3-py311` wheel contract.

## [0.3.9] - 2026-09-02

### Changed
- Align the Python, Rust, PyO3, WASM/npm, R, and citation package identities
  with the Datasets 0.3.9 V1 release train.
- Pin the executable release train to nirs4all-formats 0.2.8 and
  nirs4all-io 0.1.12 on every Python, Rust, lockfile, and R vendor surface.

### Fixed
- Use the canonical SPDX `CECILL-2.1` identifier and include both commercial
  license notices in Python source and wheel artifacts.

## [0.3.8] - 2026-07-10

### Fixed
- Allow the R-universe `rwasm` Cargo/rustc wrappers during R WebAssembly builds
  when they cannot report `--version`; native CRAN/source installs still require
  readable Cargo/rustc versions meeting the declared Rust floor.

### Tests
- Add configure/Makevars regression coverage for R-universe WebAssembly wrapper
  detection while preserving native rejection of unversioned tools.

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
