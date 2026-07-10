<!-- SPDX-License-Identifier: CECILL-2.1 OR AGPL-3.0-or-later -->
# nirs4all-datasets-core (Python)

The native (Rust) dataset-**acquisition** core of
[`nirs4all-datasets`](https://github.com/GBeurier/nirs4all-datasets), exposed to
Python via pyo3. It turns a dataset id into verified, cached canonical Parquet — and
nothing else. The scientific *analysis* layer (cards, qualify, site, health) lives in
pure Python in the `nirs4all-datasets` package.

```python
import json, nirs4all_datasets_core as core

index = json.load(open("catalog/index.json"))     # the distributable descriptor+download contract
resolved = core.resolve(index, "corn_eigenvector_nir")
print(resolved["descriptor"]["sources"])          # neutral metadata; no provider Python needed
status = core.fetch(resolved, {"token": "…"})       # download + SHA-256 verify + cache
print(status["dir"])                                # <cache>/<id> (has canonical/dataset.json)
core.verify_cached(resolved, status["dir"])          # offline re-check
```

* `resolve(index, id) -> dict` — the version-pinned contract (tier, Dataverse pin,
  per-file SHA-256, origins, retrieval, and the tier-sanitized descriptor).
* `fetch(resolved, opts={cache_dir?, token?, instance?, timeout_secs?}) -> dict` —
  downloads from the personal Dataverse (Access API by `file_id`, redirect-safe so the
  `X-Dataverse-key` never reaches signed storage) or an OPEN Zenodo / figshare /
  Dataverse origin; streams with an incremental SHA-256 + atomic write.
* `verify_cached(resolved, dir) -> dict` — offline integrity re-check.

Build from source needs a Rust toolchain (`maturin develop`); released wheels are
prebuilt per platform.
