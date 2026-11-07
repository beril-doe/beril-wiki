---
type: "Finding"
description: "Within-study predictability of eukaryotic fraction from local environment plus geography had 5-fold R\u00b2 = +0.17 \u00b1 0.06, in direct contrast to the cross-study out-of-study R\u00b2 = \u22120.30."
finding_id: "euk_in_prok_correlates--d08fdf8f"
result: "observation"
source: "euk_in_prok_correlates"
quantities: [{"value": "+0.17 \u00b1 0.06", "what": "within-study 5-fold R\u00b2 (local environment + geography to eukaryotic fraction)", "unit": "R\u00b2", "denominator": "", "scope": "within-study"}, {"value": "\u22120.30", "what": "cross-study out-of-study R\u00b2", "unit": "R\u00b2", "denominator": "", "scope": "cross-study"}]
caveat: "The within-study result is demonstrated for one soil study only (one soil study is \u224843% of runs) and may not extend to aquatic or host-associated collections."
first_added: "2026-10-27"
source_hash: "345875dfe9abb66eeb33126277f33a3a655e7e7feed29ff12ebd79787207c86a"
---
# Within one study, local environment and geography do predict eukaryotic fraction

Within-study predictability of eukaryotic fraction from local environment plus geography had 5-fold R² = +0.17 ± 0.06, in direct contrast to the cross-study out-of-study R² = −0.30. [src: euk_in_prok_correlates]

## Key figures

- **+0.17 ± 0.06 R²**: within-study 5-fold R² (local environment + geography to eukaryotic fraction) (scope within-study) [src: euk_in_prok_correlates]
- **−0.30 R²**: cross-study out-of-study R² (scope cross-study) [src: euk_in_prok_correlates]

## Evidence

> - **Within-study predictability**: 5-fold R² = **+0.17 ± 0.06** (local environment + geography → euk fraction), in direct contrast to the cross-study out-of-study R² = −0.30. [src: euk_in_prok_correlates]

From the report [[summaries/euk_in_prok_correlates__REPORT]].

## Caveat

The within-study result is demonstrated for one soil study only (one soil study is ≈43% of runs) and may not extend to aquatic or host-associated collections. [src: euk_in_prok_correlates]

> - **Few independent studies.** NMDC's read-based taxonomy spans only ~9 studies (one soil study ≈43% of runs); `data/01_data_landscape.md` documents that no on-system source provides per-sample eukaryotic read fraction across many studies (MGnify here is a MAG catalog; SPIRE/GEM/Tara are MAG collections; EMP is 16S). The cross-study generalization test is therefore under-powered, and the within-study result is demonstrated for **one soil study only** — it may not extend to aquatic or host-associated collections. [src: euk_in_prok_correlates]

## Other caveats in this report

- Kraken2 and Centrifuge yielded approximately zero domain-level Eukaryota signal because their NMDC reference databases were prokaryote-restricted; GOTTCHA2 was the only usable estimator here. [src: euk_in_prok_correlates]
- Ecosystem type reduced to the same three biomes as matrix and was not an independent confirmation; an earlier p≈10⁻⁵⁰ with the Unknown bucket was a missingness artifact. [src: euk_in_prok_correlates]
- Each biome was approximately 80–100% nested within a single study, so the univariate environment signal was confounded with study/batch. [src: euk_in_prok_correlates]
- In 292 runs with measured depth, cross-study Spearman ρ=−0.29, p=5.2×10⁻⁷; the shallower–higher-eukaryote association was not batch-controlled and is suggestive only. [src: euk_in_prok_correlates]
- The Kraken2 classification report had approximately 29 million rows; the report advises aggregation to one row per workflow_run_id before metadata joins. [src: euk_in_prok_correlates]
