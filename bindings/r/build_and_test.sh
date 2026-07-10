#!/usr/bin/env bash
# SPDX-License-Identifier: CECILL-2.1 OR AGPL-3.0-or-later
# Local dev helper: vendor the Rust core into the R package, install it from the
# self-contained tree (offline staticlib build), and run the smoke test. This is
# the SAME path CRAN / R-universe use — there is no prebuilt cdylib and no
# N4DS_CAPI_DIR anymore (the package vendors + compiles its own staticlib).
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"   # bindings/r
pkg_dir="${here}/nirs4alldatasets"
export PATH="${HOME}/.cargo/bin:${PATH}"

# 1. Vendor the workspace core crates + cargo-vendor every crates.io dep into
#    bindings/r/nirs4alldatasets/src/rust/ (needs the repo crates/ + network, like
#    the CI prep). The configure auto-detects mode: N4DS_R_VENDOR=1 forces a fresh
#    vendor from the checkout's crates/.
echo ">> N4DS_R_VENDOR=1 ./configure (vendoring the Rust core)"
( cd "${pkg_dir}" && N4DS_R_VENDOR=1 ./configure )

# Force a clean compile so a stale/foreign-arch object is never reused.
rm -f "${pkg_dir}/src/"*.o "${pkg_dir}/src/"*.so "${pkg_dir}/src/"*.dll

lib="${install_lib:-$(mktemp -d)}"
echo ">> R CMD INSTALL -> ${lib} (offline staticlib build via src/Makevars)"
R CMD INSTALL --no-multiarch --library="${lib}" "${pkg_dir}"

echo ">> smoke"
R_LIBS_USER="${lib}" Rscript "${pkg_dir}/tests/smoke.R"
