# Datasheet — FLOPP FTIR polymer classification

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** plastic
- **Description:** FLOPP FTIR polymer classification. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, plastic
- **Contributor:** ATR-FTIR Spectral Libraries of Plastic Particles, FLOPP and FLOPP-e

## Composition

- **Alignment:** sample level; 186 sample(s), 186 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | FLOPP FTIR spectra | ATR-FTIR instruments as represented in source library | MIR | 399.2–4002 none | 186 | 1869 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| polymer_name | target | categorical | *Not specified.* | n=186, missing=0, classes=17, top PP (×19) |
| library_name | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top FLOPP (×186) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top FTIR (×186) |
| sample_type | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top plastic particle (×186) |
| sample_description | metadata | categorical | *Not specified.* | n=186, missing=1, classes=162, top White Fiber (×6) |
| axis_unit | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top cm^-1 (×186) |
| axis_min | metadata | numeric | *Not specified.* | n=186, missing=0, range 399.2–399.2, mean 399.2 ± 5.7e-14 |
| axis_max | metadata | numeric | *Not specified.* | n=186, missing=0, range 4002–4002, mean 4002 ± 9.119e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=186, missing=0, range 1869–1869, mean 1869 ± 0 |
| signal_type | metadata | categorical | *Not specified.* | n=186, missing=0, classes=1, top ATR-FTIR intensity (×186) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): not_provided: 186

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://acs.figshare.com/articles/dataset/_ATR-FTIR_Spectral_Libraries_of_Plastic_Particles_FLOPP_and_FLOPP-e_for_the_Analysis_of_Microplastics/17070059`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://api.figshare.com/v2/articles/17070059`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://figshare.com/ndownloader/articles/17070059/versions/1`
- figshare — kind `figshare`, access `open`, license *Not specified.*: `10.6084/m9.figshare.17070059`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *Not specified.* — [10.1021/acs.analchem.1c02549](https://doi.org/10.1021/acs.analchem.1c02549)

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** Rights are not cleared for public redistribution, internal/private use only by default.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `c861462a52e9d92b3db711eaa4eb3201940f8434e7a3d270bfdd530deddb95a2`
- **Processing hash:** `4b07d22cb966349d226328d3cf037e801a9ad34123061660cac3c0151c2512f8` | **metadata hash:** `1706d1b2e71e01e6f6d4fedbe992a05fa9eb6c08a864e4de65bac8ead84d3895`
