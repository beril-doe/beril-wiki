---
type: "Finding"
description: "Local environment and geography predict NEON soil eukaryotic fraction with within-study 5-fold R\u00b2 = +0.17 \u00b1 0.06, in contrast to the cross-study out-of-study R\u00b2 = \u22120.30."
finding_id: "euk_in_prok_correlates--d08fdf8f"
result: "observation"
source: "euk_in_prok_correlates"
quantities: [{"value": "+0.17 \u00b1 0.06", "what": "within-study 5-fold R\u00b2", "unit": "R\u00b2", "denominator": "", "scope": "NEON soil study"}, {"value": "\u22120.30", "what": "cross-study out-of-study R\u00b2", "unit": "R\u00b2", "denominator": "", "scope": "NMDC"}]
caveat: "Even within one study, env_local_scale and geography may track sub-batches (sampling campaigns); the within-study effect is the best available control, not a randomized one."
first_added: "2026-11-24"
source_hash: "345875dfe9abb66eeb33126277f33a3a655e7e7feed29ff12ebd79787207c86a"
---
# Environment predicts eukaryotic fraction within one soil study but not across studies

Local environment and geography predict NEON soil eukaryotic fraction with within-study 5-fold R² = +0.17 ± 0.06, in contrast to the cross-study out-of-study R² = −0.30. [src: euk_in_prok_correlates]

## Key figures

- **+0.17 ± 0.06 R²**: within-study 5-fold R² (scope NEON soil study) [src: euk_in_prok_correlates]
- **−0.30 R²**: cross-study out-of-study R² (scope NMDC) [src: euk_in_prok_correlates]

## Evidence

> - **Within-study predictability**: 5-fold R² = **+0.17 ± 0.06** (local environment + geography → euk fraction), in direct contrast to the cross-study out-of-study R² = −0.30. [src: euk_in_prok_correlates]

From the report [[summaries/euk_in_prok_correlates__REPORT]].

## Caveat

Even within one study, env_local_scale and geography may track sub-batches (sampling campaigns); the within-study effect is the best available control, not a randomized one. [src: euk_in_prok_correlates]

> - **Confounding within study.** Even within one study, `env_local_scale` and geography may track sub-batches (sampling campaigns); the within-study effect is the best available control, not a randomized one. [src: euk_in_prok_correlates]

## Other caveats in this report

- Kraken2 and Centrifuge have domain-level Eukaryota signals of ≈0 because their NMDC reference databases are prokaryote-restricted, leaving GOTTCHA2 as the only usable eukaryotic estimator here. [src: euk_in_prok_correlates]
- After excluding Unknown or missing metadata, NMDC ecosystem_type reduces to Soil, Freshwater and Roots, making its test identical to the matrix test rather than independent confirmation. [src: euk_in_prok_correlates]
- An earlier NMDC analysis including the Unknown bucket, which has the highest median eukaryotic fraction, reported inflated p≈10⁻⁵⁰ that the report removed as a missingness artifact. [src: euk_in_prok_correlates]
- In NMDC each biome is ~80–100% nested within a single study, preventing separation of the strong univariate environment signal from study/batch. [src: euk_in_prok_correlates]
- The report warns that naive cross-collection regression of NMDC eukaryotic fraction on environmental metadata would report a strong but largely spurious batch-driven association. [src: euk_in_prok_correlates]
