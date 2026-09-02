---
type: "Concept"
description: "Tests whether ecology shapes whole genomes or specific gene loci"
sources: ["summaries/ecotype_analysis__REPORT.md"]
---
# Genome-Wide Versus Locus-Specific Ecological Adaptation

This concept distinguishes genome-wide gene-content similarity driven by ancestry from ecological adaptation concentrated in particular genes, pathways, or functional categories. The [[summaries/ecotype_analysis__REPORT]] provides the central test: across bacterial species, phylogenetic similarity generally explained more of genome-wide gene-content similarity than environmental similarity, while the results leave open the possibility that ecology acts more strongly at specific loci. [src: ecotype_analysis]

## Core Interpretation

The analysis supports the interpretation that vertical inheritance generally dominates genome-wide bacterial gene-content similarity, whereas environmental adaptation may be concentrated in specific gene subsets rather than distributed uniformly across the genome. [src: ecotype_analysis] This **refines** [[concepts/pangenome-integration]] by indicating that integrating environmental and phylogenetic distances at the whole-genome level can obscure ecological signals restricted to particular functional categories. [src: ecotype_analysis]

The result is consistent with a model in which clonal ancestry structures broad genome-wide similarity, while horizontal gene transfer and selection contribute to population structure at particular loci. [src: ecotype_analysis] This **connects** the question to [[concepts/phylogenetic-confounding-of-pangenome-associations]], because genome-wide ancestry can make an ecological association appear weaker or less general than a locus-specific association. [src: ecotype_analysis]

## Evidence

The study evaluated 172 bacterial species with sufficient environmental and phylogenetic data. [src: ecotype_analysis] Across these species, the median partial correlation for environment was 0.0025, compared with 0.0143 for phylogeny; partial correlation measures the association between two variables while accounting for another variable. [src: ecotype_analysis]

Phylogeny dominated the gene-content signal in 60.5% of species, whereas environment dominated in 39.5% of species. [src: ecotype_analysis] A significant positive environment effect was detected in 12 species (7.0%), a significant negative environment effect in 4 species (2.3%), and no significant effect in 156 species (90.7%). [src: ecotype_analysis] These results **support** phylogeny as the stronger general predictor of whole-genome gene-content similarity, but they do not exclude ecological effects in a minority of species or in restricted genomic regions. [src: ecotype_analysis]

Environmental and host-associated bacteria did not show a significant difference in environmental effects (p=0.66). [src: ecotype_analysis] The analysis cautioned that geographic coordinates for host-associated bacteria may represent collection sites rather than the organisms’ actual microenvironments. [src: ecotype_analysis]

The source analysis used environmental embeddings from [[entities/alph-aearth]], genome metadata and taxonomy, NCBI environmental and isolation-source metadata, pangenome composition, and gene-cluster presence/absence profiles queried from [[entities/kbase-ke-pangenome]]. [src: ecotype_analysis] It extracted data for 13,381 genomes across 224 species and produced correlation results for 172 species. [src: ecotype_analysis]

## Scope and Limitations

Environmental embeddings from [[entities/alph-aearth]] covered only 28.4% of genomes, limiting the environmental signal available for analysis. [src: ecotype_analysis] Geographic coordinates in NCBI metadata were often missing or imprecise, reducing the quality of environmental associations. [src: ecotype_analysis] Partial correlations assume linear relationships between distance matrices and may fail to capture nonlinear ecological effects. [src: ecotype_analysis]

The evidence for locus-specific adaptation is therefore a hypothesis suggested by the weak whole-genome environmental signal, not a direct demonstration that particular loci are environmentally selected. [src: ecotype_analysis] The analysis did not establish that any specific COG functional category has a stronger environmental association than whole-genome gene content. [src: ecotype_analysis]

## Tensions

The dataset indicates that environment dominated the gene-content signal in 39.5% of species, yet significant positive or negative environmental effects were detected in only 12 species (7.0%) and 4 species (2.3%), respectively. [src: ecotype_analysis] This apparent tension may reflect differences between dominance in comparative effect sizes and statistical significance, but the source does not resolve that distinction. [src: ecotype_analysis]

The absence of a strong genome-wide environmental signal may indicate that ecological adaptation is locus-specific, but it may also result from incomplete AlphaEarth coverage, imprecise metadata, or environmental embeddings that do not capture biologically relevant variation. [src: ecotype_analysis]

## Open Directions

- Use the existing 13,381-genome dataset and test COG functional categories, including V-Defense and L-Mobile, with the same distance-based correlation framework to determine whether specific functional subsets show stronger environmental effects than whole-genome gene content. [src: ecotype_analysis]
- Reanalyze the 172 species with alternative [[entities/alph-aearth]] embedding distances and direct environmental metadata to test whether the weak environmental signal is caused by representation or distance-choice limitations. [src: ecotype_analysis]
- For species with identified ecotype clusters, compare gene-cluster presence/absence profiles between clusters while controlling for phylogenetic similarity to test whether ecological differentiation is concentrated in particular loci. [src: ecotype_analysis]
- Quantify the effect of missing or imprecise geographic metadata by repeating the analysis on species and genomes with higher-resolution environmental records, asking whether environmental effects become stronger when microenvironment assignments improve. [src: ecotype_analysis]
