# nirs4all-datasets

Store, **qualify**, and organize NIRS (Near-Infrared Spectroscopy) reference datasets for
benchmarks and lab experiments — following research/industrial ML standards (FAIR, DOI-citable,
reproducible).

- **Code** lives on GitHub (this repo): the Python package, the dataset **catalog** (descriptors +
  generated *identity cards*), and a static site.
- **Data** lives on [Recherche Data Gouv](https://entrepot.recherche.data.gouv.fr) (a French national
  [Dataverse](https://dataverse.org) instance, INRAE) — free, sovereign, with native DOIs, versions,
  embargoes and restricted files. The [CIRAD Dataverse](https://dataverse.cirad.fr) is also supported.
- **Access** is *pooch-style*: `load("name")` downloads a dataset on demand by its pinned DOI/version,
  verifies its checksum, and caches it locally for reuse.

It reuses [`nirs4all`](../nirs4all) for qualification and [`nirs4all-io`](../nirs4all-io) for reading
instrument formats (OPUS, JCAMP-DX, SPC, ASD, …). It never re-implements NIRS/IO logic.

> Status: **alpha / under construction.** See [`docs`](docs/) and the implementation plan.

## Install (development)

```bash
uv venv && uv pip install -e ".[dev,docs]"
# (uses local editable nirs4all + nirs4all-io via [tool.uv.sources])
```

## Quickstart

```python
import nirs4all_datasets as n4ad

n4ad.list()                       # the catalog
n4ad.card("corn_protein")         # the dataset identity card (dict)
ds = n4ad.load("corn_protein")    # -> nirs4all DatasetConfigs (downloaded, checksummed, cached)
```

## API token — where to put it

A Dataverse API token is **only** needed to **upload/publish** datasets or to download
**private/restricted** ones; public datasets need no token. Resolution order:

1. Environment variable `NIRS4ALL_DATAVERSE_TOKEN` (recommended; required in CI).
2. `~/.config/nirs4all-datasets/config.toml` (`chmod 600`):
   ```toml
   [dataverse]
   instance = "https://entrepot.recherche.data.gouv.fr"
   token = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
   ```
3. A project `.env` (gitignored) — see `.env.example`.

In CI, store it as a GitHub Actions secret `DATAVERSE_TOKEN`. **Never commit it**
(`.env`, `config.toml`, `*.token` are gitignored). Tokens expire after 1 year — rotate them.

## License

Code: MIT (see [`LICENSE`](LICENSE)). Each dataset carries its own SPDX license in its descriptor.
