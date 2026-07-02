# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

`nirs4all-datasets` is the **dataset catalog + acquisition stack** of the nirs4all ecosystem: a
git-tracked descriptor catalog, a Rust acquisition core, and optional consumer bindings/packages on top.
A dataset here is *raw measured reality, not a benchmark task* — `1..n` spectral sources, `0..n`
variables (every target *and* metadata column), the native splits if the origin defined them, and full
provenance back to the **origin** that published the data. The heavy bytes never enter git and are
**never re-hosted**: the catalog links to the origin (Zenodo / a data Dataverse / a vendor archive), and
the native acquisition core resolves, fetches, verifies, and caches canonical bytes. The optional Python
package wraps that core as `get()/retrieve()/NirsDataset`.

Status: **0.3.x, pre-1.0**. CLI entry point: `n4a-datasets`. Schema version: **2.0**.

### The boundary rule (load-bearing)

This repo **never re-implements NIRS or IO logic**. The optional `[nirs4all]` extra reuses `nirs4all`
for qualification (`XOutlierFilter`, `compute_pca_projection`, `SpectroDataset` in `to_nirs4all()`),
and the optional `[io]` extra reuses `nirs4all-io` / `nirs4all-formats` for raw-origin reproduction and
instrument-file reads. If a NIRS/data/ML capability seems missing, it almost certainly exists in
`nirs4all` or `nirs4all-io` — find it there rather than building it here. This repo owns only:
descriptors, the canonical Parquet writer, the Rust acquisition core + bindings, manifests/incrementality,
card/datasheet/Croissant rendering, the catalog index + whole-bank summary, origin health, the static
site, the (future) personal-Dataverse publish/fetch path, and config/secrets.

## Commands

```bash
# Dev install (builds the optional Python package + embedded native core; uses editable sibling bridges via [tool.uv.sources])
uv venv && uv pip install -e ".[dev]"

# Green gate (mirror of CI, run before reporting work complete)
ruff check .
mypy --config-file pyproject.toml src
python catalog/scripts/validate.py                  # schema validity of all descriptors
python catalog/scripts/validate.py --check-publish  # also require public-tier datasets publishable
python -m nirs4all_datasets.cli catalog --root .    # regenerate the index...
git diff --exit-code catalog/datasets.yaml          # ...CI fails if it is not committed
pytest -q

# Single test / file
pytest tests/test_canonical.py
pytest tests/test_schema.py::<test_name>
```

Tests use **no network** — the Dataverse client/access layer and the origin health probe are tested
with an injected fake `requests.Session` / `HttpSession`. The `network` pytest marker exists for
live-instance tests (`pytest -m "not network"` to deselect). Some canonical round-trip tests need a
recent nirs4all ParquetLoader fix and **skip** on older versions.

### CLI surface (`n4a-datasets <cmd>`)

A thin typer layer (`cli.py`) that lazy-imports heavy deps. It mirrors the lifecycle stages below;
`n4a-datasets <command> --help` documents every flag.

```bash
# Author / build the catalog
n4a-datasets bootstrap <source_tree> [--prune] [--force]            # bootstrap.py: a descriptor per v2.0/<leaf>
n4a-datasets add <raw_source> <id>                                  # one raw source -> canonical + card + index
n4a-datasets build-all --source-tree <tree> [--only a,b] [--force]  # bulk.py: parallel organize+qualify, then index
                       [--protocol-refresh] [--skip-assets] [--site]
n4a-datasets qualify <id> [--anonymize]                             # (re)build one card.json (+ card.anon.json)
n4a-datasets health-check [--only a,b]                              # health.py: probe open origins -> catalog/health.json
n4a-datasets catalog                                                # regenerate catalog/datasets.yaml
n4a-datasets site [--out site]                                      # site/: interactive static catalog
n4a-datasets list [--tier ...] [--domain ...] [--spectro-family ...]   # inspect the local catalog
n4a-datasets card <id>                                              # print one identity card (JSON)

# Access
n4a-datasets get <id> [--source X1] [--token ...] [--instance ...]  # local-first, else fetch; print a summary

# Publish + governance (FUTURE — personal Dataverse for protected data; see docs/PUBLISHING.md)
n4a-datasets publish <id> --collection <alias> --contact-email <addr>  # first publish mints a DOI; later = version update
n4a-datasets restrict <id> [--off]                                  # (un)restrict all files, then publish a minor version
n4a-datasets grant|revoke <id> --to @user|&group [--role fileDownloader]
```

## The dataset lifecycle (core data flow)

Adding/maintaining a dataset is a pipeline driven by the `n4a-datasets` CLI (`src/.../cli.py`, a thin
typer layer that lazy-imports heavy deps). Each module owns one stage:

```
NIRS DB/v2.0/<leaf>/dataset_card.json   1. DESCRIBE   bootstrap.py authors catalog/datasets/<id>.yaml
        │                                              (a schema-2.0 DatasetDescriptor; managed)
        ▼
organize.py  ──► canonical.py           2. CANONICAL  id-keyed CSV -> datasets/<id>/canonical/
        │                                              {sources/<sid>.parquet, variables.parquet,
        │                                               splits/<name>.parquet, dataset.json}
        ▼                                              joined by sample_id, never row position
manifest.py                             3. MANIFEST   content-addressed manifest.json
        │                                              (processing_hash + metadata_hash)
        ▼
qualify/profile.py                      4. QUALIFY    card.json + card.md + croissant.json + assets/*.png
        │
        ▼
catalog.py                              5. INDEX      catalog/datasets.yaml (per-dataset entries + a
        │                                              whole-bank `summary` / bank_summary)
        ▼
health.py                               6. HEALTH     probe open origins -> catalog/health.json
        │                                              (degrade a PUBLIC dataset whose open origins all died)
        ▼
access.py  ◄── get("<id>")              USE           local-first, else fetch by DOI/origin, verify SHA-256,
        │                                              cache, return a NirsDataset
        ▼
publish.py + dataverse.py               (future) PUBLISH   personal Dataverse for PROTECTED (private/
                                                            anonymized) data — NOT done now; public data
                                                            is only ever linked to its origin.
```

**One dataset vs. the whole fleet.** The diagram is the per-dataset path (`add`). The catalog itself
is populated in bulk: `bootstrap.py` (`bootstrap`) sweeps the `<tree>/v2.0/*` standardized packages
and authors one schema-valid descriptor per leaf from its machine-readable `dataset_card.json` (mapping
spectral blocks → `sources[]`, targets + metadata → `variables[]`, native split, license/governance,
origin sources vs. publications) — re-implementing no NIRS/IO logic. `bulk.py` (`build-all`) then runs
`organize` + `qualify` across a process pool with **per-dataset failure isolation** (each result is
`ok`/`partial`/`failed`/`skipped` in a deterministic `bulk_report.json`; one failure never aborts the
run) and refreshes the index (and, with `--site`, the static site). The `site/` package renders the
static catalog by pure formatting of already-generated artifacts — no nirs4all import, no
recomputation.

The `qualify/` package splits the card build (step 4): `profile.py` orchestrates and owns the card
schema, `metrics.py` computes the descriptive stats nirs4all does not expose, `registry.py` holds the
metric registry + `PROTOCOL_VERSION` (bumped to re-qualify under a new protocol), `plots.py` renders
the PNG assets (Agg backend), `croissant.py` / `datasheet.py` emit the MLCommons Croissant JSON-LD and
the Datasheets-for-Datasets `card.md`, and `anonymize.py` produces the anonymized-tier transform
(masked variable names + z-scored numeric targets) consumed by both `get()` and the site.

## What lives where (3-tier storage)

- **git-tracked** (small): `catalog/datasets/<id>.yaml` (descriptor), `catalog/datasets.yaml` (index +
  whole-bank `summary`), `catalog/health.json`, `catalog/reconciliation.json`, and per-dataset
  `card.json`, `card.md`, `croissant.json`, `manifest.json`.
- **the origin** (Zenodo / a data Dataverse / a vendor archive): the raw + canonical **bytes**, fetched
  on demand and **never re-hosted** by this project; a personal Dataverse is only a *future* fallback
  for protected data and rotted origins.
- **gitignored, local working bytes**: `datasets/<id>/raw/` and `datasets/<id>/canonical/`.
- **local cache** (downloaded on demand): the verified canonical Parquet under the native acquisition
  core's platform cache root.

## The dataset model (schema 2.0, `schema.py`)

A `DatasetDescriptor` carries: `sources[]` (`Source` — one X block/instrument, kept separate, with its
own axis unit/range), `variables[]` (`Variable` — `role` `target`|`metadata`, `type`
`numeric`|`categorical`|`text`|`identifier`|`datetime`; `.targets` is a property over `role==target`),
`ids` (`IdentitySpec` — `observation_id` / `sample_id` / `sample_id_available`), `alignment_level`
(`observation`|`sample`), `splits[]` (`SplitRef`, `applied` always False), `tier` (`Tier`
`public`|`private`|`anonymized`), `versions` (`content` + `schema_protocol`), `provenance`,
`governance` (`license` + open-data fields; **no** visibility/confidentiality/embargo), `origin_sources[]`
(where the bytes live), `publications[]`, `datacite`, `dataverse` (future personal-Dataverse pointer),
`reproducibility`, and `generation` (set on machine-authored descriptors).

Load-bearing model points (also in `README.md` / `docs/DESIGN.md`):

- **Sources kept separate.** Multi-instrument datasets keep each block as its own source; sources may
  carry *different* numbers of spectra (asymmetric repetitions) and are aligned by **sample identity**
  (`sample_id`), never by row position.
- **Every metadata column is a potential target.** No intrinsic Y/metadata distinction; a target is
  flagged only when the origin declares it. X-only / metadata-only datasets are valid; **no target is
  ever invented**.
- **Native splits documented, never applied.** `get()` returns the per-sample partition labels; it
  never silently partitions.
- **Three tiers.** `public` (shown + openly fetchable from the origin), `private` (shown; export needs a
  token), `anonymized` (variable names masked + numeric targets z-scored; export needs a token).
- **Two version axes.** `versions.content` (bumps on a byte change) and `versions.schema_protocol`
  (lets cards be re-qualified under a new metric protocol without rebuilding the data).

### Key invariants to preserve when editing

- **Canonical = Parquet, `tabIngest=false`.** Parquet is chosen because Dataverse does *not*
  auto-ingest it, so any uploaded bytes stay byte-identical to the local ones. This is what makes the
  download SHA-256 verification in `access.py` work. Never upload with `tab_ingest=True`.
- **Incrementality is content-addressed (two hash axes, `manifest.py`).** `needs_rebuild` compares
  *inputs* (raw file hashes + `processing_hash` + converter name/version/config) against the previous
  manifest; unchanged inputs are skipped. `processing_hash` includes only the byte-determining fields
  (the source structure, id keying, `alignment_level`, native splits, `versions.content`) and
  deliberately **excludes** every descriptive field (name/variables/tier/governance/origin sources/...)
  *and* `versions.schema_protocol` — so editing metadata or bumping the metric protocol never rebuilds
  canonical bytes. `metadata_hash` covers the human-authored, *displayed* content (variables, tier,
  governance, origins, citations) and drives card/site re-render (`card_metadata_fresh`) without a
  rebuild.
- **Hand-authored vs. machine-generated descriptors.** `bootstrap` / `build-all` only ever touch
  descriptors flagged `generation.managed: true`; a human-edited descriptor (`managed` false/absent) is
  never overwritten (`--force` re-overwrites, still only managed ones). `generation.source_relpath`
  (`v2.0/<leaf>`) is how reconciliation finds the leaf again, and the whole `generation` block is
  **excluded from both hashes** so refreshing it never forces a rebuild. `bootstrap --prune` deletes
  managed orphans (and their `datasets/<id>` dir) the source no longer produces; human orphans are only
  flagged. Every run writes a committed `catalog/reconciliation.json`.
- **Staleness, not lies.** `catalog.py` only enriches an index entry from a card/manifest whose
  `processing_hash` (and `metadata_hash`) match the current descriptor; otherwise it sets `is_stale` and
  omits the computed fields. Card sections (`profile.py`) use stable keys: a failed optional computation
  becomes `None` + a `warnings[]` entry, never a dropped key. All card floats are finite-sanitized (no
  NaN/Inf in JSON).
- **Two-level validation in `schema.py`.** *Schema validity* (every field well-formed) is separate from
  *publishability*. `DatasetDescriptor.publication_blockers()` is the governance gate and is **tier-gated**:
  only the `public` tier is checked, and it requires an open SPDX license (`_OPEN_LICENSES`), open origin
  sources (no re-hosting non-open data as open), and non-blank responsible-release governance fields.
  `private` and `anonymized` descriptors are *valid* catalog entries — they are simply token-gated, never
  published openly.
- **Enum mirror.** `AxisUnit` / `SignalType` / `Modality` mirror nirs4all's vocabulary by *value* (kept
  import-light on purpose); the rest of the enums (`Tier`, `VariableRole`, `VarType`, `AlignmentLevel`,
  `SourceKind`/`SourceMode`/`SourceAccess`, …) are this package's own domain. `tests/test_schema.py`
  guards the mirrored ones against drift; keep them in sync.
- **Token hygiene.** The Dataverse API token (`config.py`, wrapped in `SecretStr`) travels only in the
  `X-Dataverse-key` header, never as a query param, never logged. Private downloads (`access.py`) do
  **not** follow a redirect with the key attached (signed S3 storage must not receive it). Resolution
  order: explicit arg → `NIRS4ALL_DATAVERSE_TOKEN` env → `~/.config/nirs4all-datasets/config.toml`
  (chmod 600 enforced) → project `.env`. A token is only needed to publish or to fetch private/anonymized
  data.

### Canonical specifics (`canonical.py`)

- **Input is a standardized v2.0 leaf**, not a vendor file: a directory of `;`-delimited CSVs whose
  first column is `observation_id` — `X.csv` / `X1.csv` / `X2.csv` … (one per spectral block), optional
  `Y.csv` (targets), optional `M.csv` (`dataset_id`, `observation_id`, optionally `sample_id`,
  `split_original`, and arbitrary metadata). The upstream `source_to_standard.py` already converted the
  vendor bytes; this stage does not re-parse them.
- **Output keeps sources separate and joins by sample identity.** One Parquet per X block under
  `canonical/sources/<source_id>.parquet` (`observation_id`, `sample_id`, then float32 spectral cols);
  the per-sample `canonical/variables.parquet` (Y ∪ extra-M, one row per `sample_id`, omitted when there
  is no Y and no extra M); any native `canonical/splits/<name>.parquet` (`sample_id` → `partition`, never
  invented); and a loadable `canonical/dataset.json` with **relative** paths (`resolve_config()`
  absolutizes them). Robust to: no Y, multi-block, a missing `sample_id` column (identity fallback), and
  large files (spectral columns read float32 in chunks). `ConversionStatus` is `OK` / `PARTIAL` (warnings)
  / `FAILED` (no convertible X block).

## Conventions

- `id`: stable lowercase slug `^[a-z0-9]+(_[a-z0-9]+)*$`, permanent (it is the catalog/URL identity).
- `versions.content`: semver; bump on any byte change (the manifest's content hash detects it).
- Python 3.11+, Google docstrings, ruff line length **220**, type hints on public APIs, `py.typed`.
- Full contributor walkthrough is in `CONTRIBUTING.md`; the design is in `docs/DESIGN.md`; token setup
  is in `README.md`; (future) publishing of protected data is in `docs/PUBLISHING.md`.
