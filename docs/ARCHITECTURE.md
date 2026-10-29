# Architecture

The detailed reference. For the high‑level picture read
[`ONBOARDING.md`](https://github.com/GBeurier/nirs4all-datasets/blob/main/ONBOARDING.md); for the
rationale, see {doc}`DESIGN`.

## 1. The lifecycle pipeline

A dataset flows through eight stages; each module owns one. The CLI (`n4a-datasets`) is a thin Typer
layer that lazy‑imports the heavy deps.

```
NIRS DB/v2.0/<leaf>/dataset_card.json + X*/Y/M.csv
        │  bootstrap.py            DESCRIBE   card.json -> catalog/datasets/<id>.yaml (schema-2.0 descriptor)
        ▼
organize.py ─► canonical.py        CANONICAL  id-keyed CSV -> datasets/<id>/canonical/ (per-source Parquet,
        │                                     joined by sample_id), + dataset.json
        ▼
manifest.py                        MANIFEST   content-addressed manifest.json (drives incrementality)
        │
        ▼
qualify/profile.py                 QUALIFY    card.json + card.md + croissant.json + assets/*.png
        │  (registry.py metrics, plots.py, anonymize.py, croissant.py, datasheet.py)
        ▼
catalog.py                         INDEX      catalog/datasets.yaml + a whole-bank `summary`
        │
        ▼
health.py                          HEALTH     probe origins -> catalog/health.json (degrade dead public)
        │
        ▼
status.py                          STATUS     docs/DATASET_STATUS.md + docs/PRIVATE_DATASETS.md
        │                                     + catalog/validation.yaml (human review)
        ├─► site/                  SITE        the static catalog site (pure-render)
        ▼
access.py ◄── get("<id>")          USE         local-first, else fetch by DOI/origin, verify, cache -> NirsDataset
        ▲
publish.py + dataverse.py          PUBLISH     (future) personal-Dataverse governance for protected data
```

**Bulk vs one dataset.** `bulk.py` runs organize+qualify across a process pool (spawn, with a serial
fallback if a worker dies) with per‑dataset failure isolation; `discover`‑style bulk authoring is
`bootstrap.py` over the whole `v2.0/` tree (idempotent, managed‑orphan prune, `catalog/reconciliation.json`).

## 2. Module map

| Module | Role |
|---|---|
| `schema.py` | The contract: `DatasetDescriptor` + `Manifest` pydantic models, enums, validators, `publication_blockers()`. |
| `bootstrap.py` | v2.0 `dataset_card.json` → schema‑2.0 descriptor (modality/axis/variable‑type inference, honest governance, origin/publication routing). |
| `canonical.py` | id‑keyed CSV → per‑source Parquet + per‑sample `variables.parquet` + `splits/` + `dataset.json`; sample‑identity join; comma‑decimal coercion. |
| `manifest.py` | `processing_hash` (byte‑determining) + `metadata_hash` (displayed) + `needs_rebuild` incrementality. |
| `organize.py` | Place raw → call `build_canonical` → write the manifest, incrementally. |
| `qualify/profile.py` | Build `card.json` from the canonical Parquet (per‑source + per‑variable stats); orchestrate `qualify()` (card.json + card.md + croissant.json + assets). |
| `qualify/registry.py` | Extensible, protocol‑versioned metric registry (scopes: source/variable/dataset). |
| `qualify/metrics.py` `plots.py` | Pure numerics; per‑source + per‑variable plots (Agg). |
| `qualify/anonymize.py` | The anonymized‑tier transform + the `public_card` / `public_descriptor` chokepoints. |
| `qualify/croissant.py` `datasheet.py` | MLCommons Croissant JSON‑LD + Datasheets‑for‑Datasets `card.md`. |
| `dataset.py` | `NirsDataset` — the consumer reader (`x`/`y`/`metadata`/`split`/`to_nirs4all`), tier‑masking on read. |
| `access.py` | `get()` — local‑first, else fetch by Dataverse DOI (token) / open origin; SHA‑256 verify; cache. |
| `catalog.py` | The index entry + the whole‑bank `bank_summary`; staleness, not lies. |
| `health.py` | Origin liveness probe (injectable session) → `catalog/health.json`. |
| `status.py` | Per‑dataset status (state/origin/validation/distribution) + the reports + the validation registry. |
| `site/` | The static‑site generator (pure‑render: pyyaml + stdlib; tier‑gating in `model.py`). |
| `bulk.py` | Parallel organize+qualify with failure isolation. |
| `cli.py` | The `n4a-datasets` Typer CLI. |
| `config.py` `dataverse.py` `publish.py` | Token hygiene; the Dataverse REST client; the publish/governance flow. |

## 3. Schema 2.0 (the descriptor)

`catalog/datasets/<id>.yaml` → `DatasetDescriptor`:

- `sources: list[Source]` (≥1) — `source_id`, instrument, modality, axis unit/range, n_observations, n_variables.
- `variables: list[Variable]` (may be empty) — `name`, `role` (target|metadata), `type`
  (numeric|categorical|text|identifier|datetime), unit, classes. `.targets` / `.metadata_variables`
  are properties. **No `task_type`** — the task is a consumer concern.
- `ids: IdentitySpec` — `observation_id` (per spectrum), `sample_id` (physical sample), `sample_id_available`.
- `alignment_level` — `observation` | `sample`. `splits: list[SplitRef]` (`applied=False`).
- `tier` — public | private | anonymized. `versions: Versions` — `content` + `schema_protocol`.
- `governance` (license + open‑data fields; **no** visibility/confidentiality), `provenance`,
  `origin_sources: list[OriginSource]` (where the bytes live — never checksums), `publications`,
  `datacite`, `dataverse`, `reproducibility`, `generation` (managed‑descriptor provenance).

**Two‑level validation** (`schema.py` + `catalog/scripts/validate.py`): *schema validity* (every field
well‑formed) is separate from *publishability* (`publication_blockers()`, which gates only the `public`
tier: open license + open non‑SCRIPT origins + the responsible‑release fields).

## 4. Canonical on‑disk layout

```
datasets/<id>/canonical/
  dataset.json                 {format_version, id, join_key:"sample_id", alignment_level,
                                sources:[{source_id,path,n_observations,n_variables,axis_*}], variables, splits}
  sources/<source_id>.parquet  observation_id (str), sample_id (str), <wavelength cols> (float32)
  variables.parquet            sample_id (str), <all non-spectral Y/M cols> (native dtype)   [optional]
  splits/<name>.parquet        sample_id (str), partition (str)                              [optional]
```

Sources may have **different row counts** (asymmetric repetitions). Everything is joined by `sample_id`,
never by row position. `variables.parquet` is per‑sample (one row per `sample_id`); the standardization
script's `source_*` provenance‑plumbing columns are excluded. Parquet is chosen because Dataverse does
**not** auto‑ingest it, so uploaded bytes stay byte‑identical to local ones (the SHA‑256 verify depends on it).

## 5. Tiers and anonymization (load‑bearing)

`public` shows everything and is openly fetchable; `private` shows metadata + metrics but export needs a
token; `anonymized` masks variable names (`var_NNN`), z‑scores numeric targets, and removes identifying
free text. The anonymized tier is enforced **automatically by tier** through one chokepoint —
`qualify.anonymize.public_card` / `public_descriptor`:

- `qualify()` writes `card.json` itself already‑anonymized for the anonymized tier (and renders
  `card.md`/`croissant.json` from the masked view);
- the catalog entry, `NirsDataset.descriptor`/`variables()`/`card()`, the site, and Dataverse publish
  metadata all derive their displayed fields from the public card/descriptor.

So no tracked artifact, index entry, public API, or published metadata can leak an anonymized identity.
(Reviewed by Codex: GO. Regression test: `tests/test_anon_enforcement.py`.)

## 6. Incrementality + the two axes

- **`processing_hash`** covers only byte‑determining descriptor fields (sources, ids, alignment, splits,
  `versions.content`); editing a name/tier/variable‑role/origin or bumping `versions.schema_protocol`
  never rebuilds canonical bytes.
- **`metadata_hash`** covers the displayed content and drives card re‑render (`card_metadata_fresh`).
- `needs_rebuild` compares raw‑file hashes + the converter identity + `processing_hash` against the
  previous manifest. A **content** version bumps on a byte change; a **metric‑protocol** version bumps to
  re‑qualify cards (`build-all --protocol-refresh`) without rebuilding data.

## 7. Status + validation

`status.py` derives, per dataset: **state** (described→canonical→**qualified**=metrics computed),
**materialized** (canonical + SHA‑256), **origin** (reachability from the health probe), **distribution**
(open / on_dataverse / upload_pending). **Validation** is the human axis, recorded in
`catalog/validation.yaml` (`pending`→`reviewed`→`approved`), which `bootstrap` never touches. `n4a-datasets
status` refreshes the registry and writes `docs/DATASET_STATUS.md` + `docs/PRIVATE_DATASETS.md`.

## 8. Access model (and the PyPI caveat)

`get(name, *, root=".", source, split, token, …)` resolves **local‑first** (`<root>/datasets/<id>/
canonical` + `<root>/catalog/datasets/<id>.yaml`), else fetches by the descriptor's Dataverse DOI (token
for private/anonymized) or an open origin, verifies SHA‑256, and caches. The token travels only in the
`X-Dataverse-key` header and is never sent on an S3 redirect.

> **PyPI note.** The wheel ships the code **and** the bundled cross-language
> `catalog/index.json`. A pip‑installed Python consumer still points
> `get(root=<checkout>)` at a clone of this repo for the high-level
> `get()/list()/card()` surface, because that layer reads descriptors/cards and
> returns `NirsDataset`. Non-Python bindings consume `catalog/index.json`
> directly: `n4ds_resolve` returns the byte contract plus the tier-sanitized
> descriptor, so R/WASM/Rust can inspect sources/variables and read verified
> Parquet without the Python provider package. See [`RELEASING.md`](RELEASING.md).

## 9. Conventions

Python 3.11+, Google docstrings, ruff (line length 220) + mypy, type hints on public APIs, `py.typed`.
nirs4all is an **optional** extra (`[nirs4all]`) — imported lazily, degrading gracefully when absent. Each
green gate: `ruff check .` + `mypy --config-file pyproject.toml src` + `validate.py` (+ `--check-publish`)
+ `pytest`. The enum mirror (`AxisUnit`/`SignalType`/`Modality` mirror nirs4all by value) is guarded by
`tests/test_schema.py`.


## Optional external assessments and curation protocol

Qualification protocol 6 preserves missing evidence as null. Diagnostic scores are
heuristic signatures with `confidence_status: unvalidated`; they are not
probabilities of physical causes. RMS/SAM in the legacy profile describe distance
to the dataset mean, rather than an independent reference. Partial evidence is
reported with coverage and cannot establish a reassuring "normal" score.

`qualify.assessments` stores optional version-1 `assessments.json` sidecars next to
`card.json`. Each assessment binds dataset/content/source/population/context and
producer engine/protocol versions. Intrinsic and task/split-scoped reports remain
separate. `write_assessments` validates identity against the canonical bytes;
`NirsDataset.assessments()` reads them with anonymized-tier redaction. The raw
producer `report` is retained losslessly when provided. Unavailable metrics have a
null value and explicit reason. Unknown additive metrics remain in the report.

`build_card(..., assessment_mode="shared")` consumes one explicitly selected
intrinsic report per source without calling the legacy PCA/QC kernels. Missing
metrics remain unavailable; there is no silent fallback or required unpublished
package. Task reports are attached separately and never populate intrinsic QC.
The default `legacy` mode preserves historical consumer contracts and labels its
heuristic results explicitly. Protocol changes do not overwrite old cards.

Canonical curation adds `observations.parquet` for acquisition-varying variables,
`provenance.parquet` for original metadata, and a `curation.json` raw-token/rule
journal. These local bytes are never placed in the public site. Variables varying
within one sample are omitted from the per-sample table and retained by acquisition;
`NirsDataset.observation_variables()` exposes that grain. Source-specific identity
rules distinguish subject/aspect, vial/acquisition, product and unknown specimen
identity. Exact duplicate spectral vectors are counted without removing rows or
claiming a technical reacquisition. Unknown physical sample counts remain null.

`Variable` optionally declares an original name, semantic role, equivalence or
explicit derivation, column-specific missing tokens/sentinels and numeric dialect.
Defaults preserve valid categorical `NA`, `ND` and `none` tokens. Censored numeric
values retain operator, bound, unit and original token in the journal. The
processing hash includes byte-affecting normalization directives while descriptive
roles remain metadata. `NirsDataset.consumer_views(targets=[...])` returns explicit
Y/M/structure/passport views with exclusion reasons; all original values remain
accessible. Scientific API/reference targets are preserved by declared role, and
copies/declared derivatives of the selected target are excluded from M.

For LUCAS, `organize(..., source_context={"soilsite": "/path/to/ossl_soilsite_L0_v1.2.csv.gz"})`
joins documented OSSL dataset/layer keys, exports site and campaign intervals,
coordinates and geographic uncertainty, and records the source SHA-256. It does
not reconstruct site identity from coordinates or treat campaign periods as exact
individual collection dates. Changes to this side input invalidate incrementality.
A missing soilsite input remains an explicit design-availability warning.
