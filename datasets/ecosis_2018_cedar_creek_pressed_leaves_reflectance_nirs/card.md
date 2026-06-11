# Datasheet — EcoSIS 2018 Cedar Creek pressed leaves (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS 2018 Cedar Creek pressed leaves (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 9 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** 2018 Cedar Creek pressed leaves

## Composition

- **Alignment:** observation level; 332 sample(s), 332 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | pressed_spec_MN_all_avg.csv | Spectral Evolution PSR+ 3500 | NIR | 400–2400 nm | 332 | 2001 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Species | target | categorical | *Not specified.* | n=332, missing=0, classes=29, top JUVI (×26) |
| Type | target | categorical | *Not specified.* | n=332, missing=0, classes=3, top PIG, RWC (×229) |
| FunctionalGroup | target | categorical | *Not specified.* | n=332, missing=0, classes=3, top broadleaf (×177) |
| FullSpecies | target | categorical | *Not specified.* | n=332, missing=0, classes=28, top Juniperus virginiana (×26) |
| LatinGenus | target | categorical | *Not specified.* | n=332, missing=0, classes=20, top Quercus (×94) |
| LatinSpecies | target | categorical | *Not specified.* | n=332, missing=0, classes=27, top alba (×29) |
| genotype | target | numeric | *Not specified.* | n=332, missing=326, range 2–6, mean 3.333 ± 2.066 |
| C | target | numeric | *Not specified.* | n=332, missing=5, range 35.67–59.82, mean 46.97 ± 4.425 |
| N | target | numeric | *Not specified.* | n=332, missing=5, range 0.75–4.68, mean 1.577 ± 0.5977 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top 0c48eebd-08d9-4411-a2e2-25437fa0950f (×332) |
| site | metadata | numeric | *Not specified.* | n=332, missing=40, range 2–336, mean 72.79 ± 57.86 |
| location | metadata | categorical | *Not specified.* | n=332, missing=332, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=332, missing=332, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=332, missing=0, range 45.4–45.4, mean 45.4 ± 1.423e-14 |
| longitude | metadata | numeric | *Not specified.* | n=332, missing=0, range -93.19–-93.19, mean -93.19 ± 1.423e-14 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top source-provided coordinates when available (×332) |
| year | metadata | numeric | *Not specified.* | n=332, missing=0, range 2022–2022, mean 2022 ± 0 |
| date | metadata | categorical | *Not specified.* | n=332, missing=332, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=332, missing=0, classes=29, top JUVI (×26) |
| genus | metadata | categorical | *Not specified.* | n=332, missing=332, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=332, missing=332, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top Leaf (×332) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=332, missing=332, classes=0, — |
| instrument | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top Spectral Evolution PSR+ 3500 (×332) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top Contact (×332) |
| signal_type | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top reflectance (×332) |
| axis_unit | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top nm (×332) |
| axis_min | metadata | numeric | *Not specified.* | n=332, missing=0, range 400–400, mean 400 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=332, missing=0, range 2400–2400, mean 2400 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=332, missing=0, range 2001–2001, mean 2001 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top 10.1101/2021.04.21.440856v5 \| 10.21232/b5uXd859 \| 10.21232/dep7jvyq (×332) |
| citation | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top Shan Kothari, Megan Erding and Jeannine Cavender-Bares. 2022. 2018 Cedar Creek pressed leaves. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/b5uXd859 (×332) |
| license | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top Creative Commons Attribution Share-Alike (×332) |
| rights_status | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top explicit_open (×332) |
| usage_scope | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top public_reuse_possible (×332) |
| notes | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top EcoSIS package 2018-cedar-creek-pressed-leaves, no interpolation applied by project. (×332) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/2018-cedar-creek-pressed-leaves`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- https://www.biorxiv.org/content/10.1101/2021.04.21.440856v5 — [10.1101/2021.04.21.440856v5](https://doi.org/10.1101/2021.04.21.440856v5)
- 2018 Cedar Creek pressed leaves — [10.21232/b5uXd859](https://doi.org/10.21232/b5uXd859)
- *Not specified.* — [10.21232/dep7jvyq](https://doi.org/10.21232/dep7jvyq)

## Distribution

- **License:** CC-BY-SA-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `0e8c810caef6be2bb2265e4a62b8c466b14d245c1941262f583524ecda0563b3`
- **Processing hash:** `e8f2dacc15cad73c18c4bd8454900470b86b3433dc98209b6ab4fe1987828093` | **metadata hash:** `38de554161f9cd2c5ac184d6df8a9e1b60bdae09ce2c3cf0269dc8efb36cbd66`
