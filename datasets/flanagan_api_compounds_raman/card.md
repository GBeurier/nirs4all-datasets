# Datasheet — Flanagan API compounds Raman

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** flanagan
- **Description:** Flanagan API compounds Raman. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, flanagan
- **Contributor:** Open-source Raman spectra of chemical compounds for API development

## Composition

- **Alignment:** sample level; 3510 sample(s), 3510 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Flanagan Raman spectra | Raman instrument as documented by source article | Raman | 150–3425 none | 3510 | 3276 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| compound | target | categorical | *Not specified.* | n=3510, missing=0, classes=32, top Cyclohexane (×145) |
| common_application | target | categorical | *Not specified.* | n=3510, missing=0, classes=2, top Intermediate (×2187) |
| solvent_reagent | target | categorical | *Not specified.* | n=3510, missing=0, classes=3, top Solvent (×2429) |
| compound_rep_index | metadata | numeric | *Not specified.* | n=3510, missing=0, range 1–145, mean 55.73 ± 32.41 |
| publication_url | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top https://www.nature.com/articles/s41597-025-04848-6 (×3510) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top Raman (×3510) |
| sample_type | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top chemical compound / active pharmaceutical ingredient context (×3510) |
| formula | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=30, top C4H11N (×211) |
| organic | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top Y (×3510) |
| supplier_product | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=25, top Scharlau - HPLC grade (×316) |
| assay_pct | metadata | numeric | *Not specified.* | n=3510, missing=0, range 95–99.9, mean 99.24 ± 0.9525 |
| exposure_secs | metadata | numeric | *Not specified.* | n=3510, missing=0, range 2–45, mean 11.74 ± 10.37 |
| pixel_fill_pct | metadata | numeric | *Not specified.* | n=3510, missing=0, range 40–73, mean 59.14 ± 8.471 |
| compound_source_sample_count | metadata | numeric | *Not specified.* | n=3510, missing=0, range 100–145, mean 110.5 ± 9.943 |
| approx_raman_bands_source | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=31, top 186, 679, 1061, 1204, 1398, 1660, 2782, 2963 (×210) |
| axis_unit | metadata | categorical | *Not specified.* | n=3510, missing=0, classes=1, top cm^-1 (×3510) |
| axis_min | metadata | numeric | *Not specified.* | n=3510, missing=0, range 150–150, mean 150 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=3510, missing=0, range 3425–3425, mean 3425 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=3510, missing=0, range 3276–3276, mean 3276 ± 0 |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): not_provided: 3510

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- figshare — kind `figshare`, access `open`, license *Not specified.*: `10.6084/m9.figshare.27931131`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://api.figshare.com/v2/articles/27931131`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.nature.com/articles/s41597-025-04848-6`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *Not specified.* — [10.1038/s41597-025-04848-6](https://doi.org/10.1038/s41597-025-04848-6)

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** Rights are not cleared for public redistribution, internal/private use only by default.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `9e76d5da963ccb1664f475c17ad50e887a3e0db52b5a612702409fb5cb035d9f`
- **Processing hash:** `3a2d81775b84d0776e3a127e87eabbda48fc5e7e18f470722043a48879a4871b` | **metadata hash:** `68a01a323144322a2a535b90f57045f99beed00f4a8ab848186d559dcc695a96`
