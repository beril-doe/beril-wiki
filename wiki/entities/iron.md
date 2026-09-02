---
type: "Compound"
description: "Iron (Fe), a metal condition associated with conserved fitness responses."
sources: ["summaries/metal_cross_resistance__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/metal_specificity__REPORT.md"]
---
# Iron (Fe)

## What this entity is

**Canonical name:** Iron. **Known alias:** Fe. **Stable external identifier:** No stable external identifier is reported in the source documents. [src: metal_cross_resistance, metal_fitness_atlas]

Iron is a metal condition analyzed in gene-level fitness experiments across diverse bacteria. [src: metal_cross_resistance] It is related to [[entities/zinc]], [[entities/cobalt]], and [[entities/copper]] in the study's cross-resistance analysis. [src: metal_cross_resistance]

## Key facts from the studies

Iron showed strong positive consensus cross-resistance with zinc, with a mean correlation of **r = 0.61 across 6 organisms**, the strongest association listed in the study. [src: metal_cross_resistance] The study reports that **98.1% of gene-level fitness correlations were positive (311/317)** across 317 organism-metal pair observations involving 28 organisms and 85 unique metal pairs. [src: metal_cross_resistance]

The iron-copper association had **r = 0.45 across 7 organisms**, while the iron-cobalt association also had **r = 0.45 across 7 organisms**. [src: metal_cross_resistance] These results support the study's broader finding that cross-resistance has a universal positive directional layer, while the magnitude of associations varies with metal chemistry. [src: metal_cross_resistance]

The report identifies shared cellular processes—including protein stability, DNA integrity, membrane function, and cofactor insertion—as possible contributors to the common positive direction of metal cross-resistance. [src: metal_cross_resistance] This interpretation remains subject to the study's caveat that no non-metal stress controls were tested, so the analysis cannot distinguish universal metal cross-resistance from a general-stress response to all metals. [src: metal_cross_resistance]

The [[summaries/metal_fitness_atlas__REPORT]] **refines** this cross-resistance picture by separating broadly required iron-stress functions from specialized resistance genes: it identified **651** iron-important genes with a **0.919** core fraction, a **+0.116** core-fraction delta, **OR = 3.07**, and **p = 8.5e-18**. [src: metal_fitness_atlas] Iron therefore showed stronger core-genome enrichment than the atlas's toxic-metal pattern, consistent with essential-metal stress exposing vulnerabilities in conserved cellular functions rather than only accessory resistance mechanisms. [src: metal_fitness_atlas] Iron produced **12.3% important genes** in the atlas, although iron had cross-species coverage in only **3 organisms**, so this comparison has limited coverage. [src: metal_fitness_atlas]

The metal-specificity analysis **refines** this atlas result by classifying **144/659 (21.9%)** iron-important gene records as metal-specific—the lowest metal-specific fraction reported among the metals tested—using fitness defects under metal experiments and a **<5%** sick rate across non-metal experiments. [src: metal_specificity] Thus, the new analysis supports the interpretation that iron responses include broadly required functions, while indicating that a smaller fraction is specifically attributable to iron stress rather than broader stress sensitivity. [src: metal_specificity]

## Related synthesis

Iron contributes evidence to [[concepts/metal-cross-resistance]], which synthesizes conserved positive cross-metal fitness correlations and chemistry-dependent association magnitudes. [src: metal_cross_resistance] The atlas **supports** this synthesis by showing that iron fitness defects are also enriched among conserved core genes, while **refining** it with the distinction between general metal-sensitive functions and specialized accessory resistance. [src: metal_fitness_atlas] The metal-specificity analysis further **refines** the distinction by quantifying the relatively small iron-specific subset and comparing it with non-metal fitness defects. [src: metal_specificity] Iron also contributes to [[concepts/cofitness-network-architecture]], because gene-level fitness correlations across iron and other metal conditions reveal shared structure across conditions. [src: metal_cross_resistance]

The underlying reports are [[summaries/metal_cross_resistance__REPORT]], [[summaries/metal_fitness_atlas__REPORT]], and [[summaries/metal_specificity__REPORT]]. [src: metal_cross_resistance, metal_fitness_atlas, metal_specificity]
