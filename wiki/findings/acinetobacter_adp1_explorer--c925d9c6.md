---
type: "Finding"
description: "20% of genes (177/866) change FBA flux class between rich and minimal media, which the report reads as condition-dependent metabolic rewiring."
finding_id: "acinetobacter_adp1_explorer--c925d9c6"
result: "observation"
source: "acinetobacter_adp1_explorer"
quantities: [{"value": "177", "what": "genes changing FBA flux class between rich and minimal media", "unit": "genes", "denominator": "866 genes", "scope": "ADP1 FBA predictions"}, {"value": "20%", "what": "fraction of genes changing flux class", "unit": "percent", "denominator": "866 genes", "scope": ""}]
caveat: "Of 121,519 growth phenotype predictions across 14 genomes, 105,376 (87%) require at least one gapfilled reaction, so prediction accuracy is tightly coupled to gapfilling quality."
first_added: "2026-10-27"
source_hash: "ec7429b1cf2b99caae21a458ffae48609efc6384c9a4b7e3a9b1385d70024218"
---
# A fifth of genes change FBA flux class between media

20% of genes (177/866) change FBA flux class between rich and minimal media, which the report reads as condition-dependent metabolic rewiring. [src: acinetobacter_adp1_explorer]

## Key figures

- **177 genes**: genes changing FBA flux class between rich and minimal media (denominator 866 genes; scope ADP1 FBA predictions) [src: acinetobacter_adp1_explorer]
- **20%**: fraction of genes changing flux class (denominator 866 genes) [src: acinetobacter_adp1_explorer]

## Evidence

> 20% of genes (177/866) change FBA flux class between rich and minimal media, reflecting condition-dependent metabolic rewiring. [src: acinetobacter_adp1_explorer]

From the report [[summaries/acinetobacter_adp1_explorer__REPORT]].

## Caveat

Of 121,519 growth phenotype predictions across 14 genomes, 105,376 (87%) require at least one gapfilled reaction, so prediction accuracy is tightly coupled to gapfilling quality. [src: acinetobacter_adp1_explorer]

> Of 121,519 growth phenotype predictions across 14 genomes, 105,376 (87%) require at least one gapfilled reaction. This heavy dependence on gapfilling means that prediction accuracy is tightly coupled to gapfilling quality. False negatives have higher mean gap counts than correct predictions. [src: acinetobacter_adp1_explorer]

## Other caveats in this report

- No gene has all six modalities; FBA coverage is 15%, restricting the FBA–TnSeq concordance analysis to 866 genes. [src: acinetobacter_adp1_explorer]
- Although reported as 100% complete, the three-table cluster mapping may have split-or-merge edge cases. [src: acinetobacter_adp1_explorer]
- The report cautions that 87% of growth predictions depend on gapfilled reactions and that 243 missing functions limit genomic support. [src: acinetobacter_adp1_explorer]
- The database covers only *Acinetobacter baylyi*; comparable databases would be needed for direct cross-species comparisons. [src: acinetobacter_adp1_explorer]
- A 37-table PhageFoundry Acinetobacter genome-browser collection was identified but not deeply queried. [src: acinetobacter_adp1_explorer]
