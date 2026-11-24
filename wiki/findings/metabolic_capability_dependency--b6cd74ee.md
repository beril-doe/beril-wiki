---
type: "Finding"
description: "Latent capabilities showed slightly higher mean conservation than active dependencies (Mann-Whitney U, p = 0.94 for active > latent; rank-biserial r = 0.052), so H2a is not supported."
finding_id: "metabolic_capability_dependency--b6cd74ee"
result: "null result"
source: "metabolic_capability_dependency"
quantities: [{"value": "p = 0.94", "what": "Mann-Whitney U test for active > latent conservation", "unit": "", "denominator": "", "scope": ""}, {"value": "r = 0.052", "what": "rank-biserial effect size", "unit": "", "denominator": "", "scope": ""}]
caveat: "The pathway conservation measure is coarse and does not detect partial gene erosion, meaning individual gene deletions within an otherwise complete pathway."
first_added: "2026-11-24"
source_hash: "1412a5c1aa7711732d548b57744f3324a207e5eba6d0b4052c8882ac9cc593fe"
---
# Pathway conservation does not separate latent from active pathways

Latent capabilities showed slightly higher mean conservation than active dependencies (Mann-Whitney U, p = 0.94 for active > latent; rank-biserial r = 0.052), so H2a is not supported. [src: metabolic_capability_dependency]

## Key figures

- **p = 0.94**: Mann-Whitney U test for active > latent conservation [src: metabolic_capability_dependency]
- **r = 0.052**: rank-biserial effect size [src: metabolic_capability_dependency]

## Evidence

> Latent capabilities showed slightly *higher* mean conservation than active dependencies (Mann-Whitney U, p = 0.94 for active > latent; rank-biserial r = 0.052). H2a is not supported. [src: metabolic_capability_dependency]

From the report [[summaries/metabolic_capability_dependency__REPORT]].

## Caveat

The pathway conservation measure is coarse and does not detect partial gene erosion, meaning individual gene deletions within an otherwise complete pathway. [src: metabolic_capability_dependency]

> This is a coarse measure — it does not detect partial gene erosion (individual gene deletions within an otherwise complete pathway). [src: metabolic_capability_dependency]

## Other caveats in this report

- Varying the active threshold ±25% (1.5–2.5) and latent threshold ±25% (0.75–1.25) gave latent fractions of 4.7% to 21.1% (SD = 5.9 percentage points across 16 threshold combinations). [src: metabolic_capability_dependency]
- The report states that the large intermediate zone (32.3%) makes the latent fraction moderately sensitive to threshold tightening. [src: metabolic_capability_dependency]
- GapMind deoxyribonate and myoinositol pathways lacked matching SEED subsystem role descriptions and were absent from all analyses. [src: metabolic_capability_dependency]
- Full-name GapMind phenylalanine and tyrosine entries lacked SEED coverage, but their phe and tyr equivalents were included through abbreviation-based matching. [src: metabolic_capability_dependency]
- Alanine appeared in fitness metrics but was excluded from classification for all organisms because fewer than 3 SEED-annotated genes met the minimum coverage threshold. [src: metabolic_capability_dependency]
