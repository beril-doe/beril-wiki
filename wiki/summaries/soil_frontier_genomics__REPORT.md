---
type: "Summary"
description: "Tests the clay shield hypothesis and identifies alkaline-soil genomic sampling gaps."
doc_type: "short"
full_text: "sources/soil_frontier_genomics__REPORT.md"
---
# Soil Microbial Dark Matter and the Clay Shield Null Result

## Overview

This preliminary report evaluates the global-scale clay shield hypothesis using 5,441 soil samples and introduces a Genomic Discovery Index (GDI) to characterize spatial gaps in genomic representation. Clay-shield and GDI analyses are complete across all source notebooks, while NB05 spatial validation and NB06 figures remain pending. [src: soil_frontier_genomics]

## Key Findings

### Clay shield hypothesis

The dataset contains 5,441 soil samples with clay content, mine proximity, nighttime lights, uranium, and functional gene counts (`n_genes_by_counts`). All predictive model families had negative out-of-sample R²: Soil & Climate, R² = −0.205 ± 0.197; Geochemical, R² = −0.331 ± 0.071; and Industrial, R² = −0.221 ± 0.042. [src: soil_frontier_genomics]

The shield-efficiency test produced low-clay cross-validation R² = −0.268 and high-clay cross-validation R² = −0.292, with a difference of 0.024 and 95% CI: −0.423, 0.161. Because the confidence interval includes zero, the difference was not significant. Clay was a consistent feature, with importance approximately 0.14, but did not improve predictive accuracy in high-clay soils. [src: soil_frontier_genomics]

At global scale, the clay shield hypothesis is not supported. Clay content showed correlational associations with microbial functional potential and some interaction with industrial stressors, but high-clay soils were not more predictable than low-clay soils. The negative out-of-sample R² values indicate that functional potential was not predictable from the measured stressors at this scale, although the report states that spatial autocorrelation, batch effects, and unmeasured confounders may contribute. [src: soil_frontier_genomics]

### Genomic Discovery Index

The GDI is defined as OTU Richness / (Mean Genome Completeness + 1), calculated at 1° spatial bins. Forest had GDI = 902.36 and cropland had GDI = 890.82, while grassland had GDI = 503.42 and wetland had GDI = 525.13. Forest and cropland were therefore identified as jointly highest-GDI biomes, whereas grassland and wetland were relatively well-mapped. [src: soil_frontier_genomics]

Frontier areas with GDI > 1000 had mean pH = 6.74, compared with mean pH = 5.94 in mapped areas, a +0.8 pH unit gap. The report interprets this as evidence of systematic under-sampling of alkaline soil microbiomes in public genomic databases. [src: soil_frontier_genomics]

The GDI results indicate that forest and cropland soils are diverse but poorly represented at the genomic level, creating a potential limitation for functional inferences based on genome reference databases in these biomes. [src: soil_frontier_genomics]

## Caveats and Required Validation

The negative out-of-sample R² diagnosis is incomplete. The three model families predict worse than the training mean, but the analyses do not distinguish among train/test distributional shift caused by spatial autocorrelation within GroupKFold folds, high-leverage outlier samples dominating test-fold mean squared error, and genuine unpredictability of functional gene counts from the measured predictors at global scale. Only the third explanation would support a strong biological null interpretation; the first two would indicate modelling failure. [src: soil_frontier_genomics]

The GDI is a novel index without published precedent. Because GDI = Richness / (Mean_Completeness + 1), it can equal 902 even when there are zero genomes, because completeness = 0 makes the denominator 1. The index also conflates sampling gap and OTU richness, potentially allowing the richness term to dominate; separate reporting of richness and completeness with a two-dimensional scatterplot may be more interpretable. [src: soil_frontier_genomics]

The Forest GDI = 902.36 versus Cropland GDI = 890.82 difference is 1.3%; without bootstrap confidence intervals, the two values are not meaningfully distinguishable. The report therefore recommends describing forest and cropland as jointly the highest-GDI biomes rather than implying a ranked ordering. [src: soil_frontier_genomics]

The +0.8 pH unit discovery-bias gap requires a reverse-causality check. Alkaline soils may have fewer genomes in databases because fewer samples from those pH ranges were sequenced, rather than because alkaline microbes are harder to assemble or less studied. Controlling for the number of 16S samples in each pH bin before computing GDI would distinguish assembly or annotation gaps from sampling gaps. [src: soil_frontier_genomics]

Pending analyses are: decomposing negative R² into distributional shift, outlier leverage, and true unpredictability using spatial blocking; computing rarefaction-corrected GDI after uniform 16S sequencing-depth correction; estimating bootstrap 95% CIs for biome-level GDI rankings; controlling pH discovery bias for the number of 16S samples per pH bin; and reporting Forest versus Cropland GDI with uncertainty. These NB05 validations require re-running from the BERIL Observatory 16S tables and `kbase_ke_pangenome` completeness data because no local CSV output is available. [src: soil_frontier_genomics]

## Slots Into

- [[concepts/functional-dark-matter]] — The GDI identifies forest and cropland genomic under-representation and an alkaline-soil sampling gap relevant to uncharacterized microbial functional potential. [src: soil_frontier_genomics]
- [[concepts/environment-embedding-geography]] — The report tests spatially structured prediction and shows that spatial autocorrelation and distributional shift must be separated from biological unpredictability. [src: soil_frontier_genomics]
- [[concepts/provenance-aware-resource-discovery]] — The proposed controls for 16S sampling effort and completeness highlight the need to distinguish database sampling gaps from assembly or annotation gaps. [src: soil_frontier_genomics]
