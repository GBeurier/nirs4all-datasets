# Datasheet — Diesel fuels NIR Eigenvector

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** diesel
- **Description:** Diesel fuels NIR Eigenvector. v2.0 standardized NIRS package: 1 spectral source(s), 7 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, diesel
- **Contributor:** Eigenvector data sets

## Composition

- **Alignment:** sample level; 784 sample(s), 784 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | diesel_spec | unknown | NIR | 750–1550 nm | 784 | 401 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| BP50 | target | numeric | *Not specified.* | n=784, missing=389, range 182–297, mean 258.4 ± 20.72 |
| CN | target | numeric | *Not specified.* | n=784, missing=403, range 36.9–61.3, mean 49.16 ± 3.52 |
| D4052 | target | numeric | *Not specified.* | n=784, missing=389, range 0.7818–0.8728, mean 0.8446 ± 0.01542 |
| FLASH | target | numeric | *Not specified.* | n=784, missing=389, range 23–96, mean 62.43 ± 8.648 |
| FREEZE | target | numeric | *Not specified.* | n=784, missing=389, range -59.5–6.6, mean -14.01 ± 11.68 |
| TOTAL | target | numeric | *Not specified.* | n=784, missing=389, range 8.3–47.2, mean 30.75 ± 6.759 |
| VISC | target | numeric | *Not specified.* | n=784, missing=389, range 1.12–4.05, mean 2.517 ± 0.5284 |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `manual`, license *Not specified.*: `https://eigenvector.com/wp-content/uploads/2019/06/SWRI_Diesel_NIR_CSV.zip`
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
- **Redistribution rights:** license unknown, redistribution not cleared
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `31deae41b71565e75d54780a71ab4b12d20c36cc0bdb2e10dc4d20159150cae2`
- **Processing hash:** `70d479d26ddebd5a57747e5cf6eb17f74d362699628a3a9e0ba93ecff6ac9b0a` | **metadata hash:** `a42d6bc96426733597e7def0578e95ec5c9b10846d6e116dd590ab13e5c11eb5`
