---
type: "Finding"
description: "After aggregating 41 organisms to 22 unique species clades, the fraction of latent capabilities per clade correlated positively with pangenome openness (Spearman \u03c1 = 0.69, p = 0.0004, n = 22 clades)."
finding_id: "metabolic_capability_dependency--3bcc11af"
result: "observation"
source: "metabolic_capability_dependency"
quantities: [{"value": "\u03c1 = 0.69", "what": "Spearman correlation of latent fraction with pangenome openness", "unit": "", "denominator": "", "scope": ""}, {"value": "n = 22 clades", "what": "number of species clades", "unit": "", "denominator": "", "scope": ""}]
caveat: "The fitness experiments cover only 48 organisms, and many organisms in the same species clade may not have been fitness-tested, inflating apparent conservation of pathways that are complete but untested."
first_added: "2026-11-24"
source_hash: "1412a5c1aa7711732d548b57744f3324a207e5eba6d0b4052c8882ac9cc593fe"
---
# Latent pathway fraction rises with pangenome openness across species clades

After aggregating 41 organisms to 22 unique species clades, the fraction of latent capabilities per clade correlated positively with pangenome openness (Spearman ρ = 0.69, p = 0.0004, n = 22 clades). [src: metabolic_capability_dependency]

## Key figures

- **ρ = 0.69**: Spearman correlation of latent fraction with pangenome openness [src: metabolic_capability_dependency]
- **n = 22 clades**: number of species clades [src: metabolic_capability_dependency]

## Evidence

> After aggregating 41 organisms to 22 unique species clades (to ensure independence — multiple Fitness Browser strains from the same clade share a single pangenome openness value), the fraction of latent capabilities per clade correlated positively with pangenome openness (Spearman ρ = 0.69, p = 0.0004, n = 22 clades). [src: metabolic_capability_dependency]

From the report [[summaries/metabolic_capability_dependency__REPORT]].

## Caveat

The fitness experiments cover only 48 organisms, and many organisms in the same species clade may not have been fitness-tested, inflating apparent conservation of pathways that are complete but untested. [src: metabolic_capability_dependency]

> **Species-level averaging**: The fitness experiments cover only 48 organisms; many organisms in the same species clade may not have been fitness-tested, inflating apparent conservation of pathways that are "complete" but untested. [src: metabolic_capability_dependency]

## Other caveats in this report

- Varying the active threshold ±25% (1.5–2.5) and latent threshold ±25% (0.75–1.25) gave latent fractions of 4.7% to 21.1% (SD = 5.9 percentage points across 16 threshold combinations). [src: metabolic_capability_dependency]
- The report states that the large intermediate zone (32.3%) makes the latent fraction moderately sensitive to threshold tightening. [src: metabolic_capability_dependency]
- GapMind deoxyribonate and myoinositol pathways lacked matching SEED subsystem role descriptions and were absent from all analyses. [src: metabolic_capability_dependency]
- Full-name GapMind phenylalanine and tyrosine entries lacked SEED coverage, but their phe and tyr equivalents were included through abbreviation-based matching. [src: metabolic_capability_dependency]
- Alanine appeared in fitness metrics but was excluded from classification for all organisms because fewer than 3 SEED-annotated genes met the minimum coverage threshold. [src: metabolic_capability_dependency]
