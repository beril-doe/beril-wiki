---
type: "Finding"
description: "Across 1,695 pathway-organism pairs from 48 organisms, 15.8% of genomically complete pathways were classified as latent capabilities (no detectable fitness importance under tested conditions; mean |t-score| < 1.0, < 5% essential genes), and an additional 32.3% fell in an intermediate zone."
finding_id: "metabolic_capability_dependency--f41ac91a"
result: "observation"
source: "metabolic_capability_dependency"
quantities: [{"value": "15.8%", "what": "genomically complete pathways classified as latent capabilities", "unit": "percent", "denominator": "1,695 pathway-organism pairs", "scope": "48 organisms"}, {"value": "32.3%", "what": "pathways in the intermediate zone", "unit": "percent", "denominator": "1,695 pathway-organism pairs", "scope": "48 organisms"}]
caveat: "Across 16 threshold combinations the latent fraction ranged from 4.7% to 21.1% (SD = 5.9 percentage points) versus 15.8% at default thresholds, so the estimate is moderately threshold-sensitive."
first_added: "2026-10-27"
source_hash: "1412a5c1aa7711732d548b57744f3324a207e5eba6d0b4052c8882ac9cc593fe"
---
# Many genomically complete pathways show no detectable fitness importance

Across 1,695 pathway-organism pairs from 48 organisms, 15.8% of genomically complete pathways were classified as latent capabilities (no detectable fitness importance under tested conditions; mean |t-score| < 1.0, < 5% essential genes), and an additional 32.3% fell in an intermediate zone. [src: metabolic_capability_dependency]

## Key figures

- **15.8%**: genomically complete pathways classified as latent capabilities (denominator 1,695 pathway-organism pairs; scope 48 organisms) [src: metabolic_capability_dependency]
- **32.3%**: pathways in the intermediate zone (denominator 1,695 pathway-organism pairs; scope 48 organisms) [src: metabolic_capability_dependency]

## Evidence

> Across 1,695 pathway-organism pairs from 48 organisms, **15.8% of genomically complete pathways were classified as latent capabilities** — pathways the genome encodes but that show no detectable fitness importance under tested conditions (mean |t-score| < 1.0, < 5% essential genes). An additional 32.3% fell in an intermediate zone. [src: metabolic_capability_dependency]

From the report [[summaries/metabolic_capability_dependency__REPORT]].

## Caveat

Across 16 threshold combinations the latent fraction ranged from 4.7% to 21.1% (SD = 5.9 percentage points) versus 15.8% at default thresholds, so the estimate is moderately threshold-sensitive. [src: metabolic_capability_dependency]

> **Threshold sensitivity**: Varying the active threshold ±25% (1.5–2.5) and latent threshold ±25% (0.75–1.25), the latent fraction ranged from 4.7% to 21.1% (SD = 5.9 percentage points across 16 threshold combinations). At the default thresholds the result is 15.8%. The large intermediate zone (32.3%) means the latent fraction is moderately sensitive to threshold tightening. The qualitative conclusion — that a non-trivial fraction of complete pathways are fitness-neutral, with carbon pathways most affected — holds across the full range tested. [src: metabolic_capability_dependency]

## Other caveats in this report

- Deoxyribonate and myoinositol were absent from all analyses for lack of SEED matches; phenylalanine and tyrosine entered via phe and tyr abbreviations; alanine was excluded from classification because fewer than 3 SEED-annotated genes met coverage. [src: metabolic_capability_dependency]
- The report interprets the positive clade-level openness association alongside the null pathway-level conservation comparison as mixed evidence for the Black Queen framework, not uniform support. [src: metabolic_capability_dependency]
- The pathway-completeness conservation measure cannot detect partial gene erosion. [src: metabolic_capability_dependency]
- Fitness coverage of only 48 organisms may inflate apparent conservation when other members of their species clades were not fitness-tested. [src: metabolic_capability_dependency]
- SEED-based proxy mapping can introduce false-positive pathway genes, dilute fitness signals, and misclassify pathways. [src: metabolic_capability_dependency]
