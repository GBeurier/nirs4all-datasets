#!/usr/bin/env bash
# SPDX-License-Identifier: CECILL-2.1 OR AGPL-3.0-or-later
#
# bump_version.sh — nirs4all-datasets version source-of-truth syncer.
#
# Reads the canonical workspace version from the root Cargo.toml
# ([workspace.package] version) and propagates it to every downstream
# binding manifest, translating the spelling each ecosystem requires.
#
# Usage:
#   scripts/bump_version.sh                # sync manifests to the SoT (idempotent)
#   scripts/bump_version.sh --check        # exit 1 if any manifest drifts from the SoT
#   scripts/bump_version.sh --bump X.Y.Z[-pre]   # rewrite the SoT then sync
#   scripts/bump_version.sh --help
#
# The single source of truth is the Cargo workspace version (Cargo SemVer,
# e.g. `0.2.0-alpha.1`). Three spellings are derived from it:
#
#   * Cargo   : the SoT verbatim, e.g. `0.2.0-alpha.1`  (or plain `0.2.0`).
#               Used by the root Cargo.toml [workspace.dependencies]
#               nirs4all-datasets-core internal-dep `version` (required so the
#               published crates resolve each other from crates.io),
#               bindings/python/Cargo.toml, and bindings/wasm/Cargo.toml.
#               The npm package.json (bindings/wasm/pkg-node/) is a gitignored
#               wasm-pack build artifact, NOT a sync target — release-npm.yml
#               injects the SoT version into it at build time.
#   * PEP 440 : `0.2.0a1` for `0.2.0-alpha.1`; `0.2.0b2` / `0.2.0rc1` for
#               beta / rc; plain `X.Y.Z` maps to itself.
#               Used by the root pyproject.toml [project] version (the maturin
#               build reads it to stamp the `nirs4all-datasets` wheel/sdist) and,
#               if present, src/nirs4all_datasets/_version.py.
#   * R       : the plain base `X.Y.Z` for a final release; `X.Y.Z.9000`
#               (the canonical R "in-development toward X.Y.Z" spelling) for
#               ANY pre-release — CRAN does not accept SemVer pre-release
#               suffixes. Used by bindings/r/nirs4alldatasets/DESCRIPTION.
#
# Requires: bash >= 4, GNU sed, python3 (no external Python deps).

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CARGO_TOML="${ROOT}/Cargo.toml"

if [[ ! -f "${CARGO_TOML}" ]]; then
    echo "error: root Cargo.toml not found at ${CARGO_TOML}" >&2
    exit 2
fi

# ---------------------------------------------------------------------------
# 1. Read the canonical Cargo version from [workspace.package] version
# ---------------------------------------------------------------------------
read_workspace_version() {
    # Extract the `version = "…"` line inside the [workspace.package] table.
    local value
    value=$(sed -nE '/^\[workspace\.package\]/,/^\[/{s/^version[[:space:]]*=[[:space:]]*"([^"]+)".*/\1/p}' \
            "${CARGO_TOML}" | head -n1 || true)
    if [[ -z "${value}" ]]; then
        echo "error: could not parse [workspace.package] version from ${CARGO_TOML}" >&2
        exit 2
    fi
    printf '%s' "${value}"
}

# ---------------------------------------------------------------------------
# 2. Spelling translators (Cargo SemVer is the canonical input)
# ---------------------------------------------------------------------------
# Cargo SemVer grammar accepted here: X.Y.Z optionally followed by a
# `-<pre>` identifier. The pre-release we translate is one of:
#   alpha[.N] | beta[.N] | rc[.N]   (the only ones the ecosystems map cleanly).
# Anything else with a `-` suffix is rejected so drift can't sneak through.

# to_pep440 <cargo_version> -> PEP 440 spelling
to_pep440() {
    local v="$1"
    local base="${v%%-*}"          # X.Y.Z
    if [[ ! "${base}" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        echo "error: version base '${base}' is not X.Y.Z" >&2
        exit 2
    fi
    local pre=""
    [[ "${v}" == *-* ]] && pre="${v#*-}"
    if [[ -z "${pre}" ]]; then
        printf '%s' "${base}"
        return 0
    fi
    # The pre-release must be exactly alpha[.N] | beta[.N] | rc[.N] with a
    # canonical numeric N (no leading zeros). Reject anything else so we never
    # emit invalid / non-canonical PEP 440 (e.g. 'alpha.foo' -> 'afoo',
    # 'alpha.01' -> 'a01' which PyPI normalises to 'a1' and breaks tag↔version).
    if [[ ! "${pre}" =~ ^(alpha|beta|rc)(\.(0|[1-9][0-9]*))?$ ]]; then
        echo "error: unsupported pre-release '${pre}' (want alpha[.N]|beta[.N]|rc[.N], N canonical)" >&2
        exit 2
    fi
    local kind num
    kind="${pre%%.*}"
    if [[ "${pre}" == *.* ]]; then num="${pre#*.}"; else num="0"; fi
    case "${kind}" in
        alpha) printf '%sa%s'  "${base}" "${num}" ;;
        beta)  printf '%sb%s'  "${base}" "${num}" ;;
        rc)    printf '%src%s' "${base}" "${num}" ;;
    esac
}

# to_r <cargo_version> -> R DESCRIPTION spelling
to_r() {
    local v="$1"
    local base="${v%%-*}"          # X.Y.Z
    if [[ "${v}" == *-* ]]; then
        # Any pre-release → the canonical R "in development toward base" form.
        printf '%s.9000' "${base}"
    else
        printf '%s' "${base}"
    fi
}

# ---------------------------------------------------------------------------
# 3. CLI handling
# ---------------------------------------------------------------------------
MODE="sync"
NEW_VERSION=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --check)  MODE="check"; shift ;;
        --bump)
            if [[ $# -lt 2 ]]; then
                echo "error: --bump requires X.Y.Z[-pre]" >&2
                exit 2
            fi
            MODE="bump"
            NEW_VERSION="$2"
            shift 2
            ;;
        -h|--help)
            sed -nE '2,/^$/{ s/^# ?//; /^!/!p }' "${BASH_SOURCE[0]}"
            exit 0
            ;;
        *) echo "error: unknown argument: $1" >&2; exit 2 ;;
    esac
done

# ---------------------------------------------------------------------------
# 4. --bump: rewrite the SoT first
# ---------------------------------------------------------------------------
if [[ "${MODE}" == "bump" ]]; then
    if [[ ! "${NEW_VERSION}" =~ ^[0-9]+\.[0-9]+\.[0-9]+(-[0-9A-Za-z.]+)?$ ]]; then
        echo "error: --bump requires X.Y.Z[-pre] (got: '${NEW_VERSION}')" >&2
        exit 2
    fi
    # Validate the pre-release translates (fails loudly before any write).
    to_pep440 "${NEW_VERSION}" >/dev/null
    # Rewrite ONLY the version inside [workspace.package].
    sed -i -E "/^\[workspace\.package\]/,/^\[/{s/^(version[[:space:]]*=[[:space:]]*\")[^\"]+(\")/\1${NEW_VERSION}\2/}" \
        "${CARGO_TOML}"
    echo "  bumped [workspace.package] version to ${NEW_VERSION}"
    MODE="sync"
fi

# ---------------------------------------------------------------------------
# 5. Re-read the SoT (post --bump if any) and derive the three spellings
# ---------------------------------------------------------------------------
CARGO_VERSION="$(read_workspace_version)"
PEP440_VERSION="$(to_pep440 "${CARGO_VERSION}")"
R_VERSION="$(to_r "${CARGO_VERSION}")"

if [[ "${MODE}" == "check" ]]; then
    echo "  canonical Cargo version : ${CARGO_VERSION}"
    echo "  derived PEP 440 version : ${PEP440_VERSION}"
    echo "  derived R version       : ${R_VERSION}"
else
    echo "  syncing manifests to Cargo=${CARGO_VERSION} / PEP440=${PEP440_VERSION} / R=${R_VERSION}"
fi

# ---------------------------------------------------------------------------
# 6. Manifest update / check engine
# ---------------------------------------------------------------------------
EXIT_CODE=0
DRIFTED=()

# update_with_sed <relative_path> <expected_value> <sed_match_regex> <sed_replace_regex> [optional]
#   sed_match_regex: must capture the version with group \1 (for --check extraction).
#   sed_replace_regex: full sed -E expression  s/MATCH/REPLACEMENT/.
#   optional (5th arg, "optional"): a missing file is skipped, not a drift.
update_with_sed() {
    local rel="$1" expected="$2" match="$3" replace="$4" optional="${5:-}"
    local abs="${ROOT}/${rel}"

    if [[ ! -f "${abs}" ]]; then
        if [[ "${optional}" == "optional" ]]; then
            return 0  # planned/absent manifest — not a drift
        fi
        echo "  DRIFT: ${rel} missing (expected manifest)" >&2
        DRIFTED+=("${rel}")
        EXIT_CODE=1
        return 0
    fi

    local current
    current=$(grep -E "${match}" "${abs}" | head -n1 || true)
    if [[ -z "${current}" ]]; then
        echo "  DRIFT: ${rel} has no line matching /${match}/" >&2
        DRIFTED+=("${rel}")
        EXIT_CODE=1
        return 0
    fi

    local found
    found=$(printf '%s\n' "${current}" | sed -E "s|.*${match}.*|\1|" | head -n1)

    if [[ "${MODE}" == "check" ]]; then
        if [[ "${found}" != "${expected}" ]]; then
            echo "  DRIFT: ${rel} reports '${found}' (expected '${expected}')" >&2
            DRIFTED+=("${rel}")
            EXIT_CODE=1
        fi
    else
        if [[ "${found}" == "${expected}" ]]; then
            return 0  # already in sync
        fi
        sed -i -E "${replace}" "${abs}"
        echo "  updated ${rel}: ${found} → ${expected}"
    fi
}

# ---------------------------------------------------------------------------
# 7. The manifest table — every downstream version string lives here.
# ---------------------------------------------------------------------------

# --- Cargo SemVer targets (the SoT spelling verbatim) ----------------------

# Internal workspace dep version in the root Cargo.toml [workspace.dependencies].
# It carries an explicit `version` (alongside `path`) so the published crates
# resolve each other from crates.io; the value MUST track the workspace version.
update_with_sed \
    "Cargo.toml" \
    "${CARGO_VERSION}" \
    "^nirs4all-datasets-core[[:space:]]*=.*version[[:space:]]*=[[:space:]]*\"([0-9A-Za-z.-]+)\"" \
    "s/^(nirs4all-datasets-core[[:space:]]*=.*version[[:space:]]*=[[:space:]]*\")[0-9A-Za-z.-]+(\")/\1${CARGO_VERSION}\2/"

# Python PyO3 crate (bindings/python/Cargo.toml: line  version = "X.Y.Z[-pre]")
update_with_sed \
    "bindings/python/Cargo.toml" \
    "${CARGO_VERSION}" \
    "^version[[:space:]]*=[[:space:]]*\"([0-9A-Za-z.-]+)\"" \
    "s/^(version[[:space:]]*=[[:space:]]*\")[0-9A-Za-z.-]+(\")/\1${CARGO_VERSION}\2/"

# WASM crate (bindings/wasm/Cargo.toml)
update_with_sed \
    "bindings/wasm/Cargo.toml" \
    "${CARGO_VERSION}" \
    "^version[[:space:]]*=[[:space:]]*\"([0-9A-Za-z.-]+)\"" \
    "s/^(version[[:space:]]*=[[:space:]]*\")[0-9A-Za-z.-]+(\")/\1${CARGO_VERSION}\2/" \
    optional

# R vendored Rust workspace (generated by N4DS_R_VENDOR=1 ./configure, committed
# so source installs can build the staticlib offline).
update_with_sed \
    "bindings/r/nirs4alldatasets/src/rust/Cargo.toml" \
    "${CARGO_VERSION}" \
    "^version[[:space:]]*=[[:space:]]*\"([0-9A-Za-z.-]+)\"" \
    "s/^(version[[:space:]]*=[[:space:]]*\")[0-9A-Za-z.-]+(\")/\1${CARGO_VERSION}\2/" \
    optional

update_with_sed \
    "bindings/r/nirs4alldatasets/src/rust/Cargo.toml" \
    "${CARGO_VERSION}" \
    "^nirs4all-datasets-core[[:space:]]*=.*version[[:space:]]*=[[:space:]]*\"([0-9A-Za-z.-]+)\"" \
    "s/^(nirs4all-datasets-core[[:space:]]*=.*version[[:space:]]*=[[:space:]]*\")[0-9A-Za-z.-]+(\")/\1${CARGO_VERSION}\2/" \
    optional

# NOTE: bindings/wasm/pkg-node/package.json is a wasm-pack BUILD ARTIFACT — the
# pkg-node/ directory is gitignored, so it is NOT in version control and is
# absent on a fresh checkout. release-npm.yml injects the canonical SoT version
# into the generated pkg-node/package.json at build time (the "Pin package.json
# name + version" step reads the Cargo SoT), so there is nothing to sync here.

# --- PEP 440 targets -------------------------------------------------------

# Root Python package version: pyproject.toml [project] version. maturin reads
# the repo-root pyproject to stamp the `nirs4all-datasets` wheel + sdist, so this
# is the version PyPI sees.
update_with_sed \
    "pyproject.toml" \
    "${PEP440_VERSION}" \
    "^version[[:space:]]*=[[:space:]]*\"([0-9A-Za-z.+!-]+)\"" \
    "s/^(version[[:space:]]*=[[:space:]]*\")[0-9A-Za-z.+!-]+(\")/\1${PEP440_VERSION}\2/"

# Citation metadata uses the plain final PEP 440 spelling for release artifacts.
update_with_sed \
    "CITATION.cff" \
    "${PEP440_VERSION}" \
    "^version:[[:space:]]*\"([0-9A-Za-z.+!-]+)\"" \
    "s/^(version:[[:space:]]*\")[0-9A-Za-z.+!-]+(\")/\1${PEP440_VERSION}\2/"

# Optional runtime version string, if the package grows one.
update_with_sed \
    "src/nirs4all_datasets/_version.py" \
    "${PEP440_VERSION}" \
    "^__version__[[:space:]]*=[[:space:]]*\"([0-9A-Za-z.+!-]+)\"" \
    "s/^(__version__[[:space:]]*=[[:space:]]*\")[0-9A-Za-z.+!-]+(\")/\1${PEP440_VERSION}\2/" \
    optional

# --- R DESCRIPTION target --------------------------------------------------

# R DESCRIPTION (Version: X.Y.Z[.9000]). The R binding dir is created
# concurrently; treat it as optional until it lands.
update_with_sed \
    "bindings/r/nirs4alldatasets/DESCRIPTION" \
    "${R_VERSION}" \
    "^Version:[[:space:]]+([0-9.]+)" \
    "s/^(Version:[[:space:]]+)[0-9.]+/\1${R_VERSION}/" \
    optional

# ---------------------------------------------------------------------------
# 8. Summary
# ---------------------------------------------------------------------------
if [[ "${MODE}" == "check" ]]; then
    if [[ ${EXIT_CODE} -eq 0 ]]; then
        echo "  OK: every manifest is in sync with the Cargo workspace version (${CARGO_VERSION})"
    else
        echo "" >&2
        echo "FAIL: ${#DRIFTED[@]} manifest(s) drifted from the Cargo workspace version." >&2
        echo "      Run scripts/bump_version.sh to re-sync." >&2
    fi
fi
exit ${EXIT_CODE}
