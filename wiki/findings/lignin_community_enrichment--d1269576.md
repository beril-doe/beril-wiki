---
type: "Finding"
description: "Observed bacterial OTUs drop from 1,594 to 163 after lignin enrichment, a 90% reduction."
finding_id: "lignin_community_enrichment--d1269576"
result: "observation"
source: "lignin_community_enrichment"
quantities: [{"value": "1,594", "what": "observed OTUs in Base", "unit": "", "denominator": "", "scope": ""}, {"value": "163", "what": "observed OTUs after lignin enrichment", "unit": "", "denominator": "", "scope": ""}, {"value": "90%", "what": "reduction in observed OTUs", "unit": "", "denominator": "", "scope": ""}]
caveat: "Effect sizes (CLR differences, R\u00b2 values) remain interpretable even when p-values are constrained."
first_added: "2026-11-24"
source_hash: "f0bce929a335ab8e8ef7a4731d9934d5e53d9244e175f9b21ac411501aad0360"
---
# Lignin enrichment collapses bacterial OTU richness

Observed bacterial OTUs drop from 1,594 to 163 after lignin enrichment, a 90% reduction. [src: lignin_community_enrichment]

## Key figures

- **1,594**: observed OTUs in Base [src: lignin_community_enrichment]
- **163**: observed OTUs after lignin enrichment [src: lignin_community_enrichment]
- **90%**: reduction in observed OTUs [src: lignin_community_enrichment]

## Evidence

> Alpha diversity drops dramatically: Shannon index from 6.46 (Base) to 3.16 (L), and observed OTUs from 1,594 to 163 — a 90% reduction. [src: lignin_community_enrichment]

From the report [[summaries/lignin_community_enrichment__REPORT]].

## Caveat

Effect sizes (CLR differences, R² values) remain interpretable even when p-values are constrained. [src: lignin_community_enrichment]

> Effect sizes (CLR differences, R² values) remain interpretable even when p-values are constrained. [src: lignin_community_enrichment]

## Other caveats in this report

- Poor ITS replicate consistency limits statistical inference: within-group Bray-Curtis distances reach 0.99–1.00 for several Round 2 groups versus 0.09 for 16S. [src: lignin_community_enrichment]
- With n=3 per group, pairwise Mann-Whitney U tests have minimum achievable p-value 0.10 because only 10 permutations are possible for 3 vs 3, preventing FDR-corrected significance for individual OTUs. [src: lignin_community_enrichment]
- Pairwise PERMANOVA with 3 vs 3 samples has a permutation floor of p~0.10. [src: lignin_community_enrichment]
- The report cautions that dispersion differences contribute to lignin-enrichment PERMANOVA signals, although group separation is real. [src: lignin_community_enrichment]
- Extreme fungal replicate variability limits ITS statistical inference in the lignin-enrichment study, whose ITS PERMANOVA R² is lower than that of bacterial communities (0.582 vs 0.979). [src: lignin_community_enrichment]
