---
type: "Organism"
description: "Sole Bacteroidetes among the 14 organisms, with the lowest annotation-gap resolution."
sources: ["summaries/amr_fitness_cost__REPORT.md", "summaries/annotation_gap_discovery__REPORT.md", "summaries/cofitness_coinheritance__REPORT.md", "summaries/functional_dark_matter__REPORT.md"]
aliases: ["B. thetaiotaomicron", "Btheta"]
---
# Bacteroides thetaiotaomicron

Bacteroides thetaiotaomicron (also B. thetaiotaomicron, Btheta) is the sole Bacteroidetes among the 14 organisms in the annotation-gap analysis. It had the lowest annotation-gap resolution rate there. [src: annotation_gap_discovery] It also appears in the co-fitness, dark-matter and antimicrobial resistance (AMR) projects.

## Key facts

- The AMR fitness-cost report lists B. thetaiotaomicron, with 287 genomes, among the well-sampled species. [src: amr_fitness_cost]
- The extracted co-fitness dataset for Btheta had 287 genomes, 4,649 clusters and 328,455 cofit pairs, with a phylogenetic tree. [src: cofitness_coinheritance]

## Annotation-gap resolution

Resolution rates ranged from 20% in B. thetaiotaomicron to 71% in [[entities/klebsiella-michiganensis|Klebsiella michiganensis]]. [src: annotation_gap_discovery] Btheta had 15 total annotation gaps, of which 3 were resolved (20.0%). [src: annotation_gap_discovery] The report links the low rate to its more divergent Bacteroidetes metabolism and its phylogenetic distance from the proteobacterial majority. [src: annotation_gap_discovery] It suggests the approach may be less effective for phylogenetically distant clades with divergent metabolism. [src: annotation_gap_discovery] See [[concepts/reference-database-coverage-and-phylogenetic-bias-in-annotation-gap-estimates]] and [[summaries/annotation_gap_discovery__REPORT]].

## Co-fitness and co-inheritance

Pairwise co-fitness showed almost no difference from random for Btheta. Its 242,676 cofit pairs had mean phi 0.067, against 0.067 for random pairs (delta +0.001, two-sided p <1e-6). [src: cofitness_coinheritance] At the module level the signal was the strongest in the report. Of 36 modules, 22 (61%) were significant, with mean phi 0.192 against a null mean of 0.086. [src: cofitness_coinheritance] See [[concepts/co-fitness-as-a-predictor-of-gene-co-inheritance-in-pangenomes]], [[concepts/conservation-of-cofitness-modules-across-genomes-and-organisms]] and [[summaries/cofitness_coinheritance__REPORT]].

## Dark-gene prioritization

B. thetaiotaomicron contributes 1,382 genes and 267 kingdom gaps, the highest raw count. A tractability score of 0.3 deprioritizes it. [src: functional_dark_matter] In Route B it ranks fourth. The report calls its raw OG (ortholog group) count the highest of any organism and its Bacteroidota coverage critical for non-Proteobacteria coverage despite low tractability. [src: functional_dark_matter] See [[concepts/organism-selection-and-taxonomic-coverage-bias-for-experimental-characterization-of-dark-genes]] and [[summaries/functional_dark_matter__REPORT]].

Two loci have stress phenotypes with a human-associated carrier environment and universal breadth:

- Locus 354052 has |fit| 2.4, odds ratio 0.17 and FDR (false discovery rate) 0.005. [src: functional_dark_matter]
- Locus 350920 has |fit| 2.2, odds ratio 0.37 and FDR 0.031. [src: functional_dark_matter]

See [[concepts/concordance-between-laboratory-fitness-phenotypes-and-field-environments-of-gene-carriers]]. The AMR work is in [[concepts/fitness-cost-of-antimicrobial-resistance-genes]] and [[summaries/amr_fitness_cost__REPORT]].
