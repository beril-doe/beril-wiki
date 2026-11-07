---
type: "Research direction"
description: "Genes that stay hypothetical after reannotation are depleted in stress phenotypes and enriched in nutrient, mixed-community and iron conditions. Do they encode narrow-substrate uptake or catabolic parts that only show a phenotype on a specific compound?"
hypothesis: "Truly dark genes with nutrient phenotypes sit next to annotated transporter or catabolic genes more often than later-annotated genes with similar phenotypes. Their phenotypes are limited to one related compound family."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Condition labels, dark-gene status and gene positions exist; the neighbourhood and substrate-breadth comparison is new."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["truly_dark_genes--8c818410", "truly_dark_genes--947aec4f", "functional_dark_matter--cefca00d"]
conflicts: ["conflict--experimental-prioritization-of-functional-dark-matter--6247b74c"]
papers: ["29769716", "22125499", "25968644", "41984924"]
builds_on: ["findings/truly_dark_genes--8c818410", "findings/truly_dark_genes--947aec4f", "findings/functional_dark_matter--cefca00d", "conflicts/conflict--experimental-prioritization-of-functional-dark-matter--6247b74c"]
projects: ["caulobacter_fur_lipida_loss", "functional_dark_matter", "truly_dark_genes"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Do truly dark genes hold nutrient-acquisition roles that rarely tested substrates hide?

Genes that stay hypothetical after reannotation are depleted in stress phenotypes and enriched in nutrient, mixed-community and iron conditions. Do they encode narrow-substrate uptake or catabolic parts that only show a phenotype on a specific compound?

## Hypothesis

Truly dark genes with nutrient phenotypes sit next to annotated transporter or catabolic genes more often than later-annotated genes with similar phenotypes. Their phenotypes are limited to one related compound family.

## Why it matters

This would give a concrete functional class for genes that now look random. It would also explain the opposing stress findings: dark genes overall look stress-dominated, while stress is depleted among truly dark genes, and two stress comparisons (28.7% versus 43.2% and 43.3% versus 54.7%) remain unreconciled.

## How to test it

Take truly dark genes with strong nutrient phenotypes in the Fitness Browser and, from the Pangenome Collection, list their genomic neighbours. Compute the share adjacent to annotated transporters, regulators or catabolic enzymes, and the number of compound families each gene responds to. Compare with annotation-lag genes with strong nutrient phenotypes in the same organisms. Use organisms with the most conditions, such as Shewanella oneidensis MR-1 with 121.

## What would support or refute it

Support: dark nutrient genes are more often next to uptake or catabolic genes and respond to fewer, related compounds. Refutation: their neighbourhoods and substrate breadth look like those of annotation-lag genes, or they respond to many unrelated nutrients.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Condition labels, dark-gene status and gene positions exist; the neighbourhood and substrate-breadth comparison is new.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/truly_dark_genes--8c818410|Truly dark genes are depleted, not enriched, in stress conditions]] (Candidate novel)
- Finding: [[findings/truly_dark_genes--947aec4f|Truly dark genes are shorter, more accessory, with narrower ortholog breadth]] (Candidate novel)
- Finding: [[findings/functional_dark_matter--cefca00d|Stress-condition dark genes are not more accessory than carbon/nitrogen genes]] (Candidate novel)
- Conflict: [[conflicts/conflict--experimental-prioritization-of-functional-dark-matter--6247b74c|Stress dominance versus stress depletion among strong-phenotype dark genes]]

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 22125499](https://pubmed.ncbi.nlm.nih.gov/22125499/) Evidence-based annotation of gene function in Shewanella oneidensis MR-1 using genome-wide fitness profiling across 121 conditions.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.
- [PMID 41984924](https://pubmed.ncbi.nlm.nih.gov/41984924/) High-throughput characterization of Mycobacterium tuberculosis gene function across diverse conditions.

PMID 29769716 and PMID 22125499 tie poorly annotated genes to conditions but do not compare truly dark genes with later-annotated genes for substrate specificity or genomic neighbours.
