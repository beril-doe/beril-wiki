---
type: "Concept"
description: "Tests whether environmental embeddings capture ecological variation relevant to bacterial gene content."
sources: ["summaries/ecotype_analysis__REPORT.md"]
---
# Ecological Validity of Environmental Embeddings

## Scope

This concept concerns whether environmental embeddings capture ecological variation at a resolution relevant to bacterial genome and gene-content comparisons. The [[summaries/ecotype_analysis__REPORT]] analysis evaluated whether environmental similarity or phylogenetic similarity better predicted gene-content similarity across bacterial species. [src: ecotype_analysis]

## Key Evidence

The analysis included 172 bacterial species with sufficient environmental and phylogenetic data, drawn from 13,381 genomes across 224 species. [src: ecotype_analysis] Environmental embeddings were obtained from [[entities/alph-aearth]], while genome metadata, taxonomy, isolation-source information, pangenome composition, and gene-cluster presence/absence profiles were also used. [src: ecotype_analysis]

A partial correlation, defined here as the association between two variables after accounting for a third variable, had a median value of 0.0025 for environment and 0.0143 for phylogeny. [src: ecotype_analysis] Phylogeny dominated the gene-content signal in 60.5% of species, whereas environment dominated in 39.5% of species. [src: ecotype_analysis]

Only 12 species (7.0%) showed a significant positive environmental effect, while 4 species (2.3%) showed a significant negative environmental effect and 156 species (90.7%) showed no significant environmental effect. [src: ecotype_analysis] These results support the interpretation that vertical inheritance generally dominates genome-wide gene-content similarity, while environmental adaptation may be concentrated in specific gene subsets rather than reflected across the whole genome. [src: ecotype_analysis]

## Ecological-Validity Limitations

AlphaEarth embeddings covered only 28.4% of genomes in the analysis, limiting the environmental signal available for comparison with gene content. [src: ecotype_analysis] Geographic coordinates in NCBI metadata were often missing or imprecise, further reducing the quality of environmental associations. [src: ecotype_analysis] For host-associated bacteria, coordinates may describe collection sites rather than the organisms’ actual microenvironments, making geographic location a weak proxy for ecological exposure. [src: ecotype_analysis]

The analysis used partial correlations between distance matrices and therefore assumed linear relationships; this approach may miss nonlinear ecological effects. [src: ecotype_analysis] Environmental and host-associated bacteria did not show a significant difference in environmental effects (p=0.66), but the limited biological meaning of host-associated geographic coordinates constrains that comparison. [src: ecotype_analysis]

## Interpretation and Relations

The findings **refine** [[concepts/ecotype-environment-gene-content]] by indicating that whole-genome gene-content similarity is usually more strongly structured by phylogeny than by the available environmental representation. [src: ecotype_analysis] They also **support** [[concepts/environment-embedding-geography]] because incomplete embedding coverage, imprecise coordinates, and collection-site bias can weaken associations between environmental distance and genomic variation. [src: ecotype_analysis]

The result **supports** [[concepts/environmental-resistome]] by showing that metadata resolution and the mismatch between collection location and organismal microenvironment can limit ecological inference. [src: ecotype_analysis] It **connects to** [[concepts/pangenome-integration]] because the environmental test was performed against pangenome gene-content similarity rather than against a single phenotype. [src: ecotype_analysis]

The analysis suggests the hypothesis that AlphaEarth embeddings do not fully capture ecologically relevant environmental variation. [src: ecotype_analysis] This is a hypothesis rather than an established limitation of all environmental embeddings because the analysis had incomplete embedding coverage and relied partly on imperfect geographic metadata. [src: ecotype_analysis]

## Tensions

The analysis found that environmental similarity was generally weaker than phylogenetic similarity for explaining genome-wide gene-content similarity, while also allowing environmental effects to dominate in 39.5% of species. [src: ecotype_analysis] This is a quantitative tension between a broad phylogenetic pattern and species-level exceptions, not evidence that environmental effects are absent. [src: ecotype_analysis]

## Open Directions

- Use the 13,381-genome metadata set and alternative environmental embedding distances to test whether non-AlphaEarth representations recover stronger associations with gene-content similarity. [src: ecotype_analysis]
- Combine direct environmental metadata with embedding distances and partial-correlation or nonlinear distance-based methods to ask whether environmental effects are hidden by linear modeling or coarse descriptors. [src: ecotype_analysis]
- Partition gene clusters into COG functional categories, including V-Defense and L-Mobile, and test whether category-specific associations with environment exceed the whole-genome signal. [src: ecotype_analysis]
- For species with identified ecotype clusters, compare gene content between clusters to determine whether environmental structure is detectable at the ecotype or locus level despite weak genome-wide correlations. [src: ecotype_analysis]
- Restrict host-associated analyses to metadata describing actual microenvironments rather than collection coordinates and test whether the environmental effect changes. [src: ecotype_analysis]
