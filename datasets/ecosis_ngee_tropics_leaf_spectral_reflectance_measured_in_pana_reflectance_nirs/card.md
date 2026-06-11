# Datasheet — EcoSIS NGEE Tropics Leaf Spectral Reflectance Measured in Panama Collected February to April 2016 (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS NGEE Tropics Leaf Spectral Reflectance Measured in Panama Collected February to April 2016 (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** NGEE Tropics Leaf Spectral Reflectance Measured in Panama Collected February to April 2016

## Composition

- **Alignment:** observation level; 708 sample(s), 709 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–2 (mean 1.001).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | ngee-tropics_panama_2016_svc_feb_mar_apr_leaf_spectra.csv | Spectra Vista Corporation, Spectral Evolution HR-1024i | NIR | 350–2500 nm | 709 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| H20_pc | target | numeric | *Not specified.* | n=708, missing=124, range 29.3–82.44, mean 55.77 ± 7.224 |
| LMA_gDW_m2 | target | numeric | *Not specified.* | n=708, missing=124, range 22.01–204.9, mean 106.7 ± 30.86 |
| SLA_cm2_gDW | target | numeric | *Not specified.* | n=708, missing=124, range 48.8–454.4, mean 104.8 ± 45.67 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top 78a97d90-36b1-4e4b-9c93-7e2db590f154 (×708) |
| site | metadata | categorical | *Not specified.* | n=708, missing=0, classes=2, top PA-SLZ (×487) |
| location | metadata | categorical | *Not specified.* | n=708, missing=708, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=708, missing=708, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=708, missing=708, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=708, missing=708, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top source-provided coordinates when available (×708) |
| year | metadata | numeric | *Not specified.* | n=708, missing=0, range 2019–2019, mean 2019 ± 0 |
| date | metadata | categorical | *Not specified.* | n=708, missing=708, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=708, missing=708, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=708, missing=708, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=708, missing=708, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top Leaf (×708) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top leaf (×708) |
| instrument | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top Spectra Vista Corporation, Spectral Evolution HR-1024i (×708) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top Contact (×708) |
| signal_type | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top reflectance (×708) |
| axis_unit | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top nm (×708) |
| axis_min | metadata | numeric | *Not specified.* | n=708, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=708, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=708, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top 10.1111/nph.16029 \| 10.15486/ngt/1411867 \| 10.15486/ngt/1411971 \| 10.15486/ngt/1411972 \| 10.15486/ngt/1411973 \| 10.15486/ngt/1478523 \| 10.15486/ngt/1478647 \| 10.15486/ngt/1507766 (×708) |
| citation | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top Shawn Serbin Kim Ely Alistair Rogers Turin Dickman Matteo Detto Jin Wu Brett Wolfe Nate McDowell Charlotte Grossiord Sean Michaletz Adam Collins. 2019. NGEE Tropics Leaf Spectral Reflectance Measured in Panama Collected February to April 2016. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). http://dx.doi.org/10.15486/ngt/1478523 (×708) |
| license | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top Open Data Commons Attribution License (×708) |
| rights_status | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top explicit_open (×708) |
| usage_scope | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top public_reuse_possible (×708) |
| notes | metadata | categorical | *Not specified.* | n=708, missing=0, classes=1, top EcoSIS package ngee-tropics-leaf-spectral-reflectance-measured-in-panama-collected-february-to-april-2016, no interpolation applied by project. (×708) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/ngee-tropics-leaf-spectral-reflectance-measured-in-panama-collected-february-to-april-2016`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Leaf spectra, Feb2016-April2016, PA-SLZ, PA-PNM, PA-BCI: Panama — [10.15486/ngt/1478523](https://doi.org/10.15486/ngt/1478523)
- Leaf water potential, Feb2016-May2016, PA-SLZ, PA-PNM, PA-BCI: Panama — [10.15486/ngt/1507766](https://doi.org/10.15486/ngt/1507766)
- 2016 Panama ENSO Non-Structural Carbohydrates (NSC), Feb2016-May2016, PA-SLZ, PA-PNM, PA-BCI — [10.15486/ngt/1478647](https://doi.org/10.15486/ngt/1478647)
- CO2 response (ACi) gas exchange, calculated Vcmax & Jmax parameters, Feb2016-May2016, PA-SLZ, PA-PNM: Panama — [10.15486/ngt/1411867](https://doi.org/10.15486/ngt/1411867)
- Leaf mass area, Feb2016-May2016, PA-SLZ, PA-PNM, PA-BCI: Panama — [10.15486/ngt/1411973](https://doi.org/10.15486/ngt/1411973)
- Diurnal leaf gas exchange survey, Feb2016-May2016, PA-SLZ, PA-PNM: Panama — [10.15486/ngt/1411972](https://doi.org/10.15486/ngt/1411972)
- Leaf sample detail, Feb2016-May2016, PA-SLZ, PA-PNM, PA-BCI: Panama — [10.15486/ngt/1411971](https://doi.org/10.15486/ngt/1411971)
- Leaf reflectance spectroscopy captures variation in carboxylation capacity across species, canopy environment and leaf age in lowland moist tropical forests — [10.1111/nph.16029](https://doi.org/10.1111/nph.16029)

## Distribution

- **License:** ODC-By-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `97398aa5e2e8449c19f0d2a1c70f23e936c3b9d3b95e70c83fe3c9b4cfde1b74`
- **Processing hash:** `882ca1faad2e10923d2bad9662871454876a0feba7f57c03869de894912beece` | **metadata hash:** `9a30d8f5bc76011d9bde8a0a231928a4129ba190f0d6093d823e3dbbfe343287`
