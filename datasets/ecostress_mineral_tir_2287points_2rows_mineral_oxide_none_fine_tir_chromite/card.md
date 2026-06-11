# Datasheet — ECOSTRESS mineral tir axis cbf25a1b

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecostress
- **Description:** ECOSTRESS mineral tir axis cbf25a1b. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecostress
- **Contributor:** ECOSTRESS Spectral Library

## Composition

- **Alignment:** observation level; 2 sample(s), 2 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | mineral tir | source instruments vary by sample | other | 2.079–25.04 none | 2 | 2287 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=2, missing=0, classes=2, top Chromite Fe+2Cr2O4 (×1) |
| class_label | target | categorical | *Not specified.* | n=2, missing=0, classes=2, top Oxide (×1) |
| subclass | target | categorical | *Not specified.* | n=2, missing=1, classes=1, top Nesosilicate (×1) |
| ecostress_resource_id | metadata | categorical | *Not specified.* | n=2, missing=0, classes=2, top mineral.oxide.none.fine.tir.chromite_1.jhu.nicolet.spectrum (×1) |
| category | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top mineral (×2) |
| material_type | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top Mineral (×2) |
| site | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=2, missing=0, classes=2, top Smithsonian NMNH 117075, Sample from Tiebaghi Mine, NewCaledonia. (×1) |
| country | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| year | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=2, missing=2, classes=0, — |
| sample_description | metadata | categorical | *Not specified.* | n=2, missing=0, classes=2, top The sample was one large (3.5 cm x 2 cm x 2 cm) piece with a few crystal faces showing, weighing 42 g. Minimal contamination (<1%) occurred along a few thin veins containing mostly kaolinte. Microscopic examination confirmed the substantial purity of the sample. Most of the contaminating earthy material was removed by ultrasonic cleaning of the crushed sample. Particle size was less than 2 Micrometers.(Spinel Group) Original ASTER Spectral Library name was jhu.nicolet.mineral.oxide.none.powder.chromi1.spectrum.txt (×1) |
| instrument | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top jhu.nicolet (×2) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top Transmission (×2) |
| signal_type | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top Transmittance (percent) (×2) |
| axis_unit | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top Wavelength (micrometers) (×2) |
| axis_min | metadata | numeric | *Not specified.* | n=2, missing=0, range 2.079–2.079, mean 2.079 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=2, missing=0, range 25.04–25.04, mean 25.04 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=2, missing=0, range 2287–2287, mean 2287 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top 10.1016/j.rse.2019.05.015 (×2) |
| citation | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top Meerdink et al. 2019, Baldridge et al. 2009 (×2) |
| license | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top Copyright California Institute of Technology / JPL, all rights reserved (×2) |
| rights_status | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top manual_review_needed (×2) |
| usage_scope | metadata | categorical | *Not specified.* | n=2, missing=0, classes=1, top private_use_only (×2) |
| notes | metadata | categorical | *Not specified.* | n=2, missing=0, classes=2, top mineral.oxide.none.fine.tir.chromite_1.jhu.nicolet.ancillary.txt (×1) |

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
- **Content hash:** `51ab5d739d783138184319d025d37092560c9f8a170779604b3e548d62a3d00f`
- **Processing hash:** `1583cdbef41b8de732a059aa13c41c858cecde1cd4baaa22032bb2e21dde95e0` | **metadata hash:** `55f438c141002e2b96783ae6ae3af88c1f81106a2121a1745e1e053503e415c7`
