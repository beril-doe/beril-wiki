---
type: "Concept"
description: "High prevalence compresses variation and weakens pangenome co-occurrence inference"
sources: ["summaries/cofitness_coinheritance__REPORT.md"]
---
# Prevalence ceilings limit detection and interpretation of pangenome co-occurrence

## Core idea

A prevalence ceiling arises when gene clusters occur in nearly every genome, leaving little presence/absence variation for detecting co-occurrence. In this setting, phi coefficients—the association between two binary presence/absence patterns—can approach zero for both cofit and random gene pairs, so a weak observed association does not necessarily indicate weak biological coupling. [src: cofitness_coinheritance]

This concept connects [[summaries/cofitness_coinheritance__REPORT]] to [[concepts/cofitness-network-architecture]] and [[concepts/fitness-matched-null-models]]: the study found that prevalence matching can control a major null-model artifact, but it cannot recover signal absent from nearly invariant gene distributions. [src: cofitness_coinheritance]

## Evidence from co-fitness and pangenome data

The study analyzed 2,253,491 cofit pairs against 22,534,910 prevalence-matched random pairs across 9 organisms. [src: cofitness_coinheritance] Pairwise cofit pairs had an aggregate delta phi of +0.003, with Mann-Whitney p=1.66e-29, but the across-organism Wilcoxon signed-rank test was not significant (W=9, p=0.13), indicating that the aggregate signal was small relative to inter-organism variation. [src: cofitness_coinheritance]

Co-fitness strength was weakly anti-correlated with co-occurrence across 1.04M pairs (Spearman rho=-0.109, p<1e-300). [src: cofitness_coinheritance] The report attributes this pattern to a prevalence ceiling: the strongest co-fitness pairs were often core genes with near-universal prevalence, leaving little variation for measuring co-occurrence. [src: cofitness_coinheritance]

The prevalence problem was especially visible in the Korea dataset, where 95.2% of cofit pairs had NaN phi because both genes were present in 100% of 72 genomes. [src: cofitness_coinheritance] Only approximately 8,000 of 166,601 pairs were computable, so the observed negative delta of -0.042 was interpreted as statistical noise rather than a biological signal. [src: cofitness_coinheritance]

The module analysis provides a contrast because coordinated sets can retain detectable variation even when individual pairwise associations are weak. Across 195 ICA (independent component analysis) modules in 6 organisms, within-module co-occurrence had mean phi=0.229 versus a prevalence-matched null mean of 0.177 from 1000 permutations, for delta=+0.053. [src: cofitness_coinheritance] However, Korea had no significant modules because all Korea modules were >90% core with prevalence near 1.0. [src: cofitness_coinheritance]

## Interpretation

The results support restricting primary co-occurrence comparisons to auxiliary gene pairs, because the report specifically proposes requiring both clusters to be below 95% prevalence. [src: cofitness_coinheritance] This restriction would target the portion of the pangenome where presence/absence variation can distinguish co-inherited genes from prevalence-matched controls, although it would also exclude genuinely coupled genes that are nearly universal. [src: cofitness_coinheritance]

Prevalence ceilings also complicate comparisons among organisms. Ddia6719 had delta=+0.093 and pseudo3_N2E3 had delta=+0.026 despite near-clonal ANI values of 99.47% and 99.66%, respectively; both retained enough accessory variation to detect co-inheritance, but their high baseline phi values made absolute phi values less interpretable. [src: cofitness_coinheritance] The study therefore supports interpreting delta phi together with prevalence distributions, auxiliary-versus-core status, and the amount of computable data rather than treating a raw phi value as a directly comparable measure across species. [src: cofitness_coinheritance]

This prevalence limitation is distinct from, but interacts with, [[concepts/phylogenetic-confounding-of-pangenome-associations]]: cofit-pair phi was higher among near genomes (mean=0.102) than medium-distance genomes (mean=0.067), while most species lacked genomes in the far stratum (>0.05 branch distance). [src: cofitness_coinheritance] Thus, both insufficient prevalence variation and incomplete phylogenetic separation can limit interpretation of pangenome associations. [src: cofitness_coinheritance]

## Implications for pangenome integration

The study demonstrates that linking Fitness Browser co-fitness data with pangenome presence/absence data is informative only when the joined gene clusters have sufficient prevalence variation. [src: cofitness_coinheritance] This refines [[concepts/pangenome-integration]] by making prevalence an explicit quality criterion for cross-dataset association analyses. [src: cofitness_coinheritance]

The stronger signal for ICA modules than for individual pairs suggests that prevalence-aware analyses should test coordinated multi-gene units as well as pairwise relationships. [src: cofitness_coinheritance] Accessory modules had mean delta phi +0.108, compared with +0.059 for core modules (>90% core) and +0.031 for mixed modules (50–90%), although the accessory-versus-core difference only trended toward significance (Mann-Whitney p=0.051). [src: cofitness_coinheritance]

## Open Directions

- Use the existing pangenome presence matrices to restrict both members of each pair to clusters below 95% prevalence, then test whether the cofit-versus-random delta phi increases and whether the organism-level heterogeneity persists. [src: cofitness_coinheritance]
- Recompute co-fitness from raw genefitness data for Ralstonia UW163 and Ralstonia GMI1000, then repeat prevalence-matched association tests to determine whether their exclusion removed informative low-ANI diversity. [src: cofitness_coinheritance]
- Combine prevalence-stratified phi estimates with reference-resolved phylogenetic distances, then test whether co-fitness predicts co-occurrence after separately controlling for prevalence and shared ancestry. [src: cofitness_coinheritance]
- Build module co-transfer networks from the ICA modules and test whether cross-module prediction remains detectable after matching module prevalence and auxiliary content. [src: cofitness_coinheritance]
- Expand the analysis to species with >30% auxiliary genes and existing co-fitness data, then measure whether increased accessory variation improves pairwise and module-level detection. [src: cofitness_coinheritance]
