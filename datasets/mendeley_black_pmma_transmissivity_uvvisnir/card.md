# Datasheet — Mendeley black PMMA transmissivity UV-Vis-NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** mendeley
- **Description:** Mendeley black PMMA transmissivity UV-Vis-NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, mendeley
- **Contributor:** Spectral radiative properties of black PMMA

## Composition

- **Alignment:** observation level; 2 sample(s), 2 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | black PMMA UV-Vis-NIR transmissivity | *Not specified.* | NIR | 0.25–2.6 none | 2 | 2351 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| film_thickness_um | target | numeric | um | n=2, missing=0, range 50–73, mean 61.5 ± 16.26 |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/datasets/8wpgzrp33s/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/8wpgzrp33s/snapshot/1`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/8wpgzrp33s/files?folder_id=root&version=1&$start=0&$limit=1000`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://creativecommons.org/licenses/by/4.0/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** X: native axis unit is 'um' (micrometers), which is not supported by the axis unit enum; axis values remain in micrometers. Multiply by 1000 to convert to nm.; Corrected inherited sample_temperature_C target to film_thickness_um: original files are Transmissivity_50µm_UV-Vis-NIR.xlsx and Transmissivity_73µm_UV-Vis-NIR.xlsx; their sheets contain no temperature measurement.

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

- **Content version:** 1.0.1 | **schema/protocol:** 2.0
- **Content hash:** `7bda9775fca4b483d7fc2d9ac28227af789d48b9f0508dc657bc9c51f914f84d`
- **Processing hash:** `1822df04eca9c91f709170d846fa134f0456ffa4133f93e77544b7d4819038db` | **metadata hash:** `4ca8c3ff9d0ced4a6e003bb1019e26e7ca49dcc574eceb0f3a77f4471912c1fc`
