# Datasheet — ECOSTRESS mineral all axis 20b176d4

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS mineral all axis 20b176d4. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 4 sample(s), 4 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | mineral all | source instruments vary by sample | other | 0.4–14.05 none | 4 | 2231 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=4, missing=0, classes=4, top Natron Na2CO310H2O (×1) |
| class_label | target | categorical | *Not specified.* | n=4, missing=0, classes=2, top Sulfate (×3) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=4, missing=0, classes=4, top mineral.carbonate.none.coarse.all.natron.usgs.perknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top mineral (×4) |
| material_type | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top Mineral (×4) |
| site | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top Produced in lab (×4) |
| country | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top N/A (×4) |
| species | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=4, missing=4, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=4, missing=0, classes=4, top SyntheticSample was unsieved powder. Original ASTER Spectral Library name was usgs.perknic.mineral.carbonate.none.coarse.natron.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top usgs.perknic (×4) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top Directional Hemispherical Reflectance (×4) |
| signal_type | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top Reflectance (percent) (×4) |
| axis_unit | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top Wavelength (micrometers) (×4) |
| axis_min | metadata | numeric | *Not specified.* | n=4, missing=0, range 0.4–0.4, mean 0.4 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=4, missing=0, range 14.05–14.05, mean 14.05 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=4, missing=0, range 2231–2231, mean 2231 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×4) |
| citation | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×4) |
| license | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×4) |
| rights_status | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top manual_review_needed (×4) |
| usage_scope | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top private_use_only (×4) |
| notes | metadata | categorical | *Not specified.* | n=4, missing=0, classes=1, top none (×4) |

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
- **Curated views:** M: 0 fields, Y: 2 fields, measurements: 5 fields, passport: 49 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `aa4a6354bb04afa8cbd7b31b70b3573d8b5696d7c98c10fc3767f0d5f45191be`
- **Processing hash:** `96c339d2aa87130a3ae85273bf9300c00566c9c86a6e830e1a58b2b12236c032` | **metadata hash:** `d7b57beb2e802b4e819d74679327010f82042d30c30e8e7112e9648f7093347c`
