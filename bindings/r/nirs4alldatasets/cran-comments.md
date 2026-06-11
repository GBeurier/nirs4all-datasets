<!-- SPDX-License-Identifier: MIT -->
# cran-comments.md — nirs4alldatasets

Maintainer: Gregory Beurier (CIRAD) <beurier@cirad.fr>

> **TEMPLATE — not yet CRAN-ready.** This package is the R binding of
> `nirs4all-datasets`, a Rust-first dataset-**acquisition** core for the nirs4all
> ecosystem. The R binding is a thin **C shim** (`src/n4ds.c`) that links the
> **prebuilt** `nirs4all-datasets-capi` shared library
> (`libnirs4all_datasets_capi`) via the `N4DS_INCLUDE` / `N4DS_CAPI_DIR`
> environment variables (see `src/Makevars`).

## Honest CRAN-self-containment note (follow-up tracked)

In its current form this package is **NOT CRAN-submittable**: CRAN's build farm has
no prebuilt `libnirs4all_datasets_capi`, and the package does not vendor or compile
the Rust core at install time. The tarball produced by `release-r.yml`
(`nirs4alldatasets_<version>.tar.gz`) is therefore an **R-universe / GitHub-Release
asset only** — the exact same model as the sibling `nirs4all-io` R binding.

A CRAN-submittable variant requires reworking the binding to **bundle and compile
the Rust core offline at install time**, mirroring the `nirs4all-formats`
`./configure` vendor-mode tarball:

1. a `./configure` that copies the `crates/nirs4all-datasets-core` +
   `nirs4all-datasets-capi` sources into `src/rust/vendored/`, runs `cargo vendor`
   on the crates.io dependencies, and compresses them to `src/rust/vendor.tar.xz`
   (shipped in the tarball; the extracted `vendor/` is `.Rbuildignore`d);
2. a `src/Makevars` that extracts `vendor.tar.xz` and runs
   `cargo build --release --offline` with inline
   `--config source.crates-io.replace-with=…` (no hidden `.cargo/` dir), then prunes
   build artefacts post-link;
3. `SystemRequirements: Cargo (rustc)`, a `Makevars.win`/`Makevars.ucrt` for the
   Rtools mingw toolchain, and the `-lgcc` panic-unwind shim.

The `ureq` + `rustls` networking stack the core uses links the platform TLS roots;
the vendored build must keep that offline-reproducible. That rework is a tracked
follow-up; until it lands, the R binding ships via R-universe / GitHub Releases.

## Test environments

* Local: Ubuntu 22.04, R 4.6.0, rustc 1.95.0 — `R CMD INSTALL` + `tests/smoke.R`
  against the cargo-built `libnirs4all_datasets_capi.so` (see
  `bindings/r/build_and_test.sh`).
* CI (`.github/workflows/release-r.yml`): Linux release + devel, macOS arm64,
  Windows release (Rtools mingw, x86_64-pc-windows-gnu staticlib).

## R CMD check

`NeedsCompilation: yes`. Expected NOTE on a clean machine: a `SystemRequirements:
Cargo` note (the Rust toolchain is required to build the core) — documented above.
No network access happens during `R CMD check`; the smoke test is fully offline
(resolve / verify_cached / abi_version). The actual byte download is exercised only
by an explicit, network-gated integration test, never in `R CMD check`.
