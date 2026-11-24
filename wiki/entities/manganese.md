---
type: "Compound"
description: "Essential metal and USGS critical mineral; covered in one organism (DvH) in the atlas."
sources: ["summaries/comprehensive_metal_ecology__REPORT.md", "summaries/counter_ion_effects__REPORT.md", "summaries/discoveries.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/metal_specificity__REPORT.md"]
aliases: ["Mn"]
---
# Manganese

Manganese (Mn) is an essential metal and a USGS (United States Geological Survey) critical mineral. In the metal fitness atlas it is covered in only one organism, *Desulfovibrio vulgaris* Hildenborough (DvH). [src: metal_fitness_atlas]

## Key facts

- Manganese is a USGS critical mineral. *Shewanella* MR-1 can reduce Mn(IV), so it could test whether metal reducers show different conservation patterns. [src: metal_fitness_atlas]
- In the bacterial global MGnify MAG (metagenome assembled genomes) niche-breadth analysis, the Mn-specific set of 34 KOs (KEGG orthologs) has a significant negative association (β = −0.017, BH-FDR (Benjamini-Hochberg false discovery rate) p = 3.8×10⁻⁴). [src: comprehensive_metal_ecology]

## Conservation of important genes

In the Pan-Bacterial Metal Fitness Atlas, all 30 manganese-important genes are core. This gives a core fraction of 1.000, a delta of +0.198, an OR (odds ratio) of inf and p = 2.0e-03. [src: metal_fitness_atlas] This was the strongest enrichment among the metals. [src: metal_fitness_atlas] See [[concepts/core-genome-enrichment-of-metal-stress-fitness-genes]].

The counter-ion analysis gave a core fraction of 1.000 against a baseline of 0.818. The delta was +0.182, and the correction did not change it. [src: counter_ion_effects] That analysis is low-powered (n=30, 1 organism). The report still treats the 100% core result as robust because of a ceiling effect. [src: counter_ion_effects]

## Metal specificity

With DvH included, 20 of 33 manganese-important gene records are metal-specific (60.6%). [src: metal_specificity] An earlier analysis showed 0% specificity for essential metals. A locusId type mismatch had silently excluded DvH, and fixing it gave 61% for manganese. [src: discoveries] See [[concepts/metal-specific-versus-pleiotropic-stress-gene-classification]].

## Overlap with sodium chloride stress

In DvH, the whole-genome fitness correlation between manganese and NaCl (sodium chloride) was r=0.545. Manganese ranked second among 13 metals, behind zinc (r=0.715). [src: counter_ion_effects] Manganese (chloride) had a mean NaCl-overlap of 57.6% across 1 organism, with a mean maximum Cl⁻ of 200 mM. [src: counter_ion_effects] See [[concepts/counter-ion-confounding-in-metal-fitness-assays]] and [[entities/desulfovibrio-vulgaris-hildenborough]].
