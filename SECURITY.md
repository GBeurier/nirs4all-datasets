# Security policy

## Scope

`nirs4all-datasets` is a **catalog** that downloads curated, DOI-pinned NIRS/spectroscopy
reference datasets on demand (via the `n4a-datasets` CLI / Python API) from public research
data repositories (Recherche Data Gouv / CIRAD Dataverse). It does not execute downloaded
content; it materializes data files and hands them to `nirs4all` / `nirs4all-io`.

Security-relevant properties:

- **Downloads are integrity-checked.** Each dataset is pinned by DOI and verified against a
  recorded checksum; a mismatch aborts the acquisition rather than using the bytes.
- **No arbitrary code execution.** The catalog reads data/metadata files only.
- **No secrets.** Public datasets are fetched over HTTPS; no credentials are required or stored.

Treat downloaded datasets according to their own licenses (see each dataset's identity card /
datasheet). Do not commit large downloaded artifacts back into the repository.

## Reporting a vulnerability

Please report security issues **privately** — do not open a public GitHub issue. Email
**nirs4all-admin@cirad.fr** with a description, affected version, and reproduction steps. We aim
to acknowledge within a few working days and will coordinate a fix and disclosure timeline.
