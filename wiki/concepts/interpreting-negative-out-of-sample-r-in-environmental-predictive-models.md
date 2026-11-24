---
type: "Concept"
description: "Covers how negative cross-validated R² in models predicting soil functional gene counts from environmental predictors should be diagnosed (distributional shift, outlier leverage, true unpredictability) and what it does or does not imply about a biological null; stops at the clay-shield test itself."
sources: ["summaries/soil_frontier_genomics__REPORT.md"]
---
# Interpreting negative out-of-sample R² in environmental predictive models

Negative out-of-sample R² means a model predicts worse than the training mean. [src: soil_frontier_genomics] In the soil_frontier_genomics report, every predictive model of soil functional gene counts had negative cross-validated (CV) R². [src: soil_frontier_genomics] The report's diagnosis of this result is incomplete: it suggests a likely explanation but has not tested it, so the result does not yet separate a modelling failure from a biological null. [src: soil_frontier_genomics] The evidence comes from one report. See [[summaries/soil_frontier_genomics__REPORT]] and [[concepts/clay-content-as-a-protective-modifier-of-soil-microbial-functional-potential]] for the clay-shield test itself.

## What was observed

All three predictive model families achieved negative CV R², so they predict worse than the training mean. [src: soil_frontier_genomics] The reported values are below.

| Model | Out-of-sample R² |
|---|---|
| Soil & Climate | −0.205 ± 0.197 [src: soil_frontier_genomics] |
| Geochemical | −0.331 ± 0.071 [src: soil_frontier_genomics] |
| Industrial | −0.221 ± 0.042 [src: soil_frontier_genomics] |

The shield efficiency test gave low-clay CV R² = −0.268 and high-clay CV R² = −0.292. The difference was 0.024 [95% confidence interval (CI): −0.423, 0.161], which is not significant because the CI includes zero. [src: soil_frontier_genomics] Clay appears as a consistent feature (importance ≈ 0.14) but does not improve predictive accuracy in high-clay soils. [src: soil_frontier_genomics] The report concludes that the clay shield hypothesis is not supported at global scale. [src: soil_frontier_genomics]

## Candidate diagnoses

The report names three causes that it has not distinguished [src: soil_frontier_genomics]:

- Train/test distributional shift, caused by spatial autocorrelation within GroupKFold folds. [src: soil_frontier_genomics]
- High-leverage outlier samples in test folds that dominate the mean squared error (MSE). [src: soil_frontier_genomics]
- Genuine unpredictability of functional gene counts from the measured predictors at global scale. [src: soil_frontier_genomics]

The report says its diagnosis of the negative R² is incomplete. [src: soil_frontier_genomics] It suggests the inability to predict is likely due to spatial autocorrelation, batch effects and unmeasured confounders. [src: soil_frontier_genomics] That is a suggested explanation, not a tested result. [src: soil_frontier_genomics]

## What it implies for a biological null

The three causes carry different implications. Only genuine unpredictability supports a strong null interpretation. Distributional shift or outlier leverage would indicate a modelling failure, not a biological null. [src: soil_frontier_genomics] The decomposition of the negative R² is still pending and requires a rerun with spatial blocking. [src: soil_frontier_genomics]

## Open Directions

- Rerun the models with spatial blocking and decompose the negative R² into shift, leverage and true unpredictability. This is the step the report lists as pending.
- Refit with outlier-robust metrics, such as median absolute error, or drop the highest-leverage test samples. This would show whether a few samples dominate the MSE.
- Compare spatially blocked and random folds on the same data. This would show how much of the negative R² comes from distributional shift.
- Repeat the shield efficiency comparison once the model has a positive baseline R². The current CI includes zero, and both R² values are negative.
