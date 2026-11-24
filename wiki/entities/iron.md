---
type: "Compound"
description: "Essential metal with the lowest metal-specificity among metals tested."
sources: ["summaries/comprehensive_metal_ecology__REPORT.md", "summaries/counter_ion_effects__REPORT.md", "summaries/metal_cross_resistance__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/metal_specificity__REPORT.md"]
aliases: ["Fe"]
---
# Iron

Iron (Fe) has the lowest metal-specificity of the metals tested, at 21.9%. [src: metal_specificity] Its fitness genes are mostly core genes. [src: metal_fitness_atlas]

## Key facts

- Iron has the lowest metal-specificity, 21.9%. The report suggests this likely reflects its central role in core metabolism. [src: metal_specificity]
- For iron, categorized as essential, 144/659 metal-important gene records are metal-specific (21.9%). [src: metal_specificity]
- Iron and essential-metal limitation give the highest fractions of important genes in the atlas: 12.3% for Fe and 11.2% for Mo/W. [src: metal_fitness_atlas]
- Fitness Browser metal experiments cover iron in 3 organisms. Cobalt covers 27, nickel 26, copper 23, aluminum 22 and zinc 17. [src: metal_fitness_atlas]

## Conservation of iron fitness genes

Iron fitness genes are enriched in the core genome. In the Pan-Bacterial Metal Fitness Atlas, iron has 651 important genes, a core fraction of 0.919, a delta of +0.116, an odds ratio (OR) of 3.07 and p = 8.5e-18. [src: metal_fitness_atlas] The atlas ranks iron's delta (+0.116) among its strongest enrichments. [src: metal_fitness_atlas]

In the counter-ion analysis, the core fraction of iron-important genes changes from 0.778 to 1.000 against a baseline of 0.818, and the delta reverses from -0.040 to +0.182. This rests on n=9 genes from 1 organism. [src: counter_ion_effects] The report warns that the corrected deltas for cadmium (n=92) and iron (n=9), each from a single organism, are statistically unreliable. [src: counter_ion_effects]

## Cross-resistance with other metals

Every iron pair below has 100% sign consistency in the consensus cross-resistance matrix. Fe-Zn has mean Pearson r = 0.61 across 6 organisms. [src: metal_cross_resistance] Cu-Fe has r = 0.45 across 7 organisms. [src: metal_cross_resistance] Co-Fe has r = 0.45 across 7 organisms. [src: metal_cross_resistance] Al-Fe has r = 0.38 across 5 organisms. [src: metal_cross_resistance] Fe-Ni has r = 0.38 across 7 organisms. [src: metal_cross_resistance]

The report calls Fe-Zn unexpectedly strong. It suggests this likely reflects shared disruption of iron-sulfur cluster proteins. [src: metal_cross_resistance]

## Relation to salt stress

In Desulfovibrio vulgaris Hildenborough (DvH), the whole-genome fitness correlation between iron and NaCl was r=0.086. [src: counter_ion_effects] The report attributes this to iron limitation affecting specific Fe-dependent enzymes rather than general cellular damage. [src: counter_ion_effects] In the per-metal NaCl-overlap analysis, iron (media comp.) had mean overlap of 33.3% across 1 organism, with mean maximum Cl⁻ of 0 mM. [src: counter_ion_effects]

## Niche breadth

In the bacterial global MGnify MAG (metagenome assembled genomes) niche-breadth analysis, the Fe-specific set of 98 KOs (KEGG orthologs) has a significant negative association (β = −0.025, BH-FDR p = 1.2×10⁻⁷). BH-FDR is the Benjamini-Hochberg false discovery rate. [src: comprehensive_metal_ecology]

## Related pages

See zinc, [[concepts/metal-specific-versus-pleiotropic-stress-gene-classification]] and [[concepts/core-genome-enrichment-of-metal-stress-fitness-genes]].
