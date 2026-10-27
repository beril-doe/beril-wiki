---
type: "Finding"
description: "Of 866 genes with both FBA flux predictions and TnSeq essentiality calls, 639 (73.8%) are concordant, and the discordant 26% are candidates for model refinement or may reflect regulatory effects not captured by FBA."
finding_id: "acinetobacter_adp1_explorer--1cfedc83"
result: "observation"
source: "acinetobacter_adp1_explorer"
quantities: [{"value": "639", "what": "genes with concordant FBA and TnSeq essentiality calls", "unit": "genes", "denominator": "866 genes with both FBA and TnSeq data", "scope": "Acinetobacter baylyi ADP1 database"}, {"value": "73.8%", "what": "fraction of genes concordant between FBA and TnSeq", "unit": "percent", "denominator": "866 genes", "scope": ""}, {"value": "26%", "what": "discordant fraction of genes", "unit": "percent", "denominator": "866 genes", "scope": ""}]
caveat: "No gene has data across all 6 modalities, and FBA flux data is the sparsest (15% of genes), limiting the concordance analysis to 866 genes."
first_added: "2026-10-27"
source_hash: "ec7429b1cf2b99caae21a458ffae48609efc6384c9a4b7e3a9b1385d70024218"
---
# FBA and TnSeq essentiality agree for about three-quarters of shared genes

Of 866 genes with both FBA flux predictions and TnSeq essentiality calls, 639 (73.8%) are concordant, and the discordant 26% are candidates for model refinement or may reflect regulatory effects not captured by FBA. [src: acinetobacter_adp1_explorer]

## Key figures

- **639 genes**: genes with concordant FBA and TnSeq essentiality calls (denominator 866 genes with both FBA and TnSeq data; scope Acinetobacter baylyi ADP1 database) [src: acinetobacter_adp1_explorer]
- **73.8%**: fraction of genes concordant between FBA and TnSeq (denominator 866 genes) [src: acinetobacter_adp1_explorer]
- **26%**: discordant fraction of genes (denominator 866 genes) [src: acinetobacter_adp1_explorer]

## Evidence

> Of 866 genes with both FBA flux predictions and TnSeq essentiality calls, 639 (73.8%) are concordant. The discordant 26% — genes where the metabolic model and experimental data disagree — are candidates for model refinement or may reflect regulatory effects not captured by FBA. [src: acinetobacter_adp1_explorer]

From the report [[summaries/acinetobacter_adp1_explorer__REPORT]].

## Caveat

No gene has data across all 6 modalities, and FBA flux data is the sparsest (15% of genes), limiting the concordance analysis to 866 genes. [src: acinetobacter_adp1_explorer]

> - **Data modality overlap**: No gene has data across all 6 modalities. FBA flux data is the sparsest (15% of genes), limiting the concordance analysis to 866 genes. [src: acinetobacter_adp1_explorer]

## Other caveats in this report

- Of 121,519 growth predictions across 14 genomes, 105,376 (87%) required at least one gapfilled reaction; false negatives had higher mean gap counts than correct predictions. Prediction reliability therefore depends on gapfilling quality. [src: acinetobacter_adp1_explorer]
- Although reported as 100% complete, the three-table cluster mapping may have split-or-merge edge cases. [src: acinetobacter_adp1_explorer]
- The report cautions that 87% of growth predictions depend on gapfilled reactions and that 243 missing functions limit genomic support. [src: acinetobacter_adp1_explorer]
- The database covers only *Acinetobacter baylyi*; comparable databases would be needed for direct cross-species comparisons. [src: acinetobacter_adp1_explorer]
- A 37-table PhageFoundry Acinetobacter genome-browser collection was identified but not deeply queried. [src: acinetobacter_adp1_explorer]
