---
type: "Concept"
description: "Taxonomic shifts (phylum and genus level) in soil microbial communities under long-term experimental warming, by soil horizon; stops at functional gene-level responses."
sources: ["summaries/harvard_forest_warming__REPORT.md"]
---
# Warming response of soil microbial community composition

This page covers phylum- and genus-level shifts in soil microbial community composition under long-term experimental warming, by soil horizon. The evidence comes from one site, Harvard Forest Barre Woods, in one report ([[summaries/harvard_forest_warming__REPORT]]). It shows a real but modest community-level response that reproduces published findings for the site. [src: harvard_forest_warming]

## Literature Context

Two candidate papers address warming at the same Harvard Forest long-term ecological research site. The first used 16S rRNA gene sequencing and quantitative PCR across soils warmed 5°C above ambient for 5, 8 and 20 years [PMID 25762989](https://pubmed.ncbi.nlm.nih.gov/25762989/). Only the 20-year warmed site showed significant change in bacterial community structure in the organic horizon, and the mineral soil showed no significant change. Individual members of the Actinobacteria, Alphaproteobacteria and Acidobacteria showed strong warming responses. One Actinomycete fell from 4.5 to 1% relative abundance. The authors also reported increased bacterial evenness, shifting beta diversity, decreased fungal abundance and increased abundance of bacteria with low rRNA operon copy number, including Alphaproteobacteria and Acidobacteria. They interpreted these changes as suggesting that more or alternative niche space is being created [PMID 25762989](https://pubmed.ncbi.nlm.nih.gov/25762989/).

The second paper combined metagenomics with cultivation across the 5, 8 and 20-year experiments [PMID 27590813](https://pubmed.ncbi.nlm.nih.gov/27590813/). Warming increased the fraction of carbohydrate-degrading genes in mineral soil associated with Actinobacteria in all studies. It decreased the proportion of organic-horizon carbohydrate-degrading genes derived from eukaryotes. Carbohydrate-degradation genes rose in the organic horizon after 5 years but had decreased after 20 years. Among 295 isolates from the 20-year experiment, a greater proportion from heated plots depolymerized cellulose and xylan. The authors stress that carbohydrate-degradation capacity is not uniformly enriched in the metagenomes [PMID 27590813](https://pubmed.ncbi.nlm.nih.gov/27590813/).

The corpus report (Harvard Forest Barre Woods, kraken2 read-based taxonomy, 14 control and 14 heated samples) is partly consistent with this literature. Its organic-horizon signal, with Actinobacteria up (log2 FC +0.341, q 0.049) and no phylum-level change in the mineral horizon after FDR, matches the amplicon study's organic-horizon focus and its lack of mineral-soil change [PMID 25762989](https://pubmed.ncbi.nlm.nih.gov/25762989/). The match is only partial for Acidobacteria. The report finds Acidobacteria decreasing at phylum level (log2 FC −0.549, q 0.049). The amplicon study instead describes increased abundance of low-rRNA-copy bacteria that include Acidobacteria, alongside strong responses of individual members of the group. These results are at different taxonomic levels and use different methods, so they are not necessarily contradictory. Still, the Acidobacteria direction is not clearly reproduced, and the report's claim that it reproduces the earlier signature should be read with that difference in mind.

The report's whole-community result is a treatment effect on Bray-Curtis genus distances of R²=7.6% (p=0.069), which is not significant at p<0.05. Horizon explains R²=30.6% (p=0.0002). The amplicon study reported a significant organic-horizon community change at the 20-year site [PMID 25762989](https://pubmed.ncbi.nlm.nih.gov/25762989/). The two tests differ in design, since the report's test pools horizons. The report's non-significant pooled test therefore does not contradict that finding, and it does not confirm it. The report's hypothesis that Actinobacteria enrichment reflects sub-clade selection fits the metagenomic and isolate evidence of Actinobacteria-linked carbohydrate-degradation changes [PMID 27590813](https://pubmed.ncbi.nlm.nih.gov/27590813/). It stays a hypothesis. The corpus does not resolve sub-clades or measure gene function, so it extends the literature only at the phylum level.

## Phylum-level response by horizon

The organic horizon carries the signal. Actinobacteria and Acidobacteria shift in opposite directions, and both pass the q<0.05 threshold. The mineral horizon shows no phylum-level changes after FDR (false discovery rate). [src: harvard_forest_warming]

The phylum test was a per-phylum Welch t-test on [[entities/kraken2]] read-based relative abundance. It used n=14 control + 14 heated direct samples, with BH-FDR (Benjamini-Hochberg false discovery rate) applied across phyla × horizon. [src: harvard_forest_warming]

Organic horizon, relative abundance in control and heated samples, log2 FC (fold change), and q (BH, Benjamini-Hochberg):

- Actinobacteria: 0.249 control, 0.315 heated, log2 FC +0.341, q 0.049. [src: harvard_forest_warming]
- Acidobacteria: 0.035 control, 0.024 heated, log2 FC −0.549, q 0.049. [src: harvard_forest_warming]
- Verrucomicrobia: 0.0058 control, 0.0041 heated, log2 FC −0.513, q 0.088. [src: harvard_forest_warming]
- Cyanobacteria: 0.0032 control, 0.0026 heated, log2 FC −0.305, q 0.072. [src: harvard_forest_warming]
- Proteobacteria: 0.654 control, 0.605 heated, log2 FC −0.111, q 0.088. [src: harvard_forest_warming]

Verrucomicrobia, Cyanobacteria and Proteobacteria have q above 0.05, so they do not pass q<0.05. [src: harvard_forest_warming]

The report states that the Actinobacteria-up, Acidobacteria-down signal is recoverable from kraken2 read-based taxonomy at q<0.05 in 14+14 samples. [src: harvard_forest_warming] It also states that this signal directly reproduces the 16S-amplicon and metagenome-based warming signature from the same research team. [src: harvard_forest_warming]

## Whole-community structure

Horizon explains more community variation than warming does. PERMANOVA (permutational multivariate analysis of variance, see [[entities/permanova]]) on Bray-Curtis genus distances gives treatment R²=7.6% (p=0.069). [src: harvard_forest_warming] It gives horizon R²=30.6% (p=0.0002). [src: harvard_forest_warming] The treatment × horizon 4-cell model gives R²=41% (p=0.0002). [src: harvard_forest_warming] The treatment effect alone is therefore not significant at p<0.05 in this test. [src: harvard_forest_warming]

## Relation to published work

The report cites DeAngelis et al. (2015, Front. Microbiol.) as finding Actinobacteria, Alphaproteobacteria and Acidobacteria the strongest warming-responsive phyla across 5/8/20-year warmed plots, with shifts most pronounced in the organic horizon. [src: harvard_forest_warming] This **supports** the horizon pattern above. The report cites Pold et al. (2016, AEM) as showing that warming increases the fraction of carbohydrate-degrading genes affiliated with Actinobacteria. [src: harvard_forest_warming] It cites Choudoir et al. (2025, mSphere) as finding that heated-plot isolate genomes are enriched in central carbohydrate and N metabolism and show reduced codon usage bias. [src: harvard_forest_warming] The report reads this as a hypothesis-level interpretation: the Actinobacteria enrichment may reflect sub-clade selection rather than only a compositional shift. [src: harvard_forest_warming]

## Open Directions

- Test the mineral horizon with more samples or a genus-level test, to see whether the absence of phylum-level change reflects low power or a true lack of response.
- Test the near-threshold phyla (Verrucomicrobia, Cyanobacteria, Proteobacteria) in a larger sample set.
- Resolve Actinobacteria to sub-clade level and compare it with the published isolate pangenome results, to test the sub-clade selection hypothesis.
- Fit a treatment-within-horizon PERMANOVA, to separate the treatment effect from the large horizon effect.
