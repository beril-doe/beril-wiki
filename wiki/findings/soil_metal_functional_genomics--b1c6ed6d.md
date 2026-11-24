---
type: "Finding"
description: "In soil, db-RDA gave R\u00b2 = 0.799, p = 0.005 (permutation test, 999 permutations), reported as metal concentrations explaining 80% of variance in community COG profiles after conditioning on batch/project effects."
finding_id: "soil_metal_functional_genomics--b1c6ed6d"
result: "observation"
source: "soil_metal_functional_genomics"
quantities: [{"value": "R\u00b2 = 0.799", "what": "db-RDA variance in community COG profiles explained by metals, conditional on project", "unit": "", "denominator": "", "scope": "soil communities"}, {"value": "p = 0.005", "what": "permutation test p-value", "unit": "", "denominator": "999 permutations", "scope": ""}]
caveat: "If batch effects (project) account for the majority of community COG variance, the reported R\u00b2 describes how well metals explain the residual variance, not the total variance."
first_added: "2026-11-24"
source_hash: "afe5423a06222e7ee2957401c00f4af52fea13df31be748b4ab108fb1dfe6144"
---
# Soil metals explain most community COG profile variance after conditioning on project

In soil, db-RDA gave R² = 0.799, p = 0.005 (permutation test, 999 permutations), reported as metal concentrations explaining 80% of variance in community COG profiles after conditioning on batch/project effects. [src: soil_metal_functional_genomics]

## Key figures

- **R² = 0.799**: db-RDA variance in community COG profiles explained by metals, conditional on project (scope soil communities) [src: soil_metal_functional_genomics]
- **p = 0.005**: permutation test p-value (denominator 999 permutations) [src: soil_metal_functional_genomics]

## Evidence

> **db-RDA**: R² = 0.799, p = 0.005 (permutation test, 999 permutations) — metal concentrations explain 80% of variance in community COG profiles after conditioning on batch/project effects. [src: soil_metal_functional_genomics]

From the report [[summaries/soil_metal_functional_genomics__REPORT]].

## Caveat

If batch effects (project) account for the majority of community COG variance, the reported R² describes how well metals explain the residual variance, not the total variance. [src: soil_metal_functional_genomics]

> **R² = 0.799 requires careful interpretation.** db-RDA conditions on project accession before fitting the metal concentration predictors. If batch effects (project) account for the majority of community COG variance, the reported R² describes how well metals explain the *residual* variance, not the *total* variance. [src: soil_metal_functional_genomics]

## Other caveats in this report

- The report is preliminary: Spearman correlation, db-RDA, and PGLS analyses are complete in NB01–NB04, while NB05 effect size and spatial validation and NB06 figures are pending. [src: soil_metal_functional_genomics]
- All reported metal-COG associations are observational. [src: soil_metal_functional_genomics]
- Co-contamination is a significant confound because Cr, Cu, Pb, and Zn co-vary in many industrial soils. [src: soil_metal_functional_genomics]
- Whether individual COG-metal associations are metal-specific or reflect a generic stress response to multi-metal contamination remains unresolved, with NB05 partial correlation models pending. [src: soil_metal_functional_genomics]
- Spearman ρ effect sizes have not been systematically reported across all 2,355 associations, and many associations may be statistically significant but biologically small. [src: soil_metal_functional_genomics]
