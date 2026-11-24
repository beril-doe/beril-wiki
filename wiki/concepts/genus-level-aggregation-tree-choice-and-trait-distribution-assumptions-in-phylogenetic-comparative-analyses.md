---
type: "Concept"
description: "Methodological choices in PGLS and Pagel's lambda analyses: reference tree, genus pruning, count-trait distribution, row ordering; stops at specific biological findings."
sources: ["summaries/gene_function_ecological_agora__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md"]
---
# Genus-level aggregation, tree choice and trait distribution assumptions in phylogenetic comparative analyses

This page covers methodological choices in PGLS (phylogenetic generalized least squares) and Pagel's λ analyses: reference tree, genus pruning, count-trait distribution and row ordering.

The metal-ecology report ran all of its analyses on one GTDB tree and did not test other trees. [src: microbeatlas_metal_ecology] Its one direct test is a synthetic-data check showing that row order matters. [src: microbeatlas_metal_ecology] The gene-function report adds an argument about non-independence. [src: gene_function_ecological_agora] See [[summaries/microbeatlas_metal_ecology__REPORT]] and [[summaries/gene_function_ecological_agora__REPORT]].

## Literature Context

The candidate papers speak to the general behaviour of phylogenetic comparative methods. They do not address microbial genus-level trees or integer count traits. Simulation work found that most comparative methods, including phylogenetic generalized least squares (PGLS), performed well even when their Brownian-motion assumptions were violated. Felsenstein's independent contrasts did best in many cases. They were biased when strong constraints opposed the variance-generating forces. Estimates from different methods were occasionally very different from one another, so the choice among them should depend on the trait and the evolutionary process [PMID 11913655](https://pubmed.ncbi.nlm.nih.gov/11913655/). Ignoring phylogeny gave poor correlation estimates that were never substantially better than the other methods [PMID 11913655](https://pubmed.ncbi.nlm.nih.gov/11913655/).

The papers also show that tree and signal assumptions can change conclusions. In mammalian metabolic scaling, assuming no phylogenetic signal or a strong one gave allometric slopes that were erroneous in 30% and 50% of cases, respectively. The authors conclude that estimating the signal is essential [PMID 20957970](https://pubmed.ncbi.nlm.nih.gov/20957970/). A study of flight-initiation distance in 41 bird species ran PGLS on five phylogenetic hypotheses. Analyses that assumed strong signal differed substantially between trees, whereas the estimated signal was absent and gave results equivalent to ordinary least squares [PMID 24637884](https://pubmed.ncbi.nlm.nih.gov/24637884/). A gorilla pelvic-shape study found no significant elevation relationship under any phylogenetic assumption. It suggested that the covariation depends on those assumptions [PMID 31669913](https://pubmed.ncbi.nlm.nih.gov/31669913/). A Bayesian extension of PGLS can carry uncertainty about the tree, evolutionary regimes and other parameters into the inference. Its abstract reports good inferential properties and predictive performance [PMID 31849034](https://pubmed.ncbi.nlm.nih.gov/31849034/). Work on non-independence among populations within species argues that mixed models can incorporate both shared ancestry and gene flow [PMID 21444315](https://pubmed.ncbi.nlm.nih.gov/21444315/).

The metal-ecology report's single-tree design, which uses the GTDB r214 genus-representative tree, is consistent with the cautions in this literature. The report itself flags the lack of tree-sensitivity testing as a gap. The bird and gorilla studies suggest that this gap could matter, because conclusions can shift with the tree. Those studies are on vertebrates, though, so this is a hypothesis for the microbial data and not a demonstrated result. The report's Gaussian treatment of an integer predictor is not covered by any candidate paper. The same is true of its synthetic-data finding that unsorted row order breaks PGLS, which we regard as novel to this corpus. Its Brownian-motion λ for metal_types is likewise unaddressed. The simulation evidence that PGLS is fairly robust to violated assumptions [PMID 11913655](https://pubmed.ncbi.nlm.nih.gov/11913655/) gives only indirect support, since it concerned continuous traits.

The gene-function report's argument that per-leaf Sankoff parsimony already encodes tree structure, and its replacement of PIC with a UniRef cluster bootstrap, are not tested by any candidate. The related point that PIC may be a poor fit when its assumptions fail is loosely consistent with the reported bias of independent contrasts under strong constraints [PMID 11913655](https://pubmed.ncbi.nlm.nih.gov/11913655/). Those corpus choices therefore extend the literature and have no direct external validation here.

## Reference tree

All PGLS and Pagel's λ analyses in the metal-ecology report use the [[entities/gtdb]] r214 genus-representative tree, built from 120 concatenated marker genes. [src: microbeatlas_metal_ecology] The report calls this the current field standard for bacterial phylogenetics and the best available reconciliation of phylogenomic signal with 16S taxonomy. [src: microbeatlas_metal_ecology]

The report did not test sensitivity to NCBI trees, SILVA-based 16S trees or a different GTDB release. It names this as a known methodological gap. [src: microbeatlas_metal_ecology] A 16S-based tree would align more directly with the 16S-derived niche breadth values, but it has lower resolution at genus level. [src: microbeatlas_metal_ecology]

## Genus-level pruning

The report keeps one tip per genus, chosen as the GTDB species cluster representative. It calls this standard in macro-ecological PGLS studies of this scale. [src: microbeatlas_metal_ecology] The cost is that within-genus phylogenetic structure is discarded. [src: microbeatlas_metal_ecology]

## Count-trait distribution

Metal type diversity is an integer count from 1 to 7. The report enters it as a continuous z-scored predictor in a Gaussian PGLS. It calls this standard practice when the count is the predictor and not the response. [src: microbeatlas_metal_ecology] The Gaussian assumption applies to the residuals of B_std, not to the distribution of metal types, so the report says the PGLS residuals should be inspected for normality. [src: microbeatlas_metal_ecology]

The concern would be larger if metal types were the response. Poisson or negative binomial PGLS (`phylolm` with Poisson family, or `MCMCglmm`) would then be appropriate. [src: microbeatlas_metal_ecology] The report's Pagel's λ analysis of metal_types assumes Brownian motion with Gaussian increments, which approximates an integer trait. [src: microbeatlas_metal_ecology] Discrete-state Mk models or threshold models are alternatives, but they are not standard for this continuous-trait PGLS analysis. [src: microbeatlas_metal_ecology]

The report acknowledges the count-predictor issue as a limitation and proposes MCMCglmm as future work. [src: microbeatlas_metal_ecology] The proposed work applies MCMCglmm with Poisson or negative binomial family to test whether niche breadth predicts metal type count in the reverse regression direction. [src: microbeatlas_metal_ecology]

## Row ordering

PGLS was fitted jointly with λ by maximum likelihood (`ape::gls` with `nlme::corPagel`). Data were sorted to `tree$tip.label` order before fitting. [src: microbeatlas_metal_ecology] A unit test, `scripts/test_pgls_ordering.py`, generates synthetic data with λ = 0.8 and β = 0.05 and scrambles the row order. Sorted PGLS recovers the correct λ and β within tolerance, and unsorted PGLS fails. The test passes. [src: microbeatlas_metal_ecology]

## Non-independence: PIC versus cluster bootstrap

The gene-function report has not implemented PIC (phylogenetic independent contrasts) correction for phylogenetic non-independence. [src: gene_function_ecological_agora] PIC (method M9) was promoted to mandatory Phase 2 methodology in plan v2.4 but remained unimplemented. [src: gene_function_ecological_agora]

The report argues that classical Felsenstein PIC controls taxon non-independence on per-species traits. Sankoff parsimony (M16) is already tree-aware, because per-leaf parsimony (`gain_events / n_present_leaves`) encodes tree topology. [src: gene_function_ecological_agora]

The report instead identifies a residual concern at GTDB scale: UniRef-cluster non-independence. Several UniRef50s within a Pfam family inherit related phylogenetic distributions. A Mann-Whitney test across UniRefs then treats them as independent and identically distributed, which inflates the effective sample size. [src: gene_function_ecological_agora] It retires M9 on this rationale. [src: gene_function_ecological_agora] Plan v2.7 binds M19 in its place. M19 is a cluster bootstrap on UniRefs at Pfam-family granularity, with B = 200 resamples per function class. It recomputes per-leaf Sankoff Cohen's d under each bootstrap and reports a 95% CI (confidence interval). [src: gene_function_ecological_agora]

## Open Directions

- Refit the PGLS and Pagel's λ analyses on an NCBI tree, a SILVA-based 16S tree and a different GTDB release. This would close the untested tree-sensitivity gap. A 16S tree would also show whether matching the niche breadth data changes the results.
- Compare genus-representative pruning with species-level or multi-tip-per-genus trees. This would show how much within-genus structure matters.
- Inspect PGLS residuals for normality. Then fit the reverse regression with `MCMCglmm` or `phylolm` using Poisson or negative binomial families.
- Compare Brownian-motion λ for metal_types with Mk or threshold models. This would test how much the Gaussian approximation distorts the integer trait.
- Run the M19 Pfam-family cluster bootstrap. Then check whether the 95% CIs on per-leaf Sankoff Cohen's d support dropping PIC.
