---
type: "Concept"
description: "Asks how well genome-derived carbon pathway profiles associate with or predict isolation environment and lifestyle within a genus; stops at species-level classification and does not cover phylogenetic modelling."
sources: ["summaries/discoveries.md", "summaries/pseudomonas_carbon_ecology__REPORT.md"]
---
# Carbon pathway profiles as predictors of environment and lifestyle

Genome-derived carbon pathway profiles in [[entities/pseudomonas]] are associated with isolation environment, but they predict it only modestly. [src: discoveries, pseudomonas_carbon_ecology] Lifestyle differences (free-living, plant-associated, host-associated) show up as small shifts in pathway richness that overlap heavily within a subgenus. [src: pseudomonas_carbon_ecology] The evidence comes from a single genus, with one significant association test and one classifier of moderate accuracy. The page stops at species-level classification.

## Association with isolation environment

Among free-living species, carbon profiles are significantly associated with isolation environment (PERMANOVA, permutational multivariate analysis of variance, p = 0.006). [src: discoveries] The detailed test behind the same p-value used a different population: 54 free-living and plant-associated species with at least 5 genomes and at least 60% majority environment agreement. It used 999 permutations. Between-group mean distance was 2.054, and within-group mean distance was 1.890. [src: pseudomonas_carbon_ecology] The between/within ratio was 1.087 (p = 0.006). [src: pseudomonas_carbon_ecology] The report reads this as evidence of metabolic niche partitioning within the genus. [src: pseudomonas_carbon_ecology] See [[entities/permanova]].

In principal component analysis (PCA) of these 54 species, the first 5 components captured 74.9% of carbon pathway variance. PC1 (principal component 1) explained 31.2% and PC2 explained 17.9%. [src: pseudomonas_carbon_ecology] The same variance figures are given for the 62-pathway profiles. [src: pseudomonas_carbon_ecology] See [[entities/principal-component-analysis]].

## Predictive accuracy

Prediction is modest. A Random Forest used 4 classes: soil (13), freshwater (13), plant_surface (19) and rhizosphere (6). It covered 51 species after filtering. Balanced accuracy was 0.408 +/- 0.169 in 5-fold stratified cross-validation (CV), against a 0.250 chance baseline. [src: pseudomonas_carbon_ecology] The report states that the profiles are not strongly predictive, though they carry ecological signal. [src: pseudomonas_carbon_ecology] They are insufficient alone to discriminate fine-grained environment types among free-living species. [src: pseudomonas_carbon_ecology] The report considers the hypothesis of ecology prediction from carbon profiles only partially supported. [src: pseudomonas_carbon_ecology] See [[entities/random-forest-classification]].

The report says the moderate accuracy likely reflects small class sizes, overlap between related environments such as soil and rhizosphere, and the coarse resolution of 62 GapMind pathways. [src: pseudomonas_carbon_ecology] See [[concepts/reliability-and-coverage-limits-of-gapmind-pathway-predictions]].

### Discriminating pathways

D-serine, arabinose, rhamnose and fucose are the most discriminating pathways. [src: discoveries] The classifier importances were:

| Pathway | Importance | Report's description |
|---|---|---|
| D-serine | 0.132 | associated with rhizosphere niches [src: pseudomonas_carbon_ecology] |
| Arabinose | 0.094 | plant-derived pentose sugar [src: pseudomonas_carbon_ecology] |
| Rhamnose | 0.086 | plant cell wall component [src: pseudomonas_carbon_ecology] |
| Fucose | 0.085 | plant/animal glycan sugar [src: pseudomonas_carbon_ecology] |
| Xylose | 0.070 | hemicellulose-derived sugar [src: pseudomonas_carbon_ecology] |

The report cites Ghirardi et al. (2012), who associated rhizosphere competence in fluorescent pseudomonads with catabolic profile diversity. It calls this consistent with D-serine, arabinose and rhamnose being top discriminators. [src: pseudomonas_carbon_ecology] It also cites Saati-Santamaria et al. (2022), who found niche-dependent functional divergence and environment-specific pathway sets in 3,274 Pseudomonas genomes. [src: pseudomonas_carbon_ecology]

## Lifestyle

Across species with at least 5 genomes, free-living and plant-associated species had higher pathway richness than host-associated species. The median was 57 pathways complete in more than 50% of genomes, against 55. [src: pseudomonas_carbon_ecology] Within the Pseudomonas_E subgenus the trend holds but the gaps are small. Plant-associated species averaged 56.7 pathways [src: pseudomonas_carbon_ecology], free-living 56.1 [src: pseudomonas_carbon_ecology] and host-associated 55.2. [src: pseudomonas_carbon_ecology] Lifestyle categories overlap substantially there, so lifestyle variation is subtler than the deep phylogenetic divide. [src: pseudomonas_carbon_ecology] See [[concepts/phylogenetic-structure-versus-ecological-adaptation-in-gene-content-patterns]].

## Caveats

Assigning each species one environment by majority vote obscures generalists. [src: pseudomonas_carbon_ecology] The report notes that P. fluorescens and P. putida are isolated from multiple environments. [src: pseudomonas_carbon_ecology] The report presents itself as the first systematic quantification of standardized carbon pathway profiles across 433 species and 12,732 genomes. [src: pseudomonas_carbon_ecology]

## Open Directions

- Replace majority-vote labels with multi-label or proportion-based environment assignments. This would test whether generalist species such as P. fluorescens and P. putida explain part of the modest accuracy.
- Merge soil and rhizosphere, or add more rhizosphere species (only 6 now). Then repeat the Random Forest to see whether class size and overlap limit accuracy.
- Add finer-resolution pathway or gene-level features beyond 62 GapMind pathways. Compare their accuracy with the 0.408 baseline.
- Test whether D-serine, arabinose, rhamnose and fucose still discriminate environments after accounting for phylogeny. This needs a phylogenetic model, which this page does not cover.
- Repeat the analysis in other genera to see whether the modest signal is specific to Pseudomonas.
