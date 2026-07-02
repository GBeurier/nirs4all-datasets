# Design — reference NIRS dataset bank

*v1 — rephrased from your annotations. Reference document for rethinking the project before the full
analysis and implementation. Annotate / correct freely.*

---

## 1. Vision

A **versioned and qualified database of raw NIRS datasets**, **cataloged and linked to its sources**
(we never republish other people's open data; we point to the origin). Three deliverables:

- a **catalog** (descriptors + identity cards + index) — lightweight and tracked in git;
- a **website** — navigation, identity cards, dataviz;
- a native **acquisition core** — Rust crates + C ABI + bindings that retrieve verified dataset bytes
  without requiring Python;
- an optional Python **package/binding** — `import …` / `….get("name")` to retrieve a dataset (or its
  metadata) locally, plus bridges into the rest of the ecosystem.

The **bytes live at their source**; git only carries metadata + cards + index. Everything is **hashed
and versioned**. An **add/qualification pipeline** grows and evolves the bank.

Ultimate goal: make it possible to **cite, benchmark, compare, and explore** on a serious,
reproducible base, with datasets ranging from **X only** to **X + Y** to **X + Y + metadata**.

---

## 2. A dataset = measured reality (raw, first-class)

A **dataset** is **not** a benchmark task (a Y+split choice). It is raw data, kept **as raw as
possible**. It contains:

| Element | Rule |
|---|---|
| **X** — 1..n **sources** | One source = one instrument / acquisition, **kept separate** (never merged or resampled), with its own native axis (nm / cm^-1 / um / ...). A dataset can be **multi-source** (several X blocks), and sources can have **different sizes** — see the note below. (`nirs4all-formats` / `nirs4all-io` added *as needed* to read vendor formats and run metrics.) |
| **Variables (Y + metadata)** | **No intrinsic difference.** If the source declares targets, mark them. Otherwise **any column is a potential Y**. Multi-target, mixed types, **never split apart**. If no Y is declared, do not invent one; document metadata and metrics. |
| **Sample ID** | `observation_id`, etc. — index, never a Y. |
| **Metadata** | **All preserved**, with no prior filtering or processing for now. |
| **Splits / folds** | **None by default.** Kept *only if the source defines them* (train/test, folds, even several versions), and then **documented**. |

Coverage: **X only** · X + Y · X + Y + metadata. The Python package can return data **with or without a
split** (concatenated by default).

**Multi-sources & repetitions (structural).** Like Y, **X can be multiple** (multi-source dataset:
several instruments / acquisitions). Each source is managed **independently**: no fusion, no
resampling, no imposed common grid. Most importantly, because of **asymmetric spectral repetitions**
(a sample scanned a variable number of times depending on the source), **sources can have different
numbers of spectra**; they are **not row-aligned**. Implications:

- each source carries its own `(n_spectra x n_wavelengths)` dimension and its own repetition indexing;
- **alignment** between sources, and with Y / metadata, is done **by sample identity (ID), never by row
  position**;
- the pipeline, card (stats **per source**), and Python package **preserve** this structure (never flatten or
  force alignment); the package returns sources separately and can, on request, concatenate repetitions
  or return only one source.

---

## 3. Governance & visibility — 3 tiers

We **catalog everything**. What varies is what we **show** and what we **export**. The **right token**
(in the consumer binding/package) unlocks full access.

| Tier | Website — metadata & metrics | Byte export (consumer binding/package) |
|---|---|---|
| **public** | everything, named | **yes, for everyone** (from the origin) |
| **private** | everything, named | **token required** (private Dataverse) |
| **anonymized** | **unnamed** metadata + **normalized Y** (metrics on anonymized data) | **token required** |

- Datasets whose **source cannot be automated** go into a **private Dataverse**, retrievable with a
  token (no open publication from us).
- Anonymization (the most protected tier) masks variable names and normalizes Y: metrics are published
  **without revealing** real values/identities.

---

## 4. Architecture

```text
  origin sources (DOI / URL / private Dataverse)
                    |  (tested regularly; if an origin goes down -> switch to private Dataverse)
                    v
  +-------------------------------------------------------------+
  |  add / qualification PIPELINE (re-runnable script)           |
  |  raw ingest (nirs4all-formats/io)  ->  metrics  ->  card     |
  +-------------------------------------------------------------+
                    | writes / updates
                    v
        git: descriptors + identity cards + index        (bytes never in git)
                    |
        +-----------+---------------------------+
        v                                       v
   website (cards + dataviz, by tier)      optional Python package  ....get("name")
                                           (local download; token = full access; with/without split)
```

- **Catalog (git)** — one descriptor + one card per dataset, plus the index. Lightweight source of truth.
- **Add/qualification pipeline** (a script) — (1) records a new raw dataset, (2) computes metrics ->
  identity card, (3) **updates the website + acquisition/catalog files**. **Re-runnable**: when the metric protocol
  evolves, run it again to **update old cards** without touching the data.
- **Website** — navigable catalog, cards, **dataviz on X, Y, and metadata**, respecting tiers.
- **Acquisition core + bindings** (this repo) — the Rust core resolves/fetches/verifies bytes; the
  optional Python package adds `get()/NirsDataset`, metadata/card access, and the bridges to
  `nirs4all` / `nirs4all-io`.

---

## 5. Provenance, integrity, versions, evolution

- **Provenance** — origin source(s) (DOI/URL + mode: open / token / manual / script); related
  **publications** (papers) referenced but kept distinct from **data** sources.
- **Integrity** — hash chain **origin -> raw -> canonical -> card**.
- **Versions (2 proposed axes)** — (a) dataset **content version**: bump when bytes change; (b)
  **metric protocol version**: bump when metrics are enriched -> re-qualification without content
  changes. *(to validate)*
- **Origin resilience** — origins **tested regularly**; if an origin goes down, the dataset switches to
  the **private Dataverse**.
- **Evolution** — datasets come from a **OneDrive**; pulls will evolve, `chantiers/` + `unusable/` will
  **migrate** into the existing structure later, and **version iterations** are expected. Therefore the
  pipeline (§4) must provide a robust **add mechanism** + hashes/versions designed for that evolution.

---

## 6. Identity card (diagnostics)

Per dataset, **as complete as possible**, and **extensible** (a final protocol + metric list will
arrive; we must be able to add them and **re-qualify existing datasets**):

- spectral + PCA / dimensionality + **quality by X block**;
- **stats by Y variable** (distribution / class balance) — multi-target;
- **dataviz on X, Y, and metadata**;
- train<->test shift *if* a split exists;
- hashes + citation + provenance.

---

## 7. Migration from the current state (`NIRS DB/`, 19 GB)

| Source | Decision |
|---|---|
| **`v2.0/` (164)** — machine-readable `dataset_card.json` cards | **canonical**: the bank becomes these datasets. |
| **`regression/ classification/ multimachines/` (484 v1 sheets)** | **deleted** (they were tasks, not datasets). |
| **`Publications/`** | keep + organize **those referenced** by a dataset; ignore the rest. |
| **`chantiers/`, `unusableDB/`** | ignored **for now** — they will migrate into the existing structure later (anticipate this). |

Code consequences: remove the v1 path (`discover.find_leaves` / `build_descriptor`) because it becomes
dead; the card becomes **multi-Y**; add the 3 tiers + `get()` package/binding + add pipeline + origin
health-check. Guardrail: **list** any v1 datasets with no v2.0 equivalent before deletion (no silent
loss).

---

## 8. Still-open points (next iteration)

1. **Consumer API** — should `get()` default to concatenated (no split) or partitioned data? How should
   multiple splits be handled? What should metadata / card accessors be named? Maintainer note: if
   splits are available, users must be able to download split data, so these should be options; choose
   natural names for metadata and metric functions.
2. **Anonymization** — define "normalized Y" (z-score? min-max? rank?) and "unnamed metadata" (drop
   names -> `col_0...`?). Maintainer note: choose what feels natural in ML or spectroscopy.
3. **Token** — one token for all private data, or per dataset? Reuse the Dataverse token. Maintainer
   note: start from the existing Dataverse behavior once Dataverse is up; use a Dataverse token.
4. **Versions** — validate the 2 axes content / metric protocol (§5). Maintainer note: the protocol and
   metric/metadata schema will evolve, including repetitions, aggregations, etc.; start with these axes.
5. **Default Y designation** — when no Y is declared, what rule chooses the metadata column (and how is
   it documented)? Maintainer note: no rule; do not set Y. Show metadata and provide metadata dataviz
   like Y dataviz (histograms, etc.).
