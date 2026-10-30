# Datasheet — ECOSTRESS rock all axis 66af2adc

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS rock all axis 66af2adc. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 2 sample(s), 2 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | rock all | source instruments vary by sample | other | 0.4–14.98 none | 2 | 2868 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=2, missing=0, classes=2, top Dolomitic Limestone (×1) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=2, missing=0, classes=2, top rock.sedimentary.limestone.fine.all.limestone_2.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top rock (×2) |
| material_type | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top rock (×2) |
| site | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=2, missing=0, classes=2, top Sample No. 353, The Hunt and Salisbury Collection at the U.S.Geological Survey, Denver, Co. (×1) |
| country | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top N/A (×2) |
| species | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=2, missing=0, classes=2, top This somewhat heterogeneous sample consists of bands of pure fine-grained to microcrystalline dolomite, alternating with bands of coarser dolomite crystals and subangular aligned quartz grains showing pressure solution texture. There is also a greenish-brown material (clay) scattered throughout the sample in small amounts. Particle size was 0-75 Micrometers. Original ASTER Spectral Library name was jhu.becknic.rock.sedimentary.limestone.fine.limest2.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top jhu.becknic (×2) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top Directional (10 Degree) Hemispherical Reflectance (×2) |
| signal_type | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top Reflectance (percent) (×2) |
| axis_unit | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top Wavelength (micrometers) (×2) |
| axis_min | metadata | numeric | *Not specified.* | n=2, missing=0, range 0.4–0.4, mean 0.4 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=2, missing=0, range 14.98–14.98, mean 14.98 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=2, missing=0, range 2868–2868, mean 2868 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×2) |
| citation | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×2) |
| license | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×2) |
| rights_status | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top manual_review_needed (×2) |
| usage_scope | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top private_use_only (×2) |
| notes | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top none (×2) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://speclib.jpl.nasa.gov/download`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://speclib.jpl.nasa.gov/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** X: native axis unit is 'Wavelength (micrometers)' (micrometers), which is not supported by the axis unit enum; axis values remain in micrometers. Multiply by 1000 to convert to nm.; Curation identity contract: Identifiant échantillon déclaré dans M La clé est le numéro de spécimen source ; préparations, géométries et instruments peuvent différer. Aucun regroupement par nom de matériau.
- **Curated views:** M: 1 fields, Y: 1 fields, passport: 48 fields, measurements: 5 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- The ECOSTRESS spectral library version 1.0 — [10.1016/j.rse.2019.05.015](https://doi.org/10.1016/j.rse.2019.05.015)
- The ASTER Spectral Library Version 2.0 — [10.1016/j.rse.2008.11.007](https://doi.org/10.1016/j.rse.2008.11.007)

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** Official ECOSTRESS page requests citation and states copyright/all rights reserved; converted matrices are private/internal until redistribution rights are clarified.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `79b67a1046b851f9ca68932f9946a3b590610258d2f99323ec16c484faa82e02`
- **Processing hash:** `76da40b3002bce9afa473afcc241ac10b6e52ff204fa29143b9d75e09a72838a` | **metadata hash:** `1e2dd8356128f76646009138205d831ae145fe63ea2f6dc02b4e6482d396b112`
