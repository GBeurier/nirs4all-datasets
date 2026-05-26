# nirs4all-datasets

A registry of NIRS reference datasets: raw native data + a canonical, nirs4all-loadable form,
each qualified into an **identity card** and published (DOI) on Recherche Data Gouv / Dataverse.

```{toctree}
:maxdepth: 2

datasets/index
```

## Quickstart

```python
import nirs4all_datasets as n4ad

n4ad.get_settings()            # resolved Dataverse instance + (masked) token
```

```bash
n4a-datasets catalog           # (re)build the catalog index
n4a-datasets list              # browse datasets
n4a-datasets card <id>         # a dataset's identity card
```

The dataset pages below are generated from each dataset's `card.json` (`docs/gen.py`).
```
