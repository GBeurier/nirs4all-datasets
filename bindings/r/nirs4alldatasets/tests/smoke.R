# SPDX-License-Identifier: MIT
# Smoke test for the R binding (offline: resolve / verify / abi). Run after installing
# the package (see bindings/r/build_and_test.sh).
library(nirs4alldatasets)

index <- paste0(
  '{"schema":"1.0","n_datasets":1,"datasets":{"demo":{',
  '"tier":"public",',
  '"dataverse":{"instance":"https://dv.example","doi":"10.70112/ABC","dataset_version":"1.0"},',
  '"files":[{"name":"X.parquet","relpath":"canonical/sources/X.parquet","directory_label":"canonical/sources","sha256":"aa","size":9,"file_id":42}],',
  '"origins":[{"kind":"zenodo","mode":"canonical","locator":"10.5281/zenodo.5","access":"open"}],',
  '"retrieval":{"schema_version":"1.0","status":"raw_reproducible","routes":[{"id":"raw","method":"raw_retrieve","provider":"url","locator":"https://example.test/raw.csv","resources":[{"id":"raw","selector":{"kind":"direct_url","value":"https://example.test/raw.csv"}}]}]},',
  '"descriptor":{"id":"demo","retrieval":{"schema_version":"1.0","status":"raw_reproducible","routes":[]}}}}}'
)

# resolve -> a contract that mentions the tier + file id; trailing newline-free JSON.
contract <- n4ds_resolve(index, "demo")
stopifnot(is.character(contract), grepl('"tier"', contract, fixed = TRUE), grepl('"file_id":42', contract, fixed = TRUE))
stopifnot(grepl('"retrieval"', contract, fixed = TRUE), grepl('"raw_reproducible"', contract, fixed = TRUE))

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

if (requireNamespace("nirs4allio", quietly = TRUE) && requireNamespace("jsonlite", quietly = TRUE)) {
  gate_root <- file.path(tempdir(), "n4ds_r_io_gate")
  cache_dir <- file.path(gate_root, "cache")
  dataset_dir <- file.path(cache_dir, "demo")
  x_rel <- "canonical/sources/X.csv"
  y_rel <- "canonical/variables.csv"
  x_path <- file.path(dataset_dir, x_rel)
  y_path <- file.path(dataset_dir, y_rel)
  dir.create(dirname(x_path), recursive = TRUE, showWarnings = FALSE)
  dir.create(dirname(y_path), recursive = TRUE, showWarnings = FALSE)

  x_body <- "sample_id,w1,w2\ns1,1,2\ns2,3,4\n"
  y_body <- "sample_id,target\ns1,10\ns2,20\n"
  writeBin(charToRaw(x_body), x_path)
  writeBin(charToRaw(y_body), y_path)

  manifest <- list(files = list(
    list(name = "X.csv", relpath = x_rel, directory_label = "canonical/sources", sha256 = "8cb4ae7faf3d5b91287a9b24a6a8cc5f05e0056aaf81a682341f5b1962514b8d", size = nchar(x_body, type = "bytes"), file_id = NULL),
    list(name = "variables.csv", relpath = y_rel, directory_label = "canonical", sha256 = "29206e3a4c4aef9d106214dede0aed2a0f3485fd948ba02c353ff3d23e82a193", size = nchar(y_body, type = "bytes"), file_id = NULL)
  ))
  card <- list(
    identity = list(id = "demo"),
    sources = list(list(source_id = "X")),
    variables = list(list(name = "target", role = "target"))
  )

  index <- list(
    schema = "1.0",
    n_datasets = 1L,
    datasets = list(demo = list(
      tier = "public",
      dataverse = list(instance = "https://dv.example", doi = NULL, dataset_version = NULL),
      files = manifest$files,
      origins = list(),
      retrieval = list(schema_version = "1.0", status = "canonical_verified", routes = list()),
      descriptor = list(id = card$identity$id)
    ))
  )
  index_json <- jsonlite::toJSON(index, auto_unbox = TRUE, null = "null")
  contract <- n4ds_resolve(index_json, "demo")
  fetch_status <- n4ds_fetch(contract, jsonlite::toJSON(list(cache_dir = cache_dir), auto_unbox = TRUE))
  stopifnot(grepl('"cached"', fetch_status, fixed = TRUE))
  verify_status <- n4ds_verify_cached(contract, dataset_dir)
  stopifnot(grepl('"ok":true', gsub("[[:space:]]+", "", verify_status)))

  spec <- list(
    name = card$identity$id,
    sample_index = list(by = "id", key = "sample_id"),
    sources = list(
      list(
        id = card$sources[[1]]$source_id,
        role = "mixed",
        input = x_path,
        key = "sample_id",
        columns = list(
          list(role = "ignore", select = "sample_id"),
          list(role = "features", select = c("w1", "w2"))
        )
      ),
      list(
        id = "variables",
        role = "mixed",
        input = y_path,
        key = "sample_id",
        columns = list(
          list(role = "ignore", select = "sample_id"),
          list(role = "targets", select = "target")
        ),
        join = list(to = card$sources[[1]]$source_id, on = "sample_id", how = "1:1", coverage = "complete")
      )
    )
  )
  summary <- nirs4allio::nio_load(spec)
  stopifnot(is.list(summary), length(summary$blocks) >= 1L, summary$n_sources == 1L)
} else {
  message("R datasets -> io micro-gate skipped: install nirs4allio to enable it")
}

cat("R binding smoke OK\n")
