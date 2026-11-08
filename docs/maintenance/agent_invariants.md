---
orphan: true
---

# Residual Datasets agent invariants

## Uncovered maintenance rules

Curated descriptors refined by `scripts/curate_catalog.py` must not be regenerated indiscriminately with a full `bootstrap`; rebuild selected datasets with `curate_catalog.migrate_one`. The old approximately-200 rewrite warning is historical, not a current inventory.

Dataset-specific identities must not use global suffix-stripping or grouping heuristics, or infer joins from equal row counts; unknown identity is `null`. Keep original source columns, declared renames/missing tokens/sentinels and target-dependency exclusions under the existing curation contract.

Only enrich index entries from cards/manifests whose processing and metadata hashes match the current descriptor; otherwise set `is_stale` and omit computed fields. Failed optional card computations keep stable keys as `None` plus warnings, not dropped keys. Sanitize all card floats to finite JSON.

Keep `generation.source_relpath` as the reconciliation locator and exclude the complete `generation` block from both hashes. The existing managed/prune policy still protects human descriptors and human orphans; `--force` does not authorize overwriting them.

At the standardized-leaf canonical-writer seam, preserve relative `canonical/dataset.json` paths (`resolve_config()` absolutizes them), optional no-Y variables, float32 chunked spectral reads and `ConversionStatus` OK/PARTIAL-with-warnings/FAILED-with-no-convertible-X distinctions. This seam does not re-parse vendor files or establish support in every acquisition binding.

## Residual invocation variants

From the Datasets checkout and its package venv, retain these uncovered selections. The R recipe tests include native/Windows ARM64/WebR build recipes; the no-default build needs the Rust acquisition toolchain and sibling IO/Formats dependencies. Targeted tests supplement, not replace, the owner gate.

```bash
pytest -q bindings/r/tests
cargo build -p nirs4all-datasets-core --no-default-features
pytest tests/test_canonical.py
pytest tests/test_schema.py::<test_name>
cargo test -p nirs4all-datasets-core <name>
wasm-pack build bindings/wasm --release --target nodejs --out-dir pkg-node --scope nirs4all
node bindings/wasm/tests/node_smoke.cjs
```

Version-sync `scripts/bump_version.sh --check` and offline `python scripts/check_release_train.py` retain their conditions in the existing release blockers. ABI, bindings, release platforms and publication restrictions remain in those owner documents; this note does not duplicate them.
