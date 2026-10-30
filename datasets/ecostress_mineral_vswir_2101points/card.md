# Datasheet — ECOSTRESS mineral vswir axis 61f98690

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS mineral vswir axis 61f98690. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 148 sample(s), 406 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–3 (mean 2.743).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | mineral vswir | source instruments vary by sample | other | 0.4–2.5 none | 406 | 2101 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=406, missing=0, classes=131, top Quartz SiO_2 (×15) |
| class_label | target | categorical | *Not specified.* | n=406, missing=0, classes=12, top Silicate (×198) |
| subclass | target | categorical | *Not specified.* | n=406, missing=0, classes=8, top None (×202) |
| particle_size | target | categorical | *Not specified.* | n=406, missing=0, classes=4, top Fine (×147) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=406, missing=0, classes=406, top mineral.arsenate.none.coarse.vswir.a-1a.jpl.perkin.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=406, missing=0, classes=1, top mineral (×406) |
| material_type | metadata | categorical | *Not specified.* | n=406, missing=0, classes=1, top Mineral (×406) |
| site | metadata | categorical | *Not specified.* | n=406, missing=406, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=406, missing=0, classes=117, top Unknown. (×34) |
| country | metadata | categorical | *Not specified.* | n=406, missing=406, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=406, missing=406, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=406, missing=406, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=406, missing=406, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=406, missing=0, classes=1, top N/A (×406) |
| species | metadata | categorical | *Not specified.* | n=406, missing=406, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=406, missing=406, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=406, missing=406, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=406, missing=0, classes=406, top Particle size was 125-500um.Collected by: JPL Original ASTER Spectral Library name was jpl.perkin.mineral.arsenate.none.coarse.a01a.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=406, missing=0, classes=1, top jpl.perkin (×406) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=406, missing=0, classes=1, top Hemispherical reflectance (×406) |
| signal_type | metadata | categorical | *Not specified.* | n=406, missing=0, classes=1, top Reflectance (percent) (×406) |
| axis_unit | metadata | categorical | *Not specified.* | n=406, missing=0, classes=1, top Wavelength (micrometers) (×406) |
| axis_min | metadata | numeric | *Not specified.* | n=406, missing=0, range 0.4–0.4, mean 0.4 ± 5.558e-17 |
| axis_max | metadata | numeric | *Not specified.* | n=406, missing=0, range 2.5–2.5, mean 2.5 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=406, missing=0, range 2101–2101, mean 2101 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=406, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×406) |
| citation | metadata | categorical | *Not specified.* | n=406, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×406) |
| license | metadata | categorical | *Not specified.* | n=406, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×406) |
| rights_status | metadata | categorical | *Not specified.* | n=406, missing=0, classes=1, top manual_review_needed (×406) |
| usage_scope | metadata | categorical | *Not specified.* | n=406, missing=0, classes=1, top private_use_only (×406) |
| notes | metadata | categorical | *Not specified.* | n=406, missing=0, classes=402, top None (×5) |

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

- **Conversion warnings:** X: native axis unit is 'Wavelength (micrometers)' (micrometers), which is not supported by the axis unit enum; axis values remain in micrometers. Multiply by 1000 to convert to nm.; Curation identity contract: Sample identifier declared in M; frequencies of this identifier describe exported rows without establishing technical replicates. The key is the source specimen number; preparations, geometries, and instruments may differ. No grouping by material name.
- **Curated views:** M: 1 fields, Y: 4 fields, measurements: 4 fields, passport: 49 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `e6da0f37f3529ae4c4a2fddc07a043a72ddef4ce86cba49e5ebad94745fdd747`
- **Processing hash:** `da505e014fb27b3ba3acd279155f0e52b38c7764c3d49f4b1263b7fb406ea8d6` | **metadata hash:** `05d7e47214b8af4a56712425da36c361fe831f030c2f53480a9a28c74676eb6c`
