---
type: "Finding"
description: "The db-RDA reported R\u00b2 = 0.799 and p = 0.005 (permutation test, 999 permutations), with metal concentrations explaining 80% of variance in community COG profiles after conditioning on batch/project effects."
finding_id: "soil_metal_functional_genomics--fd9b94cc"
result: "observation"
source: "soil_metal_functional_genomics"
quantities: [{"value": "0.799", "what": "db-RDA R\u00b2 of metal concentrations on community COG profiles", "unit": "", "denominator": "", "scope": "after conditioning on batch/project effects"}, {"value": "0.005", "what": "permutation p-value", "unit": "", "denominator": "999 permutations", "scope": ""}]
caveat: "Because db-RDA conditions on project accession, R\u00b2 = 0.799 describes the residual rather than necessarily total variance, and the unconditional metals-only R\u00b2 is not reported and may be substantially lower."
first_added: "2026-10-27"
source_hash: "afe5423a06222e7ee2957401c00f4af52fea13df31be748b4ab108fb1dfe6144"
---
# Metals explain most residual community COG variance after removing project effects

The db-RDA reported R² = 0.799 and p = 0.005 (permutation test, 999 permutations), with metal concentrations explaining 80% of variance in community COG profiles after conditioning on batch/project effects. [src: soil_metal_functional_genomics]

## Key figures

- **0.799**: db-RDA R² of metal concentrations on community COG profiles (scope after conditioning on batch/project effects) [src: soil_metal_functional_genomics]
- **0.005**: permutation p-value (denominator 999 permutations) [src: soil_metal_functional_genomics]

## Evidence

> - **db-RDA**: R² = 0.799, p = 0.005 (permutation test, 999 permutations) — metal concentrations explain 80% of variance in community COG profiles after conditioning on batch/project effects. [src: soil_metal_functional_genomics]

From the report [[summaries/soil_metal_functional_genomics__REPORT]].

## Caveat

Because db-RDA conditions on project accession, R² = 0.799 describes the residual rather than necessarily total variance, and the unconditional metals-only R² is not reported and may be substantially lower. [src: soil_metal_functional_genomics]

> **R² = 0.799 requires careful interpretation.** db-RDA conditions on project accession before fitting the metal concentration predictors. If batch effects (project) account for the majority of community COG variance, the reported R² describes how well metals explain the *residual* variance, not the *total* variance. The unconditional R² of metals alone — without first removing project effects — is not reported and may be substantially lower. This must be reported alongside the conditional figure. [src: soil_metal_functional_genomics]

## Other caveats in this report

- The report is preliminary: Spearman correlation, db-RDA and PGLS analyses were complete, while effect-size and spatial validation remained pending. [src: soil_metal_functional_genomics]
- All reported associations are observational. Covariation of Cr, Cu, Pb and Zn in industrial soils confounds metal-specific interpretation; whether the COG associations represent metal-specific or general multi-metal stress responses remains unresolved. [src: soil_metal_functional_genomics]
- The report flags a high 60% discovery rate from 2,355 significant associations among 3,915 tests (9 metals × 435 COGs) in 51,748 samples. It argues that metal co-contamination and dependent tests may make its reported Benjamini–Hochberg FDR anti-conservative, and calls for a partial-correlation model. This is the report's methodological assessment, not a validated recalculation of FDR. [src: soil_metal_functional_genomics]
- A 10 km sample-to-genome matching threshold may not establish site co-location; the report requires sensitivity analyses at 5 km and 20 km before attributing COG–copper associations to measured sites. [src: soil_metal_functional_genomics]
- A pending effect-size audit would examine the ρ distribution across 2,355 associations and flag ρ < 0.05. [src: soil_metal_functional_genomics]
