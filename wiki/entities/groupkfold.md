---
type: Method
description: Grouped cross-validation method for testing generalization across studies.
sources:
- id: euk_in_prok_correlates
  resource: ../summaries/euk_in_prok_correlates__REPORT.md
  title: euk in prok correlates
- id: soil_frontier_genomics
  resource: ../summaries/soil_frontier_genomics__REPORT.md
  title: soil frontier genomics
title: GroupKFold
---
# GroupKFold

## What this entity is

**Canonical name:** GroupKFold  
**Type:** method  
**Known aliases:** grouped cross-validation by study; study-held-out cross-validation. [^euk_in_prok_correlates]  
**Stable external identifier:** None reported in the source. [^euk_in_prok_correlates]

GroupKFold is a cross-validation method in which complete studies are held out as groups, preventing runs from the same study from appearing in both training and validation partitions. [^euk_in_prok_correlates]

## Use in the source projects

The project used GroupKFold by study to test whether environmental metadata predicted the GOTTCHA2-derived eukaryotic fraction beyond study or batch effects in 2,759 NMDC ReadbasedAnalysis runs from 9 studies. [^euk_in_prok_correlates]

A gradient-boosted model using environment achieved R²=0.35 under random cross-validation but R²=−0.30 under GroupKFold out-of-study validation. [^euk_in_prok_correlates] Adding sequencing metadata produced R²=−0.39 under GroupKFold, indicating no improvement in out-of-study prediction. [^euk_in_prok_correlates] The corresponding out-of-study detection AUC was 0.56, approximately chance. [^euk_in_prok_correlates]

These results show that GroupKFold exposed strong cross-study environment associations as largely study- or batch-confounded rather than reliably generalizable across held-out studies. [^euk_in_prok_correlates]

Within the dominant NEON soil study, a model using local environment and geography was evaluated with five-fold cross-validation and achieved R²=+0.17 ± 0.06, contrasting with the cross-study GroupKFold result of R²=−0.30. [^euk_in_prok_correlates] The within-study analysis controlled approximately for batch but remained potentially affected by sub-batch structure such as sampling campaigns. [^euk_in_prok_correlates]

The soil-frontier analysis **refines** this interpretation: negative out-of-sample R² under GroupKFold can reflect spatial autocorrelation within folds, train/test distribution shift, or high-leverage outliers, so it does not alone establish genuine global unpredictability. [^soil_frontier_genomics] It recommends spatial blocking and explicit decomposition of these effects before assigning a strong biological meaning to a negative R². [^soil_frontier_genomics]

## Interpretation and limitations

GroupKFold is especially relevant to [environment-embedding-geography](../concepts/environment-embedding-geography.md) because it distinguishes environmental signal that transfers across studies from signal that may encode study-specific sampling or processing. [^euk_in_prok_correlates] The method also supports the report's data-bridging workflow in [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md), where workflow runs were linked to biosamples and studies without treating pooled biosamples as independent observations. [^euk_in_prok_correlates]

The cross-study generalization test was under-powered because it included only approximately 9 studies, and one soil study accounted for approximately 43% of runs. [^euk_in_prok_correlates] The within-study result was demonstrated for one soil study only and may not extend to aquatic or host-associated collections. [^euk_in_prok_correlates]

The soil-frontier result therefore **supports** using held-out groups to expose transfer failures but **contradicts** treating every negative GroupKFold R² as evidence of biological nullity; spatially blocked validation, leverage diagnostics, and distribution-shift checks are needed to distinguish modelling failure from true unpredictability. [^soil_frontier_genomics]

## Related pages

- [euk_in_prok_correlates__REPORT](../summaries/euk_in_prok_correlates__REPORT.md) — source-project summary. [^euk_in_prok_correlates]
- [soil_frontier_genomics__REPORT](../summaries/soil_frontier_genomics__REPORT.md) — soil-scale validation of GroupKFold interpretation. [^soil_frontier_genomics]
- [environment-embedding-geography](../concepts/environment-embedding-geography.md) — environmental and geographic prediction under batch control. [^euk_in_prok_correlates]
- [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md) — linking workflow runs with biosamples and studies. [^euk_in_prok_correlates]
- [gottcha2](gottcha2.md) — classifier used to estimate relative eukaryotic abundance. [^euk_in_prok_correlates]

[^euk_in_prok_correlates]: [euk in prok correlates](../summaries/euk_in_prok_correlates__REPORT.md)
[^soil_frontier_genomics]: [soil frontier genomics](../summaries/soil_frontier_genomics__REPORT.md)
