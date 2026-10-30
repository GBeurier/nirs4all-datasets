# Datasheet — ECOSTRESS mineral tir axis d3032c60

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS mineral tir axis d3032c60. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** sample level; 5 sample(s), 5 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | mineral tir | source instruments vary by sample | other | 2.079–25.04 none | 5 | 2287 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=5, missing=0, classes=5, top Diopside CaMgSi2O6 (×1) |
| subclass | target | categorical | *Not specified.* | n=5, missing=0, classes=4, top Tectosilicate (×2) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=5, missing=0, classes=5, top mineral.silicate.inosilicate.fine.tir.diopside_2.jhu.nicolet.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top mineral (×5) |
| material_type | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top Mineral (×5) |
| site | metadata | categorical | *Not specified.* | n=5, missing=5, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=5, missing=0, classes=5, top Sample from DeKalb, New York via the Smithsonian (sampleno. NMNH R18685). (×1) |
| country | metadata | categorical | *Not specified.* | n=5, missing=5, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=5, missing=5, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=5, missing=5, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=5, missing=5, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top N/A (×5) |
| species | metadata | categorical | *Not specified.* | n=5, missing=5, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=5, missing=5, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=5, missing=5, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=5, missing=0, classes=5, top Most of the 13 mm x 10 mm x 6 mm sample was clean, fresh and green. One area was eroded and weathered and probably impure. The crushed sample was hand-picked to avoid impurities. A moderate amount of weathering and alteration can be seen under the microscope. The alteration is brown in color (limonite). Particle size was less than 2 Micrometers.(Chain Silicates) (Pyroxene Group) Original ASTER Spectral Library name was jhu.nicolet.mineral.silicate.inosilicate.powder.diopsi2.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top jhu.nicolet (×5) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top Transmission (×5) |
| signal_type | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top Transmittance (percent) (×5) |
| axis_unit | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top Wavelength (micrometers) (×5) |
| axis_min | metadata | numeric | *Not specified.* | n=5, missing=0, range 2.079–2.079, mean 2.079 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=5, missing=0, range 25.04–25.04, mean 25.04 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=5, missing=0, range 2287–2287, mean 2287 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×5) |
| citation | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×5) |
| license | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×5) |
| rights_status | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top manual_review_needed (×5) |
| usage_scope | metadata | categorical | *Not specified.* | n=5, missing=0, classes=1, top private_use_only (×5) |
| notes | metadata | categorical | *Not specified.* | n=5, missing=0, classes=5, top mineral.silicate.inosilicate.fine.tir.diopside_2.jhu.nicolet.ancillary.txt (×1) |

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

- **Conversion warnings:** X: native axis unit is 'Wavelength (micrometers)' (micrometers), which is not supported by the axis unit enum; axis values remain in micrometers. Multiply by 1000 to convert to nm.; Curation identity contract: Sample identifier declared in M. The key is the source specimen number; preparations, geometries, and instruments may differ. No grouping by material name.
- **Curated views:** M: 1 fields, Y: 2 fields, measurements: 4 fields, passport: 49 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `71c637ed5f56dbf44be7c36f776fc7746190eab86cb7a58290a9c37cac5ff21a`
- **Processing hash:** `9816b01811353d2fccdafa03fb7bebb2c626f36d5343621741a87256254a62bf` | **metadata hash:** `33a6b19470bf39207b7fb2e4c44fab5fbe7734f560058f95c5036c7643eacf7a`
