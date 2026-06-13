# Datasheet — roche_type_roche_ts

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** timeseries
- **Description:** roche_type_roche_ts. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, timeseries
- **Contributor:** timeseries_classif_nirs_database

## Composition

- **Alignment:** observation level; 70 sample(s), 70 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | recovered_spectra | unknown | NIR | 0.4–14.01 none | 70 | 2844 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| type_roche | target | categorical | *Not specified.* | n=70, missing=0, classes=4, top 0 (×26) |
| ID_sample | metadata | categorical | *Not specified.* | n=70, missing=0, classes=70, top Rock_train_0001 (×1) |
| SpectralRep | metadata | numeric | *Not specified.* | n=70, missing=0, range 1–1, mean 1 ± 0 |
| dataset | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top Rock (×70) |
| product | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top roche (×70) |
| trait_header | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top type_roche (×70) |
| trait_description | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top Rock type. (×70) |
| split | metadata | categorical | *Not specified.* | n=70, missing=0, classes=2, top test (×50) |
| spectro | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top spectral reflectance (×70) |
| raw_label | metadata | categorical | *Not specified.* | n=70, missing=0, classes=4, top 1 (×26) |
| reference_value | metadata | categorical | *Not specified.* | n=70, missing=0, classes=4, top mafic (×26) |
| class_index | metadata | categorical | *Not specified.* | n=70, missing=0, classes=4, top 0 (×26) |
| dimensions | metadata | numeric | *Not specified.* | n=70, missing=0, range 1–1, mean 1 ± 0 |
| feature_count_per_dimension | metadata | numeric | *Not specified.* | n=70, missing=0, range 2844–2844, mean 2844 ± 0 |
| wavelength_note | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top ASTER/ECOSTRESS sources: the All spectra from the ASTER library have 2844 X values, from 14.0110 to 0.4000 um. The Beckman VSWIR section is documented over 0.4–2.5 um with a step of 0.001 um from 0.4 to 0.8 then 0.004 um from 0.8 to 2.5, but the merged band-by-band vector is not provided in the Rock archive; a linear axis interpolated here in decreasing order 14.0110->0.4000 over 2844 variables. (×70) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): test: 50, train: 20

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/aeon-toolkit/Rock.zip`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.timeseriesclassification.com/description.php?Dataset=Rock`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** Recovered from local initial-source exports; rights not cleared for redistribution.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `f13d5758243042cae3468d559c6d6494282a91358e15680a4719888bbf4edd28`
- **Processing hash:** `446387bb317f4cf17d4f625487f09c0386fd6670195a7492af1b6c494f69e191` | **metadata hash:** `2e50b96301c8eab81aa62f629bbf13900562c8ac30f3317e818e543fecf5ba83`
