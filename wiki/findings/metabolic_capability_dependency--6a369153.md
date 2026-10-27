---
type: "Finding"
description: "After aggregating 41 organisms to 22 unique species clades, the fraction of latent capabilities per clade correlated positively with pangenome openness (Spearman \u03c1 = 0.69, p = 0.0004, n = 22 clades), which the report calls consistent with the Black Queen framework at the species level."
finding_id: "metabolic_capability_dependency--6a369153"
result: "observation"
source: "metabolic_capability_dependency"
quantities: [{"value": "0.69", "what": "Spearman correlation between clade latent-capability fraction and pangenome openness", "unit": "Spearman \u03c1", "denominator": "", "scope": "22 species clades (aggregated from 41 organisms)"}, {"value": "0.0004", "what": "p-value of the correlation", "unit": "", "denominator": "", "scope": "n = 22 clades"}]
caveat: "The clade-level openness association diverges from the null pathway-level conservation comparison (H2a), so the report treats the evidence for the Black Queen framework as mixed rather than uniformly supportive."
first_added: "2026-10-27"
source_hash: "1412a5c1aa7711732d548b57744f3324a207e5eba6d0b4052c8882ac9cc593fe"
---
# Clades with more latent pathways have more open pangenomes

After aggregating 41 organisms to 22 unique species clades, the fraction of latent capabilities per clade correlated positively with pangenome openness (Spearman ρ = 0.69, p = 0.0004, n = 22 clades), which the report calls consistent with the Black Queen framework at the species level. [src: metabolic_capability_dependency]

## Key figures

- **0.69 Spearman ρ**: Spearman correlation between clade latent-capability fraction and pangenome openness (scope 22 species clades (aggregated from 41 organisms)) [src: metabolic_capability_dependency]
- **0.0004**: p-value of the correlation (scope n = 22 clades) [src: metabolic_capability_dependency]

## Evidence

> **H2b — Pangenome openness (supported).** After aggregating 41 organisms to 22 unique species clades (to ensure independence — multiple Fitness Browser strains from the same clade share a single pangenome openness value), the fraction of latent capabilities per clade correlated positively with pangenome openness (Spearman ρ = 0.69, p = 0.0004, n = 22 clades). Clades with more fitness-neutral complete pathways tend to have more dynamic, less-conserved pangenomes — consistent with the Black Queen framework at the species level. [src: metabolic_capability_dependency]

From the report [[summaries/metabolic_capability_dependency__REPORT]].

## Caveat

The clade-level openness association diverges from the null pathway-level conservation comparison (H2a), so the report treats the evidence for the Black Queen framework as mixed rather than uniformly supportive. [src: metabolic_capability_dependency]

> The positive correlation between per-clade latent capability rate and pangenome openness (ρ = 0.69, p = 0.0004, n = 22 clades, H2b) provides clade-level support for the Black Queen framework: bacterial clades that carry more fitness-neutral complete pathways also have more dynamic pangenomes, consistent with ongoing streamlining. However, at the pathway level, conservation rates did not distinguish latent from active pathways (H2a). This divergence suggests that the Black Queen signal operates at the level of genome dynamics and community context, rather than being detectable in per-pathway cross-genome conservation ratios. [src: metabolic_capability_dependency]

## Other caveats in this report

- Across 16 threshold combinations, the latent fraction ranged from 4.7% to 21.1% (SD = 5.9 percentage points), versus 15.8% at default thresholds; the estimated fraction is moderately threshold-sensitive. [src: metabolic_capability_dependency]
- Deoxyribonate and myoinositol were absent from all analyses for lack of SEED matches; phenylalanine and tyrosine entered via phe and tyr abbreviations; alanine was excluded from classification because fewer than 3 SEED-annotated genes met coverage. [src: metabolic_capability_dependency]
- The pathway-completeness conservation measure cannot detect partial gene erosion. [src: metabolic_capability_dependency]
- Fitness coverage of only 48 organisms may inflate apparent conservation when other members of their species clades were not fitness-tested. [src: metabolic_capability_dependency]
- SEED-based proxy mapping can introduce false-positive pathway genes, dilute fitness signals, and misclassify pathways. [src: metabolic_capability_dependency]
