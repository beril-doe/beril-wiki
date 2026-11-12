---
type: "Research direction"
description: "Methanococcus strains account for most of the genes that stay unannotated after reannotation. Are these genes real methanogen-specific functions, instead of genes that look dark because reference databases cover archaea poorly?"
hypothesis: "The dark Methanococcus genes are conserved within methanogens but absent from other archaea and bacteria. They also show phenotypes under methanogen-specific conditions such as nitrogen source and metal limitation, which marks them as lineage innovations."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Ortholog breadth and existing fitness conditions can be analysed now, but the metal conditions for Methanococcus have not been measured."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["truly_dark_genes--d1b84273", "truly_dark_genes--947aec4f"]
conflicts: []
papers: ["39120137", "29769716", "42706541", "34739369"]
builds_on: ["findings/truly_dark_genes--d1b84273", "findings/truly_dark_genes--947aec4f"]
projects: ["truly_dark_genes"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Are archaeal dark genes methanogen-specific innovations rather than annotation lag?

Methanococcus strains account for most of the genes that stay unannotated after reannotation. Are these genes real methanogen-specific functions, instead of genes that look dark because reference databases cover archaea poorly?

## Hypothesis

The dark Methanococcus genes are conserved within methanogens but absent from other archaea and bacteria. They also show phenotypes under methanogen-specific conditions such as nitrogen source and metal limitation, which marks them as lineage innovations.

## Why it matters

If so, the apparent excess of dark genes in archaea reflects unique biology that annotation transfer from bacteria cannot reach, and calls for archaeal-specific experiments. If they are database-coverage artefacts, they would resolve with better archaeal references.

## How to test it

In the Pangenome Collection, trace ortholog breadth of the dark Methanococcus genes across archaeal and bacterial genomes. In the Fitness Browser, check which conditions give them strong effects, and use cofitness to place them in operons with annotated genes. Then run the proposed metal panel (nickel, cobalt, copper, zinc, tungsten and molybdenum) on Methanococcus maripaludis S2 and JJ, which carry metal candidates but only iron fitness data, and score the dark genes.

## What would support or refute it

Support: the genes are restricted to methanogens and gain strong phenotypes under methanogen-relevant nutrient or metal conditions. Refute: they have orthologs in annotated non-methanogen lineages, or show no condition-specific phenotypes.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Ortholog breadth and existing fitness conditions can be analysed now, but the metal conditions for Methanococcus have not been measured.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/truly_dark_genes--d1b84273|Archaeal Methanococcus strains dominate the truly dark gene set]] (Insufficient literature evidence)
- Finding: [[findings/truly_dark_genes--947aec4f|Truly dark genes are shorter, more accessory, with narrower ortholog breadth]] (Candidate novel)

## Closest published work

- [PMID 39120137](https://pubmed.ncbi.nlm.nih.gov/39120137/) High-throughput genetics enables identification of nutrient utilization and accessory energy metabolism genes in a model methanogen.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 42706541](https://pubmed.ncbi.nlm.nih.gov/42706541/) Large-scale benchmarking of prokaryotic annotation tools across thousands of species.
- [PMID 34739369](https://pubmed.ncbi.nlm.nih.gov/34739369/) Bakta: rapid and standardized annotation of bacterial genomes via alignment-free sequence identification.

PMID 39120137 identifies nutrient-utilisation genes in a model methanogen by high-throughput genetics, and PMID 42706541 benchmarks annotation tools across species. Neither asks whether archaeal dark genes are lineage-specific innovations.
