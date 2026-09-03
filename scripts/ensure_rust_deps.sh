#!/usr/bin/env bash
# SPDX-License-Identifier: CECILL-2.1 OR AGPL-3.0-or-later
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

read_dependency_version() {
    local name="$1"
    local value
    value=$(sed -nE "/^${name}[[:space:]]*=/s/.*version[[:space:]]*=[[:space:]]*\"=?([^\"]+)\".*/\1/p" \
        "${ROOT}/Cargo.toml" | head -n1 || true)
    if [[ -z "${value}" ]]; then
        echo "error: cannot read the explicit ${name} version from ${ROOT}/Cargo.toml" >&2
        return 2
    fi
    printf '%s\n' "${value}"
}

read_workspace_version() {
    local dest="$1"
    awk '
        /^\[workspace\.package\]$/ { in_package = 1; next }
        in_package && /^\[/ { exit }
        in_package && /^version[[:space:]]*=/ {
            value = $0
            sub(/^[^=]*=[[:space:]]*"/, "", value)
            sub(/".*/, "", value)
            print value
            exit
        }
    ' "${dest}/Cargo.toml"
}

checkout_ref_if_needed() {
    local dest="$1"
    local ref="$2"
    local pinned_version="$3"
    local selected_ref=""
    if [[ "${ref}" == rc/* ]]; then
        selected_ref="${ref}"
    elif [[ "${ref}" == v[0-9]* ]]; then
        # A Datasets tag names this repository's release, not its siblings'.
        # Build it from the exact dependency tags declared in Cargo.toml; using
        # each sibling's moving default branch could silently compile different
        # source under Cargo's compatible-version requirement.
        selected_ref="v${pinned_version}"
    else
        return 0
    fi
    echo "  selecting ${selected_ref} in ${dest}"
    git -C "${dest}" fetch --depth 1 origin "${selected_ref}"
    git -C "${dest}" checkout --detach FETCH_HEAD
    if [[ "${ref}" == v[0-9]* ]]; then
        local actual_version
        actual_version=$(read_workspace_version "${dest}")
        if [[ "${actual_version}" != "${pinned_version}" ]]; then
            echo "error: ${dest}@${selected_ref} reports workspace version ${actual_version:-missing}; expected ${pinned_version}" >&2
            return 2
        fi
    fi
}

ensure_repo() {
    local name="$1"
    local url="$2"
    local alias="$3"
    local ref="$4"
    local pinned_version="$5"
    local dest="${PARENT}/${name}"
    if [[ -d "${dest}/.git" ]]; then
        echo "  found ${dest}"
        checkout_ref_if_needed "${dest}" "${ref}" "${pinned_version}"
        return 0
    fi
    if [[ -e "${dest}" ]]; then
        echo "error: ${dest} exists but is not a git checkout" >&2
        return 2
    fi
    if [[ -e "${PARENT}/${alias}/.git" ]]; then
        echo "  cloning local ${PARENT}/${alias} -> ${dest}"
        git clone "${PARENT}/${alias}" "${dest}"
        checkout_ref_if_needed "${dest}" "${ref}" "${pinned_version}"
        return 0
    fi
    echo "  cloning ${url} -> ${dest}"
    git clone --depth 1 "${url}" "${dest}"
    checkout_ref_if_needed "${dest}" "${ref}" "${pinned_version}"
}

REF="$(resolve_ref)"
FORMATS_VERSION="$(read_dependency_version nirs4all-formats)"
IO_VERSION="$(read_dependency_version nirs4all-io)"

ensure_repo "nirs4all-formats" "https://github.com/GBeurier/nirs4all-formats.git" "RC-v1-formats" "${REF}" "${FORMATS_VERSION}"
ensure_repo "nirs4all-io" "https://github.com/GBeurier/nirs4all-io.git" "RC-v1-io" "${REF}" "${IO_VERSION}"
