# Codex Gate 3 — main diff review (nirs4all-datasets)

**Reviewer:** Codex CLI 0.142.5 — `codex exec review --uncommitted`, 2026-07-04 (run in background; the diff of
56 action pins across 12 workflows exceeded the interactive timeout, so a longer budget was used).

## Verdict
> "The workflow pinning changes are mechanical" — no correctness/CI-break issue in the 56 SHA-pins.
Three actionable issues in the added maintenance metadata, all fixed.

## Findings & disposition

| # | sev | finding | disposition |
|---|---|---|---|
| P2 | minor | `quality_gates.md` documented `mypy .`, which descends into non-package data trees (`NIRS DB/...`) and aborts on duplicate modules. | **Fixed** — now `mypy --config-file pyproject.toml src` (matches CI). |
| P2 | minor | `CITATION.cff` `license` used non-canonical SPDX casing `CeCILL-2.1`. | **Fixed** — canonical `CECILL-2.1`. Kept the **list** form (valid CFF 1.2.0 for dual-licensing; Codex's "single SPDX expression string" suggestion does *not* validate in CFF, which has no expression grammar). The generator template was corrected so remaining repos inherit it; the already-pushed cluster/repository CITATIONs carry the same casing and are flagged for a touch-up in the cross-repo pass. |
| P3 | minor | dependabot `pip` scanned only `/`, missing `docs/requirements.txt`. | **Fixed** — added a second `pip` update for `directory: "/docs"`. |

## Verified during review
- SECURITY.md's "checksum-verified download" claim is accurate (repo uses `pooch` + `hashlib.sha256`).
- `release-*` workflows are tag-gated (`push: tags: v*` + `if: startsWith(github.ref,'refs/tags/v')`) — a
  branch push does not publish to any registry.
