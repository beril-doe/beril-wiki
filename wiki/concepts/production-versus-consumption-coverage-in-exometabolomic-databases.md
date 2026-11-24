---
type: "Concept"
description: "How exometabolomic action codes distinguish de novo production, amplification, detection and no change, what the 2018 snapshot lacks (consumption), and what that blocks; stops short of gene-level interpretation."
sources: ["summaries/discoveries.md", "summaries/pitfalls.md", "summaries/webofmicrobes_explorer__REPORT.md"]
---
# Production versus consumption coverage in exometabolomic databases

The 2018 snapshot has no organism consumption action, so it covers production only. [src: discoveries, webofmicrobes_explorer] Control and organism entries use different code meanings, so the actor must be known to read any code. [src: pitfalls, webofmicrobes_explorer]

## How the action codes work

The WoM database uses a 4-action system whose meaning differs between control and organism entries. [src: webofmicrobes_explorer] Actor identity is therefore needed to read any code. [src: pitfalls]

For organisms, E (Emerged) means a metabolite was absent from the control medium and is now detected, interpreted as de novo biosynthesis. [src: discoveries] I (Increased) means the metabolite was present in the control and its level went up. [src: discoveries] N means no significant change. [src: webofmicrobes_explorer]

For the control ("The Environment"), D means Detected in medium and N means Not detected. [src: discoveries] Mixing control and organism meanings without the actor distinction is wrong. [src: pitfalls]

Observation counts in the snapshot:

| Actor | Code | Meaning | Observations |
|---|---|---|---|
| Control | D | Detected in starting medium | 742 [src: webofmicrobes_explorer] |
| Control | N | Not detected | 1,023 [src: webofmicrobes_explorer] |
| Organisms | I | Increased | 1,338 [src: webofmicrobes_explorer] |
| Organisms | E | Emerged (de novo production) | 1,155 [src: webofmicrobes_explorer] |
| Organisms | N | No significant change | 7,509 [src: webofmicrobes_explorer] |

E and I never overlap: there are 0 overlaps across 10,744 observations. [src: discoveries, webofmicrobes_explorer, pitfalls] The E/I distinction was not prominently documented and had to be decoded by exploring the data. [src: webofmicrobes_explorer]

## Turning codes into a produced label

A plain selection of the action field returns raw codes, not a binary produced/consumed label. [src: pitfalls] The pitfalls report also lists an occasional D as decreased. [src: pitfalls] One working definition, used in two notebooks of the genotype_to_phenotype_enigma project, is produced = action IN ('I', 'E'). It counts a compound as produced if it increased in supernatant or emerged from below the detection limit. [src: pitfalls]

Both ways of getting this wrong have a cost. Adding N to the produced set makes every strain look like a production generalist and collapses the signal. [src: pitfalls] Dropping E misses genuinely novel production. [src: pitfalls]

## Separating de novo production from amplification

The E/I split gives a measure of how much of an isolate's metabolite change is new. The report states that this fraction varies 2-fold across ENIGMA isolates in R2A medium. [src: webofmicrobes_explorer] ([[entities/r2a-medium]]) It describes the 15–32% range as a new "metabolic novelty rate" measure. [src: webofmicrobes_explorer]

| Isolate | I | E | Novelty rate |
|---|---|---|---|
| Pseudomonas GW456-L13 | 49 | 34 | 32.4% [src: webofmicrobes_explorer] |
| Pseudomonas FW507-14TSA | 44 | 33 | 31.4% [src: webofmicrobes_explorer] |
| Pseudomonas FW300-N2A2 | 26 | 32 | 30.5% [src: webofmicrobes_explorer] |
| Acidovorax GW101-3E06 | 48 | 30 | 28.6% [src: webofmicrobes_explorer] |
| Bacillus FW507-8R2A | 39 | 16 | 15.2% [src: webofmicrobes_explorer] |

GW456-L13 has the highest reported rate and FW507-8R2A the lowest. [src: webofmicrobes_explorer] ([[entities/pseudomonas-sp-gw456-l13]])

## What the snapshot lacks

The 2018 snapshot has no Decreased (consumption) action for any organism. All 742 D observations belong to the control. [src: discoveries, webofmicrobes_explorer] The database therefore records production, not consumption. [src: discoveries] This absence is by design, not a query bug. [src: pitfalls]

The snapshot is a 2018 frozen copy, and newer data live in GNPS2, not in this dataset. [src: pitfalls] The Wayback Machine archive may not match the current WoM. [src: webofmicrobes_explorer]

Consumption is part of the schema. The Kosina et al. paper describes "decrease" as a valid action, so the export omits something the schema supports. [src: webofmicrobes_explorer] Consumption data may therefore exist in the newer GNPS2 version. [src: webofmicrobes_explorer]

### What this blocks

Without consumption, the snapshot cannot test whether consumed metabolites predict gene essentiality. [src: webofmicrobes_explorer] See [[concepts/metabolite-production-versus-utilization-discordance]] and [[concepts/matching-exometabolite-profiles-to-gene-fitness-experiments]] for the related questions. The report names a possible fix. The de Raad et al. (2022) NLDM study tested 110 soil bacteria with full consumption and production tracking. [src: webofmicrobes_explorer] The report suggests that dataset likely contains consumption data and may be in the current GNPS2 version. [src: webofmicrobes_explorer] It predicts that ingesting it would resolve the no-consumption limitation and increase the organism count 3–5×. [src: webofmicrobes_explorer] It also proposes re-running the ingestion pipeline (`data/wom_ingest/`) when newer WoM data are available, to update kescience_webofmicrobes and enable the blocked consumption analyses. [src: webofmicrobes_explorer] It expects the GNPS2 version or Northen lab internal datasets to be substantially richer. [src: webofmicrobes_explorer]

## Open Directions

- Check whether the current GNPS2 version of WoM carries a decrease action. Compare its codes with the 2018 snapshot, which has none. This would settle whether the gap is only in the export.
- Re-run the ingestion pipeline once newer data are available. This enables the consumption analyses that are now blocked.
- Once consumption exists, test whether consumed metabolites predict gene essentiality. This is the question the 2018 snapshot cannot answer.
- Recompute the novelty rate (E share of changes) with consumption included. This would show whether the 15–32% range holds across a larger organism panel.
