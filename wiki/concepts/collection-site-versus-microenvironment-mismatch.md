---
type: "Concept"
description: "Collection coordinates may not represent an organism's true habitat."
sources: ["summaries/ecotype_analysis__REPORT.md"]
---
# Collection-Site Versus Organismal Microenvironment Mismatch

## Overview

Collection-site versus organismal microenvironment mismatch occurs when geographic coordinates recorded for a microbial sample describe where it was collected rather than the physical, chemical, or host-associated environment experienced by the organism. [src: ecotype_analysis] This mismatch can weaken tests of whether environmental similarity predicts bacterial gene-content similarity. [src: ecotype_analysis]

The issue is especially relevant for host-associated bacteria, for which collection coordinates may represent the sampling location while the biologically relevant microenvironment is inside or on the host. [src: ecotype_analysis] The [[summaries/ecotype_analysis__REPORT]] provides the principal evidence for this limitation.

## Evidence from Ecotype Correlation Analysis

The analysis evaluated 172 bacterial species with sufficient environmental and phylogenetic data and compared environmental and phylogenetic distances with gene-content similarity. [src: ecotype_analysis] Across these species, the median partial correlation for environment was 0.0025, compared with 0.0143 for phylogeny. [src: ecotype_analysis] Partial correlation measures the association between two variables while accounting for another variable. [src: ecotype_analysis]

Phylogeny dominated the gene-content signal in 60.5% of species, whereas environment dominated in 39.5% of species. [src: ecotype_analysis] A significant positive environmental effect was detected in 12 species (7.0%), a significant negative environmental effect in 4 species (2.3%), and no significant environmental effect in 156 species (90.7%). [src: ecotype_analysis] These results support [[concepts/ecotype-environment-gene-content]] and [[concepts/environmental-embedding-ecological-validity]] by showing that weak environmental associations may reflect limitations in environmental representation rather than the absence of ecological differentiation. [src: ecotype_analysis]

Environmental and host-associated bacteria did not show a significant difference in environmental effects (p=0.66). [src: ecotype_analysis] This result does not establish that host-associated organisms lack environmental structuring, because geographic coordinates may not encode their actual microenvironments. [src: ecotype_analysis] The finding therefore supports treating collection-site coordinates as potentially mismatched proxies for organismal exposure, rather than as direct measurements of habitat conditions. [src: ecotype_analysis]

## Data and Representation Limitations

The analysis used AlphaEarth environmental embeddings, genome metadata, taxonomy, NCBI environmental and isolation-source metadata, pangenome composition, and gene-cluster presence/absence profiles queried from the kbase_ke_pangenome database. [src: ecotype_analysis] It extracted data for 13,381 genomes across 224 species and produced correlation results for 172 species. [src: ecotype_analysis]

AlphaEarth embeddings covered only 28.4% of genomes, limiting the environmental signal available for analysis. [src: ecotype_analysis] Geographic coordinates in NCBI metadata were often missing or imprecise, reducing the quality of environmental associations. [src: ecotype_analysis] These limitations connect this concept to [[concepts/environmental-resistome]], [[concepts/environment-embedding-geography]], and [[concepts/collection-site-versus-microenvironment-mismatch]]. [src: ecotype_analysis]

The partial-correlation analysis assumed linear relationships between distance matrices and may not have captured nonlinear ecological effects. [src: ecotype_analysis] The analysis also suggested the hypothesis that AlphaEarth embeddings do not fully capture ecologically relevant environmental variation. [src: ecotype_analysis]

## Interpretation

The overall result supports the interpretation that vertical inheritance generally dominates genome-wide gene-content similarity, while environmental adaptation may act on specific gene subsets rather than across the whole genome. [src: ecotype_analysis] It also refines [[concepts/ecotype-environment-gene-content]] by identifying a measurement problem: environmental predictors can be biologically misaligned with the organism even when their geographic coordinates are available. [src: ecotype_analysis]

The weak environmental signal should therefore not be interpreted as definitive evidence that collection environments are irrelevant to gene content. [src: ecotype_analysis] A more defensible interpretation is that the analysis measured environmental similarity imperfectly, particularly for host-associated organisms and samples with incomplete or imprecise metadata. [src: ecotype_analysis]

## Tensions

The analysis found that phylogeny dominated gene-content similarity in most species, but it also found that environment dominated in 39.5% of species. [src: ecotype_analysis] This is a within-analysis tension between broad genome-wide ancestry effects and species-specific ecological effects, not a contradiction that can be resolved by averaging the two signals. [src: ecotype_analysis] Testing functional subsets rather than whole-genome gene content could determine whether environmental associations are concentrated in particular categories. [src: ecotype_analysis]

## Open Directions

- Combine the 13,381-genome metadata table with direct environmental metadata and alternative embedding distances, then test whether environmental predictors improve gene-content associations after accounting for phylogenetic distance. [src: ecotype_analysis]
- Stratify the 172-species result by host-associated versus environmental lifestyle and replace collection coordinates with host, tissue, body-site, or other organism-proximal metadata where available; test whether the environmental effect changes. [src: ecotype_analysis]
- Use COG functional categories, including V-Defense and L-Mobile, instead of whole-genome gene content to ask whether collection-site mismatch obscures environment-associated variation in specific gene subsets. [src: ecotype_analysis]
- For species with identified ecotypes, compare gene content between ecotype clusters using organism-proximal environmental metadata and ask whether within-species contrasts recover associations missed by collection-site coordinates. [src: ecotype_analysis]
