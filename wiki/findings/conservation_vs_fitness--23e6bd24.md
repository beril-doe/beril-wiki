---
type: "Finding"
description: "18 of 33 organisms showed statistically significant enrichment of essential genes in core clusters by Fisher's exact test with BH-FDR q < 0.05."
finding_id: "conservation_vs_fitness--23e6bd24"
result: "observation"
source: "conservation_vs_fitness"
quantities: [{"value": "18 of 33", "what": "organisms with significant essential-gene enrichment in core clusters", "unit": "organisms", "denominator": "33 organisms", "scope": "Fisher's exact test, BH-FDR q < 0.05"}]
caveat: "The essential-gene definition is an upper bound, since genes lacking fitness data may lack insertions because they are short, in low-complexity regions, or at scaffold edges, and essential genes are slightly shorter on average, suggesting some insertion bias."
first_added: "2026-10-27"
source_hash: "e0d31ced5965dc2bd3597dc43f0c63a33ad3497af8e9ec712d9369ae6c9aa197"
---
# Essential-gene core enrichment is significant in just over half of organisms

18 of 33 organisms showed statistically significant enrichment of essential genes in core clusters by Fisher's exact test with BH-FDR q < 0.05. [src: conservation_vs_fitness]

## Key figures

- **18 of 33 organisms**: organisms with significant essential-gene enrichment in core clusters (denominator 33 organisms; scope Fisher's exact test, BH-FDR q < 0.05) [src: conservation_vs_fitness]

## Evidence

> - **18 of 33 organisms** show statistically significant enrichment (Fisher's exact test, BH-FDR q < 0.05) [src: conservation_vs_fitness]

From the report [[summaries/conservation_vs_fitness__REPORT]].

## Caveat

The essential-gene definition is an upper bound, since genes lacking fitness data may lack insertions because they are short, in low-complexity regions, or at scaffold edges, and essential genes are slightly shorter on average, suggesting some insertion bias. [src: conservation_vs_fitness]

> - **Essential gene definition is an upper bound**: Genes without fitness data may lack transposon insertions due to being short, in low-complexity regions, or at scaffold edges -- not necessarily because they are essential. Gene length validation shows essential genes are slightly shorter on average, suggesting some insertion bias. [src: conservation_vs_fitness]

## Other caveats in this report

- 34 organisms had >=90% mapping coverage, but only 33 entered downstream analysis because Dyella79 had a locus-tag mismatch. [src: conservation_vs_fitness]
- Putative essential genes were slightly shorter on average, consistent with possible transposon-insertion bias. [src: conservation_vs_fitness]
- The report characterizes the essential-core association as modest (OR=1.56), noting that many genes are core irrespective of essentiality. [src: conservation_vs_fitness]
- The report cites TraDIS work in E. coli K-12 as a precedent for gene-length bias in transposon-based essentiality calls. [src: conservation_vs_fitness]
- Two-genome clades can yield trivially high core fractions—a gene present in both is 100% core—weakening core/auxiliary discrimination. [src: conservation_vs_fitness]
