---
type: Gene_Or_Pathway
description: REE-dependent methanol dehydrogenase marker
sources:
- id: lanthanide_methylotrophy_atlas
  resource: ../summaries/lanthanide_methylotrophy_atlas__REPORT.md
  title: lanthanide methylotrophy atlas
title: xoxF
---
# xoxF

## What it is

**Canonical name:** xoxF. **Known aliases:** eggNOG K00114; EC 1.1.2.8; xoxF, the gene encoding a rare-earth-element-dependent methanol dehydrogenase marker. [^lanthanide_methylotrophy_atlas] A stable external identifier for this entity is eggNOG K00114; the associated enzyme classification is EC 1.1.2.8. [^lanthanide_methylotrophy_atlas] xoxF annotation indicates a candidate marker for lanthanide-dependent methanol oxidation, but its presence alone does not establish enzyme activity or methylotrophic physiology. [^lanthanide_methylotrophy_atlas]

## Evidence from the lanthanide methylotrophy atlas

The atlas detected eggNOG K00114 in 3,690 genomes, compared with 195 genomes containing K14028 for [mxaf](mxaf.md), giving an xoxF:mxaF ratio of 18.92:1 with a Clopper–Pearson 95% confidence interval of [13.07, 27.69]. [^lanthanide_methylotrophy_atlas] xoxF represented 0.9498 of joint xoxF plus mxaF calls, with a 95% confidence interval of [0.9425, 0.9558], and a one-sided binomial test against an xoxF fraction of 10/11 ≈ 0.909 gave p = 7.6 × 10⁻²². [^lanthanide_methylotrophy_atlas]

The xoxF-dominance result was retained after Benjamini–Hochberg false-discovery-rate correction across 29 testable phyla in every phylum with methanol dehydrogenase calls and adequate sample size. [^lanthanide_methylotrophy_atlas] Three phylogenetic validations reported xoxF fractions of 0.950 [95% CI 0.942, 0.956] under naive genome-level pooling, 0.960 [95% CI 0.941, 0.976] with equal weighting across 271 informative GTDB families, and 0.993 [95% CI 0.992, 0.994] under a Bayesian binomial generalized linear mixed model with phylum and family random intercepts. [^lanthanide_methylotrophy_atlas] The phylogeny-corrected model corresponded to an approximately 143:1 xoxF:mxaF ratio with a 95% credible interval of [122, 169]. [^lanthanide_methylotrophy_atlas]

High-rate xoxF carriers occurred beyond canonical methylotroph lineages. [acidobacteria](acidobacteria.md) contained 285 xoxF genomes and 3 mxaF genomes among 1,006 genomes, corresponding to a 28.3% xoxF rate, a 95:1 xoxF:mxaF ratio, and p_BH = 1.2 × 10⁻⁷⁹. [^lanthanide_methylotrophy_atlas] [gemmatimonadota](gemmatimonadota.md) contained 98 xoxF genomes and 1 mxaF genome among 386 genomes, corresponding to a 25.4% xoxF rate, a 98:1 ratio, and p_BH = 1.5 × 10⁻²⁷. [^lanthanide_methylotrophy_atlas] Methylomirabilota contained 23 xoxF genomes and 7 mxaF genomes among 80 genomes, corresponding to a 28.7% xoxF rate, a 3.3:1 ratio, and p_BH = 0.011. [^lanthanide_methylotrophy_atlas]

[pseudomonadota](pseudomonadota.md) contained 2,988 xoxF genomes and 171 mxaF genomes among 117,619 genomes, corresponding to a 2.5% xoxF rate and a 17.5:1 ratio. [^lanthanide_methylotrophy_atlas] Within Pseudomonadota, Pseudomonadaceae contributed 566 xoxF genomes versus 1 mxaF genome, Beijerinckiaceae had 171 xoxF genomes among 508 genomes for a 33.7% rate, and Hyphomicrobiaceae had 33 xoxF genomes among 56 genomes for a 58.9% rate. [^lanthanide_methylotrophy_atlas] Bacteroidota, Cyanobacteriota, Chloroflexota, Planctomycetota, Campylobacterota, Actinomycetota, Halobacteriota, and Thermoproteota had xoxF calls but zero mxaF annotations. [^lanthanide_methylotrophy_atlas]

## Environmental associations and functional context

Among environmental classes, soil_sediment contained 13,779 genomes and had a 6.84% xoxF rate, with enrichment relative to generic_environmental of OR = 1.92 and p_BH = 6.1 × 10⁻³⁹. [^lanthanide_methylotrophy_atlas] Marine environments contained 15,554 genomes and had a 4.76% xoxF rate, OR = 1.31, and p_BH = 7.8 × 10⁻⁷, whereas the generic_environmental reference contained 21,538 genomes with a 3.69% rate. [^lanthanide_methylotrophy_atlas] Within Acidobacteriota, soil_sediment enrichment remained significant with OR = 2.16 and p_BH = 2.2 × 10⁻⁵. [^lanthanide_methylotrophy_atlas] These results connect xoxF distribution to [environment-embedding-geography](../concepts/environment-embedding-geography.md) and broader [pangenome-integration](../concepts/pangenome-integration.md). [^lanthanide_methylotrophy_atlas]

Of 2,320 xoxF-bearing genomes initially lacking any eggNOG PQQ-biosynthesis annotation, 33 had complete eggNOG pqqA-E calls, 1,472 had partial eggNOG PQQ calls covering 1–4 of A–E, 899 had Bakta-only strong evidence with at least 3 PQQ products, 389 had Bakta-only partial evidence with 1–2 PQQ products, and 897 had no PQQ detected by either source. [^lanthanide_methylotrophy_atlas] Of 2,185 genomes with no eggNOG PQQ annotation, 1,288 (59%) had at least 1 Bakta PQQ product, while 897 genomes, equal to 24% of all xoxF carriers, lacked PQQ evidence from either source. [^lanthanide_methylotrophy_atlas] This annotation-source discrepancy refines interpretation of xoxF as functional evidence and relates to [pqq-biosynthesis](pqq-biosynthesis.md) and [gene-function-acquisition-depth](../concepts/gene-function-acquisition-depth.md). [^lanthanide_methylotrophy_atlas]

## Marker-source calibration

In a 134,578-row hit-bearing matrix, xoxF had 418 calls in both eggNOG and Bakta, 3,272 eggNOG-only calls, and 1,402 Bakta-only calls; eggNOG K00114 was therefore used as the primary source and Bakta as a union source. [^lanthanide_methylotrophy_atlas] This source calibration differs from the lanmodulin rule: Bakta was preferred for lanmodulin because eggNOG produced 505 lanM-only calls that were concentrated in unrelated gut Bacillota. [^lanthanide_methylotrophy_atlas]

## Limitations

The atlas did not screen sequence-level evidence for pseudogenes, truncated open reading frames, or assembly fragmentation, and novel rare-earth-element-handling enzymes lacking KEGG or RefSeq homologs could be missed. [^lanthanide_methylotrophy_atlas] Consequently, xoxF counts should be interpreted as annotation-based genomic evidence rather than direct measurements of methanol dehydrogenase activity. [^lanthanide_methylotrophy_atlas]

## Related pages

- [lanthanide_methylotrophy_atlas__REPORT](../summaries/lanthanide_methylotrophy_atlas__REPORT.md) — source report for the atlas findings. [^lanthanide_methylotrophy_atlas]
- [pangenome-integration](../concepts/pangenome-integration.md) — cross-genome and taxonomic integration of xoxF and mxaF markers. [^lanthanide_methylotrophy_atlas]
- [environment-embedding-geography](../concepts/environment-embedding-geography.md) — environmental distribution of xoxF carriers. [^lanthanide_methylotrophy_atlas]
- [gene-function-acquisition-depth](../concepts/gene-function-acquisition-depth.md) — annotation calibration and limits on functional interpretation. [^lanthanide_methylotrophy_atlas]
- [mxaf](mxaf.md) — calcium-dependent methanol dehydrogenase comparator. [^lanthanide_methylotrophy_atlas]
- [lanmodulin](lanmodulin.md) — clade-restricted lanthanide-handling marker assessed alongside xoxF. [^lanthanide_methylotrophy_atlas]
- [bakta](bakta.md) — annotation source used for secondary xoxF evidence and marker calibration. [^lanthanide_methylotrophy_atlas]
- [eggnog](eggnog.md) — primary annotation source for K00114 xoxF calls. [^lanthanide_methylotrophy_atlas]

[^lanthanide_methylotrophy_atlas]: [lanthanide methylotrophy atlas](../summaries/lanthanide_methylotrophy_atlas__REPORT.md)
