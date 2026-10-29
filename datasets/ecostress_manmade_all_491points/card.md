# Datasheet — ECOSTRESS manmade all axis 21e24555

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS manmade all axis 21e24555. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 14 sample(s), 14 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | manmade all | source instruments vary by sample | other | 0.42–14 none | 14 | 491 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=14, missing=0, classes=7, top Construction Concrete (×4) |
| class_label | target | categorical | *Not specified.* | n=14, missing=0, classes=3, top General Construction Material (×6) |
| subclass | target | categorical | *Not specified.* | n=14, missing=0, classes=6, top Paving Concrete (×4) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=14, missing=0, classes=14, top manmade.concrete.pavingconcrete.solid.all.0092uuu_cnc.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top manmade (×14) |
| material_type | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top manmade (×14) |
| site | metadata | categorical | *Not specified.* | n=14, missing=14, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top Spectra obtained from the Noncoventional Exploitation FactorsData System of the National Photographic Interpretation Center. (×14) |
| country | metadata | categorical | *Not specified.* | n=14, missing=14, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=14, missing=14, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=14, missing=14, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=14, missing=14, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top N/A (×14) |
| species | metadata | categorical | *Not specified.* | n=14, missing=14, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=14, missing=14, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=14, missing=14, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=14, missing=0, classes=14, top Gray and white weathered runway concrete. Sample had a flat surface, with a matte texture, and very little aggregate showing. Original ASTER Spectral Library name was jhu.becknic.manmade.concrete.paving.solid.0092uuu.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top jhu.becknic (×14) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top Directional (10 Degree) Hemispherical Reflectance (×14) |
| signal_type | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top Reflectance (percent) (×14) |
| axis_unit | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top Wavelength (micrometers) (×14) |
| axis_min | metadata | numeric | *Not specified.* | n=14, missing=0, range 0.42–0.42, mean 0.42 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=14, missing=0, range 14–14, mean 14 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=14, missing=0, range 491–491, mean 491 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×14) |
| citation | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×14) |
| license | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×14) |
| rights_status | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top manual_review_needed (×14) |
| usage_scope | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top private_use_only (×14) |
| notes | metadata | categorical | *Not specified.* | n=14, missing=0, classes=1, top none (×14) |

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
- **Curated views:** M: 0 fields, Y: 3 fields, measurements: 4 fields, passport: 50 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `3a72de50b80497309b6b6a6ad444b236c4e7f67b318c60678ee2e7f78c76211e`
- **Processing hash:** `3e6274e0ef11c73e229b615bad3ecb37c5cc3ab734cbd0d2fa7e2f385be73d19` | **metadata hash:** `40bcd13b89f10b535c08b727250b91b6f058f3c15f3406296994e051522ad7f0`
