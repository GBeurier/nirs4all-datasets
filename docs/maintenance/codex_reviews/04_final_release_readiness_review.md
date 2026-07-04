# Codex Gate 4 — final release-readiness (nirs4all-datasets)

Per-repo final release-readiness is **consolidated into the ecosystem-level Gate 5**. The per-repo Codex
effort was concentrated on **Gate 3** (`03_main_diff_review.md`); the SHA-pinner is comprehensive
(56 pins, only `rust-toolchain@stable` left by design) so the "missed-a-workflow" defect class does not apply.

**Readiness snapshot:** `datasets` is a maturin (Rust+Python) package with R/MATLAB/WASM bindings and a
**multi-registry** release fleet (PyPI/crates.io/npm/CRAN/MATLAB), all **tag-gated**. Push-hardening added the
community-health set, SHA-pins, and CHANGELOG catch-up; **no code/ABI/release changes**.

**Documented / flagged (not changed here):**
- **License header mismatch** — `CHANGELOG.md` `SPDX-License-Identifier: MIT` vs pyproject `CeCILL/AGPL`.
  License identity is a maintainer decision (legally sensitive); reconcile before release.
- Release is an immutable multi-registry fan-out — dry-run each registry via dispatch first
  (`release_checklist.md`), tag the exact release commit, and handle partial-failure per the checklist.
- No enforced coverage floor.
