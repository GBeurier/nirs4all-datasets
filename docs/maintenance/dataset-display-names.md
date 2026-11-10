# Dataset display names

The [5 November 2026 crosswalk](../../catalog/documentation/dataset-display-names-20261105.csv)
records the previous and revised display names of all 242 descriptors on the
proposal branch (241 official-base records and the pending Lyonia addition).
It is keyed by the stable `dataset_id`. Five previous names were shared by
multiple descriptors; previous display names alone are therefore not unique
lookup keys. The source record and current descriptor IDs remain the authority.

## Convention

Use the material or recognized collection, then the distinguishing experimental
context and spectral measurement. Keep informative collection names such as
LUCAS, OSSL, CABO, NGEE, ECOSTRESS and RRUFF. Remove redundant repository names,
file formats, license labels and opaque axis hashes from presentation names.
Keep repository or instrument qualifiers where they distinguish similar data.
Names are English and unique after whitespace normalization and case folding.

- Separate leaf/canopy, reflectance/transmittance, fresh/dried and instrument
  series where they identify distinct data. No dataset is merged by renaming.
- ECOSTRESS names identify material, native wavelength coverage in micrometres,
  channel count and, for otherwise ambiguous subsets, the number of **spectra**.
  These counts are observations, not inferred independent sample counts. Units
  come from the explicit native-unit warnings in each descriptor.
- ROD names distinguish native Raman grids using axis bounds and channel counts.
- OSSL names retain their collection identity, including separate LUCAS and
  LUCAS Woodwell records and each declared spectral modality.
- UCR/UEA records recover their native archive names from origin locators.
  Legacy NIR labels are not used to guess the physical modality.
- Unexpanded source labels such as `NHReflectance`, `NNReflectance` and `SPC`
  remain recognizable rather than receiving an unsupported interpretation.
- The NIST-origin quantitative IR subset keeps its historical `pnnl_quant_ir`
  ID; its display name follows the documented contributor. Original descriptions,
  quotations, filenames and origin titles remain unchanged as provenance.

The revised names average 44.7 characters (previously 52.0); the maximum is 78.
The crosswalk preserves every previous title and records the reason/evidence
basis. Existing consolidation/legacy-ID mappings remain valid because no ID,
URL, path, source ID, variable, repetition or sample identity changes.

## Apply and verify

```sh
python scripts/rename_dataset_displays.py          # Validate every row first
python scripts/rename_dataset_displays.py --write  # Apply and rebuild both indexes
python catalog/scripts/validate.py
pytest -q tests/test_display_names.py tests/test_manifest.py tests/test_profile.py tests/test_catalog.py tests/test_index.py
```

This maintenance command rejects unexpected current names and stale card metadata
or processing identities. It changes only descriptor `name`, card `identity.name`
and the card metadata hash. Existing Datasets renderers refresh the datasheet;
Croissant keeps its technical dataset-ID `name`. Numerical sections, content and
processing hashes, qualification dates and producer provenance are preserved.
Descriptor-only candidates remain unqualified. The operation is idempotent.

The crosswalk is historical traceability, not a runtime alias or an ID migration.
Before rerunning source `bootstrap`, review these manually curated titles: a
managed descriptor can be overwritten by bootstrap. Reapply the reviewed names
only after independently refreshing any changed source metadata; the rename
command deliberately refuses to conceal stale qualifications. Future title
revisions should append a new dated crosswalk rather than rewrite this history.

## Verification receipt

The [validation receipt](../../catalog/documentation/dataset-display-name-validation-20261105.json)
records the comparison against `e11031fce61d498d8e4ea46417e489199f067d07`:
242 unchanged IDs, 241 cards differing only in display name and metadata hash,
and both indexes differing only in name fields. Manifests, Croissant technical
names, numerical profiles, repetitions and qualification dates are unchanged.
The 83 owner regression tests pass, as do descriptor validation, Ruff and mypy.
The private library retains its official 241-record snapshot and passes 31 tests;
its assets, publications, resources and scientific relations are unchanged.
