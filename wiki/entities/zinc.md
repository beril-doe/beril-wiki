---
type: "Compound"
description: "Metal with highest NaCl fitness correlation in DvH."
sources: ["summaries/comprehensive_metal_ecology__REPORT.md", "summaries/counter_ion_effects__REPORT.md", "summaries/metal_cross_resistance__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/metal_specificity__REPORT.md"]
aliases: ["Zn"]
---
# Zinc

Zinc (Zn) had the highest NaCl fitness correlation of the metals tested in Desulfovibrio vulgaris Hildenborough (DvH). [src: counter_ion_effects] The page also reports zinc's cross-resistance with other metals, its core-genome enrichment and metal specificity, and its niche-breadth associations. The fitness results are measured correlations. The niche-breadth results are model associations. See [[entities/desulfovibrio-vulgaris-hildenborough]] and [[entities/zinc-sulfate]].

## Key facts

- In DvH, profiled with 13 metals and 6 NaCl experiments, the whole-genome fitness correlation between zinc and NaCl was r=0.715. This was the top of a ranking that put manganese at 0.545 and iron at 0.086. [src: counter_ion_effects]
- Zinc has Fitness Browser metal-experiment coverage in 17 organisms. [src: metal_fitness_atlas] See [[entities/fitness-browser]].

## Zinc and NaCl: not a chloride artefact

Zinc is supplied as sulfate with zero chloride, so chloride cannot explain its overlap with NaCl stress. [src: counter_ion_effects] Zinc sulfate had 44.6% mean NaCl overlap across 12 organisms. [src: counter_ion_effects] It ranked 4th, above 10 of 14 metals. [src: counter_ion_effects] That exceeded cobalt at 41.3% (up to 500 mM Cl⁻), copper at 41.0% and nickel at 39.3%. [src: counter_ion_effects] The report reads this, together with the DvH correlation, as support for rejecting chloride confounding. [src: counter_ion_effects] See [[concepts/counter-ion-confounding-in-metal-fitness-assays]] and [[concepts/shared-metal-and-osmotic-stress-fitness-determinants]].

## Core-genome enrichment

Zinc-important genes are enriched in the core genome. In the Pan-Bacterial Metal Fitness Atlas, zinc (toxic) has 1,517 important genes, core fraction 0.890, delta +0.151, OR (odds ratio) 2.94 and p-value 2.0e-49. [src: metal_fitness_atlas] Zinc's delta is the second strongest in the atlas, after manganese at +0.198. [src: metal_fitness_atlas] After correction for shared stress, the core fraction changed from 0.895 to 0.865 against a baseline of 0.750, and the delta fell from +0.145 to +0.115. [src: counter_ion_effects] The report calls this a modest decrease. [src: counter_ion_effects] See [[concepts/core-genome-enrichment-of-metal-stress-fitness-genes]] and [[entities/metal-fitness-atlas]].

## Metal specificity

For zinc, categorized as toxic, 843/1,786 metal-important gene records (47.2%) were metal-specific. [src: metal_specificity] See [[concepts/metal-specific-versus-pleiotropic-stress-gene-classification]].

## Cross-resistance with other metals

Zinc showed positive cross-resistance with every metal listed, with 100% sign consistency in each pair. [src: metal_cross_resistance] Mean Pearson r values from the consensus matrix are below.

- Fe-Zn: 0.61 across 6 organisms [src: metal_cross_resistance]
- Co-Zn: 0.52 across 18 organisms [src: metal_cross_resistance]
- Ni-Zn: 0.51 across 18 organisms [src: metal_cross_resistance]
- Cu-Zn: 0.48 across 16 organisms [src: metal_cross_resistance]
- Al-Zn: 0.44 across 13 organisms [src: metal_cross_resistance]

The report calls Fe-Zn unexpectedly strong. It suggests this likely reflects shared disruption of iron-sulfur cluster proteins, which is an interpretation and not a measured result. [src: metal_cross_resistance] See [[concepts/universal-positivity-and-chemistry-specific-magnitude-of-metal-cross-resistance]], [[entities/iron]], [[entities/cobalt]], [[entities/nickel]], [[entities/copper]] and [[entities/aluminum]].

## Niche breadth in environmental data

Metal-gene density is negatively associated with genus niche breadth for zinc. In the GeoROC J_Zn model without pH control (n = 1,213 genera), β_metal = −0.0210 with p_metal = 4.5×10⁻⁸. Bedrock Zn was not significant, with β_bedrock = −0.0034, p_raw = 0.278 and p_BH = 0.333. [src: comprehensive_metal_ecology] In the bacterial global MGnify MAG (metagenome assembled genomes) analysis, the Zn-specific set of 67 KOs (KEGG orthologs) had β = −0.023 with BH-FDR (Benjamini-Hochberg false discovery rate) p = 1.1×10⁻⁶. [src: comprehensive_metal_ecology] See [[concepts/environmental-drivers-of-genus-niche-breadth-and-metal-gene-density]].
