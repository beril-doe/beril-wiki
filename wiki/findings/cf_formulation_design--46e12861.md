---
type: "Finding"
description: "Adding genus-level taxonomy increases the PA14 inhibition model to R\u00b2 = 0.360, an additional 8.6% of variance, which the report interprets as intrinsic species-level mechanisms (likely direct antagonism) contributing independently of metabolism."
finding_id: "cf_formulation_design--46e12861"
result: "inference"
source: "cf_formulation_design"
quantities: [{"value": "R\u00b2 = 0.360", "what": "variance explained with genus added", "unit": "", "denominator": "", "scope": "PA14 inhibition model"}, {"value": "8.6%", "what": "additional variance explained by genus", "unit": "", "denominator": "", "scope": ""}]
caveat: "Five-fold cross-validation yields CV R\u00b2 = 0.145 \u00b1 0.142, below the training R\u00b2 of 0.274, indicating the multivariate model overfits to the 142-isolate cohort."
first_added: "2026-11-24"
source_hash: "06931c95e1ee4b3b3a4a95563e11b057ffbada9817b91426fd15b4be9ef75bfe"
---
# Taxonomy adds explanatory power beyond metabolism, suggesting direct antagonism

Adding genus-level taxonomy increases the PA14 inhibition model to R² = 0.360, an additional 8.6% of variance, which the report interprets as intrinsic species-level mechanisms (likely direct antagonism) contributing independently of metabolism. [src: cf_formulation_design]

## Key figures

- **R² = 0.360**: variance explained with genus added (scope PA14 inhibition model) [src: cf_formulation_design]
- **8.6%**: additional variance explained by genus [src: cf_formulation_design]

## Evidence

> Adding genus-level taxonomy increases this to **R² = 0.360** — genus explains an additional 8.6% of variance, indicating intrinsic species-level mechanisms (likely direct antagonism) contribute independently of metabolism. [src: cf_formulation_design]

From the report [[summaries/cf_formulation_design__REPORT]].

## Caveat

Five-fold cross-validation yields CV R² = 0.145 ± 0.142, below the training R² of 0.274, indicating the multivariate model overfits to the 142-isolate cohort. [src: cf_formulation_design]

> Five-fold cross-validation yields **CV R² = 0.145 ± 0.142**, below the training R² of 0.274, indicating the multivariate model overfits to the 142-isolate cohort. [src: cf_formulation_design]

## Other caveats in this report

- In the integrated PROTECT analysis of Pseudomonas aeruginosa PA14 inhibition, metabolic overlap explains only 27% of variance. [src: cf_formulation_design]
- The report states that repeated antibiotic courses used to treat cystic fibrosis airway infection select for resistance and disrupt the commensal microbiome. [src: cf_formulation_design]
- The report uses GTDB species taxonomy, which may differ from NCBI names. [src: cf_formulation_design]
- The PROTECT isolate collection reflects the typical cystic fibrosis airway microbiome plus deliberate oversampling of pathogens. [src: cf_formulation_design]
- Pseudomonas aeruginosa PA14's amino acid specialization is not universal among cystic fibrosis pathogens, suggesting protective formulations may need to be pathogen-specific. [src: cf_formulation_design]
