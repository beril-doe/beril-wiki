---
type: "Finding"
description: "For ITS, the PERMANOVA R\u00b2 is lower (0.582 vs 0.979) and the ecological memory signal is not statistically detectable (R1 history p=0.090)."
finding_id: "lignin_community_enrichment--8b7c9a44"
result: "null result"
source: "lignin_community_enrichment"
quantities: [{"value": "0.582 vs 0.979", "what": "PERMANOVA R\u00b2, ITS first, as stated in the report", "unit": "", "denominator": "", "scope": ""}, {"value": "0.090", "what": "p-value for the R1 history effect in ITS", "unit": "", "denominator": "", "scope": "ITS"}]
caveat: "ITS replicate consistency is poor, with within-group Bray-Curtis distances of 0.99\u20131.00 for several Round 2 groups versus 0.09 for 16S, limiting ITS statistical inference."
first_added: "2026-10-27"
source_hash: "f0bce929a335ab8e8ef7a4731d9934d5e53d9244e175f9b21ac411501aad0360"
---
# Ecological memory not detectable in fungal ITS data

For ITS, the PERMANOVA R² is lower (0.582 vs 0.979) and the ecological memory signal is not statistically detectable (R1 history p=0.090). [src: lignin_community_enrichment]

## Key figures

- **0.582 vs 0.979**: PERMANOVA R², ITS first, as stated in the report [src: lignin_community_enrichment]
- **0.090**: p-value for the R1 history effect in ITS (scope ITS) [src: lignin_community_enrichment]

## Evidence

> This limits statistical inference for ITS — the PERMANOVA R² is lower (0.582 vs 0.979) and the ecological memory signal is not statistically detectable in ITS (R1 history p=0.090). [src: lignin_community_enrichment]

From the report [[summaries/lignin_community_enrichment__REPORT]].

## Caveat

ITS replicate consistency is poor, with within-group Bray-Curtis distances of 0.99–1.00 for several Round 2 groups versus 0.09 for 16S, limiting ITS statistical inference. [src: lignin_community_enrichment]

> ITS diversity collapses to 3–8 OTUs per group after enrichment (from 253 in Base). However, ITS replicate consistency is poor — within-group Bray-Curtis distances reach 0.99–1.00 for several Round 2 groups (vs 0.09 for 16S), limiting statistical inference for ITS. [src: lignin_community_enrichment]

## Other caveats in this report

- With n=3 per group, pairwise Mann–Whitney tests have a minimum achievable p-value of 0.10 and pairwise PERMANOVA has a p~0.10 floor; FDR significance for individual OTUs is unattainable, whereas pooled/global and n=12 factorial tests gain power. [src: lignin_community_enrichment]
- Significant PERMDISP for both markers (16S p=0.0004; ITS p=0.0001) means heterogeneous dispersion contributes to PERMANOVA separation. [src: lignin_community_enrichment]
- The report links the ~0.50 memory index and nonconvergence to a priority-effect hypothesis, rather than a directly measured mechanism. [src: lignin_community_enrichment]
- Bacterial 16S replicates had within-group Bray–Curtis distance 0.09, whereas ITS replicates had 0.65, reaching 0.99–1.00 for Round-2 groups. [src: lignin_community_enrichment]
- Fungal ITS replicate variability was high: within-group Bray–Curtis distance was 0.65 and reached 0.99–1.00 in Round 2 groups. [src: lignin_community_enrichment]
