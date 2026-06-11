#!/usr/bin/env bash
# SPDX-License-Identifier: MIT
# Build the nirs4all-datasets-capi cdylib, install the R package against it, and run
# the smoke test. Self-contained: computes paths from the repo root. Set $PATH to
# include the Rust toolchain (cargo) and an R with a C compiler before running.
set -euo pipefail

ds_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
export PATH="${HOME}/.cargo/bin:${PATH}"
pkg_dir="${ds_root}/bindings/r/nirs4alldatasets"

# On Windows the R package is linked by Rtools' mingw-w64 gcc (gnu ABI), so the capi
# must be built with the matching x86_64-pc-windows-gnu toolchain (its ABI matches
# Rtools' mingw gcc). Build only the staticlib there (an `ar` archive, no linker), so
# rustc never tries to link the cdylib with -lgcc_eh (Rtools ships no libgcc_eh.a).
case "$(uname -s 2>/dev/null || echo unknown)" in
  MINGW*|MSYS*|CYGWIN*|Windows_NT)
    rust_target="x86_64-pc-windows-gnu"
    rustup target add "${rust_target}" >/dev/null 2>&1 || true
    capi_dir="${ds_root}/target/${rust_target}/release"
    echo ">> building nirs4all-datasets-capi staticlib (release, ${rust_target})"
    ( cd "${ds_root}" && cargo rustc -q -p nirs4all-datasets-capi --release --target "${rust_target}" --crate-type staticlib )
    ;;
  *)
    capi_dir="${ds_root}/target/release"
    echo ">> building nirs4all-datasets-capi (release)"
    ( cd "${ds_root}" && cargo build -q -p nirs4all-datasets-capi --release )
    ;;
esac

export N4DS_INCLUDE="${ds_root}/crates/nirs4all-datasets-capi/include"
export N4DS_CAPI_DIR="${capi_dir}"

# Force a clean compile so a stale/foreign-arch object is never reused.
rm -f "${pkg_dir}/src/"*.o "${pkg_dir}/src/"*.so "${pkg_dir}/src/"*.dll

lib="${install_lib:-$(mktemp -d)}"
echo ">> R CMD INSTALL -> ${lib}"
R CMD INSTALL --no-multiarch --library="${lib}" "${pkg_dir}"

echo ">> smoke"
R_LIBS_USER="${lib}" Rscript "${pkg_dir}/tests/smoke.R"
