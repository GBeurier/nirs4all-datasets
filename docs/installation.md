# Installation

`nirs4all-datasets` is published on PyPI as **`nirs4all-datasets`** (the importable package is
`nirs4all_datasets`).

```{admonition} Status
:class: note
**Alpha (0.x), pre-1.0.** Requires **Python 3.11+**.
```

## Install with pip

```bash
pip install nirs4all-datasets
```

This installs the pure-Python analysis layer **and** the native acquisition extension
(`nirs4all_datasets._n4ds`) — the small Rust core that resolves a DOI, performs the redirect-safe
download, streams the SHA-256 verification, and manages the cache. There is no separate Python
distribution: one wheel gives you both.

The catalog index, `get()` / `NirsDataset` readers, and the static site all work with the base
install — the `nirs4all` imports are lazy and degrade gracefully.

## Optional extras

The base install browses the catalog and downloads public datasets. Two extras unlock the deeper
integrations, both of which **delegate the NIRS modelling objects and file reads to the ecosystem
libraries** rather than re-implementing them:

`nirs4all`
: ```bash
  pip install "nirs4all-datasets[nirs4all]"
  ```
  Pulls in [`nirs4all`](https://nirs4all.readthedocs.io/en/latest/) (`>=0.9`). Needed for the
  nirs4all-powered parts of card qualification (PCA projection, the outlier filter, signal detection)
  and to hand a dataset to nirs4all via `NirsDataset.to_nirs4all()`. Without it, those nirs4all-backed
  metrics become `None` with a card warning and `to_nirs4all()` raises a clear error; the
  descriptive statistics this package computes itself are unaffected.

`io`
: ```bash
  pip install "nirs4all-datasets[io]"
  ```
  Pulls in [`nirs4all-io`](https://nirs4all-io.readthedocs.io/en/latest/) and
  [`nirs4all-formats`](https://nirs4all-formats.readthedocs.io/en/latest/). Needed only for the
  opt-in "reproduce from origin" path, which re-ingests a dataset from an open origin's **raw**
  vendor bytes (`nirs4all-io` owns assembly; `nirs4all-formats` owns the vendor decoders).

```bash
# everything at once
pip install "nirs4all-datasets[nirs4all,io]"
```

## Development install

The repository builds the native acquisition core with [maturin](https://www.maturin.rs/) and needs a
Rust toolchain. Using [uv](https://docs.astral.sh/uv/), which wires the sibling ecosystem checkouts as
editable sources via `[tool.uv.sources]`:

```bash
uv venv && uv pip install -e ".[dev]"
```

## Dataverse API token

A token is **only** required to fetch **private/anonymized** datasets or to publish to a personal
Dataverse. **Public datasets need no token.** Resolution order:

1. the `NIRS4ALL_DATAVERSE_TOKEN` environment variable (recommended; required in CI);
2. `~/.config/nirs4all-datasets/config.toml` (`chmod 600`):
   ```toml
   [dataverse]
   instance = "https://entrepot.recherche.data.gouv.fr"
   token = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
   ```
3. a project `.env` (gitignored) — see `.env.example`.

The token travels only in the `X-Dataverse-key` header, is never logged, and is never forwarded on a
redirect to signed object storage. **Never commit it.**
