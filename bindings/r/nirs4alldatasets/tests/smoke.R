# SPDX-License-Identifier: CECILL-2.1 OR AGPL-3.0-or-later
# Smoke test for the R binding (offline: resolve / cache fetch / verify / abi). Run after installing
# the package (see bindings/r/build_and_test.sh).
library(nirs4alldatasets)

index <- paste0(
  '{"schema":"1.0","n_datasets":1,"datasets":{"demo":{',
  '"tier":"public",',
  '"dataverse":{"instance":"https://dv.example","doi":"10.70112/ABC","dataset_version":"1.0"},',
  '"files":[{"name":"X.parquet","relpath":"canonical/sources/X.parquet","directory_label":"canonical/sources","sha256":"aa","size":9,"file_id":42}],',
  '"origins":[{"kind":"zenodo","mode":"canonical","locator":"10.5281/zenodo.5","access":"open"}],',
  '"retrieval":{"schema_version":"1.0","status":"raw_reproducible","routes":[{"id":"raw","method":"raw_retrieve","provider":"url","locator":"https://example.test/raw.csv","resources":[{"id":"raw","selector":{"kind":"direct_url","value":"https://example.test/raw.csv"}}]}]},',
  '"descriptor":{"id":"demo","sources":[{"source_id":"X","modality":"NIR"}],"variables":[{"name":"target","role":"target","type":"numeric"}],"ids":{"sample_id":"sample_id"},"retrieval":{"schema_version":"1.0","status":"raw_reproducible","routes":[]}}}}}'
)

# resolve -> a contract that mentions the tier + file id; trailing newline-free JSON.
contract <- n4ds_resolve(index, "demo")
stopifnot(is.character(contract), grepl('"tier"', contract, fixed = TRUE), grepl('"file_id":42', contract, fixed = TRUE))
stopifnot(grepl('"retrieval"', contract, fixed = TRUE), grepl('"raw_reproducible"', contract, fixed = TRUE))
stopifnot(grepl('"descriptor"', contract, fixed = TRUE), grepl('"source_id":"X"', contract, fixed = TRUE), grepl('"role":"target"', contract, fixed = TRUE))

# an unknown id is an error.
err <- tryCatch({ n4ds_resolve(index, "nope"); FALSE }, error = function(e) TRUE)
stopifnot(err)

# verify_cached on an empty dir reports the file missing.
report <- n4ds_verify_cached(contract, tempdir())
stopifnot(grepl('"missing"', report, fixed = TRUE))

# retrieve_raw rejects non-automatic routes without network.
manual_request <- '{"dataset_id":"demo","route":{"id":"manual","method":"manual","provider":"manual","access":"manual","locator":"https://example.org"}}'
err <- tryCatch({ n4ds_retrieve_raw(manual_request, paste0('{"cache_dir":"', tempdir(), '"}')); FALSE }, error = function(e) TRUE)
stopifnot(err)

# prepare_raw shares the same route validation and rejects manual routes.
err <- tryCatch({ n4ds_prepare_raw(manual_request, paste0('{"cache_dir":"', tempdir(), '"}')); FALSE }, error = function(e) TRUE)
stopifnot(err)

# ABI version looks like semver.
stopifnot(grepl("^[0-9]+\\.[0-9]+\\.[0-9]+", n4ds_abi_version()))

# A cache hit exercises the fetch and successful verification C ABI paths without
# requiring an ambient R IO package or JSON parser.
cache_dir <- normalizePath(tempfile("n4ds-r-cache-"), winslash = "/", mustWork = FALSE)
dataset_dir <- file.path(cache_dir, "demo")
x_rel <- "canonical/sources/X.csv"
y_rel <- "canonical/variables.csv"
x_body <- "sample_id,w1,w2\ns1,1,2\ns2,3,4\n"
y_body <- "sample_id,target\ns1,10\ns2,20\n"
x_path <- file.path(dataset_dir, x_rel)
y_path <- file.path(dataset_dir, y_rel)
dir.create(dirname(x_path), recursive = TRUE, showWarnings = FALSE)
dir.create(dirname(y_path), recursive = TRUE, showWarnings = FALSE)
writeBin(charToRaw(x_body), x_path)
writeBin(charToRaw(y_body), y_path)

cache_index <- paste0(
  '{"schema":"1.0","n_datasets":1,"datasets":{"demo":{',
  '"tier":"public",',
  '"dataverse":{"instance":"https://dv.example","doi":null,"dataset_version":null},',
  '"files":[',
  '{"name":"X.csv","relpath":"', x_rel, '","directory_label":"canonical/sources","sha256":"8cb4ae7faf3d5b91287a9b24a6a8cc5f05e0056aaf81a682341f5b1962514b8d","size":', nchar(x_body, type = "bytes"), '},',
  '{"name":"variables.csv","relpath":"', y_rel, '","directory_label":"canonical","sha256":"29206e3a4c4aef9d106214dede0aed2a0f3485fd948ba02c353ff3d23e82a193","size":', nchar(y_body, type = "bytes"), '}],',
  '"origins":[],',
  '"retrieval":{"schema_version":"1.0","status":"canonical_verified","routes":[]},',
  '"descriptor":{"id":"demo","sources":[{"source_id":"X"}],"variables":[{"name":"target","role":"target"}]}}}}'
)
cache_contract <- n4ds_resolve(cache_index, "demo")
fetch_opts <- paste0('{"cache_dir":', encodeString(cache_dir, quote = '"'), '}')
fetch_status <- n4ds_fetch(cache_contract, fetch_opts)
stopifnot(grepl('"status":"cached"', gsub("[[:space:]]+", "", fetch_status), fixed = TRUE))
verify_status <- n4ds_verify_cached(cache_contract, dataset_dir)
stopifnot(grepl('"ok":true', gsub("[[:space:]]+", "", verify_status), fixed = TRUE))
unlink(cache_dir, recursive = TRUE)

cat("R binding smoke OK\n")
