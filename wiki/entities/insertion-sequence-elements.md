---
type: "Gene_Or_Pathway"
description: "Mobile transposable elements and their gene fragments, which the report links to short costly non-conserved genes."
sources: ["summaries/costly_dispensable_genes__REPORT.md", "summaries/gene_copy_number_variation__REPORT.md"]
aliases: ["IS elements", "transposases"]
---
# Insertion sequence elements

This page covers insertion sequence elements: mobile transposable elements and their gene fragments, also called IS elements or transposases. The costly_dispensable_genes report links them to costly genes that are not conserved across a species pangenome. [src: costly_dispensable_genes] The evidence is correlative (keyword, length and SEED category enrichments), and the interpretation is the report's explanation, not a direct test. [src: costly_dispensable_genes] See mobile element origin of costly non conserved genes for the wider argument.

## Key facts

### Association with costly, dispensable genes

Costly+dispensable genes carry mobile-element signals on several measures. [src: costly_dispensable_genes]

- Costly+dispensable genes are 7.45x more likely than costly+conserved genes to contain mobile-element keywords in their descriptions (transposase, integrase, phage, IS element, recombinase, prophage; OR=7.45, p=4.6e-71). OR means odds ratio. [src: costly_dispensable_genes]
- Their median gene length is 615 bp, versus 765 bp for costly+conserved genes (p=4.2e-75, rank-biserial r=0.170). The report calls this consistent with IS elements and gene fragments. [src: costly_dispensable_genes]
- The SEED category "Phages, Prophages, Transposable elements, Plasmids" is 11.7x enriched in costly+dispensable versus costly+conserved genes (FDR=1.3e-17). FDR means false discovery rate. See [[entities/seed-subsystems]]. [src: costly_dispensable_genes]

### Interpretation

The report reads costly+dispensable genes as the genomic debris of horizontal gene transfer. This debris includes insertion sequences, prophage remnants, transposases and defense systems. These impose metabolic cost on the host and are not conserved across the species pangenome. [src: costly_dispensable_genes] See [[summaries/costly_dispensable_genes__REPORT]].

### Relevance to copy-number variation

In the gene_copy_number_variation report, COG category L (COG means clusters of orthologous groups) contains transposases, integrases and IS elements. The report says these are known to expand in bacterial pangenomes. [src: gene_copy_number_variation] See [[entities/cog-category-l-replication-recombination-and-repair]].

The report adds a caveat. If the L effect concentrates in IS elements, the story becomes transposition-mediated copy-number variation rather than adaptive paralogy. This matters for the dosage-balance interpretation. [src: gene_copy_number_variation] See [[concepts/mechanisms-and-confounders-of-copy-number-variation-in-pangenomes]] and [[summaries/gene_copy_number_variation__REPORT]].
