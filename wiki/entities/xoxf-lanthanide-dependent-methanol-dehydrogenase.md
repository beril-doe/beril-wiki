---
type: "Gene_Or_Pathway"
description: "Lanthanide-dependent PQQ methanol dehydrogenase (EC 1.1.2.8; KO K00114)."
sources: ["summaries/discoveries.md", "summaries/lanthanide_methylotrophy_atlas__REPORT.md"]
aliases: ["K00114", "xoxF"]
---
# XoxF lanthanide-dependent methanol dehydrogenase

XoxF is a lanthanide-dependent PQQ methanol dehydrogenase (EC 1.1.2.8), annotated as KEGG ortholog (KO) K00114. [src: lanthanide_methylotrophy_atlas] Across the KBase Data Lakehouse pangenome it is far more common than the calcium-dependent mxaF. [src: lanthanide_methylotrophy_atlas] The size of any xoxF count depends on the annotation source: 418 genomes are called by both eggNOG and bakta, 3,272 by eggNOG only and 1,402 by bakta only. [src: lanthanide_methylotrophy_atlas]

## Key facts

- eggNOG K00114 marks xoxF, and K14028 marks mxaF, Ca-dependent methanol dehydrogenase (EC 1.1.2.7). [src: lanthanide_methylotrophy_atlas]
- Among 293,059 GTDB-r214 genomes, xoxF is annotated in 3,690 genomes and mxaF in 195. [src: lanthanide_methylotrophy_atlas]
- The report places these ~3,690 xoxF-bearing genomes across diverse phyla, including Acidobacteriota, Gemmatimonadota, Bacteroidota and archaea. [src: lanthanide_methylotrophy_atlas]
- 102/209 *Methylobacterium* genomes carry xoxF, which the report calls consistent with the lanthanide-switch model. [src: lanthanide_methylotrophy_atlas] See also [[entities/methylobacterium-extorquens]].

## Prevalence relative to mxaF

xoxF outnumbers mxaF by approximately 19 : 1 across the pangenome. The directional verdict survives Benjamini-Hochberg false discovery rate (BH-FDR) correction across phyla. Several major phyla have zero mxaF annotations while carrying xoxF. [src: lanthanide_methylotrophy_atlas] The global ratio is 18.92 : 1, with a Clopper-Pearson 95% confidence interval (CI) of [13.07, 27.69]. [src: lanthanide_methylotrophy_atlas] The xoxF fraction of joint MDH calls is 0.9498 [95% CI 0.9425, 0.9558]. [src: lanthanide_methylotrophy_atlas] A one-sided binomial test against the pre-registered H1 threshold (xoxF fraction > 10/11 ≈ 0.909) gives p = 7.6 × 10⁻²², so the report treats H1 as strongly supported. [src: lanthanide_methylotrophy_atlas] A Bayesian binomial GLMM gives a phylogeny-corrected ratio of ~143 : 1. [src: lanthanide_methylotrophy_atlas] See [[concepts/taxonomic-distribution-and-relative-prevalence-of-xoxf-and-mxaf-methanol-dehydrogenases]].

## Annotation-source disagreement

Of 5,092 genomes carrying any xoxF marker, only 418 (8%) hit both eggNOG K00114 and bakta Lanthanide-dependent methanol dehydrogenase-family products. [src: discoveries] The hit-bearing matrix gives 418 genomes called by both sources, 3,272 by eggNOG only and 1,402 by bakta only. The report uses eggNOG K00114 as primary and bakta as a union. [src: lanthanide_methylotrophy_atlas]

The eggNOG-only set appears to include bakta entries labeled Putative dehydrogenase XoxF, which the report's regex missed. It also appears to include other generic dehydrogenases that hit K00114. [src: discoveries] The bakta-only set includes lanthanide-dependent ethanol dehydrogenase variants that the KEGG KO filter excludes. [src: discoveries]

For downstream analyses, the report recommends reporting results both ways, with eggNOG-K00114 as the primary set and either-source as the inclusive set. It also recommends disclosing the gap and never giving a single xoxF count without naming its source. [src: discoveries] See [[concepts/annotation-source-disagreement-and-coverage]] and [[concepts/annotation-based-gene-detection-limits-in-pangenome-trait-surveys]].
