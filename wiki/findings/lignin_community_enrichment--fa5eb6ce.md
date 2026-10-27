---
type: "Finding"
description: "The pre-registered per-group Procrustes M\u00b2 analysis to test 16S\u2013ITS concordance was not completed because extreme ITS replicate variability (within-group BC approaching 1.0 for Round 2 groups) would render it meaningless, leaving bacterial\u2013fungal concordance formally untested."
finding_id: "lignin_community_enrichment--fa5eb6ce"
result: "null result"
source: "lignin_community_enrichment"
quantities: [{"value": "approaching 1.0", "what": "within-group Bray-Curtis distance for Round 2 ITS groups", "unit": "Bray-Curtis distance", "denominator": "", "scope": "Round 2 ITS"}]
caveat: "Round 2 ITS within-group Bray-Curtis distances were near 1.0, so the report treats ITS-based findings as preliminary."
first_added: "2026-10-27"
source_hash: "f0bce929a335ab8e8ef7a4731d9934d5e53d9244e175f9b21ac411501aad0360"
---
# Planned bacterial–fungal Procrustes concordance test was not completed

The pre-registered per-group Procrustes M² analysis to test 16S–ITS concordance was not completed because extreme ITS replicate variability (within-group BC approaching 1.0 for Round 2 groups) would render it meaningless, leaving bacterial–fungal concordance formally untested. [src: lignin_community_enrichment]

## Key figures

- **approaching 1.0 Bray-Curtis distance**: within-group Bray-Curtis distance for Round 2 ITS groups (scope Round 2 ITS) [src: lignin_community_enrichment]

## Evidence

> **Procrustes analysis (pre-registered):** The research plan specified a per-group Procrustes M² analysis to formally test 16S–ITS concordance. This analysis was not completed because the extreme ITS replicate variability (within-group BC approaching 1.0 for Round 2 groups) would render the Procrustes rotation meaningless — rotating a cloud of near-random ITS points onto structured 16S ordination would produce high M² (poor fit) regardless of biological concordance. The qualitative comparison above captures the key finding: bacterial communities show robust, reproducible structure while fungal communities are dominated by stochastic variation at this sample size and sequencing depth, making formal concordance testing uninformative. [src: lignin_community_enrichment]

From the report [[summaries/lignin_community_enrichment__REPORT]].

## Caveat

Round 2 ITS within-group Bray-Curtis distances were near 1.0, so the report treats ITS-based findings as preliminary. [src: lignin_community_enrichment]

> - **ITS replicate consistency is poor** — within-group Bray-Curtis distances near 1.0 for Round 2 groups limit the reliability of ITS-based statistical tests. Findings from ITS should be considered preliminary. [src: lignin_community_enrichment]

## Other caveats in this report

- ITS richness fell from 253 OTUs in Base to 3–8 per enriched group, but Round 2 within-group Bray–Curtis distances reached 0.99–1.00 versus 0.09 for 16S, limiting ITS inference. [src: lignin_community_enrichment]
- With n=3 per group, pairwise Mann–Whitney tests have a minimum achievable p-value of 0.10 and pairwise PERMANOVA has a p~0.10 floor; FDR significance for individual OTUs is unattainable, whereas pooled/global and n=12 factorial tests gain power. [src: lignin_community_enrichment]
- Significant PERMDISP for both markers (16S p=0.0004; ITS p=0.0001) means heterogeneous dispersion contributes to PERMANOVA separation. [src: lignin_community_enrichment]
- The report links the ~0.50 memory index and nonconvergence to a priority-effect hypothesis, rather than a directly measured mechanism. [src: lignin_community_enrichment]
- Bacterial 16S replicates had within-group Bray–Curtis distance 0.09, whereas ITS replicates had 0.65, reaching 0.99–1.00 for Round-2 groups. [src: lignin_community_enrichment]
