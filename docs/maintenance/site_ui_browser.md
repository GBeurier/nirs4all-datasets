# Catalogue browser preview resources

The public `build_site(root, out) -> Path` and installed `n4a-datasets site` entrypoints
remain unchanged. Site building reads committed catalogue artifacts and package resources;
it needs no Node, npm, subprocess or UI build. Index and detail rendering are unchanged.

Only `catalog.html` loads the local classic `vendor/nirs4all-ui/nirs4all-ui-browser.iife.js`
and `browser.css`. One application/json block carries whitelisted `DatasetPreviewView`
values from public/anonymized catalogue entries. The initializer passes `{view, className}`
to the existing `Nirs4allUIBrowser.mountDatasetPreview`, without a `dataset` input or UI
inference. No card, descriptor, origin, credential, axis or split payload is serialized.
The existing `inline_json` helper is reused; its HTML-comment escape is corrected to
valid JSON (`\u003c`) so script-context text round-trips through `JSON.parse`.

Static headings, links, glyphs and filter/sort attributes remain host-owned. The static
preview remains visible without JavaScript, when the IIFE is absent, or when JSON parsing
or mounting fails. It is hidden only after the shared card is present in the DOM. Sorting
moves existing cards; there is no mount registry or lifecycle framework.

Counts accept declared integers, excluding booleans. Unknown values display as a dash;
zero remains zero. Unknown targets/sources match neither specific filter option. A
metadata-only badge requires a declared target count of zero. The preview labels spectral
variables without assuming wavelength units. The shared view uses three stats and a
declared-source badge; the static fallback retains its four stat cells. Shared badge
tones replace the fallback's tier badge colors and tier tooltip; the card tier stripe
and access explanation remain. The domain/family line follows the summary/glyphs in
the fallback so the preview can be hidden as one block.

Resource source: accepted `nirs4all-ui-0.2.2-local.20261107.1.tgz`, SHA-256
`2f9c7847886beefde05a661481b784b544dd36d1c003cea896c1a76659501b70`.
This is an unpublished local development artifact. Root stages byte-exact IIFE/CSS,
`LICENSE`, `LICENSING.md`, `THIRD_PARTY_NOTICES.md`, the complete `LICENSES/` tree and
`PROVENANCE.json` under `src/nirs4all_datasets/site/ui_assets/nirs4all-ui/`. Source authors
must not rebuild or modify these assets. The provenance file records package version,
archive SHA-256, publication state and each copied upstream file's SHA-256.

`_copy_ui_assets` copies the tree with `importlib.resources` Traversable reads, including
non-filesystem packages on Python 3.11. Missing required assets raise a packaging error.
Package inclusion must be checked through the existing wheel/site pipeline; source
placement alone is not evidence of wheel inclusion. No packaging settings were changed.

After source freeze, Root runs the existing site/anonymization tests plus lint/types,
the deploy-equivalent site build, wheel inclusion and installed CLI without Node. Root's
single browser wave covers HTTP and file URLs, shared mount count, title/stat visibility,
all filters/search/sort, JavaScript disabled, missing IIFE, invalid JSON and mount failure.
Record initialization time for the real catalogue; there is no performance threshold.
These checks were not executed by the source author.
