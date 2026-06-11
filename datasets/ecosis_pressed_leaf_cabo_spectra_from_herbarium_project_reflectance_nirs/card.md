# Datasheet — EcoSIS Pressed-leaf CABO spectra from herbarium project (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Pressed-leaf CABO spectra from herbarium project (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 50 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Pressed-leaf CABO spectra from herbarium project

## Composition

- **Alignment:** observation level; 614 sample(s), 614 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | pressed_spec_avg.csv | Spectral Evolution PSR+ 3500 | NIR | 400–2400 nm | 614 | 2001 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Species | target | categorical | *Not specified.* | n=614, missing=0, classes=70, top Populus tremuloides Michaux (×102) |
| LatinGenus | target | categorical | *Not specified.* | n=614, missing=0, classes=46, top Acer (×137) |
| LatinSpecies | target | categorical | *Not specified.* | n=614, missing=0, classes=65, top tremuloides (×102) |
| Discoloration | target | numeric | *Not specified.* | n=614, missing=0, range 0–4, mean 0.5212 ± 0.821 |
| GrowthForm | target | categorical | *Not specified.* | n=614, missing=0, classes=4, top broadleaf (×503) |
| SLA | target | numeric | *Not specified.* | n=614, missing=5, range 4.589–42.75, mean 15.11 ± 5.394 |
| LDMC | target | numeric | *Not specified.* | n=614, missing=7, range 154.8–573, mean 402.7 ± 65.43 |
| LMA | target | numeric | *Not specified.* | n=614, missing=5, range 0.02339–0.2179, mean 0.07694 ± 0.03657 |
| EWT | target | numeric | *Not specified.* | n=614, missing=7, range 0.04878–0.2815, mean 0.1111 ± 0.03633 |
| N | target | numeric | *Not specified.* | n=614, missing=0, range 0.8833–5.618, mean 2.127 ± 0.5908 |
| C | target | numeric | *Not specified.* | n=614, missing=0, range 39.54–53.6, mean 48.12 ± 2.178 |
| NDF | target | numeric | *Not specified.* | n=614, missing=8, range 11.05–61.47, mean 29.93 ± 8.119 |
| ADF | target | numeric | *Not specified.* | n=614, missing=12, range 7.972–34.66, mean 19.41 ± 4.415 |
| ADL | target | numeric | *Not specified.* | n=614, missing=12, range 1.145–21.8, mean 9.024 ± 3.446 |
| solubles | target | numeric | *Not specified.* | n=614, missing=8, range 38.53–88.95, mean 70.07 ± 8.12 |
| hemicellulose | target | numeric | *Not specified.* | n=614, missing=12, range 2.773–34.1, mean 10.56 ± 4.842 |
| cellulose | target | numeric | *Not specified.* | n=614, missing=12, range 5.19–25.77, mean 10.39 ± 3.135 |
| lignin | target | numeric | *Not specified.* | n=614, missing=12, range 0.918–21.47, mean 8.707 ± 3.406 |
| chlA | target | numeric | *Not specified.* | n=614, missing=50, range 1.242–15.5, mean 6.005 ± 2.195 |
| chlB | target | numeric | *Not specified.* | n=614, missing=50, range 0.486–5.293, mean 2.04 ± 0.7653 |
| car | target | numeric | *Not specified.* | n=614, missing=50, range 0.193–3.048, mean 1.252 ± 0.4386 |
| Al | target | numeric | *Not specified.* | n=614, missing=1, range 0–0.379, mean 0.05692 ± 0.04645 |
| Ca | target | numeric | *Not specified.* | n=614, missing=0, range 1.639–36.54, mean 11.37 ± 6.064 |
| Cu | target | numeric | *Not specified.* | n=614, missing=1, range 0–0.052, mean 0.007868 ± 0.005912 |
| Fe | target | numeric | *Not specified.* | n=614, missing=1, range 0.01497–0.266, mean 0.07628 ± 0.04005 |
| K | target | numeric | *Not specified.* | n=614, missing=1, range 1.058–38.15, mean 7.146 ± 4.586 |
| Mg | target | numeric | *Not specified.* | n=614, missing=0, range 0.482–7.862, mean 2.499 ± 0.9286 |
| Mn | target | numeric | *Not specified.* | n=614, missing=0, range 0–1.023, mean 0.1728 ± 0.1898 |
| Na | target | numeric | *Not specified.* | n=614, missing=1, range 0–4.872, mean 0.8547 ± 0.7056 |
| P | target | numeric | *Not specified.* | n=614, missing=0, range 0.2228–7.178, mean 1.762 ± 1.026 |
| Zn | target | numeric | *Not specified.* | n=614, missing=0, range 0.001424–0.647, mean 0.07194 ± 0.08375 |
| N_area | target | numeric | *Not specified.* | n=614, missing=5, range 5.15e-05–0.0002801, mean 0.0001512 ± 4.332e-05 |
| C_area | target | numeric | *Not specified.* | n=614, missing=5, range 0.00109–0.01102, mean 0.003742 ± 0.001927 |
| solubles_area | target | numeric | *Not specified.* | n=614, missing=13, range 0.001542–0.01589, mean 0.005396 ± 0.002615 |
| hemicellulose_area | target | numeric | *Not specified.* | n=614, missing=17, range 0.000118–0.002964, mean 0.0007992 ± 0.000473 |
| cellulose_area | target | numeric | *Not specified.* | n=614, missing=17, range 0.000199–0.002419, mean 0.0008014 ± 0.0004317 |
| lignin_area | target | numeric | *Not specified.* | n=614, missing=17, range 5.55e-05–0.002528, mean 0.0007072 ± 0.0005209 |
| chlA_area | target | numeric | *Not specified.* | n=614, missing=54, range 1.2e-05–0.0001246, mean 4.222e-05 ± 1.205e-05 |
| chlB_area | target | numeric | *Not specified.* | n=614, missing=54, range 3.99e-06–4.26e-05, mean 1.436e-05 ± 4.141e-06 |
| car_area | target | numeric | *Not specified.* | n=614, missing=54, range 2.92e-06–2.45e-05, mean 8.743e-06 ± 2.373e-06 |
| Al_area | target | numeric | *Not specified.* | n=614, missing=6, range 0–4.04e-06, mean 4.043e-07 ± 3.454e-07 |
| Ca_area | target | numeric | *Not specified.* | n=614, missing=5, range 3.83e-06–0.0003779, mean 8.511e-05 ± 5.545e-05 |
| Cu_area | target | numeric | *Not specified.* | n=614, missing=6, range 0–4.37e-07, mean 5.137e-08 ± 3.488e-08 |
| Fe_area | target | numeric | *Not specified.* | n=614, missing=6, range 1.46e-07–1.71e-06, mean 5.221e-07 ± 2.454e-07 |
| K_area | target | numeric | *Not specified.* | n=614, missing=6, range 1.48e-05–0.0002228, mean 4.868e-05 ± 2.603e-05 |
| Mg_area | target | numeric | *Not specified.* | n=614, missing=5, range 3.82e-06–8.18e-05, mean 1.866e-05 ± 1.008e-05 |
| Mn_area | target | numeric | *Not specified.* | n=614, missing=5, range 0–1.62e-05, mean 1.316e-06 ± 1.783e-06 |
| Na_area | target | numeric | *Not specified.* | n=614, missing=6, range 0–6.96e-05, mean 7.811e-06 ± 1.058e-05 |
| P_area | target | numeric | *Not specified.* | n=614, missing=5, range 3.09e-06–7.28e-05, mean 1.255e-05 ± 8.178e-06 |
| Zn_area | target | numeric | *Not specified.* | n=614, missing=5, range 2.3e-08–5.23e-06, mean 5.099e-07 ± 6.304e-07 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=614, missing=0, classes=1, top 263f1dcd-3790-4383-9c5d-ec1623d83eb4 (×614) |
| site | metadata | categorical | *Not specified.* | n=614, missing=614, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=614, missing=614, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=614, missing=614, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=614, missing=0, range -34.81–45.99, mean 36.84 ± 25.04 |
| longitude | metadata | numeric | *Not specified.* | n=614, missing=0, range -75.52–116.1, mean -53.13 ± 59.22 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=614, missing=0, classes=1, top source-provided coordinates when available (×614) |
| year | metadata | numeric | *Not specified.* | n=614, missing=0, range 2022–2022, mean 2022 ± 0 |
| date | metadata | categorical | *Not specified.* | n=614, missing=614, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=614, missing=0, classes=70, top Populus tremuloides Michaux (×102) |
| genus | metadata | categorical | *Not specified.* | n=614, missing=614, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=614, missing=614, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=614, missing=0, classes=1, top Leaf (×614) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=614, missing=0, classes=1, top leaf (×614) |
| instrument | metadata | categorical | *Not specified.* | n=614, missing=0, classes=1, top Spectral Evolution PSR+ 3500 (×614) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=614, missing=0, classes=1, top Contact (×614) |
| signal_type | metadata | categorical | *Not specified.* | n=614, missing=0, classes=1, top reflectance (×614) |
| axis_unit | metadata | categorical | *Not specified.* | n=614, missing=0, classes=1, top nm (×614) |
| axis_min | metadata | numeric | *Not specified.* | n=614, missing=0, range 400–400, mean 400 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=614, missing=0, range 2400–2400, mean 2400 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=614, missing=0, range 2001–2001, mean 2001 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=614, missing=0, classes=1, top 10.1101/2021.04.21.440856v5.full \| 10.21232/KS7MbtCK (×614) |
| citation | metadata | categorical | *Not specified.* | n=614, missing=0, classes=1, top Shan Kothari, Rosalie Beauchamp-Rioux, Etienne Lalibert and Jeannine Cavender-Bares. 2022. Pressed-leaf CABO spectra from herbarium project. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/KS7MbtCK (×614) |
| license | metadata | categorical | *Not specified.* | n=614, missing=0, classes=1, top Creative Commons Attribution Share-Alike (×614) |
| rights_status | metadata | categorical | *Not specified.* | n=614, missing=0, classes=1, top explicit_open (×614) |
| usage_scope | metadata | categorical | *Not specified.* | n=614, missing=0, classes=1, top public_reuse_possible (×614) |
| notes | metadata | categorical | *Not specified.* | n=614, missing=0, classes=1, top EcoSIS package pressed-leaf-cabo-spectra-from-herbarium-project, no interpolation applied by project. (×614) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/pressed-leaf-cabo-spectra-from-herbarium-project`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Reflectance spectroscopy allows rapid, accurate, and non-destructive estimates of functional traits from pressed leaves — [10.1101/2021.04.21.440856v5.full](https://doi.org/10.1101/2021.04.21.440856v5.full)
- Pressed-leaf CABO spectra from herbarium project — [10.21232/KS7MbtCK](https://doi.org/10.21232/KS7MbtCK)

## Distribution

- **License:** CC-BY-SA-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `c1f91c2ce0ab141a5183ea3dedc4c45730f4645f05656ed6ac43145cd4797265`
- **Processing hash:** `689a4ec32795c716202648fa10a205cbfb9abfc353bc102e1a4c887774df1f5a` | **metadata hash:** `2fd85ef2889a837527b29dbf805c47c25800a52e56e7f0164dabf684f73dbc2f`
