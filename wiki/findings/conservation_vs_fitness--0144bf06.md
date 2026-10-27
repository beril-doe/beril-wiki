---
type: "Finding"
description: "The main Escherichia coli clade was absent from the pangenome (too many genomes), and Keio (E. coli BW25113) mapped to the small s__Escherichia_coli_E clade at only 26.1% coverage."
finding_id: "conservation_vs_fitness--0144bf06"
result: "null result"
source: "conservation_vs_fitness"
quantities: [{"value": "26.1%", "what": "coverage of Keio (E. coli BW25113) mapping to the s__Escherichia_coli_E clade", "unit": "%", "denominator": "", "scope": "Keio, small clade"}]
caveat: "34 organisms had >=90% coverage but only 33 were used downstream because Dyella79 was excluded for a locus tag mismatch."
first_added: "2026-10-27"
source_hash: "e0d31ced5965dc2bd3597dc43f0c63a33ad3497af8e9ec712d9369ae6c9aa197"
---
# Main E. coli clade absent from pangenome; Keio maps at low coverage

The main Escherichia coli clade was absent from the pangenome (too many genomes), and Keio (E. coli BW25113) mapped to the small s__Escherichia_coli_E clade at only 26.1% coverage. [src: conservation_vs_fitness]

## Key figures

- **26.1%**: coverage of Keio (E. coli BW25113) mapping to the s__Escherichia_coli_E clade (scope Keio, small clade) [src: conservation_vs_fitness]

## Evidence

> - **E. coli excluded**: The main *E. coli* clade was absent from the pangenome (too many genomes). *Keio* (E. coli BW25113) mapped to the small `s__Escherichia_coli_E` clade at only 26.1% coverage. [src: conservation_vs_fitness]

From the report [[summaries/conservation_vs_fitness__REPORT]].

## Caveat

34 organisms had >=90% coverage but only 33 were used downstream because Dyella79 was excluded for a locus tag mismatch. [src: conservation_vs_fitness]

> - 34 organisms have >=90% coverage; 33 used for downstream analysis (Dyella79 excluded due to locus tag mismatch) [src: conservation_vs_fitness]

## Other caveats in this report

- Putative essential genes were slightly shorter on average, consistent with possible transposon-insertion bias. [src: conservation_vs_fitness]
- The report characterizes the essential-core association as modest (OR=1.56), noting that many genes are core irrespective of essentiality. [src: conservation_vs_fitness]
- The report cites TraDIS work in E. coli K-12 as a precedent for gene-length bias in transposon-based essentiality calls. [src: conservation_vs_fitness]
- The putative-essential definition is an upper bound: absent fitness data may reflect short genes, low-complexity regions, or scaffold edges rather than essentiality; shorter average gene length suggests some insertion bias. [src: conservation_vs_fitness]
- Two-genome clades can yield trivially high core fractions—a gene present in both is 100% core—weakening core/auxiliary discrimination. [src: conservation_vs_fitness]
