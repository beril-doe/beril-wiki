---
type: "Concept"
description: "Local co-occurrence clusters of genera in Oak Ridge groundwater communities and whether they reflect a global pH and temperature niche axis; it stops at causal microbial interactions."
sources: ["summaries/genotype_to_phenotype_enigma__REPORT.md"]
---
# pH-driven niche partitioning and genus co-occurrence in contaminated subsurface communities

In Oak Ridge groundwater, two groups of genera rise and fall in opposition to each other, and the genotype_to_phenotype_enigma report links this pattern to a global pH and temperature gradient. The evidence is correlational: it comes from one local survey and one global 16S dataset, and it does not show direct microbial interactions. [src: genotype_to_phenotype_enigma] See [[summaries/genotype_to_phenotype_enigma__REPORT]] and [[entities/enigma]] for context.

## Local co-occurrence clusters

Spearman correlation across 587 Oak Ridge 100-Well-Survey communities identifies two anti-correlated genus clusters with 47 significant pairs (|rho| > 0.2, p < 0.01). [src: genotype_to_phenotype_enigma] Cluster A contains Brevundimonas, Caulobacter, Sphingomonas, Variovorax and Sphingobium, and its strongest pair has rho = +0.56. [src: genotype_to_phenotype_enigma] Cluster B contains Rhodanobacter, Ralstonia, Dyella, Serratia and Comamonas, with rho = +0.40. [src: genotype_to_phenotype_enigma] The two clusters are negatively correlated, for example Brevundimonas–Rhodanobacter at rho = -0.34. [src: genotype_to_phenotype_enigma]

## Global pH and temperature axis

The report finds that the local pattern is recapitulated across 464K global 16S samples as a pH-driven niche partition. [src: genotype_to_phenotype_enigma] Worldwide, the Rhodanobacter-Ralstonia-Dyella cluster occupies environments 1.35 pH units more acidic and 6.9°C warmer than the Brevundimonas-Caulobacter-Sphingomonas cluster. [src: genotype_to_phenotype_enigma] Cluster B environments average pH 5.4, versus 6.8 for Cluster A. [src: genotype_to_phenotype_enigma] The report's comparison table gives the same figures:

| Measure | Cluster A | Cluster B | Difference |
|---|---|---|---|
| Mean pH | 6.78 [src: genotype_to_phenotype_enigma] | 5.43 [src: genotype_to_phenotype_enigma] | -1.35 [src: genotype_to_phenotype_enigma] |
| Mean temperature | 15.7 C [src: genotype_to_phenotype_enigma] | 22.6 C [src: genotype_to_phenotype_enigma] | +6.9 C [src: genotype_to_phenotype_enigma] |
| Exclusive samples (global) | 179,023 [src: genotype_to_phenotype_enigma] | 3,720 [src: genotype_to_phenotype_enigma] | 48x rarer [src: genotype_to_phenotype_enigma] |
| Dominant environments | aquatic 33%, plant 23%, soil 22% [src: genotype_to_phenotype_enigma] | aquatic 39%, soil 23%, plant 18% [src: genotype_to_phenotype_enigma] | |

## Interpretation

The report reads the pattern as mirroring the Oak Ridge contamination gradient, where nitric acid leachate lowers pH in plume wells. [src: genotype_to_phenotype_enigma] It calls Cluster B organisms acid-tolerant generalists enriched wherever pH drops, such as contamination sites, peatlands and acidic soils. [src: genotype_to_phenotype_enigma] It says Cluster A organisms prefer neutral, cooler conditions typical of uncontaminated groundwater. [src: genotype_to_phenotype_enigma] From this it concludes that the pattern is a fundamental microbial niche axis rather than site-specific adaptation. [src: genotype_to_phenotype_enigma] These are the report's interpretations of the correlations.

The report also draws a prediction from this. It argues that pH tolerance is a first-order phenotype that genotype-to-phenotype models must capture. [src: genotype_to_phenotype_enigma] It hypothesizes that Cluster B strains should show different pH-dependent growth profiles from Cluster A strains, and that the genomic features distinguishing the clusters should predict pH tolerance. [src: genotype_to_phenotype_enigma] The report presents this global niche partition as one of the foundations of its first phase. [src: genotype_to_phenotype_enigma]

## Caveats and proposed checks

Co-occurrence is correlation, not causation. Spearman co-occurrence suggests shared or exclusive niches but does not prove direct interaction. [src: genotype_to_phenotype_enigma] The report proposes compositionally aware SparCC analysis on the full 100WS ASV (amplicon sequence variant) matrix to strengthen the findings. [src: genotype_to_phenotype_enigma] The report has no geochemistry linkage yet. Uranium, nitrate and metal concentrations per well are in CORAL bricks 10/80, but sample-to-location name resolution is incomplete. [src: genotype_to_phenotype_enigma] The report proposes linking strain-isolation-well coordinates in coral_strain_locations.tsv to per-well geochemistry, to test whether acid-tolerant Cluster B strains come from higher-contamination wells locally. [src: genotype_to_phenotype_enigma]

## Open Directions

- Run SparCC on the full 100WS ASV matrix to test whether the two clusters hold up beyond Spearman correlation.
- Finish sample-to-location name resolution, then join per-well geochemistry to the community data.
- Link strain-isolation wells to per-well geochemistry to test the local origin of Cluster B strains.
- Measure pH-dependent growth for Cluster A and Cluster B strains, and test whether genomic features separating the clusters predict pH tolerance.
