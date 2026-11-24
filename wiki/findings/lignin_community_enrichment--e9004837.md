---
type: "Finding"
description: "PERMANOVA on the 12 Round 2 samples shows R1 history explains 58.9% of community variance (F=14.31, R\u00b2=0.589, p=0.002), while current R2 carbon source explains only 32.7% (F=4.85, R\u00b2=0.327, p=0.018)."
finding_id: "lignin_community_enrichment--e9004837"
result: "observation"
source: "lignin_community_enrichment"
quantities: [{"value": "58.9%", "what": "variance explained by R1 history", "unit": "", "denominator": "", "scope": ""}, {"value": "32.7%", "what": "variance explained by current R2 carbon source", "unit": "", "denominator": "", "scope": ""}]
caveat: "PERMANOVA results should be interpreted alongside PERMDISP \u2014 the group separation is real but dispersion differences contribute to the signal."
first_added: "2026-11-24"
source_hash: "f0bce929a335ab8e8ef7a4731d9934d5e53d9244e175f9b21ac411501aad0360"
---
# Earlier enrichment history explains most later bacterial community variance

PERMANOVA on the 12 Round 2 samples shows R1 history explains 58.9% of community variance (F=14.31, R²=0.589, p=0.002), while current R2 carbon source explains only 32.7% (F=4.85, R²=0.327, p=0.018). [src: lignin_community_enrichment]

## Key figures

- **58.9%**: variance explained by R1 history [src: lignin_community_enrichment]
- **32.7%**: variance explained by current R2 carbon source [src: lignin_community_enrichment]

## Evidence

> PERMANOVA on the 12 Round 2 samples shows R1 history explains 58.9% of community variance (F=14.31, R²=0.589, p=0.002), while current R2 carbon source explains only 32.7% (F=4.85, R²=0.327, p=0.018). [src: lignin_community_enrichment]

From the report [[summaries/lignin_community_enrichment__REPORT]].

## Caveat

PERMANOVA results should be interpreted alongside PERMDISP — the group separation is real but dispersion differences contribute to the signal. [src: lignin_community_enrichment]

> PERMANOVA results should be interpreted alongside PERMDISP — the group separation is real but dispersion differences contribute to the signal. [src: lignin_community_enrichment]

## Other caveats in this report

- Poor ITS replicate consistency limits statistical inference: within-group Bray-Curtis distances reach 0.99–1.00 for several Round 2 groups versus 0.09 for 16S. [src: lignin_community_enrichment]
- With n=3 per group, pairwise Mann-Whitney U tests have minimum achievable p-value 0.10 because only 10 permutations are possible for 3 vs 3, preventing FDR-corrected significance for individual OTUs. [src: lignin_community_enrichment]
- Pairwise PERMANOVA with 3 vs 3 samples has a permutation floor of p~0.10. [src: lignin_community_enrichment]
- The report states that CLR differences and R² effect sizes remain interpretable even when p-values are constrained. [src: lignin_community_enrichment]
- Extreme fungal replicate variability limits ITS statistical inference in the lignin-enrichment study, whose ITS PERMANOVA R² is lower than that of bacterial communities (0.582 vs 0.979). [src: lignin_community_enrichment]
