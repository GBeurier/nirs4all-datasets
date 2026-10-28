# Datasheet — Tree leaf girdling reflectance spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Tree leaf girdling reflectance spectra. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD tree leaf

## Composition

- **Alignment:** sample level; 2737 sample(s), 2737 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 350–2500 nm | 2737 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| treatment | target | categorical | *Not specified.* | n=2737, missing=0, classes=2, top control (×1563) |
| leaf_code | metadata | categorical | *Not specified.* | n=2737, missing=0, classes=2728, top 'GRD-T1477-MAC01-L500000.asd.txt' (×2) |
| camera | metadata | categorical | *Not specified.* | n=2737, missing=0, classes=5, top Cam02 (×700) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.d51c5b01n`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Original-source loading retains source observations and native axes; this revision supersedes the inherited standardized snapshot counts. See docs/PUBLIC_ORIGIN_LOADING.md.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC0-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Dryad source recorded as CC0-1.0 in blocked inventory; manual download retained as provenance.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `c51ef833ceef6343885fe0993a56d1a1d00fdec268e051482d4fa4f03dc5febf`
- **Processing hash:** `21b87e9bd2872d162f5218a6c73d4bd0f10f0a5b49aea7c2bbc14221cad2abe5` | **metadata hash:** `7114df7988abe7428ae4e7e5843a82d79e50131e5e67502009ccb243e959b862`
