# Datasheet — ECOSTRESS rock all axis 8cf1b56d

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS rock all axis 8cf1b56d. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 35 sample(s), 35 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | rock all | source instruments vary by sample | other | 0.4–14.01 none | 35 | 2826 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=35, missing=0, classes=3, top Basalt (×22) |
| class_label | target | categorical | *Not specified.* | n=35, missing=0, classes=2, top Igneous (×22) |
| subclass | target | categorical | *Not specified.* | n=35, missing=0, classes=4, top Mafic (×22) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=35, missing=0, classes=35, top rock.igneous.mafic.solid.all.ba12c1f.usgs.perknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top rock (×35) |
| material_type | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top Rock (×35) |
| site | metadata | categorical | *Not specified.* | n=35, missing=35, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=35, missing=0, classes=9, top Ronda, Spain (×13) |
| country | metadata | categorical | *Not specified.* | n=35, missing=35, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=35, missing=35, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=35, missing=35, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=35, missing=35, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top N/A (×35) |
| species | metadata | categorical | *Not specified.* | n=35, missing=35, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=35, missing=35, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=35, missing=35, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=35, missing=0, classes=35, top dark gray vesicular basalt Sample was Whole rock chips Original ASTER Spectral Library name was usgs.perknic.rock.igneous.mafic.solid.ba12c1f.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top usgs.perknic (×35) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top Reflectance (×35) |
| signal_type | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top Reflectance (percent) (×35) |
| axis_unit | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top Wavelength (micrometers) (×35) |
| axis_min | metadata | numeric | *Not specified.* | n=35, missing=0, range 0.4–0.4, mean 0.4 ± 5.632e-17 |
| axis_max | metadata | numeric | *Not specified.* | n=35, missing=0, range 14.01–14.01, mean 14.01 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=35, missing=0, range 2826–2826, mean 2826 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×35) |
| citation | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×35) |
| license | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×35) |
| rights_status | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top manual_review_needed (×35) |
| usage_scope | metadata | categorical | *Not specified.* | n=35, missing=0, classes=1, top private_use_only (×35) |
| notes | metadata | categorical | *Not specified.* | n=35, missing=0, classes=35, top rock.igneous.mafic.solid.all.ba12c1f.usgs.perknic.ancillary.txt (×1) |

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
- **Content hash:** `3d8a41aba1a020ca881921ae9062fcb09d776b0c09c72e1710958041174fd796`
- **Processing hash:** `32c70144a9fb453d52385f3449f1d5f13a12a43a8906d8aca96c05e8ae823dea` | **metadata hash:** `ba7ba6e5f4cb13f29cbc6bab2734b2c0dac4661fa862bba2a0ba995230bee29a`
