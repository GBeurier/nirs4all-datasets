<!-- SPDX-License-Identifier: MIT -->
# Development — Release Process

How each binding of `nirs4all-datasets` is versioned, gated, and published. The
Python wheels + sdist (the analysis package **with** the embedded native
acquisition core), the Rust crates, the npm WASM package, the Octave/MATLAB zip,
and the source/provenance bundle publish from CI; the R (CRAN / R-universe) leg
attaches a tarball and its registry steps are documented below.

The authoritative Python/C-ABI build workflow is
[`.github/workflows/release-python.yml`](../../.github/workflows/release-python.yml);
the per-surface workflows are `release-crates.yml`, `release-r.yml`,
`release-matlab.yml`, `release-npm.yml`, and `release-source.yml`. The gates are
`ci.yml`, `version-sync.yml`, and `abi-check.yml`.

> **The Python package is the acquisition core's home.** Unlike the other repos
> there is **no separate Python distribution** for the binding — the pyo3
> extension (`nirs4all_datasets._n4ds`) is built by maturin **into** the
> `nirs4all-datasets` wheel. `pip install nirs4all-datasets` gets the pure-Python
> analysis layer **and** the native acquisition core together (root
> [`pyproject.toml`](../../pyproject.toml) `[tool.maturin]`).

> **No macOS deferral.** The acquisition core is **pure-Rust** (`serde`/
> `serde_json`/`sha2`/`hex`/`ureq`/`directories`/`tempfile` — no C system
> library), so it ships **macOS binary wheels** and macOS C-ABI archives
> alongside Linux + Windows with no special handling.

## Single source of truth

The canonical version is the **`[workspace.package] version` in the root
[`Cargo.toml`](../../Cargo.toml)** (Cargo SemVer, currently `0.2.0-alpha.1`).
`scripts/bump_version.sh` propagates it to every binding manifest, translating the
spelling each ecosystem requires:

| Spelling | Example (`0.2.0-alpha.1`) | Manifests |
|---|---|---|
| Cargo SemVer (verbatim) | `0.2.0-alpha.1` | root `Cargo.toml` `[workspace.package]` + the `[workspace.dependencies]` internal-crate `version`, `bindings/python/Cargo.toml`, `bindings/wasm/Cargo.toml` |
| PEP 440 | `0.2.0a1` (`alpha.N→aN`, `beta.N→bN`, `rc.N→rcN`; plain `X.Y.Z`→itself) | root `pyproject.toml` `[project] version` |
| R | `0.2.0.9000` (plain `X.Y.Z` for a final; `X.Y.Z.9000` "in development toward X.Y.Z" for ANY pre-release, since CRAN rejects SemVer pre-release suffixes) | `bindings/r/DESCRIPTION` |

> The npm `bindings/wasm/pkg/package.json` is a **gitignored wasm-pack build
> artifact** (not in version control), so it is **not** a sync target —
> `release-npm.yml` injects the SoT version into the generated package at build
> time.

```bash
scripts/bump_version.sh --check          # exit 1 on any drift (CI gate)
scripts/bump_version.sh --bump X.Y.Z     # rewrite the SoT, then sync
scripts/bump_version.sh                   # sync every manifest to the SoT
```

The C ABI version (`N4DS_ABI_VERSION` in
[`crates/nirs4all-datasets-capi/src/lib.rs`](../../crates/nirs4all-datasets-capi/src/lib.rs),
runtime `n4ds_abi_version()`, currently `0.1.0`) bumps **independently** from the
Rust semver, and the `n4ds_` exported-symbol surface is diffed by
`.github/workflows/abi-check.yml`.

## Binding → registry → automation

| Binding | Package | Registry | Automation | Trigger |
|---------|---------|----------|------------|---------|
| Python (analysis + embedded native core) | `nirs4all-datasets` | PyPI | **Automated** — `release-python.yml` (maturin abi3 wheels all-3-OS + sdist) publishes via Trusted Publishing | push tag `v*` (non-pre-release) → PyPI |
| Rust crates | `nirs4all-datasets-core`, `nirs4all-datasets-capi`, `nirs4all-datasets-cli` | crates.io | **Automated** — `release-crates.yml` publishes leaf-first | push tag `v*` (non-pre-release) + `CARGO_REGISTRY_TOKEN` |
| R | `nirs4alldatasets` | **R-universe / GitHub Release** (CRAN deferred) | **Build CI-automated** — `release-r.yml` installs + smokes across the matrix, `R CMD build` attaches the tarball. R-universe is a one-time registry entry; CRAN is a deferred follow-up (the binding links a prebuilt cdylib; see *R → CRAN*). | tag push attaches the tarball |
| Octave / MATLAB | `nirs4all-datasets-matlab-octave-<version>.zip` | GitHub Release | **Automated** — `release-matlab.yml` (`git archive HEAD:bindings/matlab`) | push tag `v*` (non-pre-release) |
| JS / WASM | `@nirs4all/datasets-wasm` | npm | **Automated** — `release-npm.yml` (wasm-pack nodejs build, scoped name + provenance, node smoke) publishes via `npm publish` | push tag `v*` (non-pre-release) + `NPM_TOKEN` |
| Source + provenance | — | GitHub Release | **Automated** — `release-source.yml` (reproducible git-archive tar.gz + zip, CycloneDX SBOM, `SHA256SUMS`, keyless Sigstore provenance) | push tag `v*` (non-pre-release) |

## Exact release artifacts — what each binding ships, and where to upload it

Every artifact below is also attached to the **GitHub Release** for the tag, so
they are downloadable from one place. **The bundled `catalog/index.json` rides
inside the Python wheel** (`[tool.maturin] include = ["catalog/index.json"]`) and
is attached to the Release as the cross-language download contract every binding
reads.

| Binding | Registry | Exact file(s) | Upload |
|---|---|---|---|
| Python `nirs4all-datasets` | PyPI | `nirs4all_datasets-<version>-*.whl` (maturin abi3 wheels: Linux + macOS + Windows, the embedded `_n4ds` core + the bundled `catalog/index.json`) + `nirs4all_datasets-<version>.tar.gz` (maturin sdist) | **Automated** — Trusted Publishing, *no manual upload* |
| Rust crates | crates.io | the 3 workspace crates (`nirs4all-datasets-core` / `nirs4all-datasets-capi` / `nirs4all-datasets-cli`) | **Automated** — `cargo publish`, leaf-first |
| R `nirs4alldatasets` | R-universe / Release | **`nirs4alldatasets_<version>.tar.gz`** (source tarball) | **Automated to the Release** (R-universe builds from Git). **NOT CRAN-self-contained** — see *R → CRAN* |
| Octave / MATLAB | GitHub Release | `nirs4all-datasets-matlab-octave-<version>.zip` (the `bindings/matlab` subtree) | **Automated** — `release-matlab.yml` |
| JS / WASM `@nirs4all/datasets-wasm` | npm | the staged `pkg-node/` package (via `npm publish`) | **Automated** — `release-npm.yml` (needs `NPM_TOKEN` + the `@nirs4all` scope) |
| C-ABI archive | GitHub Release | `nirs4all-datasets-capi-<os>.tar.gz` (lib + `nirs4all_datasets.h` + LICENSE), Linux/macOS/Windows | **Automated** — `release-python.yml` |
| Source + provenance | GitHub Release | `nirs4all-datasets-<version>-src.tar.gz` · `…-src.zip` · `nirs4all-datasets-<version>.cdx.json` (SBOM) · `SHA256SUMS` | **Automated** — `release-source.yml` |

## Pre-release gates (release blockers)

Run these before tagging or publishing anything:

1. **Version sync** — `scripts/bump_version.sh --check`. The canonical version
   lives in the root `Cargo.toml` `[workspace.package] version`; the script syncs
   it into every tracked binding manifest (the `[workspace.dependencies]`
   internal-crate versions used for crates.io resolution, the two binding Cargo
   manifests, the PEP 440 root `pyproject.toml`, and the R `DESCRIPTION`).
   **Bump with** `bump_version.sh --bump X.Y.Z[-pre]`. Enforced in CI by
   `version-sync.yml`.
2. **Green gate** — both halves, mirrored by `ci.yml`:
   - **Rust:** `cargo fmt --check`, `cargo clippy --workspace --all-targets -D
     warnings`, `cargo test --workspace`, plus the Python / R / Octave-MATLAB /
     WASM binding smokes.
   - **Python:** `ruff check .`, `mypy --config-file pyproject.toml src`,
     `python catalog/scripts/validate.py` (+ `--check-publish`), and `pytest -q`.
     Regenerate the catalog and confirm it is committed:
     `python -m nirs4all_datasets.cli catalog --root .` then
     `git diff --exit-code catalog/datasets.yaml`. The cross-language
     `catalog/index.json` is regenerated the same way (`index.py` `build_index`)
     and must be committed.
3. **C ABI sanity** — the committed
   `crates/nirs4all-datasets-capi/include/nirs4all_datasets.h` matches the current
   surface; the `n4ds_` exported-symbol set matches
   `crates/nirs4all-datasets-capi/abi/expected_symbols_*.txt`
   (`tests/abi_surface.rs` locally, `abi-check.yml` in CI). Bump
   `N4DS_ABI_VERSION` only on an ABI change.

## Tag-to-release flow

1. `scripts/bump_version.sh --bump X.Y.Z` (rewrites the SoT + syncs every
   manifest), then run `scripts/bump_version.sh --check` to confirm.
2. Verify the green gate locally (both halves above) and confirm
   `catalog/index.json` + `catalog/datasets.yaml` are regenerated and committed.
3. Commit, then tag: `git tag vX.Y.Z && git push --tags`.
4. CI builds wheels + sdist + C-ABI archives + crates + npm package + R tarball +
   Octave/MATLAB zip + source/SBOM bundle, then — **for a non-pre-release tag** —
   publishes to PyPI / crates.io / npm and cuts the GitHub Release.

**Pre-release tags** (anything containing `-`, e.g. `v0.2.0-alpha.1`) are
**excluded from publishing**: every publish job gates on
`!contains(github.ref_name, '-')`, so a pre-release never reaches a registry or
cuts a public Release. To publish the current alpha to PyPI, tag it with the PEP
440 spelling (`v0.2.0a1`) — `publish-pypi` validates that the tag minus `v` equals
the built wheel/sdist version, but the production-only auto-publish check
additionally requires a plain `vX.Y.Z`.

`workflow_dispatch` runs build/dry-run jobs only; the PyPI publish also gates on
`github.event_name != 'workflow_dispatch'`, the crates publish dry-runs by default
(`dry_run` input), and the npm publish gates on `inputs.publish == true`.

---

## Gated / maintainer one-time setup

### Python → PyPI (Trusted Publisher)

`release-python.yml`'s `publish-pypi` uses PyPI Trusted Publishing (OIDC,
`id-token: write`) — no API token. One-time maintainer setup at
<https://pypi.org/manage/account/publishing/>:

| Field | Value |
|---|---|
| PyPI Project Name | `nirs4all-datasets` |
| Owner | `GBeurier` |
| Repository name | `nirs4all-datasets` |
| Workflow filename | `release-python.yml` |
| Environment | **`pypi`** |

> The `publish-pypi` job runs in the GitHub `pypi` environment, so the OIDC token
> carries an `environment: pypi` claim — the Trusted Publisher MUST be created with
> **Environment = `pypi`**. A publisher whose Environment field differs (blank or
> anything else) fails with `invalid-publisher`. Because the project does not exist
> on PyPI yet, create this as a **pending publisher** (same form, at the URL
> above). **One convention across the whole ecosystem: Environment = `pypi`**
> (identical to `nirs4all-formats` / `nirs4all-io` / `nirs4all-methods`).

### Rust → crates.io

`release-crates.yml` publishes the three workspace crates leaf-first
(`nirs4all-datasets-core → nirs4all-datasets-capi → nirs4all-datasets-cli`). The
internal crate carries an explicit `version` in the root
`[workspace.dependencies]` (alongside `path`) so each published crate resolves its
in-tree dependency from crates.io; the workflow's `sleep 30` lets the sparse index
catch up between crates. A downstream crate's `cargo publish --dry-run` only fully
verifies once its dependency is actually on crates.io — so the dispatch dry-run
reports the leaf crate cleanly and the downstream crates show "no matching package
… on crates.io index" until the real leaf-first publish lands them. One-time:
generate a crates.io API token with publish-new + publish-update scope and add it
as the GitHub Actions secret `CARGO_REGISTRY_TOKEN`. Validate first with the
`workflow_dispatch` dry-run (`dry_run = true` runs `cargo publish --dry-run` for
every crate). The real publish fires only on a non-pre-release `vX.Y.Z` tag;
crates.io is immutable, so a bad version can only be **yanked**, never replaced.

> The pyo3 binding crate `nirs4all-datasets-py` (`bindings/python`) is **excluded
> from the cargo workspace** and **not** published to crates.io — it is built by
> maturin into the PyPI wheel, not consumed as a crate.

### JS → npm (`@nirs4all/datasets-wasm`)

`release-npm.yml` builds the wasm-pack `nodejs` target, pins the scoped name +
provenance in the generated `package.json`, runs the committed Node smoke, and
publishes via `npm publish`.

One-time: own the `@nirs4all` scope on [npmjs.com](https://www.npmjs.com) (*Add
Organization* → create the free org `nirs4all`), generate a granular
**Automation** token with read+write on the `@nirs4all/datasets-wasm` package, and
add it as the GitHub Actions secret `NPM_TOKEN`. Provenance
(`publishConfig.provenance = true`) needs `id-token: write` (already set) and a
public repo.

> **WASM scope caveat (`migration_ABI_C.md` §4).** The WASM binding is scoped to
> **metadata + small public datasets**: Dataverse emits CORS only when the
> instance is configured to, the S3/CDN serving the bytes needs its own bucket
> CORS, there is no real filesystem (→ OPFS/IndexedDB, bounded), and large
> datasets are impractical in the browser. The npm package is published all the
> same; the README documents the constraint.

### R → R-universe (registration)

R-universe builds binaries (Windows/macOS/Linux) straight from Git — no review, no
submission. Users then
`install.packages("nirs4alldatasets", repos = "https://gbeurier.r-universe.dev")`.

- **Registry repo**: public `GBeurier/GBeurier.r-universe.dev` with a
  `packages.json` entry:
  ```json
  { "package": "nirs4alldatasets", "url": "https://github.com/GBeurier/nirs4all-datasets", "subdir": "bindings/r" }
  ```
  No `branch` field → it tracks the default branch.
- **GitHub App** (one manual browser step): install
  <https://github.com/apps/r-universe> on the `GBeurier` account.
- **Verify**: watch <https://gbeurier.r-universe.dev> (it *shows* the
  `R CMD check` result but, unlike CRAN, does not block on a NOTE/WARNING).

> **Caveat:** the R binding links the **prebuilt** `nirs4all-datasets-capi`
> cdylib, so R-universe's from-Git build needs the cdylib available on its
> builders. R-universe is the lower-friction target; if its build cannot locate
> the prebuilt library, the binding must be reworked (see *R → CRAN*).

### R → CRAN (submission) — deferred follow-up

> **The R binding is NOT CRAN-submittable in its current form.** It is a C shim
> that links the **prebuilt** `libnirs4all_datasets_capi`. CRAN's build farm has
> no such prebuilt library and the package does not vendor or compile the Rust
> core at install time, so a plain `R CMD build bindings/r` tarball **cannot
> install on CRAN**. The `nirs4alldatasets_<version>.tar.gz` produced by
> `release-r.yml` is an **R-universe / GitHub-Release asset only**.
>
> **CRAN self-containment is a tracked follow-up.** A CRAN-submittable R package
> requires **reworking the binding** to bundle and compile the Rust core offline
> at install time (extendr-static, or a vendored cdylib mirroring
> `nirs4all-formats`' `./configure` vendor mode: copy the workspace core crate
> into `src/rust/vendored/`, `cargo vendor` the crates.io closure into
> `vendor.tar.xz`, and build offline from `src/Makevars(.win)`). Until that lands,
> ship the R binding via **R-universe + the GitHub Release**.

When the CRAN-ready variant exists, CRAN submission is a **manual web form** with
human review. Get the self-contained source tarball, then upload **only**
`nirs4alldatasets_<version>.tar.gz` at <https://cran.r-project.org/submit.html>:

| Field | Value |
|---|---|
| Your name | `Gregory Beurier` |
| Your email | **`gregory.beurier@cirad.fr`** — must match the `Maintainer` (`cre`) in `DESCRIPTION` **exactly** |
| Upload | `nirs4alldatasets_<version>.tar.gz` (the R source tarball only — never a binary, the repo zip, or the Python sdist) |
| Optional comment to CRAN | **paste the block below** |

**Paste-ready CRAN submission comment** (kept in sync with
`bindings/r/cran-comments.md`):

```text
This is a new submission.

nirs4alldatasets is a thin R binding for the Rust-first nirs4all-datasets
dataset-acquisition core for the nirs4all NIRS / spectroscopy ecosystem. It
exposes the stable n4ds_* C ABI to R: resolve a dataset id from the distributable
catalog index, download the pinned canonical Parquet from its origin (Dataverse /
Zenodo / figshare), SHA-256-verify against the index, and cache it. The JSON
surface crosses the C ABI and results are canonical JSON strings; no scientific
arrays cross the boundary (R reads the verified Parquet with the arrow package).
License: MIT.

Self-contained source tarball: the package vendors the nirs4all-datasets Rust core
and its crates.io transitive dependencies and compiles them OFFLINE at install
time via src/Makevars(.win) (no network, no external monorepo crates/). The Cargo
/ rustc toolchain is declared in SystemRequirements.

Test environments: local Ubuntu/WSL2 R release (offline standalone install ->
installs, loads, native path active); CI matrix (release-r.yml) on Ubuntu 22.04
(R release + devel), macOS 14 (R release, arm64), Windows Server 2022 (R release);
win-builder + R-hub v2 run manually before submission.

R CMD check --as-cran: 0 ERRORs. Any WARNING/NOTE comes from the bundled
third-party Rust sources or the local toolchain, not from the package's own R or
build logic. The package does no network access during install/examples/tests
(downloads happen only on an explicit user fetch call) and imports only base R +
jsonlite.

Maintainer: Grégory Beurier (CIRAD), gregory.beurier@cirad.fr.
```

> **CRAN version note:** CRAN rejects SemVer pre-release suffixes
> (`0.2.0-alpha.1`). While the project is pre-final the R spelling is the
> development version `0.2.0.9000`, which is **R-universe / dev only and is NOT
> submitted to CRAN**. The first CRAN-eligible R version is the plain `0.2.0` cut
> by `scripts/bump_version.sh --bump 0.2.0` — and only after the self-containment
> rework above.

---

## Rollback / yank

PyPI wheels and crates.io crates are immutable. **Yank** a bad release (the PyPI
web UI / `cargo yank --version X.Y.Z <crate>`) so it is unavailable to new installs
without breaking existing pins. For npm, `npm deprecate`. For the GitHub Release,
`gh release delete vX.Y.Z` and re-run `release-source.yml` for a corrected tag.

> **The catalog index pins the bytes.** Because every release ships a
> version-pinned `catalog/index.json` (each entry's `dataset_version` + every
> file's `sha256`), a yanked package never serves wrong bytes: a consumer on an old
> pin re-fetches and SHA-256-verifies exactly that release's data. Fixing a *data*
> error means re-publishing the dataset at its origin, bumping `versions.content`,
> and cutting a new index — not editing a shipped wheel.

## Operational notes

- **crates.io requires a valid SPDX license id.** This repo is **`MIT`**
  (`[workspace.package].license`), which crates.io accepts verbatim — no all-caps
  remap (unlike the CeCILL repos).
- **crates.io rate-limits NEW crates** (burst ~5, then throttled). Publishing the
  three new names at once can fail with `429 — too many new crates`; wait for the
  stated reset and re-run `release-crates` (already-uploaded crates skip; only the
  pending leaf re-publishes).
- **Verify crates.io with a `User-Agent` header** — the API returns nothing without
  one, so a *successful* publish can look "absent". The `cargo publish` log line
  `Published <crate> at registry crates-io` is the source of truth.
- **Pre-release versions don't auto-publish.** `0.2.0-alpha.1` (a `-` tag) is gated
  out of every publish job — bump to a plain `vX.Y.Z` (`bump_version.sh --bump
  0.2.0`, then refresh `Cargo.lock`) to release.
- **Network tests are gated.** The conformance/parity `fetch` jobs hit the
  RDG/CIRAD sandbox under the `network` pytest marker / a `network`-gated CI leg;
  the default suite injects a fake `HttpSession` and touches no network.
