# Datasheet — Mendeley coffee drying FT-NIR moisture

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** mendeley
- **Description:** Mendeley coffee drying FT-NIR moisture. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, mendeley
- **Contributor:** Fourier Transform Near Infrared (FT-NIR) spectral monitoring of parchment coffee beans during drying

## Composition

- **Alignment:** observation level; 76 sample(s), 76 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | FT-NIR spectra | FT-NIR spectrometer | NIR | 4000–1.2e+04 cm-1 | 76 | 2001 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Moisture_WB | target | numeric | *Not specified.* | n=76, missing=3, range 8.5–52.49, mean 32.29 ± 17.63 |
| sample_group | metadata | categorical | *Not specified.* | n=76, missing=0, classes=21, top M 10 (×5) |
| replicate | metadata | numeric | *Not specified.* | n=76, missing=0, range 1–5, mean 2.421 ± 1.169 |
| moisture_standard_deviation | metadata | numeric | *Not specified.* | n=76, missing=3, range 0.1029–2.019, mean 0.5485 ± 0.463 |
| moisture_coefficient_of_variation_pct | metadata | numeric | *Not specified.* | n=76, missing=3, range 0.2026–4.11, mean 2.009 ± 1.138 |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/datasets/7c6gx7rr6d/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/7c6gx7rr6d/snapshot/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/7c6gx7rr6d/files?folder_id=root&version=1&$start=0&$limit=1000`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://creativecommons.org/licenses/by/4.0/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Original-source loading retains source observations and native axes; this revision supersedes the inherited standardized snapshot counts. See docs/PUBLIC_ORIGIN_LOADING.md.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Mendeley Data record is licensed CC BY 4.0; redistribution/publication reuse allowed with attribution.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `fcc957e26197727a3176ce20d3ba622e14c06f1f79f234f1fed911ec59e32dc2`
- **Processing hash:** `8d4712d1bea002dbd3774fa08646acc6dd0e0076fa1f72a5665a2b1d949d95b6` | **metadata hash:** `d35d2103c6d57ac714340ba23f59c80c58e0f0552a561428e1c50f77f4396610`
