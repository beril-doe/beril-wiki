---
type: "Concept"
description: "AMR costs may be obscured by compensation and experimental context."
sources: ["summaries/amr_fitness_cost__REPORT.md"]
---
# Compensation and the hidden cost of antimicrobial resistance

Antimicrobial-resistance (AMR) genes can impose a measurable baseline burden while appearing less costly than expected because the available strains may already be laboratory-adapted or compensated. In this report, the evidence supports a relative AMR-associated fitness difference, but the extent to which compensation produced that difference remains a hypothesis rather than a directly measured process. [src: amr_fitness_cost]

## Evidence for a residual baseline cost

The analysis used genome-wide random barcode transposon sequencing (RB-TnSeq), a pooled transposon method that estimates mutant fitness relative to the pool average, across 25 organisms. Every organism showed a positive AMR-versus-background fitness shift, and the DerSimonian-Laird random-effects meta-analysis estimated a pooled effect of **+0.086 [95% CI: +0.074, +0.098], z = 14.3, p ~ 0**. The median per-organism Cohen's d was **0.18**, with heterogeneity of **I² = 54.3%** and Cochran's **Q = 52.54, p = 0.0007**. [src: amr_fitness_cost]

This effect is relative rather than an absolute growth advantage for AMR knockouts. Absolute AMR knockout fitness averaged **−0.024**, whereas the non-AMR knockout background averaged approximately **−0.11**; a one-sample Wilcoxon test of AMR knockout fitness against zero gave **p = 0.999**. Thus, the result indicates that AMR knockouts were less impaired than the comparison knockout background, not that they had positive absolute fitness. [src: amr_fitness_cost]

The residual burden was not explained by resistance mechanism in the measured baseline data. Efflux (**N=254**), enzymatic inactivation (**N=304**), metal resistance (**N=144**), and unknown (**N=74**) mechanisms had no significant baseline-cost difference: Kruskal-Wallis **H = 0.65, p = 0.89**, and the predicted ordering efflux > enzymatic > metal > unknown gave Jonckheere-Terpstra **z = 0.23, p = 0.41**. [src: amr_fitness_cost]

## Why compensation is a plausible interpretation

The report proposes that the approximately **+0.086** common cost may be a residual metabolic overhead after compensatory evolution in lab-adapted RB-TnSeq strains. This is an interpretation consistent with the measurements, not a direct measurement of compensatory mutations, their timing, or their causal effect. [src: amr_fitness_cost]

All **25** tested organisms were lab-adapted strains, so laboratory history may have reduced measurable AMR costs relative to costs in natural populations. The report therefore treats the observed estimate as potentially lower than the unmitigated cost of newly acquired resistance. [src: amr_fitness_cost]

The core-versus-accessory comparison is also consistent with cost optimization or post-acquisition compensation, but does not distinguish those explanations. Core/intrinsic AMR genes (**N=638**) and accessory/acquired AMR genes (**N=163**) both had mean fitness of **−0.024**, Cohen's **d = 0.002**, and Mann-Whitney U **p = 0.33**. The report suggests that preferential horizontal transfer of cost-optimized genes or rapid compensation after acquisition could produce this null result, while emphasizing that the evidence is strongest for well-sampled species. [src: amr_fitness_cost]

The null result is especially cautious because core/accessory labels used a **≥95%** prevalence threshold, while most Fitness Browser species had few GTDB genomes: the median was **9**, with a range of **2–399**. A gene present in all **9** sampled genomes could be labeled core at this sampling depth but not remain core with broader sampling. [src: amr_fitness_cost]

## Cost is condition-dependent

The baseline burden does not imply that AMR genes are uniformly dispensable. Across any-antibiotic experiments, **57.0%** of AMR genes showed a fitness flip toward greater importance under antibiotic exposure, with **N = 797**, mean flip **+0.045** (non-antibiotic fitness minus antibiotic fitness), and Wilcoxon signed-rank **p = 0.0001**. [src: amr_fitness_cost]

This supports [[concepts/condition-specific-fitness]]: the same resistance system can carry a modest relative burden without antibiotics yet become important when the matching environmental challenge is present. Broad-spectrum efflux genes had a mean flip of **+0.094**, compared with **−0.001** for enzymatic inactivation genes, with Mann-Whitney U **p = 0.007**. [src: amr_fitness_cost]

The class-matched validation provides weaker support for this condition-specific interpretation. Across **157 gene-antibiotic pairs**, the mean flip was **+0.113**, the flip rate was **54.8%**, and Wilcoxon **p = 0.14**; chloramphenicol resistance genes showed the strongest validation at **6/6 (100%)**, while beta-lactam resistance comprised **105 pairs across 10 organisms** with a **50%** flip rate. [src: amr_fitness_cost]

## Hidden-cost interpretation

The central implication is that observed AMR fitness costs should not be treated as fixed properties of resistance genes. The measured baseline signal supports a residual cost, while the similarity of costs across mechanisms and between core and accessory genes suggests that evolutionary history, strain background, and condition may obscure the original cost of resistance acquisition. The compensation component remains a hypothesis until genomic changes or experimentally reconstructed lineages are linked to restored fitness. [src: amr_fitness_cost]

This interpretation connects to [[concepts/antimicrobial-resistance-fitness-cost]], which addresses the measured AMR burden, and to [[concepts/fitness-cost-and-network-breadth]], which provides a broader framework for relating fitness costs to the breadth of gene effects. It also informs [[concepts/environmental-resistome]] because resistance retention may reflect ecological protection, compensated persistence, or both rather than baseline cost alone. [src: amr_fitness_cost]

The source report and its detailed evidence are available in [[summaries/amr_fitness_cost__REPORT]]. [src: amr_fitness_cost]

## Open Directions

- Use matched genomes from the **25** lab-adapted organisms, comparative genomics, and fitness association analysis to ask whether specific compensatory mutations explain the residual **+0.086** AMR-versus-background shift. [src: amr_fitness_cost]
- Reconstruct newly acquired and compensated AMR genotypes in isogenic strains and measure growth and competition fitness to distinguish the original cost from the post-compensation cost. [src: amr_fitness_cost]
- Subclassify efflux genes into narrow-spectrum pumps and general RND systems such as AcrAB-TolC, then use condition-specific fitness assays to ask whether constitutive systems have lower baseline costs. [src: amr_fitness_cost]
- Cross-reference the **144** metal-resistance genes with the metal fitness atlas and test, using matched metal-stress fitness measurements, whether genes costly under standard conditions are protective under metal stress. [src: amr_fitness_cost]
- Expand GTDB sampling beyond the median of **9** genomes per Fitness Browser species and recompute the **≥95%** core/accessory labels to ask whether the core-versus-accessory cost null result persists with deeper pangenomes. [src: amr_fitness_cost]
