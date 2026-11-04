# Documentary enrichment review

This directory holds **review candidates**, separate from the authoritative
runtime descriptors in `catalog/datasets/` and their generated cards.
It is not a new dataset schema, provider, qualification engine or public sidecar API.

`enrichment-review-20261104.json` reconciles a local 298-entry documentary audit
against official commit `03937ed490b7b955e17391b515363c4318e693a1` (241 datasets).
The current owner's `consolidation.json` supplies the identity mapping.
The original 72 retired identifiers remain provenance, rather than new aliases
that make old observations or results silently interchangeable.

The 13 claim groups cover nine current datasets. Each preserves the primary URL,
evidence level, original evidence IDs, legacy member/content context, explicit
current source mapping and limitations. Unknown fields are null. An absent
source mapping requires review; it is not broadcast to every instrument.
The publication RMSECV statement remains documentary and does not become an
independent-test score. The 1,183 historical Domains scores are not migrated.

## Review and integration

1. Check each claim against its original methods or repository documentation.
2. Confirm its scope within the current source and content version, including
   preparation, averaging, repeated measurements and variable names/units.
3. Admit reviewed fields through the existing descriptor/curation owner, then
   regenerate and qualify artifacts through that owner's actual data path.

Existing descriptors, native partitions, variables and generated numerical
profiles are deliberately not rewritten by this review inventory. In particular,
neither cache hashes nor qualification timestamps are advanced to pretend that
the current consolidated data were rebuilt from the old audit.

PDFs and HTML captures remain in an access-controlled documentary archive.
There are no copyrighted PDFs, full-text copies, raw/canonical data, workbook
snapshots, credentials or local absolute paths in this review delivery.

Sparse publication `.n4a` records await the agreed fields. Core owns the container;
Repository owns recipe/bundle publication; Datasets owns source metadata;
Domains owns source-study interpretation and evaluation limits. A paper citation
does not constitute an executable or validated pipeline.
