# Datasheet — Zenodo Western Highveld soil NIR MIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** zenodo
- **Description:** Zenodo Western Highveld soil NIR MIR. v2.0 standardized NIRS package: 2 spectral source(s), 6 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, zenodo
- **Contributor:** Western Highveld Soil fertility, NIR and MIR spectral data

## Composition

- **Alignment:** sample level; 803 sample(s), 1606 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X1 | NeoSpectra handheld NIR | NeoSpectra handheld FT-NIR spectrometer | NIR | 4003–7407 cm-1 | 803 | 251 |
| X2 | Bruker Alpha II MIR | Bruker Alpha II DRIFT-MIR spectrometer | MIR | 600–3997 cm-1 | 803 | 1655 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| pH(KCl) | target | numeric | *Not specified.* | n=803, missing=0, range 3.69–7.62, mean 5.252 ± 0.7959 |
| P(Bray 1) | target | numeric | *Not specified.* | n=803, missing=0, range 0.825–255.7, mean 26.07 ± 23.98 |
| K | target | numeric | *Not specified.* | n=803, missing=0, range 2–526.3, mean 148.2 ± 76.4 |
| Ca | target | numeric | *Not specified.* | n=803, missing=0, range 45–2243, mean 469.3 ± 255.2 |
| Mg | target | numeric | *Not specified.* | n=803, missing=0, range 16–461.6, mean 117.2 ± 70.33 |
| Na | target | numeric | *Not specified.* | n=803, missing=0, range 0.5246–84.58, mean 11.68 ± 7.804 |
| file_url | metadata | categorical | *Not specified.* | n=803, missing=0, classes=1, top https://zenodo.org/api/records/17510653/files/NWU_NIR_MIR_Dataset.csv/content (×803) |
| article_url | metadata | categorical | *Not specified.* | n=803, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S2352340926007079 (×803) |
| doi_dataset | metadata | categorical | *Not specified.* | n=803, missing=0, classes=1, top 10.5281/zenodo.17510653 (×803) |
| doi_publication | metadata | categorical | *Not specified.* | n=803, missing=0, classes=1, top 10.1016/j.dib.2026.113160 (×803) |
| license | metadata | categorical | *Not specified.* | n=803, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×803) |
| license_id | metadata | categorical | *Not specified.* | n=803, missing=0, classes=1, top cc-by-4.0 (×803) |
| license_url | metadata | categorical | *Not specified.* | n=803, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×803) |
| rights_status | metadata | categorical | *Not specified.* | n=803, missing=0, classes=1, top explicit_open (×803) |
| usage_scope | metadata | categorical | *Not specified.* | n=803, missing=0, classes=1, top public_reuse_possible (×803) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=803, missing=0, classes=1, top True (×803) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=803, missing=0, classes=1, top NIR \| MIR (×803) |
| axis_unit | metadata | categorical | *Not specified.* | n=803, missing=0, classes=1, top cm^-1 \| cm^-1 (×803) |
| axis_min | metadata | categorical | *Not specified.* | n=803, missing=0, classes=1, top 4003 \| 600 (×803) |
| axis_max | metadata | categorical | *Not specified.* | n=803, missing=0, classes=1, top 7407 \| 3997 (×803) |
| n_points_original | metadata | categorical | *Not specified.* | n=803, missing=0, classes=1, top 251 \| 1655 (×803) |
| notes | metadata | categorical | *Not specified.* | n=803, missing=0, classes=1, top Single Zenodo CSV contains NIR spectra from about 7407-4003 cm^-1 and MIR spectra from about 3997-600 cm^-1. (×803) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Zenodo — kind `zenodo`, access `open`, license *Not specified.*: `https://zenodo.org/records/17510653`
- Zenodo — kind `zenodo`, access `open`, license *Not specified.*: `https://zenodo.org/api/records/17510653/files/NWU_NIR_MIR_Dataset.csv/content`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://creativecommons.org/licenses/by/4.0/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 0 fields, Y: 6 fields, passport: 20 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Zenodo record license is CC-BY-4.0; redistribution/publication reuse allowed with attribution.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `25bf7273e53ebda86b8be10b0aa49e54b34153dd415453c645b3375a6888877b`
- **Processing hash:** `8ece68ab717cb514af66678c6bb77bc69a404554c7ee61a6e2e8af6f11c082ff` | **metadata hash:** `85340fab27cd325f58c921e911e8fe4603f332381ced3fdcc09fa713c6e6aef6`
