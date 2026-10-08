<!-- tension-hash: ae3d6d637a58653d -->
# Are metal-specific genes core or accessory? Conflicting core fractions and gene-set definitions

Projects report different core fractions for metal genes described as specific to metals, and they disagree about what the earlier gene set contained. [src: metal_fitness_atlas, field_vs_lab_fitness, metal_specificity] "Core" genes are those present across most genomes of a species' pangenome, its full gene repertoire. The earlier value comes from a single organism that field_vs_lab_fitness analysed on its own; the sources name it only by the abbreviation DvH and do not expand it. [src: field_vs_lab_fitness] The metal atlas and field_vs_lab_fitness describe that gene set differently. [src: metal_fitness_atlas, field_vs_lab_fitness] A multi-organism analysis that explicitly separates metal-specific genes reports a higher core fraction. [src: metal_specificity] Whether metal-specific function sits in the core or accessory genome shapes how [[concepts/pangenome-conservation-fitness-decoupling]] reads metal fitness evidence, and whether the earlier result can serve as a baseline expectation.

## Evidence Sides

**Side A: the atlas's account of the prior DvH result**
The atlas describes the prior result for DvH, a single organism, as 71.2% core and says it concerns condition-specific heavy-metal genes. [src: metal_fitness_atlas]

**Side B: the originating project's own definition**
The field_vs_lab_fitness report defines the heavy-metal class as 198 genes with fitness < -2 under heavy-metal conditions. A fitness score is the measured growth effect of disrupting a gene, so more negative values mean a stronger defect. The report states no exclusion of genes that are also important under other stresses. [src: field_vs_lab_fitness] Its below-baseline trend for this class was not significant (FDR q=0.14). FDR is the false discovery rate, and q is the multiple-testing-adjusted significance value. [src: field_vs_lab_fitness] On this reading, it is unclear whether the set was restricted to condition-specific genes, and its deviation from baseline is a null result rather than an established depletion.

**Side C: an explicit metal-specific gene set across organisms**
The metal_specificity project explicitly separates metal-specific genes. It found them 84.8% core, pooled across 22 organisms. [src: metal_specificity]

The DvH figure comes from a single organism, and the analyses define their metal gene sets differently. The wiki does not prefer either value, and it does not prefer the atlas's characterization of the DvH gene set over the originating report's definition. [src: metal_fitness_atlas, field_vs_lab_fitness, metal_specificity]

## Possible Reconciliations

- **Hypothesis: definitional mismatch.** The two values may describe different gene sets: a fitness-threshold set with no stated exclusion of genes important under other stresses [src: field_vs_lab_fitness], and an explicitly metal-specific set [src: metal_specificity]. If so, they are not directly comparable.
- **Hypothesis: organism effect.** The DvH value comes from a single-organism analysis and may not reflect a general pattern, so a figure pooled across 22 organisms [src: metal_specificity] need not contradict it.
- **Hypothesis: mischaracterization.** The atlas's "condition-specific" label may not match the set field_vs_lab_fitness defined; the explanation built on that label would then need revisiting.
- **Hypothesis: no real depletion in DvH.** The DvH below-baseline trend was not significant [src: field_vs_lab_fitness], so the apparent contrast may partly reflect noise in a single-organism estimate.

## Resolving Work

- Re-derive the DvH heavy-metal set from the source fitness data and apply metal_specificity's metal-specific filter, testing whether identically defined DvH metal-specific genes fall closer to Side A or Side C.
- Recompute the core fraction of the original fitness < -2 DvH set after excluding genes important under other stresses, testing whether the atlas's "condition-specific" description matches the data.
- If DvH is among the 22 organisms, extract its organism-level value from metal_specificity to see whether the same pipeline reproduces the single-organism result.
- Run a threshold sensitivity analysis across fitness cutoffs for metal-specific sets in all organisms, with FDR correction, asking whether the core-versus-accessory conclusion depends on the cutoff.
- Fit a mixed model (a regression with per-organism random effects, i.e. organism-level intercepts drawn from a shared distribution) of metal-specific core enrichment, separating organism heterogeneity from definitional differences.
