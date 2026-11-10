---
type: "Finding"
description: "86.1% of putative essential genes were core versus 81.2% of non-essential genes."
finding_id: "conservation_vs_fitness--e95508d3"
result: "observation"
source: "conservation_vs_fitness"
quantities: [{"value": "86.1%", "what": "share of putative essential genes that are core", "unit": "%", "denominator": "putative essential genes", "scope": ""}, {"value": "81.2%", "what": "share of non-essential genes that are core", "unit": "%", "denominator": "non-essential genes", "scope": ""}]
caveat: "The report characterizes the enrichment as modest (OR=1.56), reflecting that most genes in well-characterized bacteria are core regardless of essentiality."
first_added: "2026-10-27"
source_hash: "e0d31ced5965dc2bd3597dc43f0c63a33ad3497af8e9ec712d9369ae6c9aa197"
---
# Putative essential genes are modestly more often core than non-essential genes

86.1% of putative essential genes were core versus 81.2% of non-essential genes. [src: conservation_vs_fitness]

## Key figures

- **86.1%**: share of putative essential genes that are core (denominator putative essential genes) [src: conservation_vs_fitness]
- **81.2%**: share of non-essential genes that are core (denominator non-essential genes) [src: conservation_vs_fitness]

## Evidence

> - Essential genes are **86.1% core** vs 81.2% for non-essential genes [src: conservation_vs_fitness]

From the report [[summaries/conservation_vs_fitness__REPORT]].

## Caveat

The report characterizes the enrichment as modest (OR=1.56), reflecting that most genes in well-characterized bacteria are core regardless of essentiality. [src: conservation_vs_fitness]

> - Our finding that essential genes are enriched in core clusters aligns with the general expectation that genes required for viability are conserved across a species. However, the enrichment is modest (OR=1.56), reflecting that most genes in well-characterized bacteria are core regardless of essentiality. [src: conservation_vs_fitness]

## Other caveats in this report

- 34 organisms had >=90% mapping coverage, but only 33 entered downstream analysis because Dyella79 had a locus-tag mismatch. [src: conservation_vs_fitness]
- Putative essential genes were slightly shorter on average, consistent with possible transposon-insertion bias. [src: conservation_vs_fitness]
- The report cites TraDIS work in E. coli K-12 as a precedent for gene-length bias in transposon-based essentiality calls. [src: conservation_vs_fitness]
- The putative-essential definition is an upper bound: absent fitness data may reflect short genes, low-complexity regions, or scaffold edges rather than essentiality; shorter average gene length suggests some insertion bias. [src: conservation_vs_fitness]
- Two-genome clades can yield trivially high core fractions—a gene present in both is 100% core—weakening core/auxiliary discrimination. [src: conservation_vs_fitness]
