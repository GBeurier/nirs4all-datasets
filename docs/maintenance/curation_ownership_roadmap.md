# Curation ownership roadmap

This record captures the accepted scope of the current curation and qualification
work. It is not a new backlog or authorization to move every related feature.
The current work fixes the three identified curation and cache consistency bugs,
and moves a numerical method only when a suitable native `nirs4all-methods`
method is absent. All other transfers, including normalization to
`nirs4all-io`, are roadmap items only. Do not modify `nirs4all-io`, `dag-ml`,
or `dag-ml-data` as part of this work.

## Current work

- Curation applies declared missing tokens and numeric sentinels consistently
  with declared source-column renames. The local dependency guard follows
  transitive declared dependencies when excluding response-derived predictors.
- Processing/cache identity includes variable type, role, unit, and dependency
  declarations so changes to these contracts invalidate affected work. The
  focused curation and cache tests passed during implementation; final gate
  results belong in the work's completion report.
- Methods already exposes PCA, Q residuals and Hotelling T²; it also exposes a
  Savitzky–Golay smoothing-residual noise proxy. The latter is a different
  calculation from the second-difference median absolute deviation (MAD)
  roughness proxy in dataset qualification. Do not introduce a duplicate PCA
  kernel merely to transfer ownership.
- Methods 1.3.10 already provides global second-difference MAD roughness through
  `diagnostics.spectral_noise_proxy` and the generic C ABI 2.20. Datasets uses
  `n4m.roles.SpectralNoiseProxy`, with an explicit validity mask and producer
  provenance. Bandwise output is an extension of this existing procedure
  ([Methods PR #46](https://github.com/GBeurier/nirs4all-methods/pull/46)),
  released in Methods 1.3.11; it adds no C ABI entry point or ABI bump. Older
  native libraries can supply global results while bandwise results remain
  unavailable. See the [review](2026-10-30-dcornet-review.md).

Existing dataset PCA qualification stays in place until the native API is
shown to match its complete protocol and satisfy its callers: missing-value
handling, deterministic sampling, component selection, outputs, and degenerate
cases. Existing related methods alone do not establish that parity.

## Ownership and deferred transfers

`nirs4all-datasets` retains source-specific declarations and evidence, origin
and redistribution rights, recipes, curation policy, cache identity, manifests,
and card rendering. It orchestrates qualification and consumes numerical
methods through supported interfaces.

`nirs4all-methods` owns reusable numerical kernels and their public native ABI.
Python interfaces remain thin native facades. Before adding a method, check the
existing API and compare its mathematical definition, missing-data behavior,
population, and output contract with the intended use.

A future `nirs4all-io` slice may own a neutral variable normalization DTO and
normalizer, including missing, invalid, and censored value evidence. It requires
native Rust and Python MVP parity, an explicit contract, and preservation of the
dataset-specific source rules and audit meaning. This is not part of the current
implementation.

Future `dag-ml-data` contracts may represent identities, groups, exclusions,
and fit scopes; `dag-ml` owns the associated split, fit, and OOF leakage
enforcement. These boundaries are recorded for later planning only. This work
does not change either repository or claim to complete those integrations.

## Acceptance and rollout

- Preserve raw source values, declared missing and censor evidence, identity,
  and target-dependency exclusions. Verify renames, sentinels, transitive
  dependencies, and cache invalidation with focused regression tests.
- For native roughness, verify parity against the existing qualification
  protocol, including missing values, constant and short inputs, band outputs,
  and edge cases; exercise both the C ABI and Python facade. Verify Dataset
  integration uses the intended library and reports unavailable native support
  according to the chosen integration contract.
- Run the applicable repository checks and record exact results and any
  remaining limitations in the completion report. ABI changes require the
  Methods repository's version, symbol-snapshot, and documentation gates.
- Changed processing hashes invalidate old caches. Rebuild affected canonical
  outputs and requalify from the actual inputs before publishing regenerated
  artifacts. Never edit old manifests or hashes to make stale data appear
  current. A code change or a passing test alone does not rebuild the catalog.
- The bandwise extension is published in Methods 1.3.11, and the `methods` extra
  requires `nirs4all-methods>=1.3.11` and scikit-learn; the global procedure
  alone is available since 1.3.10.

## Verified local reconstruction — 2026-10-30

All 297 canonical caches and cards were rebuilt from the actual local inputs.
Independent checks verified all 7,311 manifest entries and the unchanged 2,796
raw files. All 319 source profiles identify the native operation, protocol, ABI,
engine version and exact library SHA-256; this distinguishes the development
extension from an installed 1.3.10 artifact. Source rights and tiers remain
135 public and 162 private. The private tier still describes redistribution,
separately from original-source retrieval.

The [machine-readable receipt](../../catalog/curation/remediation_validation_20261030.json)
records the measured checks and their limits. Published issue evidence contains
aggregate counts; 95,180 per-observation issue rows remain in local canonical
mappings. No raw or canonical data payload is committed.

Methods validation passed 30 CTest suites, 1,622 Python tests (7 optional skips)
and 8 Rust generic binding tests. Dataset validation passed with and without the
native provider; the completion report records the final test counts.
Precomputed site profiles record the exact tested development binary.

## Published-artifact verification — 2026-11-02

The bandwise extension is published in nirs4all-methods 1.3.11 (PyPI). In a clean
target directory holding only that wheel (`n4m` 1.3.11, ABI 2.20.0), the
second-difference roughness section was recomputed from the canonical source
Parquet of every one of the 319 source profiles and compared with the committed
cards: all nine fields (`noise_rms`, `snr`, `snr_db`, bandwise minimum and median,
worst-band index and axis, roughness proxy, availability) match, with zero
mismatches at a relative tolerance of 1e-12. The cards therefore reproduce from
the released artifact. They still name the development library
(`1.3.10+abi.2.20.0`, SHA-256 `0dafb507871302f43e7657cc701220a8b59712b432fec8d283ecf7478830b7b3`)
that produced them, because no card was rewritten to simulate a rebuild.

English narrative text is now maintained in the source contracts and descriptor
warnings. Seven contracts with translated unit/evidence labels were rebuilt;
the remaining provenance updates changed descriptive metadata only. All numeric
card values were preserved. The final language audit reviewed all 53 unique
provenance warnings and 76 identity narratives across the 297 regenerated cards.
