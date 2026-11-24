---
type: "Research direction"
description: "Do costly-but-dispensable genes in Fitness Browser organisms sit on recently acquired mobile elements, and are they older or younger than costly conserved genes?"
hypothesis: "Costly dispensable genes are mostly recent acquisitions inside prophage or transposon regions, so they are accessory, patchily distributed across the species, and near other mobile genes more often than costly conserved genes."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Both datasets are in the catalog, but linking genes to clusters and computing gene neighbourhoods needs new joins."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.gene", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.bakta_annotations"]
findings: ["costly_dispensable_genes--31cecf6a", "costly_dispensable_genes--e1254d2a", "costly_dispensable_genes--f3a85492", "cog_analysis--e7589648", "cog_analysis--42e8db6b"]
conflicts: []
papers: ["22448042", "36097170", "29769716", "21298028", "18948295"]
builds_on: ["findings/costly_dispensable_genes--31cecf6a", "findings/costly_dispensable_genes--e1254d2a", "findings/costly_dispensable_genes--f3a85492", "findings/cog_analysis--e7589648", "findings/cog_analysis--42e8db6b"]
projects: ["cog_analysis", "costly_dispensable_genes"]
topics: ["resistance-defense-systems-and-mobile-elements"]
---
# Are costly but dispensable genes mostly horizontally acquired mobile elements still awaiting loss?

Do costly-but-dispensable genes in Fitness Browser organisms sit on recently acquired mobile elements, and are they older or younger than costly conserved genes?

## Hypothesis

Costly dispensable genes are mostly recent acquisitions inside prophage or transposon regions, so they are accessory, patchily distributed across the species, and near other mobile genes more often than costly conserved genes.

## Why it matters

If true, genome expansion by horizontal transfer, not decaying metabolism, is the main source of burden genes, and gene loss is a slow clean-up of selfish DNA.

## How to test it

Link Fitness Browser genes with max fitness above 1 to pangenome clusters. Compare costly+dispensable and costly+conserved genes for neighbour distance to transposase, integrase and phage genes, accessory or singleton status, and GC deviation, within each species. Use COG L and V annotations as a cross-check.

## What would support or refute it

Support: costly dispensable genes cluster near mobile genes and are singleton or accessory far more often, in most species. Refute: after matching for annotation, proximity and patchiness do not differ, or enrichment disappears when one-experiment burden calls are replaced by repeated-experiment calls.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Both datasets are in the catalog, but linking genes to clusters and computing gene neighbourhoods needs new joins.

## Builds on

- Finding: [[findings/costly_dispensable_genes--31cecf6a|Costly dispensable genes are strongly enriched for mobile-element keywords]] (Candidate novel)
- Finding: [[findings/costly_dispensable_genes--e1254d2a|Costly non-conserved genes are mostly mobile-element debris from horizontal transfer]] (Candidate novel)
- Finding: [[findings/costly_dispensable_genes--f3a85492|SEED phage and transposable element category enriched among costly dispensable genes]] (Candidate novel)
- Finding: [[findings/cog_analysis--e7589648|Mobile elements dominate novel genes across all species]] (Candidate novel)
- Finding: [[findings/cog_analysis--42e8db6b|Defense genes are also enriched among novel genes]] (Candidate novel)

## Closest published work

- [PMID 22448042](https://pubmed.ncbi.nlm.nih.gov/22448042/) The Black Queen Hypothesis: evolution of dependencies through adaptive gene loss.
- [PMID 36097170](https://pubmed.ncbi.nlm.nih.gov/36097170/) A bacterial pan-genome makes gene essentiality strain-dependent and evolvable.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 21298028](https://pubmed.ncbi.nlm.nih.gov/21298028/) Horizontal transfer, not duplication, drives the expansion of protein families in prokaryotes.
- [PMID 18948295](https://pubmed.ncbi.nlm.nih.gov/18948295/) Genomics of bacteria and archaea: the emerging dynamic view of the prokaryotic world.

22448042 and 36097170 treat gene loss and pangenome essentiality, but not whether burden genes are mobile-element debris; this tests their position and age directly.
