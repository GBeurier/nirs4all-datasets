<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/brand/horizontal-dark.svg">
    <img alt="nirs4all-datasets" src="assets/brand/horizontal.svg" width="440">
  </picture>
</p>

# nirs4all-datasets

A **citable, reproducible bank of raw NIRS** (Near-Infrared Spectroscopy) **reference datasets** — for
benchmarking, exploring, and comparing models on a common, version-pinned, provenance-rich footing.

Part of the [open-source NIRS tools](https://nirs4all.org/open-source-nirs-tools.html)
ecosystem: file readers, datasets, methods, browser modelling, reproducible pipelines,
papers, benchmarks, and release dashboards for near-infrared spectroscopy.

A dataset here is **raw measured reality, not a benchmark task**: one or more spectral **sources**
(instruments), any number of **variables** (every target *and* metadata column — nothing is invented, and
nothing is thrown away), the native splits if the source defined them, and full provenance back to the
**origin** that published the data. The *task* — which Y, which split, which metric — is a choice the
consumer makes; it is never baked into the dataset.

This repository is split into one native acquisition layer and optional consumer-facing layers:

1. a git-tracked **catalog** — one hand-checkable descriptor + a machine-generated *identity card* (stats,
   per-source/per-variable dataviz, MLCommons Croissant, a Datasheet) per dataset. The heavy bytes never
   enter git.
2. a native **acquisition core** — Rust crates + stable `n4ds_` C ABI + CLI/bindings that resolve dataset
   ids, fetch canonical bytes from their origin, verify SHA-256, and manage the platform cache. This
   surface does **not** require Python.
3. an optional Python **package/binding** — `nirs4all-datasets` embeds that acquisition core for
   `get()/retrieve()/NirsDataset`, plus the catalog, cards, and site tooling.
4. optional **ecosystem bridges** — the `[nirs4all]` extra for modelling/qualification and the `[io]`
   extra for raw-origin reproduction through `nirs4all-io` / `nirs4all-formats`.

It reuses [`nirs4all`](../nirs4all) only through the optional `[nirs4all]` bridge for qualification and
`to_nirs4all()`, and [`nirs4all-io`](../nirs4all-io) / [`nirs4all-formats`](../nirs4all-formats) only
through the optional `[io]` bridge for raw-origin reproduction. **It never re-implements NIRS/IO logic.**

> Status: **0.3.x, pre-1.0** — the on-disk and API contracts may still change.

## The dataset model

- **Sources (X) — `1..n`, kept separate.** Multi-instrument / multi-block datasets keep each block as its
  own source. Sources may even carry *different numbers of spectra* (asymmetric repetitions): they are
  aligned by **sample identity** (`sample_id`), **never by row position**.
- **Variables (Y + metadata) — `0..n`.** There is no intrinsic Y/metadata distinction: every column is a
  *potential* target. A dataset may declare no target at all (X-only / metadata-only is valid). Declared
  targets are flagged; everything else is kept as metadata, with full per-variable dataviz either way.
- **Splits — documented, never auto-applied.** Native train/test/fold partitions are recorded so you can
  reproduce a paper's split, but `get()` never silently applies one.
- **Tiers — how a dataset is shown and exported.** `public` (everything shown, openly fetchable from the
  origin), `private` (everything shown; export needs a token), `anonymized` (variable names masked +
  targets normalized; export needs a token). **Bytes are never served from git or the site** — the catalog
  points at the origin DOI/URL; a personal Dataverse is only a *future* fallback for protected datasets.
- **Versions — two axes.** A **content** version (bumps when the dataset bytes change) and a
  **metric-protocol** version (lets the cards be re-qualified under a new protocol without rebuilding the
  data).

## Install (development)

```bash
uv venv && uv pip install -e ".[dev]"   # builds the optional Python package + embedded native core
# (uses local editable sibling bridges via [tool.uv.sources]; needs a Rust toolchain)
```

## Native acquisition core, bindings, and optional bridges

The **download/acquisition** path of a dataset — version-pinned DOI resolution, redirect-safe Dataverse /
Zenodo / figshare fetch, streaming SHA-256 verification, and platform-cache management — lives in a small
**Rust core** (`crates/nirs4all-datasets-core`) behind a stable **C ABI** (`n4ds_`). The scientific
**analysis** layer (cards, qualify, site, health) stays in Python. The cross-language contract is one
distributable `catalog/index.json`; `n4ds resolve` returns both the byte contract and the tier-sanitized
schema-2.0 descriptor (`sources`, `variables`, `ids`, `splits`, `retrieval`). The `n4ds` CLI is the
parity oracle. Surfaces over that core:

| Binding | Package | Status |
|---|---|---|
| Python | optional `nirs4all-datasets` package, embedding `nirs4all_datasets._n4ds` (pyo3) | built + tested |
| Rust | `nirs4all-datasets-core` / `-capi` (crates.io) | built + tested |
| WASM/JS | `@nirs4all/datasets-wasm` (npm) — metadata + small public datasets | built + tested |
| R | `nirs4alldatasets` (C shim, r-universe / Release) | built + tested |
| Octave/MATLAB | MEX (GitHub Release zip) | built + tested |

See [`bindings/SPEC.md`](bindings/SPEC.md) (the binding contract) and
[`docs/dev/release_process.md`](docs/dev/release_process.md).

For the high-level Python API, `get()/list()/card()` still operate against a registry root checkout
(`catalog/` + `datasets/`). For non-Python consumers, the native acquisition core consumes the bundled
or committed `catalog/index.json` contract directly. R/WASM/Rust clients do not need the Python provider
package: they resolve the index, inspect the returned descriptor, fetch/verify the listed files, then read
the canonical Parquet with host-native tooling.

## Quickstart

```python
import nirs4all_datasets as n4ad

n4ad.list()                              # the catalog index
n4ad.card("corn_eigenvector_nir")        # the identity card (dict): sources, variables, stats, provenance

ds = n4ad.get("corn_eigenvector_nir")    # -> NirsDataset (fetched from origin, checksum-verified, cached)
ds.sources()                             # ['X1', 'X2', 'X3'] — the same corn measured on three NIR instruments
ds.x("X1")                               # one source's spectra as a 2D numpy array
ds.x(concat=False)                       # {source_id: array} for every source (sample-aligned, not row-aligned)
ds.y()                                   # all declared targets, per sample
ds.metadata()                            # the metadata columns (each a potential target)
ds.split("original")                     # the native split labels, if the source defined one
ds.to_nirs4all()                         # hand off to nirs4all for modelling
```

Private / anonymized datasets need a Dataverse token: `n4ad.get("name", token=...)`.

## CLI (`n4a-datasets`)

```text
bootstrap <tree>                 author schema-2.0 descriptors from <tree>/v2.0/*  (--prune to re-base)
build-all --source-tree <tree>   organize + qualify every dataset in parallel  (--protocol-refresh, --site)
add <raw_source> <id>            one raw source -> canonical + card + index
qualify <id>                     (re)build a dataset's card  (--anonymize -> card.anon.json)
health-check                     probe each dataset's open origins -> catalog/health.json
catalog | list | card | get      regenerate the index / inspect / load a dataset
publish | grant | revoke | restrict   personal-Dataverse governance for protected data (future)
```

`n4a-datasets <command> --help` documents every flag.

## What lives where (3-tier storage)

- **git** (small, tracked): `catalog/datasets/<id>.yaml` (descriptor), `catalog/datasets.yaml` (index +
  whole-bank summary), and per-dataset `card.json` / `card.md` / `croissant.json` / `manifest.json`.
- **the origin** (Zenodo, a data Dataverse, a vendor archive, …): the raw + canonical **bytes**, fetched
  on demand and never re-hosted by this project.
- **local cache** (downloaded on demand): the verified canonical Parquet under the native acquisition
  core's platform cache root.

## API token — where to put it

A Dataverse API token is **only** needed to fetch **private/anonymized** datasets or to publish to a
personal Dataverse; public datasets need none. Resolution order:

1. Environment variable `NIRS4ALL_DATAVERSE_TOKEN` (recommended; required in CI).
2. `~/.config/nirs4all-datasets/config.toml` (`chmod 600`):
   ```toml
   [dataverse]
   instance = "https://entrepot.recherche.data.gouv.fr"
   token = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
   ```
3. A project `.env` (gitignored) — see `.env.example`.

The token travels only in the `X-Dataverse-key` header, is never logged, and is never sent on a redirect
to signed object storage. **Never commit it** (`.env`, `config.toml`, `*.token` are gitignored).

## Contributing

Full walkthrough in **[CONTRIBUTING.md](CONTRIBUTING.md)**; the design is in
**[docs/DESIGN.md](docs/DESIGN.md)**. The green gate (run before every commit) mirrors CI:

```bash
ruff check . && mypy --config-file pyproject.toml src
python catalog/scripts/validate.py            # every descriptor is schema-valid
pytest -q
```

## License

**Code** is dual-licensed open-source — **`CeCILL-2.1 OR AGPL-3.0-or-later`** (your choice) — with an
optional **commercial license** for closed-source / SaaS use; for any commercial use, contact
<nirs4all-admin@cirad.fr>. See [`LICENSING.md`](LICENSING.md), [`LICENSES/`](LICENSES/) and
[`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

**Catalog content** (cards, datasheets, metadata) is licensed **CC-BY-4.0**. Each **dataset** carries
its **own** SPDX license in its descriptor and is only ever linked to its origin — open data is never
re-hosted under a different license.
