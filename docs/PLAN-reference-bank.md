# Plan — `nirs4all-datasets` as a citable, reproducible **reference dataset bank**

**Date:** 2026-06-11 · **Status:** proposed (pending Codex + Claude review) · supersedes the *local
bulk-qualification* phase recorded in [`../ROADMAP.md`](../ROADMAP.md) (that phase is **done** and live).

This is the "retour complet" on the work to be done. It is grounded in the current code
(`access.py`, `schema.py`, `ingest.py`, `qualify/`, `site.py`) and in the new authoritative source
tree `NIRS DB/` (still extracting at the time of writing).

---

## 0. Verdict first

**The machinery for the vision already exists and works** (pooch DOI download + checksum verify +
cache, content-addressed manifests with SHA-256, semver versions, publication-grade identity cards,
Croissant + datasheet, an interactive site live on GitHub Pages, Dataverse publish/access, a
license/governance gate). The 254→250 catalog built from `nirs4all-lab/tabpfn_paper/data` proves it
end-to-end.

So the right move splits in two: **rebuild the catalog/data from scratch** with `NIRS DB/` as the
single source of truth, but **extend the codebase in place** rather than rewriting working modules.

**The new DB replaces the old on any conflict — this is a replacement, not an update** (user, pre-v1).
We are not at v1, so there is **no id/version/DOI stability contract** to preserve: the prior
tabpfn-based catalog (255 descriptors) is *superseded*, ids may change, and where `NIRS DB/` and the
old catalog disagree, `NIRS DB/` wins outright. No rename-maps, no merge, no migration shims — the old
catalog is regenerated from the new source. "From scratch" therefore applies to the **data sourcing and
the provenance model**; the package code (download/checksum/cards/site/publish) is kept and extended.

What is genuinely missing (the real work):

1. **A first-class origin-source registry.** Today the original home of a dataset is smuggled into
   free-text fields — e.g. `provenance.contributor: doi.org/10.57745/WVAPOL`,
   `citation: 'DOI: 10.1002/ppj2.70059'`. It is *present but not actionable*: nothing can fetch from it.
2. **A multi-method fetcher** that pulls **from the original spots** (Zenodo / figshare / data-gouv /
   URL), not only from a personal Dataverse — with the personal Dataverse as the licensed-data fallback.
3. **Acquisition scripts** for datasets that are "ailleurs" and need assembly, not a single download.
4. **Anonymization & normalization as options** (today `anonymization_status` is only a *string*).
5. **Publications → citations**, wired from `NIRS DB/Publications/` into each descriptor.
6. **The catalog re-based on `NIRS DB/`** (richer: `multimachines/`, more families, the papers).
7. **Web page refreshed** with the new datasets, license-respecting.

---

## 1. What already exists (do not rebuild)

| Capability | Where | State |
|---|---|---|
| On-demand download by DOI, checksum-verified, OS-cached (pooch) | `access.fetch_public` | ✅ works |
| Private/restricted download via Dataverse access API + token (no key leak on S3 redirect) | `access.fetch_private` | ✅ works |
| Local-first `load(name)` consumer API + lazy top-level wrappers | `access.load`, `__init__` | ✅ works |
| Content-addressed manifest: raw+canonical SHA-256, sizes, Dataverse file-ids, native checksums | `manifest.py`, `schema.FileEntry` | ✅ works |
| Incrementality (rebuild only on input change; `descriptor_hash` excludes DOI/version) | `manifest.needs_rebuild` | ✅ works |
| Publication-grade cards: PCA/effective-rank, train↔test shift, per-partition/-class stats, 5 plots | `qualify/` | ✅ works |
| Croissant 1.0 JSON-LD + Datasheets-for-Datasets `card.md` | `qualify/croissant.py`, `datasheet.py` | ✅ works |
| Catalog index with staleness flags; interactive static site (search/filter/sort + ID-card pages) | `catalog.py`, `site.py` | ✅ live |
| Two-level validation (schema validity vs publishability) + governance gate | `schema.publication_blockers` | ✅ works |
| Bulk fleet path: `bootstrap` → `build-all` (parallel, failure-isolated) → `site` | `discover.py`, `bulk.py` | ✅ works |
| Dataverse publish / versioned update / grant / revoke / restrict | `publish.py`, `dataverse.py` | ✅ works (mock-tested) |
| Boundary rule: reuse `nirs4all`/`nirs4all-io`, never re-implement NIRS/IO | everywhere | ✅ held |
| 3-tier storage: git=descriptors+cards, Dataverse=bytes, local cache | `.gitignore` | ✅ holds |

## 2. The vision → capability gap analysis

| # | Vision (user's words) | Exists today | Gap / work |
|---|---|---|---|
| V1 | Download datasets online by known id + DOI/Zenodo | DOI via pooch (resolves Zenodo/figshare/Dataverse DOIs) | **Origin not modeled.** DOI is the *personal* `dataverse.doi`, or free text. Need structured `sources[]`. |
| V2 | "…soit ailleurs et y a des scripts" | — | **Script-based acquisition** route + `scripts/` convention. |
| V3 | License-gated access (some only with token) | publishability gate + token download | Mostly ✅; extend to per-source `access: open\|token\|manual`. |
| V4 | Local documented base; keep only lib-necessary bytes | `.gitignore` tracks descriptors/cards only | ✅; define `NIRS DB/` ↔ repo relationship (D2). |
| V5 | Exhaustive diagnostics; hashes/versions; traceability; scientific rigor | cards + manifest hashes + semver | Surface the **full chain** (origin→raw→canonical→card→DOI) + **citation bundle** in card/site. |
| V6 | Anonymize + normalize, as **options** | `anonymization_status` string only | **Real opt-in transforms** (D3). |
| V7 | Pull remotely from **original spots** OR personal Dataverse for licensed | personal Dataverse only | **Dual-remote fetcher** keyed on `sources[]` (V1+V7 together). |
| V8 | Orchestrated, reproducible, citable, benchmark/compare | CLI orchestration + manifests + Croissant | ✅ core; add citation export + (later) `nirs4all-arena` hook. |
| V9 | Update the web page (license-respecting) | `site.py` → GH Pages | Regenerate with re-based catalog; metadata-only for restricted. |

## 3. The `NIRS DB/` corpus (authoritative source)

Top level (mid-extraction, ~1912 files so far):

```
NIRS DB/
  DatabaseDetail.xlsx, DatabaseDetailGreg.xlsx   master metadata sheets (two; reconcile)
  regression/<FAMILY>/<LEAF>/…                    AMYLOSE COLZA CASSAVA ALPINE CORN BEER DIESEL …
  classification/<FAMILY>/<LEAF>/…                Cassava COFFEE_orig MALARIA ARABIDOPSIS_CEFE FUSARIUM
                                                  FLOPP RRUFF ECOSTRESS Wood_Sustainability MILK PISTACIA
                                                  ECOSIS TIMESERIES
  multimachines/<FAMILY>/…                        GRAPEVINE_LeafTraits, CORN, WASTE_todo, VITIS_todo  ← multi-instrument
  Publications/…                                  the actual papers (classification/, todo/)
  chantiers/rtbfoods/…                            work-in-progress (NOT ready)
```

How it re-bases the catalog (vs the prior `tabpfn_paper/data`):

- **Authoritative provenance.** `Publications/` holds the papers → real citations + `related_publications`.
- **`multimachines/`** = genuinely multi-instrument datasets (e.g. GRAPEVINE: ASD / MicroNIR / NeoSpectra).
  Today these are modeled as **separate single-source leaves per instrument-combo** (`n_sources: 1`);
  decision **D4**: keep per-combo leaves, or model true multi-source (`n_sources > 1`, X-file list).
- **WIP markers.** `*_todo`, `chantiers/`, `Publications/todo/` → **skip** (not reference-ready); log what was skipped.
- **Two master sheets** (`DatabaseDetail.xlsx` + `…Greg.xlsx`) → reconcile; richer than the ~65-row sheet used before.

**Embargo:** `NIRS DB/` is still extracting; no processing until it settles (≈20–30 min from task start).
Until then: schema + fetcher + scripts design, which do not depend on the bytes.

## 4. Proposed architecture (additive, boundary-safe)

### 4.1 Origin-source registry — `schema.py` (new `OriginSource`, `descriptor.sources: list`)

```python
class SourceKind(StrEnum):
    DATAVERSE = "dataverse"   # any Dataverse instance (data-gouv, CIRAD, Harvard…)
    ZENODO    = "zenodo"
    FIGSHARE  = "figshare"
    URL       = "url"          # direct file(s) over http(s)
    SCRIPT    = "script"       # reproducible acquisition script (see 4.3)
    MANUAL    = "manual"       # license requires manual download; we only document + checksum

class SourceAccess(StrEnum):
    OPEN = "open"; TOKEN = "token"; MANUAL = "manual"

class OriginSource(BaseModel):
    kind: SourceKind
    locator: str                 # DOI ('10.x/y'), URL, or 'scripts/<id>.py'
    access: SourceAccess = OPEN
    license: str | None = None   # SPDX of the source if it differs from governance.license
    title: str | None = None
    expected_files: list[str] = []     # basenames this source yields (→ checksum map)
    notes: str | None = None
```

- `DatasetDescriptor.sources: list[OriginSource] = []` — the **original homes**; distinct from
  `dataverse: DataverseRef` (the *personal* republish location + pinned DOI for the licensed fallback).
- **Excluded from `descriptor_hash`** (like `dataverse`/`generation`): editing where data is fetched
  from must not trigger a canonical rebuild.
- Migration: lift the misplaced `provenance.contributor: doi.org/…` / `citation: 'DOI:…'` into
  `sources[]` (`kind: dataverse|zenodo`, `access: open`) automatically during the re-base.
- Validation: `validate.py` gains a check that a **public** dataset has ≥1 `access: open` source *or*
  a personal `dataverse.doi`; a **restricted** one is allowed to have only `manual`/`token` sources.

### 4.2 Multi-method fetcher — `access.py`

`load(name)` resolution order becomes:
1. **Local** `datasets/<id>/canonical` → load (unchanged).
2. **Origin sources** in order: `open` `dataverse`/`zenodo`/`figshare` DOI via pooch (already
   supported by pooch's DOI handler); `url` via verified direct GET; `script` via the runner (4.3).
   Each verified against the manifest's canonical SHA-256 (when the source yields canonical files) or
   the source's `expected_files` checksums (raw).
3. **Personal Dataverse fallback** (licensed/restricted): existing `fetch_private` with token.
4. Else error with an actionable message (which `manual` source to download by hand).

Token hygiene preserved (no `X-Dataverse-key` on the S3 redirect). All paths checksum-verify before
caching. Tests: mocked `requests.Session` + a fake pooch registry, **no network** (existing pattern).

### 4.3 Acquisition scripts — `scripts/<id>.py` + a runner

For "ailleurs + scripts" datasets. Convention: a script exposes `fetch(dest: Path) -> list[Path]`
(pure download/assembly, no NIRS logic), pinned and checksum-gated. The `script` source records the
script path + the expected output checksums. The runner executes it into the cache and verifies. This
is the *only* place arbitrary acquisition code lives; the boundary rule still bars NIRS/IO logic here.

### 4.4 Anonymization & normalization — opt-in (`organize`/`access` options)

- **Anonymize** (`anonymize: bool`): drop or hash identifying metadata columns + sample ids at the
  canonical step; record exactly what was removed; set `governance.anonymization_status` honestly
  (no more "Not assessed"). Default **off** (reference fidelity); per-dataset opt-in in the descriptor.
- **Normalize** (`normalize: 'none'|'canonical'`): **canonical** = unit/format normalization only
  (axis to nm/cm⁻¹ canonical, consistent dtype/orientation). **Scope guard (D3):** spectral
  *preprocessing* (SNV, derivatives, resampling to a common grid) is **nirs4all pipeline territory** and
  must NOT live here — that would break the boundary rule. Confirm the intended meaning of "normalise"
  with Codex before building anything beyond unit/format canonicalization.

### 4.5 Exhaustive diagnostics & traceability chain

Surface in `card.json` + the site, per dataset: `origin DOI/URL → raw sha256 → canonical sha256 →
card → personal DOI/version`, plus a **citation bundle** (paper DOI/BibTeX from `Publications/`,
dataset DOI). The numbers already exist in the manifest; this is plumbing them into the card section
and the ID-card page. No new NIRS compute.

### 4.6 Web page

Regenerate `site/` from the re-based catalog. Restricted datasets: **metadata only** (no byte links;
show the `manual`/`token` access note + license). Add an "origin & citation" block per card. Keep the
GH Pages deploy (light deps; `site.py` is pure rendering). Landing page (`nirs4all-webpage`) update
only if the user means that one too — confirm scope (D5).

## 5. Phased execution

- **P0 — design sign-off.** This doc → Codex (gpt-5.5, read-only) + a Claude Fable review agent →
  resolve blockers. *(does not touch `NIRS DB/`)*
- **P1 — schema.** `OriginSource` + `sources[]` + validation + tests + enum-mirror guard.
- **P2 — fetcher + scripts.** `access.py` dispatch + `scripts/` runner + mocked tests.
- **P3 — re-base on `NIRS DB/`** *(after extraction settles)*. Point `bootstrap` at `NIRS DB/`;
  reconcile ids with the current 255 (no silent drops); lift origins into `sources[]`; wire
  `Publications/` citations; skip WIP; `build-all` → canonical + cards.
- **P4 — anonymize/normalize options** (scope per D3).
- **P5 — diagnostics/traceability + citation bundle** in card/site.
- **P6 — web page** regenerate (license-respecting).
- **P7 — green gate** (ruff, mypy, `validate.py`, catalog regen committed, pytest) → **commit + push**
  (final Codex validation before push).

## 6. Decisions needing validation (→ Codex; the user delegated confirmation to Codex)

- **D1.** ~~Extend vs rewrite~~ **RESOLVED (user):** catalog rebuilt from `NIRS DB/`, new replaces old
  on conflict, pre-v1 so no stability contract; code is extended in place. Codex to sanity-check only.
- **D2.** `NIRS DB/` = read-only authoritative master (raw + pubs + scripts); repo stays
  descriptors/cards-only; pubs registered as citations (heavy PDFs not in git). Confirm.
- **D3.** Scope of "normalise" — unit/format canonicalization only, *not* spectral preprocessing
  (boundary). Confirm. Scope of "anonymise" — metadata columns + sample ids. Confirm.
- **D4.** `multimachines/` — keep per-instrument-combo single-source leaves, or model true multi-source
  (`n_sources > 1`). *(Recommend: keep per-combo now; add true multi-source only if a leaf ships one
  aligned sample set across instruments.)*
- **D5.** "la page web" = the generated catalog site (`site/` → GH Pages), or also the
  `nirs4all-webpage` landing page? *(Assume the catalog site unless told otherwise.)*

## 7. Risks & mitigations

- **Re-base churn.** Pre-v1, no stability contract — `NIRS DB/` wins on conflict, old catalog is
  regenerated. → Still **report** adds/removes/renames for transparency (and to catch extraction gaps),
  but no preservation requirement; the new source is authoritative.
- **`NIRS DB/` heavy + mid-extraction.** → Honor the embargo; one dataset per worker; float32; subsample
  for PCA/plots; per-section timeouts (already in `bulk.py`).
- **Two xlsx sheets disagree.** → Deterministic precedence (prefer the richer/most-recent), log conflicts.
- **Original-source links rot.** → Always keep the personal-Dataverse fallback + manifest checksums;
  `manual` sources documented even when not auto-fetchable.
- **Scope creep on normalise/anonymise.** → Gate on D3 before writing code.

## 8. Boundary compliance (non-negotiable)

No NIRS/IO/ML logic added. Reading/qualifying stays `nirs4all`; instrument files stay `nirs4all-io`;
the only new code is (a) descriptor *authoring* fields, (b) *acquisition* (download/assembly) — both
already this package's own domain — and (c) descriptive card plumbing. Anonymise/normalise stay at
unit/format/metadata level; spectral preprocessing remains in `nirs4all`.

---

# v2 — reviews incorporated

Pre-implementation review by **Codex (gpt-5.5, read-only)**: *proceed-with-changes*, 4 BLOCKER /
7 MAJOR / 1 MINOR. Resolutions below are the **design of record** and supersede any conflicting bullet
above. Core theme: keep four concerns separate — **acquisition-provenance**, **processing-hash**,
**card-freshness**, **publishability**. *(A second, independent Claude Fable review is pending; its
delta will be appended.)*

### Blockers (resolved)

1. **(B1) Two hashes, not one.** Cards/site freshness is keyed solely on `descriptor_hash`
   (`catalog.py:37`); if cards show origin/citation, editing `sources[]` must refresh the card without
   forcing a canonical rebuild. → Keep **`processing_hash`** (today's `descriptor_hash`; excludes
   `dataverse`, `generation`, **and `sources`**) for canonical rebuilds; add **`metadata_hash`**
   (includes `sources[]`, citations, license/access notes) for card/site re-render. `catalog.py`
   staleness checks both: stats from a matching `processing_hash`, origin/citation block from a
   matching `metadata_hash`.
2. **(B2) `SourceArtifact`, not `expected_files`.** Checksum-gated acquisition needs per-file detail:
   `SourceArtifact{ path, sha256, size?, role: raw|canonical, source_path? (unpack/rename) }`. Required
   for `url`/`script`/`manual` sources; `OriginSource.artifacts: list[SourceArtifact]`.
3. **(B3) Canonical-download ≠ raw-origin acquisition.** Add `OriginSource.mode: canonical|raw`.
   `canonical` sources must provide the full canonical set incl. `nirs4all_config.json` (verified vs
   manifest canonical SHA-256). `raw` sources download to **staging** → verify raw hashes → run the
   existing `organize`/`ingest` → verify the resulting canonical hashes. The fetcher never assumes an
   origin yields canonical Parquet.
4. **(B4) Scripts are never auto-executed by `load()`.** Acquisition scripts are **opt-in** and
   interactive only (`n4a-datasets acquire <id>` / `load(..., allow_scripts=True)`), constrained to
   `scripts/<id>.py`, pinned by `script_sha256` + dependency pins, run in a temp dest, path-traversal
   rejected, with an acquisition log written into the manifest/card. The boundary rule still bars
   NIRS/IO logic in scripts (download/assembly only).

### Majors (resolved)

5. **(M5) Two-level validation preserved.** `OriginSource` gets only *syntactic* model validation
   (valid descriptors stay valid even when restricted/internal). The "public ⇒ has an `open` source or
   a personal DOI" rule goes into `publication_blockers()` + `validate.py --check-publish` **only**.
6. **(M6) Token hygiene generalized.** `access: token` stores a **`credential_ref`** (a name), never a
   token; requires a Dataverse `instance`; reuses the no-redirect-with-key pattern; **never** sends a
   token to a generic `url` source.
7. **(M7) Version-pinned locators.** Prefer version-specific Zenodo/figshare/Dataverse DOIs (not
   "latest"). A checksum mismatch is a **provenance failure** (hard error), not a silent fallback;
   the personal-Dataverse fallback is for rot/permissions only, never to paper over upstream drift.
8. **(M8) Anonymization covers raw too.** Publishing uploads `raw/` + `canonical/`. If `anonymize` is
   on: transform the staged raw as well, **or** exclude raw from public payloads, **or** force
   restricted publication — plus file-scope anonymization evidence in the card (not just a status string).
9. **(M9) D4 locked: per-instrument single-source leaves.** GRAPEVINE ASD/MicroNIR/NeoSpectra stay
   related single-source leaves (profiling reads source 0; schema has one `instrument`). True
   `n_sources > 1` only later, with per-source instrument metadata + multi-source cards.
10. **(M10) Explicit replacement workflow.** Re-base stages a **fresh** catalog, emits an
    add/remove/rename/conflict/skipped-WIP report, then replaces descriptors/cards under an explicit
    `--replace-catalog` step (deletes managed descriptors not regenerated; loudly flags any human-edited
    conflict). "New replaces old" is a deliberate, reported action — never a silent drop.
11. **(M11) Structured citations + release manifest.** Replace `related_publications: list[str]` with
    `PublicationRef{ doi, title, authors[], year, bibtex, pdf_sha256? }`. Add a **catalog release
    manifest** (git commit, package version, `NIRS DB/` source-tree fingerprint, aggregate hashes,
    bank DOI) + a `CITATION.cff`, so the *bank itself* is citable, not just each dataset.

### Minor (resolved)

12. **(m12) Normalise boundary confirmed** (unit/format only; no SNV/derivative/resample). Record the
    `normalize`/`anonymize` choices in the **converter config** so they participate in incrementality;
    use `nirs4all`/`nirs4all-io` primitives for any physical unit handling.

### Claude Fable review — delta (independent, *proceed-with-changes*)

A second read (Claude Fable agent) inspected `NIRS DB/` + the xlsx directly and **confirms both
blockers**. Its additional/sharper findings, folded in (these win where they conflict with v2 above):

- **(C-A) Manifest is the single checksum authority — reconciles B2.** Do **not** put per-file SHA-256
  in `sources[]` (a parallel, hash-excluded store that can drift). `OriginSource` carries
  locator/access/license/title + `expected_files` as **basenames only** (what to fetch). Verification
  always runs against the committed manifest (`FileEntry.sha256`, `Provenance.raw_sha256`). → **drop the
  `SourceArtifact` checksum model;** keep an optional archive-member mapping only if a real dataset needs
  unpacking (YAGNI until then).
- **(C-B) Origin fetch is raw → re-ingest → *reproduced* canonical, never byte-pinned.** Re-ingesting
  raw won't byte-match the published Parquet (float32/zstd/nirs4all-version drift). So: verify raw vs the
  committed manifest raw hashes, re-ingest locally, load **without** asserting canonical byte-equality,
  and **mark the card** "reproduced canonical (not the pinned artifact)". Never advertise
  canonical-checksum verification for origin sources.
- **(C-C) Classify DOIs by prefix at migration — provenance integrity.** The xlsx `Ref`/`Source`
  columns mix **data-repo** DOIs (Zenodo `10.5281`, figshare `10.6084`, Dataverse
  `10.7910/10.18710/10.34725/10.57745/10.15454`) with **journal** DOIs (`10.1002/10.1016/10.1038/…`) in
  5+ text formats. → data-prefix → `sources[]`; publisher-prefix → `related_publications`; reset
  `provenance.contributor`/`owner_steward` to real org/person strings; unclassifiable → `warnings`,
  never silent-drop.
- **(C-D) Scripts are maintainer-ingest-only.** Run during `bootstrap`/`build-all` to produce canonical
  bytes that go to the personal Dataverse; **consumer `load()` never executes a script** (a
  script/manual dataset with no canonical copy → actionable error). Stricter than v2-B4 — adopt it.
- **(C-E) Metadata persistence is a prerequisite for anonymise.** `write_canonical` writes only X/Y —
  the `M` files (sample ids + covariates) are dropped (`ingest.py:250-263`). So anonymise has nothing to
  act on, **and** the multimachines cross-instrument join key lives in those M files. → **P4 becomes:
  optionally persist metadata canonically (opt-in), then descriptor-driven drop/hash of named columns**
  (no heuristic PII detection) with a **stable keyed hash shared across sibling leaves** so joins
  survive. If metadata is not persisted, anonymise is out of scope — say so, don't ship a no-op.
- **(C-F) Citations from xlsx DOIs via Crossref-at-build, committed.** `Publications/` is a heavy PDF
  dump (not in git, no machine link). Resolve BibTeX/CSL from the xlsx DOIs once at build, **commit** the
  resolved `PublicationRef` records; PDFs are offline convenience only.
- **(C-G) Re-base traversal + committed reconciliation.** `find_leaves` only scans
  `regression/`+`classification/` (`discover.py:117`) — extend to `multimachines/` with a **curated
  include-list**, excluding `chantiers/`, `unusableDB/`, `v2.0/`, `Publications/`. Emit a **committed**
  (not gitignored) tombstone/reconciliation report (added/renamed/removed + reason); handle orphans and
  human-managed (`managed:false`) descriptors explicitly.
- **(C-H) normalise = unit *labelling* only.** Even wavenumber↔wavelength *conversion* recomputes and
  reorders the axis (derived data). Canonical-normalise = dtype + orientation + unit label; **leave axis
  values native**. It is nearly a no-op (Parquet/float32 already happen) — keep it minimal.
- **(C-I) Publish-gate license check.** Add an **origin-license vs `governance.license` re-hosting
  compatibility** check to `publication_blockers()` (re-hosting NC/ND origin data as open violates the
  source license; nothing checks this today). Populate `instrument.model` (the leaf id encodes the
  device) + a shared group key so multimachines siblings stay linkable. Commit a **`NIRS DB/`
  source-tree fingerprint** so the catalog records "built from NIRS DB @ <hash>".
- **(C-J) Schema nits.** `SourceAccess.OPEN` (not `OPEN`); `Field(default_factory=list)`;
  `model_config = ConfigDict(extra="forbid")`; `SourceKind`/`SourceAccess` are **this package's** domain
  (acquisition), so keep them **out** of the nirs4all enum-mirror guard.

### Revised execution order (both reviews incorporated)

---

# Delivered (2026-06-11)

Implemented and green-gated (ruff + mypy + `validate.py`=485 + `pytest`=133 all pass; both reviews folded in):

- **P1 schema** — `OriginSource`/`SourceKind`/`SourceMode`/`SourceAccess` + `PublicationRef` +
  `descriptor.sources[]`; `related_publications` upgraded to structured `PublicationRef`;
  **hash split** (`descriptor_hash` excludes `sources`; new `metadata_hash` includes them);
  re-host-license check in `publication_blockers()`.
- **P2 fetcher** — `access.load()` resolves local → personal Dataverse DOI → **open origin** (canonical
  byte-verified; raw via `reproduce=True` → re-ingest, flagged *reproduced*) → actionable guidance.
  **Scripts are maintainer-only** (never executed on consumer `load`); token never sent to a
  non-Dataverse host.
- **P3 re-base** — `discover` walks `regression/classification/multimachines`, skips WIP
  (`_todo`/`chantiers`/`unusableDB`/`v2.0`/`Publications`); **DOI-prefix classification** (data →
  `sources[]`, journal → `related_publications`); honest steward (repo name, not the DOI);
  `instrument.model` from multimachines leaf names; family-level xlsx backfill; `bootstrap --prune`
  + committed `catalog/reconciliation.json`. Result: **484 datasets** (was 254); 3 managed orphans
  pruned; 44 `multimachines/CORN` exact-duplicate collisions dropped (kept `regression/CORN`).
- **P5 cards** — card `provenance` block (sources + structured publications) + `integrity.metadata_hash`
  + `integrity.traceability` (origin → raw → canonical hash chain). **build-all: 474 ok / 1 partial /
  8 failed** (genuine source X/Y row-count mismatches: rice_redox×3, wood_sustain; 4 ECOSIS quirks) /
  2 skipped → 476 cards.
- **P6 site** — "Origin &amp; citation" block per dataset page (locator links + provenance-chain
  summary); metadata-only, so license-respecting for restricted datasets.
- **gitignore** — `NIRS DB/`, `OneDrive_*.zip`, `.codegraph/` are heavy local sources, never committed.

**Deferred — P4 anonymise/normalise (optional, "au pire" per user).** The Claude review (C-E) showed it
is a *prerequisite-bearing* change: `write_canonical` drops the `M` metadata files (sample ids +
covariates), so anonymise has nothing to act on until metadata is persisted canonically — and that same
metadata is the multimachines cross-instrument join key. Doing it right (opt-in metadata persistence +
descriptor-driven column drop/hash with a stable keyed hash shared across sibling leaves) is a
canonical-format change requiring a full rebuild; sequenced as the next phase rather than shipped as a
no-op. `normalise` (unit-label only, C-H) is a near no-op and folded into that phase. **Not yet done.**

### Original phased plan (for reference)

P0 reviews ✅ → **P1** schema: `OriginSource`(`kind`,`mode`,`locator`,`access`,`credential_ref`,
`license`,`title`,`expected_files`[basenames],`notes`; `extra=forbid`) + `PublicationRef` + `sources[]`
+ **hash split** (`processing_hash` excl. dataverse/generation/sources · `metadata_hash` incl. sources/
citations) + source rule in `publication_blockers()` (incl. re-host-license check) — **no checksums in
sources** (manifest is authority) → **P2** fetcher (canonical-from-Dataverse vs raw-from-origin →
re-ingest → *reproduced* canonical, honestly flagged; version-pinned locators; per-kind token hygiene;
**scripts maintainer-only**) → **P3** re-base on `NIRS DB/`: curated-include traversal (+`multimachines/`,
−WIP), **DOI-prefix classification**, origins→`sources[]`, xlsx-DOI→Crossref→`PublicationRef`, committed
reconciliation report, source-tree fingerprint → **P4** (opt-in metadata persistence + descriptor-driven
anonymise w/ shared keyed hash) / normalise (unit-label only) → **P5** traceability chain + structured
citations + release manifest + `CITATION.cff` → **P6** web page (license-respecting) → **P7** green gate
+ commit/push (final Codex check).
