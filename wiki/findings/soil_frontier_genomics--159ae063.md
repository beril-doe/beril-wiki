---
type: "Finding"
description: "The clay shield hypothesis is not supported at global scale."
finding_id: "soil_frontier_genomics--159ae063"
result: "null result"
source: "soil_frontier_genomics"
quantities: []
caveat: "Only genuine unpredictability supports a strong biological null interpretation, whereas distributional shift or outlier leverage would indicate modelling failure."
first_added: "2026-11-24"
source_hash: "f3931fe9d68922f56c7c150229f466d5cddab2ea6b166362e8b31933149f9a8d"
---
# Clay shield hypothesis not supported at global scale

The clay shield hypothesis is not supported at global scale. [src: soil_frontier_genomics]

## Evidence

> The clay shield hypothesis is **not supported** at global scale. [src: soil_frontier_genomics]

From the report [[summaries/soil_frontier_genomics__REPORT]].

## Caveat

Only genuine unpredictability supports a strong biological null interpretation, whereas distributional shift or outlier leverage would indicate modelling failure. [src: soil_frontier_genomics]

> These three causes have different scientific implications — only (c) supports a strong null result interpretation. Causes (a) and (b) would indicate a modelling failure, not a biological null result. [src: soil_frontier_genomics]

## Other caveats in this report

- The soil_frontier_genomics report is preliminary, with clay shield and GDI analyses complete across all source notebooks but NB05 spatial validation and NB06 figures pending. [src: soil_frontier_genomics]
- The report suggests that the inability to predict soil functional potential from measured stressors at this scale is likely due to spatial autocorrelation, batch effects, and unmeasured confounders. [src: soil_frontier_genomics]
- The report states that diagnosis of the negative out-of-sample R² is incomplete and that all three predictive model families predict worse than the training mean. [src: soil_frontier_genomics]
- Train/test distributional shift due to spatial autocorrelation within GroupKFold folds remains an undistinguished possible cause of the negative soil-model CV R². [src: soil_frontier_genomics]
- High-leverage outlier samples in test folds dominating the MSE remain an undistinguished possible cause of the negative soil-model CV R². [src: soil_frontier_genomics]
