---
type: "Research direction"
description: "Genes found in one genome show near-zero fitness effects, and condition-specific genes are not more accessory. Are singletons idle, or do they act in conditions the lab never imposes, such as phage attack?"
hypothesis: "A substantial share of singleton genes confer protection or counter-defence only when phages are present, so they are neutral in standard conditions but matter under phage challenge."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Predictions use existing data, but phage-challenge fitness has not been measured."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome", "phagefoundry"]
findings: ["fitness_effects_conservation--87474237", "fitness_effects_conservation--13498333"]
conflicts: []
papers: ["29769716", "22448042", "9419362", "30809245"]
builds_on: ["findings/fitness_effects_conservation--87474237", "findings/fitness_effects_conservation--13498333"]
projects: ["fitness_effects_conservation"]
topics: ["gene-essentiality-and-perturbation-assay-validity"]
---
# Are singleton genes neutral in the lab because they act only against phages?

Genes found in one genome show near-zero fitness effects, and condition-specific genes are not more accessory. Are singletons idle, or do they act in conditions the lab never imposes, such as phage attack?

## Hypothesis

A substantial share of singleton genes confer protection or counter-defence only when phages are present, so they are neutral in standard conditions but matter under phage challenge.

## Why it matters

It would explain why laboratory fitness fails to explain the accessory genome and show where hidden function lies. It would also direct fitness screens to phage challenge.

## How to test it

Pick Fitness Browser organisms with phages in PhageFoundry Browsers. Predict phage-related singleton genes, run transposon-library fitness under infection, and compare phage-related with other singletons, and with core genes.

## What would support or refute it

Support: singleton genes, mainly phage-related ones, show strong effects under phage challenge but not in standard conditions. Refutation: singletons stay neutral under phage challenge too, favouring lack of function or other niches.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Predictions use existing data, but phage-challenge fitness has not been measured.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/phagefoundry|PhageFoundry Browsers]]

## Builds on

- Finding: [[findings/fitness_effects_conservation--87474237|Singleton genes show near-zero fitness, likely invisible to lab assays]] (Insufficient literature evidence)
- Finding: [[findings/fitness_effects_conservation--13498333|Condition-specific genes are not preferentially accessory]] (Insufficient literature evidence)

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 22448042](https://pubmed.ncbi.nlm.nih.gov/22448042/) The Black Queen Hypothesis: evolution of dependencies through adaptive gene loss.
- [PMID 9419362](https://pubmed.ncbi.nlm.nih.gov/9419362/) Marginal fitness contributions of nonessential genes in yeast.
- [PMID 30809245](https://pubmed.ncbi.nlm.nih.gov/30809245/) Bacterial 'Grounded' Prophages: Hotspots for Genetic Renovation and Innovation.

PMID 29769716 maps condition-specific phenotypes for poorly annotated genes without phage challenge. PMID 9419362 shows small effects for non-essential yeast genes but does not test hidden conditions.
