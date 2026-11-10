---
type: "Finding"
description: "A variational-Bayes binomial mixed model with phylum and family random intercepts yielded an approximately 143:1 xoxF:mxaF ratio (95% credible interval [122, 169]), and a bootstrap equally weighting 271 informative families yielded 0.960 [0.941, 0.976]."
finding_id: "lanthanide_methylotrophy_atlas--4129a02d"
result: "observation"
source: "lanthanide_methylotrophy_atlas"
quantities: [{"value": "~143 : 1", "what": "phylogeny-corrected xoxF:mxaF ratio from the binomial mixed model", "unit": "ratio", "denominator": "", "scope": "random intercepts for phylum and family; 95% credible interval [122, 169]"}, {"value": "0.960", "what": "xoxF fraction with each of 271 MDH-informative GTDB families weighted equally", "unit": "fraction", "denominator": "271 families", "scope": "95% CI [0.941, 0.976]"}]
caveat: "eggNOG and bakta calls disagree substantially for several markers (xoxJ, lanmodulin, PQQ biosynthesis); headline statistics use the calibrated source per marker, with secondary union-of-sources analyses."
first_added: "2026-10-27"
source_hash: "4c006958be98f494be09edfff08176308c57490b4b48dc38c5753450c3d8e304"
---
# xoxF dominance holds under several phylogeny-aware corrections, strongest in the mixed model

A variational-Bayes binomial mixed model with phylum and family random intercepts yielded an approximately 143:1 xoxF:mxaF ratio (95% credible interval [122, 169]), and a bootstrap equally weighting 271 informative families yielded 0.960 [0.941, 0.976]. [src: lanthanide_methylotrophy_atlas]

## Key figures

- **~143 : 1 ratio**: phylogeny-corrected xoxF:mxaF ratio from the binomial mixed model (scope random intercepts for phylum and family; 95% credible interval [122, 169]) [src: lanthanide_methylotrophy_atlas]
- **0.960 fraction**: xoxF fraction with each of 271 MDH-informative GTDB families weighted equally (denominator 271 families; scope 95% CI [0.941, 0.976]) [src: lanthanide_methylotrophy_atlas]

## Evidence

> The GLMM (variational-Bayes binomial GLMM via `statsmodels.BinomialBayesMixedGLM`, with random intercepts for phylum and family) gives the *strongest* xoxF dominance signal — a phylogeny-corrected ratio of **~143 : 1** with 95% credible interval [122, 169] — because the random effects absorb phylum-level heterogeneity and reveal that *within typical phyla*, xoxF dominance is more extreme than the global pooled estimate suggests. The family-equal-weight bootstrap (each of 271 MDH-informative GTDB families counted once regardless of genome count) gives 0.960 [0.941, 0.976], confirming H1 is not driven by Pseudomonadota's 117 K-genome size advantage. **H1 is robust to all three phylogenetic-correction frameworks.** [src: lanthanide_methylotrophy_atlas]

From the report [[summaries/lanthanide_methylotrophy_atlas__REPORT]].

## Caveat

eggNOG and bakta calls disagree substantially for several markers (xoxJ, lanmodulin, PQQ biosynthesis); headline statistics use the calibrated source per marker, with secondary union-of-sources analyses. [src: lanthanide_methylotrophy_atlas]

> eggNOG and bakta calls disagree substantially for several markers (xoxJ, lanmodulin, PQQ biosynthesis). Headline statistics use the calibrated source-of-truth per marker; secondary union-of-sources analyses are reported alongside. [src: lanthanide_methylotrophy_atlas]

## Other caveats in this report

- The initial per-phylum binomial framework did not formally control phylogenetic non-independence; the report describes three subsequent validation strategies. [src: lanthanide_methylotrophy_atlas]
- Environmental associations used per-class Fisher exact tests for any xoxF against a generic-environmental reference, with Benjamini–Hochberg correction. [src: lanthanide_methylotrophy_atlas]
- The REE-impacted class had only 37 genomes; its 10.81% xoxF rate and odds ratio 3.51 were descriptive, with adjusted p value 0.082. [src: lanthanide_methylotrophy_atlas]
- The report grades H2 as partially supported: soil/sediment and marine enrichment and host-associated depletion passed its correction, while the n=37 REE-impacted elevation did not pass the false-discovery-rate threshold (p_BH = 0.082). [src: lanthanide_methylotrophy_atlas]
- Of 2,185 genomes with no eggNOG pqq, 1,288 (59%) had at least one bakta PQQ product. The other 897 (24% of all xoxF carriers) lacked evidence in both sources; assembly incompleteness, pseudogenization, and community-acquired PQQ remain unresolved without sequence-level inspection. [src: lanthanide_methylotrophy_atlas]
