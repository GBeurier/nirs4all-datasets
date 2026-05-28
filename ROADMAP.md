# Roadmap — local bulk qualification + interactive catalog site

**Goal.** Make `nirs4all-datasets` work **fully locally** (no Dataverse): bulk-ingest a large
folder tree of NIRS datasets, compute **publication-grade statistical identity cards**, and render
an **interactive website** for the whole catalog and per-dataset ID cards. Online publishing stays
deferred (the Dataverse collections are not open yet); descriptors are produced **valid but not
auto-published**.

**Source data.** `/home/delete/nirs4all/nirs4all-lab/tabpfn/paper/data` (read-only), 5.6 GB
(was `tabpfn_paper/data`; the lab repo relocated it mid-session — once copied into this repo we no
longer depend on the lab path):
`regression/<FAMILY>/<LEAF>/…` and `classification/<FAMILY>/<LEAF>/…` plus a master metadata sheet
`DatabaseDetail.xlsx`. A **leaf** = one dataset = a directory holding semicolon-delimited
`Xtrain/Xtest/Ytrain/Ytest(/Mtrain/Mtest).csv` (a few use `Xcal/Xval`). Census: **254 leaf datasets**
(237 regression + 17 classification) across 40 families.

**Scope (confirmed): all 254 leaves.** Each split/preprocessing variant is its own card (per-split
train/test statistics are benchmark-relevant). Disk budget ≈ 5 GB raw copy + ≈ 1.5 GB canonical
Parquet. Heaviest families flagged: LUCAS 1.7 G, SOIL_ESDAC 718 M, ECOSIS 656 M, CASSAVA 477 M,
PISTACIA 330 M, GRAPEVINE_LeafTraits 321 M.

---

## What already works (verified by probe)

The existing pipeline is sound and the boundary rule (reuse `nirs4all`, never re-implement NIRS/IO)
holds. End-to-end probe on a clean dataset (`CORN/Corn_Oil_80_WangStyle_m5spec`): **folder load →
canonical Parquet → round-trip reload → card all succeed.** Confirmed facts:

- nirs4all's `FolderParser` recognizes `Xtrain/Ytrain/Xtest/Ytest/Mtrain/Mtest` (and `*cal/*val`),
  case-insensitive; auto-detects the `;` delimiter and the wavelength header; factorizes string class
  labels; task type can be forced via the config dict / `DatasetConfigs(..., task_type=…)`.
- The installed editable `nirs4all` is **0.9.1 but already contains the ParquetLoader fix**
  (`parquet_loader.py:170-173` drops `categorical_mode` & friends before `pd.read_parquet`), so the
  canonical round-trip the card builder depends on works. **No change to `nirs4all` is required.**
- `nirs4all-io` is **not installed**; irrelevant here — every leaf uses the tabular folder route.

## Blockers found (must fix) — both solved with nirs4all's own config knobs

1. **0-byte / empty metadata files crash the loader** (`COFFEE_orig`: empty `Mtrain.csv` →
   "File is empty or could not be read"). 4 leaves affected.
2. **NaNs in X trigger nirs4all's default `na_policy='abort'`** (`ALPINE_C_424_KS`: "NA values
   detected … column '1226' row 355").

Resolution (no re-implementation): build an **explicit config dict** for the folder route and
- set `train_x_params/test_x_params/train_y_params/test_y_params = {"na_policy": "ignore", …}`
  (`ignore` keeps NaN in place, all rows preserved → the card honestly reports `has_nan`/`nan_summary`;
  verified in `nirs4all/data/loaders/base.py:143`), and
- **omit** `train_group/test_group` when the metadata file is empty/0-byte (`*_group` keys are
  optional; loader skips when absent — `loader.py:285`). Metadata is best-effort, never a hard blocker.

---

## Architecture of the additions (all inside `nirs4all-datasets`, boundary-safe)

```
src/nirs4all_datasets/
  ingest.py            (MODIFY)  directory route → robust explicit config (na_policy, skip empty M)
  discover.py          (NEW)     walk a source tree → leaf datasets → auto descriptors (+xlsx enrich)
  bulk.py              (NEW)     orchestrate discover→organize→qualify over many leaves, in parallel
  qualify/metrics.py   (MODIFY)  + PCA/effective-rank, train↔test shift, per-partition/-class stats
  qualify/plots.py     (MODIFY)  + PCA scatter, per-class/quantile mean spectra, train/test overlay
  qualify/profile.py   (MODIFY)  assemble the new sections (stable keys, finite-sanitized, seeded)
  site.py              (NEW)     self-contained interactive site/ (index + per-dataset ID-card pages)
  cli.py               (MODIFY)  + `bootstrap`, `build-all`, `site` commands
catalog/datasets/<id>.yaml       254 auto-generated descriptors (git-tracked, marked auto)
site/                            generated site (gitignore: add `/site/`)
```

### Phase A — robust folder ingest (`ingest.py`) — *prereq for everything*
- New helper `build_folder_config(path, *, task_type) -> dict`: get the file→role mapping from
  nirs4all's `FolderParser` (reuse — do **not** re-derive filename rules), then (a) attach
  `na_policy="ignore"` + the detected `header_unit` to the `*_x_params`/`*_y_params`, (b) drop
  `*_group` whose file is missing/0-byte, (c) set `task_type`. `load_dataset()` for a directory uses
  this. Single `add` benefits too.
- Fallback: if `FolderParser` is awkward to call for a raw dict, build the mapping from a small
  documented stem table (the same stems FolderParser uses) — still nirs4all's vocabulary, no NIRS logic.
- Tests: fixtures with (a) NaN in X, (b) 0-byte `Mtrain.csv`, (c) header-only metadata, (d) `Xcal/Yval`
  naming, (e) string-label classification → all load and round-trip.

### Phase B — descriptor auto-generation (`discover.py`)
- `find_leaves(root)`: dirs containing a recognized X-train file. Returns `(family, leaf, task_hint)`.
- `dataset_id(family, leaf)`: slugify to `^[a-z0-9]+(_[a-z0-9]+)*$`, collision-safe, **stable**.
- Build a **schema-valid** `DatasetDescriptor`:
  - `task_type` from the `regression/`|`classification/` root, refined by Y dtype; `targets[0].name`
    from the Y header (or xlsx `Trait`); `classes` = factorize-order labels read from raw `Ytrain`
    for classification.
  - `instrument`: modality NIR (default), `axis_unit` from header detection (nm vs cm⁻¹), `signal_type:
    auto`.
  - `provenance.contributor`, `citation`, `governance.license`, source/reference: from
    `DatabaseDetail.xlsx`, matched by leaf `Dataset` name (then family). License string → SPDX
    (`CC0 1.0`→`CC0-1.0`, `CC BY 4.0`→`CC-BY-4.0`, `etalab 2.0`→`etalab-2.0`, `GPL (>= 2)`→
    `GPL-2.0-or-later`); unknown → `LicenseRef-<raw>`. Unmatched leaves → conservative defaults +
    a `provenance.warnings` note that the descriptor was auto-generated.
  - **Governance for local-only:** `visibility: restricted`, `confidentiality_class: internal`.
    These are **valid but intentionally not publishable**, so we never trip the open-license/DOI gate
    while the collections are closed. (Publishing later = edit governance + run the existing publish flow.)
- Idempotent: don't clobber a descriptor a human has edited (detect a `x-autogenerated: true` marker;
  regenerate only auto ones unless `--force`).

### Phase C — enriched, publication-grade cards (`qualify/`)
New **metrics** (pure numpy/scipy, JSON-stable keys, `None`+warning on degenerate input):
- **PCA / dimensionality:** explained-variance ratio of the first *k* PCs, cumulative components to
  reach 95 %/99 % variance, **effective rank** (participation ratio). Computed on standardized,
  **row-subsampled** (≤ 4000) and SVD-truncated X to stay fast on LUCAS-scale matrices.
- **Train↔test shift:** target mean/std shift + 2-sample KS on y; X centroid distance in PC space.
- **Per-partition target stats** (train vs test) and **per-class counts/fractions per partition**.
- Keep existing spectral noise/smoothness/dynamic-range, class balance, wavelength spacing.
- **Outliers:** keep `XOutlierFilter` but run it on the **PCA-reduced** space (guard against
  high-dim covariance blow-ups / MCD slowness); already wrapped best-effort.

New **plots** (Agg backend, seeded, subsampled for big sets):
- PCA scatter (PC1×PC2) colored by target (continuous) or class.
- Per-class mean spectra (classification) or quantile-banded mean spectra (regression).
- Train vs test mean-spectrum overlay.
- Keep mean±std envelope and target distribution.

`profile.py` assembles these under new top-level keys (`dimensionality`, `shift`, per-partition
blocks) without breaking existing keys; everything finite-sanitized, `generated_at` still the only
volatile field. The datasheet (`card.md`) gains a short stats section; Croissant unchanged.

### Phase D — interactive static site (`site.py`)
- `build_site(root, out_dir)`: read `catalog/datasets.yaml` + every `datasets/<id>/card.json`,
  copy each dataset's PNG assets, and emit a **self-contained** `site/`:
  - `index.html` — summary header (counts, totals, task/signal/domain breakdown) + a **client-side
    searchable / sortable / filterable** table of all datasets. **Data is embedded inline** as a JS
    const (so it works from `file://` with no fetch/CORS issue *and* under `python -m http.server`).
  - `dataset/<id>.html` — the full ID card: identity, KPI strip, plots, statistics tables (spectral,
    targets, dimensionality, shift, quality), datasheet, provenance & governance, and download links
    (`card.json`, `croissant.json`). Static HTML, no fetch.
  - `assets/style.css` (+ tiny `app.js` for the index). Clean, responsive, teal/cyan to match the
    ecosystem. No build step, no external CDN.
- CLI `n4a-datasets site --root . --out site/`. Add `/site/` to `.gitignore`.
- **docs/ reconciliation:** the standalone site is the catalog browser. `docs/gen.py` (Sphinx/MyST)
  is redundant for dataset pages at 254-row scale → **remove `docs/gen.py` and the `datasets/index`
  toctree entry** (no dead code), keeping `docs/` for narrative docs only. *(Open for Codex: keep vs
  remove.)*

### Phase E — bulk CLI + execution (`bulk.py`, `cli.py`)
- `n4a-datasets bootstrap <source_tree> [--xlsx PATH] [--force]` → write/refresh all descriptors.
- `n4a-datasets build-all [--workers N] [--only PATTERN] [--skip-assets]` → for each descriptor:
  `organize` (copy raw → canonical, manifest, incremental skip) then `build_card`; **process pool**
  (card building is CPU-bound, independent); per-dataset status captured; failures isolated
  (one bad dataset never aborts the run). Then `build_catalog` + `build_site`.
- A `bulk_report.json` (and console summary): counts ok/partial/failed with reasons; never silently
  truncates — any skipped/failed leaf is listed.

### Phase F — green gate + verification
- `ruff check .`; `mypy --config-file pyproject.toml src`; `python catalog/scripts/validate.py`
  (254 descriptors valid); regenerate `catalog/datasets.yaml` and confirm committed; `pytest -q`
  (existing + new tests for discover, robust ingest, enriched metrics, site).
- Spot-check 3 cards (a clean one, one with NaN, one classification). **Screenshot** the generated
  `index.html` and one `dataset/<id>.html` in a browser to confirm rendering.

---

## Execution order & milestones
1. **A** robust ingest (unblocks all) → tests green.
2. **C** enriched metrics/plots/profile → card schema stable on the 3 probe datasets.
3. **B** discover + descriptor generation → 254 descriptors written & schema-valid.
4. **E** bulk orchestration → run on a 5-dataset sample, then **all 254** (parallel), produce report.
5. **D** site generator → build `site/`, screenshot-verify.
6. **F** full green gate.

## Risks & mitigations
- **Runtime over 254 (heavy families).** Parallel process pool; subsample rows for PCA/plots; PCA-space
  outliers; per-dataset timeout + graceful failure. Expect tens of minutes to ~1–2 h wall-clock.
- **Memory on LUCAS-scale X.** Stream to float32; cap plotted/PCA rows; never hold all 254 in memory
  (one dataset per worker at a time).
- **Disk ≈ 6–7 GB** under `datasets/*/raw` + `*/canonical` (both gitignored). Acceptable; documented.
- **254 auto descriptors committed.** Small YAMLs, clearly marked auto-generated; reviewable/editable;
  they are the catalog's source of truth.
- **`robust_mahalanobis` on high-dim X** can be slow/singular → run on PCA-reduced space, best-effort.

## Boundary compliance (non-negotiable)
No NIRS/IO/ML logic is re-implemented. Reading/qualifying = `nirs4all` (`DatasetConfigs`,
`get_dataset_metadata`, `detect_signal_type`, `XOutlierFilter`, `core.metrics`); file→role mapping =
nirs4all `FolderParser`; the only new compute is descriptive statistics nirs4all does not expose
(PCA summary, shift, per-partition aggregates) — pure numpy/scipy in `qualify/metrics.py`, exactly the
gap this package already owns.

## Out of scope (now)
Dataverse publish/DOI (collections closed); `nirs4all-io` instrument-file route; editing `nirs4all`.

---

# v2 — Codex review incorporated (gpt-5.5, xhigh)

A pre-implementation review (`codex exec`, read-only) raised 4 BLOCKER / 11 MAJOR / 5 MINOR findings.
Resolutions below **supersede** any conflicting bullet above. Verified nirs4all APIs to reuse:
`nirs4all.analysis.projections.compute_pca_projection`, `nirs4all.analysis.transfer_metrics`
(`TransferMetricsComputer`), `nirs4all.data.parsers.normalizer` (`ConfigNormalizer.normalize` /
`normalize_config`), `nirs4all.data.detection.detector` (`AutoDetector` / `detect_file_parameters`),
and `XOutlierFilter` (already PCA-reduces to 20 comps internally).

**Data facts that close several findings (verified):** every leaf has exactly one single-column Y →
**no targetless and no multi-target datasets** in this corpus; one leaf uses `Xcal/Yval`
(`COFFEE_sp/Species_56_Bagnall`), handled by the parser; no multi-source leaves.

1. **(B1) `extra="forbid"` rejects an `x-autogenerated` marker.** → Add a real schema submodel
   `Generation{ managed: bool, generator: str, generator_version: str, source_relpath: str|None,
   source_fingerprint: str|None, xlsx_row: int|None }` on `DatasetDescriptor` (`generation: Generation|None`).
   It is excluded from `descriptor_hash` (like `dataverse`) so writing the fingerprint doesn't self-trigger rebuilds.
2. **(B2) descriptor→source mapping for `build-all`.** → `generation.source_relpath` (relative to a
   source root). `build-all --source-tree <root>` resolves `root/source_relpath`. Solves B1+B2+idempotency together.
3. **(B3) `na_policy` must also be in the canonical Parquet config.** → `write_canonical()` writes
   `train_x_params/test_x_params = {"header_unit": …, "na_policy": "ignore"}` (and the same on Y params)
   into `nirs4all_config.json`, so `build_card()` reloading canonical Parquet never aborts on NaN.
4. **(B4) targetless not wired through schema/consumers.** → **Out of scope** (no targetless leaf exists);
   no schema change. Documented.
5. **(M5) multi-target.** → None exist, but generate **one `Target` per Y column** generically (cheap, correct);
   per-target + per-partition stats handle the single-target case naturally.
6. **(M6) FolderParser fallback table re-implements nirs4all.** → **Drop the fallback table.** Use
   `ConfigNormalizer().normalize({"folder": str(leaf)})` (or `FolderParser().parse`) to get the config,
   then augment params only.
7. **(M7) header-unit detection.** → Use `detect_file_parameters()`/`AutoDetector` for delimiter/decimal/header;
   for the nm-vs-cm⁻¹ *label*, prefer instrument/xlsx metadata, else the verified range rule (nm if max≤2600
   after stripping quotes/`_nm`), recording it in `instrument.axis_unit` with a confidence note.
8. **(M8) incrementality misses converter config.** → Compute the augmented folder config, hash it, pass as
   `converter_config` to **both** `needs_rebuild()` and `build_manifest()`; store in the manifest.
9. **(M9) organize recopies raw before deciding to skip.** → Hash from the **source** (mapped to expected
   `raw/` relpaths) and run `needs_rebuild` *before* copying; copy only when rebuilding; atomic staging.
10. **(M10) restricted/internal is not an honest gate.** → Represent honestly: `confidentiality_class:
    public` for open-licensed datasets / `internal` for unknown-license; `visibility: restricted` is the
    *workflow* state (not yet published). No fake lock; publishing later is the intended explicit action.
11. **(M11) class-name recovery fragility.** → Take class names from the authoritative nirs4all load where
    exposed; validate train/test class-set consistency; record unseen-test-class labels as a hard warning.
12. **(M12) integer regression misclassified.** → The `regression/`|`classification/` **root is authoritative**
    for `task_type`; Y dtype only emits a validation warning.
13. **(M13) PCA/effective-rank honesty.** → Full SVD on the **capped, NaN-imputed** subsample (record
    `n_rows_used`, `n_components_computed`, `seed`); report censored `">k"` + warning when truncated.
    Reuse `compute_pca_projection`.
14. **(M14) shift metrics.** → Regression: KS + Wasserstein + standardized mean difference on y. Classification:
    class-proportion delta + Jensen–Shannon. X-shift: scaler+PCA **fit on train only**, project test; reuse
    `transfer_metrics.TransferMetricsComputer` where it fits.
15. **(M15) NaNs break PCA/outlier.** → Metrics-level finite policy: impute NaN with **train** column means for
    PCA/outlier inputs, report affected rows/features/cells, **never** change reported sample counts
    (`has_nan`/`nan_summary` stay from the raw dataset).
16. **(M16) duplication of nirs4all.** → Reuse `projections`, `transfer_metrics`, `XOutlierFilter`; only the
    thin descriptive glue (per-partition aggregates, censored-rank summary) stays here.
17. **(M17) LUCAS-scale perf.** → float32 throughout; cap workers by memory; subsample for optional
    metrics/plots; per-section timeouts; a failed optional section → `None` + warning, never a failed dataset.
18. **(M18) don't remove `docs/gen.py` yet.** → **Keep** the Sphinx bridge and its toctree; the standalone
    `site/` is the primary browser, built independently. No docs deletion.
19. **(M19) inline site data.** → Index embeds **summary rows only** (not full cards/PCA coords), JSON
    `<\/`-escaped; each dataset page is self-contained and also copies its `card.json`/`croissant.json` beside it.
20. **(M20) tests + report.** → Add tests: Generation-field validation, source-mapping stability, **canonical
    NaN round-trip**, ambiguous xlsx match, id-collision, failure isolation, stale-card rebuild, the `Xcal/Yval`
    leaf. `bulk_report.json` is deterministic and **gitignored** (it carries local paths).

**Revised execution order:** A′ = schema `Generation` field + `write_canonical` na_policy + robust
normalize-based ingest + source-aware incremental organize → C′ enriched metrics/plots reusing nirs4all
analysis → B′ discover/descriptors (root-authoritative task, honest governance, per-column targets,
source_relpath) → E′ bulk orchestration (capped workers, deterministic gitignored report) → 254 run →
D′ site (summary index + self-contained pages) → F green gate (+ new tests).
