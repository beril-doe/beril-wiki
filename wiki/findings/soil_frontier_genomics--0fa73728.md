---
type: "Finding"
description: "All three model families had negative out-of-sample R\u00b2: Soil & Climate \u22120.205 \u00b1 0.197, Geochemical \u22120.331 \u00b1 0.071, and Industrial \u22120.221 \u00b1 0.042."
finding_id: "soil_frontier_genomics--0fa73728"
result: "null result"
source: "soil_frontier_genomics"
quantities: [{"value": "\u22120.205 \u00b1 0.197", "what": "Out-of-sample R\u00b2 for the Soil & Climate model", "unit": "R\u00b2", "denominator": "", "scope": "Soil & Climate model family"}, {"value": "\u22120.331 \u00b1 0.071", "what": "Out-of-sample R\u00b2 for the Geochemical model", "unit": "R\u00b2", "denominator": "", "scope": "Geochemical model family"}, {"value": "\u22120.221 \u00b1 0.042", "what": "Out-of-sample R\u00b2 for the Industrial model", "unit": "R\u00b2", "denominator": "", "scope": "Industrial model family"}]
caveat: "The cause of the negative cross-validation R\u00b2 is unresolved: distributional shift, high-leverage outliers, and genuine unpredictability are not distinguished, and only genuine unpredictability supports a biological null result."
first_added: "2026-10-27"
source_hash: "f3931fe9d68922f56c7c150229f466d5cddab2ea6b166362e8b31933149f9a8d"
---
# All soil functional-gene prediction models fail out-of-sample

All three model families had negative out-of-sample R²: Soil & Climate −0.205 ± 0.197, Geochemical −0.331 ± 0.071, and Industrial −0.221 ± 0.042. [src: soil_frontier_genomics]

## Key figures

- **−0.205 ± 0.197 R²**: Out-of-sample R² for the Soil & Climate model (scope Soil & Climate model family) [src: soil_frontier_genomics]
- **−0.331 ± 0.071 R²**: Out-of-sample R² for the Geochemical model (scope Geochemical model family) [src: soil_frontier_genomics]
- **−0.221 ± 0.042 R²**: Out-of-sample R² for the Industrial model (scope Industrial model family) [src: soil_frontier_genomics]

## Evidence

> - **All predictive models have negative out-of-sample R²**: - Soil & Climate: R² = −0.205 ± 0.197 - Geochemical: R² = −0.331 ± 0.071 - Industrial: R² = −0.221 ± 0.042 [src: soil_frontier_genomics]

From the report [[summaries/soil_frontier_genomics__REPORT]].

## Caveat

The cause of the negative cross-validation R² is unresolved: distributional shift, high-leverage outliers, and genuine unpredictability are not distinguished, and only genuine unpredictability supports a biological null result. [src: soil_frontier_genomics]

> **Negative out-of-sample R² diagnosis is incomplete.** All three predictive model families achieve negative CV R², meaning they predict worse than the training mean. Three possible causes have not been distinguished: (a) train/test distributional shift due to spatial autocorrelation within GroupKFold folds, (b) high-leverage outlier samples in test folds that dominate the MSE, or (c) genuine unpredictability of functional gene counts from the measured predictors at global scale. These three causes have different scientific implications — only (c) supports a strong null result interpretation. Causes (a) and (b) would indicate a modelling failure, not a biological null result. [src: soil_frontier_genomics]

## Other caveats in this report

- The report is preliminary: clay-shield and GDI analyses are complete, but spatial validation and figures remain pending. [src: soil_frontier_genomics]
- GDI is a novel index without published precedent; it can equal 902 with zero genomes (completeness = 0, denominator = 1), and richness may dominate its combined measure of sampling gap and richness. [src: soil_frontier_genomics]
- Forest GDI 902.36 and Cropland GDI 890.82 differ by 1.3%; without bootstrap confidence intervals, the report says they are not meaningfully distinguishable and should not be ranked. [src: soil_frontier_genomics]
- The +0.8-unit pH gap needs a sampling-effort check: fewer alkaline-soil genomes could reflect fewer sequenced samples rather than an assembly or annotation gap. [src: soil_frontier_genomics]
- NB05 validations require re-running the 16S and completeness data; no local CSV output is available. [src: soil_frontier_genomics]
