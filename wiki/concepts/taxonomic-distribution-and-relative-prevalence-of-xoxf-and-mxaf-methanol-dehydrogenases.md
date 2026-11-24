---
type: "Concept"
description: "Global and per-phylum/family prevalence of lanthanide-dependent xoxF versus calcium-dependent mxaF across bacterial and archaeal genomes, including carriage in non-canonical methylotroph lineages and phylogeny-corrected comparisons; stops at environmental drivers and marker calibration."
sources: ["summaries/lanthanide_methylotrophy_atlas__REPORT.md"]
---
# Taxonomic Distribution and Relative Prevalence of xoxF and mxaF Methanol Dehydrogenases

This page covers how common xoxF (lanthanide-dependent methanol dehydrogenase) is relative to mxaF (calcium-dependent methanol dehydrogenase) across bacterial and archaeal genomes. The evidence comes from one report, the lanthanide methylotrophy atlas. It reports xoxF outnumbering mxaF by approximately 19 : 1 across 293,059 GTDB-r214 genomes. [src: lanthanide_methylotrophy_atlas] The report says the verdict holds under three validations, which include a naive pooled analysis and two analyses that take taxonomy into account. [src: lanthanide_methylotrophy_atlas] The report calls this the first pangenome-scale atlas of the cassette. [src: lanthanide_methylotrophy_atlas] See [[entities/xoxf-lanthanide-dependent-methanol-dehydrogenase]] and [[summaries/lanthanide_methylotrophy_atlas__REPORT]].

## Global prevalence

The report presents this as the first quantitative test of the hypothesis that lanthanide-dependent oxidation has displaced the calcium-dependent pathway. [src: lanthanide_methylotrophy_atlas] In 293,059 genomes, xoxF (KEGG K00114, EC 1.1.2.8) is annotated in 3,690 genomes and mxaF (K14028, EC 1.1.2.7) in 195 genomes. That gives a ratio of 18.92 : 1 with Clopper-Pearson 95% CI [13.07, 27.69]. [src: lanthanide_methylotrophy_atlas] The xoxF fraction of joint calls is 0.9498 [95% CI 0.9425, 0.9558]. [src: lanthanide_methylotrophy_atlas] A one-sided binomial test against the pre-registered threshold (xoxF fraction > 10/11 ≈ 0.909) gives p = 7.6 × 10⁻²². [src: lanthanide_methylotrophy_atlas] The report calls this the first numerical answer at scale [src: lanthanide_methylotrophy_atlas], and says it confirms Chistoserdova's hypothesis at larger scale. [src: lanthanide_methylotrophy_atlas] It also says the survey supports Pol et al.'s claim that XoxF is the more widespread enzyme. [src: lanthanide_methylotrophy_atlas]

## Phylogeny-corrected comparisons

The report concedes that its per-phylum binomial framework does not formally control phylogenetic non-independence. [src: lanthanide_methylotrophy_atlas] It therefore ran three validations: a naive pooled analysis, a family-equal-weight bootstrap, and a Bayesian binomial GLMM (generalised linear mixed model) with phylum and family random intercepts. [src: lanthanide_methylotrophy_atlas] All three give lower confidence bounds above the 10 : 1 threshold, and the report concludes that H1 is robust to all three. [src: lanthanide_methylotrophy_atlas]

| Method | Units | xoxF fraction | Interval |
|---|---|---|---|
| NB03 naive pooled (genome-level) | 3,885 | 0.950 | [0.942, 0.956] [src: lanthanide_methylotrophy_atlas] |
| NB08 family-level equal-weight | 271 | 0.960 | [0.941, 0.976] [src: lanthanide_methylotrophy_atlas] |
| NB08 Bayesian GLMM | 3,885 | 0.993 | [0.992, 0.994] [src: lanthanide_methylotrophy_atlas] |

The equal-weight bootstrap counts each of 271 MDH-informative families once. It shows the result is not driven by Pseudomonadota's 117 K-genome size advantage. [src: lanthanide_methylotrophy_atlas] The GLMM gives a phylogeny-corrected ratio of ~143 : 1, 95% credible interval [122, 169]. [src: lanthanide_methylotrophy_atlas] The report attributes this larger figure to random effects absorbing phylum-level heterogeneity, so that xoxF dominance within typical phyla is more extreme than the pooled estimate. [src: lanthanide_methylotrophy_atlas] This is the report's explanation, not a separate measurement.

## Per-phylum patterns

After BH-FDR (Benjamini-Hochberg false discovery rate) correction across 29 testable phyla, the directional verdict survives in every phylum with MDH calls and adequate sample size. [src: lanthanide_methylotrophy_atlas] Several phyla are xoxF-only with zero mxaF: Bacteroidota, Cyanobacteriota, Chloroflexota, Planctomycetota, Campylobacterota, Actinomycetota, and the archaeal lineages Halobacteriota and Thermoproteota. [src: lanthanide_methylotrophy_atlas] The report places ~3,690 xoxF-bearing genomes across diverse phyla, including Acidobacteriota, Gemmatimonadota, Bacteroidota and archaea. [src: lanthanide_methylotrophy_atlas]

| Phylum | Genomes | xoxF | mxaF | xoxF rate | xoxF:mxaF | p_BH |
|---|---|---|---|---|---|---|
| Pseudomonadota | 117,619 | 2,988 | 171 | 2.5 % | 17.5 : 1 | 0.0 [src: lanthanide_methylotrophy_atlas] |
| Acidobacteriota | 1,006 | 285 | 3 | 28.3 % | 95 : 1 | 1.2 × 10⁻⁷⁹ [src: lanthanide_methylotrophy_atlas] |
| Gemmatimonadota | 386 | 98 | 1 | 25.4 % | 98 : 1 | 1.5 × 10⁻²⁷ [src: lanthanide_methylotrophy_atlas] |
| Methylomirabilota | 80 | 23 | 7 | 28.7 % | 3.3 : 1 | 0.011 [src: lanthanide_methylotrophy_atlas] |
| Verrucomicrobiota | 2,440 | 19 | 5 | 0.78 % | 3.8 : 1 | 0.015 [src: lanthanide_methylotrophy_atlas] |

## Carriage outside the methylotroph canon

The highest per-genome xoxF rates fall in phyla rarely linked to one-carbon metabolism in textbook accounts. [src: lanthanide_methylotrophy_atlas] These are Acidobacteriota (28 %), Gemmatimonadota (25 %) and Methylomirabilota (29 %). [src: lanthanide_methylotrophy_atlas] See also [[entities/acidobacteria]]. The report reads this as widening the candidate set of free-living lanthanide-utilising organisms beyond classical methylotrophs. [src: lanthanide_methylotrophy_atlas] That reading is an interpretation of annotation counts.

Canonical methylotroph families are enriched in xoxF as well. Beijerinckiaceae has 171 xoxF genomes in 508, a 33.7 % rate. [src: lanthanide_methylotrophy_atlas] Hyphomicrobiaceae has 33 in 56, a 58.9 % rate. [src: lanthanide_methylotrophy_atlas] The report states that the per-genome rate is highest in Acidobacteriota and Gemmatimonadota, but these are phylum-level rates and the family rates are not directly comparable to them. [src: lanthanide_methylotrophy_atlas] Within Pseudomonadota, Pseudomonadaceae alone contributes 566 xoxF genomes versus 1 mxaF. [src: lanthanide_methylotrophy_atlas] Xanthobacteraceae (Bradyrhizobium) and Rhizobiaceae (Mesorhizobium) follow. [src: lanthanide_methylotrophy_atlas] In Methylobacterium, 102/209 genomes carry xoxF, which the report calls consistent with the lanthanide-switch model. [src: lanthanide_methylotrophy_atlas] See [[entities/methylobacterium-extorquens]].

## Open Directions

- Rerun the comparison with a tree-based method, such as phylogenetic generalised least squares on the GTDB tree. This would test whether the GLMM's ~143 : 1 figure holds when phylogeny is modelled explicitly, since the report's correction used only taxonomic random effects. See [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]].
- Check the xoxF-only phyla for mxaF with a sequence-based search. This would show whether the zero mxaF counts reflect real absence or annotation gaps.
- Look in Acidobacteriota and Gemmatimonadota for the other parts of the lanthanide cassette, to see whether xoxF calls there indicate lanthanide use.
- Resolve Methylomirabilota (3.3 : 1) and Verrucomicrobiota (3.8 : 1) with more genomes, since their ratios are far below the global value.
