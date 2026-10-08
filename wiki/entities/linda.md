---
type: "Method"
description: "LinDA, a compositional differential-abundance method (linear CLR regression with bias correction) used in this corpus as the second-method concordance check for gut-microbiome differential-abundance calls."
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md"]
---
# LinDA

LinDA is a compositional differential-abundance (DA) method — differential abundance being the test of whether a taxon's abundance differs between sample groups — described as "linear CLR regression with bias correction", where CLR is the centered log-ratio transform of compositional abundances. Its primary reference is Zhou H, He K, Chen J, Zhang X. (2022), "LinDA: linear models for differential abundance analysis of microbiome compositional data," *Genome Biology* 23(1):95, PMID: 35421994 [src: ibd_phage_targeting].

## Aliases and identifiers

- Names used in this corpus: "LinDA", "Zhou et al. 2022, pure-Python" [src: discoveries]
- Described in the corpus as "linear CLR regression with bias correction"; primary reference *Genome Biology* 23(1):95, PMID: 35421994 [src: ibd_phage_targeting]

## Role as a second differential-abundance method

In the IBD phage-targeting project LinDA served as the second compositional DA method alongside CLR plus Mann–Whitney testing (see [[entities/mann-whitney-u-test]]) in notebook section NB04c §4, and was implemented in pure NumPy for that project — a pure-Python implementation chosen to avoid an R/rpy2 dependency [src: ibd_phage_targeting].

The same project reports reproducing the compositional-bias result directly on a curated battery, following work establishing that raw Mann-Whitney testing on relative abundance is systematically biased by the sum-to-constant constraint, and introduces LinDA as the simple pure-Python-implementable alternative used as the second-method concordance check in NB04c §4 — this **supports** the argument on [[concepts/compositional-robustness-of-differential-abundance-calls]] that single-method relative-abundance calls need a compositional cross-check [src: ibd_phage_targeting].

As a repair for single-method DA, the second of the candidate-gating filters required LinDA to show CD↑ (enrichment in Crohn's disease samples) with FDR < 0.10 — FDR, the false discovery rate, being the expected share of false positives among the calls declared significant (see [[entities/benjamini-hochberg-fdr]]) — in the same ecotype [src: discoveries].

Three of 15 candidates passed all three filters in ecotype E3, and were designated the trustworthy Tier-A set [src: discoveries]:

- [[entities/mediterraneibacter-gnavus]] — within-substudy CD↑ +5.13, LinDA E3 +1.64 [src: discoveries]
- [[entities/flavonifractor-plautii]] — within-substudy +1.89, LinDA +2.91 [src: discoveries]
- blautia wexlerae — within-substudy +0.91, LinDA +2.00 [src: discoveries]

## Caveats on its evidential weight

LinDA as deployed here does not satisfy the originally planned consensus design: the plan called for ≥ 2 / 3 of {ANCOM-BC, MaAsLin2, LinDA} methods to agree, and LinDA was implemented in pure Python (NB04c §4) to avoid the R/rpy2 dependency, so the planned three-method consensus was not implemented and a full three-method R-native consensus is flagged as a publication-grade follow-up [src: ibd_phage_targeting]. The phrase "additional independent evidence streams" is applied in the source only to the NB04c bootstrap-CI and NB04e within-substudy-meta outputs, not to LinDA, and even those outputs "are not drop-in ANCOM-BC / MaAsLin2 substitutes"; the source's wording is itself in tension on this point, since the consensus discussion calls the bootstrap-CI output an additional independent evidence stream while the project's leakage caveat states that bootstrap + LinDA are not independent evidence streams [src: ibd_phage_targeting].

LinDA also shares, rather than breaks, the key bias of the primary method: bootstrap-stable within-ecotype DA and LinDA (NB04c) operate on the same ecotype-defined subsamples as CLR–Mann-Whitney (NB04) and therefore share the selection-on-outcome bias (see [[concepts/selection-on-outcome-leakage]]), so only the within-substudy CD-vs-nonIBD contrast (NB04c §3, NB04e) is an independent evidence source — which is why the NB04d Tier-A gating requires within-substudy concordance, precisely because bootstrap + LinDA are not independent evidence streams [src: ibd_phage_targeting].
