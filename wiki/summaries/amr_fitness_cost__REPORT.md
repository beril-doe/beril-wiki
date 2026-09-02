---
type: "Summary"
description: "Pan-bacterial analysis finds small, universal, mechanism-independent AMR fitness costs."
doc_type: "short"
full_text: "sources/amr_fitness_cost__REPORT.md"
---
# Fitness Cost of Antimicrobial Resistance Genes

## Overview

This report uses genome-wide transposon fitness data from the KBase Fitness Browser compendium to test antimicrobial-resistance (AMR) fitness costs across bacteria. It identifies 1,352 AMR genes across 43 organisms, links them to fitness measurements and pangenome conservation, and evaluates baseline costs, antibiotic-dependent importance, resistance mechanism, and core-versus-accessory status. Twenty-five organisms qualify for per-organism tests, with 25/25 showing a positive AMR-versus-background fitness shift. [src: amr_fitness_cost]

## Key Findings

### Universal baseline cost

Under non-antibiotic conditions, AMR gene knockouts have systematically higher fitness than non-AMR gene knockouts, indicating that AMR genes impose a relative metabolic burden. A DerSimonian-Laird random-effects meta-analysis across 25 organisms gives a pooled effect of **+0.086 [95% CI: +0.074, +0.098], z = 14.3, p ~ 0**; all 25 of 25 organisms show a positive shift. The median per-organism Cohen's d is **0.18**, and heterogeneity is **I² = 54.3%** with Cochran's **Q = 52.54, p = 0.0007**. Six organisms are nominally significant at p<0.05 and two are FDR-significant at q<0.05: acidovorax_3H11 and Koxy. [src: amr_fitness_cost]

The report interprets the +0.086 effect as a relative difference between AMR knockout fitness and the non-AMR knockout background, not as beneficial absolute growth. Absolute AMR knockout fitness averages **−0.024**, while the non-AMR background averages approximately **−0.11**; a one-sample Wilcoxon test of AMR knockout fitness against zero gives **p = 0.999**. [src: amr_fitness_cost]

Only **4.6%** of AMR genes are absent from the fitness matrices and therefore putatively essential, compared with an approximately **14%** background essential rate estimated in a prior analysis using a different organism set. Tier 1 (bakta_amr, **N=110**) and Tier 2 keyword-annotated genes (**N=691**) have indistinguishable fitness distributions (**KS p = 0.17**), while the broader assembly contains **178 Tier 1** and **1,174 Tier 2** genes. [src: amr_fitness_cost]

### Increased importance under antibiotic exposure

Across any-antibiotic experiments, **57.0%** of AMR genes show a fitness flip toward greater importance under antibiotic exposure, with **N = 797**, mean flip **+0.045** (non-antibiotic fitness minus antibiotic fitness), and Wilcoxon signed-rank **p = 0.0001**. The flip is mechanism-dependent: broad-spectrum efflux genes show a mean flip of **+0.094**, compared with **−0.001** for enzymatic inactivation genes, with Mann-Whitney U **p = 0.007**. [src: amr_fitness_cost]

In the class-matched validation, **157 gene-antibiotic pairs** across four resistance classes show a mean flip of **+0.113**, a flip rate of **54.8%**, and Wilcoxon **p = 0.14**. Chloramphenicol resistance genes show the strongest validation, with **6/6 (100%)** showing the expected flip. Beta-lactam resistance has **105 pairs across 10 organisms** and a **50%** flip rate. [src: amr_fitness_cost]

The report interprets the contrast between baseline cost and antibiotic-dependent benefit as a decoupling: AMR mechanisms have similar modest costs without antibiotics, but broad-spectrum efflux systems become important under many antibiotic conditions whereas narrow-spectrum enzymes generally require matching antibiotics. [src: amr_fitness_cost]

### Resistance mechanism does not predict baseline cost

Baseline fitness cost does not differ significantly among efflux (**N=254**), enzymatic inactivation (**N=304**), metal resistance (**N=144**), and unknown (**N=74**) mechanisms. The Kruskal-Wallis test gives **H = 0.65, p = 0.89**, and the Jonckheere-Terpstra test for the predicted ordering efflux > enzymatic > metal > unknown gives **z = 0.23, p = 0.41**; no pairwise comparison survives FDR correction. [src: amr_fitness_cost]

The report proposes that the approximately **+0.086** common cost may represent a residual metabolic overhead after compensatory evolution in lab-adapted RB-TnSeq strains, rather than the unmitigated cost of newly acquired resistance. This interpretation is presented as an explanation consistent with the data, not as a directly measured compensatory-evolution process. [src: amr_fitness_cost]

### Core and accessory AMR genes have similar costs

Core, or intrinsic, AMR genes (**N=638**) and accessory, or acquired, AMR genes (**N=163**) have virtually identical distributions: both have mean **−0.024**, Cohen's **d = 0.002**, and Mann-Whitney U **p = 0.33**. The broader stratification table likewise reports no conservation difference (**p = 0.33**), no Tier 1-versus-Tier 2 difference (**p = 0.26**), and no antibiotic-versus-metal resistance-type difference (**p = 0.87**). [src: amr_fitness_cost]

The report interprets this null result as consistent with preferential horizontal transfer of cost-optimized genes or rapid compensation after acquisition, while noting that the evidence is strongest for well-sampled species. [src: amr_fitness_cost]

### Mechanism predicts conservation status but not cost

Mechanism is strongly associated with pangenome conservation status (**χ² = 69.3, p = 1.4×10⁻¹³**): **44%** of metal-resistance genes are accessory, compared with **13%** of efflux genes and **16%** of enzymatic-inactivation genes. Thus, in this dataset, mechanism predicts where an AMR gene occurs in the pangenome but not its baseline fitness cost. [src: amr_fitness_cost]

### Data scope

The analysis classifies **6,804 experiments**: **2,868** carbon/nitrogen, **1,862** stress, **727** standard, **447** metal, and **443** antibiotic experiments. It uses `kbase_ke_pangenome` tables `bakta_amr` and `bakta_annotations`, `kescience_fitnessbrowser` tables `genefitness`, `gene`, and `experiment`, a cross-project Fitness Browser–pangenome bridge, and cached fitness matrices; the generated datasets include **1,352** AMR genes, **6,804** classified experiments, **801** non-antibiotic per-gene fitness records, **25** organism effect sizes, **954** antibiotic-validation records, and **10** stratification summaries. [src: amr_fitness_cost]

## Caveats

- All **25** tested organisms are lab-adapted strains. Laboratory compensation may have reduced measurable costs relative to wild strains, so the estimate may underestimate costs in natural populations. [src: amr_fitness_cost]
- Tier 2 contains **86%** of the AMR genes and is based on keyword matching from Bakta annotations, which may include non-AMR genes such as general efflux transporters; the Tier 1 sensitivity analysis gives consistent results. [src: amr_fitness_cost]
- Matched antibiotic validation covers only four AMR classes: beta-lactam, aminoglycoside, chloramphenicol, and tetracycline. Macrolide, glycopeptide, and polymyxin resistance could not be validated. [src: amr_fitness_cost]
- Approximately **4.6%** of AMR genes are putatively essential and absent from fitness matrices. If these are the most costly AMR genes, **+0.086** is a lower bound. [src: amr_fitness_cost]
- RB-TnSeq measures fitness relative to the pool average. The **+0.086** value is the difference between AMR knockout fitness (**−0.024**) and non-AMR knockout fitness (approximately **−0.11**), not an absolute selection coefficient; comparison with isogenic-strain literature is not a direct equivalence. [src: amr_fitness_cost]
- Transposon insertions can have polar effects on downstream genes in operons, potentially confounding AMR-gene fitness measurements. [src: amr_fitness_cost]
- The product classifier does not handle fosfomycin or tellurite resistance annotations, leaving approximately **25 genes** in the unknown mechanism category; reclassification would move them to enzymatic inactivation and metal resistance, respectively. [src: amr_fitness_cost]
- Core/accessory labels use a **≥95%** prevalence threshold, but most Fitness Browser species have few GTDB genomes: the median is **9**, with a range of **2–399**. A gene present in all **9** sampled genomes may be mislabeled core at larger sampling depth, so the core-versus-accessory null result is especially cautious for species with fewer than **20** genomes. [src: amr_fitness_cost]
- The class-matched analysis has only **157** pairs and is non-significant (**p = 0.14**) despite a mean flip of **+0.113**; the any-antibiotic analysis has greater power (**N = 797**, **p = 0.0001**). [src: amr_fitness_cost]

## Future Directions

- Test mechanism effects within organisms with many AMR genes, including Cup4G11 (**77**) and BFirm (**50**), while controlling for genetic background. [src: amr_fitness_cost]
- Subclassify efflux pumps into narrow-spectrum drug pumps and general RND systems such as AcrAB-TolC, and test whether constitutively expressed systems have lower costs. [src: amr_fitness_cost]
- Replace averages across non-antibiotic experiments with condition-specific analyses of metal, osmotic, and carbon-limitation stresses. [src: amr_fitness_cost]
- Cross-reference the **144** metal-resistance genes with fitness data against the metal fitness atlas to test whether genes costly under standard conditions are protective under metal stress. [src: amr_fitness_cost]
- Extend the analysis from **25** Fitness Browser organisms to all **293K** BERDL genomes by predicting AMR cost from gene-cluster conservation patterns. [src: amr_fitness_cost]

## Slots Into

- [[concepts/environmental-resistome]] — AMR gene conservation, mechanism-specific pangenome location, and the distinction between resistance retention and metabolic cost.
- [[concepts/condition-specific-fitness]] — the relative baseline burden of AMR genes and their increased importance under antibiotic exposure.
- [[concepts/gene-essentiality]] — the **4.6%** putative essential rate among AMR genes and its comparison with the approximately **14%** background rate.
- [[concepts/pangenome-integration]] — integration of Fitness Browser fitness measurements with pangenome core/accessory labels and the mechanism-by-conservation association.
