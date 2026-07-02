# nirs4all-datasets

A **citable, reproducible bank of raw NIRS** (Near-Infrared Spectroscopy) **reference datasets** — for
benchmarking, exploring, and comparing models on a common, version-pinned, provenance-rich footing.

A dataset here is **raw measured reality, not a benchmark task**: one or more spectral **sources**
(instruments), any number of **variables** (every target *and* metadata column), the native splits if
the origin defined them, and full provenance back to the **origin** that published the data. The
*task* — which Y, which split, which metric — is a choice the consumer makes; it is never baked into
the dataset.

The heavy bytes **never enter git and are never re-hosted**. The catalog links to each dataset's
**origin** (Zenodo / a data Dataverse / a vendor archive) and downloads on demand: `get("name")`
resolves a dataset **local-first** (from the registry checkout), otherwise fetches it by its
Dataverse / open-canonical DOI, **SHA-256-verifies** it, caches it through the native acquisition core,
and returns a
`NirsDataset`.

```{admonition} You need the catalog checkout
:class: important
`get()` / `list()` read the git-tracked catalog under a **registry root** (`root=`, default `.`):
`list()` reads `catalog/datasets.yaml`, and `get()` needs the dataset's local descriptor + manifest
before it can fetch. Until the catalog index is bundled into the wheel, a pip-installed consumer points
`get(root=<checkout>)` at a clone of this repository. See {doc}`getting_started`.
```

```{admonition} Boundary rule
:class: important
For NIRS modelling objects and instrument-file reads, nirs4all-datasets **delegates** and re-implements
nothing: it reuses [`nirs4all`](https://nirs4all.readthedocs.io/en/latest/) for PCA projection, outlier
filtering, and the `SpectroDataset` handed back by `to_nirs4all()`, and
[`nirs4all-io`](https://nirs4all-io.readthedocs.io/en/latest/) /
[`nirs4all-formats`](https://nirs4all-formats.readthedocs.io/en/latest/) for reading instrument files.
It owns only catalog-level concerns — descriptors, the canonical Parquet writer, the descriptive card
statistics nirs4all does not expose, Croissant/Datasheet rendering, the index, origin health, and the
site.
```

```{admonition} Status
:class: note
**0.3.x, pre-1.0** — the on-disk and API contracts may still change.
```

## What you get

Three deliverables sit behind one catalog:

- a git-tracked **catalog** — one hand-checkable descriptor plus a machine-generated **identity card**
  (stats, per-source / per-variable dataviz, an MLCommons **Croissant** record, and a Datasheet) per
  dataset. The heavy bytes never enter git.
- an optional Python **package/binding** — `nirs4all_datasets.get("name")` wraps the native acquisition
  core and returns a `NirsDataset` from a registry checkout;
- a static **site** — a browsable, qualified catalog with whole-bank dataviz and per-dataset
  identity cards.

The command-line entry point is **`n4a-datasets`**; see {doc}`getting_started`.

## Contents

```{toctree}
:maxdepth: 2
:caption: Get started

installation
getting_started
```

```{toctree}
:maxdepth: 2
:caption: Catalog

catalog
DATASET_STATUS
DATAVERSE_PENDING
```

```{toctree}
:maxdepth: 2
:caption: Reference

DESIGN
ARCHITECTURE
```

```{toctree}
:maxdepth: 1
:caption: Operations

PUBLISHING
RELEASING
```

## The nirs4all ecosystem

<!-- RTD slugs are assumed equal to the repo name; edit a :link: URL below if a slug differs at import. -->

::::{grid} 1 2 2 2
:gutter: 2

:::{grid-item-card} nirs4all
:link: https://nirs4all.readthedocs.io/en/latest/
Main Python modelling library — pipelines, SpectroDataset, predictions.
:::
:::{grid-item-card} nirs4all-io
:link: https://nirs4all-io.readthedocs.io/en/latest/
Dataset-assembly bridge → SpectroDataset (nirs4all-datasets reads through this).
:::
:::{grid-item-card} nirs4all-formats
:link: https://nirs4all-formats.readthedocs.io/en/latest/
Rust readers for ~58 NIRS/spectroscopy file formats.
:::
:::{grid-item-card} nirs4all-methods
:link: https://nirs4all-methods.readthedocs.io/en/latest/
Portable C-ABI PLS/NIRS engine (libn4m) + bindings.
:::
:::{grid-item-card} nirs4all-lite
:link: https://nirs4all-lite.readthedocs.io/en/latest/
Portable aggregate distribution (Rust + bindings).
:::
:::{grid-item-card} dag-ml
:link: https://dag-ml.readthedocs.io/en/latest/
Reproducible, OOF/leakage-safe ML coordinator.
:::
:::{grid-item-card} dag-ml-data
:link: https://dag-ml-data.readthedocs.io/en/latest/
Typed sample-aligned multi-source data contracts.
:::
::::
