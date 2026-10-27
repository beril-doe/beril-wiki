---
type: "Finding"
description: "Latent capabilities showed slightly higher mean conservation than active dependencies (Mann-Whitney U, p = 0.94 for active > latent; rank-biserial r = 0.052), so H2a (pathway-level conservation difference) is not supported."
finding_id: "metabolic_capability_dependency--b6cd74ee"
result: "null result"
source: "metabolic_capability_dependency"
quantities: [{"value": "0.94", "what": "Mann-Whitney U p-value for active > latent conservation", "unit": "", "denominator": "", "scope": "H2a test"}, {"value": "0.052", "what": "rank-biserial effect size", "unit": "r", "denominator": "", "scope": "latent versus active pathways"}]
caveat: "Conservation here is pathway-completeness per genome, a coarse measure that cannot detect partial gene erosion within an otherwise complete pathway."
first_added: "2026-10-27"
source_hash: "1412a5c1aa7711732d548b57744f3324a207e5eba6d0b4052c8882ac9cc593fe"
---
# Latent pathways are not less conserved than active pathways

Latent capabilities showed slightly higher mean conservation than active dependencies (Mann-Whitney U, p = 0.94 for active > latent; rank-biserial r = 0.052), so H2a (pathway-level conservation difference) is not supported. [src: metabolic_capability_dependency]

## Key figures

- **0.94**: Mann-Whitney U p-value for active > latent conservation (scope H2a test) [src: metabolic_capability_dependency]
- **0.052 r**: rank-biserial effect size (scope latent versus active pathways) [src: metabolic_capability_dependency]

## Evidence

> Latent capabilities showed slightly *higher* mean conservation than active dependencies (Mann-Whitney U, p = 0.94 for active > latent; rank-biserial r = 0.052). H2a is not supported. [src: metabolic_capability_dependency]

From the report [[summaries/metabolic_capability_dependency__REPORT]].

## Caveat

Conservation here is pathway-completeness per genome, a coarse measure that cannot detect partial gene erosion within an otherwise complete pathway. [src: metabolic_capability_dependency]

> 1. **Measurement granularity**: `conservation_rate` here captures whether the pathway is complete in each genome in the species clade. This is a coarse measure — it does not detect partial gene erosion (individual gene deletions within an otherwise complete pathway). [src: metabolic_capability_dependency]

## Other caveats in this report

- Across 16 threshold combinations, the latent fraction ranged from 4.7% to 21.1% (SD = 5.9 percentage points), versus 15.8% at default thresholds; the estimated fraction is moderately threshold-sensitive. [src: metabolic_capability_dependency]
- Deoxyribonate and myoinositol were absent from all analyses for lack of SEED matches; phenylalanine and tyrosine entered via phe and tyr abbreviations; alanine was excluded from classification because fewer than 3 SEED-annotated genes met coverage. [src: metabolic_capability_dependency]
- The report interprets the positive clade-level openness association alongside the null pathway-level conservation comparison as mixed evidence for the Black Queen framework, not uniform support. [src: metabolic_capability_dependency]
- Fitness coverage of only 48 organisms may inflate apparent conservation when other members of their species clades were not fitness-tested. [src: metabolic_capability_dependency]
- SEED-based proxy mapping can introduce false-positive pathway genes, dilute fitness signals, and misclassify pathways. [src: metabolic_capability_dependency]
