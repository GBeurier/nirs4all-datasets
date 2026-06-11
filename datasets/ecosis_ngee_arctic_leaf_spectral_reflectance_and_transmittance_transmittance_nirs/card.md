# Datasheet — EcoSIS NGEE Arctic Leaf Spectral Reflectance and Transmittance Data 2014 to 2016 Utqiagvik (Barrow) Alaska (transmittance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS NGEE Arctic Leaf Spectral Reflectance and Transmittance Data 2014 to 2016 Utqiagvik (Barrow) Alaska (transmittance). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** NGEE Arctic Leaf Spectral Reflectance and Transmittance Data 2014 to 2016 Utqiagvik (Barrow) Alaska

## Composition

- **Alignment:** observation level; 31 sample(s), 31 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | NGEE-Arctic_Barrow_2015_SVCHR1024i_Leaf_Spectral_Transmittance.csv | Spectra Vista Corporation HR-1024i | NIR | 350–2500 nm | 31 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| USDA_Species_Code | target | categorical | *Not specified.* | n=31, missing=0, classes=4, top PEFR5 (×10) |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=31, missing=0, classes=1, top 4367a915-4354-4162-b97e-b8e99d9e17c1 (×31) |
| site | metadata | categorical | *Not specified.* | n=31, missing=0, classes=1, top Barrow (Utqiagvik) Environmental Observatory (×31) |
| location | metadata | categorical | *Not specified.* | n=31, missing=31, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=31, missing=31, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=31, missing=31, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=31, missing=31, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=31, missing=0, classes=1, top source-provided coordinates when available (×31) |
| year | metadata | numeric | *Not specified.* | n=31, missing=0, range 2019–2019, mean 2019 ± 0 |
| date | metadata | categorical | *Not specified.* | n=31, missing=0, classes=2, top 20150712 (×21) |
| species | metadata | categorical | *Not specified.* | n=31, missing=31, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=31, missing=31, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=31, missing=31, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=31, missing=0, classes=1, top Leaf (×31) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=31, missing=0, classes=1, top leaf (×31) |
| instrument | metadata | categorical | *Not specified.* | n=31, missing=0, classes=1, top Spectra Vista Corporation HR-1024i (×31) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=31, missing=0, classes=1, top Contact (×31) |
| signal_type | metadata | categorical | *Not specified.* | n=31, missing=0, classes=1, top transmittance (×31) |
| axis_unit | metadata | categorical | *Not specified.* | n=31, missing=0, classes=1, top nm (×31) |
| axis_min | metadata | numeric | *Not specified.* | n=31, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=31, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=31, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=31, missing=0, classes=1, top 10.5440/1336809 \| 10.5440/1336812 \| 10.5440/1437044 \| 10.5440/1482338 (×31) |
| citation | metadata | categorical | *Not specified.* | n=31, missing=0, classes=1, top Shawn Serbin Wil Lieberman-Cribbin Kim Ely Alistair Rogers. 2019. NGEE Arctic Leaf Spectral Reflectance and Transmittance Data 2014 to 2016 Utqiagvik (Barrow) Alaska. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). https://doi.org/10.5440/1437044 (×31) |
| license | metadata | categorical | *Not specified.* | n=31, missing=0, classes=1, top not specified (×31) |
| rights_status | metadata | categorical | *Not specified.* | n=31, missing=0, classes=1, top manual_review_needed (×31) |
| usage_scope | metadata | categorical | *Not specified.* | n=31, missing=0, classes=1, top private_use_only (×31) |
| notes | metadata | categorical | *Not specified.* | n=31, missing=0, classes=1, top EcoSIS package ngee-arctic-leaf-spectral-reflectance-and-transmittance-data-2014-to-2016-utqiagvik--barrow--alaska, no interpolation applied by project. (×31) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/ngee-arctic-leaf-spectral-reflectance-and-transmittance-data-2014-to-2016-utqiagvik--barrow--alaska`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- NGEE Arctic Leaf Spectral Reflectance and Transmittance, Barrow, Alaska, 2014-2016 — [10.5440/1437044](https://doi.org/10.5440/1437044)
- Leaf Mass Area, Leaf Carbon and Nitrogen Content, Barrow, Alaska, 2012-2016 — [10.5440/1336812](https://doi.org/10.5440/1336812)
- Leaf Photosynthetic Parameters Vcmax and Jmax and Supporting Gas Exchange Data, Barrow, Alaska, 2012-2016 — [10.5440/1336809](https://doi.org/10.5440/1336809)
- Leaf Photosynthetic Parameters: Quantum Yield, Convexity, Respiration, Gross CO2 Assimilation Rate and Raw Gas Exchange Data, Barrow, Alaska, 2016 — [10.5440/1482338](https://doi.org/10.5440/1482338)

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** EcoSIS license is missing or unclear; private/internal conversion only by v0.5 policy.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `ddf884bbea69ee4312dfe88a526bb90d08b1eba44d19cace468da85bb9231ccb`
- **Processing hash:** `0d246a0123fc691453229c5f9227b84a20508403321ef0bea43a77cccbffc085` | **metadata hash:** `6d510e82e4033f790acbf9ffcc2acdca66063619dfbcc770b2f9b512e28c6046`
