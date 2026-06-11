# Datasheet — Grapevine LeafTraits multisensor NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** grapevine
- **Description:** Grapevine LeafTraits multisensor NIR. v2.0 standardized NIRS package: 4 spectral source(s), 31 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, grapevine
- **Contributor:** GRAPEVINE LeafTraits local source files

## Composition

- **Alignment:** observation level; 2079 sample(s), 8316 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X1 | micronir | micronir | NIR | 908.1–1676 none | 2079 | 125 |
| X2 | neospectra | neospectra | NIR | 1350–2550 none | 2079 | 257 |
| X3 | micronir_neospectra | micronir_neospectra | NIR | 908.1–2550 none | 2079 | 276 |
| X4 | asd | asd | NIR | 400–2500 none | 2079 | 2101 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| LMA | target | categorical | *Not specified.* | n=2079, missing=0, classes=1168, top 4,83831026999362 (×11) |
| WCf | target | categorical | *Not specified.* | n=2079, missing=643, classes=1423, top 0,730133752950433 (×2) |
| WQ | target | numeric | *Not specified.* | n=2079, missing=1993, range 61–137, mean 88.62 ± 15.03 |
| An | target | categorical | *Not specified.* | n=2079, missing=1972, classes=107, top 1,639896968 (×1) |
| PSI | target | categorical | *Not specified.* | n=2079, missing=1974, classes=102, top -0,637 (×2) |
| WUEintr | target | categorical | *Not specified.* | n=2079, missing=1975, classes=104, top 183,344392601678 (×1) |
| WUEinst | target | categorical | *Not specified.* | n=2079, missing=1975, classes=104, top 11,3140818666648 (×1) |
| gsw | target | categorical | *Not specified.* | n=2079, missing=1, classes=2074, top 0,3240405 (×2) |
| gbw | target | categorical | *Not specified.* | n=2079, missing=1, classes=1739, top 2,918605 (×5) |
| gtw | target | categorical | *Not specified.* | n=2079, missing=1, classes=2072, top 0,0147365 (×2) |
| E_apparent | target | categorical | *Not specified.* | n=2079, missing=1, classes=2077, top 0,0002330015 (×2) |
| VPcham | target | categorical | *Not specified.* | n=2079, missing=1, classes=2077, top 2,3235295 (×2) |
| VPref | target | categorical | *Not specified.* | n=2079, missing=1, classes=2076, top 2,5061955 (×2) |
| VPleaf | target | categorical | *Not specified.* | n=2079, missing=1, classes=2077, top 4,5957205 (×2) |
| VPDleaf | target | categorical | *Not specified.* | n=2079, missing=1, classes=2075, top 2,441038 (×2) |
| H2O_r | target | categorical | *Not specified.* | n=2079, missing=1, classes=2077, top 22,7950135 (×2) |
| H2O_s | target | categorical | *Not specified.* | n=2079, missing=1, classes=2077, top 22,859375 (×2) |
| H2O_leaf | target | categorical | *Not specified.* | n=2079, missing=1, classes=2077, top 45,213667 (×2) |
| Fs | target | categorical | *Not specified.* | n=2079, missing=1, classes=2076, top 110,3550185 (×2) |
| Fm. | target | categorical | *Not specified.* | n=2079, missing=1, classes=2077, top 108,7147905 (×2) |
| PhiPS2 | target | categorical | *Not specified.* | n=2079, missing=1, classes=2075, top 0,3937105 (×2) |
| ETR | target | categorical | *Not specified.* | n=2079, missing=1, classes=2077, top 57,317551 (×2) |
| rh_s | target | numeric | *Not specified.* | n=2079, missing=2071, range 38–59, mean 47.38 ± 7.558 |
| rh_r | target | numeric | *Not specified.* | n=2079, missing=2072, range 33–58, mean 47.43 ± 8.696 |
| Tref | target | numeric | *Not specified.* | n=2079, missing=2071, range 31–34, mean 32.25 ± 1.165 |
| Tleaf | target | numeric | *Not specified.* | n=2079, missing=2066, range 31–35, mean 32.85 ± 1.405 |
| P_atm | target | numeric | *Not specified.* | n=2079, missing=2045, range 101–101, mean 101 ± 0 |
| Qamb | target | numeric | *Not specified.* | n=2079, missing=1045, range 131–1932, mean 913.1 ± 470.1 |
| G | target | categorical | *Not specified.* | n=2079, missing=1, classes=2074, top 0,3240405 (×2) |
| Species_code_grpStrat | target | categorical | *Not specified.* | n=2079, missing=536, classes=246, top V1576 (×13) |
| Brix | target | categorical | *Not specified.* | n=2079, missing=0, classes=1, top not_available_in_grapevine_source (×2079) |
| Leaf_ID | metadata | categorical | *Not specified.* | n=2079, missing=0, classes=2079, top 4005_20/07/21 (×1) |
| Experiment | metadata | categorical | *Not specified.* | n=2079, missing=0, classes=2, top Greenhouse (×1543) |
| Phenotyping_type | metadata | categorical | *Not specified.* | n=2079, missing=0, classes=2, top HT (×1972) |
| li600_present | metadata | categorical | *Not specified.* | n=2079, missing=0, classes=2, top True (×2078) |
| instruments | metadata | categorical | *Not specified.* | n=2079, missing=0, classes=1, top MicroNIR \| NeoSpectra \| MicroNIR_NeoSpectra \| ASD (×2079) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): historical_splits_documented_not_applied: 2079

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** Rights retained from source metadata; review before public redistribution.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `2b36cd90db0658aec00a485eac10b03ad70e34018e530bc51dd3e6e1628065e8`
- **Processing hash:** `22f21b9ac57b6f69247aae6f79f94a14da7d999a7e8e5491e11d9b690e0f6077` | **metadata hash:** `bda8a3d59ea36308dbc93f190365aaf3188879af90dd047f5d471b78f53052c1`
