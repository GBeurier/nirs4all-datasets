# Third-Party Notices — nirs4all-datasets

`nirs4all-datasets` is distributed under `CeCILL-2.1 OR AGPL-3.0-or-later` (plus an optional
commercial license; see [`LICENSING.md`](LICENSING.md)). It relies on the third-party
open-source components listed below.

The Python dependencies below are installed separately from their official distributions;
their licenses are acknowledged here as a courtesy and
for compliance. Licenses are reported on a best-effort basis; the authoritative text
always ships with each upstream project (linked).

## Bundled catalogue browser UI

The static catalogue progressively mounts the real `DatasetPreviewCard` from the locally
accepted `nirs4all-ui` version `0.2.2-local.20261107.1`. This is an **unpublished local
development artifact**, not a registry release. Its IIFE, CSS, upstream notices and license
tree live in [`src/nirs4all_datasets/site/ui_assets/nirs4all-ui/`](src/nirs4all_datasets/site/ui_assets/nirs4all-ui/)
and are copied unchanged to the generated site's `vendor/nirs4all-ui/` directory.

The UI is licensed under `CeCILL-2.1 OR AGPL-3.0-or-later`, with an optional commercial
license described in its bundled `LICENSING.md`. The browser IIFE includes **React 19.2.7,
React DOM 19.2.7 and Scheduler 0.27.0**, under MIT, copyright Meta Platforms, Inc. and
affiliates. Their exact notices are retained in the UI's `THIRD_PARTY_NOTICES.md` and
`LICENSES/THIRD-PARTY/{react,react-dom,scheduler}.LICENSE.txt`. Retain these files when
redistributing the site. `PROVENANCE.json` records the accepted archive and file hashes;
see [the source maintenance notes](docs/maintenance/site_ui_browser.md).

## Separately installed Python dependencies

| Component | License (SPDX) | Copyright | Upstream |
|---|---|---|---|
| `numpy` | BSD-3-Clause | Copyright (c) 2005-2025, NumPy Developers | https://github.com/numpy/numpy |
| `scipy` | BSD-3-Clause | Copyright (c) 2001-2025, SciPy Developers | https://github.com/scipy/scipy |
| `pandas` | BSD-3-Clause | Copyright (c) 2008-2025, pandas Development Team | https://github.com/pandas-dev/pandas |
| `pyarrow` | Apache-2.0 | Copyright Apache Arrow Developers | https://github.com/apache/arrow |
| `pydantic` | MIT | Copyright (c) 2017-present Pydantic Services Inc. and contributors | https://github.com/pydantic/pydantic |
| `pyyaml` | MIT | Copyright (c) 2006-2025 PyYAML contributors | https://github.com/yaml/pyyaml |
| `jsonschema` | MIT | Copyright (c) 2013 Julian Berman | https://github.com/python-jsonschema/jsonschema |
| `python-dotenv` | BSD-3-Clause | Copyright (c) 2014 Saurabh Kumar | https://github.com/theskumar/python-dotenv |
| `matplotlib` | Matplotlib License (PSF-based, BSD-compatible) | Copyright (c) Matplotlib Development Team | https://github.com/matplotlib/matplotlib |
| `requests` | Apache-2.0 | Copyright Kenneth Reitz and the Python Software Foundation | https://github.com/psf/requests |
| `typer` | MIT | Copyright (c) 2019 Sebastian Ramirez | https://github.com/fastapi/typer |

## Bundled license-family texts (`LICENSES/`)

- `LICENSES/Apache-2.0.txt` — Apache-2.0
- `LICENSES/BSD-3-Clause.txt` — BSD-3-Clause
- `LICENSES/MIT.txt` — MIT
