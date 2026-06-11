# Datasheet — ECOSTRESS rock all axis d24e4e1f

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS rock all axis d24e4e1f. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 28 sample(s), 28 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | rock all | source instruments vary by sample | other | 0.4–14.98 none | 28 | 2868 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=28, missing=0, classes=25, top Dolomitic Marble (×2) |
| class_label | target | categorical | *Not specified.* | n=28, missing=0, classes=2, top Metamorphic (×21) |
| subclass | target | categorical | *Not specified.* | n=28, missing=0, classes=10, top Schist (×7) |
| particle_size | target | categorical | *Not specified.* | n=28, missing=0, classes=2, top Coarse (×27) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=28, missing=0, classes=28, top rock.metamorphic.gneis.coarse.all.gneiss1.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=28, missing=0, classes=1, top rock (×28) |
| material_type | metadata | categorical | *Not specified.* | n=28, missing=0, classes=1, top rock (×28) |
| site | metadata | categorical | *Not specified.* | n=28, missing=28, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=28, missing=0, classes=26, top Sample No. 468, The Hunt and Salisbury Collection at the U.S.Geological Survey, Denver, Co. (×3) |
| country | metadata | categorical | *Not specified.* | n=28, missing=28, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=28, missing=28, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=28, missing=28, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=28, missing=28, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=28, missing=28, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=28, missing=28, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=28, missing=28, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=28, missing=28, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=28, missing=0, classes=28, top This is a greenish rock containing only 20% quartz, 35% albite, a mixture of chlorite and muscovite (40%) and 5% rutile.Particle size was 500-1500 Micrometers. Original ASTER Spectral Library name was jhu.becknic.rock.metamorphic.gneiss.coarse.gneiss1.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=28, missing=0, classes=1, top jhu.becknic (×28) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=28, missing=0, classes=1, top Directional (10 Degree) Hemispherical Reflectance (×28) |
| signal_type | metadata | categorical | *Not specified.* | n=28, missing=0, classes=1, top Reflectance (percent) (×28) |
| axis_unit | metadata | categorical | *Not specified.* | n=28, missing=0, classes=1, top Wavelength (micrometers) (×28) |
| axis_min | metadata | numeric | *Not specified.* | n=28, missing=0, range 0.4–0.4, mean 0.4 ± 5.653e-17 |
| axis_max | metadata | numeric | *Not specified.* | n=28, missing=0, range 14.98–14.98, mean 14.98 ± 3.618e-15 |
| n_points_original | metadata | numeric | *Not specified.* | n=28, missing=0, range 2868–2868, mean 2868 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=28, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×28) |
| citation | metadata | categorical | *Not specified.* | n=28, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×28) |
| license | metadata | categorical | *Not specified.* | n=28, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×28) |
| rights_status | metadata | categorical | *Not specified.* | n=28, missing=0, classes=1, top manual_review_needed (×28) |
| usage_scope | metadata | categorical | *Not specified.* | n=28, missing=0, classes=1, top private_use_only (×28) |
| notes | metadata | categorical | *Not specified.* | n=28, missing=1, classes=3, top none (×25) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://speclib.jpl.nasa.gov/download`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://speclib.jpl.nasa.gov/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

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

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `88651efdf9b45c18d8a48ee8c5344d1adf110952120a3f35489d7b20d9e81e31`
- **Processing hash:** `45fc424975ad46096a67082784dfa3c334ec8578ef6c47d7bce7edf5f740b1eb` | **metadata hash:** `7ea88a31b4cd36247076ab7c9692552629fb16ccaf93c7952fe4a9c7dc90adfe`
