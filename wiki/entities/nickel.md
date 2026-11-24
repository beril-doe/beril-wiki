---
type: "Compound"
description: "Divalent metal whose toxicity cross-correlates strongly with cobalt and zinc at gene level."
sources: ["summaries/comprehensive_metal_ecology__REPORT.md", "summaries/counter_ion_effects__REPORT.md", "summaries/metal_cross_resistance__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/metal_specificity__REPORT.md"]
aliases: ["Ni"]
---
# Nickel

Nickel (Ni) is a divalent metal. Its strongest gene-level cross-resistance partner is cobalt, and zinc is also correlated. [src: metal_cross_resistance]

## Key facts

- Fitness Browser metal experiments cover nickel in 26 organisms. [src: metal_fitness_atlas]
- Nickel is categorized as toxic. In the Pan-Bacterial Metal Fitness Atlas it has 1,760 important genes. [src: metal_fitness_atlas]
- For nickel-important genes, the core fraction is 0.877, delta is +0.088, OR (odds ratio) is 1.93 and p is 3.0e-22. [src: metal_fitness_atlas] See [[concepts/core-genome-enrichment-of-metal-stress-fitness-genes]].
- A separate analysis reports the nickel core fraction changing from 0.882 to 0.892 against a baseline of 0.794. Delta strengthens from +0.088 to +0.098. [src: counter_ion_effects]

## Cross-resistance with other metals

Nickel's strongest partner is [[entities/cobalt]]. Co-Ni was the strongest metal pair, with median r ≈ 0.58 across 28 organisms. Those organisms span Proteobacteria, Bacteroidetes, Firmicutes and Actinobacteria. [src: metal_cross_resistance] The consensus matrix gives mean Pearson r = 0.56 for Co-Ni across 28 organisms, with 100% sign consistency. [src: metal_cross_resistance] The report describes this as validating the classic divalent cation cross-resistance pair at gene resolution across diverse phyla. [src: metal_cross_resistance]

The other nickel pairs in the consensus matrix are weaker than Co-Ni. All have high sign consistency. [src: metal_cross_resistance] See universal positivity and chemistry specific magnitude of metal cross resistance.

| Pair | Mean r | Organisms | Sign consistency |
|---|---|---|---|
| Ni-Zn (zinc) | 0.51 | 18 | 100% [src: metal_cross_resistance] |
| Cu-Ni ([[entities/copper]]) | 0.43 | 24 | 96% [src: metal_cross_resistance] |
| Fe-Ni ([[entities/iron]]) | 0.38 | 7 | 100% [src: metal_cross_resistance] |
| Al-Ni ([[entities/aluminum]]) | 0.34 | 20 | 95% [src: metal_cross_resistance] |

## Specificity and counter-ion effects

For nickel, 993 of 2,271 metal-important gene records (43.7%) are metal-specific. [src: metal_specificity] See [[concepts/metal-specific-versus-pleiotropic-stress-gene-classification]].

Nickel fitness also overlaps with salt stress. In [[entities/desulfovibrio-vulgaris-hildenborough]], the whole-genome fitness correlation between nickel and NaCl (sodium chloride) was r=0.446. [src: counter_ion_effects] In the per-metal NaCl-overlap analysis, nickel (chloride) had mean overlap of 39.3% across 17 organisms. The mean maximum Cl⁻ was 2 mM. [src: counter_ion_effects] See [[concepts/counter-ion-confounding-in-metal-fitness-assays]].

## Environmental niche breadth

In the joint GeoROC niche-breadth model, bedrock Ni has β = −0.0164, p = 5.5×10⁻⁵. The sign reverses, so Ni acts as a suppressor relative to Cr. [src: comprehensive_metal_ecology] The report calls this a partial-regression effect. It is consistent with Cr and Ni sharing a mafic rock association. It advises cautious interpretation because this GeoROC result is exploratory. [src: comprehensive_metal_ecology]

In the separate bacterial global MGnify MAG (metagenome assembled genomes) niche-breadth analysis, the Ni-specific set of 84 KOs (KEGG orthologs) has a significant negative association. β = −0.025 and BH-FDR (Benjamini-Hochberg false discovery rate) p = 1.9×10⁻⁷. [src: comprehensive_metal_ecology] See [[concepts/environmental-drivers-of-genus-niche-breadth-and-metal-gene-density]].
