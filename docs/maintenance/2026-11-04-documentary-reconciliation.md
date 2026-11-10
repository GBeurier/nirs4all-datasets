# Local documentary reconciliation against the origin-record catalog

## Official baseline

The work starts at `03937ed490b7b955e17391b515363c4318e693a1`, not the old
October curation branch or the ecosystem's published 0.3.18 pin.
The 4 November commit consolidates 297 legacy records into 241 current datasets
(95 public, 146 private), retires 72 identifiers and requalifies the cards.
It also removes stale variable declarations and recognizes the documented
same-export keyless Y/M layout. No new independent-sample claim follows from
positional alignment.

Earlier October/November fixes include transitive target-derivation exclusion,
colliding variable aliases, consistent missing-value directives, cache identity,
LUCAS metadata, UCPH API references and publication-license metadata. The old
spreadsheet cannot override those current declarations.

## Documentary input

The supplied audit contains 298 historical rows. Current consolidation rules
resolve 297 of them to all 241 current datasets: 222 unchanged identifiers,
three case aliases, 52 composed members and 20 superseded views. The remaining
`zenodo_lyonia_petal_transmission_uvvisnir_wave3` entry is held outside the catalog
until its owner identity is established.

The compact [review inventory](../../catalog/documentation/enrichment-review-20261104.json)
contains 13 groups of source-bound documentary assertions for nine datasets.
It separates primary article/repository/package statements from title inference,
generated catalog declarations, historical scores and unresolved questions.
Eight cereal task exports do not become eight independent studies. Grapevine
preparation remains source-specific, and mosquito-cohort exclusions do not
automatically become current per-export exclusion counts.

The local bibliography and PDF collection are additional evidence candidates;
they do not make every legacy article–dataset link valid. Known mismatches,
including the forage article attached to mosquito exports, remain explicit.
Content-addressed files and presentation-page captures stay outside this public
repository, with private manifests preserving original filename aliases.

## Ownership and handoff

Owner: Datasets for identity, provenance and passport metadata. Domains consumes
only its existing `study-evidence.v1` interpretation contract, bound to current
dataset/content/source identifiers. Its historical numerical records are not
reassigned. No Methods, IO, Data, DAG, Preflight, Core or UI implementation changes
are proposed in this batch.

Both working branches are based on explicit official commits. The ecosystem's
25 submodule pins remain intact. A later passport-field admission and publication
`.n4a` implementation need their own reviewed field/consumer delta; this review
inventory grants no execution permission and invents no split, CV membership,
preprocessing sequence, fitted state or evaluation result.

Review source and target: `03937ed490b7b955e17391b515363c4318e693a1` plus the local
enrichment package hash recorded in the inventory. Rollback removes the additive
review files; no runtime descriptor, canonical content or historical result
requires reversal.
