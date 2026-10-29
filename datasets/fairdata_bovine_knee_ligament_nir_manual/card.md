# Datasheet — Bovine knee ligament multi-instrument NIR data

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** fairdata
- **Description:** Bovine knee ligament multi-instrument NIR data. v2.0 standardized NIRS package: 2 spectral source(s), 28 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, fairdata
- **Contributor:** Data In Brief / Fairdata bovine knee joint ligament

## Composition

- **Alignment:** sample level; 50 sample(s), 500 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 5–5 (mean 5).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X_AvaSpec_NIR256_2_5_HSC | X_AvaSpec_NIR256_2_5_HSC | *Not specified.* | NIR | 943.8–2497 nm | 250 | 243 |
| X_AvaSpec_ULS2048L_USB2 | X_AvaSpec_ULS2048L_USB2 | *Not specified.* | NIR | 319.4–1093 nm | 250 | 1343 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Phase difference 0.1 Hz | target | numeric | *Not specified.* | n=250, missing=225, range 3.143–6.921, mean 4.741 ± 1.301 |
| Phase difference 0.5 Hz | target | numeric | *Not specified.* | n=250, missing=225, range 3.438–8.03, mean 5.628 ± 1.781 |
| Phase difference 1 Hz | target | numeric | *Not specified.* | n=250, missing=225, range 4.923–10.39, mean 7 ± 1.966 |
| Dynamic modulus 0.1 Hz | target | numeric | *Not specified.* | n=250, missing=225, range 76.08–450.8, mean 164 ± 147.7 |
| Dynamic modulus 0.5 Hz | target | numeric | *Not specified.* | n=250, missing=225, range 78.16–457.8, mean 167.6 ± 149.5 |
| Dynamic modulus 1 Hz | target | numeric | *Not specified.* | n=250, missing=225, range 75.21–461.8, mean 168.5 ± 151.2 |
| Young's modulus | target | numeric | *Not specified.* | n=250, missing=225, range 58.44–410.7, mean 197.6 ± 127.4 |
| A | target | numeric | *Not specified.* | n=250, missing=225, range 383.2–2685, mean 961.5 ± 891.1 |
| B | target | numeric | *Not specified.* | n=250, missing=225, range -5.329–8.184, mean 3.722 ± 5.18 |
| C | target | numeric | *Not specified.* | n=250, missing=225, range 0.1287–0.4288, mean 0.2217 ± 0.1147 |
| D | target | numeric | *Not specified.* | n=250, missing=230, range 0.8253–1.497, mean 1.188 ± 0.2964 |
| F | target | numeric | *Not specified.* | n=250, missing=230, range 13.89–46.1, mean 25.45 ± 12.61 |
| Linear region length | target | numeric | *Not specified.* | n=250, missing=225, range 10.5–12.16, mean 11.49 ± 0.6218 |
| Toe region strain | target | numeric | *Not specified.* | n=250, missing=225, range 2.609–12.8, mean 6.923 ± 3.793 |
| Toe region stress | target | numeric | *Not specified.* | n=250, missing=225, range 0.5984–7.866, mean 4.643 ± 2.903 |
| Yield strain | target | numeric | *Not specified.* | n=250, missing=225, range 14.64–23.94, mean 18.41 ± 3.714 |
| Yield stress | target | numeric | *Not specified.* | n=250, missing=225, range 6.929–43.1, mean 24.23 ± 13.42 |
| Toughness at yield | target | numeric | *Not specified.* | n=250, missing=225, range 0.4717–2.644, mean 1.817 ± 0.9326 |
| Ultimate strain | target | numeric | *Not specified.* | n=250, missing=225, range 16.12–24.82, mean 21.1 ± 3.662 |
| Ultimate strength | target | numeric | *Not specified.* | n=250, missing=225, range 10–45.17, mean 26.02 ± 13.51 |
| Toughness at failure | target | numeric | *Not specified.* | n=250, missing=225, range 0.9599–3.408, mean 2.345 ± 1.085 |
| Water content | target | numeric | *Not specified.* | n=250, missing=225, range 69.11–83.03, mean 78.66 ± 5.001 |
| Hydroxyproline content of wet weight | target | numeric | *Not specified.* | n=250, missing=225, range 22.44–39.59, mean 28.45 ± 6.391 |
| Hydroxyproline content of dry weight | target | numeric | *Not specified.* | n=250, missing=225, range 121.2–152, mean 133.7 ± 10.48 |
| Uronic acid content of wet weight | target | numeric | *Not specified.* | n=250, missing=225, range 0.2465–0.6049, mean 0.4092 ± 0.1518 |
| Uronic acid content of dry weight | target | numeric | *Not specified.* | n=250, missing=225, range 0.7983–3.565, mean 2.1 ± 1.047 |
| Elastin content of wet weight | target | numeric | *Not specified.* | n=250, missing=225, range 5.973–12.64, mean 9.29 ± 2.653 |
| Elastin content of dry weight | target | numeric | *Not specified.* | n=250, missing=225, range 29.9–60.08, mean 41.28 ± 10.89 |
| site | metadata | numeric | *Not specified.* | n=250, missing=0, range 1–5, mean 3 ± 1.417 |
| knee_identifier | metadata | categorical | *Not specified.* | n=250, missing=225, classes=1, top 10.0 (×25) |
| ligament_type | metadata | categorical | *Not specified.* | n=250, missing=225, classes=5, top ACL (×5) |
| manual_download | metadata | categorical | *Not specified.* | n=250, missing=0, classes=1, top True (×250) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=250, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\bovine knee (×250) |
| manual_download_file | metadata | categorical | *Not specified.* | n=250, missing=0, classes=1, top minimal_source/Data_NIRS.xlsx \| minimal_source/Data_biomechanics_and_biochemistry.xlsx (×250) |
| official_source_url | metadata | categorical | *Not specified.* | n=250, missing=0, classes=1, top https://etsin.fairdata.fi/dataset/925999ad-8127-4428-b7cc-c03c12e62d3c/data (×250) |
| standardization_batch | metadata | categorical | *Not specified.* | n=250, missing=0, classes=1, top v0.8.57 (×250) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://etsin.fairdata.fi/dataset/925999ad-8127-4428-b7cc-c03c12e62d3c/data`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: 50 ligaments mesurés en cinq sites chacun, dans deux blocs alignés ; 5 positions spatiales, pas cinq préparations indépendantes.
- **Curated views:** M: 2 fields, Y: 28 fields, measurements: 0 fields, passport: 7 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Fairdata API license was recorded as CC BY 4.0 in the blocked inventory; files were supplied manually.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `b18f0d138e10784cb7d316d57711b629f8b86a39248dfb24d77ce5884040bf23`
- **Processing hash:** `e42e3f20f09b47d3dddfa3a0134d7f9bc6c7d761b3e8cd3fc0b9a3ba29afb495` | **metadata hash:** `fefd91a439e1cec160402724283c16c6a6fb7c4b539ec607843f3ebbd72ad935`
