# Dataset catalog

The catalog is the heart of nirs4all-datasets: a git-tracked set of descriptors and machine-generated
identity cards, one per curated dataset. Every entry is **version-pinned** and **provenance-rich**, and
its heavy bytes are downloaded on demand from the dataset's **origin** — never re-hosted here.

## How a dataset is described

Each dataset carries:

- **Sources (X), `1..n`** — one spectral block per instrument, kept separate, with its own axis unit
  and range. Multi-instrument datasets keep each block as its own source; sources are aligned by
  **sample identity**, never by row position.
- **Variables (Y + metadata), `0..n`** — every column is a *potential* target. A target is flagged
  only when the origin declares one; X-only / metadata-only datasets are valid, and no target is ever
  invented.
- **Splits** — native train/test/fold partitions are recorded so you can reproduce a paper's split,
  but they are **documented, never auto-applied**.
- **Tier** — `public` (shown and openly fetchable from the origin), `private` (shown; export needs a
  token), or `anonymized` (variable names masked + numeric targets normalized; export needs a token).
- **Versions** — a **content** version (bumps when the bytes change) and a **metric-protocol** version
  (lets cards be re-qualified under a new protocol without rebuilding the data).

Each generated card bundles descriptive statistics, per-source / per-variable dataviz, an MLCommons
**Croissant** JSON-LD record, and a **Datasheet** (`card.md`).

## Browse what is available

The current, generated overview of every catalogued dataset — its state, whether it is materialized,
its origin, distribution, and human-validation status — lives in the **{doc}`DATASET_STATUS`** page.

From your own checkout you can list and inspect the catalog directly:

```bash
n4a-datasets list                 # every catalogued dataset
n4a-datasets list --tier public   # filter by tier / domain / spectro-family
n4a-datasets card <id>            # one dataset's identity card
```

or from Python:

```python
import nirs4all_datasets as n4ad

n4ad.list(tier="public")
n4ad.card("corn_eigenvector_nir")
```

See {doc}`getting_started` for downloading and loading a dataset.
