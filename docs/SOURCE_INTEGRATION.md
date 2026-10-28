# CIRAD NIRS DB source integration

The October 2026 integration adds 133 datasets to the existing 164, using the
supplied standardized X/Y/M tables. The primary workflow is local access from
the registry checkout, followed by the nirs4all bridge:

```python
import nirs4all_datasets as bank

dataset = bank.get("barley_moisture_perten", root="/path/to/nirs4all-datasets")
spectra = dataset.x()
targets = dataset.y()
n4a_dataset = dataset.to_nirs4all()
```

The package catalog contains metadata and retrieval pointers; the heavy local
canonical data remain outside Git and the wheel. A consumer on another machine
needs the source bundle or an available origin route. Local use of the supplied
standardized data does not require the historical raw conversion scripts.

[`catalog/integration_validation.json`](../catalog/integration_validation.json)
records the local round-trip checks for all 297 datasets, with zero failed
datasets. The Python suite passes 272 tests; single-source and six-source
`to_nirs4all()` bridge checks also pass. The live origin health report records
HTTP 403 for the Lake Fire EcoSIS source; its supplied local tables remain
available.

The audited snapshot is the CIRAD [NIRS DB v2.0 folder](https://ciradfr-my.sharepoint.com/personal/denis_cornet_cirad_fr/Documents/NIRS%20DB/v2.0), synchronized locally for this integration. The folder may require CIRAD authorization; these files are not republished here. Dataset availability and permitted use remain governed by the source and individual catalog descriptors.

[`catalog/source_audit.json`](../catalog/source_audit.json) inventories all 297 standardized leaves. It records 133 IDs absent from baseline commit `e68d1befb6cb8245799e83d4b4e4c41e66287689`, relative leaf names, card and script fingerprints, table filenames, sizes, SHA-256 fingerprints and structural header details. It contains no table values or machine-specific paths. A leaf's presence establishes that a standardized bundle was supplied; it does not establish that its original raw source is downloadable or reproducible.

All 297 leaves contain `source_to_standard.py`. Static inspection finds 255 scripts referencing 50 distinct `convert_*.py` files absent from the supplied source tree. The audit lists each reference and each missing filename. This is a filename-based dependency inventory, not execution or a complete analysis of Python imports. The other 42 scripts are not thereby certified self-contained. The locally available standardized tables remain importable subject to their format and rights, but these missing files prevent independently reconstructing the affected standardized bundles from their original raw sources with the supplied wrappers. No wrapper is executed automatically.

The inventory also identifies 116 nonempty `Y.csv` tables without an
`observation_id` header. Import retains their paired X/Y/M layout only when
row counts match and X/M observation order agrees, and records the Y/M pairing
assumption in provenance and conversion warnings. This preserves the supplied
values without independently establishing their physical sample alignment.

For 22 datasets, repeated source sample IDs have differing target or metadata
values. Those datasets use observation IDs as canonical keys and preserve the
source sample IDs as `original_sample_id` metadata, so the sample-level table
does not discard observation-specific values. Consistent repeated samples keep
their source identity mapping. Native micrometer axes remain numerically
unchanged and their original unit is documented in provenance.

To regenerate the audit against the same baseline, from the repository root:

```bash
python catalog/scripts/source_audit.py 'NIRS DB' --baseline e68d1befb6cb8245799e83d4b4e4c41e66287689 --out catalog/source_audit.json
```

The audit reads and hashes local files and does not access the network.

## Paths for using the collection

- `n4a-datasets bootstrap 'NIRS DB'` derives catalog descriptors from local standardized cards; it does not download data or run converters.
- `n4a-datasets build-all --source-tree 'NIRS DB'` uses the local standardized tables to build canonical files and cards for catalog entries. Review the generated `bulk_report.json` for warnings and failures.
- `n4a-datasets retrieve ID` uses documented retrieval routes to fetch available bytes and may prepare them. A successful raw download or preparation does not guarantee a complete dataset-level canonical conversion. Manual or restricted routes require the access and terms described in the catalog.
- `n4a-datasets import-standardized 'NIRS DB/v2.0/LEAF' ID --root . --out /path/to/dataset` converts a bundle the user already possesses to a local `canonical/` directory. It checks the normalized card ID against the descriptor, leaves existing canonical data untouched, reports partial-conversion warnings, and runs no scripts. It does not build a manifest, qualify a card, update the catalog, or assert that the original raw data can be reproduced.

The same explicit local operation is available as `nirs4all_datasets.reproduce.import_standardized(leaf_dir, descriptor, out_dir)`, returning a `CanonicalResult` with status and warnings. The standardized layout and canonical writer have their own documented limitations; consult warnings, especially when source and declared blocks or identifier columns differ. Use `nirs4all-datasets[io]` and `assemble()` for compatible raw formats through nirs4all-io; inference from arbitrary origin files is not guaranteed to reproduce a particular standardized bundle.
