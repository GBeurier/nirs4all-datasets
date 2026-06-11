#!/usr/bin/env bash
# SPDX-License-Identifier: MIT
# Build the n4ds MEX and smoke-test it with Octave. MATLAB users run build.m + smoke.m
# the same way. SKIPs (exit 0) if octave is absent, so this is a no-op off-CI; the
# release-matlab / octave CI leg provides octave.
set -euo pipefail

ds_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
export PATH="${HOME}/.cargo/bin:${PATH}"

if ! command -v octave >/dev/null 2>&1; then
  echo "SKIP: octave not found; MATLAB/Octave binding smoke not run."
  exit 0
fi

echo ">> building nirs4all-datasets-capi (release)"
( cd "${ds_root}" && cargo build -q -p nirs4all-datasets-capi --release )

export N4DS_INCLUDE="${ds_root}/crates/nirs4all-datasets-capi/include"
export N4DS_CAPI_DIR="${ds_root}/target/release"

cd "${ds_root}/bindings/matlab"
echo ">> mex build"
octave --no-gui --norc --eval "build"
echo ">> smoke"
octave --no-gui --norc --path "$(pwd)" --eval "run('smoke.m')"
