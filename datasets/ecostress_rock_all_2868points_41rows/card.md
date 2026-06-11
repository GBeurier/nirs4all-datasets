# Datasheet — ECOSTRESS rock all axis be345a03

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS rock all axis be345a03. v2.0 standardized NIRS package: 1 spectral source(s), 5 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 39 sample(s), 41 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–2 (mean 1.051).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | rock all | source instruments vary by sample | other | 0.4–14.98 none | 41 | 2868 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=39, missing=0, classes=36, top Dolomitic Marble (×2) |
| class_label | target | categorical | *Not specified.* | n=39, missing=0, classes=2, top Metamorphic (×27) |
| subclass | target | categorical | *Not specified.* | n=39, missing=0, classes=11, top Marble (×7) |
| particle_size | target | categorical | *Not specified.* | n=39, missing=0, classes=2, top Fine (×36) |
| measurement | target | categorical | *Not specified.* | n=39, missing=0, classes=2, top Directional (10 Degree) Hemispherical Reflectance (×38) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=39, missing=0, classes=39, top rock.metamorphic.gneis.coarse.all.gneiss6.jhu.becknic.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=39, missing=0, classes=1, top rock (×39) |
| material_type | metadata | categorical | *Not specified.* | n=39, missing=0, classes=1, top rock (×39) |
| site | metadata | categorical | *Not specified.* | n=39, missing=39, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=39, missing=0, classes=39, top Sample No. 465, The Hunt and Salisbury Collection at the U.S.Geological Survey, Denver, Co. (×1) |
| country | metadata | categorical | *Not specified.* | n=39, missing=39, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=39, missing=39, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=39, missing=39, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=39, missing=39, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=39, missing=39, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=39, missing=39, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=39, missing=39, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=39, missing=39, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=39, missing=0, classes=39, top Coarse grains of slightly lineated hornblende euhedra with anhedra of alkali feldspar make up the bulk of this rock. There are scattered grains of pyrite and possibly a trace of quartz as well. The modes were 69% hornblende, 30.4% feldspar and 0.6% opaques. Particle size was 500-1500 Micrometer. Original ASTER Spectral Library name was jhu.becknic.rock.metamorphic.gneiss.coarse.gneiss6.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=39, missing=0, classes=1, top jhu.becknic (×39) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=39, missing=0, classes=2, top Directional (10 Degree) Hemispherical Reflectance (×38) |
| signal_type | metadata | categorical | *Not specified.* | n=39, missing=0, classes=1, top Reflectance (percent) (×39) |
| axis_unit | metadata | categorical | *Not specified.* | n=39, missing=0, classes=1, top Wavelength (micrometers) (×39) |
| axis_min | metadata | numeric | *Not specified.* | n=39, missing=0, range 0.4–0.4, mean 0.4 ± 5.624e-17 |
| axis_max | metadata | numeric | *Not specified.* | n=39, missing=0, range 14.98–14.98, mean 14.98 ± 7.198e-15 |
| n_points_original | metadata | numeric | *Not specified.* | n=39, missing=0, range 2868–2868, mean 2868 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=39, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×39) |
| citation | metadata | categorical | *Not specified.* | n=39, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×39) |
| license | metadata | categorical | *Not specified.* | n=39, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×39) |
| rights_status | metadata | categorical | *Not specified.* | n=39, missing=0, classes=1, top manual_review_needed (×39) |
| usage_scope | metadata | categorical | *Not specified.* | n=39, missing=0, classes=1, top private_use_only (×39) |
| notes | metadata | categorical | *Not specified.* | n=39, missing=0, classes=5, top none (×35) |

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
- **Content hash:** `0c0034554532c0956b61c9ad83fe1d7ecce28477851d06488935c79938815a2b`
- **Processing hash:** `2547b45d486e8fde9e96dfc787a3bae45deb5bda3f2e624f47da47cab5381e41` | **metadata hash:** `39a32b6edb555fe8c6e3656f0163052b78762081472f88c69f371af5caf6cf50`
