---
type: "Compound"
description: "Uranium\u2019s ecological associations and metal-specific fitness determinants"
sources: ["summaries/lab_field_ecology__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/metal_specificity__REPORT.md"]
---
# Uranium

## Identity

- **Canonical name:** uranium. [src: lab_field_ecology]
- **Known aliases:** None reported in the source document. [src: lab_field_ecology]
- **Stable external identifier:** None reported in the source document. [src: lab_field_ecology]

## Evidence from Lab–Field Ecology

The [[summaries/lab_field_ecology__REPORT]] study used uranium concentration as a geochemical gradient across 108 [[entities/oak-ridge-field-research-center]] groundwater sites and compared it with community composition measured by [[entities/16s-amplicon-sequencing]] and laboratory metal-tolerance scores from [[entities/kescience-fitnessbrowser]]. [src: lab_field_ecology]

Five of 11 tested genera had significant uranium associations after Benjamini–Hochberg false-discovery-rate correction: [[entities/herbaspirillum]] increased with uranium (Spearman rho=+0.336, p=3.8e-4, FDR q=0.001); [[entities/bacteroides]] increased (rho=+0.264, p=0.006, q=0.013); [[entities/caulobacter-vibrioides]] decreased (rho=-0.411, p=1.0e-5, q=1.1e-4); [[entities/sphingomonas]] decreased (rho=-0.382, p=4.5e-5, q=2.5e-4); and [[entities/pedobacter]] decreased (rho=-0.266, p=0.005, q=0.013). [src: lab_field_ecology]

[[entities/azospirillum-brasilense]] showed a marginal positive association with uranium (rho=+0.20, p=0.042, q=0.077). [[entities/desulfovibrio-vulgaris-hildenborough]] showed no correlation (rho=0.022, p=0.82), and [[entities/pseudomonas-fluorescens]] showed no correlation (rho=-0.059, p=0.55). [src: lab_field_ecology]

The correlation between laboratory-derived metal-tolerance score and the high-uranium/low-uranium field abundance ratio was positive but not statistically significant (Spearman rho=0.503, p=0.095, n=12 genera). [src: lab_field_ecology]

The report therefore treats the aggregate tolerance relationship as suggestive rather than supported, while finding that uranium-associated genus-level responses were bidirectional. [src: lab_field_ecology]

Sites divided at the median uranium concentration had distinct community compositions, including changes in top genera and greater prominence of rare-biosphere taxa and subsurface specialists at high-uranium sites. [src: lab_field_ecology]

The report interprets these patterns as broader ecological restructuring rather than a simple increase in metal-tolerant organisms, because redox conditions and carbon and energy sources also vary among sites. [src: lab_field_ecology]

## Cross-Species Fitness Atlas

The [[summaries/metal_fitness_atlas__REPORT]] atlas found 178 uranium-associated metal-important gene records, with a core fraction of 0.685 versus the atlas baseline, a core-fraction delta of +0.035, OR=1.18, and p=3.4e-01. [src: metal_fitness_atlas]

This **refines** the field result: the atlas does not establish a strong uranium-specific core-genome enrichment, while the field study likewise found a suggestive but non-significant aggregate tolerance relationship. Uranium had limited coverage—one or two organisms—so the atlas result is not directly comparable to the 108-site ecological gradient. [src: metal_fitness_atlas]

The [[summaries/metal_specificity__REPORT]] analysis classified 88 of 181 uranium-associated metal-important gene records (48.6%) as metal-specific, meaning they showed significant metal-stress defects but a sick rate below 5% across non-metal experiments. [src: metal_specificity]

This **supports** the distinction between uranium-associated determinants and broadly pleiotropic stress genes, but **refines** the atlas interpretation: nearly half of the classified records were condition-specific even though the aggregate uranium core-enrichment signal was weak. The fraction remains subject to the study’s locusId attrition and threshold limitations. [src: metal_specificity]

## Interpretation and Next Analyses

The uranium results connect to [[concepts/environment-embedding-geography]], because field abundance reflects a multidimensional geochemical and historical environment rather than uranium exposure alone. [src: lab_field_ecology]

They also inform [[concepts/condition-specific-fitness]]: the non-significant aggregate metal-tolerance result motivates testing uranium-specific fitness scores matched to site concentrations. [src: lab_field_ecology]

The distinction between uranium-specific and general-stress defects further connects to [[concepts/metal-cross-resistance]], with the 48.6% uranium-specific fraction providing evidence that uranium responses are neither wholly general nor wholly metal-specific. [src: metal_specificity]

The Oak Ridge setting connects uranium contamination with the [[concepts/environmental-resistome]] and with proposed analyses of metal-specific tolerance. [src: lab_field_ecology]

The report proposes multivariate CCA or RDA, methods for relating community composition to environmental variables while controlling for covariates, with pH, redox, and carbon sources included alongside uranium. [src: lab_field_ecology]

It also proposes species- or strain-level matching using ENIGMA CORAL metagenomic genome or assembly tables, temporal analysis across sampling dates, and addition of [[entities/rhodanobacter]] to the Fitness Browser. [src: lab_field_ecology]

The atlas further recommends concentration-relative-to-MIC normalization, phylogenetic independent contrasts, and uranium-specific fitness modeling to resolve whether the weak atlas signal reflects exposure differences, limited coverage, or genuinely modest uranium-specific effects. [src: metal_fitness_atlas]
