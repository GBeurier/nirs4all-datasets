# Release checklist — nirs4all-datasets

**Multi-registry, immutable fan-out.** A single `vX.Y.Z` tag fans out to PyPI, crates.io, npm, CRAN (R),
and MATLAB via the tag-triggered `release-*` workflows. crates.io/PyPI/npm are **yank-only** — a mistagged
release permanently burns a version number. Branch pushes to `main` never publish.

## Pre-release (do all before tagging)

- [ ] Green gate + CI green on the release commit (see `quality_gates.md`).
- [ ] `CHANGELOG.md` has a dated entry for the target version; **reconcile the `MIT` SPDX header vs the
      `CeCILL/AGPL` license** first.
- [ ] Every cross-manifest version is in sync (`version-sync` green); the manifest is not ahead of the tag
      until the tag exists (`version-guard`).
- [ ] **Dry-run each registry** via `workflow_dispatch` (`dry_run: true`) — `release-crates`, `release-python`,
      `release-npm`, `release-r`, `release-matlab` — and inspect artifacts/metadata.
- [ ] Confirm registry ownership / OIDC Trusted Publisher (PyPI env `pypi`), crates.io token, npm `@nirs4all`
      scope, CRAN submission readiness.
- [ ] Upstreams this depends on are already published at compatible versions (io, formats).

## Release

- [ ] Create the annotated tag `vX.Y.Z` **on the exact release commit** (final manifests/lockfiles/changelog);
      push it. The `release-*` workflows are idempotent (skip an already-published version).
- [ ] Watch every `release-*` run to green. **If one registry succeeds and another fails, do NOT re-tag** —
      re-run the failed workflow (publishes are idempotent) and reconcile before moving on.

## Post-release

- [ ] `pip install nirs4all-datasets==X.Y.Z` in a clean venv; smoke `n4a-datasets --help`.
- [ ] Verify the version appears on each registry (PyPI/crates/npm/CRAN).
