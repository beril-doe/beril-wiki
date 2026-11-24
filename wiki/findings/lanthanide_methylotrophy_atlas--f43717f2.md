---
type: "Finding"
description: "The NB08 variational-Bayes binomial GLMM with random intercepts for phylum and family gives a phylogeny-corrected xoxF:mxaF ratio of ~143 : 1 with 95% credible interval [122, 169], which the report attributes to random effects absorbing phylum-level heterogeneity so that within typical phyla xoxF dominance is more extreme than the pooled estimate."
finding_id: "lanthanide_methylotrophy_atlas--f43717f2"
result: "inference"
source: "lanthanide_methylotrophy_atlas"
quantities: [{"value": "~143 : 1", "what": "phylogeny-corrected xoxF:mxaF ratio from GLMM", "unit": "", "denominator": "", "scope": ""}, {"value": "[122, 169]", "what": "95% credible interval", "unit": "", "denominator": "", "scope": ""}]
caveat: "The reviewer noted that the per-phylum binomial framework does not formally control for phylogenetic non-independence."
first_added: "2026-11-24"
source_hash: "4c006958be98f494be09edfff08176308c57490b4b48dc38c5753450c3d8e304"
---
# Phylogeny-corrected model suggests even stronger xoxF dominance within typical phyla

The NB08 variational-Bayes binomial GLMM with random intercepts for phylum and family gives a phylogeny-corrected xoxF:mxaF ratio of ~143 : 1 with 95% credible interval [122, 169], which the report attributes to random effects absorbing phylum-level heterogeneity so that within typical phyla xoxF dominance is more extreme than the pooled estimate. [src: lanthanide_methylotrophy_atlas]

## Key figures

- **~143 : 1**: phylogeny-corrected xoxF:mxaF ratio from GLMM [src: lanthanide_methylotrophy_atlas]
- **[122, 169]**: 95% credible interval [src: lanthanide_methylotrophy_atlas]

## Evidence

> The GLMM (variational-Bayes binomial GLMM via `statsmodels.BinomialBayesMixedGLM`, with random intercepts for phylum and family) gives the *strongest* xoxF dominance signal — a phylogeny-corrected ratio of **~143 : 1** with 95% credible interval [122, 169] — because the random effects absorb phylum-level heterogeneity and reveal that *within typical phyla*, xoxF dominance is more extreme than the global pooled estimate suggests. [src: lanthanide_methylotrophy_atlas]

From the report [[summaries/lanthanide_methylotrophy_atlas__REPORT]].

## Caveat

The reviewer noted that the per-phylum binomial framework does not formally control for phylogenetic non-independence. [src: lanthanide_methylotrophy_atlas]

> The reviewer (PLAN_REVIEW_1.md, REVIEW_1.md) noted that the per-phylum binomial framework does not formally control for phylogenetic non-independence. [src: lanthanide_methylotrophy_atlas]

## Other caveats in this report

- The report suggests that the 13/62 lanmodulin-without-xoxF genomes may reflect annotation incompleteness or genuine alternative lanthanide-handling pathways, since lanmodulin can bind REEs without co-location with a lanthanide-MDH operon. [src: lanthanide_methylotrophy_atlas]
- The report says REE-impacted samples show a 3.5-fold descriptive xoxF elevation (10.8 % vs 3.7 % baseline), but n=37 is too small to clear the FDR threshold (p_BH = 0.082). [src: lanthanide_methylotrophy_atlas]
- The 897 genomes (24 % of all xoxF carriers) lacking PQQ evidence from either source are candidates for assembly incompleteness, pseudogenization or community-acquired PQQ dependence, not established cases of any one explanation. [src: lanthanide_methylotrophy_atlas]
- Discriminating assembly incompleteness, pseudogenization and community-acquired PQQ dependence requires sequence-level inspection outside the report's scope. [src: lanthanide_methylotrophy_atlas]
- REE-AMD enrichment is descriptive-only at n=37, OR=3.51, p_BH=0.082, and a larger explicitly REE-impacted metagenome collection would test whether REE supply per se selects for the cassette. [src: lanthanide_methylotrophy_atlas]
