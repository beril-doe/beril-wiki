---
type: "Concept"
description: "Tests of whether anaerobiosis, metabolic breadth or H2S production relate to metal tolerance; stops at BacDive-derived associations."
sources: ["summaries/bacdive_phenotype_metal_tolerance__REPORT.md"]
---
# Metabolic versatility, oxygen tolerance and metal tolerance

In BacDive-derived data, oxygen tolerance and metabolite breadth show no meaningful association with metal tolerance, and the H₂S result is unreliable. Enzyme breadth is the one breadth measure with a statistically significant but small association. [src: bacdive_phenotype_metal_tolerance] All evidence comes from a single report ([[summaries/bacdive_phenotype_metal_tolerance__REPORT]]), and the page stops at BacDive-derived associations.

## Literature Context

The candidate papers are mostly case studies of individual organisms. None of them tests the BacDive-wide association between oxygen tolerance, metabolic breadth and metal tolerance that the hub reports. They give mechanistic and ecological context, and they point in different directions.

Several papers describe metabolic versatility alongside metal handling in single organisms. The genome of the Gram-positive anaerobe Desulfitobacterium hafniense DCB-2 contains genes for metal reduction, dehalogenation, N2 and CO2 fixation and oxygen tolerance, which the authors read as versatility in adaptive and reductive capacities [PMID 22316246](https://pubmed.ncbi.nlm.nih.gov/22316246/). Rhodococcus aetherivorans BCP1 is described as metabolically versatile and tolerant of arsenic oxyanions. Arsenate at 30 mM boosted its growth, and the transcriptomic response included rearranged central and energetic metabolism [PMID 35311511](https://pubmed.ncbi.nlm.nih.gov/35311511/). In antimony-contaminated groundwater, antimony-oxidizing bacteria carried sulfur-oxidation, CO2-fixation and N2-fixation genes together with oxidative stress tolerance genes. The authors link these to versatile energy acquisition and survival under oxygen fluctuations [PMID 40425065](https://pubmed.ncbi.nlm.nih.gov/40425065/). These are single-habitat or single-strain observations. They show that versatility and metal tolerance can co-occur, but they do not test an association across species.

On oxygen, the literature suggests the anaerobe/aerobe boundary is not sharp for metal-related physiology. Microbacterium deferre A1-JKT reduces Fe(III) while also reducing oxygen, which challenges the view that Fe(III) reduction is restricted to anaerobic conditions [PMID 40615380](https://pubmed.ncbi.nlm.nih.gov/40615380/). Analysis of Saanich Inlet identified putative mercury-methylating groups, including Marinimicrobia. Terminal oxidases from aerobic respiratory chains were associated with several of these putative novel methylators, and the authors suggest a greater oxygen tolerance than previously recognized [PMID 33504941](https://pubmed.ncbi.nlm.nih.gov/33504941/). The methylation role there is inferred from hgc gene expression and homology modelling, not shown directly. Anaerobic metal stress is also real. ClpXP protease is required for anaerobic Fe2+ resistance in Shewanella oneidensis, and E. coli lacking clpX or clpP shows increased anaerobic Fe2+ sensitivity [PMID 29378887](https://pubmed.ncbi.nlm.nih.gov/29378887/).

The corpus finding that anaerobes and aerobes do not differ in metal tolerance (d = -0.016, p = 0.55, among 3,751 species) is consistent with this blurred boundary. Oxygen status may simply not predict tolerance. This is an interpretation, since none of these papers measured that comparison. The corpus's small negative enzyme-breadth association (rho = -0.058) and its null metabolite-breadth result (rho = -0.013) have no direct counterpart in the candidates. The case studies imply that versatility can support metal handling in particular organisms, so the corpus is not contradicted. The corpus also does not confirm that idea at the level of species-wide data.

The H₂S result stays unresolved. The only H₂S paper among the candidates is a tomato seedling study, in which endogenous H2S mediated nitric oxide-induced Cr(VI) tolerance [PMID 32738579](https://pubmed.ncbi.nlm.nih.gov/32738579/). It is a plant study and does not bear on bacterial H₂S producers. The corpus's underpowered estimate (8 H₂S-negative species) is therefore neither supported nor refuted by these papers, and the proposed sulfate-reducing bacteria challenge would be new work.

## Oxygen tolerance

Anaerobes and aerobes do not differ in metal tolerance. Among 3,751 BacDive species with oxygen tolerance data, the anaerobe–aerobe difference is negligible (d = -0.016, p = 0.55). [src: bacdive_phenotype_metal_tolerance] The report therefore finds H1b, which predicted better redox-metal tolerance in anaerobes, not supported (d = -0.02, ns). [src: bacdive_phenotype_metal_tolerance]

Facultative anaerobes have the highest mean score (0.221), versus aerobes (0.216) and anaerobes (0.215). [src: bacdive_phenotype_metal_tolerance] A Kruskal-Wallis test across the three groups is marginally significant (H = 8.53, p = 0.014), but the report calls the effect biologically trivial. [src: bacdive_phenotype_metal_tolerance]

In direct Fitness Browser–BacDive validation, the single anaerobe (*Methanococcus*) had only 1 metal tested versus 4–5 for aerobes. The report considers n = 1 not interpretable. [src: bacdive_phenotype_metal_tolerance] See [[entities/methanococcus-maripaludis]] for that organism.

## Metabolic breadth

The measures of metabolic breadth give mixed results. Metabolite breadth and acetate utilization show no significant association, while enzyme breadth shows a small significant one. [src: bacdive_phenotype_metal_tolerance] The hypothesis that metabolically versatile organisms harbor more resistance genes was not supported. [src: bacdive_phenotype_metal_tolerance] H1c, which predicted higher scores with broader metabolism, was not supported (rho = -0.01, ns). [src: bacdive_phenotype_metal_tolerance]

- Metabolite breadth: rho = -0.013, n = 3,930, p = 4.2e-01, false discovery rate (FDR) q = 4.7e-01, not significant. [src: bacdive_phenotype_metal_tolerance]
- Acetate utilization: d = +0.005, n = 422, p = 7.9e-01, FDR q = 7.9e-01, not significant. [src: bacdive_phenotype_metal_tolerance]
- Enzyme breadth: rho = -0.058, n = 3,746, p = 4.1e-04, FDR q = 8.2e-04, significant. The sign is negative, so it does not support higher tolerance with broader enzyme repertoires. [src: bacdive_phenotype_metal_tolerance]

The report tentatively attributes the lack of correlation for metabolite breadth to metabolic versatility operating in different genomic neighborhoods from metal resistance. [src: bacdive_phenotype_metal_tolerance]

## H₂S production

The H₂S result is inconclusive. H₂S production was not significant in the univariate analysis (d = -0.867, n = 880, p = 5.8e-02, FDR q = 7.3e-02). [src: bacdive_phenotype_metal_tolerance] Only 8 H₂S-negative species occur in the matched set, so the large effect size (d = -0.87) is unreliable. [src: bacdive_phenotype_metal_tolerance] The report likewise calls H1f, which predicted that H₂S producers tolerate Zn, Cu and Cd, unreliable, because small-sample bias likely inflates the effect. [src: bacdive_phenotype_metal_tolerance] It describes the hypothesis as underpowered. [src: bacdive_phenotype_metal_tolerance] The report proposes testing it experimentally with sulfate-reducing bacteria and zinc/copper challenge. [src: bacdive_phenotype_metal_tolerance]

## Open Directions

- Run the proposed sulfate-reducing bacteria zinc/copper challenge, to replace the 8-negative BacDive estimate with direct measurements.
- Repeat the oxygen-tolerance comparison with more anaerobes in Fitness Browser–BacDive validation, to address the n = 1 limit.
- Re-test enzyme breadth while controlling for relatedness, as discussed in [[concepts/phylogenetic-confounding-of-phenotype-metal-tolerance-associations]], to see whether its small association survives.
