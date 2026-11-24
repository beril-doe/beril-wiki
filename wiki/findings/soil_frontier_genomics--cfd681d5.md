---
type: "Finding"
description: "Forest soils have a GDI of 902.36 and are among the highest-GDI genomic-frontier biomes."
finding_id: "soil_frontier_genomics--cfd681d5"
result: "observation"
source: "soil_frontier_genomics"
quantities: [{"value": "902.36", "what": "Forest GDI", "unit": "", "denominator": "", "scope": ""}, {"value": "890.82", "what": "Cropland GDI, the other highest-GDI biome", "unit": "", "denominator": "", "scope": ""}]
caveat: "Forest (902.36) vs. Cropland (890.82) is a 1.3% difference; without bootstrap CIs these are not meaningfully distinguishable."
first_added: "2026-11-24"
source_hash: "f3931fe9d68922f56c7c150229f466d5cddab2ea6b166362e8b31933149f9a8d"
---
# Forest soils sit at the genomic frontier

Forest soils have a GDI of 902.36 and are among the highest-GDI genomic-frontier biomes. [src: soil_frontier_genomics]

## Key figures

- **902.36**: Forest GDI [src: soil_frontier_genomics]
- **890.82**: Cropland GDI, the other highest-GDI biome [src: soil_frontier_genomics]

## Evidence

> Highest GDI (genomic frontier): Forest (902.36), Cropland (890.82). [src: soil_frontier_genomics]

From the report [[summaries/soil_frontier_genomics__REPORT]].

## Caveat

Forest (902.36) vs. Cropland (890.82) is a 1.3% difference; without bootstrap CIs these are not meaningfully distinguishable. [src: soil_frontier_genomics]

> **Forest vs. Cropland GDI difference is small.** Forest (902.36) vs. Cropland (890.82) is a 1.3% difference; without bootstrap CIs these are not meaningfully distinguishable. [src: soil_frontier_genomics]

## Other caveats in this report

- The soil_frontier_genomics report is preliminary, with clay shield and GDI analyses complete across all source notebooks but NB05 spatial validation and NB06 figures pending. [src: soil_frontier_genomics]
- The report suggests that the inability to predict soil functional potential from measured stressors at this scale is likely due to spatial autocorrelation, batch effects, and unmeasured confounders. [src: soil_frontier_genomics]
- The report states that diagnosis of the negative out-of-sample R² is incomplete and that all three predictive model families predict worse than the training mean. [src: soil_frontier_genomics]
- Train/test distributional shift due to spatial autocorrelation within GroupKFold folds remains an undistinguished possible cause of the negative soil-model CV R². [src: soil_frontier_genomics]
- High-leverage outlier samples in test folds dominating the MSE remain an undistinguished possible cause of the negative soil-model CV R². [src: soil_frontier_genomics]
