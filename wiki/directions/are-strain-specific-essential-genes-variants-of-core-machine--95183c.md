---
type: "Research direction"
description: "Essential genes outside the core genome are explained only partly, so are they strain-specific versions of core functions?"
hypothesis: "Essential genes lacking a pangenome match or labeled auxiliary mostly share domains or pathway roles with essential core genes, so grouping them by function removes much of the apparent strain specificity."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Annotation tables are in the catalog, but essential gene calls and pangenome links must be derived from fitness data."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.seedannotation", "kescience.fitnessbrowser.seedroles", "kescience.fitnessbrowser.besthitkegg", "kescience.fitnessbrowser.keggmember", "kbase.ke_pangenome.gene_cluster"]
findings: ["conservation_vs_fitness--96327d99", "conservation_vs_fitness--631185af", "conservation_vs_fitness--3b44ab09"]
conflicts: ["conflict--annotation-and-pangenome-correlates-of-gene-essentiality--141c9f62"]
papers: ["36097170", "20949199", "30444863", "29769716"]
builds_on: ["findings/conservation_vs_fitness--96327d99", "findings/conservation_vs_fitness--631185af", "findings/conservation_vs_fitness--3b44ab09", "conflicts/conflict--annotation-and-pangenome-correlates-of-gene-essentiality--141c9f62"]
projects: ["conservation_vs_fitness", "essential_genome"]
topics: ["gene-essentiality-and-perturbation-assay-validity"]
---
# Are strain-specific essential genes variants of core machinery rather than unique functions?

Essential genes outside the core genome are explained only partly, so are they strain-specific versions of core functions?

## Hypothesis

Essential genes lacking a pangenome match or labeled auxiliary mostly share domains or pathway roles with essential core genes, so grouping them by function removes much of the apparent strain specificity.

## Why it matters

It would show that essentiality is conserved at the function level even when genes differ, and would give a route to annotate the poorly characterized essential-unmapped genes.

## How to test it

In Fitness Browser organisms, list essential genes with no pangenome cluster match or auxiliary status. Assign them to functional groups using SEED roles and KEGG groups, and compare against essential core genes in the same organism. Test whether the share assigned to a core essential function exceeds that of random non-essential genes of matched length.

## What would support or refute it

Support: a large share of these genes fall into core essential functional groups beyond matched random genes. Refute: they remain unassigned or fall into mobile or unrelated functions at the matched-gene rate.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Annotation tables are in the catalog, but essential gene calls and pangenome links must be derived from fitness data.

## Builds on

- Finding: [[findings/conservation_vs_fitness--96327d99|Essential-unmapped genes are the least characterized category]] (Insufficient literature evidence)
- Finding: [[findings/conservation_vs_fitness--631185af|Essential-core enrichment is significant in just over half of organisms]] (Insufficient literature evidence)
- Finding: [[findings/conservation_vs_fitness--3b44ab09|Essential-core genes are the most enzyme-rich and best annotated]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--annotation-and-pangenome-correlates-of-gene-essentiality--141c9f62|Modest Core Enrichment Versus Unexplained Strain-Specific Essential Genes]]

## Closest published work

- [PMID 36097170](https://pubmed.ncbi.nlm.nih.gov/36097170/) A bacterial pan-genome makes gene essentiality strain-dependent and evolvable.
- [PMID 20949199](https://pubmed.ncbi.nlm.nih.gov/20949199/) Predicting conserved essential genes in bacteria: in silico identification of putative drug targets.
- [PMID 30444863](https://pubmed.ncbi.nlm.nih.gov/30444863/) Metabolic models and gene essentiality data reveal essential and conserved metabolism in prokaryotes.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.

36097170 shows essentiality depends on the pan-genome in one species; this direction tests whether functional grouping explains strain-specific essentials across many organisms.
