---
type: "Organism"
description: "Organism (Fitness Browser Koxy) with the highest annotation-gap resolution rate."
sources: ["summaries/amr_fitness_cost__REPORT.md", "summaries/annotation_gap_discovery__REPORT.md", "summaries/cofitness_coinheritance__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/metabolic_capability_dependency__REPORT.md"]
aliases: ["K. oxytoca", "Koxy"]
---
# Klebsiella michiganensis

Klebsiella michiganensis (also K. oxytoca; Fitness Browser code Koxy) is an organism in the [[entities/fitness-browser]]. It had the highest annotation-gap resolution rate among the organisms compared in one report. [src: annotation_gap_discovery]

## Key facts

- The AMR (antimicrobial resistance) conservation analysis identifies K. michiganensis, with 399 genomes, as a well-sampled species. [src: amr_fitness_cost]
- The extracted Koxy dataset contained 399 genomes, 4,942 clusters and 423,936 cofit pairs, with a phylogenetic tree. [src: cofitness_coinheritance]

## Annotation-gap resolution

Resolution rates ranged from 20% in Bacteroides thetaiotaomicron to 71% in Klebsiella michiganensis. [src: annotation_gap_discovery] See [[entities/bacteroides-thetaiotaomicron]] for the low end. Koxy had 7 total annotation gaps, of which 5 were resolved (71.4%). [src: annotation_gap_discovery] See [[concepts/reference-database-coverage-and-phylogenetic-bias-in-annotation-gap-estimates]] and [[summaries/annotation_gap_discovery__REPORT]].

## AMR fitness

The per-organism AMR fitness analysis found 2 organisms significant at FDR (false discovery rate) q<0.05: acidovorax_3H11 and Koxy. [src: amr_fitness_cost] See [[concepts/fitness-cost-of-antimicrobial-resistance-genes]].

## Co-fitness and co-inheritance

For Koxy, the module analysis listed 44 modules, 14 (32%) significant, with mean phi 0.079 and null mean 0.040. [src: cofitness_coinheritance] Across 162,160 cofit pairs, mean phi was 0.041 versus 0.038 for random pairs, a delta of +0.003 with two-sided p-value 3.3e-2. [src: cofitness_coinheritance] See [[concepts/co-fitness-as-a-predictor-of-gene-co-inheritance-in-pangenomes]] and [[concepts/conservation-of-cofitness-modules-across-genomes-and-organisms]].

## Latent pathways

The latent pathway fraction across Fitness Browser organisms ranged 0–31.6%, with mean 15.0%. It was highest in Pseudomonas syringae strains and Klebsiella michiganensis. [src: metabolic_capability_dependency] See [[concepts/latent-metabolic-capability-versus-fitness-dependency]].

## Dark genes (listed as K. oxytoca)

The functional dark matter report uses the name K. oxytoca for these genes.

- BWI76_RS08540 ranks 3 among essential dark gene candidates, with score 0.865, OmpA and TIGR02802 domains, TolB plus CpoB (cell division) operon context, and high hypothesis confidence. [src: functional_dark_matter] The report predicts cell division function and conservation across Enterobacteriaceae. [src: functional_dark_matter] See [[concepts/essential-genes-as-a-blind-spot-of-transposon-fitness-screens]].
- A dark gene in K. oxytoca receives a yersiniabactin transporter (YbtP) annotation from Bakta's AMRFinderPlus. [src: functional_dark_matter]
- A dark gene in K. oxytoca receives an acid resistance protein (Asr) annotation from Bakta's AMRFinderPlus. [src: functional_dark_matter]
- K. oxytoca is fifth in Route A, with 396 genes and tractability 0.65. It covers Enterobacteriaceae genes absent from Escherichia coli, including BWI76_RS08540. [src: functional_dark_matter]
- K. michiganensis is fifth in Route B, with 568 OGs (ortholog groups), 65 kingdom gaps and tractability 0.65. It adds Enterobacteriaceae depth beyond E. coli. [src: functional_dark_matter]
- BWI76_RS15640 has a carbon phenotype with |fit| 2.1, carrier environment human_assoc, OR (odds ratio) 0.14, FDR 0.031, universal breadth, and module prediction Phage tail tape-measure. [src: functional_dark_matter]
- BWI76_RS15525 (carbon |fit| 2.3) and BWI76_RS15535 (carbon |fit| 2.2) each had expected soil, freshwater and plant environments in 14.3% of carriers versus 2.5% of non-carriers (OR 6.6, FDR 0.069). [src: functional_dark_matter] See [[concepts/concordance-between-laboratory-fitness-phenotypes-and-field-environments-of-gene-carriers]] and [[summaries/functional_dark_matter__REPORT]].
