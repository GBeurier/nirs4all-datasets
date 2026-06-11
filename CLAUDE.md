# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

`nirs4all-datasets` is the **dataset catalog** of the nirs4all ecosystem: a Python package + a
git-tracked descriptor catalog that **stores, qualifies, and serves curated NIRS reference
datasets**. Data bytes live on **Dataverse** (Recherche Data Gouv / CIRAD — DOI-citable, FAIR);
only the descriptors and generated metadata live in git. Access is **pooch-style**: `load("name")`
downloads a dataset on demand by its pinned DOI, checksum-verifies it, and caches it.

Status: **alpha** (version `0.1.0.dev0`). CLI entry point: `n4a-datasets`.

### The boundary rule (load-bearing)

This package **never re-implements NIRS or IO logic**. It reuses `nirs4all` for reading/qualifying
datasets (`DatasetConfigs`, `get_dataset_metadata`, `detect_signal_type`, outlier filters,
`core.metrics`) and `nirs4all-io` for instrument-file reads (`open_recordset` → `to_spectrodataset`).
If a NIRS/data/ML capability seems missing, it almost certainly exists in `nirs4all` — find it there
rather than building it here. This package owns only: descriptors, the canonical Parquet writer,
manifests/incrementality, card/datasheet/Croissant rendering, the catalog index, Dataverse
publish/fetch, and config/secrets.

## Commands

```bash
# Dev install (uses editable local nirs4all + nirs4all-io via [tool.uv.sources])
uv venv && uv pip install -e ".[dev,docs]"

# Green gate (mirror of CI, run before reporting work complete)
ruff check .
mypy --config-file pyproject.toml src
python catalog/scripts/validate.py                 # schema validity of all descriptors
python catalog/scripts/validate.py --check-publish  # also require public/embargo datasets publishable
python -m nirs4all_datasets.cli catalog --root .   # regenerate the index...
git diff --exit-code catalog/datasets.yaml         # ...CI fails if it is not committed
pytest -q

# Single test / file
pytest tests/test_ingest.py
pytest tests/test_schema.py::<test_name>
```

Tests use **no network** — the Dataverse client/access layer are tested with an injected fake
`requests.Session` / mocked fetch. The `network` pytest marker exists for live-instance tests
(`pytest -m "not network"` to deselect). Some canonical round-trip tests need the nirs4all
ParquetLoader fix (`nirs4all >= 0.9.2`) and **skip** on older versions.

### CLI surface (`n4a-datasets <cmd>`)

A thin typer layer (`cli.py`) over the stage modules. The lifecycle below shows how they chain; these
are the commands it does not name inline:

```bash
# Author / build the catalog
n4a-datasets bootstrap <source_tree> [--xlsx DatabaseDetail.xlsx]   # discover.py: write a descriptor per leaf
n4a-datasets add <raw_source> <id>                                  # one raw source -> canonical + card + index
n4a-datasets build-all --source-tree <tree> [--only a,b] [--force]  # bulk.py: parallel organize+qualify, then site
n4a-datasets qualify <id>                                           # (re)build one card.json from canonical data
n4a-datasets catalog                                                # regenerate catalog/datasets.yaml
n4a-datasets site [--out site]                                      # site.py: interactive static catalog
n4a-datasets list   /   n4a-datasets card <id>                      # inspect the local catalog

# Publish + governance (needs a Dataverse token; see Token hygiene)
n4a-datasets publish <id> --collection <alias> --contact-email <addr>  # first publish mints a DOI; later = version update
n4a-datasets restrict <id> [--off]                                  # (un)restrict all files, then publish a minor version
n4a-datasets grant|revoke <id> --to @user|&group [--role fileDownloader]

# Access
n4a-datasets load <id> [--token ...]                                # local-first, else fetch by DOI; print a summary
```

## The dataset lifecycle (core data flow)

Adding/maintaining a dataset is a pipeline driven by the `n4a-datasets` CLI (`src/.../cli.py`, a thin
typer layer that lazy-imports heavy deps). Each module owns one stage:

```
catalog/datasets/<id>.yaml        1. DESCRIBE   hand-authored DatasetDescriptor (schema.py)
        │  n4a-datasets add <raw_source> <id>
        ▼
organize.py  ──► ingest.py        2. INGEST     raw → datasets/<id>/canonical/*.parquet
        │                                        + nirs4all_config.json  (idempotent)
        ▼
manifest.py                       3. MANIFEST   content-addressed manifest.json (drives incrementality)
        │
        ▼
qualify/profile.py                4. QUALIFY    card.json + card.md + croissant.json + assets/*.png
        │
        ▼
catalog.py                        5. INDEX      regenerate catalog/datasets.yaml
        │  n4a-datasets publish <id> --collection ... (governance-gated, optional)
        ▼
publish.py + dataverse.py         6. PUBLISH    create dataset, upload, mint DOI on Dataverse
        ▲
access.py  ◄── load("<id>")       USE          fetch by DOI (pooch) / token (private), verify, cache, load
```

**One dataset vs. the whole fleet.** The diagram is the per-dataset path (`add`). The catalog itself is
populated in bulk: `discover.py` (`bootstrap`) walks a `<task>/<family>/<leaf>` source tree and writes
one schema-valid descriptor per leaf — reusing nirs4all's `FolderParser` for file→role mapping and
authoring everything else here (axis-unit/SPDX inference, honest governance defaults). `bulk.py`
(`build-all`) then runs organize + qualify across a process pool with **per-dataset failure isolation**
(each result is `ok`/`partial`/`failed`/`skipped` in a deterministic `bulk_report.json`; one failure
never aborts the run). `site.py` (`site`) renders the static catalog by pure formatting of
already-generated artifacts — no nirs4all import, no recomputation.

The `qualify/` package splits the card build (step 4): `profile.py` orchestrates and owns the card
schema, `metrics.py` computes the descriptive stats nirs4all does not expose, `plots.py` renders the
PNG assets (Agg backend), and `croissant.py` / `datasheet.py` emit the MLCommons Croissant JSON-LD and
the Datasheets-for-Datasets `card.md`.

### What lives where (3-tier storage)

- **git-tracked** (small): `catalog/datasets/<id>.yaml` (descriptor), `catalog/datasets.yaml` (index),
  and per-dataset `card.json`, `card.md`, `croissant.json`, `manifest.json`.
- **gitignored, lives on Dataverse** (heavy bytes): `datasets/<id>/raw/` and `datasets/<id>/canonical/`.
- **local cache** (downloaded on demand): `pooch.os_cache("nirs4all-datasets")/<id>/canonical/`.

### Key invariants to preserve when editing

- **Canonical = Parquet, `tabIngest=false`.** Parquet is chosen because Dataverse does *not*
  auto-ingest it, so the uploaded bytes stay byte-identical to the local ones. This is what makes the
  download SHA-256 verification in `access.py` work. Never upload with `tab_ingest=True`.
- **Incrementality is content-addressed.** `manifest.needs_rebuild` compares *inputs* (raw file
  hashes + `descriptor_hash` + converter name/version/config) against the previous manifest;
  unchanged inputs are skipped. `descriptor_hash` deliberately **excludes** `dataverse.doi` /
  `dataset_version` so publishing does not trigger a spurious rebuild.
- **Hand-authored vs. machine-generated descriptors.** `bootstrap` / `build-all` only ever touch
  descriptors flagged `generation.managed: true`; a human-edited descriptor is never overwritten
  (`--force` re-overwrites, still only managed ones). `generation.source_relpath` is how `build-all`
  finds the raw leaf again, and the whole `generation` block is **excluded from `descriptor_hash`** so
  refreshing it never forces a canonical rebuild.
- **Staleness, not lies.** `catalog.py` only enriches an index entry from a card/manifest whose
  `descriptor_hash` matches the current descriptor; otherwise it flags `is_stale` and omits the
  computed fields. Card sections (`profile.py`) use stable keys: a failed optional computation
  becomes `None` + a `warnings[]` entry, never a dropped key. All card floats are finite-sanitized
  (no NaN/Inf in JSON).
- **Two-level validation in `schema.py`.** *Schema validity* (every field well-formed) is separate
  from *publishability*. `DatasetDescriptor.publication_blockers()` is the governance gate:
  `confidentiality_class: confidential` is a hard stop (must never reach Dataverse); `visibility:
  public` requires `confidentiality_class: public` + an open SPDX license (`_OPEN_LICENSES`); live
  embargoes block; and the responsible-release governance fields must be non-blank. Internal/restricted
  descriptors are *valid* in the catalog — they just are not publishable.
- **Enum mirror.** `schema.py` enums (`TaskType`, `AxisUnit`, `SignalType`, …) mirror nirs4all's
  vocabulary by *value* (kept import-light on purpose); `tests/test_schema.py` guards against drift
  against the real nirs4all enums. Keep them in sync.
- **Token hygiene.** The Dataverse API token (`config.py`, wrapped in `SecretStr`) travels only in the
  `X-Dataverse-key` header, never as a query param, never logged. Private downloads (`access.py`) do
  **not** follow redirects with the key attached (signed S3 storage must not receive it). Resolution
  order: explicit arg → `NIRS4ALL_DATAVERSE_TOKEN` env → `~/.config/nirs4all-datasets/config.toml`
  (chmod 600 enforced) → project `.env`. A token is only needed to publish or to fetch private data.

### Ingest specifics (`ingest.py`)

- **Two input routes, one canonical output:** a *directory* of tabular files (nirs4all
  `Xcal/Ycal/Xtrain/...` convention) → `DatasetConfigs`; a *single instrument file* (OPUS/JCAMP/SPC/
  ASD/…) → `nirs4all_io.open_recordset(...).to_spectrodataset(...)`.
- Supports single- and multi-source (one X file per source; `train_x` becomes a list), regression and
  classification (classification Y is stored as nirs4all-encoded integer class indices — the human
  class *names* live in the descriptor's `Target.classes`), train-only and train+test splits, and
  targetless (X-only) datasets. The on-disk `nirs4all_config.json` uses **relative** paths;
  `resolve_config()` turns them absolute for `DatasetConfigs`.

## Conventions

- `id`: stable lowercase slug `^[a-z0-9]+(_[a-z0-9]+)*$`, permanent (it is the Dataverse/URL identity).
- `version`: semver; bump on any byte change.
- Python 3.11+, Google docstrings, ruff line length **220**, type hints on public APIs, `py.typed`.
- Full contributor walkthrough is in `CONTRIBUTING.md`; token setup in `README.md`. Prefer the
  Dataverse **sandbox** (`demo.recherche.data.gouv.fr`) before the production instance.
