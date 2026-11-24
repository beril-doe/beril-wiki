---
type: "Finding"
description: "The ADP1 database uses mmseqs2-style cluster IDs while the KBase Data Lakehouse uses centroid gene IDs, with 0% direct string match."
finding_id: "acinetobacter_adp1_explorer--88679c12"
result: "null result"
source: "acinetobacter_adp1_explorer"
quantities: [{"value": "0%", "what": "direct string match between cluster ID conventions", "unit": "", "denominator": "", "scope": ""}]
caveat: "The cluster mapping goes through 3 tables; while 100% complete, this indirection could introduce edge cases for clusters that split or merge between the two pangenome analyses."
first_added: "2026-11-24"
source_hash: "ec7429b1cf2b99caae21a458ffae48609efc6384c9a4b7e3a9b1385d70024218"
---
# ADP1 and Lakehouse cluster IDs share no direct string matches

The ADP1 database uses mmseqs2-style cluster IDs while the KBase Data Lakehouse uses centroid gene IDs, with 0% direct string match. [src: acinetobacter_adp1_explorer]

## Key figures

- **0%**: direct string match between cluster ID conventions [src: acinetobacter_adp1_explorer]

## Evidence

> The ADP1 database uses mmseqs2-style cluster IDs (`NHSXFYEX_mmseqsCluster_NNNN`) while BERDL uses centroid gene IDs (`NC_005966.1_1024`) — completely different naming conventions with 0% direct string match. [src: acinetobacter_adp1_explorer]

From the report [[summaries/acinetobacter_adp1_explorer__REPORT]].

## Caveat

The cluster mapping goes through 3 tables; while 100% complete, this indirection could introduce edge cases for clusters that split or merge between the two pangenome analyses. [src: acinetobacter_adp1_explorer]

> - **Pangenome cluster mapping is indirect**: The BERDL ↔ ADP1 cluster mapping goes through 3 tables. While 100% complete, this indirection could introduce edge cases for clusters that split or merge between the two pangenome analyses. [src: acinetobacter_adp1_explorer]

## Other caveats in this report

- The 120 unmatched ADP1 database reactions (9%) may be custom or draft reactions not yet in ModelSEED. [src: acinetobacter_adp1_explorer]
- The discordant 26% of ADP1 genes with FBA and experimental essentiality data are model-refinement candidates or may reflect regulatory effects absent from FBA. [src: acinetobacter_adp1_explorer]
- The report states that heavy gapfilling dependence tightly couples Acinetobacter growth prediction accuracy to gapfilling quality. [src: acinetobacter_adp1_explorer]
- No gene in the Acinetobacter baylyi ADP1 database has data across all 6 modalities. [src: acinetobacter_adp1_explorer]
- FBA flux data are the sparsest modality in the Acinetobacter baylyi ADP1 database, covering 15% of genes and limiting concordance analysis to 866 genes. [src: acinetobacter_adp1_explorer]
