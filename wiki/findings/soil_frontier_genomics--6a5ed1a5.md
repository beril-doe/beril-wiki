---
type: "Finding"
description: "The soil shield efficiency test gives low-clay CV R\u00b2 = \u22120.268 and high-clay CV R\u00b2 = \u22120.292, with difference = 0.024 [95% CI: \u22120.423, 0.161], which is not significant because the CI includes zero."
finding_id: "soil_frontier_genomics--6a5ed1a5"
result: "null result"
source: "soil_frontier_genomics"
quantities: [{"value": "\u22120.268", "what": "low-clay CV R\u00b2", "unit": "", "denominator": "", "scope": ""}, {"value": "\u22120.292", "what": "high-clay CV R\u00b2", "unit": "", "denominator": "", "scope": ""}, {"value": "0.024", "what": "difference in CV R\u00b2", "unit": "", "denominator": "", "scope": "95% CI: \u22120.423, 0.161"}]
caveat: "Train/test distributional shift due to spatial autocorrelation within GroupKFold folds is one of three possible causes of the negative CV R\u00b2 that have not been distinguished."
first_added: "2026-11-24"
source_hash: "f3931fe9d68922f56c7c150229f466d5cddab2ea6b166362e8b31933149f9a8d"
---
# Shield efficiency test finds no clay difference in predictive accuracy

The soil shield efficiency test gives low-clay CV R² = −0.268 and high-clay CV R² = −0.292, with difference = 0.024 [95% CI: −0.423, 0.161], which is not significant because the CI includes zero. [src: soil_frontier_genomics]

## Key figures

- **−0.268**: low-clay CV R² [src: soil_frontier_genomics]
- **−0.292**: high-clay CV R² [src: soil_frontier_genomics]
- **0.024**: difference in CV R² (scope 95% CI: −0.423, 0.161) [src: soil_frontier_genomics]

## Evidence

> **Shield efficiency test**: low-clay CV R² = −0.268, high-clay CV R² = −0.292; difference = 0.024 [95% CI: −0.423, 0.161] — **not significant, CI includes zero**. [src: soil_frontier_genomics]

From the report [[summaries/soil_frontier_genomics__REPORT]].

## Caveat

Train/test distributional shift due to spatial autocorrelation within GroupKFold folds is one of three possible causes of the negative CV R² that have not been distinguished. [src: soil_frontier_genomics]

> Three possible causes have not been distinguished: (a) train/test distributional shift due to spatial autocorrelation within GroupKFold folds, (b) high-leverage outlier samples in test folds that dominate the MSE, or (c) genuine unpredictability of functional gene counts from the measured predictors at global scale. [src: soil_frontier_genomics]

## Other caveats in this report

- The soil_frontier_genomics report is preliminary, with clay shield and GDI analyses complete across all source notebooks but NB05 spatial validation and NB06 figures pending. [src: soil_frontier_genomics]
- The report suggests that the inability to predict soil functional potential from measured stressors at this scale is likely due to spatial autocorrelation, batch effects, and unmeasured confounders. [src: soil_frontier_genomics]
- The report states that diagnosis of the negative out-of-sample R² is incomplete and that all three predictive model families predict worse than the training mean. [src: soil_frontier_genomics]
- High-leverage outlier samples in test folds dominating the MSE remain an undistinguished possible cause of the negative soil-model CV R². [src: soil_frontier_genomics]
- Genuine unpredictability of soil functional gene counts from the measured predictors at global scale remains an undistinguished possible cause of negative CV R². [src: soil_frontier_genomics]
