# Getting started

This page walks through the two ways to use the catalog: the **Python API** and the **`n4a-datasets`
CLI**. Both resolve a dataset *local-first*, otherwise download it by its Dataverse / open-canonical
DOI, verify its SHA-256, cache it, and return the canonical form. See {doc}`installation` first.

```{admonition} Point at the catalog checkout
:class: note
The API and CLI read the git-tracked catalog under a **registry root** (`root=` / `--root`, default
`.`): `list()` reads `catalog/datasets.yaml`, and `get()` needs the dataset's local descriptor +
manifest before it can fetch. Run from a clone of this repository, or pass `root=<checkout>` /
`--root <checkout>`. (Bundling the index into the wheel for fully standalone use is planned.)
```

## Python API

The consumer surface is three module-level functions — `list`, `card`, and `get` — plus the
`NirsDataset` object that `get` returns.

```python
import nirs4all_datasets as n4ad

n4ad.list()                              # the catalog index (list of dicts), supports keyword filters
n4ad.card("corn_eigenvector_nir")        # the identity card (dict): sources, variables, stats, provenance

ds = n4ad.get("corn_eigenvector_nir")    # -> NirsDataset (fetched from origin, checksum-verified, cached)
```

`list()` forwards keyword filters to the catalog search, e.g.:

```python
n4ad.list(tier="public")
n4ad.list(domain="agriculture", spectro_family="NIR")
```

### Working with a `NirsDataset`

Sources are kept **separate** and are aligned by **sample identity**, never by row position:

```python
ds.sources()                  # e.g. ['X1', 'X2', 'X3'] — the same samples on three NIR instruments
ds.x("X1")                    # one source's spectra as a 2D numpy array
ds.x(concat=False)            # {source_id: array} for every source (sample-aligned)
ds.wavelengths("X1")          # the wavelength axis of a source
ds.sample_ids()               # the sample identities
ds.observation_ids("X1")      # the per-observation identities of a source

ds.variables()                # the declared variables (targets + metadata)
ds.y()                        # all declared targets, per sample (DataFrame or None)
ds.metadata()                 # the metadata columns (each a potential target)
ds.split("original")          # the native split labels, if the origin defined one (never auto-applied)

ds.card()                     # the generated identity card (dict) for this dataset, or None
ds.tier                       # the dataset tier (public | private | anonymized)
```

Hand a dataset to nirs4all for modelling (needs the `[nirs4all]` extra — see {doc}`installation`):

```python
sd = ds.to_nirs4all()         # -> a nirs4all SpectroDataset (assembled, not re-implemented)
```

Hand the same reference dataset to nirs4all-io for pipeline-ready assembly (needs the `[io]` extra):

```python
spec = ds.to_io_spec()        # -> a nirs4all-io DatasetSpec dict over canonical Parquet files
pkg = ds.to_dataset_package() # -> nirs4all_io.DatasetPackage
```

`to_io_spec()` keeps native split labels as metadata; it does not apply train/test partitions. For
multi-source datasets with asymmetric repetitions, bridge one source at a time (`source="X1"`) unless
the sources are uniquely alignable by observation or sample id.

### Tokens for protected datasets

Public datasets need no token. Private / anonymized datasets need a Dataverse token, passed inline or
resolved from the environment / config file:

```python
ds = n4ad.get("some_private_dataset", token="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")
```

`get()` also accepts `root`, `source`, `split`, `instance`, `cache_dir`, `concat`, and `reproduce`
keyword arguments; see its docstring for the full signature.

## CLI (`n4a-datasets`)

The CLI mirrors the dataset lifecycle. Run `n4a-datasets <command> --help` for every flag.

### Inspect and load

```bash
n4a-datasets list                          # list catalog datasets
n4a-datasets list --tier public            # filter by tier / --domain / --spectro-family
n4a-datasets card <id>                      # print one identity card (JSON)
n4a-datasets get <id>                       # load (local-first, else fetch) and print a one-line summary
n4a-datasets get <id> --source X1           # a single source instead of all sources
n4a-datasets get <id> --token <tok>         # a private/anonymized dataset
n4a-datasets status                         # the dataset-status overview
```

### Author and build the catalog (maintainers)

```bash
n4a-datasets bootstrap <source_tree> [--prune] [--force]   # author one descriptor per v2.0 leaf
n4a-datasets add <raw_source> <id>                          # one raw source -> canonical + card + index
n4a-datasets build-all --source-tree <tree> [--site]        # parallel organize + qualify, then index
n4a-datasets qualify <id> [--anonymize]                     # (re)build one card.json
n4a-datasets catalog                                        # regenerate catalog/datasets.yaml
n4a-datasets index                                          # regenerate the catalog index
n4a-datasets health-check                                   # probe open origins -> catalog/health.json
n4a-datasets site [--out site]                              # render the static catalog site
```

### Publishing protected data (future)

```bash
n4a-datasets publish <id> --collection <alias> --contact-email <addr>
n4a-datasets restrict <id> [--off]
n4a-datasets grant <id> --to "@user"      # quote &group aliases: --to "&group"
n4a-datasets revoke <id> --to "@user"
```

```{admonition} Public data is never re-hosted
:class: warning
Publishing is a **future** capability reserved for **protected** (private / anonymized) datasets on a
personal Dataverse. Public datasets are only ever *linked to their origin* and fetched from there. See
{doc}`PUBLISHING`.
```

## Next steps

- Browse what is available in the {doc}`catalog`.
- Read the {doc}`DESIGN` rationale and the {doc}`ARCHITECTURE` reference.
