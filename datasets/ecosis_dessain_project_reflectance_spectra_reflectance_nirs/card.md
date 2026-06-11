# Datasheet — EcoSIS Dessain project reflectance spectra (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Dessain project reflectance spectra (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 31 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Dessain project reflectance spectra

## Composition

- **Alignment:** observation level; 200 sample(s), 200 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Dessain_spectra.csv | Analytical Spectral Devices Field Spec 4 | NIR | 400–2400 nm | 200 | 2001 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| species | target | categorical | *Not specified.* | n=200, missing=0, classes=93, top Betula alleghaniensis Britton (×6) |
| latin.genus | target | categorical | *Not specified.* | n=200, missing=0, classes=59, top Acer (×30) |
| latin.species | target | categorical | *Not specified.* | n=200, missing=0, classes=82, top americana (×9) |
| growth.form | target | categorical | *Not specified.* | n=200, missing=0, classes=4, top tree (×107) |
| family | target | categorical | *Not specified.* | n=200, missing=3, classes=37, top Sapindaceae (×30) |
| genus | target | categorical | *Not specified.* | n=200, missing=3, classes=57, top Acer (×30) |
| SLA | target | numeric | *Not specified.* | n=200, missing=0, range 9.425–46.95, mean 19.68 ± 7.375 |
| LMA | target | numeric | *Not specified.* | n=200, missing=0, range 0.0213–0.1061, mean 0.05733 ± 0.01897 |
| LDMC | target | numeric | *Not specified.* | n=200, missing=0, range 125.2–496.2, mean 328.8 ± 81.29 |
| EWT | target | numeric | *Not specified.* | n=200, missing=0, range 0.05613–0.4542, mean 0.1206 ± 0.051 |
| Cmass | target | numeric | *Not specified.* | n=200, missing=2, range 39.08–53.6, mean 46.45 ± 2.124 |
| Nmass | target | numeric | *Not specified.* | n=200, missing=2, range 1.49–5.777, mean 2.786 ± 0.7991 |
| solubles | target | numeric | *Not specified.* | n=200, missing=6, range 38.53–86.26, mean 70.71 ± 10.12 |
| hemicellulose | target | numeric | *Not specified.* | n=200, missing=6, range 3.138–33.89, mean 10.66 ± 5.758 |
| cellulose | target | numeric | *Not specified.* | n=200, missing=2, range 5.589–24.98, mean 10.76 ± 3.634 |
| lignin | target | numeric | *Not specified.* | n=200, missing=2, range 1.145–22.61, mean 7.503 ± 4.014 |
| chlA | target | numeric | *Not specified.* | n=200, missing=75, range 1.846–15.5, mean 8.374 ± 2.844 |
| chlB | target | numeric | *Not specified.* | n=200, missing=75, range 0.4658–5.293, mean 2.861 ± 1.014 |
| car | target | numeric | *Not specified.* | n=200, missing=75, range 0.4985–3.34, mean 1.731 ± 0.5503 |
| Al_mass | target | numeric | *Not specified.* | n=200, missing=3, range 0.013–0.379, mean 0.08944 ± 0.06515 |
| B_mass | target | numeric | *Not specified.* | n=200, missing=2, range -0.103–0.357, mean 0.1146 ± 0.09385 |
| B.1_mass | target | numeric | *Not specified.* | n=200, missing=2, range -0.093–0.351, mean 0.1054 ± 0.08615 |
| Ca_mass | target | numeric | *Not specified.* | n=200, missing=2, range 1.639–51.48, mean 12.94 ± 7.72 |
| Cu_mass | target | numeric | *Not specified.* | n=200, missing=4, range 0.004–0.071, mean 0.01594 ± 0.01116 |
| Fe_mass | target | numeric | *Not specified.* | n=200, missing=4, range 0.017–0.262, mean 0.09639 ± 0.04865 |
| K_mass | target | numeric | *Not specified.* | n=200, missing=3, range 3.402–43.52, mean 12.83 ± 8.193 |
| Mg_mass | target | numeric | *Not specified.* | n=200, missing=3, range 1.118–6.04, mean 2.828 ± 1.096 |
| Mn_mass | target | numeric | *Not specified.* | n=200, missing=2, range 0.005–3.741, mean 0.1794 ± 0.4219 |
| Na_mass | target | numeric | *Not specified.* | n=200, missing=3, range -0.121–5.405, mean 1.169 ± 0.8928 |
| P_mass | target | numeric | *Not specified.* | n=200, missing=2, range 0.962–6.105, mean 2.47 ± 1.076 |
| Zn_mass | target | numeric | *Not specified.* | n=200, missing=2, range 0.005–0.647, mean 0.06992 ± 0.1002 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=200, missing=0, classes=1, top 99529cc2-5cd8-4379-ba2f-c9d6e012566a (×200) |
| site | metadata | categorical | *Not specified.* | n=200, missing=0, classes=8, top ireqa (×48) |
| location | metadata | categorical | *Not specified.* | n=200, missing=200, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=200, missing=200, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=200, missing=0, range 45.12–45.99, mean 45.66 ± 0.2072 |
| longitude | metadata | numeric | *Not specified.* | n=200, missing=0, range -74.01–-72.65, mean -73.57 ± 0.3054 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=200, missing=0, classes=1, top source-provided coordinates when available (×200) |
| year | metadata | numeric | *Not specified.* | n=200, missing=0, range 2022–2022, mean 2022 ± 0 |
| date | metadata | categorical | *Not specified.* | n=200, missing=0, classes=17, top 8/16/2017 (×21) |
| plant_part | metadata | categorical | *Not specified.* | n=200, missing=0, classes=1, top Leaf (×200) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=200, missing=200, classes=0, — |
| instrument | metadata | categorical | *Not specified.* | n=200, missing=0, classes=1, top Analytical Spectral Devices Field Spec 4 (×200) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=200, missing=0, classes=1, top Contact (×200) |
| signal_type | metadata | categorical | *Not specified.* | n=200, missing=0, classes=1, top reflectance (×200) |
| axis_unit | metadata | categorical | *Not specified.* | n=200, missing=0, classes=1, top nm (×200) |
| axis_min | metadata | numeric | *Not specified.* | n=200, missing=0, range 400–400, mean 400 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=200, missing=0, range 2400–2400, mean 2400 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=200, missing=0, range 2001–2001, mean 2001 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=200, missing=0, classes=1, top 10.1080/00103624.2016.1228952 \| 10.1101/2022.07.01.498461 \| 10.21232/VYJzNBEy \| 10.21232/deP7jVyq \| 10.21232/dep7jvyq (×200) |
| citation | metadata | categorical | *Not specified.* | n=200, missing=0, classes=1, top Shan Kothari, Aurlie Dessain, Rosalie Beauchamp-Rioux, Florence Blanchard, Anna L. Crofts, Alize Girard, Xavier Guilbeault-Mayers, Paul W. Hacker, Juliana Pardo, Anna K. Schweiger, Sabrina Demers-Thibeault, Anne Bruneau, Nicholas C. Coops, Margaret Kalacska, Mark Vellend and Etienne Lalibert. 2022. Dessain project reflectance spectra. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/VYJzNBEy (×200) |
| license | metadata | categorical | *Not specified.* | n=200, missing=0, classes=1, top Creative Commons Attribution Share-Alike (×200) |
| rights_status | metadata | categorical | *Not specified.* | n=200, missing=0, classes=1, top explicit_open (×200) |
| usage_scope | metadata | categorical | *Not specified.* | n=200, missing=0, classes=1, top public_reuse_possible (×200) |
| notes | metadata | categorical | *Not specified.* | n=200, missing=0, classes=1, top EcoSIS package dessain-project-reflectance-spectra, no interpolation applied by project. (×200) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/dessain-project-reflectance-spectra`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- https://www.biorxiv.org/content/10.1101/2022.07.01.498461v2 — [10.1101/2022.07.01.498461](https://doi.org/10.1101/2022.07.01.498461)
- Dessain project reflectance spectra — [10.21232/VYJzNBEy](https://doi.org/10.21232/VYJzNBEy)
- *Not specified.* — [10.1080/00103624.2016.1228952](https://doi.org/10.1080/00103624.2016.1228952)
- *Not specified.* — [10.21232/deP7jVyq](https://doi.org/10.21232/deP7jVyq)
- *Not specified.* — [10.21232/dep7jvyq](https://doi.org/10.21232/dep7jvyq)

## Distribution

- **License:** CC-BY-SA-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `b492aa7092cfaf955817de788be44e958d6a000e6b4b67d0762c16ce3cf60984`
- **Processing hash:** `16db6194fcda60ce82e51175eee26d229a2a2a99547af11202e33d8fd870a8f2` | **metadata hash:** `9b026bb67f200bcfe675a16c6fd00fb53f0066f6e0ef5ad79c358b07b1d3c75c`
