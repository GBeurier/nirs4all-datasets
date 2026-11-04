# Datasheet — EcoSIS seasonal canopy spectra and traits, Blackhawk Island, WI

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS seasonal canopy spectra and traits, Blackhawk Island, WI. Origin database composed from 3 standardized v2.0 leaves: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Seasonal canopy spectra and traits, Blackhawk Island, WI

## Composition

- **Alignment:** sample level; 80 sample(s), 80 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | bhi2018_plot_spectra | *Not specified.* | NIR | 407.1–2389 nm | 80 | 187 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| lignin | target | numeric | *Not specified.* | n=80, missing=0, range 2.445–23.22, mean 12.31 ± 4.621 |
| lma_g_m2 | target | numeric | *Not specified.* | n=80, missing=0, range 38.37–147.7, mean 89.44 ± 20.55 |
| nitrogen | target | numeric | *Not specified.* | n=80, missing=0, range 0.6096–4.69, mean 2.281 ± 0.7039 |
| SpectralRep | metadata | numeric | *Not specified.* | n=80, missing=0, range 1–1, mean 1 ± 0 |
| plot_id | metadata | categorical | *Not specified.* | n=80, missing=0, classes=80, top bhi2018_p002 (×1) |
| plot_num | metadata | numeric | *Not specified.* | n=80, missing=0, range 2–235, mean 80.3 ± 68.39 |
| sample_date | metadata | categorical | *Not specified.* | n=80, missing=0, classes=29, top 20180518 (×5) |
| dbh_m | metadata | numeric | *Not specified.* | n=80, missing=2, range 0.319–1.168, mean 0.6181 ± 0.1707 |
| image_date | metadata | categorical | *Not specified.* | n=80, missing=0, classes=8, top 20180604 (×11) |
| calcium | metadata | numeric | *Not specified.* | n=80, missing=0, range 0.02536–3.262, mean 0.9321 ± 0.6781 |
| phosphorus | metadata | numeric | *Not specified.* | n=80, missing=0, range 0.07227–0.4436, mean 0.1865 ± 0.06907 |
| potassium | metadata | numeric | *Not specified.* | n=80, missing=0, range 0.004003–2.337, mean 0.8451 ± 0.4847 |
| tot_phenolics | metadata | numeric | *Not specified.* | n=80, missing=0, range 2.456–20.29, mean 8.803 ± 4.742 |
| chl_a_mmol_m2 | metadata | numeric | *Not specified.* | n=80, missing=0, range 24.19–556.2, mean 340 ± 134.1 |
| genus | metadata | categorical | *Not specified.* | n=80, missing=0, classes=7, top Quercus (×26) |
| species | metadata | categorical | *Not specified.* | n=80, missing=0, classes=10, top rubra (×14) |
| usda_code | metadata | categorical | *Not specified.* | n=80, missing=0, classes=10, top QURU (×14) |
| common_name | metadata | categorical | *Not specified.* | n=80, missing=0, classes=10, top Red oak (×14) |
| veg_type | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top tree (×80) |
| latitude | metadata | numeric | *Not specified.* | n=80, missing=0, range 43.65–43.65, mean 43.65 ± 0.002262 |
| longitude | metadata | numeric | *Not specified.* | n=80, missing=0, range -89.8–-89.79, mean -89.79 ± 0.002561 |
| dataset | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top EcoSIS (×80) |
| n_points_original | metadata | numeric | *Not specified.* | n=80, missing=0, range 187–187, mean 187 ± 0 |
| dimensions | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top 1D (×80) |
| axis_note | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top wavelengths_as_provided_by_EcoSIS_resource (×80) |
| official_data_url | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top https://data.ecosis.org/dataset/seasonal-canopy-spectra-and-traits--blackhawk-island--wi (×80) |
| official_package_url | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top https://ecosis.org/package/seasonal-canopy-spectra-and-traits--blackhawk-island--wi (×80) |
| license | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top Open Data Commons Public Domain Dedication and License (PDDL) (×80) |
| license_url | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top http://www.opendefinition.org/licenses/odc-pddl (×80) |
| rights_status | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top explicit_open (×80) |
| usage_scope | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top public_reuse_possible (×80) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top True (×80) |
| notes | metadata | categorical | *Not specified.* | n=80, missing=0, classes=1, top Task-specific EcoSIS target not present in active parent Y table, wavelengths kept as provided by EcoSIS resource, no project interpolation. (×80) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/seasonal-canopy-spectra-and-traits--blackhawk-island--wi`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/api/3/action/package_show?id=seasonal-canopy-spectra-and-traits--blackhawk-island--wi`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://ecosis.org/package/seasonal-canopy-spectra-and-traits--blackhawk-island--wi`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 9 fields, Y: 3 fields, passport: 21 fields, measurements: 6 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** PDDL-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN API package_show verified open license: Open Data Commons Public Domain Dedication and License (PDDL).
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `6c9d539ae0268e0f5d06fd3bf516d9a9c60f42599bb6d00dfe46260a21935e0b`
- **Processing hash:** `009752c2f643d8ef423b83e24cfd8ac78eb49c5cbcd3a45f68a07a8dda853420` | **metadata hash:** `3092d4247ce32cdeba8cc816104cbd11dabb909fbb91c51e6a412ff2b7931c9b`
