---
type: Compound
description: Uranium’s ecological associations and metal-specific fitness determinants
sources:
- id: lab_field_ecology
  resource: ../summaries/lab_field_ecology__REPORT.md
  title: lab field ecology
- id: metal_fitness_atlas
  resource: ../summaries/metal_fitness_atlas__REPORT.md
  title: metal fitness atlas
- id: metal_specificity
  resource: ../summaries/metal_specificity__REPORT.md
  title: metal specificity
title: Uranium
---
# Uranium

## Identity

- **Canonical name:** uranium. [^lab_field_ecology]
- **Known aliases:** None reported in the source document. [^lab_field_ecology]
- **Stable external identifier:** None reported in the source document. [^lab_field_ecology]

## Evidence from Lab–Field Ecology

The [lab_field_ecology__REPORT](../summaries/lab_field_ecology__REPORT.md) study used uranium concentration as a geochemical gradient across 108 [oak-ridge-field-research-center](oak-ridge-field-research-center.md) groundwater sites and compared it with community composition measured by [16s-amplicon-sequencing](16s-amplicon-sequencing.md) and laboratory metal-tolerance scores from [kescience-fitnessbrowser](kescience-fitnessbrowser.md). [^lab_field_ecology]

Five of 11 tested genera had significant uranium associations after Benjamini–Hochberg false-discovery-rate correction: [herbaspirillum](herbaspirillum.md) increased with uranium (Spearman rho=+0.336, p=3.8e-4, FDR q=0.001); [bacteroides](bacteroides.md) increased (rho=+0.264, p=0.006, q=0.013); [caulobacter-vibrioides](caulobacter-vibrioides.md) decreased (rho=-0.411, p=1.0e-5, q=1.1e-4); [sphingomonas](sphingomonas.md) decreased (rho=-0.382, p=4.5e-5, q=2.5e-4); and [pedobacter](pedobacter.md) decreased (rho=-0.266, p=0.005, q=0.013). [^lab_field_ecology]

[azospirillum-brasilense](azospirillum-brasilense.md) showed a marginal positive association with uranium (rho=+0.20, p=0.042, q=0.077). [desulfovibrio-vulgaris-hildenborough](desulfovibrio-vulgaris-hildenborough.md) showed no correlation (rho=0.022, p=0.82), and [pseudomonas-fluorescens](pseudomonas-fluorescens.md) showed no correlation (rho=-0.059, p=0.55). [^lab_field_ecology]

The correlation between laboratory-derived metal-tolerance score and the high-uranium/low-uranium field abundance ratio was positive but not statistically significant (Spearman rho=0.503, p=0.095, n=12 genera). [^lab_field_ecology]

The report therefore treats the aggregate tolerance relationship as suggestive rather than supported, while finding that uranium-associated genus-level responses were bidirectional. [^lab_field_ecology]

Sites divided at the median uranium concentration had distinct community compositions, including changes in top genera and greater prominence of rare-biosphere taxa and subsurface specialists at high-uranium sites. [^lab_field_ecology]

The report interprets these patterns as broader ecological restructuring rather than a simple increase in metal-tolerant organisms, because redox conditions and carbon and energy sources also vary among sites. [^lab_field_ecology]

## Cross-Species Fitness Atlas

The [metal_fitness_atlas__REPORT](../summaries/metal_fitness_atlas__REPORT.md) atlas found 178 uranium-associated metal-important gene records, with a core fraction of 0.685 versus the atlas baseline, a core-fraction delta of +0.035, OR=1.18, and p=3.4e-01. [^metal_fitness_atlas]

This **refines** the field result: the atlas does not establish a strong uranium-specific core-genome enrichment, while the field study likewise found a suggestive but non-significant aggregate tolerance relationship. Uranium had limited coverage—one or two organisms—so the atlas result is not directly comparable to the 108-site ecological gradient. [^metal_fitness_atlas]

The [metal_specificity__REPORT](../summaries/metal_specificity__REPORT.md) analysis classified 88 of 181 uranium-associated metal-important gene records (48.6%) as metal-specific, meaning they showed significant metal-stress defects but a sick rate below 5% across non-metal experiments. [^metal_specificity]

This **supports** the distinction between uranium-associated determinants and broadly pleiotropic stress genes, but **refines** the atlas interpretation: nearly half of the classified records were condition-specific even though the aggregate uranium core-enrichment signal was weak. The fraction remains subject to the study’s locusId attrition and threshold limitations. [^metal_specificity]

## Interpretation and Next Analyses

The uranium results connect to [environment-embedding-geography](../concepts/environment-embedding-geography.md), because field abundance reflects a multidimensional geochemical and historical environment rather than uranium exposure alone. [^lab_field_ecology]

They also inform [condition-specific-fitness](../concepts/condition-specific-fitness.md): the non-significant aggregate metal-tolerance result motivates testing uranium-specific fitness scores matched to site concentrations. [^lab_field_ecology]

The distinction between uranium-specific and general-stress defects further connects to [metal-cross-resistance](../concepts/metal-cross-resistance.md), with the 48.6% uranium-specific fraction providing evidence that uranium responses are neither wholly general nor wholly metal-specific. [^metal_specificity]

The Oak Ridge setting connects uranium contamination with the [environmental-resistome](../concepts/environmental-resistome.md) and with proposed analyses of metal-specific tolerance. [^lab_field_ecology]

The report proposes multivariate CCA or RDA, methods for relating community composition to environmental variables while controlling for covariates, with pH, redox, and carbon sources included alongside uranium. [^lab_field_ecology]

It also proposes species- or strain-level matching using ENIGMA CORAL metagenomic genome or assembly tables, temporal analysis across sampling dates, and addition of [rhodanobacter](rhodanobacter.md) to the Fitness Browser. [^lab_field_ecology]

The atlas further recommends concentration-relative-to-MIC normalization, phylogenetic independent contrasts, and uranium-specific fitness modeling to resolve whether the weak atlas signal reflects exposure differences, limited coverage, or genuinely modest uranium-specific effects. [^metal_fitness_atlas]

[^lab_field_ecology]: [lab field ecology](../summaries/lab_field_ecology__REPORT.md)
[^metal_fitness_atlas]: [metal fitness atlas](../summaries/metal_fitness_atlas__REPORT.md)
[^metal_specificity]: [metal specificity](../summaries/metal_specificity__REPORT.md)
