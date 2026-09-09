---
type: "Method"
description: "Parsimony method used to infer ancestral states and rank-attributed gains"
sources: ["summaries/gene_function_ecological_agora__REPORT.md"]
---
# Sankoff parsimony

## What it is

**Canonical name:** Sankoff parsimony.  
**Known aliases:** Sankoff algorithm; Sankoff dynamic programming.  
**Stable external identifier:** None documented in the source. [src: gene_function_ecological_agora]

Sankoff parsimony is a phylogenetic method used in the Gene Function Ecological Agora project to infer character-state changes across a species tree and assign inferred gain events to recipient-rank depths. [src: gene_function_ecological_agora]

## Use in Gene Function Ecological Agora

The project used Sankoff parsimony with M22 recipient-rank attribution instead of the earlier parent-rank dispersion metric. [src: gene_function_ecological_agora]

The analysis assigned 17,073,194 Sankoff gain events to recipient-rank depth bins. [src: gene_function_ecological_agora]

These rank-attributed gains were used to compare recent-to-ancient acquisition signatures among function classes, including CRISPR-Cas, TCS histidine kinases, β-lactamases, and clean tRNA-synthetase controls. [src: gene_function_ecological_agora]

CRISPR-Cas gains were 58.7% recent and 2.4% ancient, producing a 24.5× recent-to-ancient ratio. [src: gene_function_ecological_agora]

TCS histidine-kinase gains were 45.1% recent and 4.4% ancient, producing a 10.3× ratio. [src: gene_function_ecological_agora]

β-lactamase gains were 44.2% recent and 4.9% ancient, producing a 9.0× ratio. [src: gene_function_ecological_agora]

Clean tRNA-synthetase controls were 24.7% recent and 10.7% ancient, producing a 2.3× ratio. [src: gene_function_ecological_agora]

For Mycobacteriaceae mycolic-acid gains, 53,916 events comprised 79.87% recent, 16.72% older-recent, 3.41% mid, 0.00% older, and 0.00% ancient events. [src: gene_function_ecological_agora]

Across all mycolic-acid gains, the corresponding proportions were 48.79% recent, 31.81% older-recent, 9.60% mid, 6.12% older, and 3.68% ancient. [src: gene_function_ecological_agora]

Cyanobacteria PSII gains contained 2.05% ancient events, compared with 14.90% atlas-wide, consistent with a class-level donor-origin signature but not establishing donor identity. [src: gene_function_ecological_agora]

## Diagnostics and interpretation

The project paired Sankoff-derived gain depths with D2 annotation-density residualization and the leaf_consistency metric to diagnose bias and within-clade structure. [src: gene_function_ecological_agora]

Leaf_consistency was defined as the fraction of species in a recipient clade carrying a KO, and its mean value was 0.34 for recent gains and 0.20 for ancient gains. [src: gene_function_ecological_agora]

Hypothesis-specific leaf_consistency values were 0.88 for Cyanobacteriia × PSII, 0.41 for Bacteroidota × PUL, and 0.15 for Mycobacteriaceae × mycolic acid, against an atlas reference of 0.20. [src: gene_function_ecological_agora]

The low Mycobacteriaceae value indicated that the family-level mycolic result was a mixture of within-family sub-clades rather than a uniform family property. [src: gene_function_ecological_agora]

A follow-up sub-clade analysis found producer d = +0.394 for the mycolic-positive sub-clade comprising 10 of 13 genera, compared with family-rank d = +0.309 and mycolic-low sub-clade d = +0.211. [src: gene_function_ecological_agora]

## Findings and limitations

Sankoff diagnostics recovered a small relative horizontal-gene-transfer signal for Bacteroidota × PUL CAZymes, with Cohen’s d = 0.15, after the original absolute-zero Innovator-Exchange criterion was falsified at UniRef50 resolution. [src: gene_function_ecological_agora]

The Alm 2006 quantitative correlation was not reproduced across 18,989 species representatives because the analysis used a different substrate, a different gain-event definition, and a different definition of “recent.” [src: gene_function_ecological_agora]

The project reported four Pearson r values of 0.288, 0.157, 0.100, and 0.105, and four Spearman r values of 0.333, 0.222, 0.152, and 0.106 for the Alm 2006 reproduction framings. [src: gene_function_ecological_agora]

The qualitative TCS-HK architectural result remained supported by consumer-side KO-to-architecture concordance of r = 0.673, while producer concordance was exploratory at r = 0.093. [src: gene_function_ecological_agora]

Sankoff results were not comprehensively cross-validated against DTLOR or other modern reconciliation methods, and bootstrap confidence intervals for individual M22 events were deferred. [src: gene_function_ecological_agora]

Deep-rank donor identities were not resolved because per-CDS sequence data were unavailable in queryable BERDL schemas. [src: gene_function_ecological_agora]

M26 tree-based donor inference remained exploratory and algebraically counted potential family-mate donors, which biased classifications toward Open-Innovator assignments. [src: gene_function_ecological_agora]

## Related pages

- [[summaries/gene_function_ecological_agora__REPORT]] — source-project summary. [src: gene_function_ecological_agora]
- [[concepts/gene-function-acquisition-depth]] — cross-project synthesis of acquisition-depth signatures and rank-attributed gains.
- [[concepts/pangenome-integration]] — integration of KO presence, pangenome openness, GTDB phylogeny, and genome-context measurements.
- [[entities/gtdb]] — taxonomic reference framework used for the 18,989-species atlas.
- [[entities/tnseq]] — another method represented in the wider BERIL corpus for gene-function and fitness analysis.
