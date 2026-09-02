---
type: "Concept"
description: "How to interpret relative fitness effects from RB-TnSeq perturbations"
sources: ["summaries/amr_fitness_cost__REPORT.md"]
---
# Interpreting relative fitness costs from transposon perturbation data

## Core interpretation

[[entities/tnseq|RB-TnSeq]] (random barcode transposon sequencing) measures the competitive fitness of insertion mutants relative to the pool average, rather than an absolute selection coefficient measured in an isogenic strain. [src: amr_fitness_cost] Consequently, a difference between mutant classes should be interpreted as a relative shift in perturbation fitness, not automatically as beneficial or harmful absolute growth. [src: amr_fitness_cost]

The [[summaries/amr_fitness_cost__REPORT|AMR fitness-cost analysis]] illustrates this distinction: under non-antibiotic conditions, AMR-gene knockouts had an average fitness of **−0.024**, whereas the non-AMR knockout background averaged approximately **−0.11**, producing a relative difference of **+0.086**. [src: amr_fitness_cost] The positive difference means that AMR knockouts were less impaired than the comparison knockout background in these measurements; it does not mean that the AMR knockouts grew faster than an unperturbed reference. [src: amr_fitness_cost] Consistently, a one-sample Wilcoxon test of AMR-knockout fitness against zero gave **p = 0.999**. [src: amr_fitness_cost]

## Evidence for a relative AMR-associated shift

Across **25** organisms, every organism showed a positive AMR-versus-background shift, and a DerSimonian-Laird random-effects meta-analysis estimated a pooled effect of **+0.086 [95% CI: +0.074, +0.098], z = 14.3, p ~ 0**. [src: amr_fitness_cost] The median per-organism Cohen's d was **0.18**, while heterogeneity was **I² = 54.3%** with Cochran's **Q = 52.54, p = 0.0007**. [src: amr_fitness_cost] Thus, the evidence supports a reproducible relative difference across organisms, while the heterogeneity indicates that its magnitude is not uniform. [src: amr_fitness_cost]

The report describes this relative shift as a baseline AMR burden, but the interpretation is indirect because it compares knockout classes rather than directly measuring the cost of acquiring or expressing an intact resistance gene. [src: amr_fitness_cost] The estimate may also be conservative because approximately **4.6%** of AMR genes were absent from the fitness matrices and were therefore putatively essential, compared with an approximately **14%** background essential rate estimated in a prior analysis using a different organism set. [src: amr_fitness_cost] These omitted genes cannot contribute ordinary knockout fitness values and could alter the observed contrast if they are disproportionately costly. [src: amr_fitness_cost]

## Condition dependence changes the interpretation

The relative baseline comparison should not be confused with condition-specific protection: across any-antibiotic experiments, **57.0%** of AMR genes showed a fitness flip toward greater importance under antibiotic exposure, with **N = 797**, mean flip **+0.045**, and Wilcoxon signed-rank **p = 0.0001**. [src: amr_fitness_cost] In this analysis, the flip was defined as non-antibiotic fitness minus antibiotic fitness, so a positive value indicates greater importance of the gene during antibiotic exposure. [src: amr_fitness_cost]

The condition-dependent signal was mechanism-specific: broad-spectrum efflux genes had a mean flip of **+0.094**, compared with **−0.001** for enzymatic-inactivation genes, with Mann-Whitney U **p = 0.007**. [src: amr_fitness_cost] The class-matched validation included **157 gene-antibiotic pairs**, had a mean flip of **+0.113**, a flip rate of **54.8%**, and Wilcoxon **p = 0.14**. [src: amr_fitness_cost] Chloramphenicol resistance genes showed the strongest validation, with **6/6 (100%)** showing the expected flip, whereas beta-lactam resistance included **105 pairs across 10 organisms** and had a **50%** flip rate. [src: amr_fitness_cost]

These results support separating [[concepts/condition-specific-fitness|condition-specific fitness]] from a pooled baseline contrast: AMR mechanisms had similar modest relative costs without antibiotics, while broad-spectrum efflux systems became important across many antibiotic conditions and narrow-spectrum enzymes generally required matching antibiotics. [src: amr_fitness_cost]

## Null models and comparison design

A relative fitness effect is meaningful only with an explicitly defined comparison background, because the sign and magnitude depend on which perturbations and conditions enter the reference distribution. [src: amr_fitness_cost] In the AMR analysis, the comparison was between AMR and non-AMR knockouts under non-antibiotic conditions, rather than between AMR knockouts and an unperturbed wild type. [src: amr_fitness_cost] This design makes [[concepts/fitness-matched-null-models|fitness-matched null models]] and condition matching central to interpreting whether an apparent cost reflects resistance biology or differences in experiment composition. [src: amr_fitness_cost]

The baseline effect did not differ significantly among efflux (**N=254**), enzymatic inactivation (**N=304**), metal resistance (**N=144**), and unknown (**N=74**) mechanisms: Kruskal-Wallis **H = 0.65, p = 0.89**, and Jonckheere-Terpstra **z = 0.23, p = 0.41**, with no pairwise comparison surviving FDR correction. [src: amr_fitness_cost] This null result means that the data do not establish a mechanism-specific ordering of baseline relative costs, even though mechanism was strongly associated with pangenome conservation status (**χ² = 69.3, p = 1.4×10⁻¹³**). [src: amr_fitness_cost]

## Measurement limitations

All **25** tested organisms were lab-adapted strains, so laboratory compensation may have reduced measurable costs relative to those in natural populations. [src: amr_fitness_cost] The report therefore presents the approximately **+0.086** effect as consistent with residual metabolic overhead after compensatory evolution, but not as a directly measured compensatory-evolution process. [src: amr_fitness_cost]

Transposon insertions can have polar effects on downstream genes in operons, which may confound attribution of a fitness phenotype to the targeted AMR gene itself. [src: amr_fitness_cost] Tier 2 contained **86%** of the AMR genes and was based on keyword matching from Bakta annotations, which may include non-AMR genes such as general efflux transporters, although the Tier 1 sensitivity analysis gave consistent results. [src: amr_fitness_cost] These issues connect relative-fitness interpretation to [[concepts/environmental-resistome|annotation-dependent resistome inference]] and [[concepts/perturbation-modality-dependent-phenotypic-architecture|perturbation-modality-dependent phenotypic architecture]].

The class-matched antibiotic analysis was less powered than the any-antibiotic analysis: it contained **157** pairs and was non-significant at **p = 0.14**, whereas the any-antibiotic analysis contained **N = 797** records and gave **p = 0.0001**. [src: amr_fitness_cost] This difference cautions against treating the positive pooled antibiotic signal as equally strong for every drug-resistance class. [src: amr_fitness_cost]

## Practical interpretation rule

A reported positive or negative transposon fitness contrast should be stated with its perturbation, reference population, condition set, and scale before being called a biological cost or benefit. [src: amr_fitness_cost] For this dataset, the most defensible wording is that AMR knockouts showed a positive relative shift against the non-AMR knockout background under non-antibiotic conditions, while AMR genes often became more important under antibiotic exposure. [src: amr_fitness_cost] This wording preserves the distinction between [[concepts/relative-fitness-and-transposon-interpretation|relative perturbation fitness]], absolute growth, and condition-specific resistance function. [src: amr_fitness_cost]

## Open Directions

- Use isogenic strains with direct growth-rate or competition assays to test whether the **+0.086** knockout-class contrast corresponds to an absolute cost of intact AMR genes rather than only a relative perturbation shift. [src: amr_fitness_cost]
- Reanalyze the **801** non-antibiotic per-gene fitness records with matched metal, osmotic, and carbon-limitation conditions to ask whether the baseline contrast changes across stress environments. [src: amr_fitness_cost]
- Model insertion position and operon context, using gene-neighborhood information to test how much of the measured AMR phenotype could arise from polar effects on downstream genes. [src: amr_fitness_cost]
- Incorporate the approximately **4.6%** putatively essential AMR genes through targeted essentiality assays or alternative perturbations to test whether their exclusion makes **+0.086** a lower bound. [src: amr_fitness_cost]
- Subclassify efflux systems and compare broad-spectrum RND systems with narrow-spectrum pumps using condition-matched antibiotic fitness data to test whether breadth predicts antibiotic-dependent importance. [src: amr_fitness_cost]
