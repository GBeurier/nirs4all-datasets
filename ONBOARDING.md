# Onboarding — `nirs4all-datasets`

Start here. This page explains **what the project is**, the **principles** it is built on, and **how the
repo is organized**. For the deep dive, read [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md); to add or
maintain a dataset, read [`CONTRIBUTING.md`](CONTRIBUTING.md); the rationale is in
[`docs/DESIGN.md`](docs/DESIGN.md).

## What it is

A **citable, reproducible bank of raw NIRS reference datasets** — for benchmarking, exploring and
comparing models on a common, version‑pinned, provenance‑rich footing. Three deliverables:

1. a git‑tracked **catalog** — one hand‑checkable descriptor + a machine‑generated *identity card* per
   dataset; the heavy bytes never enter git;
2. a Python **plugin** — `get("name") → NirsDataset`, which fetches a dataset on demand from its origin,
   checksum‑verifies it, caches it, and hands you arrays;
3. a **static site** — a browsable, qualified catalog with whole‑bank dataviz.

It **reuses `nirs4all`** (optional) for card metrics + the nirs4all bridge and **never re‑implements
NIRS/IO logic** — that is the single load‑bearing rule (see *Boundary* below).

## Principles (the mental model)

- **A dataset is raw measured reality, not a benchmark task.** It carries `1..n` **X sources**
  (instruments), `0..n` **variables** (Y *and* metadata — the same kind of thing), native splits if any,
  provenance, and a visibility tier. The *task* (which Y, which split, which metric) is a **consumer
  choice**, never baked in.
- **Multi‑source X, aligned by identity.** Sources are kept separate and may even differ in size
  (asymmetric repetitions); they are joined by **`sample_id`**, never by row position.
- **Multi‑Y, nothing invented or dropped.** Every metadata column is a *potential* target; a dataset may
  declare no target at all (X‑only / metadata‑only is valid). No target is fabricated.
- **Splits are documented, never auto‑applied.**
- **Three tiers** decide what is shown and exported: `public` (open from the origin), `private` (shown;
  export needs a token), `anonymized` (variable names masked + Y normalized; export needs a token). The
  anonymized tier is enforced automatically everywhere a public path could leak.
- **Two version axes:** a **content** version (bytes change) and a **metric‑protocol** version
  (re‑qualify the cards without rebuilding the data).
- **Origins, not re‑hosting.** Bytes live at each dataset's origin (a data Dataverse / Zenodo / vendor
  archive); we link to them and verify checksums. Open data is never re‑hosted under a different license.
  A personal Dataverse is only a *future* fallback for protected data.

## Repo organization

```
nirs4all-datasets/
├── src/nirs4all_datasets/        the package (see docs/ARCHITECTURE.md for the module map)
│   ├── schema.py                 the descriptor / manifest models (the contract)
│   ├── bootstrap.py canonical.py the data spine (card.json → descriptor; CSV → canonical Parquet)
│   ├── qualify/                  the card builder (metrics, plots, anonymize, Croissant, datasheet)
│   ├── dataset.py access.py      the plugin: get() + NirsDataset
│   ├── catalog.py health.py status.py   the index, origin health-check, per-dataset status
│   ├── site/                     the static-site generator (pure-render)
│   └── cli.py publish.py …       the n4a-datasets CLI + Dataverse governance
├── catalog/                      GIT-TRACKED metadata (small)
│   ├── datasets/<id>.yaml        one descriptor per dataset (164)
│   ├── datasets.yaml             the assembled index + whole-bank summary
│   ├── health.json               origin liveness
│   └── validation.yaml           the human-validation registry (hand-edited)
├── datasets/<id>/                per-dataset artifacts
│   ├── card.json card.md croissant.json manifest.json   GIT-TRACKED (the identity card)
│   ├── assets/…png               GIT-TRACKED dataviz
│   └── canonical/ raw/           GITIGNORED bytes (live at the origin; cached locally on get())
├── docs/                         DESIGN, ARCHITECTURE, RELEASING, DATASET_STATUS, PRIVATE_DATASETS, …
└── NIRS DB/                      GITIGNORED local authoritative source tree (the v2.0 packages)
```

**Where data lives (3 tiers):** small metadata in **git**; heavy bytes at the dataset's **origin**;
downloaded canonical data in a **local cache** (`pooch`).

## Quickstart

```bash
uv venv && uv pip install -e ".[dev,nirs4all]"   # dev install (editable local nirs4all via [tool.uv.sources])
```
```python
import nirs4all_datasets as n4ad
n4ad.list()                              # the catalog index
n4ad.card("corn_eigenvector_nir")        # the identity card (dict)
ds = n4ad.get("corn_eigenvector_nir")    # -> NirsDataset (fetched, checksum-verified, cached)
ds.x(concat=False)                       # {source_id: array} — corn on three NIR instruments
ds.y(); ds.metadata(); ds.split("original"); ds.to_nirs4all()
```

CLI (`n4a-datasets --help`): `bootstrap` · `build-all` · `qualify` · `catalog` · `health-check` ·
`status` · `site` · `list` · `card` · `get` · `publish`/`grant`/`revoke`/`restrict`.

## The Boundary (read this)

This package **never re‑implements NIRS or IO logic.** It reuses `nirs4all` for qualification (PCA,
outliers, the `SpectroDataset` bridge). The catalog, the canonical writer, the card/metric pipeline,
the tiers, the index, origin health, and the site are *this* package's domain. If a NIRS/ML capability
seems missing, it almost certainly already exists in `nirs4all` — find it there.

## Where next

- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — the modules, the lifecycle pipeline, the schema, the
  canonical layout, the tiers/anonymization, the two hashes, conventions.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — add/maintain a dataset; the green gate.
- [`docs/RELEASING.md`](docs/RELEASING.md) — PyPI release + Dataverse publishing + the validation workflow.
- [`docs/DATASET_STATUS.md`](docs/DATASET_STATUS.md) / [`docs/PRIVATE_DATASETS.md`](docs/PRIVATE_DATASETS.md)
  — live status of every dataset + the private datasets awaiting upload.
