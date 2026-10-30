# Datasheet — ChEMBL IR Raman multiblock

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** chembl
- **Description:** Original ChEMBL IR intensities and Raman activities, indexed by native vibrational mode. Each molecule retains its exact frequencies in metadata. No Lorentz broadening or fabricated common wavenumber grid is applied.
- **Keywords:** nir, v2, chembl
- **Contributor:** Raman-ChEMBL Figshare

## Composition

- **Alignment:** observation level; *Not specified.* sample(s), 100000 observation(s) total; sample_id available: False.
- **Exported observations per source unit:** ND (identity/repetition information unavailable).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X1 | IR | Gaussian09 computed spectra | MIR | 0–4000 index | 50000 | 512 |
| X2 | Raman | Gaussian09 computed spectra | Raman | 0–4000 index | 50000 | 512 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| chembl_id | target | categorical | *Not specified.* | n=50000, missing=0, classes=50000, top CHEMBL100 (×1) |
| compound_name | target | categorical | *Not specified.* | n=50000, missing=0, classes=50000, top CHEMBL100 (×1) |
| molecular_formula | target | categorical | *Not specified.* | n=50000, missing=50000, classes=0, — |
| smiles | target | categorical | *Not specified.* | n=50000, missing=0, classes=49979, top CCCCCCCCCCCCC/C=C/[C@H]([C@@H](NC(=O)C)CO)O (×2) |
| inchi | target | categorical | *Not specified.* | n=50000, missing=50000, classes=0, — |
| inchikey | target | categorical | *Not specified.* | n=50000, missing=50000, classes=0, — |
| compound_class | target | categorical | *Not specified.* | n=50000, missing=0, classes=1, top ChEMBL molecule (×50000) |
| band_gap | target | numeric | *Not specified.* | n=50000, missing=0, range 0.00043–0.3228, mean 0.09778 ± 0.0265 |
| dipole_moment_total | target | numeric | *Not specified.* | n=50000, missing=0, range 0–20.74, mean 5.178 ± 2.536 |
| isotropic_polarizability | target | numeric | *Not specified.* | n=50000, missing=0, range 12.4–2030, mean 264.9 ± 73.84 |
| homo | target | numeric | *Not specified.* | n=50000, missing=0, range -0.3226–-0.04018, mean -0.1822 ± 0.019 |
| lumo | target | numeric | *Not specified.* | n=50000, missing=0, range -0.2559–0.06839, mean -0.08443 ± 0.0293 |
| electronic_ext | target | numeric | *Not specified.* | n=50000, missing=0, range 44.98–1.401e+05, mean 1.622e+04 ± 9913 |
| heat_capacity | target | numeric | *Not specified.* | n=50000, missing=0, range 6.201–233.7, mean 94.55 ± 25.54 |
| molecule_id | metadata | categorical | *Not specified.* | n=50000, missing=0, classes=50000, top 1 (×1) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=50000, missing=0, classes=1, top ir_raman_multiblock (×50000) |
| signal_type | metadata | categorical | *Not specified.* | n=50000, missing=0, classes=1, top computed_ir_and_raman (×50000) |
| axis_unit | metadata | categorical | *Not specified.* | n=50000, missing=0, classes=1, top cm-1 (×50000) |
| axis_min | metadata | numeric | *Not specified.* | n=50000, missing=0, range 0–0, mean 0 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=50000, missing=0, range 4000–4000, mean 4000 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=50000, missing=0, range 512–512, mean 512 ± 0 |
| preprocessing_original | metadata | categorical | *Not specified.* | n=50000, missing=0, classes=1, top local common-grid Lorentz-fitted export from source SQLite, no additional interpolation in nirs_db_vf (×50000) |
| data_source | metadata | categorical | *Not specified.* | n=50000, missing=0, classes=1, top Raman-ChEMBL Figshare SQLite/local processed exports (×50000) |
| publication_doi | metadata | categorical | *Not specified.* | n=50000, missing=0, classes=1, top 10.1038/s41597-025-05289-x (×50000) |
| citation | metadata | categorical | *Not specified.* | n=50000, missing=0, classes=1, top Liang et al. 2025, A Dataset of Raman and Infrared Spectra as an Extension to the ChEMBL, Scientific Data 12, 939 (×50000) |
| license | metadata | categorical | *Not specified.* | n=50000, missing=0, classes=1, top private_use_only pending ChEMBL/Figshare rights packaging review (×50000) |
| rights_status | metadata | categorical | *Not specified.* | n=50000, missing=0, classes=1, top manual_review_needed (×50000) |
| usage_scope | metadata | categorical | *Not specified.* | n=50000, missing=0, classes=1, top private_use_only (×50000) |
| notes | metadata | categorical | *Not specified.* | n=50000, missing=0, classes=1, top Converted from local processed ChEMBL IR/Raman export with row limit and no project resampling (×50000) |
| sdf_name | metadata | categorical | *Not specified.* | n=50000, missing=0, classes=50000, top CHEMBL100.xyz.sdf (×1) |
| n_atoms | metadata | numeric | *Not specified.* | n=50000, missing=0, range 3–99, mean 47.36 ± 13.29 |
| n_modes_total | metadata | numeric | *Not specified.* | n=50000, missing=0, range 3–291, mean 136.1 ± 39.87 |
| n_modes_positive | metadata | numeric | *Not specified.* | n=50000, missing=0, range 3–291, mean 136 ± 39.88 |
| has_negative_freq | metadata | categorical | *Not specified.* | n=50000, missing=0, classes=2, top no (×48370) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://figshare.com/articles/dataset/Raman-ChEMBL-part1/28593698`
- figshare — kind `figshare`, access `open`, license *Not specified.*: `10.6084/m9.figshare.28593698.v3`
- figshare — kind `figshare`, access `open`, license *Not specified.*: `10.6084/m9.figshare.28594295.v3`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Version 2 exposes original variable-length peak lists with NaN padding and per-molecule frequency metadata; the inherited 512-point fitted representation cannot be reproduced without undocumented broadening parameters.; Curation identity contract: Non déterminé
- **Curated views:** M: 0 fields, Y: 8 fields, passport: 31 fields, measurements: 2 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Rights retained from source metadata; review before public redistribution.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 2.1.0 | **schema/protocol:** 2.0
- **Content hash:** `8e00f3b3cf7e53fdb75ffa731a2de2f556d40af29b3ebed66f3d35b36378fc0c`
- **Processing hash:** `75baac490bff8b06ab8e5a387b383940b75631764f95ff743d246653f63b20b3` | **metadata hash:** `99e6ff1f2f4b3c0b56bab0988ba5a29e0dad1941e573f3751fd3a5a8433b47e5`
