# Final hardening report — nirs4all-datasets

**Date:** 2026-07-04 · **Branch:** `main` · **Operator:** Claude (Opus 4.8) · **Reviewer:** Codex CLI 0.142.5

## Summary
Pragmatic hardening of the DOI-pinned dataset catalog (maturin Rust+Python, multi-registry): added the
community-health set, SHA-pinned every third-party action across all 12 workflows (only `rust-toolchain@stable`
left, by design), caught up the CHANGELOG, and added a `docs/maintenance/` trail. **No code, ABI, or release
changes.** The `release-*` fleet is tag-gated, so this branch push does not publish.

## Baseline / commit
- **Baseline HEAD:** `c46042da` (origin/main; == `v0.3.2`, CI-green multi-registry release commit).
- **Commit:** *(this commit)* — community-health + 56 SHA-pins + CHANGELOG + docs/maintenance.

## Files
Added: `CODE_OF_CONDUCT.md`, `CITATION.cff`, `SECURITY.md`, `.editorconfig`, `.pre-commit-config.yaml`,
`.github/dependabot.yml`, `docs/maintenance/{repository_audit,quality_gates,release_checklist,final_report}.md`,
`docs/maintenance/codex_reviews/{03,04}_*.md`.
Modified: all 12 `.github/workflows/*.yml` (56 action SHA-pins), `CHANGELOG.md` (`[0.3.2]` consolidating 0.3.0–0.3.2).

## Checks
- YAML/CFF validated. Non-code change; the Rust build/tests run in CI (authoritative). Baseline release CI green at `c46042da`.
- **Codex Gate 3** — pins mechanical/valid; 3 metadata fixes (mypy gate target, CFF SPDX casing, dependabot /docs).
- **Codex Gate 4** — consolidated into ecosystem Gate 5.

## GitHub Actions (this push)
Branch-push gating runs (no publish): `ci` (Rust build + WASM + npm dry-run), `abi-check`, `docs`,
`version-guard`, `version-sync`. Verified green post-push (see run list for this commit).

## Residual risks / flags
- **`CHANGELOG.md` `MIT` SPDX header vs `CeCILL/AGPL` license** — left for the maintainer (legally sensitive).
- cluster/repository CITATIONs share the pre-fix `CeCILL-2.1` casing — touch up in the cross-repo pass.
- Multi-registry immutable release — see `release_checklist.md` (dry-run, exact-commit tag, partial-failure rule).
- No coverage floor; `rust-toolchain@stable` intentionally unpinned.

## Release readiness
**Push-hardening complete and CI-green.** Release remains a careful multi-registry operation (documented);
reconcile the CHANGELOG license header before tagging.

## 12-month maintenance
- Merge weekly Dependabot PRs (actions/pip/pip-docs/cargo) after CI-green.
- Keep `CHANGELOG.md` current; reconcile the license header.
- Before release: dry-run each registry via `workflow_dispatch`, then tag the exact release commit.
