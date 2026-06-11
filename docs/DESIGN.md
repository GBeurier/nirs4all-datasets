# Design — banque de datasets NIRS de référence

*v1 — reformulé d'après tes annotations. Document de référence pour repenser le projet, avant l'analyse
et l'implémentation complètes. Annote / corrige librement.*

---

## 1. Vision

Une **base de données versionnée et qualifiée de datasets NIRS bruts**, **cataloguée et liée à ses
sources** (on ne republie jamais l'open data des autres — on pointe vers l'origine). Trois livrables :

- un **catalogue** (descripteurs + cartes d'identité + index) — dans git, léger ;
- une **page web** — navigation, cartes d'identité, dataviz ;
- un **plugin Python** — `import …` / `….get("nom")` pour récupérer un dataset (ou ses métadonnées) en
  local.

Les **octets vivent à leur source** ; git ne porte que métadonnées + cartes + index. Tout est **hashé et
versionné**. Un **pipeline d'ajout/qualification** fait croître et évoluer la base.

But ultime : pouvoir **citer, benchmarker, comparer, explorer** sur une base sérieuse et reproductible —
des datasets allant de **X seul** à **X + Y** à **X + Y + métadonnées**.

---

## 2. Un dataset = la réalité mesurée (brut, first-class)

Un **dataset** n'est **pas** une tâche de benchmark (un choix Y+split). C'est la donnée brute, gardée
**le plus brute possible**. Il contient :

| Élément | Règle |
|---|---|
| **X** — 1..n **sources** | une source = un instrument / une acquisition, **gardée séparée** (jamais fusionnée ni ré-échantillonnée), axe natif propre (nm / cm⁻¹ / µm / …). Un dataset peut être **multi-sources** (plusieurs X), et les sources peuvent être de **tailles différentes** — voir la note ci-dessous. (nirs4all-formats / io ajoutés *au besoin* pour lire les formats vendeurs et lancer les métriques.) |
| **Variables (Y + métadonnées)** | **aucune différence intrinsèque.** Si la source déclare des cibles → on les marque. Sinon **toute colonne est un Y potentiel**. Multi-cible, types mixtes, **jamais séparés**. Si aucun Y déclaré, on en désigne un (colonne de métadonnée) et **on le renseigne**. |
| **id d'échantillon** | `observation_id`, etc. — index, jamais un Y. |
| **métadonnées** | **toutes conservées**, sans a priori ni traitement pour l'instant. |
| **splits / folds** | **aucun par défaut.** Gardés *uniquement si la source les définit* (train/test, folds, voire plusieurs versions) et alors **renseignés**. |

Couverture : **X seul** · X + Y · X + Y + métadonnées. Le plugin sait restituer **avec ou sans split**
(concaténé par défaut).

**Multi-sources & répétitions (structurant).** Comme les Y, les **X peuvent être multiples** (dataset
multi-sources : plusieurs instruments / acquisitions). Chaque source est gérée **indépendamment** — pas
de fusion, pas de ré-échantillonnage, pas de grille commune imposée. Surtout : à cause de **répétitions
spectrales asymétriques** (un échantillon scanné un nombre variable de fois selon la source), **les
sources peuvent avoir des nombres de spectres différents** — elles ne sont **pas alignées ligne à
ligne**. Implications :

- chaque source porte sa propre dimension `(n_spectres × n_longueurs d'onde)` et son propre indexage de
  répétitions ;
- l'**alignement** entre sources, et avec les Y / métadonnées, se fait **par identité d'échantillon
  (id), jamais par position de ligne** ;
- pipeline, carte (stats **par source**) et plugin **préservent** cette structure (jamais aplatir ni
  aligner de force) ; le plugin restitue les sources séparément et peut, sur demande, concaténer les
  répétitions ou ne renvoyer qu'une source.

---

## 3. Gouvernance & visibilité — 3 tiers

On **catalogue tout**. Ce qui varie : ce qu'on **montre** et ce qu'on **exporte**. Le **bon token**
(dans le plugin) débloque l'accès complet.

| Tier | Page web — métadonnées & métriques | Export des octets (plugin) |
|---|---|---|
| **public** | tout, nommé | **oui, pour tous** (depuis l'origine) |
| **privé** | tout, nommé | **token requis** (Dataverse privé) |
| **anonymisé** | métadonnées **non nommées** + **Y normalisés** (métriques sur données anonymisées) | **token requis** |

- Datasets dont la **source n'est pas automatisable** → déposés dans un **Dataverse privé**,
  récupérables au token (pas de publication ouverte de notre part).
- L'anonymisation (tier le plus protégé) masque les noms de variables et normalise les Y : on publie des
  métriques **sans révéler** les valeurs/identités réelles.

---

## 4. Architecture

```
  sources d'origine (DOI / URL / Dataverse privé)
                    │  (testées régulièrement ; si une origine tombe → bascule Dataverse privé)
                    ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  PIPELINE d'ajout / qualification  (script ré-exécutable)     │
  │  ingest brut (nirs4all-formats/io)  →  métriques  →  carte    │
  └─────────────────────────────────────────────────────────────┘
                    │ écrit / met à jour
                    ▼
        git :  descripteurs + cartes d'identité + index        (octets jamais dans git)
                    │
        ┌───────────┴───────────────────────────┐
        ▼                                        ▼
   page web  (cartes + dataviz, par tier)   plugin Python  ….get("nom")
                                            (DL local ; token = accès complet ; avec/sans split)
```

- **Catalogue (git)** — un descripteur + une carte par dataset, + index. Source de vérité légère.
- **Pipeline d'ajout/qualification** (un script) — (1) enregistre un nouveau dataset brut, (2) calcule
  les métriques → carte d'identité, (3) **met à jour la page web + les fichiers du plugin**.
  **Ré-exécutable** : quand le protocole de métriques évolue, on relance pour **mettre à jour les
  anciennes cartes** sans toucher aux données.
- **Page web** — catalogue navigable, cartes, **dataviz sur X, Y et métadonnées**, en respectant les
  tiers.
- **Plugin Python** (ce package) — `….get("nom")` télécharge le dataset en local (origine → cache ;
  token → privé/anonymisé) ; donne aussi accès aux **métadonnées / infos de carte** ; lit les bruts via
  **nirs4all-formats** ; restitue avec ou sans split.

---

## 5. Provenance, intégrité, versions, évolution

- **Provenance** — source(s) d'origine (DOI/URL + mode : open / token / manuel / script) ;
  **publications** liées (papiers) référencées, mais distinctes des sources de **données**.
- **Intégrité** — chaîne de hashes **origine → raw → canonique → carte**.
- **Versions (2 axes proposés)** — (a) **version de contenu** du dataset : bump si les octets changent ;
  (b) **version du protocole de métriques** : bump quand on enrichit les métriques → re-qualification
  sans changer le contenu. *(à valider)*
- **Résilience des origines** — origines **testées régulièrement** ; si une origine tombe → le dataset
  bascule sur le **Dataverse privé**.
- **Évolution** — les datasets viennent d'un **OneDrive** ; le pull évoluera, `chantiers/` + `unusable/`
  **migreront** dans l'existant, des **itérations de versions** sont attendues. ⇒ le pipeline (§4) doit
  fournir un **mécanisme d'ajout** robuste + hash/versions, conçu pour cette évolution.

---

## 6. Carte d'identité (diagnostics)

Par dataset, **le plus complet possible**, et **extensible** (un protocole + une liste de métriques
définitive arriveront ; il faut pouvoir les ajouter et **re-qualifier l'existant**) :

- spectral + PCA / dimensionnalité + **qualité par bloc X** ;
- **stats par variable Y** (distribution / balance de classes) — multi-cible ;
- **dataviz sur X, Y et métadonnées** ;
- shift train↔test *si* un split existe ;
- hashes + citation + provenance.

---

## 7. Migration depuis l'état actuel (`NIRS DB/`, 19 Go)

| Source | Décision |
|---|---|
| **`v2.0/` (164)** — cartes `dataset_card.json` machine-readable | **canonique** : la base devient ces datasets. |
| **`regression/ classification/ multimachines/` (484 feuilles v1)** | **supprimées** (c'étaient des tâches, pas des datasets). |
| **`Publications/`** | garder + organiser **celles référencées** par un dataset ; ignorer le reste. |
| **`chantiers/`, `unusableDB/`** | ignorés **pour l'instant** — migreront dans l'existant plus tard (à anticiper). |

Conséquences code : retirer le chemin v1 (`discover.find_leaves` / `build_descriptor`) — devient mort ;
la carte passe en **multi-Y** ; ajouter les 3 tiers + le plugin `get()` + le pipeline d'ajout + le
health-check des origines. Garde-fou : **lister** les éventuels datasets v1 sans équivalent v2.0 avant
suppression (aucune perte silencieuse).

---

## 8. Points encore ouverts (prochaine itération)

1. **API plugin** — `get()` par défaut concaténé (sans split) ou partitionné ? gestion des splits
   multiples ? noms des accesseurs métadonnées / carte. > Si des splits sont dispo, ils doivent pouvoir être téléchargés splittés, donc c'est des options à mettre. Je te laisse trouver le nom des fonctions pour les metadonnées et métriques.
2. **Anonymisation** — définir « Y normalisés » (z-score ? min-max ? rang ?) et « métadonnées non
   nommées » (drop des noms → `col_0…` ?). > comme ca te parait naturel en ML ou spectroscopie
3. **Token** — un token unique = tout le privé, ou par dataset ? (réutilise le token Dataverse.)
> Je pense qu'on va partir sur l'existant quand le dataverse sera up, ce sera un token dataverse.

4. **Versions** — valider les 2 axes contenu / protocole-métriques (§5). > Le protocole et le schema de métriques/metadata va évoluer. Donc on part sur ca mais il va y avoir les répétitions, les aggrégations, etc. etc.
5. **Désignation du Y par défaut** — quand aucun Y n'est déclaré, quelle règle pour choisir la colonne
   de métadonnée (et comment la renseigner) ? > Aucune règle, on ne met pas de y. On montre les métadonnées et on doit avoir des dataviz metadonnées comme pour y (histogrammes, etc.)
