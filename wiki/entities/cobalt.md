---
type: "Compound"
description: "Divalent metal forming the strongest cross-resistance pair with nickel."
sources: ["summaries/comprehensive_metal_ecology__REPORT.md", "summaries/counter_ion_effects__REPORT.md", "summaries/metal_cross_resistance__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/metal_specificity__REPORT.md"]
aliases: ["Co"]
---
# Cobalt

Cobalt (Co) is a divalent metal. In Fitness Browser data it forms the strongest cross-resistance pair with [[entities/nickel]]. [src: metal_cross_resistance] The evidence is direct gene-fitness correlation across many organisms, plus genus-level ecological associations from one analysis.

## Key facts

- Cobalt has Fitness Browser (FB) metal-experiment coverage in 27 organisms. [src: metal_fitness_atlas] Aluminum, cobalt and nickel are the three United States Geological Survey (USGS) critical minerals with broad FB coverage. [src: metal_fitness_atlas]
- In the conservation analysis, cobalt (toxic) has 1,859 important genes, core fraction 0.859, delta +0.072, odds ratio (OR) 1.67 and p-value 8.1e-16. [src: metal_fitness_atlas]
- Counter-ion-corrected cobalt values are core fraction 0.866 against baseline 0.790, delta +0.076, unchanged by the correction. [src: counter_ion_effects]
- Of 2,324 metal-important gene records for cobalt, 1,167 (50.2%) are metal-specific. [src: metal_specificity]

## Cross-resistance

Co-Ni was the strongest metal pair, with median r ≈ 0.58 across 28 organisms from Proteobacteria, Bacteroidetes, Firmicutes and Actinobacteria. [src: metal_cross_resistance] In the consensus matrix, Co-Ni had mean Pearson r = 0.56 across 28 organisms and 100% sign consistency. [src: metal_cross_resistance] The report describes this as the classic divalent cation cross-resistance pair, validated at gene resolution across diverse phyla. [src: metal_cross_resistance]

Other cobalt pairs in the consensus matrix:

| Pair | Mean Pearson r | Organisms | Sign consistency |
|---|---|---|---|
| Co-Zn | 0.52 | 18 | 100% [src: metal_cross_resistance] |
| Co-Fe | 0.45 | 7 | 100% [src: metal_cross_resistance] |
| Co-Cu | 0.43 | 24 | 96% [src: metal_cross_resistance] |
| Al-Co | 0.30 | 20 | 95% [src: metal_cross_resistance] |

Al-Co and Al-Ni were the weakest pairs (median r ≈ 0.30). The report reads this as consistent with aluminum's distinct toxicity mechanism. [src: metal_cross_resistance] See universal positivity and chemistry specific magnitude of metal cross resistance and [[entities/aluminum]].

## Chloride counter-ion and NaCl overlap

In the per-metal NaCl-overlap analysis, cobalt (as chloride) had mean overlap of 41.3% across 18 organisms, with mean maximum Cl⁻ of 28 mM. [src: counter_ion_effects] Cobalt chloride delivers up to 500 mM Cl⁻, yet its overlap is lower than that of zinc sulfate. [src: counter_ion_effects] In Desulfovibrio vulgaris Hildenborough (DvH), the whole-genome fitness correlation between cobalt and NaCl was r=0.498. [src: counter_ion_effects] The report proposes comparing CoCl₂ 0.1 mM with CoSO₄ 0.1 mM in DvH. Cobalt has the highest Cl⁻ load in the current data, and the sulfate form would confirm mechanism. [src: counter_ion_effects] See [[concepts/counter-ion-confounding-in-metal-fitness-assays]] and [[entities/desulfovibrio-vulgaris-hildenborough]].

## Environmental associations

The comprehensive metal ecology report identifies cobalt as a secondary contributor to the GeoROC niche-breadth signal (β = +0.009, Benjamini-Hochberg (BH) p = 0.0084). The signal is attenuated but survives pH control (p = 0.020). Cobalt is also enriched in mafic rocks and komatiites. [src: comprehensive_metal_ecology] In the N_Co model with soil moisture added (n = 1,213 genera), bedrock cobalt had β = +0.0072, p = 0.021. pH had β = +0.0120, p = 5.2×10⁻³, and moisture was not significant (β = +0.003, p = 0.50). [src: comprehensive_metal_ecology] Soil moisture correlated negatively with bedrock cobalt at genus level (r = −0.140, p = 9.3×10⁻⁷). [src: comprehensive_metal_ecology] In the bacterial global MGnify metagenome-assembled genome (MAG) niche-breadth analysis, the Co-specific set of 101 KEGG orthologs (KOs) had a significant negative association (β = −0.022, BH false discovery rate p = 3.9×10⁻⁶). [src: comprehensive_metal_ecology] See [[concepts/environmental-drivers-of-genus-niche-breadth-and-metal-gene-density]].
