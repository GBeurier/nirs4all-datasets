# Datasheet — EcoSIS CABO 2018-2019 Leaf-Level Spectra (transmittance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS CABO 2018-2019 Leaf-Level Spectra (transmittance). v2.0 standardized NIRS package: 1 spectral source(s), 32 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** CABO 2018-2019 Leaf-Level Spectra

## Composition

- **Alignment:** observation level; 1971 sample(s), 1971 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | trans_spec.csv | Spectra Vista Corporation HR-1024i | NIR | 400–2400 nm | 1971 | 2001 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| species | target | categorical | *Not specified.* | n=1971, missing=0, classes=111, top Populus tremuloides Michaux (×120) |
| latin.genus | target | categorical | *Not specified.* | n=1971, missing=0, classes=66, top Acer (×265) |
| latin.species | target | categorical | *Not specified.* | n=1971, missing=0, classes=94, top tremuloides (×120) |
| growth.form | target | categorical | *Not specified.* | n=1971, missing=0, classes=4, top tree (×1124) |
| family | target | categorical | *Not specified.* | n=1971, missing=0, classes=31, top Sapindaceae (×268) |
| genus | target | categorical | *Not specified.* | n=1971, missing=0, classes=66, top Acer (×265) |
| functional.group | target | categorical | *Not specified.* | n=1971, missing=0, classes=7, top broadleaf (×996) |
| SLA | target | numeric | *Not specified.* | n=1971, missing=28, range 2.453–118.5, mean 17.1 ± 9.319 |
| LDMC | target | numeric | *Not specified.* | n=1971, missing=41, range 35.81–573, mean 353.7 ± 92.39 |
| Cmass | target | numeric | *Not specified.* | n=1971, missing=8, range 36.72–56.95, mean 46.92 ± 2.708 |
| Nmass | target | numeric | *Not specified.* | n=1971, missing=8, range 0.7948–5.953, mean 2.257 ± 0.7088 |
| solubles_mass | target | numeric | *Not specified.* | n=1971, missing=52, range 23.68–88.95, mean 63.9 ± 12.84 |
| hemicellulose_mass | target | numeric | *Not specified.* | n=1971, missing=56, range 2.229–42.93, mean 14.15 ± 7.954 |
| cellulose_mass | target | numeric | *Not specified.* | n=1971, missing=25, range 5.19–34.32, mean 13.95 ± 6.584 |
| lignin_mass | target | numeric | *Not specified.* | n=1971, missing=25, range 0.5314–23.44, mean 7.68 ± 4.237 |
| chlA_mass | target | numeric | *Not specified.* | n=1971, missing=30, range 1.242–28.57, mean 7.26 ± 3.697 |
| chlB_mass | target | numeric | *Not specified.* | n=1971, missing=30, range 0.388–10.82, mean 2.434 ± 1.27 |
| car_mass | target | numeric | *Not specified.* | n=1971, missing=30, range 0.193–5.297, mean 1.554 ± 0.7151 |
| Al_mass | target | numeric | *Not specified.* | n=1971, missing=1294, range 0–0.332, mean 0.04917 ± 0.03904 |
| B208.9_mass | target | numeric | *Not specified.* | n=1971, missing=1361, range -0.29–0.43, mean 0.04166 ± 0.1266 |
| B249.8_mass | target | numeric | *Not specified.* | n=1971, missing=1361, range -0.26–0.4, mean 0.04184 ± 0.1173 |
| Ca_mass | target | numeric | *Not specified.* | n=1971, missing=1293, range 0.959–36.54, mean 9.988 ± 5.97 |
| Cu_mass | target | numeric | *Not specified.* | n=1971, missing=1296, range 0–0.027, mean 0.006616 ± 0.003616 |
| Fe_mass | target | numeric | *Not specified.* | n=1971, missing=1294, range 0.01497–0.245, mean 0.06682 ± 0.03476 |
| K_mass | target | numeric | *Not specified.* | n=1971, missing=1293, range 1.058–27.05, mean 6.155 ± 3.057 |
| Mg_mass | target | numeric | *Not specified.* | n=1971, missing=1293, range 0.482–7.862, mean 2.193 ± 0.9503 |
| Mn_mass | target | numeric | *Not specified.* | n=1971, missing=1293, range 0–1.398, mean 0.2016 ± 0.2174 |
| Na_mass | target | numeric | *Not specified.* | n=1971, missing=1293, range 0–4.872, mean 0.7995 ± 0.6255 |
| P_mass | target | numeric | *Not specified.* | n=1971, missing=1293, range 0.2228–7.178, mean 1.553 ± 0.9141 |
| Zn_mass | target | numeric | *Not specified.* | n=1971, missing=1294, range 0.001424–0.37, mean 0.06444 ± 0.06999 |
| LMA | target | numeric | *Not specified.* | n=1971, missing=28, range 0.008442–0.4077, mean 0.07772 ± 0.05393 |
| EWT | target | numeric | *Not specified.* | n=1971, missing=42, range 0.03745–0.669, mean 0.1456 ± 0.0961 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=1971, missing=0, classes=1, top 33aec64d-bb0c-42c2-a5e2-bb733f8ce721 (×1971) |
| site | metadata | categorical | *Not specified.* | n=1971, missing=0, classes=41, top IdB_ile_ste_marg (×260) |
| location | metadata | categorical | *Not specified.* | n=1971, missing=1971, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=1971, missing=1971, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=1971, missing=0, range -34.81–48.81, mean 43.15 ± 14.74 |
| longitude | metadata | numeric | *Not specified.* | n=1971, missing=0, range -123.6–116.1, mean -72.01 ± 38.64 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=1971, missing=0, classes=1, top source-provided coordinates when available (×1971) |
| year | metadata | numeric | *Not specified.* | n=1971, missing=0, range 2022–2022, mean 2022 ± 0 |
| date | metadata | categorical | *Not specified.* | n=1971, missing=0, classes=130, top 2019-07-25 (×37) |
| plant_part | metadata | categorical | *Not specified.* | n=1971, missing=0, classes=1, top Leaf (×1971) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=1971, missing=0, classes=1, top leaf (×1971) |
| instrument | metadata | categorical | *Not specified.* | n=1971, missing=0, classes=1, top Spectra Vista Corporation HR-1024i (×1971) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=1971, missing=0, classes=1, top Contact (×1971) |
| signal_type | metadata | categorical | *Not specified.* | n=1971, missing=0, classes=1, top transmittance (×1971) |
| axis_unit | metadata | categorical | *Not specified.* | n=1971, missing=0, classes=1, top nm (×1971) |
| axis_min | metadata | numeric | *Not specified.* | n=1971, missing=0, range 400–400, mean 400 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=1971, missing=0, range 2400–2400, mean 2400 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=1971, missing=0, range 2001–2001, mean 2001 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=1971, missing=0, classes=1, top 10.1080/00103624.2016.1228952 \| 10.1101/2022.07.01.498461 \| 10.1111/1365-2745.13972 \| 10.21232/44vxHorW \| 10.21232/deP7jVyq \| 10.21232/dep7jvyq (×1971) |
| citation | metadata | categorical | *Not specified.* | n=1971, missing=0, classes=1, top Shan Kothari, Rosalie Beauchamp-Rioux, Florence Blanchard, Anna L. Crofts, Alize Girard, Xavier Guilbeault-Mayers, Paul W. Hacker, Juliana Pardo, Anna K. Schweiger, Sabrina Demers-Thibeault, Anne Bruneau, Nicholas C. Coops, Margaret Kalacska, Mark Vellend and Etienne Lalibert. 2022. CABO 2018-2019 Leaf-Level Spectra. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/44vxHorW (×1971) |
| license | metadata | categorical | *Not specified.* | n=1971, missing=0, classes=1, top Creative Commons Attribution (×1971) |
| rights_status | metadata | categorical | *Not specified.* | n=1971, missing=0, classes=1, top explicit_open (×1971) |
| usage_scope | metadata | categorical | *Not specified.* | n=1971, missing=0, classes=1, top public_reuse_possible (×1971) |
| notes | metadata | categorical | *Not specified.* | n=1971, missing=0, classes=1, top EcoSIS package cabo-2018-2019-leaf-level-spectra, no interpolation applied by project. (×1971) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/cabo-2018-2019-leaf-level-spectra`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Plant spectra as integrative measures of phenotypes — [10.1111/1365-2745.13972](https://doi.org/10.1111/1365-2745.13972)
- Predicting leaf traits across functional groups using reflectance spectroscopy — [10.1101/2022.07.01.498461](https://doi.org/10.1101/2022.07.01.498461)
- CABO 2018-2019 Leaf-Level Spectra — [10.21232/44vxHorW](https://doi.org/10.21232/44vxHorW)
- *Not specified.* — [10.1080/00103624.2016.1228952](https://doi.org/10.1080/00103624.2016.1228952)
- *Not specified.* — [10.21232/deP7jVyq](https://doi.org/10.21232/deP7jVyq)
- *Not specified.* — [10.21232/dep7jvyq](https://doi.org/10.21232/dep7jvyq)

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `1b63c49548a5fa5faba5ad2cdb7e145b24c0e9dfc75a1f6fc44dca40dc060560`
- **Processing hash:** `62fc66ee3b0ea82d250e073cdcc94b1b4fabd0a3422b17ae69bffad235d21cbb` | **metadata hash:** `92da201686bff26e0d7b7ecb0b1ce0a199e6cdf181384d629cfad1fd16481408`
