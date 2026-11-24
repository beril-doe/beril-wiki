---
type: "Concept"
description: "ICA fitness modules that respond to metal experiments, how responsiveness and metal-specificity are thresholded and affected by normalization, and how conserved their genes are."
sources: ["summaries/metal_cross_resistance__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/metal_specificity__REPORT.md", "summaries/pitfalls.md"]
---
# Metal-responsive ICA fitness modules

This page covers ICA (independent component analysis) fitness modules that respond to metal experiments, how thresholds and normalization shape what is detected, and how conserved the module genes are. The Pan-Bacterial Metal Fitness Atlas identified 600 responsive module records at a z-score threshold. [src: metal_fitness_atlas] A later specificity analysis found 0 metal-specific modules, and its report lists normalization limitations that may bear on that result. [src: metal_specificity] See [[entities/independent-component-analysis-fitness-modules]] for the method.

## Literature Context

The candidate papers give only indirect context for metal-responsive ICA (independent component analysis) fitness modules. None of them applies ICA to metal fitness data. The closest work is a barcoded transposon mutant study of Pseudomonas stutzeri RCH2 under denitrifying conditions. It combined mutant fitness data with regulon predictions to map Cu(2+) and Zn(2+) resistance, and it expanded what is known about the CzcCBA, CzcD and CusCBA exporters and their accessory proteins CzcI and CusF [PMID 27474723](https://pubmed.ncbi.nlm.nih.gov/27474723/). It also identified genes with no known link to zinc resistance (corB, corC, Psest_3226, Psest_3322 and Psest_0618) and genes with no known link to copper resistance (an Mrp antiporter subunit gene, Psest_2850 and Psest_0584). Deletion mutants confirmed the Zn-dependent phenotypes for corB, corC, Psest_3226 and Psest_3322 [PMID 27474723](https://pubmed.ncbi.nlm.nih.gov/27474723/). The same study reported a null result under Cu(2+) exposure. Mutants in some predicted Cu(2+) resistance systems did not show decreased fitness relative to the wild type [PMID 27474723](https://pubmed.ncbi.nlm.nih.gov/27474723/). That observation concerns only the conditions tested. It does not show that those genes lack phenotypes in general.

Two other papers touch on core versus accessory content. In Acinetobacter baumannii, a transposon sequencing study of pneumonia and septicaemia infections found that 89% of genes with aberrant in vivo fitness were part of the core genome. It also highlighted metal acquisition as important during septicaemia [PMID 41217819](https://pubmed.ncbi.nlm.nih.gov/41217819/). This is a host-infection setting, not a metal-stress screen. In a Klebsiella pneumoniae ST1412 strain, curing an IncFIB(K) plasmid that encodes heavy-metal resistance was accompanied by enhanced copper tolerance [PMID 34068663](https://pubmed.ncbi.nlm.nih.gov/34068663/). That is the opposite direction from what one might expect. It is a single-strain observation, and it does not show that accessory genes drive metal tolerance. In K. pneumoniae biofilms, sublethal carbapenem treatment downregulated genes coding for metal transporters, which was measured by RNA-Seq [PMID 25583711](https://pubmed.ncbi.nlm.nih.gov/25583711/). This shows that metal-related genes can respond to non-metal stress.

The corpus's conservation finding is consistent with the A. baumannii result. The atlas reported a mean core fraction of 0.826 and a median of 0.929 across 183 metal-responsive modules, and these figures agree in direction with the 89% core share in [PMID 41217819](https://pubmed.ncbi.nlm.nih.gov/41217819/). The two measure different things, however: modules versus individually perturbed genes, and metals versus infection. The P. stutzeri work is also consistent with the atlas finding that psRCH2 has 11 responsive modules across 6 metals. Its novel Zn and Cu determinants are the kind of genes that module-level analysis could group together. This is a hypothesis, because the candidate papers do not test it [PMID 27474723](https://pubmed.ncbi.nlm.nih.gov/27474723/).

The corpus's central points have no counterpart in these papers. These are the 600 responsive records (3.1%) at |z| > 2.0, the 0 metal-specific modules, and the normalization limitations the specificity report lists. One of those limitations is that per-module z-normalization gives max |z| < 2.0 for most metal experiments. That limitation may affect how the zero result should be read. The corpus's treatment of module thresholds and normalization is therefore novel relative to the candidate literature. The K. pneumoniae plasmid result is not in tension with the core-dominated picture, but it leaves open whether accessory elements matter for metal tolerance.

## Responsiveness in the atlas

Atlas notebook NB05 analyzed 19,453 module × metal-experiment records across 31 organisms, using module profiles standardized per module across all experiments. [src: metal_fitness_atlas] With a responsiveness threshold of |z| > 2.0, 600 records (3.1%) qualify. [src: metal_fitness_atlas] The atlas data file data/metal_module_conservation.csv has 183 rows of metal-responsive module conservation statistics. [src: metal_fitness_atlas]

[[entities/desulfovibrio-vulgaris-hildenborough|DvH]] leads, with 47 responsive modules spanning 12 metals. [src: metal_fitness_atlas] [[entities/pseudomonas-stutzeri-rch2|psRCH2]] has 11 responsive modules across 6 metals. [src: metal_fitness_atlas]

## Conservation of the module genes

Metal-responsive modules are mostly made of core genes. The 183 modules with conservation data have a mean core fraction of 0.826, consistent with core enrichment of metal-fitness genes overall. [src: metal_fitness_atlas] The median is higher, at 0.929, so most of these modules are predominantly core genes. [src: metal_fitness_atlas] This relates to [[concepts/conservation-of-cofitness-modules-in-the-core-genome]] and [[concepts/conserved-multi-metal-tolerance-gene-families]].

## Normalization and what is detectable

The reports describe several normalization limits on module analyses.

- The atlas's first attempt with raw scores from module_conditions.csv produced 0 responsive modules. Raw scores (max 0.96) are on a different scale from z-scores. Using per-experiment profiles with z-normalization resolved this. [src: metal_fitness_atlas]
- The metal_specificity report found 0 metal-specific modules in its module-level analysis using z-scored activity profiles. [src: metal_specificity]
- That report notes that per-module z-normalization gives max |z| < 2.0 for most metal experiments, because metal experiments are a small fraction of each organism's experiments. [src: metal_specificity]
- The cross-project pitfalls digest gives an example: 12/176 experiments for MR1. The standard deviation across all experiments is dominated by the non-metal majority. [src: pitfalls]
- Raw module-condition scores are on a different scale from the z-scored profiles in atlas NB05. [src: metal_specificity]
- Recomputing z-scores from raw module_conditions.csv values does not reproduce the same responsiveness threshold. [src: pitfalls]
- NB05 used pre-computed z-scores from metal_modules.csv, standardized per module across all experiments rather than per experiment type. [src: pitfalls]

## Proposed follow-up in the source reports

The metal_specificity report proposes a metal-specific module re-analysis using pre-computed z-scored module activities from atlas NB05. [src: metal_specificity] It recommends that a future revision use the atlas's pre-computed z-scores directly. [src: metal_specificity] The metal_cross_resistance report proposes applying ICA to metal conditions to identify co-regulated metal-response modules and test whether cross-resistance genes cluster into coherent regulatory units. [src: metal_cross_resistance]

## Tensions

- The atlas found 600 responsive module records using z-scored profiles. [src: metal_fitness_atlas] The metal_specificity report found 0 metal-specific modules with z-scored profiles. [src: metal_specificity] The two ask different questions (responsiveness versus specificity), and the specificity report documents normalization limits on its own analysis. [src: metal_specificity, pitfalls]

## Open Directions

- Apply ICA to metal conditions and test whether cross-resistance genes cluster into coherent modules (see [[summaries/metal_cross_resistance__REPORT]]).
- Compare the 0.826 mean core fraction with non-metal modules, to test whether the core enrichment is specific to metal modules.
- Check how sensitive the 3.1% responsive fraction is to the |z| threshold and to the share of metal experiments per organism.
