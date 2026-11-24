---
type: "Finding"
description: "Ecological memory is not statistically detectable in ITS (R1 history p=0.090), where the PERMANOVA R\u00b2 is lower (0.582 vs 0.979)."
finding_id: "lignin_community_enrichment--8b7c9a44"
result: "null result"
source: "lignin_community_enrichment"
quantities: [{"value": "0.090", "what": "p-value for R1 history in ITS", "unit": "", "denominator": "", "scope": ""}, {"value": "0.582", "what": "ITS PERMANOVA R\u00b2", "unit": "", "denominator": "", "scope": ""}]
caveat: "ITS replicate consistency is poor \u2014 within-group Bray-Curtis distances reach 0.99\u20131.00 for several Round 2 groups (vs 0.09 for 16S), limiting statistical inference for ITS."
first_added: "2026-11-24"
source_hash: "f0bce929a335ab8e8ef7a4731d9934d5e53d9244e175f9b21ac411501aad0360"
---
# Ecological memory not detectable in fungal communities

Ecological memory is not statistically detectable in ITS (R1 history p=0.090), where the PERMANOVA R² is lower (0.582 vs 0.979). [src: lignin_community_enrichment]

## Key figures

- **0.090**: p-value for R1 history in ITS [src: lignin_community_enrichment]
- **0.582**: ITS PERMANOVA R² [src: lignin_community_enrichment]

## Evidence

> This limits statistical inference for ITS — the PERMANOVA R² is lower (0.582 vs 0.979) and the ecological memory signal is not statistically detectable in ITS (R1 history p=0.090). [src: lignin_community_enrichment]

From the report [[summaries/lignin_community_enrichment__REPORT]].

## Caveat

ITS replicate consistency is poor — within-group Bray-Curtis distances reach 0.99–1.00 for several Round 2 groups (vs 0.09 for 16S), limiting statistical inference for ITS. [src: lignin_community_enrichment]

> However, ITS replicate consistency is poor — within-group Bray-Curtis distances reach 0.99–1.00 for several Round 2 groups (vs 0.09 for 16S), limiting statistical inference for ITS. [src: lignin_community_enrichment]

## Other caveats in this report

- With n=3 per group, pairwise Mann-Whitney U tests have minimum achievable p-value 0.10 because only 10 permutations are possible for 3 vs 3, preventing FDR-corrected significance for individual OTUs. [src: lignin_community_enrichment]
- Pairwise PERMANOVA with 3 vs 3 samples has a permutation floor of p~0.10. [src: lignin_community_enrichment]
- The report states that CLR differences and R² effect sizes remain interpretable even when p-values are constrained. [src: lignin_community_enrichment]
- The report cautions that dispersion differences contribute to lignin-enrichment PERMANOVA signals, although group separation is real. [src: lignin_community_enrichment]
- Extreme fungal replicate variability limits ITS statistical inference in the lignin-enrichment study, whose ITS PERMANOVA R² is lower than that of bacterial communities (0.582 vs 0.979). [src: lignin_community_enrichment]
