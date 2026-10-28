# Loading public datasets from their origins

Install `nirs4all-datasets` and call `get()` from any directory. The wheel contains
the catalog and the recipes for all 135 public datasets; a repository checkout,
the CIRAD source bundle, and historical `convert_*.py` files are unnecessary.

```bash
pip install 'nirs4all-datasets[nirs4all]'
```

```python
import nirs4all_datasets as bank

dataset = bank.get("barley_moisture_perten")
X = dataset.x()
y = dataset.y()
model_data = dataset.to_nirs4all()
```

`get()` downloads original resources from the recorded providers, reads them
with the existing native readers or table libraries, joins their identifiers,
and writes local canonical Parquet. The cache retains original resources and
an `origin-pull.json` record with stable origin URLs, runtime layout, warnings,
and output checksums. Cached canonical files are checked before reuse.
Original sample identifiers and native partitions are retained where available.
No dataset bytes are hosted by this project.

There are 133 recipes without a personal-profile requirement, and two Harvard
malaria recipes requiring explicit guestbook responses. Provider availability,
terms, and rate limits still apply. HTTP 429 is retried with backoff; if the
provider continues refusing requests, the exception is reported to the caller.
Source archives may be large: the ChEMBL resource is approximately 5 GB.

## Optional Harvard guestbook profile

For the two malaria datasets, pass your own answers using `guestbook_response`.
Without them, the package reports the required fields before submitting a
guestbook response. It never invents an identity or prompts interactively inside
the Python API. Other datasets do not require this argument.

Create a local JSON file containing the Harvard `guestbookResponse` object:

```json
{
  "name": "YOUR NAME",
  "email": "YOUR EMAIL",
  "institution": "YOUR INSTITUTION",
  "position": "YOUR POSITION",
  "answers": [
    {"id": 231, "value": "YOUR INITIALS"},
    {"id": 510, "value": "Other"},
    {"id": 509, "value": "YOUR INTENDED USE"}
  ]
}
```

Check the original [guestbook schema](https://dataverse.harvard.edu/api/guestbooks/293)
for current choices and requirements. These responses are sent to Harvard only
when you explicitly request the corresponding download; they are not written
to the provenance record. Keep your profile file outside version control.

```python
import json
from pathlib import Path

profile = json.loads(Path("my-guestbook.json").read_text())
dataset = bank.get("malaria_anopheles_gambiae_oocyst_nir", guestbook_response=profile)
```

The CLI accepts the same object with `--guestbook-response my-guestbook.json`.
The Harvard forage archive has an optional-only guestbook and accepts empty
answers without personal information.

## Representation and scientific corrections

Fresh assembly preserves the original tables and is not promised to reproduce
the bytes of old standardized exports. Historical canonical checksums are not
used to certify a newly assembled representation.

- ChEMBL provides frequencies and IR/Raman peak intensities, without a
  trustworthy broadening parameter. The recipe exposes padded native peak lists
  for 50,000 molecules, with mode index as the source axis and exact frequencies
  in metadata. It does not generate an assumed broadened 512-point spectrum.
  Five inherited annotation fields absent from the SQLite resource remain null:
  compound name, molecular formula, InChI, InChIKey, and compound class.
- PMMA measurements describe 50 and 73 micrometre film thicknesses. The target is
  `film_thickness_um`; the original files do not provide sample temperatures.
- The Fairdata cartilage recipe joins zero-padded sample IDs to their targets;
  targets are not silently replaced with missing values.
- Original additional or unlabeled observations are retained: tree tissue
  1,270, tree girdling 2,737, sea cucumber 62, and coffee drying 76. Gastropod
  spectra retain the union of 2,482 original wavelengths with missing values
  where an observation did not measure a wavelength; no interpolation is added.

The packaged recipes assemble datasets in Python. Rust, C, R, and WASM clients
can inspect the same catalog and use native acquisition contracts; these clients
do not execute the Python dataset recipes.
