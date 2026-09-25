<!-- tension-hash: 1a717775ba242721 -->
# How core is the metal genome? Conflicting core fractions for metal-important genes

Four analyses in this corpus report how often genes required for growth under metal stress belong to the **core genome** (the gene set shared by essentially all genomes of a species pangenome) rather than the accessory genome, and they do not agree. A cross-organism metal atlas reports 87.4% core among broad metal-important genes versus a 76.9% baseline; a single-organism condition-specific analysis reports 71.2% core and no significant enrichment after correction (adjustment of significance thresholds for multiple testing) — a null result; and two specificity analyses report further, mutually different values for similarly named gene classes. This matters because the readings imply different evolutionary stories about whether metal survival is dominated by conserved cellular functions or by specialized resistance genes, and because the values are close enough to invite an illegitimate average. They must not be averaged: definitions, thresholds, organism sets, general-stress capture, exclusion of putatively essential genes, and stress histories differ. [src: metal_fitness_atlas] [src: field_vs_lab_fitness] [src: metal_specificity]

## Evidence Sides

**Broad metal-important genes are core-enriched (atlas).** Genes with any metal fitness defect across the atlas's organism set were 87.4% core versus a 76.9% baseline, and the atlas explicitly attributes much of that signal to general cellular vulnerability rather than specialized resistance. [src: metal_cross_resistance, metal_fitness_atlas]

**Condition-specific heavy-metal genes are not core-enriched (DvH).** In the single-organism *Desulfovibrio vulgaris* Hildenborough (DvH) analysis, heavy-metal-important genes were 71.2% core and were **not** significantly enriched after correction — a null result, which stays null here. [src: field_vs_lab_fitness]

**Specificity tiers put metal-specific genes below general stress genes.** The metal-specificity analysis found 84.8% pooled core for metal-specific genes against 90.2% for general sick genes, and 94.3% core for metal+stress genes. [src: metal_specificity] This **refines** rather than resolves the disagreement, since it applies its own inclusion and classification rules. [src: metal_specificity]

**A fourth estimate for "metal-specific" from three-tier cross-resistance.** The three-tier analysis reported metal-specific genes at 89.8% core, a different value for a similarly named class under different gene classes and organism sets. [src: metal_cross_resistance, metal_fitness_atlas]

## Possible Reconciliations

- *Hypothesis (definitional):* the conflict is a category mismatch — broad "any metal defect" sets capture general stress functions, while condition-specific sets isolate genes important for metals only, so the two measure different populations rather than disagreeing about one. [src: metal_fitness_atlas] [src: field_vs_lab_fitness]
- *Hypothesis (coverage):* the DvH value is a single-organism, single-lineage estimate whose stress history and accessory content differ from a multi-organism pool, so organism coverage, not biology, drives the gap. [src: field_vs_lab_fitness]
- *Hypothesis (threshold and dose):* fitness-effect thresholds and metal doses relative to inhibitory concentration differ across projects, shifting which genes enter each category. [src: metal_specificity]

## Resolving Work

- Apply one shared metal-specific gene definition to all projects' fitness matrices and recompute core fractions per organism, asking whether the direction of enrichment survives a common definition. [src: metal_fitness_atlas; field_vs_lab_fitness; metal_specificity]
- Add non-metal stress controls under identical thresholds to test whether general-stress capture alone explains the atlas-versus-DvH gap. [src: metal_fitness_atlas; field_vs_lab_fitness; metal_specificity]
- Normalize doses relative to each organism's minimum inhibitory concentration before classifying genes, asking whether dose severity, not gene class, drives core fraction. [src: metal_fitness_atlas; field_vs_lab_fitness; metal_specificity]
- Run phylogenetic contrasts across the organism set to test whether the 87.4%-versus-71.2% difference is lineage-confounded. [src: metal_fitness_atlas; field_vs_lab_fitness; metal_specificity]
- Recompute every category with putatively essential genes excluded uniformly, asking how much of the 84.8%/90.2%/94.3% ordering is an essentiality artifact. [src: metal_specificity]

Source tensions: [[concepts/condition-specific-fitness]], [[concepts/gene-essentiality]], [[concepts/metal-cross-resistance]]
