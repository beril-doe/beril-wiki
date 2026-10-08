<!-- tension-hash: a172813cc5214cca -->
# Are Metal-Important Genes Core or Accessory?

The corpus disagrees about where genes that matter for heavy-metal fitness sit in the pangenome. The pangenome is a species' full gene set, split into core genes (shared by nearly all strains) and accessory genes (variable). [src: counter_ion_effects, field_vs_lab_fitness] A single-organism analysis of *Desulfovibrio vulgaris* Hildenborough (DvH) found heavy-metal-important genes less core than field-stress genes. [src: field_vs_lab_fitness] The Metal Fitness Atlas, cited in counter_ion_effects, found metal-important genes enriched in the core. [src: counter_ion_effects] This matters for [[concepts/laboratory-fitness-versus-natural-selection]] because it tests whether conditions treated as ecologically relevant behave alike when compared against conservation. [src: field_vs_lab_fitness]

## Evidence Sides

**Side A: DvH heavy-metal-important genes are less core than field-stress genes**

In DvH, field-stress genes were more core than heavy-metal-important genes, although both categories were treated as ecologically relevant. [src: field_vs_lab_fitness] The report gives a DvH heavy-metal core figure of 71.2%. [src: counter_ion_effects, field_vs_lab_fitness] It hypothesizes that specific metal-resistance mechanisms may be accessory, while uranium- and mercury-related responses may involve fundamental stress pathways. This is a hypothesis, not a direct mobile-element or natural-selection measurement. [src: field_vs_lab_fitness]

This side is internally inconsistent. The report's prose says heavy-metals was lowest at every fitness threshold. Its own table contradicts that at the -1.0 threshold, where lab-antibiotic was 76.2% and heavy-metals was 76.7%. [src: field_vs_lab_fitness]

**Side B: Atlas metal-important genes lean core**

The Metal Fitness Atlas finding, cited in counter_ion_effects, is that metal-important genes were 87.4% core, with OR=2.08. An odds ratio (OR) compares the odds of being core between two gene groups. [src: counter_ion_effects]

Counter_ion_effects raised a pre-correction concern that a shared-stress component might inflate this figure, because osmotic stress genes are core cellular machinery. [src: counter_ion_effects] After correction for that component, the core enrichment persisted and increased for 7 of 14 metals: molybdenum (Mo), tungsten (W), mercury (Hg), selenium (Se), nickel (Ni), chromium (Cr) and uranium (U). The report judged the atlas conclusions robust. [src: counter_ion_effects]

## Possible Reconciliations

- **Hypothesis 1 (scope):** The two analyses differ in organism scope and in how they define their categories. The single-organism DvH pattern may therefore not generalize to the atlas's organism set. The figures are not reconciled here. [src: counter_ion_effects, field_vs_lab_fitness]
- **Hypothesis 2 (metal composition):** The DvH heavy-metal class and the atlas metal set may weight different metals. The atlas metals whose enrichment increased (Mo, W, Hg, Se, Ni, Cr, U) [src: counter_ion_effects] may differ in conservation from the metals that dominate the DvH class.
- **Hypothesis 3 (threshold sensitivity):** The DvH contrast may depend on the fitness threshold chosen. The ordering of heavy-metals relative to lab-antibiotic changes at -1.0 [src: field_vs_lab_fitness], so a single-threshold comparison may overstate the gap.

## Resolving Work

- Restrict the atlas core-fraction analysis to DvH alone, using the threshold and core definition of field_vs_lab_fitness, to test whether the disagreement is an organism-scope effect.
- Apply the counter_ion_effects shared-stress correction to the DvH heavy-metal gene set, to test whether removing shared-stress genes shifts its core fraction as it did for the atlas.
- Compute per-metal DvH core fractions at each threshold and compare them with the atlas results for Mo, W, Hg, Se, Ni, Cr and U, asking whether specific metals rather than the class drive the contrast.
- Annotate DvH heavy-metal-important accessory genes for mobile-element context (plasmids, transposases, genomic islands), a measurement the DvH report did not make.
- Correct the DvH report so its prose matches its threshold table, then re-state the heavy-metal ranking with a statistical test at each threshold.
