#!/usr/bin/env bash
# SPDX-License-Identifier: MIT
#
# Ensure sibling Rust reader repos are present for local/CI builds.
# nirs4all-datasets keeps path+version dependencies so local development uses
# the checked-out sibling crates, while cargo publish can still resolve the
# version requirement from crates.io.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PARENT="$(cd "${ROOT}/.." && pwd)"

ensure_repo() {
    local name="$1"
    local url="$2"
    local dest="${PARENT}/${name}"
    if [[ -d "${dest}/.git" ]]; then
        echo "  found ${dest}"
        return 0
    fi
    if [[ -e "${dest}" ]]; then
        echo "error: ${dest} exists but is not a git checkout" >&2
        return 2
    fi
    echo "  cloning ${url} -> ${dest}"
    git clone --depth 1 "${url}" "${dest}"
}

ensure_repo "nirs4all-formats" "https://github.com/GBeurier/nirs4all-formats.git"
ensure_repo "nirs4all-io" "https://github.com/GBeurier/nirs4all-io.git"
