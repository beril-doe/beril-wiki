---
type: "Concept"
description: "How genome count and downsampling change pangenome correlation estimates"
sources: ["summaries/ecotype_env_reanalysis__REPORT.md"]
---
# Sampling Depth and Downsampling Effects

Genome sampling depth and downsampling can substantially alter estimated relationships between environmental context and bacterial gene-content variation. The [[summaries/ecotype_env_reanalysis__REPORT]] found that a reanalysis using all genomes with AlphaEarth embeddings produced partial-correlation values that were not directly comparable to those from an earlier diversity-maximized, downsampled analysis. [src: ecotype_env_reanalysis]

## Core Finding

The reanalysis used all genomes with embeddings, including up to 3,505 genomes per species, whereas the original analysis used diversity-maximizing downsampling with a maximum of 250 genomes per species. [src: ecotype_env_reanalysis] The median partial correlation across all 183 species was 0.081 in the reanalysis, compared with 0.003 in the original analysis, a difference characterized in the report as 27x. [src: ecotype_env_reanalysis] The report attributes the discrepancy partly to different genome sets and the resulting changes in distance distributions, while cautioning that the absolute correlation values should not be compared across the two methodologies. [src: ecotype_env_reanalysis]

This result **supports** the methodological principle that genome inclusion and sampling depth can change pangenome correlation estimates, even when the biological question is unchanged. [src: ecotype_env_reanalysis] It does not establish which method gives the more accurate absolute estimate because the reanalysis changed both the sampling strategy and the genome sets. [src: ecotype_env_reanalysis]

## Within-Method Group Comparison

A partial correlation here measures the association between environmental embedding similarity and gene-content similarity after accounting for the analysis covariates used by the project. [src: ecotype_env_reanalysis] Within the reanalysis methodology, Environmental species had a median partial correlation of 0.051, mean 0.073, standard deviation 0.299, and range [-0.50, 0.78]. [src: ecotype_env_reanalysis] Human-associated species had a median of 0.084, mean 0.110, standard deviation 0.226, and range [-0.30, 0.73]. [src: ecotype_env_reanalysis] Mixed/Other species had a median of 0.109, mean 0.148, standard deviation 0.261, and range [-0.38, 0.69]. [src: ecotype_env_reanalysis]

The one-sided Mann-Whitney U test for Environmental > Human-associated gave U=1536 and p=0.83, so the null hypothesis was not rejected. [src: ecotype_env_reanalysis] The continuous Spearman analysis found no relationship between the fraction of environmental genomes per species and partial-correlation strength, with rho=-0.085 and p=0.25. [src: ecotype_env_reanalysis] The corresponding analysis for the fraction of human-associated genomes gave rho=0.030 and p=0.69. [src: ecotype_env_reanalysis]

These within-method comparisons **refine** the interpretation of the 27x discrepancy: sampling and extraction choices changed the absolute correlation scale, but the environmental-versus-human-associated comparison remained internally consistent under the reanalysis protocol. [src: ecotype_env_reanalysis]

## Sampling Bias and NaN Filtering

The reanalysis confirmed strong clinical sampling bias in the AlphaEarth subset, but concluded that this bias did not explain the weak environment–gene content relationship. [src: ecotype_env_reanalysis] Among 224 species selected for the ecotype analysis, requiring >=20 genomes with AlphaEarth embeddings and >=30% coverage, 106 species (47%) were majority human-associated, 47 (21%) were majority environmental, and 71 (32%) were Mixed/Other. [src: ecotype_env_reanalysis]

Of the 30 species with NaN partial correlations, the NaN rate was 10/47 = 21% for Environmental species, 13/66 = 20% for Mixed/Other species, and 7/100 = 7% for Human-associated species. [src: ecotype_env_reanalysis] Environmental species were therefore disproportionately removed by NaN filtering rather than human-associated species. [src: ecotype_env_reanalysis] The report argues that this filtering would, if anything, bias the comparison toward finding a stronger environmental signal, which was not observed. [src: ecotype_env_reanalysis]

The unequal number of genomes per species remains a possible source of unequal statistical power, because species with more genomes may be better able to detect weak correlations. [src: ecotype_env_reanalysis] The report presents this as a possible explanation rather than a demonstrated cause. [src: ecotype_env_reanalysis]

## Interpretation for Pangenome Integration

The result **supports** [[concepts/pangenome-integration]] by showing that integrating environmental embeddings with gene-cluster data requires explicit control of genome-set construction and sampling depth. [src: ecotype_env_reanalysis] It also connects to [[concepts/ecotype-environment-gene-content]], because the environmental-versus-human-associated null result persisted after replacing the original sampling strategy with a full-genome extraction approach. [src: ecotype_env_reanalysis]

The reanalysis does not show that downsampling is intrinsically invalid, nor that using all available genomes is intrinsically preferable. [src: ecotype_env_reanalysis] Instead, it shows that the two approaches generated materially different correlation distributions and that their absolute values should not be treated as interchangeable. [src: ecotype_env_reanalysis]

## Tensions

The principal tension is between the large difference in overall correlation values and the stability of the within-method environmental-versus-human-associated comparison. [src: ecotype_env_reanalysis] The reanalysis reported a median partial correlation of 0.081 across 183 species, whereas the original analysis reported 0.003, but the report states that the absolute values are not comparable because the analyses used different genome sets, sampling strategies, and distance distributions. [src: ecotype_env_reanalysis] Resolving whether the difference is driven mainly by downsampling, genome-set composition, extraction behavior, or another methodological factor requires a controlled reanalysis. [src: ecotype_env_reanalysis]

## Open Directions

- Use the same species and genome universe to compare diversity-maximizing downsampling with full-genome extraction, then test whether sampling strategy or genome-set composition explains the partial-correlation discrepancy. [src: ecotype_env_reanalysis]
- Add genome count as a covariate to the species-level correlation model, then test whether unequal sampling depth inflates correlations in species with more genomes. [src: ecotype_env_reanalysis]
- Recompute correlations after matched-depth downsampling across species, then test whether the environmental-versus-human-associated comparison remains null when statistical power is balanced. [src: ecotype_env_reanalysis]
- Analyze functional gene subsets, including transport and secondary-metabolism categories, with identical downsampling and extraction settings, then test whether whole-genome Jaccard distances mask sampling-depth effects on specific functions. [src: ecotype_env_reanalysis]
- Reassess species with NaN correlations using alternative missing-data and minimum-sample thresholds, then test whether the higher Environmental NaN rate changes the group comparison. [src: ecotype_env_reanalysis]
