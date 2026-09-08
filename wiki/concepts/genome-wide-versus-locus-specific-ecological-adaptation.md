---
type: Concept
description: Distinguishes genome-wide ancestry effects from locus-specific ecological
  adaptation.
sources:
- id: ecotype_analysis
  resource: ../summaries/ecotype_analysis__REPORT.md
  title: ecotype analysis
- id: ecotype_functional_differentiation
  resource: ../summaries/ecotype_functional_differentiation__REPORT.md
  title: ecotype functional differentiation
- id: pangenome_openness
  resource: ../summaries/pangenome_openness__REPORT.md
  title: pangenome openness
- id: ecotype_env_reanalysis
  resource: ../summaries/ecotype_env_reanalysis__REPORT.md
  title: ecotype env reanalysis
title: Genome-Wide Versus Locus-Specific Ecological Adaptation
---
# Genome-Wide Versus Locus-Specific Ecological Adaptation

This concept distinguishes genome-wide gene-content similarity driven by ancestry from ecological adaptation concentrated in particular genes, pathways, or functional categories. The [ecotype_analysis__REPORT](../summaries/ecotype_analysis__REPORT.md) provides the central test: across bacterial species, phylogenetic similarity generally explained more of genome-wide gene-content similarity than environmental similarity, while the results leave open the possibility that ecology acts more strongly at specific loci. [^ecotype_analysis]

## Core Interpretation

The analysis supports the interpretation that vertical inheritance generally dominates genome-wide bacterial gene-content similarity, whereas environmental adaptation may be concentrated in specific gene subsets rather than distributed uniformly across the genome. [^ecotype_analysis] New evidence from [ecotype_functional_differentiation__REPORT](../summaries/ecotype_functional_differentiation__REPORT.md) **supports and refines** this interpretation: within-species gene-content ecotypes showed systematic differences in COG functional profiles, with adaptive categories having larger effect sizes than housekeeping categories, although the analysis did not test environmental selection directly. [^ecotype_functional_differentiation] This **refines** [pangenome-integration](pangenome-integration.md) by indicating that integrating environmental and phylogenetic distances at the whole-genome level can obscure ecological signals restricted to particular functional categories. [^ecotype_analysis]

The result is consistent with a model in which clonal ancestry structures broad genome-wide similarity, while horizontal gene transfer and selection contribute to population structure at particular loci. [^ecotype_analysis] The ecotype analysis **supports** the locus-specific component of this model: valid gene-content ecotypes were detected in 12 of 15 sampled species, and all 12 showed at least one significantly differentiated COG category. [^ecotype_functional_differentiation] This **connects** the question to [phylogenetic-confounding-of-pangenome-associations](phylogenetic-confounding-of-pangenome-associations.md), because genome-wide ancestry can make an ecological association appear weaker or less general than a locus-specific association. [^ecotype_analysis]

The pangenome openness analysis **refines** this interpretation rather than demonstrating locus-specific adaptation: openness showed no significant relationship with either the environment effect (Spearman rho = -0.05, p-value = 0.54) or the phylogeny effect (Spearman rho = 0.03, p-value = 0.73). [^pangenome_openness] Thus, open-versus-closed pangenome status did not predict which force dominated gene-content variation in the tested species, suggesting that a single genome-wide openness metric is insufficient to identify eco-phylogenetic dynamics. [^pangenome_openness] The report further proposes, as hypotheses rather than direct demonstrations, that pangenome structure may be independent of eco-phylogenetic dynamics and that core/accessory classification may miss genes relevant to functional adaptation. [^pangenome_openness]

The [ecotype_env_reanalysis__REPORT](../summaries/ecotype_env_reanalysis__REPORT.md) **supports** the environmental null interpretation rather than the hypothesis that clinical sampling bias explains it: using genome-level harmonized classifications, environmental species did not show stronger environment–gene-content correlations than human-associated species (one-sided Environmental > Human-associated test U=1536, p=0.83). [^ecotype_env_reanalysis] This **refines** the earlier environmental-versus-host comparison (p=0.66) by using a more systematic classification while retaining the conclusion that the comparison does not establish stronger environmental effects. [^ecotype_analysis][^ecotype_env_reanalysis]

## Evidence

The study evaluated 172 bacterial species with sufficient environmental and phylogenetic data. [^ecotype_analysis] Across these species, the median partial correlation for environment was 0.0025, compared with 0.0143 for phylogeny; partial correlation measures the association between two variables while accounting for another variable. [^ecotype_analysis]

Phylogeny dominated the gene-content signal in 60.5% of species, whereas environment dominated in 39.5% of species. [^ecotype_analysis] A significant positive environment effect was detected in 12 species (7.0%), a significant negative environment effect in 4 species (2.3%), and no significant effect in 156 species (90.7%). [^ecotype_analysis] These results **support** phylogeny as the stronger general predictor of whole-genome gene-content similarity, but they do not exclude ecological effects in a minority of species or in restricted genomic regions. [^ecotype_analysis]

Environmental and host-associated bacteria did not show a significant difference in environmental effects (p=0.66). [^ecotype_analysis] The analysis cautioned that geographic coordinates for host-associated bacteria may represent collection sites rather than the organisms’ actual microenvironments. [^ecotype_analysis] The reanalysis **supports** this null result: among 224 species selected with >=20 genomes having AlphaEarth embeddings and >=30% coverage, 106 (47%) were majority human-associated, 47 (21%) majority environmental, and 71 (32%) Mixed/Other, confirming strong clinical sampling bias without finding stronger environmental correlations. [^ecotype_env_reanalysis]

The source analysis used environmental embeddings from [alph-aearth](../entities/alph-aearth.md), genome metadata and taxonomy, NCBI environmental and isolation-source metadata, pangenome composition, and gene-cluster presence/absence profiles queried from [kbase-ke-pangenome](../entities/kbase-ke-pangenome.md). [^ecotype_analysis] It extracted data for 13,381 genomes across 224 species and produced correlation results for 172 species. [^ecotype_analysis]

The ecotype study provides functional evidence adjacent to this genome-wide result: across 257 COG-category tests, 170 (66.1%) were significant after BH-FDR (Benjamini–Hochberg false-discovery-rate) correction at q < 0.05. [^ecotype_functional_differentiation] Adaptive categories had a significance rate of 79.8% (67/84), compared with 68.8% (33/48) for housekeeping categories, and mean effect sizes of 0.0136 versus 0.0064; the one-sided Mann–Whitney U test gave p = 2.53 x 10^-6. [^ecotype_functional_differentiation] This **supports** the hypothesis that ecotype-associated differentiation is concentrated more strongly in adaptive functions, but it remains evidence of functional differentiation rather than proof of environmental causation. [^ecotype_functional_differentiation]

## Scope and Limitations

Environmental embeddings from [alph-aearth](../entities/alph-aearth.md) covered only 28.4% of genomes, limiting the environmental signal available for analysis. [^ecotype_analysis] Geographic coordinates in NCBI metadata were often missing or imprecise, reducing the quality of environmental associations. [^ecotype_analysis] Partial correlations assume linear relationships between distance matrices and may fail to capture nonlinear ecological effects. [^ecotype_analysis]

The evidence for locus-specific adaptation is therefore a hypothesis suggested by the weak whole-genome environmental signal, not a direct demonstration that particular loci are environmentally selected. [^ecotype_analysis] The ecotype results **strengthen but do not remove** this limitation: approximately 38% of gene clusters had COG annotations, leaving 62% unannotated, and the analysis lacked within-species phylogenetic controls, so functional differences could reflect annotation bias or phylogenetic and demographic substructure. [^ecotype_functional_differentiation] The analysis did not establish that any specific COG functional category has a stronger environmental association than whole-genome gene content. [^ecotype_analysis]

The openness result has a related limitation: the sample included only species with both pangenome statistics and ecotype-analysis results, openness was represented by a single summary metric, and the environment and phylogeny effects were derived from partial correlations. [^pangenome_openness] The upstream ecotype analysis may also have had limited statistical power for some species with few genomes. [^pangenome_openness] These constraints prevent the null openness relationships from ruling out functional or locus-specific ecological adaptation. [^pangenome_openness]

The reanalysis **refines** the methodological limitation: its median partial correlation across 183 species was 0.081, whereas the original analysis reported 0.003 and characterized the difference as 27x; the reanalysis used all genomes with embeddings, including up to 3,505 genomes per species, rather than diversity-maximizing downsampling capped at 250 genomes. [^ecotype_env_reanalysis] Absolute correlations are therefore not comparable across methods, although the within-method environmental-versus-human-associated comparison remains interpretable. [^ecotype_env_reanalysis]

## Tensions

The dataset indicates that environment dominated the gene-content signal in 39.5% of species, yet significant positive or negative environmental effects were detected in only 12 species (7.0%) and 4 species (2.3%), respectively. [^ecotype_analysis] This apparent tension may reflect differences between dominance in comparative effect sizes and statistical significance, but the source does not resolve that distinction. [^ecotype_analysis]

The absence of a strong genome-wide environmental signal may indicate that ecological adaptation is locus-specific, but it may also result from incomplete AlphaEarth coverage, imprecise metadata, or environmental embeddings that do not capture biologically relevant variation. [^ecotype_analysis] The ecotype study adds functional differentiation without environmental assignment or phylogenetic control, so it **supports** the locus-specific hypothesis while leaving the ecological interpretation unresolved. [^ecotype_functional_differentiation]

The null relationship between pangenome openness and environment or phylogeny effects **qualifies** the interpretation that broad pangenome structure can explain genome-wide versus locus-specific ecological dynamics: openness did not predict either effect, but this test did not directly compare individual loci or functional categories. [^pangenome_openness] It therefore does not contradict the evidence for functional differentiation, while leaving unresolved whether openness metrics conceal category-specific ecological associations. [^pangenome_openness][^ecotype_functional_differentiation]

The original and reanalysis correlation magnitudes also cannot be treated as a directly replicated effect: the reanalysis reports a median of 0.081 across 183 species versus 0.003 in the original analysis, while the original page reports 0.0025 across its 172-species analysis. [^ecotype_env_reanalysis][^ecotype_analysis] This **refines** rather than resolves the comparison, because the reanalysis attributes the discrepancy to different genome sets and downsampling procedures and explicitly preserves only the within-method group comparison. [^ecotype_env_reanalysis]

## Open Directions

- Use the existing 13,381-genome dataset and test COG functional categories, including V-Defense and L-Mobile, with the same distance-based correlation framework to determine whether specific functional subsets show stronger environmental effects than whole-genome gene content. [^ecotype_analysis]
- Reanalyze the 172 species with alternative [alph-aearth](../entities/alph-aearth.md) embedding distances and direct environmental metadata to test whether the weak environmental signal is caused by representation or distance-choice limitations. [^ecotype_analysis]
- For species with identified ecotype clusters, compare gene-cluster presence/absence profiles between clusters while controlling for phylogenetic similarity to test whether ecological differentiation is concentrated in particular loci. [^ecotype_analysis]
- Quantify the effect of missing or imprecise geographic metadata by repeating the analysis on species and genomes with higher-resolution environmental records, asking whether environmental effects become stronger when microenvironment assignments improve. [^ecotype_analysis]
- Extend the ecotype analysis to all 456 eligible species and overlay core-genome phylogenetic trees with habitat metadata to test whether COG differentiation persists after ancestry and environment are modeled jointly. [^ecotype_functional_differentiation]
- Replace openness with auxiliary fraction, Heap’s law alpha, or pangenome fluidity, and stratify by gene function and lifestyle, to test whether alternative pangenome metrics reveal category-specific ecological or phylogenetic effects missed by openness. [^pangenome_openness]
- Compare downsampled and full-genome extraction on the same species, controlling genome count as a covariate, to determine whether sampling depth or gene-cluster extraction changes explain the 27x correlation discrepancy. [^ecotype_env_reanalysis]
- Repeat the environmental comparison with structured ENVO terms and functional subsets, testing whether more precise habitat definitions reveal locus-specific associations masked by whole-genome Jaccard distances. [^ecotype_env_reanalysis]

[^ecotype_analysis]: [ecotype analysis](../summaries/ecotype_analysis__REPORT.md)
[^ecotype_functional_differentiation]: [ecotype functional differentiation](../summaries/ecotype_functional_differentiation__REPORT.md)
[^pangenome_openness]: [pangenome openness](../summaries/pangenome_openness__REPORT.md)
[^ecotype_env_reanalysis]: [ecotype env reanalysis](../summaries/ecotype_env_reanalysis__REPORT.md)
