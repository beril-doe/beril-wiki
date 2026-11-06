---
type: "Research direction"
description: "Truly dark genes with strong phenotypes (|f| \u2265 2) are enriched in nutrient, mixed community and iron conditions. Do they encode unrecognized components of iron handling and community interaction that annotation tools miss?"
hypothesis: "Truly dark genes with strong iron-condition phenotypes cofit with known iron-acquisition or iron-homeostasis genes and carry accessory, lineage-restricted distributions more often than annotation-lag genes with iron phenotypes."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Fitness and pangenome data exist, but defined-iron growth assays and uptake measurements of deletion mutants are new work."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["truly_dark_genes--8c818410", "truly_dark_genes--ba47a194"]
conflicts: ["conflict--experimental-prioritization-of-functional-dark-matter--6247b74c"]
papers: ["29769716", "25968644", "41984924"]
builds_on: ["findings/truly_dark_genes--8c818410", "findings/truly_dark_genes--ba47a194", "conflicts/conflict--experimental-prioritization-of-functional-dark-matter--6247b74c"]
projects: ["caulobacter_fur_lipida_loss", "functional_dark_matter", "truly_dark_genes"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Iron and community-condition phenotypes of truly dark genes may mark unrecognized niche-interaction functions

Truly dark genes with strong phenotypes (|f| ≥ 2) are enriched in nutrient, mixed community and iron conditions. Do they encode unrecognized components of iron handling and community interaction that annotation tools miss?

## Hypothesis

Truly dark genes with strong iron-condition phenotypes cofit with known iron-acquisition or iron-homeostasis genes and carry accessory, lineage-restricted distributions more often than annotation-lag genes with iron phenotypes.

## Why it matters

It would turn an enrichment into a mechanism: persistent dark genes would be evidence of unexplored niche-specific physiology, not annotation lag, redirecting where to look for new functions.

## How to test it

In the Fitness Browser, select truly dark genes with |f| ≥ 2 in iron conditions. Compute cofitness with annotated iron-related genes versus matched annotation-lag genes, and check pangenome class and ortholog breadth. Repeat for mixed-community conditions. Then delete top candidates in one organism and measure growth under iron limitation and excess, plus siderophore or iron-uptake assays.

## What would support or refute it

Support: iron-phenotype dark genes cofit with iron genes beyond matched controls and growth defects replicate under defined iron conditions. Refute: cofitness is no stronger than controls or phenotypes reflect general growth effects. Enrichment alone does not identify function, and condition coverage differs among organisms.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Fitness and pangenome data exist, but defined-iron growth assays and uptake measurements of deletion mutants are new work.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/truly_dark_genes--8c818410|Truly dark genes are depleted, not enriched, in stress conditions]] (Candidate novel)
- Finding: [[findings/truly_dark_genes--ba47a194|Most truly dark genes carry some clue; few are completely dark]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--experimental-prioritization-of-functional-dark-matter--6247b74c|Stress dominance versus stress depletion among strong-phenotype dark genes]]

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.
- [PMID 41984924](https://pubmed.ncbi.nlm.nih.gov/41984924/) High-throughput characterization of Mycobacterium tuberculosis gene function across diverse conditions.

PMID 29769716 ties many poorly annotated genes to specific conditions, but its abstract does not compare condition categories between truly dark and annotation-lag genes, and no retrieved paper tests iron or community conditions for them.
