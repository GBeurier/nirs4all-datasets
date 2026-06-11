# nirs4all-datasets — point d'étape (2026-06-11)

Document de synthèse : objectifs, état actuel, ce qui vient d'être fait, ce qui reste.
Détail technique du design : [`PLAN-reference-bank.md`](PLAN-reference-bank.md).

---

## 1. Objectifs du repo (reformulation)

Une **banque de datasets NIRS de référence** — citable dans un papier, reproductible, orchestrée —
qui sert à benchmarker, comparer des modèles, explorer des techniques. Concrètement :

1. **Catalogue documenté en local**, mais le repo ne garde que le *nécessaire* (descripteurs +
   métadonnées + cartes) ; les **octets lourds vivent ailleurs** (Dataverse / sources d'origine).
2. **Téléchargement à la demande** : soit par identifiant connu (DOI / Zenodo / figshare / Dataverse),
   soit par **script d'acquisition** quand le dataset est ailleurs et doit être assemblé.
3. **License-aware** : certains datasets ne sont accessibles qu'avec token, ou pas redistribuables du
   tout (→ on documente la source, on ne republie pas).
4. **Diagnostics exhaustifs** par dataset + **traçabilité maximale** : hash, versions, chaîne
   origine → raw → canonique → carte, citations. Sérieux scientifique.
5. **Pull distant** depuis les *spots d'origine* OU depuis un **Dataverse perso** (pour les datasets
   licenciés).
6. **Anonymisation / normalisation en options** (au besoin).
7. **Page web** à jour (catalogue navigable), publiée.

---

## 2. Ce qu'on a actuellement

### Catalogue (git)
- **640 descripteurs** (`catalog/datasets/*.yaml`) = 484 (regression/classification/multimachines) +
  **164 v2.0** + 1 template − doublons. Tous schema-valides.
- **476 cartes d'identité** (diagnostics). Les **164 v2.0 sont catalogués mais sans carte** (génération
  dédiée à faire, voir §4) ; ils apparaissent sur le site avec le badge « card pending ».
- Index `catalog/datasets.yaml` + rapport de re-base `catalog/reconciliation.json`. **Site = 640 pages.**
- **0 dataset publié** sur Dataverse (aucun DOI perso minté — rien n'est encore en ligne sous notre nom).

### Données locales : `NIRS DB/` = **19 Go** (gitignoré, jamais committé)
| Sous-arbre | Taille | Statut |
|---|---|---|
| `regression/` | 11 Go | ✅ ingéré (409 leaves) |
| `classification/` | 1.6 Go | ✅ ingéré (75 leaves) |
| `multimachines/` | 614 Mo | ✅ ingéré (44 leaves, mono-source par instrument) |
| **`v2.0/`** | **2.8 Go** | 🟡 **catalogué (164 descripteurs depuis `dataset_card.json`) — cartes à générer (§4 P1)** |
| `chantiers/` | 2.5 Go | ❌ WIP (zips, rtbfoods) — écarté |
| `unusableDB/` | 772 Mo | ❌ écarté (datasets non utilisables / TODO) |
| `Publications/` | 110 Mo | PDF des papiers (non committés ; citations tirées des DOI) |

→ **484 datasets dans le catalogue** (après dédup `multimachines/CORN` = doublon de `regression/CORN`).

### Capacités de la lib (code)
- **Provenance first-class** : `descriptor.sources[]` (homes de données : dataverse/zenodo/figshare/
  url/script/manual) + `PublicationRef` (papiers). DOI classés par préfixe (data → sources, journal →
  citations).
- **`load()`** : local → Dataverse perso (DOI, public ou token) → **source d'origine ouverte**
  (canonique vérifié au hash ; raw via `reproduce=` qui ré-ingère, marqué *reproduit*) → message
  indiquant où récupérer. **Scripts jamais exécutés côté consommateur** (maintainer-only).
- **Hash split** : `descriptor_hash` (rebuild canonique) vs `metadata_hash` (rafraîchissement cartes).
- **Cartes** : stats publication-grade (PCA, shift train/test, qualité) + bloc provenance + chaîne de
  traçabilité (hashes origine→raw→canonique).
- **Page web** : site statique interactif, **déployé et live** sur GitHub Pages (484 datasets).
- **Publication Dataverse** : tout le plombing existe (`publish`/`grant`/`revoke`/`restrict`) mais
  testé en mock seulement, **jamais exécuté en vrai**.

---

## 3. Ce qui vient d'être fait (cette session)

- **Re-base complète sur `NIRS DB/`** : 254 → 484 datasets ; ancien catalogue tabpfn remplacé ;
  3 orphelins supprimés + 44 doublons écartés ; tout tracé dans `catalog/reconciliation.json`.
- **Provenance rendue actionnable** : extraction des DOI/URL depuis le master sheet, classés
  data-vs-papier (avant : planqués en texte libre). `instrument.model` rempli pour multimachines.
- **Fetcher multi-source** (`access.load`) + **split de hash** + **cartes enrichies** (provenance +
  traçabilité) + **bloc « Origin & citation »** sur le site (metadata-only → respecte les licences).
- **`bootstrap --prune`** (re-base reproductible) + garde-fou de publication (interdit de republier
  en open une source non-open).
- **Build de 476 cartes** (474 ok / 1 partial / 8 échecs = défauts de données source) + site régénéré.
- **Revue Codex (gpt-5.5) + agent Claude Fable** sur le plan ET le diff final ; Codex a attrapé un vrai
  bug (le `metadata_hash` non câblé) → corrigé + tests.
- **Green gate local vert** (ruff + mypy + validate 485 + pytest 136) ; **commit `6b4f24b` poussé** ;
  **page web redéployée**.

---

## 4. Ce qui reste à faire

### 🔴 Priorité 1 — Générer les CARTES de `v2.0/` (descripteurs ✅ faits)
**Fait :** les 164 packages `v2.0/` sont **catalogués** — `discover.build_v2_descriptor` lit le
**`dataset_card.json`** (structuré, Frictionless-style) de chaque leaf → `sources[]` (URLs officielles +
script `source_to_standard.py` maintainer-only), `related_publications`, **cibles correctes** depuis
`target_summary.target_variables` (jamais les colonnes métadonnées), `instrument`/multi-bloc depuis
`spectral_blocks`, et **governance honnête** (`public_release_allowed: false` → `restricted/internal`,
131 « private »). v2.0 gagne les 9 collisions d'id `timeseries`.

**Reste — la génération de cartes v2.0** : `write_canonical` échoue proprement aujourd'hui car `Y.csv`
mélange `observation_id` + métadonnées + cibles, et 4 leaves sont multi-bloc `X1/X2/X3` (FolderParser ne
les reconnaît pas). Il faut un **ingest v2.0 dédié** : sous-sélectionner `Y.csv` aux colonnes-cibles
déclarées (le reste → `M`), encoder les cibles classification, et construire la config multi-source pour
`X1/X2/X3`. Décision prise (validée) : ne **pas** générer de cartes tant que cet ingest n'est pas correct
(des stats fausses violeraient la rigueur). Les datasets restent affichés « card pending ».

### 🔴 Priorité 2 — Respect des licences (les 131 « private »)
Ne **jamais** publier en open les datasets `not_cleared`. Governance honnête (`visibility: restricted`,
`confidentiality_class: internal`), métadonnées-only sur le site, et un **check de compatibilité de
re-hosting** au moment de publier (déjà en place pour les sources non-open ; à étendre à v2.0).

### 🟠 Priorité 3 — Finir le mécanisme de download
- Câbler les **scripts d'acquisition maintainer** à partir des sections « Reproduce » de v2.0 (URLs
  officielles → fetch + checksum), pour les datasets re-téléchargeables.
- Tester le chemin **origine-ouverte → ré-ingestion** sur un vrai dataset Zenodo/figshare (jamais
  testé en réseau — uniquement en mock).

### 🟠 Priorité 4 — Publier sur le Dataverse perso (0 publié aujourd'hui)
Configurer le Dataverse (collection + token), **rehearsal sandbox** d'abord
(`demo.recherche.data.gouv.fr`), puis publier les datasets open (DOI), garder les licenciés en
restricted+token. Guide : `docs/PUBLISHING.md`.

### 🟡 Priorité 5 — Réparer les 8 échecs de build
Défauts de données source (X/Y désalignés : `rice_redox`×3, `wood_sustain` ; 4 ECOSIS avec `row_id`
dupliqué). Soit corriger la source, soit les exclure explicitement (documenté).

### 🟡 Priorité 6 — Anonymisation / normalisation (différé, optionnel)
Bloqué en amont : `write_canonical` jette aujourd'hui les fichiers `M` (sample ids + covariables, =
clé de jointure multimachines). Étape préalable : **persister les métadonnées en canonique** (opt-in),
puis drop/hash de colonnes piloté par descripteur. `normalise` = label d'unité seulement.

### 🟡 Priorité 7 — CI rouge (pré-existant)
`ci.yml` fait `pip install` qui ignore `[tool.uv.sources]` → le pin `nirs4all-io==0.1.0a0` (sibling
éditable non publié sur PyPI) ne résout pas. Options : publier `nirs4all-io` sur PyPI, ou faire
installer le sibling par la CI, ou détendre le pin. (Le déploiement Pages, lui, marche.)

### ⚪ Priorité 8 — Tri de `chantiers/` (2.5 Go) et `unusableDB/` (772 Mo)
Décider quoi récupérer (ex. `rtbfoods`) vs écarter définitivement.
