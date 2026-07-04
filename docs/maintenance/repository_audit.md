# Repository audit — nirs4all-datasets

> Generated from the automated pre-release audit (workflow wf_1fc87351-29f); the **Deepest hardening roadmap** section records the fullest realistic hardening even where the pragmatic pass does not implement it. Reviewed at Codex Gate 1.

- **Mode:** IN SCOPE — pragmatic hardening + push
- **Baseline HEAD:** `c46042da`
- **Role:** Dataset catalog + native acquisition core. CLI n4a-datasets: DOI-pinned, checksum-verified NIRS dataset downloads from Dataverse/Zenodo/figshare, identity cards, Croissant metadata, static site; reuses nirs4all-io/-formats and never re-parses vendor files.
- **Stack:** Polyglot maturin/PyO3 project (NOT pure Python as the brief states). Python 3.11/3.12 analysis+CLI layer in src/nirs4all_datasets (typer, pydantic v2, numpy/scipy/pandas/pyarrow, matplotlib, requests, jsonschema, pyyaml). Native acquisition core is a Rust workspace (crates/nirs4all-datasets-core|-capi|-cli; serde/sha2/ureq/zip) exposed as the embedded nirs4all_datasets._n4ds pyo3 extension, plus a stable C ABI and R / MATLAB / WASM-npm bindings. Build backend: maturin>=1.5,<2 (python-source=src, manifest-path=bindings/python/Cargo.toml). Package manager: uv. Rust edition 2021. Version SoT = Cargo [workspace.package] 0.3.2, synced to pyproject/bindings by scripts/bump_version.sh.

## Release-readiness verdict
nirs4all-datasets is more mature and more polyglot than its one-line 'Python CLI' description: it is a maturin/PyO3 package whose native acquisition core is a Rust workspace with C-ABI, R, MATLAB, and WASM/npm bindings, all released off a single version tag. CI is comprehensive and currently all-green (Rust fmt/clippy/test, WASM smoke, Python ruff/mypy/catalog-validate/pytest, ABI snapshot, version guard+sync), and release hygiene is strong (PyPI Trusted Publishing/OIDC, keyless Sigstore provenance, CycloneDX SBOM, idempotent skip-existing). The main hardening gaps are: a Pages deploy on push-to-main with no gate, non-hermetic builds that clone sibling repos from their default branch, a tested matrix (3.11/Linux only) far narrower than the published wheel matrix, no coverage/vuln-scan enforcement, and missing community/security hygiene files (SECURITY.md, CITATION.cff, dependabot, CoC, templates) plus a stale CHANGELOG. None are blockers for a tagged release, but push-to-main and tag-push both carry real blast radius (public Pages, immutable crates.io/PyPI/npm publishes) and should be treated carefully.

## Gate commands (detected)
| key | value |
|---|---|
| `install` | uv venv --clear && uv pip install -e ".[dev]" |
| `test` | uv run --no-sync pytest -m "not network" |
| `lint` | uv run --no-sync ruff check . ; cargo clippy --workspace --all-targets -- -D warnings |
| `typecheck` | uv run --no-sync mypy --config-file pyproject.toml src |
| `format` | cargo fmt --all --check |
| `docs_build` | python -m sphinx docs docs/_build |
| `package_build` | maturin build --release --out dist |

## CI
- **Latest status:** All green. Latest 8 runs (release-source/npm/matlab/python/r/crates from the n4a-v1-2026.07-refactor tag, plus Pages + CI) all [ok]. HEAD is detached on tag n4a-v1-2026.07-refactor; pyproject/Cargo version 0.3.2 == latest vX.Y.Z tag v0.3.2, so version-guard is satisfied.
- **Workflows:**
- ci.yml (rust green gate: fmt/clippy/test/build; wasm build+smoke+npm-pack; python: ruff/mypy/catalog-validate/catalog-index-drift/pytest — on push main+rc/**, PR)
- abi-check.yml (C ABI exported-symbol snapshot diff; push main+rc/**, PR, dispatch)
- version-guard.yml (manifest must not be ahead of latest v tag; push+PR main+rc/**)
- version-sync.yml (all binding manifests in sync with Cargo workspace version via bump_version.sh --check; push+PR+dispatch)
- docs.yml (builds+deploys static catalog site to GitHub Pages — DEPLOYS ON PUSH to main and redesign-v2)
- publish.yml (workflow_dispatch only, environment dataverse-publish, publishes one dataset to Dataverse)
- release-python.yml (tag v* -> maturin wheels macOS/Linux/Windows + sdist -> PyPI Trusted Publishing/OIDC + C-ABI archive + GH release)
- release-crates.yml (tag/dispatch -> crates.io, needs CARGO_REGISTRY_TOKEN)
- release-npm.yml (tag/dispatch -> @nirs4all/datasets-wasm npm, needs NPM_TOKEN)
- release-r.yml (tag -> CRAN-submittable R tarball)
- release-matlab.yml (tag -> MATLAB/Octave zip)
- release-source.yml (tag -> reproducible src archive + CycloneDX SBOM + Sigstore keyless provenance + SHA256SUMS)
- **Gaps:**
- No Python matrix — CI runs only Python 3.11 on ubuntu-latest, yet pyproject/classifiers/readthedocs claim 3.11+3.12 and wheels ship for macOS/Windows; nothing tests 3.12 or non-Linux.
- No coverage gate — pytest-cov is a dev dep and coverage.xml (157KB) exists locally, but ci.yml pytest has no --cov and no fail_under threshold; coverage is never measured or enforced in CI.
- No CodeQL / cargo-audit / pip-audit / dependency vulnerability scanning anywhere.
- GitHub Actions are pinned only to floating major tags (actions/checkout@v4, dtolnay/rust-toolchain@stable, jetli/wasm-pack-action@v0.4.0, etc.), not to commit SHAs.
- ci.yml jobs have no explicit top-level permissions block (default GITHUB_TOKEN scope), unlike the release/guard workflows which correctly set least-privilege.
- network-marked tests (9 files reference it) are deselected in CI with no scheduled job ever exercising the live-Dataverse path.

## Standard files
- **Present:** readme, changelog, contributing, license, gitignore
- **Missing:** security, code_of_conduct, citation, editorconfig, precommit, pr_template, issue_template, dependabot

## Packaging
- **name:** `nirs4all-datasets` — **version:** `0.3.2`
- **issues:**
- CHANGELOG.md is stale: top entry is [0.2.3] 2026-06-23 while the shipped version is 0.3.2 — the 0.3.0/0.3.1/0.3.2 releases have no changelog entries.
- Development Status classifier is '3 - Alpha' which understates a repo that already auto-publishes to PyPI/crates.io/npm on every tag.
- No CITATION.cff despite the project's explicit 'citable, DOI-pinned, FAIR' mission — a dataset-catalog package is the archetype that should ship citation metadata.
- sdist reproducibility of the native build depends on scripts/ensure_rust_deps.sh cloning sibling repos (nirs4all-formats, nirs4all-io) — see push_safety; a from-sdist build without siblings/crates.io availability is not self-evidently green.
- coverage.xml and bulk_report.json are gitignored yet present as tracked-looking artifacts in the worktree root (both in .gitignore, so untracked — confirm they are not accidentally committed).

## Tests
- **framework:** pytest (pytest-cov available; markers: network). 28 test modules under tests/, conftest + one JSON golden (tests/goldens/nonpython_bridge/io_dataset_spec.json). Rust side has cargo test --workspace; WASM has a node smoke test; C ABI has a symbol-snapshot check.
- **estimate:** ~224 Python test functions across 28 files (test_access/acquire/catalog/cli/dataverse/health/publish/reproduce/retrieval/schema/site/croissant/anonymize/metrics/...).
- **coverage:** Measured locally only (coverage.xml exists, 157KB) — NOT enforced in CI. ci.yml runs pytest -m 'not network' with no --cov flag and no fail_under threshold; 9 network tests are excluded from every CI run.

## Docs
- **system:** Sphinx + MyST (furo theme, sphinx-design/copybutton/opengraph) built on ReadTheDocs (.readthedocs.yaml, ubuntu-24.04, Python 3.12, docs/requirements.txt with pinned upper bounds). Separately, a bespoke static catalog site (src/nirs4all_datasets/site/) is built and deployed to GitHub Pages by docs.yml. docs/conf.py excludes PRIVATE_DATASETS.md and dev/ from the public build. Rich docs/ tree (ARCHITECTURE, DESIGN, PUBLISHING, RELEASING, RETRIEVAL_AUDIT, installation, getting_started, catalog, dev/release_process).
- **status:** Looks buildable — conf.py + requirements.txt + index.md present and consistent with the RTD config. No CI job builds the Sphinx docs, so RTD is the only place a broken docs build would surface; the Pages site build IS gated in ci-adjacent docs.yml but on push, not PR.

## Risks
| severity | area | detail |
|---|---|---|
| high | ci/pages | .github/workflows/docs.yml deploys the GitHub Pages catalog site on every push to main (and redesign-v2), with pages:write + id-token:write and concurrency cancel-in-progress. Any push to main immediately mutates the public Pages site with no tag/approval gate — a bad commit is publicly live at once. |
| high | reproducibility/cross-repo | Every Rust/Python CI + release job runs scripts/ensure_rust_deps.sh, which git-clones sibling repos nirs4all-formats and nirs4all-io from GitHub main (or the matching rc/** branch) into the parent dir. Builds are therefore NOT hermetic: a breaking change pushed to a sibling's default branch can turn this repo's CI/release red without any change here, and rc/** ref-following silently detaches siblings to FETCH_HEAD. |
| medium | release-coupling | A single vX.Y.Z tag simultaneously fans out to PyPI (release-python), crates.io (release-crates, IMMUTABLE), npm (release-npm), R tarball, MATLAB zip, and a signed source/SBOM release. A mistagged or partially-broken release is only partly reversible: crates.io versions can never be replaced, PyPI filenames can never be reused. High blast radius per tag. |
| medium | ci-scope | Python is tested on a single interpreter/OS (3.11, ubuntu-latest) while wheels are built and published for 3.11+3.12 across macOS/Windows — the published matrix is far wider than the tested matrix. |
| medium | supply-chain | No dependency/vulnerability scanning (no dependabot.yml, no cargo-audit, no pip-audit/CodeQL). ureq/zip/serde and the full Python data stack are unmonitored; Cargo.lock is committed but never audited. |
| low | docs/changelog | CHANGELOG stops at 0.2.3 while shipping 0.3.2; users cannot see what changed across the last three releases. |
| low | ci-permissions | ci.yml and abi-check.yml lack an explicit permissions: block, so their GITHUB_TOKEN uses the repo default scope instead of the least-privilege contents:read the guard/release workflows correctly set. |

## Security
- **info** — Source secret scan (src/, crates/, bindings/, scripts/, catalog/) found no plausible real credential. .env.example ships empty NIRS4ALL_DATAVERSE_TOKEN= placeholders only; .gitignore correctly excludes .env, *.token, config.toml.
- **low** — No SECURITY.md and no vulnerability-disclosure contact anywhere in README/CONTRIBUTING — the dual-license header points to nirs4all-admin@cirad.fr but there is no documented process for reporting a security issue.
- **low** — publish.yml correctly gates the Dataverse token behind the protected 'dataverse-publish' environment and contents:read; release-python/-source/-npm correctly use OIDC/Trusted-Publishing + keyless Sigstore (no long-lived PyPI key). Residual custody risk is only CARGO_REGISTRY_TOKEN (release-crates) and NPM_TOKEN (release-npm), which are unavoidable for those registries.

## Quick wins (pragmatic scope — safe to apply now)
- Add SECURITY.md with a disclosure contact (nirs4all-admin@cirad.fr) and supported-version note.
- Add an explicit least-privilege 'permissions: {contents: read}' block to ci.yml and abi-check.yml (release/guard workflows already do this).
- Add CITATION.cff — this is a citable, DOI-pinned dataset catalog; it should ship citation metadata.
- Bring CHANGELOG.md up to date with 0.3.0 / 0.3.1 / 0.3.2 entries (currently stops at 0.2.3).
- Add .editorconfig and a .pre-commit-config.yaml wiring ruff + ruff-format + cargo fmt so the green gate is runnable pre-commit.
- Add .github/dependabot.yml for pip, cargo, github-actions, and npm ecosystems.
- Add a CODE_OF_CONDUCT.md and .github/ISSUE_TEMPLATE + PULL_REQUEST_TEMPLATE.md (all absent).
- Bump the Development Status classifier from '3 - Alpha' to '4 - Beta' to match the multi-registry release automation.
- Turn on coverage in the CI pytest step (add --cov=nirs4all_datasets --cov-report=xml) so the already-collected coverage is visible per run.

## Deepest hardening roadmap (fullest realistic hardening)
- Pin every GitHub Action to a commit SHA (checkout, setup-python, setup-uv, dtolnay/rust-toolchain, PyO3/maturin-action, jetli/wasm-pack-action, softprops/action-gh-release, anchore/sbom-action, pypa/gh-action-pypi-publish) and let dependabot bump them.
- Expand the CI matrix to Python 3.11+3.12 across ubuntu/macos/windows so the tested surface equals the published wheel matrix; add a from-sdist install test to prove hermetic build.
- Make sibling-repo resolution reproducible: pin nirs4all-formats/nirs4all-io to explicit tags/SHAs (or consume the published crates.io versions) in CI/release rather than cloning their default branch, removing the cross-repo red-CI coupling.
- Introduce a coverage threshold (e.g. --cov-fail-under=85) and publish coverage to Codecov; add a scheduled (cron) job that runs the -m network live-Dataverse tests so the acquisition/checksum path is exercised.
- Add supply-chain scanning: cargo-audit + cargo-deny (license/advisory) on the Rust workspace, pip-audit on the Python deps, and CodeQL for Python+Rust; wire osv-scanner over Cargo.lock.
- Gate the GitHub Pages deploy behind a tag or manual approval (or a build-only PR check) instead of deploying on every push to main.
- Add a docs-build CI job (sphinx-build -W) on PRs so RTD breakage is caught before merge, and add link-checking.
- Add a release dry-run job (maturin build + cargo publish --dry-run + npm pack) that runs on rc/** tags before the immutable crates.io/PyPI publish, and require it green before a production tag.
- Ship provenance/SBOM consistently: the source release already does CycloneDX + Sigstore attestation — extend attestation to the wheels/crates/npm artifacts too.
- Add an SLSA-style checksum manifest for the wheels and document verification in RELEASING.md; add a CITATION.cff + DOI badge and Croissant validation as a CI check.

## Push-safety notes
- docs.yml deploys the public GitHub Pages catalog site on push to main (and redesign-v2) — a merge to main is instantly public with no gate. This is the single riskiest push-to-main automation.
- scripts/ensure_rust_deps.sh (invoked by ci.yml, abi-check.yml, release-python.yml) clones sibling repos from their default/rc branch; a push here can go red purely because a sibling's main changed, and an rc/** push detaches siblings to FETCH_HEAD — pushing to rc/** branches has non-local side effects.
- version-guard.yml + version-sync.yml enforce that the in-repo version never exceeds the latest v tag and that all binding manifests match the Cargo workspace SoT — so pushing a bumped version to main WITHOUT the matching tag will fail CI by design (bump must ship as a tag, via scripts/bump_version.sh, never a bare merge).
- Six release workflows (release-python/-crates/-npm/-r/-matlab/-source) all fire on tag push v*.*.*; pushing a tag triggers immutable publishes to PyPI, crates.io (irreversible), and npm at once — never push a version tag casually.
- publish.yml can push a dataset to the live Dataverse (production entrepot.recherche.data.gouv.fr) but is workflow_dispatch-only and gated on the protected dataverse-publish environment, so it is not triggered by a git push — comparatively safe.
- Note: HEAD is currently detached on tag n4a-v1-2026.07-refactor (an rc/refactor line), not on the v0.3.2 release commit — confirm the intended branch before any push.
