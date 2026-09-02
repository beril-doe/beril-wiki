---
type: "Summary"
description: "Ecotype analysis finds phylogeny usually outweighs environment in gene-content similarity."
doc_type: "short"
full_text: "sources/ecotype_analysis__REPORT.md"
---
# Ecotype Correlation Analysis

## Overview

This analysis evaluated 172 bacterial species with sufficient environmental and phylogenetic data to test whether environmental similarity or phylogenetic similarity better predicts gene-content similarity. It found that phylogeny generally dominates, while environmental effects are weak and often statistically non-significant. [src: ecotype_analysis]

## Key Findings

- The median partial correlation for environment was 0.0025, compared with 0.0143 for phylogeny. Partial correlation measures the association between two variables while accounting for another variable. [src: ecotype_analysis]
- Phylogeny dominated the gene-content signal in 60.5% of species, whereas environment dominated in 39.5% of species. [src: ecotype_analysis]
- A significant positive environment effect was detected in 12 species (7.0%), a significant negative environment effect in 4 species (2.3%), and no significant effect in 156 species (90.7%). [src: ecotype_analysis]
- Environmental and host-associated bacteria did not show a significant difference in environmental effects (p=0.66). Host-associated geographic coordinates may represent collection sites rather than the organisms’ actual microenvironments. [src: ecotype_analysis]
- The interpretation is that vertical inheritance generally dominates genome-wide gene-content similarity, while environmental adaptation may act on specific gene subsets rather than the whole genome. The analysis also suggests the hypothesis that AlphaEarth embeddings do not fully capture ecologically relevant environmental variation. [src: ecotype_analysis]

## Analysis and Data

The study used environmental embeddings from AlphaEarth, genome metadata and taxonomy, NCBI environmental and isolation-source metadata, pangenome composition, and gene-cluster presence/absence profiles queried from the kbase_ke_pangenome database. It extracted data for 13,381 genomes across 224 species and produced correlation results for 172 species. [src: ecotype_analysis]

The supporting analyses used one notebook to extract embeddings, average nucleotide identity (ANI) distances, and gene clusters for 224 target species, and a second notebook to calculate correlations and generate visualizations. [src: ecotype_analysis]

The findings are consistent with cited literature describing clonal ancestry as a major influence on genome-wide bacterial variation and horizontal gene transfer as a contributor to population structure at specific loci rather than necessarily across entire genomes. [src: ecotype_analysis]

## Caveats

- AlphaEarth embeddings covered only 28.4% of genomes, limiting the environmental signal available for analysis. [src: ecotype_analysis]
- Geographic coordinates in NCBI metadata were often missing or imprecise, reducing the quality of environmental associations. [src: ecotype_analysis]
- Partial correlations assume linear relationships between distance matrices and may not capture nonlinear ecological effects. [src: ecotype_analysis]
- Geographic coordinates are less biologically meaningful for host-associated organisms because they generally describe collection sites rather than the organisms’ actual microenvironments. [src: ecotype_analysis]

## Future Directions

- Test whether specific COG functional categories, including V-Defense and L-Mobile, show stronger environmental effects than whole-genome gene content. [src: ecotype_analysis]
- Evaluate alternative embedding distances and direct environmental metadata as predictors. [src: ecotype_analysis]
- For species with identified ecotypes, compare gene content between ecotype clusters. [src: ecotype_analysis]

## Slots Into

- [[concepts/pangenome-integration]] — The comparison of environmental and phylogenetic distances against pangenome gene-content similarity provides evidence about how ecological context and ancestry structure bacterial accessory genomes. [src: ecotype_analysis]
