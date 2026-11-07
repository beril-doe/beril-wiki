---
type: "Research direction"
description: "Do Rhodanobacter, Ralstonia and Dyella occupy more acidic, warmer habitats worldwide than Brevundimonas, Caulobacter and Sphingomonas because of their own tolerance limits, or because each cluster excludes the other where their tolerances overlap?"
hypothesis: "Members of the Brevundimonas-Caulobacter-Sphingomonas cluster can grow at acidic pH when alone but are outcompeted there by the Rhodanobacter cluster. Both clusters tolerate the range between their habitat peaks."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Isolates and habitat metadata exist, but growth across pH in monoculture and co-culture has not been measured."
collections: ["enigma-coral", "nmdc-ncbi-biosamples", "kbase-ke-pangenome"]
findings: ["genotype_to_phenotype_enigma--a6ede42b"]
conflicts: []
papers: ["38366921", "40118314"]
builds_on: ["findings/genotype_to_phenotype_enigma--a6ede42b"]
projects: ["genotype_to_phenotype_enigma"]
topics: ["metabolic-traits-auxotrophy-and-community-dependence"]
---
# Is the acid and warmth niche split between two Oak Ridge genus clusters caused by competition?

Do Rhodanobacter, Ralstonia and Dyella occupy more acidic, warmer habitats worldwide than Brevundimonas, Caulobacter and Sphingomonas because of their own tolerance limits, or because each cluster excludes the other where their tolerances overlap?

## Hypothesis

Members of the Brevundimonas-Caulobacter-Sphingomonas cluster can grow at acidic pH when alone but are outcompeted there by the Rhodanobacter cluster. Both clusters tolerate the range between their habitat peaks.

## Why it matters

A tolerance limit and competitive exclusion predict different outcomes for contaminated, acidified aquifers. It would also show whether the global co-occurrence map reflects physiology or interaction.

## How to test it

Using ENIGMA CORAL isolates and the NMDC BioSamples, select Oak Ridge isolates from both clusters. Measure monoculture growth across a pH series spanning the acidic and neutral habitat means, then co-culture pairs across the same series and track relative abundance by sequencing. Check whether sample-level exclusion of the clusters in NMDC BioSamples peaks at intermediate pH where monocultures overlap.

## What would support or refute it

Support: monoculture ranges overlap broadly, but in co-culture one cluster is displaced at acidic pH. Refutation: monoculture growth already fails outside each cluster's habitat range, so tolerance alone explains the split.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Isolates and habitat metadata exist, but growth across pH in monoculture and co-culture has not been measured.

- Collection: [[data/enigma-coral|ENIGMA CORAL]]
- Collection: [[data/nmdc-ncbi-biosamples|NMDC BioSamples]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/genotype_to_phenotype_enigma--a6ede42b|Global pH niche partition separates two Oak Ridge genus clusters]] (Candidate novel)

## Closest published work

- [PMID 38366921](https://pubmed.ncbi.nlm.nih.gov/38366921/) Influence of host phylogeny and water physicochemistry on microbial assemblages of the fish skin microbiome.
- [PMID 40118314](https://pubmed.ncbi.nlm.nih.gov/40118314/) The response and ecological implications between various sulfur forms and environmental factors in acid mine drainage.

PMID 38366921 and PMID 40118314 link temperature and pH to Ralstonia and Sphingomonas abundance in fish skin and acid mine drainage. They do not test whether a niche split between these clusters reflects tolerance or competition.
