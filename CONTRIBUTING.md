# Adding a dataset

A dataset in this registry is three things:

1. a hand-authored **descriptor** — `catalog/datasets/<id>.yaml` (identity, provenance, governance);
2. a generated **canonical form** — `datasets/<id>/canonical/` (Parquet, nirs4all-loadable) built from the raw bytes;
3. a generated **identity card** — `datasets/<id>/card.json` + `card.md` (datasheet) + `croissant.json`.

The heavy bytes (raw + canonical) live on **Dataverse** (Recherche Data Gouv); Git tracks only the
descriptor, the card, the manifest, and the catalog index. The whole flow is driven by the
`n4a-datasets` CLI and is **incremental** (re-running only reprocesses what changed).

## 0. One-time setup

```bash
uv venv && uv pip install -e ".[dev,docs]"     # editable nirs4all + nirs4all-io
```

A Dataverse API token is only needed for **publishing** (step 4), not for steps 1–3. See the
[README](README.md#api-token--where-to-put-it).

## 1. Write the descriptor

Copy the template and edit it:

```bash
cp catalog/datasets/example_corn.yaml catalog/datasets/<id>.yaml   # <id> must match the filename
```

`<id>` is a stable slug (`^[a-z0-9]+(_[a-z0-9]+)*$`), e.g. `wheat_protein_foss6500`. Key fields
(authoritative schema: `catalog/schema/dataset_v1.json`):

| Block | Fields |
|---|---|
| identity | `id`, `name`, `version` (semver), `description`, `domain`, `keywords`, `citation` |
| `instrument` | `vendor`, `model`, `serial`, `firmware`, `modality` (NIR/MIR/Raman/UV-Vis/hyperspectral), `axis_unit` (nm/cm-1/none/index/text), `axis_range`, `signal_type` (absorbance/reflectance/…) |
| `targets[]` | `name`, `task_type` (regression/binary_classification/multiclass_classification), `unit`, `range`, `classes` (ordered class names — the canonical Y stores their integer indices) |
| `provenance` | `contributor`, `collection_date`, `reference_method`, `lab_protocol`, `ingest_reader`, `raw_sha256`, `known_exclusions` |
| `governance` | `license` (SPDX), `visibility` (public/restricted/embargo), `confidentiality_class` (public/internal/**confidential**), `owner_steward`, `redistribution_rights`, `consent_ethics_status`, `anonymization_status`, `permitted_use`, `access_policy`, `embargo_until` |
| `datacite` | `authors` (name/orcid/affiliation), `funding`, `related_publications`, `related_software` |
| `dataverse` | `instance` (defaults to Recherche Data Gouv); `doi`/`dataset_version` are filled at publish |

**Governance gate (important).** To be *publishable*, a descriptor must have a complete `governance`
block; `visibility: public` requires `confidentiality_class: public` **and** an open license; and
`confidentiality_class: confidential` is a **hard stop** (such data must not go on Dataverse — keep
it off-cloud). Internal/restricted descriptors are valid in the catalog; they just are not published.

Validate any time:

```bash
python catalog/scripts/validate.py                 # schema validity
python catalog/scripts/validate.py --check-publish  # also require public/embargo datasets to be publishable
```

## 2. Ingest the raw data → canonical form + card

```bash
n4a-datasets add <raw_source> <id>
```

`<raw_source>` is either a **directory** of tabular files (the nirs4all `Xcal/Ycal/Xtrain/...`
convention) or a **single instrument file** (OPUS, JCAMP-DX, SPC, ASD, … — read via `nirs4all-io`).
`add` will:

- copy the raw bytes under `datasets/<id>/raw/` (preserved as-is),
- convert to `datasets/<id>/canonical/` Parquet + an explicit `nirs4all_config.json`,
- write the `manifest.json` (content hashes), the `card.json`, `card.md`, `croissant.json`, and plot assets,
- refresh `catalog/datasets.yaml`.

Supported: single- and multi-source (one X file per source), regression and classification
(`Target.classes` carries label names), and targetless (X-only) datasets. Re-running `add` on
unchanged inputs is a no-op; change the raw data or the descriptor and only that dataset rebuilds.
Re-build just the card with `n4a-datasets qualify <id>`.

Inspect:

```bash
n4a-datasets list
n4a-datasets card <id>
n4a-datasets load <id>     # loads the canonical form as a nirs4all DatasetConfigs
```

## 3. Commit (code + metadata, not the heavy bytes)

```bash
git add catalog/datasets/<id>.yaml catalog/datasets.yaml datasets/<id>/card.json datasets/<id>/card.md datasets/<id>/croissant.json datasets/<id>/manifest.json
git commit -m "data(<id>): add <name>"
git push
```

`datasets/<id>/raw/` and `datasets/<id>/canonical/` (the bytes) are **gitignored** — they belong on
Dataverse. The card, datasheet, Croissant, manifest, and catalog are small and git-tracked.

## 4. Publish to Dataverse (optional, needs a token + a collection)

```bash
export NIRS4ALL_DATAVERSE_TOKEN=...
export NIRS4ALL_DATAVERSE_INSTANCE=https://demo.recherche.data.gouv.fr   # sandbox first!
n4a-datasets publish <id> --collection <alias> --contact-email you@cirad.fr
```

This refuses to publish unless the governance gate passes, creates the Dataverse dataset, uploads the
canonical (and raw) files **with `tabIngest=false`** (so bytes stay pristine), publishes the version,
and mints a **DOI**. Record the returned DOI in the descriptor's `dataverse.doi`, re-run
`n4a-datasets qualify <id>` (so the card/Croissant carry the DOI), and commit.

## Conventions

- `id`: lowercase slug, stable forever (it is the Dataverse/URL identity).
- `version`: semantic; bump on any byte change (the manifest's content hash detects it).
- `license`: SPDX id; public datasets need an open license (CC-BY-4.0, CC0-1.0, ODbL-1.0, …).
- Prefer the **sandbox** (`demo.recherche.data.gouv.fr`) before the production instance.
