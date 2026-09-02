---
type: "Concept"
description: "ICA fitness modules show stronger pangenome co-inheritance than pairwise links"
sources: ["summaries/cofitness_coinheritance__REPORT.md"]
---
# Multi-gene fitness modules predict pangenome co-inheritance better than pairwise links

## Core claim

Laboratory-measured pairwise co-fitness showed only a weak positive relationship with gene co-occurrence across bacterial pangenomes, whereas coordinated multi-gene modules identified by independent component analysis (ICA) showed a stronger co-inheritance signal. [src: cofitness_coinheritance] This finding extends [[concepts/cofitness-network-architecture]] by indicating that multi-gene organization may be more informative than isolated pairwise links for understanding which genes travel together through a pangenome. [src: cofitness_coinheritance]

The underlying study integrated Fitness Browser co-fitness measurements with pangenome presence/absence data, phylogenetic distances, ICA modules, and SEED functional annotations; the full project summary is [[summaries/cofitness_coinheritance__REPORT]]. [src: cofitness_coinheritance]

## Pairwise co-fitness provides a weak signal

Across 9 organisms, 2,253,491 cofit pairs were compared with 22,534,910 prevalence-matched random pairs. [src: cofitness_coinheritance] The mean delta phi, defined as cofit-pair co-occurrence minus matched-random co-occurrence, was +0.011 across organisms, with 7 of 9 organisms showing positive effects and 8 of 9 significant at p<0.05 by two-sided Mann-Whitney testing. [src: cofitness_coinheritance] The aggregate effect was delta=+0.003 with Mann-Whitney p=1.66e-29, but the Wilcoxon signed-rank test across organisms was not significant (W=9, p=0.13), demonstrating high inter-organism variance. [src: cofitness_coinheritance]

The organism-level results ranged from Ddia6719 at +0.093 to Korea at -0.042, with intermediate values of +0.026 for pseudo3_N2E3, +0.009 for Phaeo, +0.006 for SyringaeB728a, +0.003 for Koxy, +0.002 for Smeli, +0.001 for Btheta, and -0.000 for Putida. [src: cofitness_coinheritance] Korea’s negative result was difficult to interpret because 95.2% of its cofit pairs had NaN phi values, only approximately 8,000 of 166,601 pairs were computable, and both genes were present in 100% of 72 genomes for the affected pairs. [src: cofitness_coinheritance]

Only 0.7% of cofit pairs were genomically adjacent within 5 genes, and excluding adjacent pairs did not change the result pattern, so operon proximity did not explain the weak pairwise association. [src: cofitness_coinheritance] Co-fitness strength was also weakly anti-correlated with co-occurrence across 1.04M pairs (Spearman rho=-0.109, p<1e-300), a pattern attributed to a prevalence ceiling in which strong co-fitness pairs are often core genes with near-universal prevalence. [src: cofitness_coinheritance]

## ICA modules show stronger co-inheritance

Across 195 ICA modules in 6 organisms, within-module co-occurrence had mean phi=0.229, compared with a prevalence-matched null mean of 0.177 from 1000 permutations, for delta=+0.053. [src: cofitness_coinheritance] A total of 51/195 modules (26%) were significant at p<0.05, and 21/195 (11%) remained significant at q<0.05 after Benjamini-Hochberg FDR correction, where FDR means false discovery rate. [src: cofitness_coinheritance]

This module-level result **supports** the interpretation that coordinated multi-gene structure captures a stronger pangenome inheritance signal than pairwise co-fitness alone. [src: cofitness_coinheritance] The result is consistent with a model in which genes participating in coordinated regulation or shared selective units are retained or transferred together even when individual pairwise co-fitness values are insufficiently predictive. [src: cofitness_coinheritance]

The strongest module-level enrichment occurred in accessory modules, defined here as modules with less than 50% core genes. [src: cofitness_coinheritance] Accessory modules had mean delta phi +0.108, with 8/11 (73%) significant at p<0.05 and 4/11 (36%) significant at FDR q<0.05. [src: cofitness_coinheritance] Core modules, defined as modules with more than 90% core genes, had mean delta +0.059, with 29/120 (24%) significant at p<0.05 and 13/120 (11%) at q<0.05. [src: cofitness_coinheritance] Mixed modules, defined as modules with 50–90% core genes, had mean delta +0.031, with 14/64 (22%) significant at p<0.05 and 4/64 (6%) at q<0.05. [src: cofitness_coinheritance] The accessory-versus-core difference trended toward significance by Mann-Whitney testing (p=0.051). [src: cofitness_coinheritance]

The 48 accessory modules identified by the module_conservation project are interpreted as functionally coherent units that travel together through the pangenome. [src: cofitness_coinheritance] This interpretation **refines** [[concepts/cofitness-versus-coregulation]] by suggesting that multi-gene coordinated regulation can leave a detectable inheritance signature, while the present analysis does not establish that co-inheritance is caused by regulation rather than other forms of functional coupling. [src: cofitness_coinheritance]

## Heterogeneity across organisms

Module-level enrichment varied substantially among organisms. [src: cofitness_coinheritance] Koxy had 44 modules, 14 (32%) significant, mean phi=0.079, and null mean=0.040; Btheta had 36 modules, 22 (61%) significant, mean phi=0.192, and null mean=0.086; Putida had 38 modules, 6 (16%) significant, mean phi=0.266, and null mean=0.202; Korea had 29 modules, 0 (0%) significant, mean phi=0.357, and null mean=0.308; Phaeo had 37 modules, 3 (8%) significant, mean phi=0.108, and null mean=0.095; and pseudo3_N2E3 had 40 modules, 4 (10%) significant, mean phi=0.444, and null mean=0.409. [src: cofitness_coinheritance]

Btheta showed the strongest module-level signal, whereas Korea had no significant modules because all Korea modules were greater than 90% core with prevalence near 1.0. [src: cofitness_coinheritance] These results **support** [[concepts/condition-space-dimensionality]] only indirectly: the observed variation is organism-dependent, but this study did not test environmental condition space as a causal explanation. [src: cofitness_coinheritance]

## Phylogenetic and prevalence constraints

Cofit-pair phi was higher among near genomes than medium-distance genomes, with mean=0.102 versus mean=0.067, consistent with shared ancestry. [src: cofitness_coinheritance] Most species lacked genomes in the far stratum (>0.05 branch distance), limiting separation of functional coupling from phylogenetic signal. [src: cofitness_coinheritance] Phylogenetic stratification was available for 7 of 9 organisms, so the stronger module signal should not be treated as independent of evolutionary relatedness without additional controls. [src: cofitness_coinheritance]

The prevalence ceiling is especially important because most Fitness Browser genes mapped to core clusters (>95% prevalence), where phi approaches 0 for both cofit and random pairs. [src: cofitness_coinheritance] The analysis is therefore most informative for species with substantial auxiliary gene content, and the stronger accessory-module result should be interpreted as evidence from the variable part of the pangenome rather than as a uniform property of all genes. [src: cofitness_coinheritance] Near-clonal organisms nevertheless retained detectable signals: Ddia6719 had ANI 99.47% and delta=+0.093, while pseudo3_N2E3 had ANI 99.66% and delta=+0.026. [src: cofitness_coinheritance]

## Implications for pangenome integration

The study **supports** [[concepts/pangenome-integration]] by showing that linked functional-fitness and pangenome data can test whether laboratory relationships correspond to population-level gene co-occurrence. [src: cofitness_coinheritance] It also **supports** [[concepts/cross-tenant-data-bridging]] because the analysis joined Fitness Browser data, KBase pangenome clusters, phylogenetic distances, ICA modules, and SEED annotations through linked files and Spark extraction. [src: cofitness_coinheritance]

The result does not establish that co-fitness causes co-inheritance, because shared ancestry, prevalence structure, genome architecture, horizontal transfer, and other forms of functional coupling can produce correlated presence patterns. [src: cofitness_coinheritance] Instead, the evidence supports a narrower conclusion: in this dataset, coordinated module membership was more strongly associated with pangenome co-occurrence than pairwise co-fitness, particularly for accessory modules. [src: cofitness_coinheritance]

## Open Directions

- Restrict the pairwise and module analyses to auxiliary-only pairs in which both clusters are below 95% prevalence, then test whether the module advantage persists after removing the prevalence ceiling. [src: cofitness_coinheritance]
- Calculate co-fitness directly from raw genefitness data for Ralstonia UW163 and Ralstonia GMI1000, then repeat the module and pairwise comparisons to recover the two organisms excluded because they had zero precomputed co-fitness data. [src: cofitness_coinheritance]
- Resolve reference-genome mapping and apply stronger phylogenetic controls, then test whether module-level delta phi remains higher than pairwise delta phi after ancestry is accounted for. [src: cofitness_coinheritance]
- Build module co-transfer networks and test cross-module prediction to determine whether modules predict one another’s pangenome distributions beyond within-module co-occurrence. [src: cofitness_coinheritance]
- Expand the analysis to species with >30% auxiliary genes and existing co-fitness data, then test whether auxiliary-gene fraction predicts the size and reproducibility of the module-level signal. [src: cofitness_coinheritance]
