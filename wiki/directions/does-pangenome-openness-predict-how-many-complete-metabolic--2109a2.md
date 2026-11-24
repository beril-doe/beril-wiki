---
type: "Research direction"
description: "Is the higher fraction of fitness-neutral complete pathways in species with open pangenomes independent of shared ancestry?"
hypothesis: "Species clades with more open pangenomes carry more latent pathways even after controlling for phylogenetic relatedness and for how many strains were fitness-tested."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Pathway, pangenome and experiment tables are in the catalog; the controlled model has to be built."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kbase.ke_pangenome.gapmind_pathways", "kbase.ke_pangenome.pangenome", "kescience.fitnessbrowser.experiment"]
findings: ["metabolic_capability_dependency--3bcc11af", "metabolic_capability_dependency--b6cd74ee", "metabolic_capability_dependency--2a8a609f"]
conflicts: []
papers: ["24910088", "40568968", "35575545"]
builds_on: ["findings/metabolic_capability_dependency--3bcc11af", "findings/metabolic_capability_dependency--b6cd74ee", "findings/metabolic_capability_dependency--2a8a609f"]
projects: ["metabolic_capability_dependency"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Does pangenome openness predict how many complete metabolic pathways are dispensable?

Is the higher fraction of fitness-neutral complete pathways in species with open pangenomes independent of shared ancestry?

## Hypothesis

Species clades with more open pangenomes carry more latent pathways even after controlling for phylogenetic relatedness and for how many strains were fitness-tested.

## Why it matters

It would link gene-flow-rich lifestyles to metabolic redundancy, suggesting that open pangenomes allow pathway stockpiling rather than reflecting lab artifacts.

## How to test it

For the 48 Fitness Browser organisms, classify GapMind pathways as latent or active using fitness data, add pangenome openness per species clade, and refit with ancestry control and tested-strain count as covariates.

## What would support or refute it

Support: the positive association survives controls. Refute: it vanishes with ancestry or testing depth.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Pathway, pangenome and experiment tables are in the catalog; the controlled model has to be built.

## Builds on

- Finding: [[findings/metabolic_capability_dependency--3bcc11af|Latent pathway fraction rises with pangenome openness across species clades]] (Candidate novel)
- Finding: [[findings/metabolic_capability_dependency--b6cd74ee|Pathway conservation does not separate latent from active pathways]] (Candidate novel)
- Finding: [[findings/metabolic_capability_dependency--2a8a609f|Roughly one in six complete pathways is fitness-neutral]] (Insufficient literature evidence)

## Closest published work

- [PMID 24910088](https://pubmed.ncbi.nlm.nih.gov/24910088/) Less is more: selective advantages can explain the prevalent loss of biosynthetic genes in bacteria.
- [PMID 40568968](https://pubmed.ncbi.nlm.nih.gov/40568968/) Microbial cross-feeding stabilized by segregation of a dependent mutant from its independent ancestor.
- [PMID 35575545](https://pubmed.ncbi.nlm.nih.gov/35575545/) Complex Ecotype Dynamics Evolve in Response to Fluctuating Resources.

24910088 explains biosynthetic gene loss but does not relate latent pathway fraction to pangenome openness.
