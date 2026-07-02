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

resolve_ref() {
    if [[ -n "${NIRS4ALL_SIBLING_REF:-}" ]]; then
        printf '%s\n' "${NIRS4ALL_SIBLING_REF}"
        return 0
    fi
    if [[ -n "${GITHUB_HEAD_REF:-}" ]]; then
        printf '%s\n' "${GITHUB_HEAD_REF}"
        return 0
    fi
    if [[ -n "${GITHUB_REF_NAME:-}" ]]; then
        printf '%s\n' "${GITHUB_REF_NAME}"
        return 0
    fi
    git -C "${ROOT}" symbolic-ref --quiet --short HEAD 2>/dev/null || true
}

checkout_ref_if_needed() {
    local dest="$1"
    local ref="$2"
    if [[ -z "${ref}" || "${ref}" != rc/* ]]; then
        return 0
    fi
    echo "  selecting ${ref} in ${dest}"
    git -C "${dest}" fetch --depth 1 origin "${ref}"
    git -C "${dest}" checkout --detach FETCH_HEAD
}

ensure_repo() {
    local name="$1"
    local url="$2"
    local alias="$3"
    local ref="$4"
    local dest="${PARENT}/${name}"
    if [[ -d "${dest}/.git" ]]; then
        echo "  found ${dest}"
        checkout_ref_if_needed "${dest}" "${ref}"
        return 0
    fi
    if [[ -e "${dest}" ]]; then
        echo "error: ${dest} exists but is not a git checkout" >&2
        return 2
    fi
    if [[ -e "${PARENT}/${alias}/.git" ]]; then
        echo "  cloning local ${PARENT}/${alias} -> ${dest}"
        git clone "${PARENT}/${alias}" "${dest}"
        checkout_ref_if_needed "${dest}" "${ref}"
        return 0
    fi
    echo "  cloning ${url} -> ${dest}"
    git clone --depth 1 "${url}" "${dest}"
    checkout_ref_if_needed "${dest}" "${ref}"
}

REF="$(resolve_ref)"

ensure_repo "nirs4all-formats" "https://github.com/GBeurier/nirs4all-formats.git" "RC-v1-formats" "${REF}"
ensure_repo "nirs4all-io" "https://github.com/GBeurier/nirs4all-io.git" "RC-v1-io" "${REF}"
