---
type: "Finding"
description: "The soil analysis found 2,355 significant COG-metal associations (FDR < 0.05) across 9 metals (Cu, Co, Cr, Ni, Zn, Pb, As, Cd, Hg) in 51,748 soil samples."
finding_id: "soil_metal_functional_genomics--0fa4f389"
result: "observation"
source: "soil_metal_functional_genomics"
quantities: [{"value": "2,355", "what": "significant COG-metal associations", "unit": "associations", "denominator": "", "scope": "FDR < 0.05"}, {"value": "51,748", "what": "soil samples", "unit": "samples", "denominator": "", "scope": ""}]
caveat: "Metals co-contaminate, so tests are not independent; Benjamini-Hochberg FDR correction will be anti-conservative under positive correlation and the true FDR is likely higher than reported."
first_added: "2026-11-24"
source_hash: "afe5423a06222e7ee2957401c00f4af52fea13df31be748b4ab108fb1dfe6144"
---
# Many soil COG-metal associations are significant across nine metals

The soil analysis found 2,355 significant COG-metal associations (FDR < 0.05) across 9 metals (Cu, Co, Cr, Ni, Zn, Pb, As, Cd, Hg) in 51,748 soil samples. [src: soil_metal_functional_genomics]

## Key figures

- **2,355 associations**: significant COG-metal associations (scope FDR < 0.05) [src: soil_metal_functional_genomics]
- **51,748 samples**: soil samples [src: soil_metal_functional_genomics]

## Evidence

> **2,355 significant COG-metal associations** (FDR < 0.05) across 9 metals (Cu, Co, Cr, Ni, Zn, Pb, As, Cd, Hg) in 51,748 soil samples. [src: soil_metal_functional_genomics]

From the report [[summaries/soil_metal_functional_genomics__REPORT]].

## Caveat

Metals co-contaminate, so tests are not independent; Benjamini-Hochberg FDR correction will be anti-conservative under positive correlation and the true FDR is likely higher than reported. [src: soil_metal_functional_genomics]

> Metals co-contaminate (Cr, Pb, Zn, Cu co-vary in industrial soils), so tests are not independent — Benjamini-Hochberg FDR correction assumes independent tests and will be anti-conservative under positive correlation. True FDR is likely higher than reported. [src: soil_metal_functional_genomics]

## Other caveats in this report

- The report is preliminary: Spearman correlation, db-RDA, and PGLS analyses are complete in NB01–NB04, while NB05 effect size and spatial validation and NB06 figures are pending. [src: soil_metal_functional_genomics]
- All reported metal-COG associations are observational. [src: soil_metal_functional_genomics]
- Co-contamination is a significant confound because Cr, Cu, Pb, and Zn co-vary in many industrial soils. [src: soil_metal_functional_genomics]
- Whether individual COG-metal associations are metal-specific or reflect a generic stress response to multi-metal contamination remains unresolved, with NB05 partial correlation models pending. [src: soil_metal_functional_genomics]
- Spearman ρ effect sizes have not been systematically reported across all 2,355 associations, and many associations may be statistically significant but biologically small. [src: soil_metal_functional_genomics]
