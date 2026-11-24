---
type: "Concept"
description: "How using all genomes versus diversity-maximizing downsampling, missing-value exclusion and genome count change measured partial correlations and group comparisons; stops at ecotype partial correlations."
sources: ["summaries/ecotype_env_reanalysis__REPORT.md"]
---
# Genome sampling depth and downsampling effects on partial correlation estimates

This page covers genome sampling depth and downsampling effects on partial correlation estimates. In the ecotype reanalysis, using all genomes instead of diversity-maximizing downsampling raised the median partial correlation to 0.081 from 0.003 in the original analysis. [src: ecotype_env_reanalysis] The evidence comes from one report. It argues that the environmental versus human-associated comparison still holds, because both groups use the same methodology. [src: ecotype_env_reanalysis] See [[entities/partial-correlation-of-environment-and-gene-content-distance]] and [[summaries/ecotype_env_reanalysis__REPORT]].

## Literature Context

Of the candidate papers, only one bears on this page. It is a review of Staphylococcus aureus phylogenomics [PMID 27751626](https://pubmed.ncbi.nlm.nih.gov/27751626/). The other two candidates concern a soybean pod borer genome and quadruplex single nucleotide polymorphisms in human gene expression. Neither addresses genome sampling or partial correlations, so they are not used here.

The S. aureus review says genome sequences have accrued in a haphazard manner. Sampling of natural variation is biased, and medical and epidemiological priorities drive it. As an example, it notes a strong bias toward sequencing epidemic lineages of methicillin-resistant S. aureus (MRSA) over sensitive isolates (MSSA) [PMID 27751626](https://pubmed.ncbi.nlm.nih.gov/27751626/). It also reports that sequencing more diverse genomes reveals a highly subdivided species. A handful of relatively clonal groups dominate particular geographical regions at any given moment [PMID 27751626](https://pubmed.ncbi.nlm.nih.gov/27751626/). The review is a qualitative abstract-level discussion. It gives no estimate of how sampling depth changes any correlation statistic.

This is **consistent** with the reanalysis's concern about uneven genome representation. The reanalysis used all genomes with embeddings, up to 3,505 per species. The original analysis used diversity-maximizing downsampling with a maximum of 250. The median partial correlation across all 183 species was 0.081 in the reanalysis and 0.003 in the original. The report also proposes that species with many genomes, often clinical, may have inflated correlations. The S. aureus review makes that suspicion plausible. If clinically driven sequencing concentrates genomes in a few dominant clones, then genome count may partly reflect lineage structure and not independent environmental variation [PMID 27751626](https://pubmed.ncbi.nlm.nih.gov/27751626/). This is an inference from a single-species review. It is not a test of the hub's claim.

The literature here does not speak to the other findings. These are the 27x magnitude difference, the NaN rates (10/47 = 21% for environmental species, 13/66 = 20% for Mixed/Other and 7/100 = 7% for human-associated), and the argument that missing-value exclusion would only strengthen the null result. Those claims are **novel** relative to these candidates, and they rest on one report. The proposals to compare downsampled and full-genome extraction and to add genome count as a covariate remain untested. The review supports their motivation, since sampling is biased toward clinical lineages. It does not show that either step fixes the bias. See [[entities/partial-correlation-of-environment-and-gene-content-distance]] and [[concepts/clinical-sampling-bias-in-environment-embedding-analyses]].

## Using all genomes versus downsampling

The reanalysis used all genomes with embeddings, up to 3,505 per species. The original analysis used diversity-maximizing downsampling with a maximum of 250. [src: ecotype_env_reanalysis] The median partial correlation across all 183 species was 0.081 in the reanalysis, compared with 0.003 in the original. [src: ecotype_env_reanalysis] The report calls this a 27x difference. [src: ecotype_env_reanalysis]

The report lists two features of the reanalysis as caveats: larger samples detect weaker correlations, and without downsampling the distance distributions change. [src: ecotype_env_reanalysis] It does not present them as tested causes of the magnitude difference. It proposes comparing downsampled and full-genome extraction to understand that difference. [src: ecotype_env_reanalysis] The report says absolute values are not comparable with the original analysis. [src: ecotype_env_reanalysis] It holds that the group comparison stays valid, because both groups use the same methodology. [src: ecotype_env_reanalysis] This is the report's argument, not a separate test.

The report also proposes that species with more genomes, often clinical, have more power to detect weak correlations. [src: ecotype_env_reanalysis] It cautions that such species may have inflated correlations and proposes adding genome count as a covariate. [src: ecotype_env_reanalysis] See [[concepts/clinical-sampling-bias-in-environment-embedding-analyses]] and [[concepts/genome-sampling-depth-genome-size-and-phylogeny-as-confounders-of-gene-content-and-pangenome-associations]].

## Missing-value exclusion

Thirty species had NaN (not a number) partial correlations. The NaN rate was highest for environmental species (10/47 = 21%) and Mixed/Other species (13/66 = 20%). It was lowest for human-associated species (7/100 = 7%). [src: ecotype_env_reanalysis]

The environmental group therefore loses more species. The report says this could slightly bias the comparison. It argues the bias would favor a stronger environmental signal, the opposite of the observed result, so correcting it would only strengthen the null result. [src: ecotype_env_reanalysis]

Klebsiella pneumoniae, a major clinical species, was excluded from the correlation data. Gene cluster extraction exceeded Spark's maxResultSize. [src: ecotype_env_reanalysis] See [[entities/klebsiella-pneumoniae]].

## Open Directions

- Compare downsampled and full-genome extraction on the same species to explain the 27x magnitude discrepancy.
- Add genome count as a covariate to test whether species with more genomes have inflated correlations.
- Re-extract Klebsiella pneumoniae in chunks to avoid the Spark limit, to test whether the largest clinical species changes the group comparison.
