# R binding platforms

The native R package compiles the acquisition core with its normal `net` and
`prepare` features. HTTPS keeps the native ureq/rustls transport and certificate
verification. Windows Rtools uses its declared Rust target; R-universe's
`CARGO_BUILD_TARGET` is authoritative for ARM64 builds.
The GNU Windows target retains `libgcc`; the LLVM gnullvm target links
`libunwind`, matching Rust's target-specific native static-library contract.

WebR (`wasm32-unknown-emscripten`) retains descriptor resolution, the virtual
filesystem cache, SHA-256 verification and local raw-file preparation through the
same Rust readers. `n4ds_fetch` can reuse verified files already in the cache.
Blocking native HTTP is unavailable in the browser: a request that needs network
access fails explicitly with the existing HTTP error status, before sending any
request or credentials. Stage files with the host's browser transport first,
then verify or prepare those files locally. No unverified HTTP fallback is used.
This does not add a browser download API or change the separate npm WASM binding.

The WebR R build passes Cargo an explicit Emscripten target and links the static
library from that target's subdirectory inside the private build directory. It
does not depend on the wrapper copying artifacts into a flattened `./target`.

To exercise the actual WebR-target C ABI without R, build the self-contained R
source package's `src/rust` workspace for `wasm32-unknown-emscripten` with its
vendored dependencies, then link `tests/emscripten_smoke.c` with that static
library using Emscripten. From this directory:

```sh
emcc tests/emscripten_smoke.c -I../../crates/nirs4all-datasets-capi/include \
  /path/to/wasm32-unknown-emscripten/release/libnirs4all_datasets_capi.a \
  -sALLOW_MEMORY_GROWTH=1 -sEXIT_RUNTIME=1 -o /tmp/n4ds-webr-smoke.js
node /tmp/n4ds-webr-smoke.js
```

The smoke verifies missing/valid/corrupt cache entries, cache-only fetch,
credential-free network refusal and actual CSV preparation. It deliberately
refuses a native build. The full R package checks remain a separate gate.
