# Scientific qualification and its provenance

Datasets owns ingestion, provenance, canonical identity, cards and caches. Methods owns reusable
numerical kernels, Preflight owns intrinsic assessment, and Domains owns task/split assessment with
its fitted reference. Python-only legacy cards remain supported during this transition. Installing
Datasets does not require an unpublished native provider.

## Interpretation, measured values and possible causes

A diagnostic signature is a weighted heuristic. **0.78 does not mean a 78% probability of a physical
cause.** Values, evidence coverage and unavailable reasons are kept separately from the possible
interpretation. A low signature is not certification that the acquisition was valid. Confirming a
cause requires external acquisition/protocol evidence; Datasets does not manufacture that evidence.

RMS/SAM in the historical intrinsic profile compare to the **mean spectrum of this dataset**, not an
independent measured white/blank reference. Investigate the actual white/dark reference records,
instrument/probe/geometry, campaign, preprocessing/resampling history and the documented meaning of
repeated IDs before drawing a physical conclusion. These checks are included in JSON and displayed
with the possible causes.

The exploratory `vera25_like` rule is disabled in generic reports. Explicit use of
`diagnostic_hypotheses(profile, domain_context="VERA25")` or
`build_card(..., diagnostic_domain="VERA25")` enables that context; its specificity and causal
confidence remain `unvalidated`. Anonymized cards withhold that context and its specific suggestion.

## Historical proxies have explicit names

| Canonical name | Historical compatibility key | Actual meaning |
| --- | --- | --- |
| `noise.roughness_sigma_proxy` | `noise.noise_rms` | Median per-spectrum robust second-difference scale, with the historical 1.4826 / sqrt(6) normalization. |
| `noise.roughness_signal_to_noise_proxy` | `noise.snr` | Mean absolute input signal divided by that roughness proxy. This is not repeat-measured instrument SNR. |
| `noise.roughness_signal_to_noise_proxy_db` | `noise.snr_db` | 20 log10 of the historical proxy ratio. |
| `noise.bandwise_roughness_signal_to_noise_proxy_min` | `noise.bandwise_snr_min` | Minimum finite bandwise ratio using the historical across-observation second-difference scale. |
| `noise.bandwise_roughness_signal_to_noise_proxy_median` | `noise.bandwise_snr_median` | Median finite bandwise proxy ratio. |
| `structure.knn_distance_ratio_p95` | `structure.local_outlier_factor_p95` | P95 of mean k-neighbour PCA-score distance divided by its population median. It is **not Local Outlier Factor**. |

Old keys remain readable and their stored numbers are retained. New names are additive aliases, not
substitutions of a different algorithm. A genuine native LOF belongs to a separate metric/protocol;
it must not silently replace the distance-ratio value. Native mask/population/normalization
semantics are not inferred from a similar name.

## Complete migration inventory

`nirs4all_datasets.qualify.migration_inventory()` returns the packaged
{download}`machine-readable inventory <../src/nirs4all_datasets/qualify/metric_inventory.json>`.
It covers source diagnostics, variable statistics, task-dependent shifts, plotting representations,
heuristic axes, and each diagnostic rule. Every entry records its exact definition/return expression,
implementation and local helpers, source fingerprint, scope, current/target owner and one action:
`keep metadata`, `delegate`, `migrate`, `replace`, or `deprecated`. Native implementations remain with
the producer; their engine/protocol version and native execution receipt provide the version binding.

The inventory is generated without running kernels:

```bash
python scripts/generate_metric_inventory.py
pytest tests/test_metric_inventory.py
```

Tests reject a stale inventory or an unclassified public metric implementation. `migrate` or
`delegate` describes the transition owner; it does not falsely claim parity or native availability.
Exact matching populations, masks, views, imputation and protocol are prerequisites to a numerical
comparison. Historical median imputation, PCA truncation, kNN score space, and roughness aggregation
must stay explicit when an owner protocol differs.

## Optional assessments and a real producer chain

The `assessments.json` sidecar is optional and excluded from canonical content identity. Its versioned
records bind dataset/content, producer/engine/protocol, source, view and population/context. Task
records additionally identify target, split, fitted population and evaluated population. Unavailable
values are null with a reason; booleans/text are not silently coerced into numbers. The original
native report and native per-metric fields are retained losslessly in the local sidecar.

The native Preflight CLI accepts its canonical input DTO, prepared from the same immutable source
and explicit identities/partition roles. A producer invocation can then be attached without moving
its scientific kernels into Datasets:

```bash
n4pf analyze input.json --methods-library /verified/libn4m.so > report.json
n4pf extract-assessment report.json context.json > assessment.json
```

`context.json` identifies the canonical content hash, source, actual population and context; it must
not rebind a report from another input. The hash is obtained with
`qualify.assessments.canonical_content_hash(dataset_dir)`. Keep the input and execution hashes with
the native report. An observation count alone is not evidence that its values or identities align.

```python
import json
from nirs4all_datasets.qualify.assessments import write_assessments
from nirs4all_datasets.qualify import build_card

report = json.load(open("assessment.json", encoding="utf-8"))
write_assessments(dataset_dir, descriptor.id, [report])
card = build_card(dataset_dir, descriptor, assessment_mode="shared")
```

For example, native `integrity.missing_cells` is consumed as a **count** with its original
`native_metric.denominators.n_cells`. It is not relabelled as the legacy NaN ratio: a native validity
mask can exclude a finite cell too. Unknown native IDs remain in the assessment rather than being
assigned a scientifically different legacy meaning. Missing owner values are not refitted using
legacy PCA/QC/XY kernels.

Several engine versions or contexts may coexist in the cache. Card generation rejects ambiguity;
select explicitly, for example
`assessment_selector={"engine_version": "0.1.1", "population_id": "development_real"}` and
`assessment_view="native"`. The selected population/view is retained in profile provenance.
Intrinsic cards contain only the selected intrinsic reports. Task/Y-test-dependent reports remain
in the separate sidecar and `NirsDataset.assessments()` API; they do not enter an intrinsic summary.
Anonymized public cards withhold report identifiers, free text, detailed findings and selectors.

## Protocol migration

Presentation/diagnostic protocol 7 makes these distinctions explicit. Previous cards remain
readable; reading a legacy `card.json` does not overwrite it or its canonical bytes.
`migrate_profile_metadata(profile, from_protocol="6")` performs an explicit, idempotent labels and
signature migration while preserving old raw numerical fields. It runs no raw scientific kernel.
Fresh calculations also refuse to make a repeat group from empty, null or non-finite identities;
literal scientific IDs such as `NA` remain valid. This is separate from claiming that an ID denotes
an independent physical preparation or a technical repeat.

The protocol6/protocol7 golden fixture protects old numbers, new proxy identifiers and the explicit
migration marker. Real native integration tests separately verify the producing executable, input,
content binding, count/denominator and card projection. Neither kind of test is presented as a new
benchmark task or as evidence of causal calibration.

The full native report can include other sources and task/test metrics. It stays
lossless in the optional sidecar/API; intrinsic cards contain only selected
intrinsic metric/view evidence and a sidecar reference plus canonical-JSON SHA-256.
They never embed the unfiltered report. Native metric source, target, view,
population and protocol identities must agree with the selected envelope.

Metric identity includes exact native parameters and denominators (strict canonical sorted JSON),
so instrument and campaign factors can coexist under one metric ID. Projection
refuses two measurements targeting the same legacy scalar slot in a selected view;
it never chooses by order or silently replaces one protocol/parameter context.

The optional producer `metric_context_id` is an opaque `sha256:<64hex>` identity
bound by the producer to its canonical parameter/denominator object. Legacy
reports without it remain valid. The consumer retains the exact native context
alongside that ID: changing an opaque ID cannot bypass duplicate detection, and
reusing one ID for two different native contexts is rejected. The consumer does
not invent a cross-language hash serialization or claim to revalidate the
producer's digest from a different floating-point JSON formatter.

Only explicit `(producer, metric_id, metric_protocol)` bindings can populate a
historical scalar slot. The initial qualified binding is Preflight
`integrity.missing_cells` protocol `0.1.0`; its native count/mask/denominator were
compared independently. A matching name under another protocol or producer is
not equivalent. Unmapped values stay lossless and consultable under their real
identities in assessments; projection provenance lists the bindings actually used.
No unmapped value invokes a legacy numerical kernel.

Task assessments belong to Domains and require distinct declared fit/evaluation
populations. Preflight and Methods evidence cannot be relabelled as an independently
fitted task assessment by adding target/split strings.

The committed fleet was explicitly migrated with
`python scripts/migrate_card_protocol7.py --root .`: protocol-7 presentation,
historical raw calculation protocol 6, unchanged raw fields/manifests/dates.
The same command is idempotent. This does not relabel existing canonical curation
1.0 caches as 1.1; rebuilding an import applies the newer curation rules.
