---
type: "Finding"
description: "Adding labile carbon alongside lignin (Group LC) increases Acinetobacter dominance (41.7% in LC vs 25.2% in L), while Pseudomonas decreases and Aeromonas emerges as a major component."
finding_id: "lignin_community_enrichment--237f0536"
result: "observation"
source: "lignin_community_enrichment"
quantities: [{"value": "41.7%", "what": "Acinetobacter in LC", "unit": "", "denominator": "", "scope": ""}, {"value": "25.2%", "what": "Acinetobacter in L", "unit": "", "denominator": "", "scope": ""}]
caveat: "n=3 per group constrains statistical power. Pairwise tests (Mann-Whitney, pairwise PERMANOVA) cannot reach significance with 3 vs 3 comparisons (permutation floor)."
first_added: "2026-11-24"
source_hash: "f0bce929a335ab8e8ef7a4731d9934d5e53d9244e175f9b21ac411501aad0360"
---
# Labile carbon shifts lignin communities toward Acinetobacter and Aeromonas

Adding labile carbon alongside lignin (Group LC) increases Acinetobacter dominance (41.7% in LC vs 25.2% in L), while Pseudomonas decreases and Aeromonas emerges as a major component. [src: lignin_community_enrichment]

## Key figures

- **41.7%**: Acinetobacter in LC [src: lignin_community_enrichment]
- **25.2%**: Acinetobacter in L [src: lignin_community_enrichment]

## Evidence

> Adding labile carbon alongside lignin (Group LC) shifts the bacterial community away from the lignin-only profile: Acinetobacter dominance increases (41.7% in LC vs 25.2% in L), Pseudomonas decreases (23.0% vs 39.3%), and Aeromonas emerges as a major component (20.2% vs 0.1%). [src: lignin_community_enrichment]

From the report [[summaries/lignin_community_enrichment__REPORT]].

## Caveat

n=3 per group constrains statistical power. Pairwise tests (Mann-Whitney, pairwise PERMANOVA) cannot reach significance with 3 vs 3 comparisons (permutation floor). [src: lignin_community_enrichment]

> **n=3 per group** constrains statistical power. Pairwise tests (Mann-Whitney, pairwise PERMANOVA) cannot reach significance with 3 vs 3 comparisons (permutation floor). [src: lignin_community_enrichment]

## Other caveats in this report

- Poor ITS replicate consistency limits statistical inference: within-group Bray-Curtis distances reach 0.99–1.00 for several Round 2 groups versus 0.09 for 16S. [src: lignin_community_enrichment]
- With n=3 per group, pairwise Mann-Whitney U tests have minimum achievable p-value 0.10 because only 10 permutations are possible for 3 vs 3, preventing FDR-corrected significance for individual OTUs. [src: lignin_community_enrichment]
- Pairwise PERMANOVA with 3 vs 3 samples has a permutation floor of p~0.10. [src: lignin_community_enrichment]
- The report states that CLR differences and R² effect sizes remain interpretable even when p-values are constrained. [src: lignin_community_enrichment]
- The report cautions that dispersion differences contribute to lignin-enrichment PERMANOVA signals, although group separation is real. [src: lignin_community_enrichment]
