# Datasheet — ECOSTRESS mineral tir axis 85fbc8f6

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS mineral tir axis 85fbc8f6. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 150 sample(s), 402 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–3 (mean 2.68).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | mineral tir | source instruments vary by sample | other | 2–15.39 none | 402 | 2256 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=402, missing=0, classes=134, top Quartz SiO_2 (×14) |
| class_label | target | categorical | *Not specified.* | n=402, missing=0, classes=12, top Silicate (×201) |
| subclass | target | categorical | *Not specified.* | n=402, missing=0, classes=8, top None (×200) |
| particle_size | target | categorical | *Not specified.* | n=402, missing=0, classes=3, top Fine (×150) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=402, missing=0, classes=402, top mineral.arsenate.none.coarse.tir.a-1a.jpl.nicolet.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top mineral (×402) |
| material_type | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top Mineral (×402) |
| site | metadata | categorical | *Not specified.* | n=402, missing=402, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=402, missing=30, classes=110, top N/A (×25) |
| country | metadata | categorical | *Not specified.* | n=402, missing=402, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=402, missing=402, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=402, missing=402, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=402, missing=402, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top N/A (×402) |
| species | metadata | categorical | *Not specified.* | n=402, missing=402, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=402, missing=402, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=402, missing=402, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=402, missing=0, classes=402, top Particle size was 125-500um.Collected by JPL Original ASTER Spectral Library name was jpl.nicolet.mineral.arsenate.none.coarse.a01a.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top jpl.nicolet (×402) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top Hemispherical reflectance (×402) |
| signal_type | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top Reflectance (percent) (×402) |
| axis_unit | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top Wavelength (micrometers) (×402) |
| axis_min | metadata | numeric | *Not specified.* | n=402, missing=0, range 2–2, mean 2 ± 4.446e-16 |
| axis_max | metadata | numeric | *Not specified.* | n=402, missing=0, range 15.39–15.39, mean 15.39 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=402, missing=0, range 2256–2256, mean 2256 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×402) |
| citation | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×402) |
| license | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×402) |
| rights_status | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top manual_review_needed (×402) |
| usage_scope | metadata | categorical | *Not specified.* | n=402, missing=0, classes=1, top private_use_only (×402) |
| notes | metadata | categorical | *Not specified.* | n=402, missing=0, classes=398, top None (×5) |

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

- **Conversion warnings:** X: native axis unit is 'Wavelength (micrometers)' (micrometers), which is not supported by the axis unit enum; axis values remain in micrometers. Multiply by 1000 to convert to nm.; Curation identity contract: Identifiant échantillon déclaré dans M ; les fréquences de cet identifiant décrivent les lignes exportées, sans établir des répétitions techniques. La clé est le numéro de spécimen source ; préparations, géométries et instruments peuvent différer. Aucun regroupement par nom de matériau.
- **Curated views:** M: 1 fields, Y: 4 fields, passport: 49 fields, measurements: 4 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `fada0b2a2c42e90316962d368ebe25e45be6e8e11ebcc0de3cdb6f5e5f315883`
- **Processing hash:** `a82511b1c79111dc267bbfcf84621829ca1055c71f43ecfb625f4e658a848e72` | **metadata hash:** `49081e5be9bbd0bb07a353ab83a8d231c1c6794cc3b66fd68e4383e1602a16a4`
