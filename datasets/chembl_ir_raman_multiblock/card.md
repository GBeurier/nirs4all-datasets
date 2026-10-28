# Datasheet — ChEMBL IR Raman multiblock

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** chembl
- **Description:** Original ChEMBL IR intensities and Raman activities, indexed by native vibrational mode. Each molecule retains its exact frequencies in metadata. No Lorentz broadening or fabricated common wavenumber grid is applied.
- **Keywords:** nir, v2, chembl
- **Contributor:** Raman-ChEMBL Figshare

## Composition

- **Alignment:** observation level; 50000 sample(s), 100000 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X1 | IR | Gaussian09 computed spectra | MIR | 1–291 index | 50000 | 291 |
| X2 | Raman | Gaussian09 computed spectra | Raman | 1–291 index | 50000 | 291 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| chembl_id | target | categorical | *Not specified.* | n=50000, missing=0, classes=50000, top CHEMBL100 (×1) |
| compound_name | target | categorical | *Not specified.* | n=50000, missing=50000, classes=0, — |
| molecular_formula | target | categorical | *Not specified.* | n=50000, missing=50000, classes=0, — |
| smiles | target | categorical | *Not specified.* | n=50000, missing=0, classes=49979, top CCCCCCCCCCCCC/C=C/[C@H]([C@@H](NC(=O)C)CO)O (×2) |
| inchi | target | categorical | *Not specified.* | n=50000, missing=50000, classes=0, — |
| inchikey | target | categorical | *Not specified.* | n=50000, missing=50000, classes=0, — |
| compound_class | target | categorical | *Not specified.* | n=50000, missing=50000, classes=0, — |
| band_gap | target | numeric | *Not specified.* | n=50000, missing=0, range 0.00043–0.3228, mean 0.09778 ± 0.0265 |
| dipole_moment_total | target | numeric | *Not specified.* | n=50000, missing=0, range 0–20.74, mean 5.178 ± 2.536 |
| isotropic_polarizability | target | numeric | *Not specified.* | n=50000, missing=0, range 12.4–2030, mean 264.9 ± 73.84 |
| homo | target | numeric | *Not specified.* | n=50000, missing=0, range -0.3226–-0.04018, mean -0.1822 ± 0.019 |
| lumo | target | numeric | *Not specified.* | n=50000, missing=0, range -0.2559–0.06839, mean -0.08443 ± 0.0293 |
| electronic_ext | target | numeric | *Not specified.* | n=50000, missing=0, range 44.98–1.401e+05, mean 1.622e+04 ± 9913 |
| heat_capacity | target | numeric | *Not specified.* | n=50000, missing=0, range 6.201–233.7, mean 94.55 ± 25.54 |
| molecule_id | metadata | categorical | *Not specified.* | n=50000, missing=0, classes=50000, top 1 (×1) |
| sdf_name | metadata | categorical | *Not specified.* | n=50000, missing=0, classes=50000, top CHEMBL100.xyz.sdf (×1) |
| n_atoms | metadata | numeric | *Not specified.* | n=50000, missing=0, range 3–99, mean 47.36 ± 13.29 |
| n_modes_total | metadata | numeric | *Not specified.* | n=50000, missing=0, range 3–291, mean 136.1 ± 39.87 |
| n_modes_positive | metadata | numeric | *Not specified.* | n=50000, missing=0, range 3–291, mean 136 ± 39.88 |
| has_negative_freq | metadata | categorical | *Not specified.* | n=50000, missing=0, classes=2, top False (×48370) |
| mode_frequencies_cm1 | metadata | text | *Not specified.* | *Not specified.* |
| database_tag | metadata | text | *Not specified.* | *Not specified.* |
| xyz_name | metadata | text | *Not specified.* | *Not specified.* |
| Rx | metadata | numeric | *Not specified.* | n=50000, missing=0, range 0–2099, mean 0.5385 ± 10.03 |
| Ry | metadata | numeric | *Not specified.* | n=50000, missing=0, range 0.00704–245, mean 0.1237 ± 1.123 |
| Rz | metadata | numeric | *Not specified.* | n=50000, missing=0, range 0.0067–133.7, mean 0.1011 ± 0.6348 |
| Dx | metadata | numeric | *Not specified.* | n=50000, missing=0, range -18.43–20.22, mean 0.001568 ± 3.956 |
| Dy | metadata | numeric | *Not specified.* | n=50000, missing=0, range -16.42–17.82, mean 0.2724 ± 3.442 |
| Dz | metadata | numeric | *Not specified.* | n=50000, missing=0, range -12.14–13.12, mean 0.1111 ± 2.38 |
| origin_url | metadata | text | *Not specified.* | *Not specified.* |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://figshare.com/articles/dataset/Raman-ChEMBL-part1/28593698`
- figshare — kind `figshare`, access `open`, license *Not specified.*: `10.6084/m9.figshare.28593698.v3`
- figshare — kind `figshare`, access `open`, license *Not specified.*: `10.6084/m9.figshare.28594295.v3`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Version 2 exposes original variable-length peak lists with NaN padding and per-molecule frequency metadata; the inherited 512-point fitted representation cannot be reproduced without undocumented broadening parameters.

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

- **Content version:** 2.0.0 | **schema/protocol:** 2.0
- **Content hash:** `374b18cfad8ccfd9fe8dc5b8559f919eefcab3c85a316d88d80253ba206f2fec`
- **Processing hash:** `2325b1cab4c9fc13af1a8145e9008ba78d73559f1b79207f70a9001247b921d4` | **metadata hash:** `6f4533875fa8a85e0a78cefefdd100f94f842ef0e802589a967372c93d069eef`
