<!-- SPDX-License-Identifier: MIT -->
# nirs4all-datasets — MATLAB / Octave binding

A thin MEX shim (`n4ds.c`) over the `nirs4all-datasets` C ABI (`n4ds_`). Resolve a
dataset id into its download contract, fetch the canonical Parquet with SHA-256
verification, and re-verify a cached directory — all from MATLAB or Octave.

```matlab
addpath('bindings/matlab');                 % n4ds + the +nirs4all_datasets package
index   = fileread('catalog/index.json');
contract = nirs4all_datasets.resolve(index, 'corn_eigenvector_nir');
status   = nirs4all_datasets.fetch(contract, '{"token":"…"}');   % JSON opts
report   = nirs4all_datasets.verify_cached(contract, jsondecode(status).dir);
```

## Build

Source distribution: download the `nirs4all-datasets-matlab-octave-<version>.zip`
GitHub Release asset (or this directory), then build against the prebuilt
`libnirs4all_datasets_capi`:

```bash
# from the repo root, with the Rust toolchain on PATH:
bash bindings/matlab/build_and_test.sh      # Octave: builds the capi, the mex, runs smoke.m
# or inside MATLAB/Octave, after setting N4DS_INCLUDE / N4DS_CAPI_DIR:
build                                        # build.m
run('smoke.m')
```

The same archive serves MATLAB (`mex`) and Octave (`mkoctfile --mex`, via `mex`).
