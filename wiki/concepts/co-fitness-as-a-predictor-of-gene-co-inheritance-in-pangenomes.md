---
type: "Concept"
description: "Whether gene pairs with correlated lab fitness profiles (co-fitness) co-occur across genomes more than prevalence-matched random pairs, including per-organism effect sizes; stops at module-level and phylogenetic questions."
sources: ["summaries/cofitness_coinheritance__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md"]
---
# Co-fitness as a predictor of gene co-inheritance in pangenomes

Pairs of genes with correlated lab fitness profiles (co-fitness) co-occur across genomes only slightly more often than prevalence-matched random pairs. The evidence is a single report covering 9 organisms. The effect is consistent in direction but very small, and it varies by organism. [src: cofitness_coinheritance]

## Literature Context

Phylogenetic profiling, the detection of genes that co-occur across genomes, is an established way to infer functional associations between genes. PhyloCorrelate applied it in all-by-all comparisons across the bacterial tree of life, using metrics that account for phylogenetic history. It linked genes with overlapping GO terms and KEGG pathways, and it produced functional predictions for many proteins of unknown function [PMID 33416870](https://pubmed.ncbi.nlm.nih.gov/33416870/). An earlier map of gene-gene co-occurrence across about 600 bacterial species found that co-occurring genes (correlogs) were highly enriched for physically interacting proteins and for co-expressed transcripts. That study removed indirect correlations before scoring [PMID 22219725](https://pubmed.ncbi.nlm.nih.gov/22219725/). Both studies measured co-occurrence against external functional annotations. Neither tested it against lab fitness profiles.

Going beyond pairs, a study of 77 cyanobacterial genomes built networks of co-occurring ortholog clusters. It found modules with a high degree of functional coherence, and it attributed this to the similar-yet-diverse nature of cyanobacteria [PMID 29522508](https://pubmed.ncbi.nlm.nih.gov/29522508/). Co-occurrence is also used as a proxy for conserved interaction. In prokaryotes, transcription factor genes showed lower co-occurrence than other genes, which the authors read as fast evolution of regulation [PMID 25515977](https://pubmed.ncbi.nlm.nih.gov/25515977/). FunCoup 4 uses phylogenetic profiles as one of several evidence types in a naive Bayesian integration for functional association networks [PMID 29165593](https://pubmed.ncbi.nlm.nih.gov/29165593/).

The corpus finding is that co-fitness pairs co-occur only slightly more than prevalence-matched random pairs. The mean delta phi was +0.011 across 9 organisms, and the aggregate delta was +0.003. This is broadly consistent with the literature's premise that functionally coupled genes tend to co-occur, since the direction is positive in 7 of 9 organisms. The across-organism Wilcoxon test was not significant (W=9, p=0.13), and Putida was null. The literature above reports enrichment against annotation or interaction benchmarks, not an effect on a fitness-derived delta phi. The two sets of results are therefore stated separately, not compared by size. Using lab co-fitness as the functional reference and prevalence-matched random pairs as the null extends the field. I found no candidate paper that did this.

The corpus also adds a caveat. PhyloCorrelate emphasises that phylogenetic structure is hard to account for [PMID 33416870](https://pubmed.ncbi.nlm.nih.gov/33416870/). The corpus's pairwise test did not use a phylogeny-aware null, so its small positive delta may partly reflect population structure. The module-level co-inheritance reported in the linked pathway report is consistent with the module coherence in cyanobacteria [PMID 29522508](https://pubmed.ncbi.nlm.nih.gov/29522508/). The cyanobacterial study did not use fitness data, and it did not test whether that coherence survives the prevalence-matched null used here.

## Overall signal

The report compared 2,253,491 cofit pairs with 22,534,910 random pairs across 9 organisms. [src: cofitness_coinheritance] The mean cofit-minus-random delta phi was +0.011 across organisms. Seven of 9 organisms had a positive effect, and 8 of 9 were significant at p<0.05 (Mann-Whitney, two-sided). [src: cofitness_coinheritance] The aggregate delta was +0.003, with Mann-Whitney p=1.66e-29. [src: cofitness_coinheritance] Overall mean phi was 0.092 for cofit pairs and 0.089 for random pairs. [src: cofitness_coinheritance]

The small effect indicates that lab-measured functional coupling explains only a tiny fraction of co-inheritance patterns. [src: cofitness_coinheritance] The across-organism Wilcoxon signed-rank test was not significant (W=9, p=0.13), which the report attributes to high inter-organism variance. [src: cofitness_coinheritance] The aggregate p-value is therefore very small, while the across-organism test is not significant. [src: cofitness_coinheritance]

Only 0.7% of cofit pairs were adjacent within 5 genes. Excluding them did not change the result pattern. [src: cofitness_coinheritance]

## Per-organism effect sizes

Effects range from clearly positive in Ddia6719 to null or negative in Putida and Korea. [src: cofitness_coinheritance] The table gives mean phi for cofit and random pairs per organism.

| Organism | Cofit pairs | Cofit phi | Random phi | Delta | p |
|---|---|---|---|---|---|
| Ddia6719 | 16,957 | 0.182 | 0.089 | +0.093 | <1e-300 [src: cofitness_coinheritance] |
| pseudo3_N2E3 | 31,959 | 0.458 | 0.433 | +0.026 | 6.6e-16 [src: cofitness_coinheritance] |
| Phaeo | 14,728 | 0.231 | 0.222 | +0.009 | 6.5e-4 [src: cofitness_coinheritance] |
| SyringaeB728a | 129,385 | 0.049 | 0.043 | +0.006 | 2.9e-4 [src: cofitness_coinheritance] |
| Koxy | 162,160 | 0.041 | 0.038 | +0.003 | 3.3e-2 [src: cofitness_coinheritance] |
| Smeli | 230,516 | 0.029 | 0.026 | +0.002 | <1e-17 [src: cofitness_coinheritance] |
| Btheta | 242,676 | 0.067 | 0.067 | +0.001 | <1e-6 [src: cofitness_coinheritance] |
| Putida | 205,323 | 0.171 | 0.171 | -0.000 | 0.41 [src: cofitness_coinheritance] |
| Korea | 7,994 | 0.447 | 0.489 | -0.042 | <1e-6 [src: cofitness_coinheritance] |

Putida showed no difference, a null result. [src: cofitness_coinheritance] Korea's negative delta is not read as biology. Only about 8,000 of 166,601 Korea pairs were computable, and the report attributes the delta to statistical noise in that small effective sample. [src: cofitness_coinheritance]

### Gene-content diversity and near-clonal species

Species with more gene-content diversity (Ddia6719, pseudo3_N2E3) show the largest positive deltas. [src: cofitness_coinheritance] Ddia6719 (ANI 99.47%, average nucleotide identity) shows the strongest signal, even though it is near-clonal. [src: cofitness_coinheritance] pseudo3_N2E3 (ANI 99.66%) also shows a positive delta. [src: cofitness_coinheritance] Despite low overall genome diversity, these species have enough accessory gene variation to detect co-inheritance. [src: cofitness_coinheritance] Their high baseline phi makes absolute phi values less interpretable. [src: cofitness_coinheritance] The analysis is most informative for species with substantial auxiliary gene content. [src: cofitness_coinheritance] See also [[entities/pseudomonas-fluorescens-fw300-n2e3]], pseudomonas putida, [[entities/bacteroides-thetaiotaomicron]], [[entities/klebsiella-michiganensis]], [[entities/pseudomonas-syringae-b728a]] and [[entities/sinorhizobium-meliloti]].

## Co-fitness strength

Stronger co-fitness scores weakly predicted lower phi (Spearman rho=-0.109, p<1e-300 across 1.04M pairs). [src: cofitness_coinheritance] The report suggests this is a prevalence ceiling effect. The strongest co-fitness pairs are core genes with near-universal prevalence, which leaves little variance for detecting co-occurrence. [src: cofitness_coinheritance] See [[concepts/core-gene-prevalence-ceiling-on-co-occurrence-signal]].

## Link to module-level work

A separate report treats the finding that 73% of accessory modules show co-inheritance with co-fitness as validation of pathway-level fitness aggregation. [src: pathway_capability_dependency] See [[concepts/conservation-of-cofitness-modules-across-genomes-and-organisms]], [[concepts/phylogenetic-confounding-of-gene-co-occurrence]], [[summaries/cofitness_coinheritance__REPORT]] and [[summaries/pathway_capability_dependency__REPORT]].

## Open Directions

- Repeat the pairwise test with a phylogeny-aware null, such as pairs matched on both prevalence and tree distance. This would show whether the small positive delta survives population structure.
- Stratify pairs by prevalence, for example accessory-only against core. This would test the prevalence-ceiling explanation for the negative rho.
- Add organisms with large accessory genomes. This would test whether gene-content diversity predicts effect size.
- Recompute Korea with more genomes or a better-powered statistic. This would tell noise from a true null.
