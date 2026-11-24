---
type: "Summary"
description: "Summary of the project Soil Microbial Dark Matter and the Clay Shield Null Result."
doc_type: "short"
full_text: "sources/soil_frontier_genomics__REPORT.md"
---
# Soil Microbial Dark Matter and the Clay Shield Null Result

This page summarises the soil_frontier_genomics report. It asked whether clay content shields soil microbial functional potential from industrial stressors, and where soil genomes are least represented in public databases. The clay shield hypothesis was not supported at global scale, and the evidence is weak because every predictive model had negative out-of-sample R². The report is preliminary: clay shield and Genomic Discovery Index (GDI) analyses are complete, but NB05 spatial validation and NB06 figures are pending. [src: soil_frontier_genomics]

## Key Findings

### Clay shield null result

No model predicted soil functional gene counts better than the training mean, and clay did not help in high-clay soils. The analysis used 5,441 soil samples with clay content, mine proximity, nighttime lights, uranium, and functional gene counts (n_genes_by_counts). [src: soil_frontier_genomics] All predictive models had negative out-of-sample R². [src: soil_frontier_genomics] The values were:

| Model | Out-of-sample R² |
|---|---|
| Soil & Climate | −0.205 ± 0.197 [src: soil_frontier_genomics] |
| Geochemical | −0.331 ± 0.071 [src: soil_frontier_genomics] |
| Industrial | −0.221 ± 0.042 [src: soil_frontier_genomics] |

In the shield efficiency test, low-clay cross-validation (CV) R² was −0.268 and high-clay CV R² was −0.292. The difference was 0.024 [95% confidence interval (CI): −0.423, 0.161], which is not significant because the CI includes zero. [src: soil_frontier_genomics] Clay was a consistent model feature with importance ≈ 0.14, yet it did not improve predictive accuracy in high-clay soils. [src: soil_frontier_genomics] Clay content shows correlational associations with microbial functional potential and some interaction with industrial stressors. [src: soil_frontier_genomics] The report concludes that the clay shield hypothesis is not supported at global scale. [src: soil_frontier_genomics]

The report suggests that the failure to predict functional potential is likely due to spatial autocorrelation, batch effects, and unmeasured confounders. [src: soil_frontier_genomics] That is an explanation, not a measured result (see the caveats below). See [[concepts/clay-content-as-a-protective-modifier-of-soil-microbial-functional-potential]] and [[concepts/interpreting-negative-out-of-sample-r-in-environmental-predictive-models]].

### Genomic discovery gap by biome

Forest and cropland soils are the genomic frontier; grassland and wetland are comparatively well mapped. The report defines GDI = OTU Richness / (Mean Genome Completeness + 1), computed at 1° spatial bins. OTU means operational taxonomic unit. [src: soil_frontier_genomics] The highest GDI values were Forest (902.36) and Cropland (890.82). [src: soil_frontier_genomics] The lower values were Grassland (503.42) and Wetland (525.13), described as relatively well-mapped. [src: soil_frontier_genomics] The report describes forest and cropland soils as diverse but poorly represented at the genomic level. It says this matters for any functional inference drawn from genome reference databases in these biomes. [src: soil_frontier_genomics]

### pH discovery bias

Frontier areas (GDI > 1000) had mean pH = 6.74, against mean pH = 5.94 in mapped areas. This is a +0.8 pH unit gap, which the report interprets as systematic under-sampling of alkaline soil microbiomes in public genomic databases. [src: soil_frontier_genomics] This interpretation is unconfirmed (see the caveats below). See [[concepts/genomic-discovery-gap-indices-and-database-representation-bias]].

## Data and Methods

The clay analysis used 5,441 soil samples with clay, mine proximity, nighttime lights, uranium, and gene-count variables. [src: soil_frontier_genomics] Three model families were evaluated with out-of-sample R². [src: soil_frontier_genomics] GDI was computed at 1° spatial bins. [src: soil_frontier_genomics] The pending NB05 validations need Spark reruns from the BERIL Observatory 16S tables and kbase_ke_pangenome completeness data. [src: soil_frontier_genomics] No local CSV output exists for them. [src: soil_frontier_genomics]

## Caveats and Open Work

### Negative R² is not fully diagnosed

The report states that its diagnosis of the negative R² is incomplete. All three model families predict worse than the training mean. [src: soil_frontier_genomics] Three causes have not been distinguished:
- Train/test distributional shift from spatial autocorrelation within GroupKFold folds. [src: soil_frontier_genomics]
- High-leverage outlier samples in test folds that dominate the mean squared error (MSE). [src: soil_frontier_genomics]
- Genuine unpredictability of functional gene counts from the measured predictors at global scale. [src: soil_frontier_genomics]

Only genuine unpredictability supports a strong biological null. Distributional shift or outlier leverage would indicate a modelling failure. [src: soil_frontier_genomics] So the "not supported" conclusion is weaker than a clean null.

### GDI validity

- GDI is a novel index without published precedent. [src: soil_frontier_genomics]
- The formula gives a GDI of 902 even with zero genomes (completeness = 0, denominator = 1). [src: soil_frontier_genomics]
- GDI conflates sampling gap and OTU richness, and the richness term alone could dominate it. [src: soil_frontier_genomics]
- Separate reporting of richness and completeness, with a 2D scatter, would be more interpretable. [src: soil_frontier_genomics]
- Forest (902.36) and Cropland (890.82) differ by 1.3%. Without bootstrap CIs they are not meaningfully distinguishable. [src: soil_frontier_genomics]
- The report recommends describing them as jointly the highest-GDI biomes, not as a ranked order. [src: soil_frontier_genomics]
- The +0.8 pH gap needs a reverse-causality check. Alkaline soils may have fewer database genomes because fewer such samples were ever sequenced, not because the microbes are harder to assemble or less studied. [src: soil_frontier_genomics]
- Controlling for the number of 16S samples in each pH bin before computing GDI would separate assembly/annotation gaps from sampling gaps. [src: soil_frontier_genomics]

### Pending work

1. Decompose the negative R² into distributional shift, outlier leverage, and true unpredictability. This requires a rerun with spatial blocking. [src: soil_frontier_genomics]
2. Compute a rarefaction-corrected GDI, using uniform 16S sequencing depth before the richness calculation. [src: soil_frontier_genomics]
3. Compute bootstrap 95% CIs on biome-level GDI rankings. This requires a raw-data rerun. [src: soil_frontier_genomics]
4. Control the pH discovery bias for the number of 16S samples per pH bin. [src: soil_frontier_genomics]
5. Report Forest versus Cropland GDI with uncertainty before claiming a ranked ordering. [src: soil_frontier_genomics]

## Slots Into

- [[concepts/clay-content-as-a-protective-modifier-of-soil-microbial-functional-potential]]: the shield efficiency difference of 0.024 [95% CI: −0.423, 0.161] includes zero, so the shield is not supported. [src: soil_frontier_genomics]
- [[concepts/interpreting-negative-out-of-sample-r-in-environmental-predictive-models]]: all three model families have negative CV R², and the causes are not yet distinguished. [src: soil_frontier_genomics]
- [[concepts/genomic-discovery-gap-indices-and-database-representation-bias]]: the GDI places forest and cropland at the frontier, and the report lists validity limits for the index. [src: soil_frontier_genomics]
