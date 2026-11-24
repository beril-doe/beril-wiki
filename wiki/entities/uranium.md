---
type: "Compound"
description: "Field contaminant at Oak Ridge; DvH uranium stress-response genes are described as deeply conserved."
sources: ["summaries/counter_ion_effects__REPORT.md", "summaries/field_vs_lab_fitness__REPORT.md", "summaries/lab_field_ecology__REPORT.md", "summaries/metal_cross_resistance__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/metal_specificity__REPORT.md"]
aliases: ["U"]
---
# Uranium

Uranium (U) is a field contaminant at Oak Ridge and the central ENIGMA contaminant. [src: metal_fitness_atlas] The evidence here is mixed. Uranium-response genes in DvH are described as deeply conserved [src: field_vs_lab_fitness], but the atlas test for core enrichment of uranium fitness genes is not significant and rests on only 2 organisms. [src: metal_fitness_atlas] See [[entities/desulfovibrio-vulgaris-hildenborough]] and [[entities/enigma]].

## Key facts

- Shewanella MR-1 can reduce U(VI). [src: metal_fitness_atlas]
- In DvH, the experiment classification labels 78 experiments (10.3%) as field-stress. These represent FRC contaminants: uranium, mercury, nitrate, nitrite, oxygen and NO. [src: field_vs_lab_fitness]

## Conservation of uranium-response genes

DvH sulfate reduction, lactate/formate/pyruvate utilization, and uranium, mercury and nitrate stress-response genes are described as deeply conserved. [src: field_vs_lab_fitness] The report hypothesizes that metal-specific efflux pumps and metal-binding proteins are accessory traits. It suggests that the uranium and mercury responses instead involve core pathways such as DNA repair and sulfate reduction. [src: field_vs_lab_fitness]

The atlas gives a weaker picture. Uranium (toxic) has 178 important genes, core fraction 0.685, delta +0.035, OR 1.18 and p = 3.4e-01. [src: metal_fitness_atlas] Uranium shows no significant core enrichment, likely because only 2 organisms cover it. [src: metal_fitness_atlas] The 2 organisms are DvH and psRCH2. [src: metal_fitness_atlas] More organisms would show whether uranium fitness genes are truly neutral or the test was underpowered. That question is unresolved. [src: metal_fitness_atlas] See [[concepts/core-genome-enrichment-of-metal-stress-fitness-genes]] and [[concepts/metal-coverage-gaps-and-proposed-validation-experiments]].

## Specificity, counter-ion and cross-resistance

- Metal-specificity: 88/181 uranium-important gene records (48.6%) are metal-specific. [src: metal_specificity]
- NaCl overlap: in DvH, the whole-genome fitness correlation between uranium and NaCl was r=0.350. [src: counter_ion_effects] Uranium was supplied as acetate, with mean NaCl overlap of 37.2% across 2 organisms and mean maximum Cl⁻ of 0 mM. [src: counter_ion_effects] It ranked 8th in NaCl overlap. [src: counter_ion_effects]
- Counter-ion adjustment: for uranium-important genes, the core fraction changed from 0.685 to 0.694 against baseline 0.654. Delta strengthened slightly, from +0.031 to +0.040. [src: counter_ion_effects] See [[concepts/counter-ion-confounding-in-metal-fitness-assays]].
- Cross-resistance: copper-uranium had r = 0.51 (n = 5). The report states that both cause membrane/oxidative damage. [src: metal_cross_resistance]

## Field associations at Oak Ridge

Oak Ridge sites split at the median uranium concentration showed distinct community compositions. [src: lab_field_ecology] After BH-FDR (Benjamini-Hochberg false discovery rate) correction, 5 Fitness Browser genera correlated significantly with uranium. [src: lab_field_ecology] The report calls its hypothesis H2 partially supported, since 5 of 11 tested genera were significant and the pattern is consistent with geochemistry shaping community structure. [src: lab_field_ecology] See [[concepts/geochemical-and-contamination-plume-control-of-subsurface-community-structure]].

| Genus | Spearman rho | p | FDR q | Direction |
|---|---|---|---|---|
| Herbaspirillum | +0.336 | 3.8e-4 | 0.001 | more abundant at high U [src: lab_field_ecology] |
| Bacteroides | +0.264 | 0.006 | 0.013 | more abundant at high U [src: lab_field_ecology] |
| Caulobacter | -0.411 | 1.0e-5 | 1.1e-4 | less abundant at high U [src: lab_field_ecology] |
| Sphingomonas | -0.382 | 4.5e-5 | 2.5e-4 | less abundant at high U [src: lab_field_ecology] |
| Pedobacter | -0.266 | 0.005 | 0.013 | less abundant at high U [src: lab_field_ecology] |

Null results limit these findings:
- Azospirillum was marginal after FDR correction (rho=+0.20, p=0.042, q=0.077). [src: lab_field_ecology]
- Desulfovibrio showed no correlation (rho=0.022, p=0.82) despite being an ENIGMA model organism. [src: lab_field_ecology]
- Pseudomonas showed no correlation (rho=-0.059, p=0.55) despite being an ENIGMA model organism. [src: lab_field_ecology]

## Open Directions

- Add uranium fitness data from organisms such as MR-1 to test whether the nonsignificant core enrichment reflects neutrality or low power.
- Test whether DNA repair and sulfate reduction genes drive the conserved uranium response in DvH.
