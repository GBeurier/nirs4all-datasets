# nirs4all-datasets

A **citable, reproducible bank of raw NIRS** (Near-Infrared Spectroscopy) **reference datasets** — for
benchmarking, exploring, and comparing models on a common, version-pinned, provenance-rich footing.

A dataset here is **raw measured reality, not a benchmark task**: one or more spectral **sources**
(instruments), any number of **variables** (every target *and* metadata column — nothing is invented, and
nothing is thrown away), the native splits if the source defined them, and full provenance back to the
**origin** that published the data. The *task* — which Y, which split, which metric — is a choice the
consumer makes; it is never baked into the dataset.

Three deliverables:

1. a git-tracked **catalog** — one hand-checkable descriptor + a machine-generated *identity card* (stats,
   per-source/per-variable dataviz, MLCommons Croissant, a Datasheet) per dataset. The heavy bytes never
   enter git.
2. a Python **plugin** — `get("name")` downloads a dataset on demand from its **origin**, verifies its
   SHA-256, caches it, and returns a `NirsDataset`.
3. a **static site** — a browsable, qualified catalog with whole-bank dataviz and per-dataset id-cards.

It reuses [`nirs4all`](../nirs4all) for qualification and [`nirs4all-io`](../nirs4all-io) /
[`nirs4all-formats`](../nirs4all-formats) for reading instrument files (OPUS, JCAMP-DX, SPC, ASD, …).
**It never re-implements NIRS/IO logic.**

> Status: **alpha (0.x), pre-1.0** — the on-disk and API contracts may still change.

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
uv venv && uv pip install -e ".[dev]"   # maturin: builds the native acquisition core into the package
# (uses local editable nirs4all via [tool.uv.sources]; needs a Rust toolchain)
```

## Native acquisition core & language bindings

The **download** of a dataset — version-pinned DOI resolution, redirect-safe Dataverse / Zenodo /
figshare fetch, streaming SHA-256 verification and the pooch-style cache — lives in a small **Rust
core** (`crates/nirs4all-datasets-core`) behind a stable **C ABI** (`n4ds_`), and is published like the
rest of the ecosystem (`nirs4all-io` is the template). The scientific **analysis** layer (cards,
qualify, site, health) stays in pure Python. The cross-language contract is one distributable
`catalog/index.json`; the `n4ds` CLI is the parity oracle. Bindings (all over the same C ABI):

| Binding | Package | Status |
|---|---|---|
| Python | embedded in `nirs4all-datasets` (`nirs4all_datasets._n4ds`, pyo3) | built + tested |
| Rust | `nirs4all-datasets-core` / `-capi` (crates.io) | built + tested |
| WASM/JS | `@nirs4all/datasets-wasm` (npm) — metadata + small public datasets | built + tested |
| R | `nirs4alldatasets` (C shim, r-universe / Release) | built + tested |
| Octave/MATLAB | MEX (GitHub Release zip) | built + tested |

See [`bindings/SPEC.md`](bindings/SPEC.md) (the binding contract) and
[`docs/dev/release_process.md`](docs/dev/release_process.md).

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
- **local cache** (downloaded on demand): the verified canonical Parquet under `pooch.os_cache`.

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
