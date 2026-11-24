---
type: "Compound"
description: "Metal tested as CuCl2 and CuSO4 across organisms."
sources: ["summaries/comprehensive_metal_ecology__REPORT.md", "summaries/counter_ion_effects__REPORT.md", "summaries/metal_cross_resistance__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/metal_specificity__REPORT.md", "summaries/soil_metal_functional_genomics__REPORT.md"]
aliases: ["Cu"]
---
# Copper

Copper (Cu) is a metal that psRCH2 was tested with as both CuCl₂ (anaerobic, 3 replicates) and CuSO₄ (aerobic, 3 replicates). It is the only organism tested with both salts. [src: counter_ion_effects] The evidence below comes from several separate reports.

## Key facts

- Copper has Fitness Browser metal-experiment coverage in 23 organisms. [src: metal_fitness_atlas]
- In the Pan-Bacterial Metal Fitness Atlas conservation analysis, copper (toxic) has 2,139 important genes, core fraction 0.867, delta +0.090, OR (odds ratio) 1.91 and p-value 3.8e-27. [src: metal_fitness_atlas]
- A second analysis reports a core fraction that changes from 0.882 to 0.876 against baseline 0.792. The delta weakens slightly from +0.090 to +0.084. [src: counter_ion_effects] See [[concepts/core-genome-enrichment-of-metal-stress-fitness-genes]].
- For copper, 1,346/2,594 metal-important gene records are metal-specific (51.9%). [src: metal_specificity]

## Counter-ion effects (CuCl₂ versus CuSO₄)

See [[entities/pseudomonas-stutzeri-rch2]] and [[concepts/counter-ion-confounding-in-metal-fitness-assays]]. In psRCH2, the cross-salt correlation was r=0.439. This is lower than the within-replicate correlations of r=0.720 for CuCl₂ and r=0.859 for CuSO₄. [src: counter_ion_effects] The comparison is severely confounded by aerobic versus anaerobic growth, because hundreds of genes differ between these conditions independent of copper. [src: counter_ion_effects]

Chloride-free CuSO₄ correlated more with NaCl (sodium chloride) than CuCl₂ did. The values were r=0.450 for aerobic CuSO₄ and r=0.212 for anaerobic CuCl₂. [src: counter_ion_effects] The report interprets this as arguing against chloride as the primary confound, and as suggesting shared aerobic stress mechanisms. [src: counter_ion_effects]

For context, the report cites Danilova et al. (2020) as reporting 2.5-fold CuSO₄–CuCl₂ toxicity differences at 0.5 M, a range where osmotic effects dominate. [src: counter_ion_effects]

In the per-metal NaCl-overlap analysis, copper (chloride) had mean overlap 41.0% across 16 organism(s), with mean maximum Cl⁻ 2 mM. [src: counter_ion_effects]

In [[entities/desulfovibrio-vulgaris-hildenborough]], the whole-genome fitness correlation between copper and NaCl was r=0.532. [src: counter_ion_effects] See [[concepts/shared-metal-and-osmotic-stress-fitness-determinants]].

## Cross-resistance with other metals

In the consensus cross-resistance matrix, copper pairs show positive mean Pearson r with high sign consistency:

- Cu-Zn: mean r = 0.48 across 16 organisms, 100% sign consistency. [src: metal_cross_resistance]
- Cu-Fe: mean r = 0.45 across 7 organisms, 100% sign consistency. [src: metal_cross_resistance]
- Co-Cu: mean r = 0.43 across 24 organisms, 96% sign consistency. [src: metal_cross_resistance]
- Cu-Ni: mean r = 0.43 across 24 organisms, 96% sign consistency. [src: metal_cross_resistance]
- Al-Cu: mean r = 0.34 across 17 organisms, 94% sign consistency. [src: metal_cross_resistance]

See universal positivity and chemistry specific magnitude of metal cross resistance.

## Ecology of niche breadth

In the GeoROC J_Cu niche-breadth model without pH control (n = 1,212 genera), metal-gene density has β_metal = −0.0208, p_metal = 6.6×10⁻⁸. Bedrock Cu has β_bedrock = −0.0036, p_raw = 0.235, p_BH = 0.333. [src: comprehensive_metal_ecology] In the bacterial global MGnify MAG (metagenome assembled genomes) niche-breadth analysis, the Cu-specific set (71 KOs, KEGG orthologs) has a significant negative association (β = −0.019, BH-FDR (Benjamini-Hochberg false discovery rate) p = 7.7×10⁻⁵). [src: comprehensive_metal_ecology] See [[concepts/environmental-drivers-of-genus-niche-breadth-and-metal-gene-density]].

## Soil functional genomics

The copper-specific analysis identified 116 COGs (clusters of orthologous groups) at FDR (false discovery rate) < 0.05, using 7,566 samples with nearby KBase genomes at 10 km. [src: soil_metal_functional_genomics] Top positive associations include cell division and nucleotide transport (BQ, FQ, FK, CF). [src: soil_metal_functional_genomics] Top negative associations include energy production (DI, CE), suggesting energetic trade-offs under copper stress. [src: soil_metal_functional_genomics] The report interprets the direction of these associations (energetic trade-offs, membrane transport enrichment) as consistent with known copper toxicity mechanisms in bacteria. [src: soil_metal_functional_genomics]

Caveat: the 10 km matching criterion means many "nearby" genomes may not be co-located with copper measurements. [src: soil_metal_functional_genomics] Sensitivity analysis at 5 km and 20 km is needed before COG-copper associations can be attributed to the measured sites. [src: soil_metal_functional_genomics] That rerun remains pending. [src: soil_metal_functional_genomics] See [[concepts/spatial-matching-of-environmental-samples-to-genomes]].
