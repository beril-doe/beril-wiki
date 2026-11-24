---
type: "Finding"
description: "After a single round of lignin enrichment, Pseudomonas (39.3%) and Acinetobacter (25.2%) become the dominant genera, together comprising >64% of 16S reads."
finding_id: "lignin_community_enrichment--aa7c506d"
result: "observation"
source: "lignin_community_enrichment"
quantities: [{"value": "39.3%", "what": "Pseudomonas share of 16S reads after one lignin round", "unit": "", "denominator": "", "scope": ""}, {"value": "25.2%", "what": "Acinetobacter share of 16S reads after one lignin round", "unit": "", "denominator": "", "scope": ""}, {"value": ">64%", "what": "combined Pseudomonas and Acinetobacter share of 16S reads", "unit": "", "denominator": "", "scope": ""}]
caveat: "With n=3 per group, pairwise Mann-Whitney U tests have a minimum achievable p-value of 0.10 (only 10 possible permutations for 3 vs 3), making FDR-corrected significance impossible for individual OTUs."
first_added: "2026-11-24"
source_hash: "f0bce929a335ab8e8ef7a4731d9934d5e53d9244e175f9b21ac411501aad0360"
---
# One lignin passage turns the bacterial community over almost completely

After a single round of lignin enrichment, Pseudomonas (39.3%) and Acinetobacter (25.2%) become the dominant genera, together comprising >64% of 16S reads. [src: lignin_community_enrichment]

## Key figures

- **39.3%**: Pseudomonas share of 16S reads after one lignin round [src: lignin_community_enrichment]
- **25.2%**: Acinetobacter share of 16S reads after one lignin round [src: lignin_community_enrichment]
- **>64%**: combined Pseudomonas and Acinetobacter share of 16S reads [src: lignin_community_enrichment]

## Evidence

> After a single round of lignin enrichment, Pseudomonas (39.3%) and Acinetobacter (25.2%) become the dominant genera, together comprising >64% of 16S reads. [src: lignin_community_enrichment]

From the report [[summaries/lignin_community_enrichment__REPORT]].

## Caveat

With n=3 per group, pairwise Mann-Whitney U tests have a minimum achievable p-value of 0.10 (only 10 possible permutations for 3 vs 3), making FDR-corrected significance impossible for individual OTUs. [src: lignin_community_enrichment]

> With n=3 per group, pairwise Mann-Whitney U tests have a minimum achievable p-value of 0.10 (only 10 possible permutations for 3 vs 3), making FDR-corrected significance impossible for individual OTUs. [src: lignin_community_enrichment]

## Other caveats in this report

- Poor ITS replicate consistency limits statistical inference: within-group Bray-Curtis distances reach 0.99–1.00 for several Round 2 groups versus 0.09 for 16S. [src: lignin_community_enrichment]
- Pairwise PERMANOVA with 3 vs 3 samples has a permutation floor of p~0.10. [src: lignin_community_enrichment]
- The report states that CLR differences and R² effect sizes remain interpretable even when p-values are constrained. [src: lignin_community_enrichment]
- The report cautions that dispersion differences contribute to lignin-enrichment PERMANOVA signals, although group separation is real. [src: lignin_community_enrichment]
- Extreme fungal replicate variability limits ITS statistical inference in the lignin-enrichment study, whose ITS PERMANOVA R² is lower than that of bacterial communities (0.582 vs 0.979). [src: lignin_community_enrichment]
