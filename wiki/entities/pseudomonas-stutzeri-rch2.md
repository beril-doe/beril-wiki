---
type: "Organism"
description: "A bacterium in the Fitness Browser collection that is the outlier for costly+dispensable genes."
sources: ["summaries/costly_dispensable_genes__REPORT.md", "summaries/counter_ion_effects__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md"]
aliases: ["PS", "psRCH2"]
---
# Pseudomonas stutzeri RCH2

Pseudomonas stutzeri RCH2 (also written PS or psRCH2) is a bacterium in the Fitness Browser collection. It is the outlier for costly+dispensable genes. [src: costly_dispensable_genes, pathway_capability_dependency] The report gives the 21.5% value for this strain and offers its explanations as suggestions, and it cautions that the value may be strain-specific. [src: costly_dispensable_genes]

## Key facts

- The costly_dispensable_genes report designates this organism psRCH2. [src: costly_dispensable_genes]
- It has 21.5% of its genes in the costly+dispensable category. The next organism, B. thetaiotaomicron, has 14.0%. [src: costly_dispensable_genes]
- It is one of 7 Fitness Browser organisms in the Tier 1 pathway analysis, abbreviated PS, which have GapMind pathway data. [src: pathway_capability_dependency]
- In the Pan-Bacterial Metal Fitness Atlas, which uses independent component analysis (ICA), it has 11 responsive modules across 6 metals. [src: metal_fitness_atlas] See [[concepts/metal-responsive-ica-fitness-modules]].

## Costly+dispensable outlier

The report suggests the outlier status reflects a recent mobile-element invasion or genomic expansion specific to this strain. [src: costly_dispensable_genes] It proposes testing recent phage invasion, IS element expansion, or genomic island acquisition. [src: costly_dispensable_genes] It cautions that the extreme value may reflect strain-specific genomic features rather than a general pattern. [src: costly_dispensable_genes] See [[summaries/costly_dispensable_genes__REPORT]] and [[concepts/gene-loss-and-black-queen-hypothesis-tests]].

## Copper salt comparison

psRCH2 is the only organism tested with copper as both CuCl₂ (anaerobic, 3 replicates) and CuSO₄ (aerobic, 3 replicates). [src: counter_ion_effects] See [[entities/copper]] and [[concepts/counter-ion-confounding-in-metal-fitness-assays]].

The cross-salt copper fitness correlation was r=0.439. Within-replicate correlations were r=0.720 for CuCl₂ and r=0.859 for CuSO₄. [src: counter_ion_effects]

This comparison is severely confounded by aerobic versus anaerobic growth. Hundreds of genes differ between these conditions independent of copper. [src: counter_ion_effects]

Chloride-free aerobic CuSO₄ correlated more with NaCl (sodium chloride) (r=0.450) than anaerobic CuCl₂ did (r=0.212). [src: counter_ion_effects] The report reads this as arguing against chloride as the primary confound. It suggests the aerobic/NaCl correlation reflects shared aerobic stress mechanisms. [src: counter_ion_effects] See [[summaries/counter_ion_effects__REPORT]].
