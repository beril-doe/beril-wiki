---
type: "Concept"
description: "Whether prior enrichment history, rather than current carbon source, determines community composition after sequential passaging; stops at the mechanisms behind memory."
sources: ["summaries/lignin_community_enrichment__REPORT.md"]
---
# Ecological memory and historical contingency in serially passaged communities

In one lignin-enrichment passaging experiment, communities with different Round 1 histories did not converge under identical Round 2 conditions. The report reads this as ecological memory. [src: lignin_community_enrichment] Bacterial history effects outweigh current carbon source in [[entities/permanova]] (permutational multivariate analysis of variance) tests. [src: lignin_community_enrichment] The fungal signal is not statistically detectable. [src: lignin_community_enrichment] All evidence comes from this one project ([[summaries/lignin_community_enrichment__REPORT]]). The page does not cover the mechanisms behind memory.

## Bacterial evidence for memory

Bacterial communities with different Round 1 (R1) histories did not converge under identical Round 2 (R2) conditions. The report presents this as direct evidence for ecological memory. [src: lignin_community_enrichment]

Mean Bray-Curtis distances separate history effects from R2 condition effects:

| Comparison | Mean distance | Report's reading |
|---|---|---|
| L-L vs LC-L (different history, same R2=L) | 0.507 | History signal persists [src: lignin_community_enrichment] |
| L-LC vs LC-LC (different history, same R2=LC) | 0.486 | History signal persists [src: lignin_community_enrichment] |
| L-L vs L-LC (same history=L, different R2) | 0.441 | R2 condition effect [src: lignin_community_enrichment] |
| LC-L vs LC-LC (same history=LC, different R2) | 0.306 | R2 condition effect [src: lignin_community_enrichment] |

The history/R2 ratios are 1.15 (R2=L) and 1.59 (R2=LC). Values above 1 mean enrichment history affects composition more than the current carbon source. [src: lignin_community_enrichment]

The memory index is about 0.50. Communities with different R1 histories keep roughly half of the maximum possible divergence under identical R2 conditions. [src: lignin_community_enrichment]

Many taxa persisted across rounds. In L to L-L passages, 81% of R1 OTUs (operational taxonomic units) were retained in R2. In LC to LC-LC passages, 91% were retained. [src: lignin_community_enrichment] Core taxa were maintained throughout the passage series. [src: lignin_community_enrichment]

## PERMANOVA partitioning

The factorial PERMANOVA on the 12 Round 2 bacterial samples gives the strongest evidence. R1 history explains 58.9% of community variance (F=14.31, R²=0.589, p=0.002). Current R2 carbon source explains 32.7% (F=4.85, R²=0.327, p=0.018). [src: lignin_community_enrichment] The report calls this design its most statistically powered test, and both factors are significant. [src: lignin_community_enrichment] The combined group factor gave F=41.12, R²=0.939, p=0.001. [src: lignin_community_enrichment]

## Fungal null result

The fungal ITS (internal transcribed spacer) data do not show the memory signal statistically. R1 history gave F=1.49, R²=0.142, p=0.090. R2 labile carbon gave F=1.71, R²=0.160, p=0.090. [src: lignin_community_enrichment] The report notes this limits inference for ITS. [src: lignin_community_enrichment] See [[concepts/small-sample-limits-in-community-amplicon-statistics]].

## Interpretation

The report reads the non-convergence as consistent with priority effects and historical contingency. Once labile carbon establishes a copiotrophic community in R1, it resists convergence with lignin-only histories. [src: lignin_community_enrichment] This is the report's interpretation, not a tested mechanism. It relates the result to Hawkes & Keitt (2015), who showed that microbial composition depends on the order and timing of environmental changes. [src: lignin_community_enrichment] The report claims controlled experimental evidence for ecological memory in lignin-degrading communities using sequential passaging. [src: lignin_community_enrichment]

## Open Directions

- Add more replicates or Round 3 passages to the fungal ITS design. This would test whether the p=0.090 result reflects low power or absent memory.
- Run a reciprocal switch or longer passage series. This would show whether the roughly 0.50 memory index decays with further passaging.
- Compare taxon-level changes between L and LC histories. This would test whether retained R1 OTUs carry the history signal.
- Inoculate copiotroph-enriched communities into lignin-only conditions. This would test the priority-effect hypothesis directly.
