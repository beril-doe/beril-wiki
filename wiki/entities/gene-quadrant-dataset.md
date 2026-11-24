---
type: "Dataset"
description: "Table of 142,190 genes across 43 bacteria with fitness statistics, conservation status and quadrant assignment."
sources: ["summaries/core_gene_tradeoffs__REPORT.md", "summaries/costly_dispensable_genes__REPORT.md"]
aliases: ["gene_quadrants.tsv"]
---
# Gene quadrant dataset

The gene quadrant dataset (`gene_quadrants.tsv`) is a table of genes with fitness statistics, conservation status and a quadrant assignment, listed in the costly_dispensable_genes report. [src: costly_dispensable_genes] The evidence here is descriptive: it comes from that report's file listing and from counts in a related report.

## Key facts

- The file `data/gene_quadrants.tsv` has 142,190 rows. Each row holds fitness statistics, conservation status and quadrant assignment for a gene. [src: costly_dispensable_genes]
- The costly_dispensable_genes report's cross-organism analysis covers 142,190 genes across 43 bacteria. The report claims novelty for this scale and for its pangenome dimension. [src: costly_dispensable_genes] The gene count matches the row count of the table. [src: costly_dispensable_genes]

## Quadrant counts reported elsewhere

The table below gives four categories of a [[entities/fitness-browser]] selection signature matrix, as counted in a separate report, [[summaries/core_gene_tradeoffs__REPORT]]. [src: core_gene_tradeoffs]

| Category | Genes | Report's reading |
|---|---|---|
| Neutral + Dispensable | 21,886 | Niche-specific genes [src: core_gene_tradeoffs] |
| Costly + Conserved | 28,017 | Maintained by natural selection despite lab-measured cost. The report says they are essential in natural environments that lab experiments do not capture. [src: core_gene_tradeoffs] |
| Costly + Dispensable | 5,526 | Candidates for ongoing gene loss, because they are burdensome and not universally conserved [src: core_gene_tradeoffs] |
| Neutral + Conserved | 86,761 | Classic housekeeping genes [src: core_gene_tradeoffs] |

The costly_dispensable_genes report ([[summaries/costly_dispensable_genes__REPORT]]) also cites 28,017 costly+conserved genes, as a contrast to its costly dispensable set. [src: costly_dispensable_genes] For interpretation, see [[concepts/costly-but-conserved-genes-laboratory-burden-versus-conservation]] and [[concepts/gene-loss-and-black-queen-hypothesis-tests]]. [src: core_gene_tradeoffs]
