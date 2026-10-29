# Datasheet — ECOSTRESS manmade all axis 0d1ca66e

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS manmade all axis 0d1ca66e. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 6 sample(s), 6 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | manmade all | source instruments vary by sample | other | 0.3–14 none | 6 | 551 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=6, missing=0, classes=6, top Plate Window Glass (×1) |
| class_label | target | categorical | *Not specified.* | n=6, missing=0, classes=2, top Roofing Material (×4) |
| subclass | target | categorical | *Not specified.* | n=6, missing=0, classes=4, top Rubber (×3) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=6, missing=0, classes=6, top manmade.generalconstructionmaterial.glas.solid.all.0796uuugls.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top manmade (×6) |
| material_type | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top manmade (×6) |
| site | metadata | categorical | *Not specified.* | n=6, missing=6, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=6, missing=0, classes=2, top Spectra obtained from the Noncoventional Exploitation FactorsData System of the National Photographic Interpretation Center. (×5) |
| country | metadata | categorical | *Not specified.* | n=6, missing=6, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=6, missing=6, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=6, missing=6, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=6, missing=6, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top N/A (×6) |
| species | metadata | categorical | *Not specified.* | n=6, missing=6, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=6, missing=6, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=6, missing=6, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=6, missing=0, classes=6, top Unweathered, transparent construction plate window glass. Original ASTER Spectral Library name was jhu.becknic.manmade.construction.glass.solid.0796uuu.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top jhu.becknic (×6) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top Directional (10 Degree) Hemispherical Reflectance (×6) |
| signal_type | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top Reflectance (percent) (×6) |
| axis_unit | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top Wavelength (micrometers) (×6) |
| axis_min | metadata | numeric | *Not specified.* | n=6, missing=0, range 0.3–0.3, mean 0.3 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=6, missing=0, range 14–14, mean 14 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=6, missing=0, range 551–551, mean 551 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×6) |
| citation | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×6) |
| license | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×6) |
| rights_status | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top manual_review_needed (×6) |
| usage_scope | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top private_use_only (×6) |
| notes | metadata | categorical | *Not specified.* | n=6, missing=0, classes=1, top none (×6) |

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
- **Curated views:** M: 1 fields, Y: 3 fields, measurements: 4 fields, passport: 49 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `d30e74c2d30737ff146edf5438d584bd81dbede72894397b7b93e8e25501e43b`
- **Processing hash:** `8f75a14559cfd1afe1a68dbe513c17709cfcd972a75bb2962be11d0d4c462542` | **metadata hash:** `009902505a598a62c01cdfbc162a0c86f8a05a6ca92231a451f029a3ee95d800`
