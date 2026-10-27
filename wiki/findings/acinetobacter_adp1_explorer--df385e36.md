---
type: "Finding"
description: "Across 8 carbon sources, mean pairwise fitness correlation was r = 0.44, while urea fitness was nearly uncorrelated with quinate (r = 0.11) and weakly correlated with all other conditions (r = 0.12-0.28), which suggests that urea catabolism involves a largely independent set of genes."
finding_id: "acinetobacter_adp1_explorer--df385e36"
result: "inference"
source: "acinetobacter_adp1_explorer"
quantities: [{"value": "r = 0.44", "what": "mean pairwise correlation of mutant fitness", "unit": "correlation coefficient", "denominator": "", "scope": "8 carbon sources"}, {"value": "r = 0.11", "what": "urea-quinate fitness correlation", "unit": "correlation coefficient", "denominator": "", "scope": ""}, {"value": "r = 0.12-0.28", "what": "urea fitness correlation with all other conditions", "unit": "correlation coefficient", "denominator": "", "scope": ""}, {"value": "r = 0.58", "what": "butanediol-acetate fitness correlation, the strongest", "unit": "correlation coefficient", "denominator": "", "scope": ""}]
caveat: "The database covers only A. baylyi, so cross-species comparisons would require similar databases for other organisms."
first_added: "2026-10-27"
source_hash: "ec7429b1cf2b99caae21a458ffae48609efc6384c9a4b7e3a9b1385d70024218"
---
# Urea fitness nearly independent of other carbon-source fitness

Across 8 carbon sources, mean pairwise fitness correlation was r = 0.44, while urea fitness was nearly uncorrelated with quinate (r = 0.11) and weakly correlated with all other conditions (r = 0.12-0.28), which suggests that urea catabolism involves a largely independent set of genes. [src: acinetobacter_adp1_explorer]

## Key figures

- **r = 0.44 correlation coefficient**: mean pairwise correlation of mutant fitness (scope 8 carbon sources) [src: acinetobacter_adp1_explorer]
- **r = 0.11 correlation coefficient**: urea-quinate fitness correlation [src: acinetobacter_adp1_explorer]
- **r = 0.12-0.28 correlation coefficient**: urea fitness correlation with all other conditions [src: acinetobacter_adp1_explorer]
- **r = 0.58 correlation coefficient**: butanediol-acetate fitness correlation, the strongest [src: acinetobacter_adp1_explorer]

## Evidence

> Mutant growth fitness across 8 carbon sources shows moderate overall correlation (mean pairwise r = 0.44) but with notable outliers. Urea fitness is nearly uncorrelated with quinate (r = 0.11) and weakly correlated with all other conditions (r = 0.12-0.28), suggesting that urea catabolism involves a largely independent set of genes. Butanediol-acetate (r = 0.58) and butanediol-lactate (r = 0.53) show the strongest correlations, consistent with shared central carbon metabolism. [src: acinetobacter_adp1_explorer]

From the report [[summaries/acinetobacter_adp1_explorer__REPORT]].

## Caveat

The database covers only A. baylyi, so cross-species comparisons would require similar databases for other organisms. [src: acinetobacter_adp1_explorer]

> - **Single species**: This database covers only *A. baylyi*. Cross-species comparisons would require similar databases for other organisms. [src: acinetobacter_adp1_explorer]

## Other caveats in this report

- Of 121,519 growth predictions across 14 genomes, 105,376 (87%) required at least one gapfilled reaction; false negatives had higher mean gap counts than correct predictions. Prediction reliability therefore depends on gapfilling quality. [src: acinetobacter_adp1_explorer]
- No gene has all six modalities; FBA coverage is 15%, restricting the FBA–TnSeq concordance analysis to 866 genes. [src: acinetobacter_adp1_explorer]
- Although reported as 100% complete, the three-table cluster mapping may have split-or-merge edge cases. [src: acinetobacter_adp1_explorer]
- The report cautions that 87% of growth predictions depend on gapfilled reactions and that 243 missing functions limit genomic support. [src: acinetobacter_adp1_explorer]
- A 37-table PhageFoundry Acinetobacter genome-browser collection was identified but not deeply queried. [src: acinetobacter_adp1_explorer]
