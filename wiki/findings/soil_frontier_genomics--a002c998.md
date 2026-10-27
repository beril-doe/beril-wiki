---
type: "Finding"
description: "In the shield efficiency test, low-clay CV R\u00b2 was \u22120.268 and high-clay CV R\u00b2 was \u22120.292, a difference of 0.024 [95% CI: \u22120.423, 0.161] that is not significant because the CI includes zero."
finding_id: "soil_frontier_genomics--a002c998"
result: "null result"
source: "soil_frontier_genomics"
quantities: [{"value": "\u22120.268", "what": "Low-clay cross-validated R\u00b2", "unit": "R\u00b2", "denominator": "", "scope": "low-clay soils"}, {"value": "\u22120.292", "what": "High-clay cross-validated R\u00b2", "unit": "R\u00b2", "denominator": "", "scope": "high-clay soils"}, {"value": "0.024", "what": "Difference in CV R\u00b2 between low-clay and high-clay", "unit": "R\u00b2", "denominator": "", "scope": "95% CI: \u22120.423, 0.161"}]
caveat: "Both groups have negative CV R\u00b2, and the cause (distributional shift, outliers, or true unpredictability) is undiagnosed, so the test may reflect modelling failure rather than a biological null."
first_added: "2026-10-27"
source_hash: "f3931fe9d68922f56c7c150229f466d5cddab2ea6b166362e8b31933149f9a8d"
---
# Clay shield efficiency test shows no significant difference

In the shield efficiency test, low-clay CV R² was −0.268 and high-clay CV R² was −0.292, a difference of 0.024 [95% CI: −0.423, 0.161] that is not significant because the CI includes zero. [src: soil_frontier_genomics]

## Key figures

- **−0.268 R²**: Low-clay cross-validated R² (scope low-clay soils) [src: soil_frontier_genomics]
- **−0.292 R²**: High-clay cross-validated R² (scope high-clay soils) [src: soil_frontier_genomics]
- **0.024 R²**: Difference in CV R² between low-clay and high-clay (scope 95% CI: −0.423, 0.161) [src: soil_frontier_genomics]

## Evidence

> - **Shield efficiency test**: low-clay CV R² = −0.268, high-clay CV R² = −0.292; difference = 0.024 [95% CI: −0.423, 0.161] — **not significant, CI includes zero**. [src: soil_frontier_genomics]

From the report [[summaries/soil_frontier_genomics__REPORT]].

## Caveat

Both groups have negative CV R², and the cause (distributional shift, outliers, or true unpredictability) is undiagnosed, so the test may reflect modelling failure rather than a biological null. [src: soil_frontier_genomics]

> **Negative out-of-sample R² diagnosis is incomplete.** All three predictive model families achieve negative CV R², meaning they predict worse than the training mean. Three possible causes have not been distinguished: (a) train/test distributional shift due to spatial autocorrelation within GroupKFold folds, (b) high-leverage outlier samples in test folds that dominate the MSE, or (c) genuine unpredictability of functional gene counts from the measured predictors at global scale. These three causes have different scientific implications — only (c) supports a strong null result interpretation. Causes (a) and (b) would indicate a modelling failure, not a biological null result. [src: soil_frontier_genomics]

## Other caveats in this report

- The report is preliminary: clay-shield and GDI analyses are complete, but spatial validation and figures remain pending. [src: soil_frontier_genomics]
- GDI is a novel index without published precedent; it can equal 902 with zero genomes (completeness = 0, denominator = 1), and richness may dominate its combined measure of sampling gap and richness. [src: soil_frontier_genomics]
- Forest GDI 902.36 and Cropland GDI 890.82 differ by 1.3%; without bootstrap confidence intervals, the report says they are not meaningfully distinguishable and should not be ranked. [src: soil_frontier_genomics]
- The +0.8-unit pH gap needs a sampling-effort check: fewer alkaline-soil genomes could reflect fewer sequenced samples rather than an assembly or annotation gap. [src: soil_frontier_genomics]
- NB05 validations require re-running the 16S and completeness data; no local CSV output is available. [src: soil_frontier_genomics]
