---
type: Method
description: Method for measuring associations while controlling for confounding variables
sources:
- id: ecotype_analysis
  resource: ../summaries/ecotype_analysis__REPORT.md
  title: ecotype analysis
- id: ecotype_env_reanalysis
  resource: ../summaries/ecotype_env_reanalysis__REPORT.md
  title: ecotype env reanalysis
- id: prophage_ecology
  resource: ../summaries/prophage_ecology__REPORT.md
  title: prophage ecology
- id: soil_metal_functional_genomics
  resource: ../summaries/soil_metal_functional_genomics__REPORT.md
  title: soil metal functional genomics
title: Partial correlation
---
# Partial correlation

## What this entity is

**Canonical name:** Partial correlation. [^ecotype_analysis]

Partial correlation measures the association between two variables while accounting for another variable. [^ecotype_analysis]

**Known aliases:** None reported in the source documents. [^ecotype_analysis][^ecotype_env_reanalysis]

**Stable external identifier:** None reported in the source documents. [^ecotype_analysis][^ecotype_env_reanalysis]

## Key applications and findings

The [ecotype_analysis__REPORT](../summaries/ecotype_analysis__REPORT.md) analysis used partial correlations to compare environmental and phylogenetic similarity as predictors of bacterial gene-content similarity across 172 species. [^ecotype_analysis]

The median partial correlation for environment was 0.0025, compared with 0.0143 for phylogeny. [^ecotype_analysis] Phylogeny dominated the gene-content signal in 60.5% of species, whereas environment dominated in 39.5% of species. [^ecotype_analysis] A significant positive environment effect was detected in 12 species (7.0%), a significant negative environment effect in 4 species (2.3%), and no significant effect in 156 species (90.7%). [^ecotype_analysis]

The analysis used environmental embeddings from [alph-aearth](alph-aearth.md), genome metadata and taxonomy, NCBI environmental and isolation-source metadata, pangenome composition, and gene-cluster presence/absence profiles from [kbase-ke-pangenome](kbase-ke-pangenome.md). [^ecotype_analysis] These results support the interpretation that vertical inheritance generally dominates genome-wide gene-content similarity, while environmental adaptation may act on specific gene subsets rather than the whole genome. [^ecotype_analysis]

The [prophage_ecology__REPORT](../summaries/prophage_ecology__REPORT.md) analysis **refines** this whole-genome result by applying a partial Spearman correlation to a more specific prophage-module phenotype: environmental niche breadth and prophage module count remained correlated at rho=0.468 after controlling for genome size, with p=8.41e-110, across 2,008 species with at least 5 embedded genomes. [^prophage_ecology] This **supports** the use of partial correlation for detecting environmental structure in targeted gene-module traits even when genome size is a major confounder, but it does not contradict the weak environment–whole-genome gene-content association because the response variables differ. [^prophage_ecology]

The [soil_metal_functional_genomics__REPORT](../summaries/soil_metal_functional_genomics__REPORT.md) report **extends** these applications to observational soil metagenomic data: partial-correlation models are planned to test whether COG–metal associations remain after controlling for co-varying chromium, copper, lead, and zinc. [^soil_metal_functional_genomics] This planned analysis is intended to distinguish metal-specific associations from a generic multi-metal-contamination response, rather than establish such specificity in the current results. [^soil_metal_functional_genomics]

## Reanalysis and methodological refinement

The [ecotype_env_reanalysis__REPORT](../summaries/ecotype_env_reanalysis__REPORT.md) **refines** the original null result by applying genome-level harmonized environmental classifications within a consistent reanalysis: environmental species had median partial correlation 0.051 versus 0.084 for human-associated species, and the one-sided Mann–Whitney U test for Environmental > Human-associated gave U=1536 and p=0.83. [^ecotype_env_reanalysis]

The reanalysis therefore **supports** the original conclusion that environmental species do not show a stronger environment–gene-content relationship, while showing that clinical sampling bias does not explain the weak signal. [^ecotype_env_reanalysis]

Its absolute correlations should not be compared directly with the original analysis: the reanalysis median across 183 species was 0.081 versus 0.003 originally, described as a 27x difference, because it used all genomes with embeddings rather than diversity-maximizing downsampling. [^ecotype_env_reanalysis]

The soil-metal application **refines** the method’s role from interpreting existing associations to a planned confounding-control test; the required COG–metal partial-correlation analysis cannot currently be completed because no local CSV contains the Spearman rho values or model residuals, and Spark access to the `kescience_mgnify` and `kbase_ke_pangenome` tables is required. [^soil_metal_functional_genomics]

## Limitations in this use

The partial-correlation analysis assumes linear relationships between distance matrices and may not capture nonlinear ecological effects. [^ecotype_analysis]

AlphaEarth embeddings covered only 28.4% of genomes, limiting the environmental signal available for analysis. [^ecotype_analysis] The prophage study likewise found that only 28% of genomes had AlphaEarth environmental embeddings, producing a biased subsample toward clinically and environmentally well-sampled lineages. [^prophage_ecology]

Geographic coordinates in NCBI metadata were often missing or imprecise, reducing the quality of environmental associations. [^ecotype_analysis] The analysis suggests the hypothesis that AlphaEarth embeddings do not fully capture ecologically relevant environmental variation. [^ecotype_analysis]

The reanalysis further found that environmental species had a 21% NaN partial-correlation rate versus 7% for human-associated species; this filtering did not reveal the hypothesized stronger environmental signal. [^ecotype_env_reanalysis]

The soil-metal application adds co-contamination and spatial dependence as limitations: positive correlations among metals may make ordinary FDR correction anti-conservative, and planned Moran’s I testing will assess spatial autocorrelation before any spatial-error validation. [^soil_metal_functional_genomics] These concerns **qualify** interpretation of the planned partial correlations because residual metal associations could reflect shared contamination or geography rather than the controlled metal alone. [^soil_metal_functional_genomics]

A downsampled-versus-full-genome extraction comparison, functional gene-subset tests, structured ENVO classification, and genome-count covariate analysis are needed to resolve the methodological discrepancy and test whether whole-genome distances mask environment-specific effects. [^ecotype_env_reanalysis]

## Related pages

- [pangenome-integration](../concepts/pangenome-integration.md) — The method was used to compare environmental and phylogenetic distances with pangenome gene-content similarity. [^ecotype_analysis]
- [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md) — The reanalysis strengthens the cross-project null result for environment–gene-content association. [^ecotype_env_reanalysis]
- [environmental-resistome](../concepts/environmental-resistome.md) — Planned partial-correlation tests will assess whether soil-metal-associated functional shifts are metal-specific. [^soil_metal_functional_genomics]
- [metal-cross-resistance](../concepts/metal-cross-resistance.md) — The method is proposed to separate individual-metal effects from correlated multi-metal contamination. [^soil_metal_functional_genomics]
- [environment-embedding-geography](../concepts/environment-embedding-geography.md) — The prophage analysis used an AlphaEarth-controlled partial correlation to relate environmental niche breadth to prophage module count. [^prophage_ecology]
- [average-nucleotide-identity](average-nucleotide-identity.md) — ANI distances were extracted as part of the supporting analysis. [^ecotype_analysis]
- [alph-aearth](alph-aearth.md) — Environmental embeddings supplied one predictor distance. [^ecotype_analysis]
- [kbase-ke-pangenome](kbase-ke-pangenome.md) — Gene-cluster presence/absence profiles supplied the gene-content data. [^ecotype_analysis]

[^ecotype_analysis]: [ecotype analysis](../summaries/ecotype_analysis__REPORT.md)
[^ecotype_env_reanalysis]: [ecotype env reanalysis](../summaries/ecotype_env_reanalysis__REPORT.md)
[^prophage_ecology]: [prophage ecology](../summaries/prophage_ecology__REPORT.md)
[^soil_metal_functional_genomics]: [soil metal functional genomics](../summaries/soil_metal_functional_genomics__REPORT.md)
