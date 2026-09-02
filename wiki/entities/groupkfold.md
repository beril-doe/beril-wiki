---
type: "Method"
description: "Grouped cross-validation method for testing generalization across studies."
sources: ["summaries/euk_in_prok_correlates__REPORT.md", "summaries/soil_frontier_genomics__REPORT.md"]
---
# GroupKFold

## What this entity is

**Canonical name:** GroupKFold  
**Type:** method  
**Known aliases:** grouped cross-validation by study; study-held-out cross-validation. [src: euk_in_prok_correlates]  
**Stable external identifier:** None reported in the source. [src: euk_in_prok_correlates]

GroupKFold is a cross-validation method in which complete studies are held out as groups, preventing runs from the same study from appearing in both training and validation partitions. [src: euk_in_prok_correlates]

## Use in the source projects

The project used GroupKFold by study to test whether environmental metadata predicted the GOTTCHA2-derived eukaryotic fraction beyond study or batch effects in 2,759 NMDC ReadbasedAnalysis runs from 9 studies. [src: euk_in_prok_correlates]

A gradient-boosted model using environment achieved R²=0.35 under random cross-validation but R²=−0.30 under GroupKFold out-of-study validation. [src: euk_in_prok_correlates] Adding sequencing metadata produced R²=−0.39 under GroupKFold, indicating no improvement in out-of-study prediction. [src: euk_in_prok_correlates] The corresponding out-of-study detection AUC was 0.56, approximately chance. [src: euk_in_prok_correlates]

These results show that GroupKFold exposed strong cross-study environment associations as largely study- or batch-confounded rather than reliably generalizable across held-out studies. [src: euk_in_prok_correlates]

Within the dominant NEON soil study, a model using local environment and geography was evaluated with five-fold cross-validation and achieved R²=+0.17 ± 0.06, contrasting with the cross-study GroupKFold result of R²=−0.30. [src: euk_in_prok_correlates] The within-study analysis controlled approximately for batch but remained potentially affected by sub-batch structure such as sampling campaigns. [src: euk_in_prok_correlates]

The soil-frontier analysis **refines** this interpretation: negative out-of-sample R² under GroupKFold can reflect spatial autocorrelation within folds, train/test distribution shift, or high-leverage outliers, so it does not alone establish genuine global unpredictability. [src: soil_frontier_genomics] It recommends spatial blocking and explicit decomposition of these effects before assigning a strong biological meaning to a negative R². [src: soil_frontier_genomics]

## Interpretation and limitations

GroupKFold is especially relevant to [[concepts/environment-embedding-geography]] because it distinguishes environmental signal that transfers across studies from signal that may encode study-specific sampling or processing. [src: euk_in_prok_correlates] The method also supports the report's data-bridging workflow in [[concepts/cross-tenant-data-bridging]], where workflow runs were linked to biosamples and studies without treating pooled biosamples as independent observations. [src: euk_in_prok_correlates]

The cross-study generalization test was under-powered because it included only approximately 9 studies, and one soil study accounted for approximately 43% of runs. [src: euk_in_prok_correlates] The within-study result was demonstrated for one soil study only and may not extend to aquatic or host-associated collections. [src: euk_in_prok_correlates]

The soil-frontier result therefore **supports** using held-out groups to expose transfer failures but **contradicts** treating every negative GroupKFold R² as evidence of biological nullity; spatially blocked validation, leverage diagnostics, and distribution-shift checks are needed to distinguish modelling failure from true unpredictability. [src: soil_frontier_genomics]

## Related pages

- [[summaries/euk_in_prok_correlates__REPORT]] — source-project summary. [src: euk_in_prok_correlates]
- [[summaries/soil_frontier_genomics__REPORT]] — soil-scale validation of GroupKFold interpretation. [src: soil_frontier_genomics]
- [[concepts/environment-embedding-geography]] — environmental and geographic prediction under batch control. [src: euk_in_prok_correlates]
- [[concepts/cross-tenant-data-bridging]] — linking workflow runs with biosamples and studies. [src: euk_in_prok_correlates]
- [[entities/gottcha2]] — classifier used to estimate relative eukaryotic abundance. [src: euk_in_prok_correlates]
