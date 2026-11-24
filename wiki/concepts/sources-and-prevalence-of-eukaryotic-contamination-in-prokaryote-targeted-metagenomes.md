---
type: "Concept"
description: "How common eukaryotic reads are in environmental metagenomes, whether they are plastid or non-plastid, and how they differ by sample matrix; stops at the statistical handling of confounding."
sources: ["summaries/euk_in_prok_correlates__REPORT.md"]
---
# Sources and prevalence of eukaryotic contamination in prokaryote-targeted metagenomes

This page covers eukaryotic contamination in prokaryote-targeted metagenomes. In the NMDC runs, eukaryotic reads are common (77% of runs carry detectable amounts) and come mostly from photosynthetic plastid DNA rather than animal hosts. [src: euk_in_prok_correlates] The amount and source differ by sample matrix. [src: euk_in_prok_correlates] The evidence comes from one report ([[summaries/euk_in_prok_correlates__REPORT]]). Its depth result is only suggestive. [src: euk_in_prok_correlates]

## Literature Context

The candidate literature is mostly about contamination in host-associated or low-biomass microbiome studies. It does not measure eukaryotic reads in environmental metagenomes. Reviews and consensus statements describe how contaminant DNA and cross-contamination arise and why they matter most when microbial biomass is low. They recommend negative controls and standard reporting [PMID 30497919](https://pubmed.ncbi.nlm.nih.gov/30497919/) [PMID 40542287](https://pubmed.ncbi.nlm.nih.gov/40542287/) [PMID 28476139](https://pubmed.ncbi.nlm.nih.gov/28476139/). Low-biomass systems named in these papers include some human tissues, the atmosphere, plant seeds, treated drinking water, hyper-arid soils and the deep subsurface [PMID 40542287](https://pubmed.ncbi.nlm.nih.gov/40542287/). A statistical tool, decontam, flags contaminants through two patterns. They are higher frequency in low-concentration samples and presence in negative controls [PMID 30558668](https://pubmed.ncbi.nlm.nih.gov/30558668/). A related review of sequence-based human microbiome studies describes biases entering at every step from sample collection onward [PMID 34006335](https://pubmed.ncbi.nlm.nih.gov/34006335/).

A second group of papers is host-focused. Human DNA is a recognised obstacle in skin metagenomics, where bacterial density is low [PMID 24361423](https://pubmed.ncbi.nlm.nih.gov/24361423/). HoCoRT is a tool for removing host sequences from shotgun data. It was benchmarked on synthetic human gut and oral microbiomes plus public data. For long reads it detected 59% of human reads [PMID 37784008](https://pubmed.ncbi.nlm.nih.gov/37784008/). A benchmark of seven host-depletion methods on respiratory samples found that all of them raised microbial reads but also reduced bacterial biomass, introduced contamination and altered microbial abundance [PMID 40624015](https://pubmed.ncbi.nlm.nih.gov/40624015/). These papers address host-derived DNA in host-associated samples. They do not say where eukaryotic reads come from in environmental samples. The human gut genome catalogue [PMID 41345261](https://pubmed.ncbi.nlm.nih.gov/41345261/) and the ancient dental pulp review [PMID 32233019](https://pubmed.ncbi.nlm.nih.gov/32233019/) are not about eukaryotic read prevalence, so they give no comparison.

Against this background, the corpus report is largely novel for environmental data. It finds detectable eukaryotic reads in 77% of NMDC runs, with a median eukaryotic fraction of 2.7%, a mean of 13.3% and 20% of runs above 20%. It also finds that the signal is mostly photosynthetic plastid DNA rather than animal-host DNA. Plastid share is 1.00 in freshwater, 0.03 in plant roots and 0.43 in soil. None of the candidate papers tests or contradicts this. The host-centred literature concerns a different class of sample, so the corpus extends the field to environmental matrices and is not in tension with it.

The corpus does fit one general theme in the literature. Biomass and what is physically in the sample shape how much unwanted DNA appears. The reviews make this point for low-biomass samples [PMID 30497919](https://pubmed.ncbi.nlm.nih.gov/30497919/) [PMID 30558668](https://pubmed.ncbi.nlm.nih.gov/30558668/). The report likewise reads the magnitude as set at collection, by sample content and biomass dilution. Its depth association (Spearman ρ = −0.29, n=292 runs with measured depth) is only suggestive. It is not batch-controlled, and the candidate papers offer no evidence on it. The report calls the eukaryotic signal co-sampled environmental DNA. The low-biomass literature mainly addresses reagent and cross-contamination, so the two uses of "contamination" differ.

## How common eukaryotic reads are

Detectable eukaryotic reads occur in 77% of runs. [src: euk_in_prok_correlates] The median eukaryotic fraction is 2.7% and the mean is 13.3%. [src: euk_in_prok_correlates] The distribution is strongly zero-inflated, since 23% of runs have no detectable eukaryotic reads. [src: euk_in_prok_correlates] It also has a long upper tail: 20% of runs exceed 20% eukaryotic reads. [src: euk_in_prok_correlates] Put another way, one run in five exceeds 20% eukaryotic abundance. [src: euk_in_prok_correlates]

## Plastid versus non-plastid sources

Among runs with detectable eukaryotic reads, plastid DNA (deoxyribonucleic acid from plant or algal chloroplasts) makes up a median 100% of the eukaryotic signal. [src: euk_in_prok_correlates] The report concludes that photosynthetic DNA, not animal-host DNA, dominates eukaryotic contamination in this largely environmental collection. [src: euk_in_prok_correlates] It interprets the contamination as co-sampled photosynthetic environmental DNA rather than laboratory or animal-host contamination. [src: euk_in_prok_correlates]

## Differences by sample matrix

The plastid share and the likely source differ by matrix. [src: euk_in_prok_correlates]

| Matrix | Eukaryotic detection | Plastid share of eukaryotes | Dominant source |
|---|---|---|---|
| Aquatic (freshwater) | 99.5% | 1.00 | algal plastid (phytoplankton chloroplast) [src: euk_in_prok_correlates] |
| Plants (roots) | 100% | 0.03 | non-plastid root-associated fungi/protists [src: euk_in_prok_correlates] |
| Terrestrial ([[entities/soil]]) | 55.7% | 0.43 | mixed plant plastid and soil fungi/protists [src: euk_in_prok_correlates] |

The report names algal chloroplasts in freshwater, plant chloroplasts and soil fungi in terrestrial samples, and root-associated fungi/protists in plant samples as the sources. [src: euk_in_prok_correlates] It reads the magnitude as set upstream at collection. In its view, what is physically in the sample and how much microbial biomass dilutes it set the magnitude. [src: euk_in_prok_correlates] This fits its finding that sequencing platform and read depth have almost no effect once environment is considered. [src: euk_in_prok_correlates] The report has not yet tested whether the algal-plastid versus root-fungal split holds within batch-controlled aquatic and plant-associated cohorts. [src: euk_in_prok_correlates]

## Depth association

Across studies, measured depth correlates negatively with eukaryotic fraction (Spearman ρ = −0.29, p=5.2×10⁻⁷, n=292 runs with measured depth; see [[entities/spearman-rank-correlation]]). Shallower samples carry more eukaryotic DNA. [src: euk_in_prok_correlates] This is suggestive only. It is not batch-controlled, the measured-depth runs come from a handful of non-soil studies, and the dominant NEON soil study records no depth. [src: euk_in_prok_correlates]

## Open Directions

- Test whether the algal-plastid versus root-fungal source split holds within batch-controlled aquatic and plant-associated cohorts. This would show whether the matrix differences survive study confounding.
- Extend the within-study design to aquatic and plant-associated studies, to test whether the vegetation and geography effect generalizes beyond soil.
- Re-test the depth association within single studies that record depth. This would show whether the cross-study ρ=−0.29 is real or a study artifact.
