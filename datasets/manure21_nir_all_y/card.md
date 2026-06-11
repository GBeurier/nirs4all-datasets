# Datasheet — MANURE21 NIR all chemistry targets

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** manure21
- **Description:** MANURE21 NIR all chemistry targets. v2.0 standardized NIRS package: 1 spectral source(s), 8 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, manure21
- **Contributor:** NIRS DB MANURE21

## Composition

- **Alignment:** observation level; 490 sample(s), 490 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | spectra-1 | *Not specified.* | NIR | 852.8–2502 nm | 490 | 1003 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| DM | target | numeric | *Not specified.* | n=490, missing=0, range 12.2–90.8, mean 28.94 ± 15.94 |
| OM | target | numeric | *Not specified.* | n=490, missing=0, range 83.3–765.2, mean 215.1 ± 121 |
| AN | target | numeric | *Not specified.* | n=490, missing=0, range 0.01–12.99, mean 2.319 ± 2.758 |
| Total_N | target | numeric | *Not specified.* | n=490, missing=0, range 2.07–40.48, mean 9.575 ± 7.459 |
| P2O5 | target | numeric | *Not specified.* | n=490, missing=0, range 0.84–43.72, mean 7.976 ± 8.373 |
| K2O | target | numeric | *Not specified.* | n=490, missing=0, range 0.66–47.72, mean 10.55 ± 6.976 |
| CaO | target | numeric | *Not specified.* | n=490, missing=0, range 1.53–145.5, mean 13.33 ± 20.09 |
| MgO | target | numeric | *Not specified.* | n=490, missing=0, range 0.52–18.76, mean 3.386 ± 2.661 |
| latitude_wgs84 | metadata | numeric | *Not specified.* | n=490, missing=11, range 47.38–48.97, mean 48.03 ± 0.4279 |
| longitude_wgs84 | metadata | numeric | *Not specified.* | n=490, missing=11, range -4.826–-1.129, mean -2.586 ± 0.8685 |
| manure_type | metadata | categorical | *Not specified.* | n=490, missing=0, classes=6, top Cattle manure (×276) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

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
- **Redistribution rights:** Redistribution not cleared; verify source terms before release.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `8bb92a2bd843d01bebffa2e9f04efbd609825e1e5e0419d134be70d639a1c033`
- **Processing hash:** `326ddc03d1a09092280487d308574822cc24aa12f21ade6958fe7814540aab83` | **metadata hash:** `453693e89aefef54eb811dfa2ddabe32503c1e1c6a71c7f40ae2ef4e7bb0cdc9`
