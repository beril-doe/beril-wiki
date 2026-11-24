---
type: "Concept"
description: "Whether genes in co-regulated fitness (ICA) modules are more often core than other genes, and how module conservation is distributed; stops at module-level composition, not mechanisms of selection."
sources: ["summaries/amr_cofitness_networks__REPORT.md", "summaries/conservation_fitness_synthesis__REPORT.md", "summaries/discoveries.md", "summaries/field_vs_lab_fitness__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/module_conservation__REPORT.md"]
---
# Conservation of cofitness modules in the core genome

This page covers whether genes in co-regulated fitness (ICA) modules are more often core than other genes, and how module conservation is distributed. Module genes are modestly but significantly enriched in core genes, and the same figures appear in two reports. [src: conservation_fitness_synthesis, module_conservation] Most modules are mostly core, and a small set of accessory modules exists. [src: module_conservation] The page stops at module composition and does not address selection mechanisms. See also [[concepts/conservation-of-cofitness-modules-across-genomes-and-organisms]] and [[entities/independent-component-analysis-fitness-modules]].

## Core enrichment of module genes

Genes assigned to independent component analysis (ICA) modules are described as co-regulated functional units that skew toward the conserved core genome. [src: module_conservation] ICA fitness modules are enriched in core genes. Two reports give the same figures: 86% core versus a 81.5% baseline, odds ratio (OR) 1.46, p=1.6e-87. [src: conservation_fitness_synthesis, module_conservation] The module_conservation analysis also states the percentages as 86.0% versus 81.5%, a difference of +4.5 percentage points. [src: module_conservation] The discoveries digest adds that this covers 29 organisms, and that a per-organism paired Wilcoxon test gave p=1.0e-03, with 22 of 29 organisms showing enrichment. [src: discoveries] The reports read this as co-regulated units residing preferentially in the conserved genome. [src: discoveries, module_conservation] The synthesis concludes that the core genome contains coordinated functional units, not only individual essential genes. [src: conservation_fitness_synthesis]

The effect is modest in absolute terms. The baseline core rate is already about 81.5%, which limits the maximum enrichment that can be observed. [src: module_conservation]

## Distribution across modules

Most modules are mostly core. Of 974 modules with at least 3 mapped genes [src: module_conservation], 577 (59%) are core modules with >90% core genes. [src: module_conservation] Another 349 (36%) are mixed, with 50-90% core. [src: module_conservation] The remaining 48 (5%) are accessory, with <50% core. [src: module_conservation] The 59% figure recurs in the other reports. [src: conservation_fitness_synthesis, discoveries] The median module is 93.4% core. [src: module_conservation] The report reads the 59% result as extending "core" from individual genes to functionally coherent regulatory units. [src: module_conservation]

The 90% and 50% cutoffs are arbitrary conveniences, not biologically motivated. [src: module_conservation] Module membership itself uses |Pearson r| >= 0.3 with at most 50 genes per module. [src: module_conservation] That threshold affects which genes are in a module and could influence conservation composition. [src: module_conservation]

### Cross-organism module families

Module families spanning more organisms do not have higher core fractions (Spearman rho=-0.01, p=0.914). [src: discoveries] The report treats this as a ceiling effect from the ~82% baseline, not as evidence against a conservation-function relationship. [src: discoveries] Separately, 38 module families have <50% core genes. They are described as co-regulated accessory modules conserved across organisms. [src: module_conservation] In the AMR (antimicrobial resistance) analysis, 99% (208/209) of AMR gene-module assignments fall in cross-organism conserved module families, which the report reads as ancient regulatory relationships. [src: amr_cofitness_networks]

## Results in single-organism and metal-focused sets

In Desulfovibrio vulgaris (DvH), 52 ICA fitness modules have a mean core fraction of 0.886 and a median of 1.000. [src: field_vs_lab_fitness] DvH conservation shows no significant correlation with field condition activity (Spearman rho=0.071, p=0.62), and that report counts its H2 hypothesis as unsupported. [src: field_vs_lab_fitness] The classification of DvH modules is below.

| DvH module class | Modules | Mean core fraction |
|---|---|---|
| Ecological (field-active + conserved) | 21 | 0.980 [src: field_vs_lab_fitness] |
| Conserved-quiet (low field activity + conserved) | 17 | 0.983 [src: field_vs_lab_fitness] |
| Field-variable (field-active + less conserved) | 5 | 0.829 [src: field_vs_lab_fitness] |
| Lab (low field + less conserved) | 9 | 0.516 [src: field_vs_lab_fitness] |

The lab modules contain accessory-genome genes. [src: field_vs_lab_fitness] The report suggests accessory-genome modules exist and tend to respond to lab-type conditions. [src: field_vs_lab_fitness]

Metal-responsive modules in the Pan-Bacterial Metal Fitness Atlas show the same pattern. The 183 modules with conservation data have a mean core fraction of 0.826 [src: metal_fitness_atlas] and a median of 0.929. [src: metal_fitness_atlas] See [[concepts/metal-responsive-ica-fitness-modules]].

## Caveats

The analysis covers 29 of 32 organisms. Cola, Kang and SB2B lack pangenome links because their species had too few genomes in GTDB for pangenome construction. [src: module_conservation] What co-regulated functions live only in the flexible genome, in the 48 accessory modules, remains an open question. [src: conservation_fitness_synthesis]

## Open Directions

- Annotate the 48 accessory modules and the 38 accessory module families by function. This would show what co-regulated functions live only in the flexible genome.
- Repeat the enrichment test against a baseline that excludes the ceiling effect, for example within accessory-rich organisms. This would test whether the lack of a breadth gradient is purely a ceiling effect.
- Vary the ICA membership threshold (|r| and the 50-gene cap) and the 90%/50% class cutoffs. This would show how robust the core, mixed and accessory proportions are.
- Test DvH-style lab versus conserved module classes in other organisms. This would check whether accessory modules tend to respond to lab-type conditions beyond one organism.
