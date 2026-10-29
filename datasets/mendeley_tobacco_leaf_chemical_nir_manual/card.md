# Datasheet — Tobacco leaf NIR spectra and chemical components

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** mendeley
- **Description:** Tobacco leaf NIR spectra and chemical components. v2.0 standardized NIRS package: 1 spectral source(s), 13 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, mendeley
- **Contributor:** Data In Brief / Mendeley tobacco leaf

## Composition

- **Alignment:** sample level; 347 sample(s), 347 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 4000–1e+04 cm-1 | 347 | 1557 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Total Alkaloids | target | numeric | *Not specified.* | n=347, missing=0, range 1.528–4.448, mean 3.05 ± 0.516 |
| Reducing Sugars | target | numeric | *Not specified.* | n=347, missing=0, range 5.513–25.49, mean 16.27 ± 3.432 |
| Total Sugars | target | numeric | *Not specified.* | n=347, missing=0, range 6.415–29.49, mean 18.84 ± 4.155 |
| Total Nitrogen | target | numeric | *Not specified.* | n=347, missing=0, range 1.637–3.063, mean 2.256 ± 0.3183 |
| K | target | numeric | *Not specified.* | n=347, missing=0, range 1.601–3.273, mean 2.341 ± 0.31 |
| cl | target | numeric | *Not specified.* | n=347, missing=0, range 1.495–9.481, mean 4.805 ± 1.516 |
| pH | target | numeric | *Not specified.* | n=347, missing=0, range 4.625–5.22, mean 4.934 ± 0.1137 |
| Starch | target | numeric | *Not specified.* | n=347, missing=0, range 2.589–7.368, mean 4.201 ± 0.8109 |
| Neochlorogenic Acid | target | numeric | *Not specified.* | n=347, missing=0, range 0.5367–2.457, mean 1.564 ± 0.339 |
| Chlorogenic Acid | target | numeric | *Not specified.* | n=347, missing=0, range 3.318–18.76, mean 10.59 ± 2.499 |
| Cryptochlorogenic Acid | target | numeric | *Not specified.* | n=347, missing=0, range 0.7951–3.918, mean 2.446 ± 0.5395 |
| Scopoletin | target | numeric | *Not specified.* | n=347, missing=0, range 0.1357–0.8212, mean 0.3342 ± 0.1236 |
| Rutin | target | numeric | *Not specified.* | n=347, missing=0, range 2.984–14.48, mean 8.954 ± 2.12 |
| year | metadata | numeric | *Not specified.* | n=347, missing=0, range 2018–2022, mean 2020 ± 1.171 |
| origin_label | metadata | categorical | *Not specified.* | n=347, missing=0, classes=6, top 巴西 (×136) |
| manual_download | metadata | categorical | *Not specified.* | n=347, missing=0, classes=1, top True (×347) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=347, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\tobacco leaf (×347) |
| manual_download_file | metadata | categorical | *Not specified.* | n=347, missing=0, classes=1, top A Near-Infrared Spectroscopy Dataset for Chemical.zip::A Near-Infrared Spectroscopy Dataset for Chemical/data/Raw-nir-spectra-data-B9Y2sV.xlsx (×347) |
| official_source_url | metadata | categorical | *Not specified.* | n=347, missing=0, classes=1, top https://data.mendeley.com/datasets/9z7dgdtggk/1 (×347) |
| standardization_batch | metadata | categorical | *Not specified.* | n=347, missing=0, classes=1, top v0.8.57 (×347) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/datasets/9z7dgdtggk/1`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Échantillon source de tabac ; regroupement par la colonne source conservée dans M. La multiplicité exportée ne prouve pas le nombre de scans moyennés en amont.
- **Curated views:** M: 2 fields, Y: 13 fields, passport: 6 fields, measurements: 1 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Official Mendeley record was recorded as CC BY 4.0 in the blocked inventory; files were supplied manually.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `27708ed58a95b00e0620228bb337a0c27096811b2bd2e8cc2017b0c60bf75bcb`
- **Processing hash:** `58c295721001955ffd8436bf81128d72f580a534b6395bff784475d44f1ec9b2` | **metadata hash:** `a42e0f1fedb95625dfb8875443339937dacbf0030e225f6058377f1d08316307`
