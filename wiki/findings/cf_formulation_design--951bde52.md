---
type: "Finding"
description: "Across the 142-isolate analysis cohort, metabolic overlap with PA14 (weighted by PA14's substrate preferences) significantly predicts planktonic inhibition, with r = 0.384, p = 2.3\u00d710\u207b\u2076."
finding_id: "cf_formulation_design--951bde52"
result: "observation"
source: "cf_formulation_design"
quantities: [{"value": "r = 0.384", "what": "correlation between weighted metabolic overlap with PA14 and planktonic inhibition", "unit": "", "denominator": "142 isolates", "scope": "analysis cohort with both inhibition and carbon utilization data"}, {"value": "p = 2.3\u00d710\u207b\u2076", "what": "significance of the overlap\u2013inhibition correlation", "unit": "", "denominator": "", "scope": "142-isolate cohort"}]
caveat: "Five-fold cross-validation yields CV R\u00b2 = 0.145 \u00b1 0.142, below the training R\u00b2 of 0.274, indicating the multivariate model overfits to the 142-isolate cohort."
first_added: "2026-10-27"
source_hash: "06931c95e1ee4b3b3a4a95563e11b057ffbada9817b91426fd15b4be9ef75bfe"
---
# Metabolic overlap with PA14 predicts inhibition, but only modestly

Across the 142-isolate analysis cohort, metabolic overlap with PA14 (weighted by PA14's substrate preferences) significantly predicts planktonic inhibition, with r = 0.384, p = 2.3×10⁻⁶. [src: cf_formulation_design]

## Key figures

- **r = 0.384**: correlation between weighted metabolic overlap with PA14 and planktonic inhibition (denominator 142 isolates; scope analysis cohort with both inhibition and carbon utilization data) [src: cf_formulation_design]
- **p = 2.3×10⁻⁶**: significance of the overlap–inhibition correlation (scope 142-isolate cohort) [src: cf_formulation_design]

## Evidence

> Across the 142-isolate analysis cohort, metabolic overlap with PA14 (weighted by PA14's substrate preferences) significantly predicts planktonic inhibition: **r = 0.384, p = 2.3×10⁻⁶**. [src: cf_formulation_design]

From the report [[summaries/cf_formulation_design__REPORT]].

## Caveat

Five-fold cross-validation yields CV R² = 0.145 ± 0.142, below the training R² of 0.274, indicating the multivariate model overfits to the 142-isolate cohort. [src: cf_formulation_design]

> Five-fold cross-validation yields **CV R² = 0.145 ± 0.142**, below the training R² of 0.274, indicating the multivariate model overfits to the 142-isolate cohort. [src: cf_formulation_design]

## Other caveats in this report

- Competitive metabolic exclusion is the study's working theory; the listed CF-sputum amino acids are proposed shared resources. [src: cf_formulation_design]
- Selective prebiotic biomass pre-loading is explicitly a hypothesis. [src: cf_formulation_design]
- GTDB taxonomy is used; Pseudomonas_E is a non-aeruginosa clade and should not be merged with P. aeruginosa. [src: cf_formulation_design]
- The three named organisms have the largest reported isolate counts; pathogen oversampling limits interpretation of collection frequencies as natural prevalence. [src: cf_formulation_design]
- Acinetobacter baumannii and Klebsiella pneumoniae are other named reporter pathogens; their distinct profiles limit generalization of the PA14-targeted formulation. [src: cf_formulation_design]
