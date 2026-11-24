---
type: "Organism"
description: "Anaerobic Fitness Browser organism matched to BacDive, with only one metal tested."
sources: ["summaries/bacdive_phenotype_metal_tolerance__REPORT.md", "summaries/conservation_vs_fitness__REPORT.md", "summaries/discoveries.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/snipe_defense_system__REPORT.md", "summaries/truly_dark_genes__REPORT.md"]
aliases: ["MMJJ_RS01635", "Methanococcus JJ", "Methanococcus S2", "Methanococcus maripaludis JJ", "Methanococcus_JJ", "Methanococcus_S2"]
---
# Methanococcus maripaludis

Methanococcus maripaludis is a methanogenic archaeon with two Fitness Browser strains, S2 and JJ. The locus MMJJ_RS01635 is in strain JJ. The evidence is strongest for its role as the only Fitness Browser carrier of a full SNIPE protein and as the main source of truly dark genes. Its metal-tolerance coverage is thin: only iron has been tested. [src: metal_fitness_atlas, snipe_defense_system, truly_dark_genes]

## Key facts

- Twelve Fitness Browser organisms match BacDive by taxonomy ID. They represent 6 unique species, and M. maripaludis is one of them. [src: bacdive_phenotype_metal_tolerance]
- It is the single anaerobe in that direct Fitness Browser–BacDive validation. It has only 1 metal tested versus 4–5 for aerobes, and the report considers n = 1 not interpretable. [src: bacdive_phenotype_metal_tolerance]
- Strain S2 had one of the strongest essential-core enrichment signals, with OR (odds ratio)=5.21. [src: conservation_vs_fitness] See [[concepts/essential-genes-and-core-genome-conservation]].

## Metal fitness coverage

Both strains have 54 novel ortholog groups and have been tested only against iron. [src: metal_fitness_atlas] The metal fitness atlas report proposes Ni, Co, Cu, Zn, W and Mo tests in S2, noting that archaea are underrepresented in metal tolerance studies. [src: metal_fitness_atlas] It also proposes the same panel in JJ, so a cross-strain comparison with S2 could reveal strain-specific metal adaptation. [src: metal_fitness_atlas] See [[concepts/metal-coverage-gaps-and-proposed-validation-experiments]] and [[concepts/metabolic-versatility-oxygen-tolerance-and-metal-tolerance]].

## SNIPE protein (strain JJ)

The Fitness Browser holds one archaeal [[entities/snipe]] protein, in strain JJ at locus MMJJ_RS01635. It carries PF13250 (DUF4041), PF13455 (Mug113/GIY-YIG nuclease) and PF10544 (DUF2525). [src: discoveries, snipe_defense_system] It has 129 fitness experiments. The reports describe it as the first SNIPE homologue with genome-wide knockout phenotypes. [src: discoveries, snipe_defense_system] Only M. maripaludis in the Fitness Browser has the full two-domain architecture (PF13250 + PF13455). [src: snipe_defense_system]

The gene shows mild fitness defects under specific conditions, with minimum fitness = -1.16 on formate/acetate. [src: snipe_defense_system] It is dispensable under most conditions. [src: snipe_defense_system] The report calls M. maripaludis the first organism with both a confirmed SNIPE protein and genome-wide fitness data. [src: snipe_defense_system] This comes with a caveat. As an archaeon, its phage biology context differs significantly from the Enterobacterales phage lambda system. [src: snipe_defense_system] See [[concepts/fitness-data-coverage-gaps-for-defense-genes]].

## Truly dark genes

Strains S2 and JJ together account for 55% of truly dark genes. [src: truly_dark_genes] The report attributes this to archaeal proteins being systematically underrepresented in reference databases compared to bacteria. [src: truly_dark_genes] See [[concepts/reference-database-coverage-and-phylogenetic-bias-in-annotation-gap-estimates]]. Among the top 100 candidates, which span 19 organisms, Methanococcus_S2 contributes 29, DvH 13, Methanococcus_JJ 13 and MR-1 8. [src: truly_dark_genes] One example is Methanococcus_S2/MMP_RS06570, with score 9 and 8 annotation clues. These include DUF190, COG-T signal transduction and an operon with fluoride efflux transporter CrcB. [src: truly_dark_genes]

The report proposes a focused Methanococcus analysis. It would use high cofitness signals (r > 0.97) to map operonic structure and generate functional predictions for archaeal-specific hypothetical proteins. [src: truly_dark_genes] See [[concepts/guilt-by-association-inference-of-dark-gene-function-from-modules-operons-synteny-and-co-fitness]].
