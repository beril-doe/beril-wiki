---
type: "Concept"
description: "Whether the transcript (RNA) functional pool responds more strongly to a perturbation such as warming than the genome (DNA) pool, including confounds from design and timing; stops at individual gene findings."
sources: ["summaries/harvard_forest_warming__REPORT.md"]
---
# DNA versus RNA pool sensitivity to environmental perturbation

This page asks whether the transcript (RNA) functional pool responds more strongly to warming than the genome (DNA) pool. The only evidence here is one Harvard Forest study. It found that the apparent DNA-versus-RNA imbalance is largely a horizon × incubation artifact, and that the two pools respond comparably (10-13% treatment R²). [src: harvard_forest_warming] The result is a single-site, single-timepoint null for the hypothesis that RNA is more sensitive, and the report's explanations for it are proposals, not tests. [src: harvard_forest_warming]

## Literature Context

The candidate papers do not directly compare DNA-pool and RNA-pool sensitivity to warming in paired samples, so none of them tests the hub's central question. They do show that warming, or climate stress, is usually studied with metagenomics, metatranscriptomics or both, and that the two layers are often read together.

In Arctic peat microcosms incubated over a 1 to 30 °C gradient, metatranscriptomic, metagenomic and metabolic profiling were combined. The authors report that the CH4 production rate at 4 °C was 25% of that at 25 °C, and that the microbial community shifted in structure, metabolic network and trophic interactions with temperature [PMID 25918393](https://pubmed.ncbi.nlm.nih.gov/25918393/). A study of river sediment used 13C-lignin and 13C-vanillin stable isotope probing. It reports that higher temperature raised CO2 emissions and the abundance and activity of putative lignin decomposers. It also reports rising transcriptional abundance of some carbon-cycling genes [PMID 40170118](https://pubmed.ncbi.nlm.nih.gov/40170118/). A Central European field study used metagenomics over the summers of 2014-2019. Extreme heatwaves and droughts in 2018-2019 changed the structure, assembly and function of the soil microbiome. Candidate drought-associated genes were checked by metatranscriptomics in 2022. The +0.6 °C warming and altered-precipitation scenarios produced a similar pattern of change, but to a much lesser extent [PMID 37419993](https://pubmed.ncbi.nlm.nih.gov/37419993/). An earlier metagenomic and metatranscriptomic survey of two Arctic peat soils found that the gene pool for polymer degradation resembled that of temperate and subtropical soils [PMID 22955232](https://pubmed.ncbi.nlm.nih.gov/22955232/). That paper is descriptive and not a warming comparison.

The corpus's Harvard Forest finding sits mostly outside this literature and partly extends it. Those studies report responses in transcripts, genes or community structure, but none of the abstracts quantifies treatment variance for DNA and RNA side by side. The hub's paired comparison found comparable treatment R² of 10-13% once the horizon × incubation confound was removed. It is a single-site, single-timepoint null for the hypothesis that RNA is more sensitive, so it is novel in design rather than contradicted by these papers.

The peat and sediment reports show transcript-level responses to temperature in manipulated experiments. Those responses are not set against a DNA-pool response, so they neither support nor contradict the hub's null. The corpus's proposal that decades of chronic heating let genome content catch up with transcript changes is not tested by any candidate. The extreme-summer study covers a much shorter span and reports only a modest metagenomic shift under the mild warming scenario. The hub's explanations therefore remain hypotheses. The candidates also do not address the hub's tension with Roy Chowdhury et al. (2021).

## The comparison and its confound

The report says it gives the first explicit paired-sample comparison of DNA-pool and RNA-pool warming-response variance at Harvard Forest. [src: harvard_forest_warming] The hypothesis, called H1, was that RNA composition shifts more than DNA under warming. [src: harvard_forest_warming]

In the paired n=25 subset, treatment [[entities/permanova]] (permutational multivariate analysis of variance) gave pseudo-F 3.12 in DNA (R²=11.9%, p=0.020) and 0.76 in RNA (R²=3.2%, p=0.60). [src: harvard_forest_warming] That points opposite to H1. However, the paired subset confounds horizon with incubation, because every organic sample is incubated and every mineral sample is direct. [src: harvard_forest_warming]

Direct-only sensitivity analysis removes the incubation confound [src: harvard_forest_warming]:

| Pool × horizon | n | F | R² | p |
|---|---|---|---|---|
| DNA × mineral | 14 | 1.75 | 12.7% | 0.081 [src: harvard_forest_warming] |
| RNA × mineral | 11 | 1.15 | 11.4% | 0.254 [src: harvard_forest_warming] |
| RNA × organic | 14 | 1.33 | 10.0% | 0.190 [src: harvard_forest_warming] |

After removing the confound, both pools show about 10-13% treatment R². [src: harvard_forest_warming] H1 is not supported. [src: harvard_forest_warming] The transcript pool is not more sensitive than the genome pool at this sample size and timepoint. [src: harvard_forest_warming]

## Proposed explanations

The report offers these as explanations, not tested results.

- **Turnover has caught up.** H1 assumes transcript-level regulation precedes genome-content turnover. The Barre Woods plots have been heated since about 1991, and the report argues 25 years is enough for genome content to reflect warming-selected lineages. [src: harvard_forest_warming] It also argues the DNA pool integrates over years and so reads the chronic +5°C signal more cleanly. [src: harvard_forest_warming]
- **Transcript noise.** All samples came from one date (2017-05-24), and transcript abundances respond to short-timescale conditions unrelated to warming. [src: harvard_forest_warming]
- **Rare-organism repertoire.** The metatranscriptome assembly recovered 14,302 distinct KOs (KEGG orthologs) versus 12,863 in the metagenome. [src: harvard_forest_warming] The report proposes that this richer repertoire raises per-KO variance and reduces power to detect treatment shifts. [src: harvard_forest_warming]
- **Global down-regulation.** Chronic substrate depletion could down-shift the active transcriptome across many categories. That would leave no preferred axis of treatment-driven RNA variance while the community keeps diverging. [src: harvard_forest_warming]

The comparable-R² verdict does not rule out an early transient in which RNA leads DNA. The report argues instead that the two pools converge in magnitude on multi-decadal timescales. [src: harvard_forest_warming]

## Relation to prior work

Roy Chowdhury et al. (2021) is the closest published precedent, using Harvard Forest organic and mineral metatranscriptomes under heated and control treatments. [src: harvard_forest_warming] The report states they found a larger treatment effect on KEGG transcripts than on carbohydrate-active enzymes (CAZymes), with ~68% of differentially expressed CAZyme transcripts upregulated in heated soils. [src: harvard_forest_warming] The report calls its comparable DNA and RNA response in tension with their larger transcript-level effect. It cautions that sampling timepoint, replication and analytical pipeline differ. [src: harvard_forest_warming]

## Caveats

- There is a single timepoint, so seasonal effects cannot be detected. Shinfuku et al. 2024 show these are substantial at this site. [src: harvard_forest_warming]
- Omics sample sizes (n=28 metagenome, n=39 metatranscriptome) limit per-KO false discovery rate (FDR) power across 12-14K KOs. [src: harvard_forest_warming]
- Metatranscriptome KO data come from contig annotations. They measure transcript-pool composition, not TPM-quantified expression, and assembly quality biases them. [src: harvard_forest_warming]
- All organic-horizon DNA samples are lab-incubated, so incubation cannot be factored out cleanly there. [src: harvard_forest_warming]
- Coverage is unbalanced because the NMDC pipeline produced no metagenomes for organic-direct or some mineral-direct samples. This drives the H1 sensitivity caveat. [src: harvard_forest_warming]

## Open Directions

- Repeat the paired DNA/RNA design across several seasons. This would test whether a transient RNA lead exists that a single timepoint cannot show. [src: harvard_forest_warming]
- Collect direct (non-incubated) organic-horizon DNA and RNA. This would remove the horizon × incubation confound that limits the organic DNA analysis. [src: harvard_forest_warming]
- Quantify transcripts by read mapping (TPM) instead of contig annotation counts. This would test whether assembly bias hides RNA treatment variance. [src: harvard_forest_warming]
- Apply the same pipeline to the Roy Chowdhury et al. data. This would test whether the tension with their larger transcript effect comes from method or from sampling. [src: harvard_forest_warming]
- Compare unheated and recently heated plots. This would test whether the compositional-turnover explanation depends on warming duration. [src: harvard_forest_warming]
