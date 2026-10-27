---
type: "Research direction"
description: "Does the sulfate-reduction enrichment in cultured deep-clay genomes come from cultivation capturing the porewater fraction, rather than from a habitat-wide metabolic bias of deep clay?"
hypothesis: "Sulfate-reduction markers are enriched in porewater-isolated cultures relative to rock-attached communities, while corrected iron-reduction markers do not differ, so isolation source rather than depth explains the skew."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Comparison rock-attached genomes must be ingested and the parallel enrichment cultures do not yet exist; the markers themselves are already corrected."
collections: ["kbase-ke-pangenome", "kbase-genomes"]
findings: ["bacillota_b_subsurface_accessory--f9a4cc6b", "bacillota_b_subsurface_accessory--bbe885ea", "clay_confined_subsurface--0265377f", "clay_confined_subsurface--208cd800"]
conflicts: []
papers: ["26542073", "37642485", "27739431", "34648720"]
builds_on: ["findings/bacillota_b_subsurface_accessory--f9a4cc6b", "findings/bacillota_b_subsurface_accessory--bbe885ea", "findings/clay_confined_subsurface--0265377f", "findings/clay_confined_subsurface--208cd800"]
projects: ["bacillota_b_subsurface_accessory", "clay_confined_subsurface"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Cultured deep-clay genomes may sample porewater sulfate reducers, not the rock-attached community

Does the sulfate-reduction enrichment in cultured deep-clay genomes come from cultivation capturing the porewater fraction, rather than from a habitat-wide metabolic bias of deep clay?

## Hypothesis

Sulfate-reduction markers are enriched in porewater-isolated cultures relative to rock-attached communities, while corrected iron-reduction markers do not differ, so isolation source rather than depth explains the skew.

## Why it matters

If sulfate-reduction rate is a fraction diagnostic, a genome collection can be audited for which habitat fraction it represents. Cultured-only subsurface cohorts could then not be used for community-level inference without that correction.

## How to test it

Score the corrected sulfate-reduction markers (K11180, K11181, K00394, K00395, K00958) and the multi-heme-cytochrome iron-reduction detector on rock-attached metagenome-assembled genomes and on cultured cohorts from other subsurface sources (needs new ingestion). Compare with the deep cohort (5/9 sulfate-reduction positive vs a rock-attached null of 0.2%). Within the eight Opalinus genomes, compare isolation sources BRC-3 and BIC-A1. Then run parallel porewater and rock-attached enrichment cultures from the same borehole and score the recovered genomes.

## What would support or refute it

Support: sulfate-reduction enrichment tracks porewater-sourced isolation across cohorts and iron reduction stays flat. Refute: rock-attached genomes or other cultured cohorts show similar sulfate-reduction rates, indicating a habitat-level signal. The iron-reduction null is power-limited with the n=9 deep cohort.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Comparison rock-attached genomes must be ingested and the parallel enrichment cultures do not yet exist; the markers themselves are already corrected.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-genomes|KBase Genomes]]

## Builds on

- Finding: [[findings/bacillota_b_subsurface_accessory--f9a4cc6b|Sulfate-reduction signal in deep clay survives while iron-reduction side fails]] (Insufficient literature evidence)
- Finding: [[findings/bacillota_b_subsurface_accessory--bbe885ea|Corrected iron-reduction comparison shows no significant deep versus shallow difference]] (Insufficient literature evidence)
- Finding: [[findings/clay_confined_subsurface--0265377f|Sulfate-reduction signal in Opalinus isolates read as porewater cultivation bias]] (Extends retrieved work)
- Finding: [[findings/clay_confined_subsurface--208cd800|Corrected iron-reduction markers show no significant cohort difference]] (Insufficient literature evidence)

## Closest published work

- [PMID 26542073](https://pubmed.ncbi.nlm.nih.gov/26542073/) A minimalistic microbial food web in an excavated deep subsurface clay rock.
- [PMID 37642485](https://pubmed.ncbi.nlm.nih.gov/37642485/) Clay-associated microbial communities and their relevance for a nuclear waste repository in the Opalinus Clay rock formation.
- [PMID 27739431](https://pubmed.ncbi.nlm.nih.gov/27739431/) Reconstructing a hydrogen-driven microbial metabolic network in Opalinus Clay rock.
- [PMID 34648720](https://pubmed.ncbi.nlm.nih.gov/34648720/) Microbiology of barrier component analogues of a deep geological repository.

PMID 26542073 finds a sulfate reducer in Opalinus porewater and PMID 37642485 finds iron reducers predominate in rock-associated communities; this direction turns that split into a cultivation-bias prediction tested across cohorts and by paired cultivation.
