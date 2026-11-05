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

## Manual source review, 5 November 2026

`manual-source-review-20261105.json` records user-confirmed source publications
for JIGO8R manure, 6VYUQN Brassica tissue, RRUFF IR/Raman and blueberry phenomics.
Its binary evidence remains in the private documentary library.

`leaf-traits-compilation-origins-20261105.csv` restores the full source list:
37 original dataset IDs, 36 distinct original-source URLs and 47,393 compiled
rows. Martha's Vineyard and Harvard Forest share one repository URL and retain
their separate IDs. Dataset#30 has a copied name in the source CSV; its original
name is retained alongside the soybean title confirmed by Supporting Table S1.
This is a metadata review inventory. Existing runtime descriptors, spectral data,
qualification cards and source memberships are unchanged by that inventory.

The retained `zenodo_lyonia_petal_transmission_uvvisnir_wave3` is separately added
as a schema-valid descriptor and catalog entry. It documents the pinned Zenodo
origin, CC-BY-4.0 license and measured transmission block. Species and tissue
type remain metadata: the source does not declare an ML prediction task.
Canonical conversion, physical-sample grouping and numerical qualification
remain unqualified; no generated card or fabricated data hashes are supplied.

## Verified clarification and paired-source proposal

`clarification-review-20261105.json` records the next fifteen association
dispositions, source-specific replacements and three resolved published-edition
flags. Full evidence captures remain private. It distinguishes FLOPP constituent
provenance in FTIR (125 of 5,000 exported spectra) from parent OpenSpecy
documentation; no FLOPP provenance was found in the supplied Raman subset.
The 2017 Arctic canopy reference uses the published BG article while preserving
its EGUsphere preprint relation. Leaf-level references remain leaf-level context.
The bread matrix and the companion hyperspectral cube remain separate scopes.

`sierra-nevada-2023-paired-sources.json` is a concrete composition candidate:
83 declared sample keys; fresh 363 spectra/35 samples, freeze-dried 492/82,
oven-dried 498/83; 35 samples occur in all three sources. Physical sample keys
and source observation keys were checked against the pinned canonical source
Parquet hashes. Metadata checks found no conflicting sampling dates, plot IDs,
genera or nonmissing species for shared sample keys. Replicate indices and
spectral row positions do not establish cross-state pairings.

The existing owner composer was executed in isolated local staging and preserved
all three repetition counts. The delivered recipe records three X blocks and
their source bindings, original IDs and input hashes. Admission of this paired
collection across three preparation-specific EcoSIS deposits remains explicit
owner review; canonical materialization and numerical qualification have not run.
The three current runtime descriptors and qualified cards remain intact.

The association of `gcb.70246` with the three July-2023 preparation-specific
packages still needs an exact publication-to-deposit or training-input link.
Shared sites, authors and verified sample pairing do not establish paper use.
