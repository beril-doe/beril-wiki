---
type: "Compound"
description: "A metal whose bedrock concentration positively predicts genus niche breadth, with redox speciation tested as a mediating pathway."
sources: ["summaries/comprehensive_metal_ecology__REPORT.md", "summaries/counter_ion_effects__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/metal_specificity__REPORT.md", "summaries/soil_metal_functional_genomics__REPORT.md"]
aliases: ["Cr"]
---
# Chromium

Chromium (Cr) is a metal whose bedrock concentration positively predicts genus niche breadth in the comprehensive metal ecology report. [src: comprehensive_metal_ecology] That report tested redox speciation as a mediating pathway and found that the signal is not mediated by soil redox. [src: comprehensive_metal_ecology] Fitness evidence for chromium comes from only two organisms, so the genome-side evidence is thin. [src: metal_fitness_atlas]

## Key facts

- Chromium is a DOE priority contaminant. [src: metal_fitness_atlas]
- Chromium fitness coverage is 2 organisms (DvH, psRCH2). [src: metal_fitness_atlas] DvH is [[entities/desulfovibrio-vulgaris-hildenborough]].
- The Oak Ridge FW300 Pseudomonas strains were isolated from chromium-contaminated groundwater but have never been tested against chromate. [src: metal_fitness_atlas] See [[entities/pseudomonas-fluorescens-fw300-n2e3]] and [[concepts/metal-coverage-gaps-and-proposed-validation-experiments]].
- Chromium and lead drive the strongest soil COG-metal association signals. [src: soil_metal_functional_genomics]

## Bedrock chromium and niche breadth

Chromium is the dominant driver of the composite GeoROC niche-breadth signal. [src: comprehensive_metal_ecology] The report links Cr and Co bedrock enrichment to mafic geology. After controlling for metal genes, both positively predict niche breadth. [src: comprehensive_metal_ecology] See [[concepts/environmental-drivers-of-genus-niche-breadth-and-metal-gene-density]].

- Without pH control (model J_Cr, n = 1,220 genera), bedrock Cr has β = +0.0187, p_raw = 1.1×10⁻⁹ and p_BH = 6.7×10⁻⁹. Metal-gene density has β = −0.0203, p = 7.8×10⁻⁸. [src: comprehensive_metal_ecology]
- With pH control (model K_Cr, n = 1,220), bedrock Cr has β = +0.0176, p = 1.0×10⁻⁸. pH has β = +0.0095, p = 3.0×10⁻³. [src: comprehensive_metal_ecology]
- In the joint M model, bedrock Cr has β = +0.0301, p = 9.5×10⁻¹³, described as dominant. [src: comprehensive_metal_ecology]
- The report reads chromium enrichment as indicating mafic/ultramafic bedrock (peridotite, dunite, ophiolite). It calls this consistent with the ecotapestry mafic-score model. [src: comprehensive_metal_ecology]
- The Q4 mechanism table also lists Cr as a driver of the GeoROC composite association (BH p=6.7×10⁻⁹). [src: comprehensive_metal_ecology]
- In the genus-scale GeoROC all-metals collinearity diagnostics, Cr has VIF 1.83. [src: comprehensive_metal_ecology]

## Redox mediation test

The report concludes that the bedrock Cr signal is not mediated by soil redox. [src: comprehensive_metal_ecology] It describes Cr speciation as redox-dominated rather than pH-dominated, and uses this to explain why pH control does not attenuate the signal. [src: comprehensive_metal_ecology]

- Soil moisture is not significantly correlated with bedrock Cr (r = −0.050, p = 0.083). [src: comprehensive_metal_ecology]
- SOM (soil organic matter, 0 cm) is also not significantly correlated with bedrock Cr (r = −0.015, p = 0.597). [src: comprehensive_metal_ecology]
- In model N_Cr (n = 1,219), adding soil moisture leaves Cr at β = +0.0175, p = 1.2×10⁻⁸. Moisture has β = +0.003, p = 0.44 (NS), and pH has β = +0.0117, p = 5.4×10⁻³. [src: comprehensive_metal_ecology]
- In model N_Cr_som (n = 1,218), Cr has β = +0.0187, p = 1.3×10⁻⁹. pH is NS (β = +0.003, p = 0.39). SOM is independently negative (β = −0.0155, p = 6.8×10⁻⁵). [src: comprehensive_metal_ecology]
- The report states that Cr and Co are unattenuated by soil moisture in the N-series models. [src: comprehensive_metal_ecology]
- The report concludes that the soil-moisture test rules out the "Cr(VI) via reducing/waterlogged soils" pathway. [src: comprehensive_metal_ecology]

Direct Cr(VI) data are missing, which limits this test. The CSU speciation table has all-null BCR fraction fields, and WoSIS contains only pH, OC and texture. GEMAS is Europe-only (4,343 pts), and NGSA mobile Cr is Australia-only (1,315 pts). [src: comprehensive_metal_ecology]

The report proposes two possible mechanisms for the redox-independent signal. One is chronic Cr(III)/Ni/Mg stress in serpentine soils. The other is that ultramafic terrain selects niche specialists through several correlated factors, such as Ca/Mg ratio, soil structure and slow weathering. [src: comprehensive_metal_ecology]

## Fitness and conservation results

- In DvH, the whole-genome fitness correlation between chromium and NaCl (sodium chloride) was r=0.318. [src: counter_ion_effects] See [[concepts/shared-metal-and-osmotic-stress-fitness-determinants]].
- In the per-metal NaCl-overlap analysis, chromium (media comp.) had mean overlap 29.2% across 2 organisms, with mean maximum Cl⁻ 0 mM. [src: counter_ion_effects] See [[concepts/counter-ion-confounding-in-metal-fitness-assays]].
- For chromium-important genes, the core fraction changes from 0.710 to 0.723 against baseline 0.654. The delta strengthens from +0.056 to +0.069. [src: counter_ion_effects]
- In the Pan-Bacterial Metal Fitness Atlas, chromium (toxic) has 262 important genes, core fraction 0.710, delta +0.060, OR (odds ratio) 1.33 and p = 4.0e-02. [src: metal_fitness_atlas] See [[concepts/core-genome-enrichment-of-metal-stress-fitness-genes]].
- In the metal-specificity analysis, 132/268 chromium (toxic) metal-important gene records are metal-specific (49.3%). [src: metal_specificity] See [[concepts/metal-specific-versus-pleiotropic-stress-gene-classification]].

## Open Directions

- Test the niche-breadth association against direct Cr(VI) or mobile-Cr data, for example NGSA in Australia and GEMAS in Europe. This would address the lack of global speciation measurements.
- Add Ni, Mg and Ca/Mg ratio to the niche-breadth models. This would separate chronic Cr(III)/Ni/Mg stress from other ultramafic factors.
- Test chromate fitness in the FW300 Pseudomonas strains. This would widen the two-organism fitness coverage.
