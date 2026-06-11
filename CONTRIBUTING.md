# Adding a dataset

A dataset in this catalog is three things:

1. a hand-checkable **descriptor** — `catalog/datasets/<id>.yaml` (identity, sources, variables, splits,
   provenance, governance, the origin where the bytes live);
2. a generated **canonical form** — `datasets/<id>/canonical/` (per-source Parquet, sample-identity
   joined, nirs4all-loadable) built from the raw bytes;
3. a generated **identity card** — `datasets/<id>/card.json` + `card.md` (datasheet) + `croissant.json`
   + `assets/*.png`.

The heavy bytes (raw + canonical) **never enter git** and are **never re-hosted**: they stay at their
origin (Zenodo / a data Dataverse / a vendor archive) and the catalog links to them. Git tracks only
the descriptor, the card/datasheet/Croissant, the manifest, and the catalog index. The whole flow is
driven by the `n4a-datasets` CLI and is **incremental** (re-running only reprocesses what changed).

## 0. One-time setup

```bash
uv venv && uv pip install -e ".[dev]"     # editable nirs4all + nirs4all-io
```

A Dataverse API token is **not** needed to add, qualify, or read public datasets — only to fetch
private/anonymized data or to publish to a personal Dataverse (a future capability; see
[`docs/PUBLISHING.md`](docs/PUBLISHING.md)). See the [README](README.md#api-token--where-to-put-it).

## 1. Write (or generate) the descriptor

Most descriptors are **auto-generated** from a standardized `NIRS DB/v2.0/<leaf>/` package by
`bootstrap` (see [Bulk authoring](#bulk-authoring-many-datasets-at-once)). To hand-author one, copy an
existing descriptor and edit it:

```bash
cp catalog/datasets/corn_eigenvector_nir.yaml catalog/datasets/<id>.yaml   # <id> must match the filename
```

`<id>` is a stable slug (`^[a-z0-9]+(_[a-z0-9]+)*$`), e.g. `wheat_protein_foss6500`. The authoritative
schema is `src/nirs4all_datasets/schema.py` (`DatasetDescriptor`). Key blocks (schema **2.0**):

| Block | Fields |
|---|---|
| identity | `schema_version` (`'2.0'`), `id`, `name`, `description`, `domain`, `keywords`, `citation` |
| `sources[]` (`1..n`) | `source_id` (`X` / `X1` / …, unique), `name`, `vendor`, `instrument_name`, `modality` (NIR/MIR/Raman/UV-Vis/VSWIR/TIR/hyperspectral/other), `axis_unit` (nm/cm-1/none/index/text), `axis_min`/`axis_max`/`axis_resolution`, `signal_type`, `n_observations`, `n_variables` |
| `variables[]` (`0..n`) | `name`, `role` (`target`/`metadata`), `type` (`numeric`/`categorical`/`text`/`identifier`/`datetime`), `unit`, `classes` (ordered class names for a categorical). May be empty — X-only is valid; never invent a target. |
| `ids` | `observation_id`, `sample_id`, `sample_id_available` |
| `alignment_level` | `observation` (one spectrum/sample, shared order) or `sample` (grouped by `sample_id`; sources may differ in size) |
| `splits[]` | native partitions, *documented not applied*: `name`, `kind` (`train_test`/`kfold`/`group`/`custom`), `path`, `n_folds`, `documented_origin`, `applied` (always `false`) |
| `tier` | `public` \| `private` \| `anonymized` (replaces the old visibility/confidentiality split) |
| `versions` | `content` (semver, bump on a byte change), `schema_protocol` (bump to re-qualify under a new metric protocol) |
| `provenance` | `contributor`, `collection_date`, `reference_method`, `lab_protocol`, `ingest_reader`, `raw_sha256`, `conversion_status`, `warnings`, `known_exclusions` |
| `governance` | `license` (SPDX), `owner_steward`, `redistribution_rights`, `consent_ethics_status`, `anonymization_status`, `permitted_use`, `access_policy` (**no** `visibility`/`confidentiality_class`/`embargo`) |
| `origin_sources[]` | where the **bytes** live: `kind` (dataverse/zenodo/figshare/url/script/manual), `mode` (raw/canonical), `locator` (pinned DOI / URL / `scripts/<id>.py`), `access` (open/token/manual), `license`, `expected_files`, `last_checked`/`alive` (health) |
| `publications[]` | related papers (journal DOIs) — distinct from `origin_sources` (data DOIs) |
| `datacite` / `dataverse` | rich citation metadata; `dataverse` is the (future) personal-Dataverse pointer (`instance`; `doi`/`dataset_version` filled at publish) |

**Governance is tier-gated.** A descriptor is always *valid* in the catalog regardless of tier;
`publication_blockers()` only checks the **`public`** tier, which requires an open SPDX license, open
origin sources (you cannot re-host non-open data as open), and non-blank responsible-release governance
fields. `private` / `anonymized` descriptors are valid — they are just token-gated, never published
openly.

Validate any time:

```bash
python catalog/scripts/validate.py                  # schema validity (every field well-formed)
python catalog/scripts/validate.py --check-publish  # also require public-tier datasets to be publishable
```

## 2. Build the canonical form + card

```bash
n4a-datasets add <raw_source> <id>
```

`<raw_source>` is a standardized **v2.0 leaf** directory of `;`-delimited CSVs (`X*.csv` / `Y.csv` /
`M.csv`, first column `observation_id`). `add` will:

- copy the raw bytes under `datasets/<id>/raw/` (preserved as-is),
- convert to `datasets/<id>/canonical/`: one `sources/<source_id>.parquet` per X block
  (`observation_id`, `sample_id`, float32 spectral cols), a per-sample `variables.parquet` (Y ∪ extra
  metadata, omitted when there is neither), any native `splits/<name>.parquet`, and a loadable
  `dataset.json` — everything joined by **`sample_id`, never by row position**,
- write `manifest.json` (`processing_hash` + `metadata_hash` + per-file SHA-256), then `card.json`,
  `card.md`, `croissant.json`, and the plot assets,
- refresh `catalog/datasets.yaml`.

Supported: single- and multi-source, regression and classification, native and no splits, and
targetless (X-only / metadata-only) datasets. Re-running `add` on unchanged inputs is a no-op
(content-addressed); change the raw data or a processing-relevant descriptor field and only that
dataset rebuilds. Re-build just the card (e.g. after a metadata-only descriptor edit) with
`n4a-datasets qualify <id>`; add `--anonymize` to also emit `card.anon.json` (masked names, z-scored
numeric targets) for the anonymized tier.

Inspect:

```bash
n4a-datasets list                       # the catalog index (filter with --tier / --domain / --spectro-family)
n4a-datasets card <id>                  # the identity card (JSON)
n4a-datasets get <id> [--source X1]     # load the canonical form (local if present) and print a summary
```

From Python: `n4ad.get("<id>")` returns a `NirsDataset` (`.x()`, `.y()`, `.metadata()`, `.split()`,
`.to_nirs4all()`).

## 3. Probe the origins

```bash
n4a-datasets health-check               # HEAD/GET each open origin -> catalog/health.json
```

A **public** dataset whose every open origin has died is flagged `degraded` (the catalog/site surface
it). Script / manual / token-gated origins are not probed. This is unit-tested with an injectable
session (no network in CI).

## 4. Commit (descriptor + metadata, not the heavy bytes)

```bash
git add catalog/datasets/<id>.yaml catalog/datasets.yaml \
        datasets/<id>/card.json datasets/<id>/card.md datasets/<id>/croissant.json datasets/<id>/manifest.json
git commit -m "data(<id>): add <name>"
git push
```

`datasets/<id>/raw/` and `datasets/<id>/canonical/` (the bytes) are **gitignored** — they live at the
origin. The card, datasheet, Croissant, manifest, and catalog are small and git-tracked.

## Bulk authoring (many datasets at once)

The catalog is normally built in bulk from a tree of standardized v2.0 packages (no Dataverse, no
network):

```bash
# 1. DESCRIBE: author one schema-2.0 descriptor per leaf under <tree>/v2.0/* from its dataset_card.json.
#    Descriptors are marked generation.managed=true (regenerable) with tier inferred honestly
#    (public only when an open license is detected AND public release is allowed; else private).
#    --prune re-bases: managed descriptors the source no longer produces are deleted; human-authored
#    ones are only flagged. Every run writes catalog/reconciliation.json.
n4a-datasets bootstrap <source_tree> --root . [--prune] [--force]

# 2. CANONICAL + QUALIFY: organize (raw -> canonical Parquet, incremental) + build every card, in
#    parallel, then refresh the index. Per-dataset failures are isolated and summarized in
#    bulk_report.json (gitignored); one bad dataset never aborts the run. --protocol-refresh re-qualifies
#    (rebuilds cards) without rebuilding canonical bytes; --site also builds the static site.
n4a-datasets build-all --source-tree <source_tree> --root . [--workers N] [--only id1,id2] [--force] \
                       [--protocol-refresh] [--skip-assets] [--site]

# 3. (re)build only the static site from the catalog + cards (also done by build-all --site).
n4a-datasets site --root . --out site/
open site/index.html      # or: python -m http.server --directory site
```

`bootstrap` re-runs are idempotent (a managed descriptor is rewritten only when `--force` or its
`metadata_hash` changed; a `generation.managed: false` descriptor is treated as human-owned and never
overwritten). `build-all` skips datasets whose source bytes + processing-relevant descriptor fields are
unchanged and whose canonical outputs are intact. The site is a self-contained `site/` (searchable index
with whole-bank dataviz + per-dataset card pages with plots, statistics, datasheet, provenance,
governance, and Croissant/JSON downloads) that opens from `file://` too.

## Green gate (run before every commit)

```bash
ruff check .
mypy --config-file pyproject.toml src
python catalog/scripts/validate.py                  # schema validity of all descriptors
python catalog/scripts/validate.py --check-publish  # public-tier datasets are publishable
python -m nirs4all_datasets.cli catalog --root .    # regenerate the index...
git diff --exit-code catalog/datasets.yaml          # ...CI fails if it is not committed
pytest -q                                           # no network (the network marker is opt-in)
```

## Conventions

- `id`: lowercase slug, stable forever (it is the catalog/URL identity).
- `versions.content`: semver; bump on any byte change (the manifest's content hash detects it).
- `license`: SPDX id; the **public** tier needs an open license (CC-BY-4.0, CC0-1.0, ODbL-1.0, …).
- Datasets are RAW: keep `1..n` sources separate (aligned by `sample_id`), keep every variable, never
  invent a target, document native splits without applying them.
- (Future) publishing of protected data uses a personal Dataverse — prefer the sandbox
  (`demo.recherche.data.gouv.fr`) before the production instance. See [`docs/PUBLISHING.md`](docs/PUBLISHING.md).
