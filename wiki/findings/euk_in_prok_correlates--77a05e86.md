---
type: "Finding"
description: "Plant root samples had 100% eukaryote detection with a plastid share of 0.03, dominated by root-associated non-plastid fungi/protists."
finding_id: "euk_in_prok_correlates--77a05e86"
result: "observation"
source: "euk_in_prok_correlates"
quantities: [{"value": "0.03", "what": "plastid share of eukaryotic signal in root samples", "unit": "", "denominator": "", "scope": "Plants (roots)"}, {"value": "100%", "what": "eukaryote detection in root samples", "unit": "", "denominator": "", "scope": "Plants (roots)"}]
caveat: "Each biome is approximately 80\u2013100% nested within a single study, so the biome contrast cannot be separated from study/batch."
first_added: "2026-10-27"
source_hash: "345875dfe9abb66eeb33126277f33a3a655e7e7feed29ff12ebd79787207c86a"
---
# Root samples carry non-plastid fungal and protist eukaryotic DNA

Plant root samples had 100% eukaryote detection with a plastid share of 0.03, dominated by root-associated non-plastid fungi/protists. [src: euk_in_prok_correlates]

## Key figures

- **0.03**: plastid share of eukaryotic signal in root samples (scope Plants (roots)) [src: euk_in_prok_correlates]
- **100%**: eukaryote detection in root samples (scope Plants (roots)) [src: euk_in_prok_correlates]

## Evidence

> | Plants (roots) | 100% | **0.03** | root-associated **fungi/protists** (non-plastid) | [src: euk_in_prok_correlates]

From the report [[summaries/euk_in_prok_correlates__REPORT]].

## Caveat

Each biome is approximately 80–100% nested within a single study, so the biome contrast cannot be separated from study/batch. [src: euk_in_prok_correlates]

> This is the central methodological result. In NMDC, **each biome is ~80–100% nested within a single study**, so the strong univariate environment signal cannot be separated from study/batch. A gradient-boosted model of the eukaryotic fraction shows: [src: euk_in_prok_correlates]

## Other caveats in this report

- Kraken2 and Centrifuge yielded approximately zero domain-level Eukaryota signal because their NMDC reference databases were prokaryote-restricted; GOTTCHA2 was the only usable estimator here. [src: euk_in_prok_correlates]
- Ecosystem type reduced to the same three biomes as matrix and was not an independent confirmation; an earlier p≈10⁻⁵⁰ with the Unknown bucket was a missingness artifact. [src: euk_in_prok_correlates]
- In 292 runs with measured depth, cross-study Spearman ρ=−0.29, p=5.2×10⁻⁷; the shallower–higher-eukaryote association was not batch-controlled and is suggestive only. [src: euk_in_prok_correlates]
- The Kraken2 classification report had approximately 29 million rows; the report advises aggregation to one row per workflow_run_id before metadata joins. [src: euk_in_prok_correlates]
- 1,067 of 2,759 ReadbasedAnalysis runs were pooled from multiple biosamples, so biosample-level joins would inflate sample size through pseudoreplication. [src: euk_in_prok_correlates]
