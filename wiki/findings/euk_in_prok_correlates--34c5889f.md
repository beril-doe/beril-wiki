---
type: "Finding"
description: "For the euk_logit response, R\u00b2 was 0.24 for study_id only (random CV), 0.35 for environment (random CV), \u22120.30 for environment under out-of-study GroupKFold, and \u22120.39 for environment plus sequencing under GroupKFold."
finding_id: "euk_in_prok_correlates--34c5889f"
result: "observation"
source: "euk_in_prok_correlates"
quantities: [{"value": "0.35", "what": "R\u00b2 of environment model, random CV", "unit": "R\u00b2", "denominator": "", "scope": "euk_logit"}, {"value": "\u22120.30", "what": "R\u00b2 of environment model, out-of-study GroupKFold", "unit": "R\u00b2", "denominator": "", "scope": "euk_logit"}, {"value": "\u22120.39", "what": "R\u00b2 of environment plus sequencing, GroupKFold", "unit": "R\u00b2", "denominator": "", "scope": "euk_logit"}, {"value": "0.24", "what": "R\u00b2 of study_id-only model, random CV (batch ceiling)", "unit": "R\u00b2", "denominator": "", "scope": "euk_logit"}]
caveat: "Each biome is approximately 80\u2013100% nested within a single study, so the strong univariate environment signal cannot be separated from study/batch."
first_added: "2026-10-27"
source_hash: "345875dfe9abb66eeb33126277f33a3a655e7e7feed29ff12ebd79787207c86a"
---
# Environment model fails when whole studies are held out

For the euk_logit response, R² was 0.24 for study_id only (random CV), 0.35 for environment (random CV), −0.30 for environment under out-of-study GroupKFold, and −0.39 for environment plus sequencing under GroupKFold. [src: euk_in_prok_correlates]

## Key figures

- **0.35 R²**: R² of environment model, random CV (scope euk_logit) [src: euk_in_prok_correlates]
- **−0.30 R²**: R² of environment model, out-of-study GroupKFold (scope euk_logit) [src: euk_in_prok_correlates]
- **−0.39 R²**: R² of environment plus sequencing, GroupKFold (scope euk_logit) [src: euk_in_prok_correlates]
- **0.24 R²**: R² of study_id-only model, random CV (batch ceiling) (scope euk_logit) [src: euk_in_prok_correlates]

## Evidence

> | Model | R² (euk_logit) | |---|---| | `study_id` only (random CV — batch ceiling) | 0.24 | | environment (random CV) | 0.35 | | **environment (GroupKFold, out-of-study)** | **−0.30** | | environment + sequencing (GroupKFold) | −0.39 | [src: euk_in_prok_correlates]

From the report [[summaries/euk_in_prok_correlates__REPORT]].

## Caveat

Each biome is approximately 80–100% nested within a single study, so the strong univariate environment signal cannot be separated from study/batch. [src: euk_in_prok_correlates]

> This is the central methodological result. In NMDC, **each biome is ~80–100% nested within a single study**, so the strong univariate environment signal cannot be separated from study/batch. A gradient-boosted model of the eukaryotic fraction shows: [src: euk_in_prok_correlates]

## Other caveats in this report

- Kraken2 and Centrifuge yielded approximately zero domain-level Eukaryota signal because their NMDC reference databases were prokaryote-restricted; GOTTCHA2 was the only usable estimator here. [src: euk_in_prok_correlates]
- Ecosystem type reduced to the same three biomes as matrix and was not an independent confirmation; an earlier p≈10⁻⁵⁰ with the Unknown bucket was a missingness artifact. [src: euk_in_prok_correlates]
- In 292 runs with measured depth, cross-study Spearman ρ=−0.29, p=5.2×10⁻⁷; the shallower–higher-eukaryote association was not batch-controlled and is suggestive only. [src: euk_in_prok_correlates]
- The Kraken2 classification report had approximately 29 million rows; the report advises aggregation to one row per workflow_run_id before metadata joins. [src: euk_in_prok_correlates]
- 1,067 of 2,759 ReadbasedAnalysis runs were pooled from multiple biosamples, so biosample-level joins would inflate sample size through pseudoreplication. [src: euk_in_prok_correlates]
