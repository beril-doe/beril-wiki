---
type: "Finding"
description: "Of 866 ADP1 genes with both FBA flux predictions and TnSeq essentiality calls, 639 (73.8%) are concordant."
finding_id: "acinetobacter_adp1_explorer--6f19fce6"
result: "observation"
source: "acinetobacter_adp1_explorer"
quantities: [{"value": "639", "what": "genes with concordant FBA and TnSeq essentiality calls", "unit": "genes", "denominator": "866 genes with both FBA flux predictions and TnSeq essentiality calls", "scope": "ADP1"}, {"value": "73.8%", "what": "fraction concordant", "unit": "percent", "denominator": "866 genes", "scope": "ADP1"}]
caveat: "FBA flux data is the sparsest modality (15% of genes), limiting the concordance analysis to 866 genes."
first_added: "2026-11-24"
source_hash: "ec7429b1cf2b99caae21a458ffae48609efc6384c9a4b7e3a9b1385d70024218"
---
# FBA and TnSeq essentiality calls agree for most ADP1 genes

Of 866 ADP1 genes with both FBA flux predictions and TnSeq essentiality calls, 639 (73.8%) are concordant. [src: acinetobacter_adp1_explorer]

## Key figures

- **639 genes**: genes with concordant FBA and TnSeq essentiality calls (denominator 866 genes with both FBA flux predictions and TnSeq essentiality calls; scope ADP1) [src: acinetobacter_adp1_explorer]
- **73.8%**: fraction concordant (denominator 866 genes; scope ADP1) [src: acinetobacter_adp1_explorer]

## Evidence

> Of 866 genes with both FBA flux predictions and TnSeq essentiality calls, 639 (73.8%) are concordant. [src: acinetobacter_adp1_explorer]

From the report [[summaries/acinetobacter_adp1_explorer__REPORT]].

## Caveat

FBA flux data is the sparsest modality (15% of genes), limiting the concordance analysis to 866 genes. [src: acinetobacter_adp1_explorer]

> FBA flux data is the sparsest (15% of genes), limiting the concordance analysis to 866 genes. [src: acinetobacter_adp1_explorer]

## Other caveats in this report

- The 120 unmatched ADP1 database reactions (9%) may be custom or draft reactions not yet in ModelSEED. [src: acinetobacter_adp1_explorer]
- The discordant 26% of ADP1 genes with FBA and experimental essentiality data are model-refinement candidates or may reflect regulatory effects absent from FBA. [src: acinetobacter_adp1_explorer]
- The report states that heavy gapfilling dependence tightly couples Acinetobacter growth prediction accuracy to gapfilling quality. [src: acinetobacter_adp1_explorer]
- No gene in the Acinetobacter baylyi ADP1 database has data across all 6 modalities. [src: acinetobacter_adp1_explorer]
- The KBase Data Lakehouse–ADP1 pangenome cluster mapping goes through 3 tables and is 100% complete, but may have edge cases for clusters that split or merge between the two pangenome analyses. [src: acinetobacter_adp1_explorer]
