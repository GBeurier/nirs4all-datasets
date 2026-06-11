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
| LMA | target | numeric | *Not specified.* | n=2079, missing=0, range 1.429–7.586, mean 4.573 ± 0.9536 |
| WCf | target | numeric | *Not specified.* | n=2079, missing=643, range 0.6061–0.8584, mean 0.7293 ± 0.03172 |
| WQ | target | numeric | *Not specified.* | n=2079, missing=643, range 41.1–189.5, mean 86.39 ± 17.06 |
| An | target | numeric | *Not specified.* | n=2079, missing=1972, range 0.05647–16.47, mean 6.299 ± 3.6 |
| PSI | target | numeric | *Not specified.* | n=2079, missing=1974, range -1.966–-0.26, mean -0.9622 ± 0.3938 |
| WUEintr | target | numeric | *Not specified.* | n=2079, missing=1975, range 14.13–187.6, mean 90.95 ± 37.11 |
| WUEinst | target | numeric | *Not specified.* | n=2079, missing=1975, range 0.8329–12.39, mean 4.364 ± 2.044 |
| gsw | target | numeric | *Not specified.* | n=2079, missing=1, range -0.01938–0.9363, mean 0.1479 ± 0.1499 |
| gbw | target | numeric | *Not specified.* | n=2079, missing=1, range 2.916–2.921, mean 2.919 ± 0.0007109 |
| gtw | target | numeric | *Not specified.* | n=2079, missing=1, range -0.01951–0.7074, mean 0.1342 ± 0.1278 |
| E_apparent | target | numeric | *Not specified.* | n=2079, missing=1, range -0.000356–0.01696, mean 0.003423 ± 0.003517 |
| VPcham | target | numeric | *Not specified.* | n=2079, missing=1, range 1.683–3.282, mean 2.374 ± 0.2638 |
| VPref | target | numeric | *Not specified.* | n=2079, missing=1, range 1.611–3.106, mean 2.278 ± 0.3003 |
| VPleaf | target | numeric | *Not specified.* | n=2079, missing=1, range 3.391–7.227, mean 4.879 ± 0.5416 |
| VPDleaf | target | numeric | *Not specified.* | n=2079, missing=1, range 1.009–5.169, mean 2.505 ± 0.6768 |
| H2O_r | target | numeric | *Not specified.* | n=2079, missing=1, range 15.88–30.58, mean 22.49 ± 2.95 |
| H2O_s | target | numeric | *Not specified.* | n=2079, missing=1, range 16.6–32.32, mean 23.43 ± 2.596 |
| H2O_leaf | target | numeric | *Not specified.* | n=2079, missing=1, range 33.51–71.71, mean 48.17 ± 5.398 |
| Fs | target | numeric | *Not specified.* | n=2079, missing=1, range 68.21–327.4, mean 138.7 ± 36.84 |
| Fm. | target | numeric | *Not specified.* | n=2079, missing=1, range 71–455.7, mean 239.9 ± 74.46 |
| PhiPS2 | target | numeric | *Not specified.* | n=2079, missing=1, range 0.009246–0.7361, mean 0.383 ± 0.163 |
| ETR | target | numeric | *Not specified.* | n=2079, missing=1, range 3.983–370.7, mean 128.8 ± 67.05 |
| rh_s | target | numeric | *Not specified.* | n=2079, missing=1, range 31.04–76.22, mean 49.97 ± 7.556 |
| rh_r | target | numeric | *Not specified.* | n=2079, missing=1, range 29.23–73.59, mean 48.05 ± 8.434 |
| Tref | target | numeric | *Not specified.* | n=2079, missing=1, range 24.88–36.44, mean 32.02 ± 1.625 |
| Tleaf | target | numeric | *Not specified.* | n=2079, missing=1, range 26.09–39.52, mean 32.29 ± 1.938 |
| P_atm | target | numeric | *Not specified.* | n=2079, missing=1, range 100.7–101.9, mean 101.3 ± 0.2958 |
| Qamb | target | numeric | *Not specified.* | n=2079, missing=1, range 114.5–1938, mean 947.9 ± 475 |
| G | target | numeric | *Not specified.* | n=2079, missing=1, range -0.01938–0.9363, mean 0.1479 ± 0.1499 |
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
- **Content hash:** `e82b52f5e07d78e1faa3fde635eaa716c2e7e73973650abf6a2fb14f76417336`
- **Processing hash:** `22f21b9ac57b6f69247aae6f79f94a14da7d999a7e8e5491e11d9b690e0f6077` | **metadata hash:** `bda8a3d59ea36308dbc93f190365aaf3188879af90dd047f5d471b78f53052c1`
