# Spectral classification correction for 0.3.20

The deployed 242-entry catalog previously counted 99 datasets (40.9%) as
unclassified in its wavelength-coverage chart. This was not the count of unknown
spectroscopy techniques. It combined 57 ECOSTRESS micrometer axes, 26 nominally
NIR datasets with unusable axis declarations, 14 Raman datasets, one MIR/Raman
dataset, and the descriptor-only Lyonia candidate.

## Corrected declarations and representations

`bootstrap.py` recognizes explicit micrometer declarations and maps them to the
supported nanometre representation. `canonical.py` converts numeric coordinate
headers with decimal arithmetic, preserving channel order, intensities,
identities, missing values and the original raw bundle. Bounds and numerical
resolution use the same factor. Canonical configuration records the conversion.
This introduces no new axis-unit enum or C ABI. The PMMA public-origin recipe
declares its native micrometer axis so fresh acquisition follows the same path.

The packaged `spectral_metadata.json` records reviewed declarations, original
grid expectations and source references. It corrects the OSSL MIR/Vis-NIR export
labels, optical ethanol spectra, cartilage, malaria and the legacy EcoSIS
Elvidge leaf units. The six UCR/UEA FTIR datasets retain MIR technique but no
physical axis unit: their exported grids were reconstructed. Rock similarly
retains an unknown technique and unitless grid. Grid mismatches refuse rather than reusing an old correction.
Original files are not rewritten. Source technique mapping no longer guesses
NIR for missing/unknown text or MIR from the `ir` substring of `Vis-SWIR`.
The migration preserves independently reviewed indexed representations such as
ChEMBL vibrational modes instead of trusting older exporter metadata over them.

The evidence links and exact per-source declarations are in
[`spectral_metadata.json`](../../src/nirs4all_datasets/spectral_metadata.json).
No new targets, sample identities, partitions, rights or acquisition routes are
inferred from these spectral corrections.

## Two separate summaries

Spectroscopy family groups the declared techniques; VSWIR groups with NIR and
TIR with MIR. A broad source label is refined only by a known absolute optical
axis. Multiple families produce `mixed`, including a single broad optical block.
The resulting counts are NIR 153, MIR 20, Raman 14, mixed 52, UV-Vis 2 and other 1.

Wavelength coverage uses the documented NIR interval of 780–2500 nm and MIR
interval above 2500 through 25000 nm. A NIR instrument extending to 2550 nm can
therefore have mixed optical coverage while retaining its NIR technique label.
Raman shift axes are never reciprocated into absolute wavelengths; Raman-only
and Raman-plus-optical datasets have separate categories. A known Raman/optical
combination does not claim that every optical axis is available. When a measured
card is pending, public descriptor axes can establish declared coverage without
inventing measured statistics.

| Coverage category | Datasets |
| --- | ---: |
| NIR | 124 |
| MIR | 9 |
| Mixed | 80 |
| Raman | 14 |
| Raman + optical | 1 |
| Axis unavailable | 14 |

The fourteen unavailable optical ranges include six indexed datasets
(`dryad_tree_tissue_nsc_nir_manual`, `nirpy_coffee_classification_nir`,
`nirpy_milk_nir`, `nirpy_milk_powder_nir`, `nirpy_peach_brix_nir`,
`nirpy_plums_brix_firmness_nir`) and
`grapevine_leaftraits_multisensor_nir`, whose supplied source-column coordinates
lack an independently established unit declaration. Their NIR technique is
retained. The six UCR FTIR datasets and UCR Rock also have reconstructed,
unitless coordinates; the documented technique is retained where supported.
No physical axis is reconstructed from channel indices or magnitude.
The overview links to each unresolved card and supplies visible data tables for
both charts. Its unavailable-axis share is 14/242, or 5.8%.

## Actual local reconstruction and checks

78 affected datasets were rebuilt and requalified from locally verified raw
bundles. Their content versions advance by one patch; manifests and integrity
hashes come from the actual new outputs. The original verified OSSL soilsite
sidecar preserves its enrichment. An independent comparison of every rebuilt
source and non-spectral Parquet table confirms exact measurement values,
identities, targets, metadata and partitions against the previous canonical
cache; only converted coordinate headers differ. Raw files match their former
manifest hashes. All 242 descriptors validate, and no catalog entry is stale.
Sample/source/target totals remain 258793 / 279 / 1671.

Qualification used published SDK 1.4.16, IO 0.3.6, Formats 0.2.16 and Methods
1.3.19 in an isolated environment. All previously available PCA and outlier
sections remain computed; a preliminary environment without the SDK was
replaced before the final artifact freeze.

Local checks executed during this batch:

- `python -m pytest -q -o addopts='' -m 'not network'`: 811 passed,
  1 skipped (optional Preflight executable), 37 network cases deselected.
  Descriptor coverage also has a regression ensuring the persisted catalog
  entry schema remains unchanged.
- `cargo test --workspace --locked`: 46 passed; C ABI snapshot checks included.
- `cargo fmt --all --check` and
  `cargo clippy --workspace --all-targets --locked -- -D warnings`: passed.
- WASM Node build and `node bindings/wasm/tests/node_smoke.cjs`: passed using
  Node 22, including native CLI resolve parity.
- Ruff, mypy, catalog validation/publication eligibility and the exact public
  dependency-train check passed. Published 0.3.19 artifacts remain unchanged.
- Chromium 153 checked overview tables, unresolved links, OSSL/ECOSTRESS cards,
  catalog rendering and 390px reflow without page errors or horizontal overflow.

These are local results, not blanket scientific validation of every dataset or
claims about unexecuted network origins. R/Octave native checks and other
platforms use their established CI/release lanes. The server's separate private
hosted-content cohort and CIRAD network/TLS acceptance are independent of this
curated-catalog correction.

Rebuild with the project environment and existing local inputs:

```bash
export NIRS4ALL_OSSL_SOILSITE=/verified/local/ossl_soilsite_L0_v1.2.csv.gz
python scripts/repair_spectral_metadata.py --source-cache /verified/local/datasets
python scripts/repair_spectral_metadata.py --source-cache /verified/local/datasets --write --workers 2
python -m nirs4all_datasets.cli catalog --root .
python -m nirs4all_datasets.cli site --root . --out site
```

The source cache and output tree must be separate. The script is a dry run unless
`--write` is supplied; descriptor-only candidates remain unqualified. Raw payloads
and canonical caches stay outside Git and are not uploaded by this workflow.
