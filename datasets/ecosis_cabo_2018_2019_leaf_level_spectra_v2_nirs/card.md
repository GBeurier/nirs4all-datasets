# Datasheet — CABO leaves 2018–2019 — reflectance + transmittance, v2

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS CABO 2018-2019 leaf-level spectra v2, reflectance and transmittance. Origin database composed from 2 standardized v2.0 leaves: 2 spectral source(s), 51 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** CABO 2018-2019 Leaf-Level Spectra v2

## Composition

- **Alignment:** sample level; 1971 sample(s), 3942 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X_reflectance | ref_spec.csv | Spectra Vista Corporation HR-1024i | NIR | 400–2400 nm | 1971 | 2001 |
| X_transmittance | trans_spec.csv | Spectra Vista Corporation HR-1024i | NIR | 400–2400 nm | 1971 | 2001 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| species | target | categorical | *Not specified.* | n=3942, missing=0, classes=106, top Populus tremuloides Michaux (×240) |
| latin.genus | target | categorical | *Not specified.* | n=3942, missing=0, classes=66, top Acer (×530) |
| latin.species | target | categorical | *Not specified.* | n=3942, missing=0, classes=93, top tremuloides (×240) |
| plant.id | target | categorical | *Not specified.* | n=3942, missing=2, classes=1738, top 8554325 (×14) |
| growth.form | target | categorical | *Not specified.* | n=3942, missing=0, classes=4, top tree (×2248) |
| family | target | categorical | *Not specified.* | n=3942, missing=0, classes=31, top Sapindaceae (×536) |
| genus | target | categorical | *Not specified.* | n=3942, missing=0, classes=66, top Acer (×530) |
| functional.group | target | categorical | *Not specified.* | n=3942, missing=0, classes=7, top broadleaf (×1992) |
| LMA | target | numeric | *Not specified.* | n=3942, missing=56, range 0.008442–0.4077, mean 0.07772 ± 0.05392 |
| LDMC | target | numeric | *Not specified.* | n=3942, missing=82, range 35.81–573, mean 353.7 ± 92.38 |
| EWT | target | numeric | *Not specified.* | n=3942, missing=84, range 0.03229–0.5179, mean 0.1241 ± 0.07782 |
| Cmass | target | numeric | *Not specified.* | n=3942, missing=16, range 36.72–56.95, mean 46.92 ± 2.708 |
| Nmass | target | numeric | *Not specified.* | n=3942, missing=16, range 0.7948–5.953, mean 2.257 ± 0.7087 |
| solubles_mass | target | numeric | *Not specified.* | n=3942, missing=104, range 23.68–88.95, mean 63.9 ± 12.84 |
| hemicellulose_mass | target | numeric | *Not specified.* | n=3942, missing=112, range 2.229–42.93, mean 14.15 ± 7.953 |
| cellulose_mass | target | numeric | *Not specified.* | n=3942, missing=50, range 5.19–34.32, mean 13.95 ± 6.583 |
| lignin_mass | target | numeric | *Not specified.* | n=3942, missing=50, range 0.5314–23.44, mean 7.68 ± 4.236 |
| chlA_mass | target | numeric | *Not specified.* | n=3942, missing=60, range 1.242–28.57, mean 7.26 ± 3.697 |
| chlB_mass | target | numeric | *Not specified.* | n=3942, missing=60, range 0.388–10.82, mean 2.434 ± 1.27 |
| car_mass | target | numeric | *Not specified.* | n=3942, missing=60, range 0.193–5.297, mean 1.554 ± 0.7151 |
| Al_mass | target | numeric | *Not specified.* | n=3942, missing=2588, range 0–0.332, mean 0.04917 ± 0.03903 |
| B208.9_mass | target | numeric | *Not specified.* | n=3942, missing=2722, range -0.29–0.43, mean 0.04166 ± 0.1266 |
| B249.8_mass | target | numeric | *Not specified.* | n=3942, missing=2722, range -0.26–0.4, mean 0.04184 ± 0.1173 |
| Ca_mass | target | numeric | *Not specified.* | n=3942, missing=2586, range 0.959–36.54, mean 9.988 ± 5.968 |
| Cu_mass | target | numeric | *Not specified.* | n=3942, missing=2592, range 0–0.027, mean 0.006616 ± 0.003614 |
| Fe_mass | target | numeric | *Not specified.* | n=3942, missing=2588, range 0.01497–0.245, mean 0.06682 ± 0.03475 |
| K_mass | target | numeric | *Not specified.* | n=3942, missing=2586, range 1.058–27.05, mean 6.155 ± 3.056 |
| Mg_mass | target | numeric | *Not specified.* | n=3942, missing=2586, range 0.482–7.862, mean 2.193 ± 0.9499 |
| Mn_mass | target | numeric | *Not specified.* | n=3942, missing=2586, range 0–1.398, mean 0.2016 ± 0.2173 |
| Na_mass | target | numeric | *Not specified.* | n=3942, missing=2586, range 0–4.872, mean 0.7995 ± 0.6253 |
| P_mass | target | numeric | *Not specified.* | n=3942, missing=2586, range 0.2228–7.178, mean 1.553 ± 0.9138 |
| Zn_mass | target | numeric | *Not specified.* | n=3942, missing=2588, range 0.001424–0.37, mean 0.06444 ± 0.06996 |
| Narea | target | numeric | *Not specified.* | n=3942, missing=2005, range 3.194e-05–0.0005152, mean 0.0001542 ± 6.173e-05 |
| Carea | target | numeric | *Not specified.* | n=3942, missing=2005, range 0.0003681–0.02103, mean 0.003718 ± 0.002776 |
| solubles_area | target | numeric | *Not specified.* | n=3942, missing=2049, range 0.0005307–0.02528, mean 0.004988 ± 0.003543 |
| hemicellulose_area | target | numeric | *Not specified.* | n=3942, missing=2053, range 7.847e-05–0.005191, mean 0.001048 ± 0.0008274 |
| cellulose_area | target | numeric | *Not specified.* | n=3942, missing=2022, range 0.00012–0.007309, mean 0.001102 ± 0.001026 |
| lignin_area | target | numeric | *Not specified.* | n=3942, missing=2022, range 2.12e-05–0.004556, mean 0.0006518 ± 0.000698 |
| chlA_area | target | numeric | *Not specified.* | n=3942, missing=2027, range 8.885e-06–0.0002939, mean 4.685e-05 ± 2.367e-05 |
| chlB_area | target | numeric | *Not specified.* | n=3942, missing=2027, range 2.971e-06–9.463e-05, mean 1.562e-05 ± 7.601e-06 |
| car_area | target | numeric | *Not specified.* | n=3942, missing=2027, range 2.482e-06–5.86e-05, mean 1.005e-05 ± 4.7e-06 |
| Al_area | target | numeric | *Not specified.* | n=3942, missing=3278, range 0–4.327e-06, mean 4.052e-07 ± 3.874e-07 |
| Ca_area | target | numeric | *Not specified.* | n=3942, missing=3277, range 1.26e-05–0.0003779, mean 7.941e-05 ± 5.325e-05 |
| Cu_area | target | numeric | *Not specified.* | n=3942, missing=3280, range 0–2.611e-07, mean 4.908e-08 ± 2.668e-08 |
| Fe_area | target | numeric | *Not specified.* | n=3942, missing=3278, range 1.799e-07–2.787e-06, mean 5.063e-07 ± 2.551e-07 |
| K_area | target | numeric | *Not specified.* | n=3942, missing=3277, range 1.482e-05–0.0002228, mean 4.735e-05 ± 2.391e-05 |
| Mg_area | target | numeric | *Not specified.* | n=3942, missing=3277, range 3.179e-06–8.179e-05, mean 1.761e-05 ± 9.907e-06 |
| Mn_area | target | numeric | *Not specified.* | n=3942, missing=3277, range 0–1.62e-05, mean 1.783e-06 ± 2.501e-06 |
| Na_area | target | numeric | *Not specified.* | n=3942, missing=3277, range 0–6.958e-05, mean 8.037e-06 ± 1.022e-05 |
| P_area | target | numeric | *Not specified.* | n=3942, missing=3277, range 3.089e-06–7.277e-05, mean 1.217e-05 ± 7.683e-06 |
| Zn_area | target | numeric | *Not specified.* | n=3942, missing=3278, range 2.297e-08–2.89e-06, mean 4.988e-07 ± 5.733e-07 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=3942, missing=0, classes=2, top a8f5093c-4383-40ad-85ae-4ad0d7a22eff (×1971) |
| site | metadata | categorical | *Not specified.* | n=3942, missing=0, classes=47, top IdB_ile_ste_marg (×520) |
| latitude | metadata | numeric | *Not specified.* | n=3942, missing=0, range -34.81–48.81, mean 43.16 ± 14.74 |
| longitude | metadata | numeric | *Not specified.* | n=3942, missing=0, range -123.7–116.1, mean -71.93 ± 38.64 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=3942, missing=0, classes=1, top source-provided coordinates when available (×3942) |
| year | metadata | numeric | *Not specified.* | n=3942, missing=0, range 2022–2022, mean 2022 ± 0 |
| date | metadata | categorical | *Not specified.* | n=3942, missing=0, classes=130, top 2019-07-25 (×74) |
| plant_part | metadata | categorical | *Not specified.* | n=3942, missing=0, classes=1, top Leaf (×3942) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=3942, missing=0, classes=1, top leaf (×3942) |
| instrument | metadata | categorical | *Not specified.* | n=3942, missing=0, classes=1, top Spectra Vista Corporation HR-1024i (×3942) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=3942, missing=0, classes=1, top Contact (×3942) |
| signal_type | metadata | categorical | *Not specified.* | n=3942, missing=0, classes=2, top absorbance (×1971) |
| axis_unit | metadata | categorical | *Not specified.* | n=3942, missing=0, classes=1, top nm (×3942) |
| axis_min | metadata | numeric | *Not specified.* | n=3942, missing=0, range 400–400, mean 400 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=3942, missing=0, range 2400–2400, mean 2400 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=3942, missing=0, range 2001–2001, mean 2001 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=3942, missing=0, classes=1, top 10.1016/j.rse.2023.113926 \| 10.1080/00103624.2016.1228952 \| 10.1111/1365-2745.13972 \| 10.1111/nph.18713 \| 10.1186/s13007-021-00816-4 \| 10.17504/protocols.io.q26g7rn23vwz/v2 \| 10.21232/44vxHorW \| 10.21232/44vxhorw \| 10.21232/58kApoRy \| 10.21232/deP7jVyq \| 10.21232/dep7jvyq \| 10.5281/zenodo.10735410 \| 10.5683/SP3/NYABAG (×3942) |
| citation | metadata | categorical | *Not specified.* | n=3942, missing=0, classes=1, top Shan Kothari, Rosalie Beauchamp-Rioux, Florence Blanchard, Anna L. Crofts, Alize Girard, Xavier Guilbeault-Mayers, Paul W. Hacker, Juliana Pardo, Anna K. Schweiger, Sabrina Demers-Thibeault, Anne Bruneau, Nicholas C. Coops, Margaret Kalacska, Mark Vellend and Etienne Lalibert. 2022. CABO 2018-2019 Leaf-Level Spectra v2. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/58kApoRy (×3942) |
| license | metadata | categorical | *Not specified.* | n=3942, missing=0, classes=1, top Creative Commons Attribution (×3942) |
| rights_status | metadata | categorical | *Not specified.* | n=3942, missing=0, classes=1, top explicit_open (×3942) |
| usage_scope | metadata | categorical | *Not specified.* | n=3942, missing=0, classes=1, top public_reuse_possible (×3942) |
| notes | metadata | categorical | *Not specified.* | n=3942, missing=0, classes=1, top EcoSIS package cabo-2018-2019-leaf-level-spectra-v2, no interpolation applied by project. (×3942) |
| source_sample_id | metadata | categorical | *Not specified.* | n=3942, missing=0, classes=1971, top 8133311 (×2) |
| source_measurement.date | metadata | categorical | *Not specified.* | n=3942, missing=0, classes=130, top 2019-07-25 (×74) |
| source_project | metadata | categorical | *Not specified.* | n=3942, missing=0, classes=11, top 2018-BeauchampRioux-MSc-UdeM (×872) |
| source_site | metadata | categorical | *Not specified.* | n=3942, missing=0, classes=47, top IdB_ile_ste_marg (×520) |
| source_stage | metadata | categorical | *Not specified.* | n=3942, missing=0, classes=8, top NA (×3806) |
| source_latitude | metadata | numeric | *Not specified.* | n=3942, missing=0, range -34.81–48.81, mean 43.16 ± 14.74 |
| source_longitude | metadata | numeric | *Not specified.* | n=3942, missing=0, range -123.7–116.1, mean -71.93 ± 38.64 |
| source_order | metadata | categorical | *Not specified.* | n=3942, missing=1971, classes=22, top Poales (×359) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/cabo-2018-2019-leaf-level-spectra-v2`
- Zenodo — kind `zenodo`, access `open`, license *Not specified.*: `10.5281/zenodo.10735410`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 7 fields, Y: 49 fields, measurements: 0 fields, passport: 24 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Plant spectra as integrative measures of phenotypes — [10.1111/1365-2745.13972](https://doi.org/10.1111/1365-2745.13972)
- Predicting leaf traits across functional groups using reflectance spectroscopy — [10.1111/nph.18713](https://doi.org/10.1111/nph.18713)
- Models for Predicting leaf traits across functional groups using reflectance spectroscopy — [10.5683/SP3/NYABAG](https://doi.org/10.5683/SP3/NYABAG)
- CABO 2018-2019 Leaf-Level Spectra v2 — [10.21232/58kApoRy](https://doi.org/10.21232/58kApoRy)
- *Not specified.* — [10.1016/j.rse.2023.113926](https://doi.org/10.1016/j.rse.2023.113926)
- *Not specified.* — [10.1080/00103624.2016.1228952](https://doi.org/10.1080/00103624.2016.1228952)
- *Not specified.* — [10.1186/s13007-021-00816-4](https://doi.org/10.1186/s13007-021-00816-4)
- *Not specified.* — [10.17504/protocols.io.q26g7rn23vwz/v2](https://doi.org/10.17504/protocols.io.q26g7rn23vwz/v2)
- *Not specified.* — [10.21232/44vxHorW](https://doi.org/10.21232/44vxHorW)
- *Not specified.* — [10.21232/44vxhorw](https://doi.org/10.21232/44vxhorw)
- *Not specified.* — [10.21232/deP7jVyq](https://doi.org/10.21232/deP7jVyq)
- *Not specified.* — [10.21232/dep7jvyq](https://doi.org/10.21232/dep7jvyq)

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `3dd80877f78b08f75e369e6c76e9237937ddeca1a2877760af90fa9d8df566eb`
- **Processing hash:** `82cf51508ec0f8fe3e4e90a23a85dcd3e31549ee4cee49b4e576cdc43a15611f` | **metadata hash:** `4d48a5c9c1c52afb886bcc62a16af6692c2ee668425f60897a2f5e70177d79e8`
