---
type: "Concept"
description: "Whether warming enriches carbon-cycling functions and shifts KO-level profiles in soil metagenomes, including horizon differences and per-gene inference limits; stops at taxonomy."
sources: ["summaries/harvard_forest_warming__REPORT.md"]
---
# Functional gene responses to soil warming

At Harvard Forest, a curated list of carbon-cycling KEGG orthologs (KOs) was enriched among warming-up KOs in organic-horizon DNA only. It was not enriched in mineral DNA or in either RNA pool. [src: harvard_forest_warming] No individual RNA KO survives false discovery rate (FDR) correction, so the RNA signals below are directional, nominal-p observations from one site. [src: harvard_forest_warming] See also [[summaries/harvard_forest_warming__REPORT]].

## Literature Context

The candidate papers show that warming commonly shifts the functional gene content of soil and cold-region metagenomes, but the direction depends on system, depth and pathway. In a tall grass prairie, a decade of warming was linked to a higher relative abundance of genes for degrading organic materials of varying recalcitrance, including in subsoil [PMID 28430189](https://pubmed.ncbi.nlm.nih.gov/28430189/). Another grassland study compared 12 metagenomes and found enrichment of cellulose degradation (~13%), CO2 production (~10%) and denitrification (~12%) under 2°C warming for 10 years [PMID 24375144](https://pubmed.ncbi.nlm.nih.gov/24375144/). A global survey of surface soils from 196 ecosystems reported that carbohydrate-metabolism and hemicellulose-degradation traits correlate with Q10, the temperature sensitivity of respiration [PMID 42779148](https://pubmed.ncbi.nlm.nih.gov/42779148/). Carbohydrate-utilization genes also rose with warming in a Tibetan alpine grassland [PMID 36191158](https://pubmed.ncbi.nlm.nih.gov/36191158/).

The literature is not uniform. A 30-year warming experiment found fewer genes for labile compounds such as cellulose and more for recalcitrant compounds such as lignin, with differences between aggregate size classes [PMID 38699060](https://pubmed.ncbi.nlm.nih.gov/38699060/). In an alpine wetland, warming plus nitrogen addition did not consistently raise overall C, N and P gene abundance and decreased complex C degradation genes [PMID 42943391](https://pubmed.ncbi.nlm.nih.gov/42943391/). In Alaskan tundra, warming reduced C-decomposing genes in the deep organic layer by functional gene array, but shotgun metagenomics did not show this [PMID 34878672](https://pubmed.ncbi.nlm.nih.gov/34878672/). Depth and habitat also structure function: permafrost gene variation across 133 metagenomes was highest for methanogenesis, fermentation, nitrate reduction and replenishment of citric acid cycle intermediates [PMID 37217592](https://pubmed.ncbi.nlm.nih.gov/37217592/). Genes for carbon and nitrogen degradation were mostly overrepresented in permafrost relative to active-layer soils at two sites [PMID 37328770](https://pubmed.ncbi.nlm.nih.gov/37328770/).

The Harvard Forest finding that a curated C-cycling KO list is enriched among warming-up KOs only in organic-horizon DNA (OR 2.78, one-sided p=0.042), and not in mineral DNA or either RNA pool, is partly consistent with the grassland reports of enriched carbon-degradation genes [PMID 28430189](https://pubmed.ncbi.nlm.nih.gov/28430189/), [PMID 24375144](https://pubmed.ncbi.nlm.nih.gov/24375144/). Its restriction to one horizon fits the literature's emphasis on depth and microenvironment dependence [PMID 38699060](https://pubmed.ncbi.nlm.nih.gov/38699060/), [PMID 34878672](https://pubmed.ncbi.nlm.nih.gov/34878672/). The null results in the other three pools sit alongside studies where warming did not uniformly raise C-cycling genes [PMID 42943391](https://pubmed.ncbi.nlm.nih.gov/42943391/).

The directional methanotrophy signal (pmoA/pmoB RNA up in both horizons, nominal p only, no KO surviving FDR) is consistent with the Tibetan grassland, where increased methanotrophic genes correlated with warming-enhanced CH4 uptake (R2 = .59, p < .001) [PMID 36191158](https://pubmed.ncbi.nlm.nih.gov/36191158/). That study also measured CH4 uptake directly, so it is stronger evidence than the Harvard Forest RNA trend, which is a single-site, uncorrected observation. The glyoxylate-cycle signal (icl and ms, heated mineral soil, p=0.037) has no direct counterpart among these papers. The permafrost study's finding on genes for replenishing citric acid cycle intermediates shows that this functional area varies across sites, but it does not test the Harvard Forest signal [PMID 37217592](https://pubmed.ncbi.nlm.nih.gov/37217592/). The glyoxylate result therefore remains hypothesis-level here. The weak, positive cross-horizon correlations of KO responses extend this literature with a genome-wide quantification of horizon specificity.

## Enrichment of a curated C-cycling KO list

The report tested a curated 62-KO list (CAZymes, peptidases, TCA, β-oxidation, aromatic catabolism, methane, C1) for enrichment in heated-up KOs (q<0.10, log2 FC > 0). [src: harvard_forest_warming] Only organic-horizon DNA showed enrichment. The other three combinations had no hits. A one-sided Fisher test was used (see [[entities/fisher-s-exact-test-with-benjamini-hochberg-fdr]]).

| Pool | C-cycling hits | Other hits | OR | one-sided p | Claim |
|---|---|---|---|---|---|
| DNA × organic | 5 / 57 | 428 / 12,806 | 2.78 | 0.042 | [src: harvard_forest_warming] |
| DNA × mineral | 0 / 57 | 2 / 12,806 | 0.0 | 1.0 | [src: harvard_forest_warming] |
| RNA × organic | 0 / 57 | 0 / 14,245 | NaN | 1.0 | [src: harvard_forest_warming] |
| RNA × mineral | 0 / 57 | 0 / 14,245 | NaN | 1.0 | [src: harvard_forest_warming] |

The DNA-organic enrichment is reported as significant. [src: harvard_forest_warming] The other three rows are null results. [src: harvard_forest_warming]

## RNA signals: methanotrophy and glyoxylate cycle

The report calls the strongest mechanistic RNA signals methanotrophy (pmoA/pmoB) and the glyoxylate cycle (icl + ms). It does not call them canonical CAZymes, which the published 5°C-respiration narrative would predict. [src: harvard_forest_warming] These are nominal p-values that do not survive FDR across 14K KOs. [src: harvard_forest_warming] The report describes the carbon-cycling RNA signals as biologically directional. It says the multiple-testing burden prevents individual FDR significance. [src: harvard_forest_warming]

| KO | Gene | Horizon | log2 FC | nominal p | Claim |
|---|---|---|---|---|---|
| K10944 | pmoA | organic | +0.730 | 0.009 | [src: harvard_forest_warming] |
| K10945 | pmoB | organic | +0.669 | 0.012 | [src: harvard_forest_warming] |
| K10944 | pmoA | mineral | +0.743 | 0.029 | [src: harvard_forest_warming] |
| K10945 | pmoB | mineral | +0.880 | 0.054 | [src: harvard_forest_warming] |
| K01637 | aceA / icl | mineral | +0.460 | 0.037 | [src: harvard_forest_warming] |
| K01638 | aceB / glcB | mineral | +0.268 | 0.037 | [src: harvard_forest_warming] |
| K01183 | chiA | organic | +0.236 | 0.074 | [src: harvard_forest_warming] |
| K00382 | lpdA | organic | −0.161 | 0.021 | [src: harvard_forest_warming] |

Methanotrophy signals are directional and consistent across horizons. Both glyoxylate signals have p=0.037 in heated mineral soil. [src: harvard_forest_warming] The glyoxylate signals are reported only for mineral soil, so cross-horizon consistency is not claimed for them. [src: harvard_forest_warming] The report describes the methanotrophy-up and glyoxylate-up RNA signature as previously unreported at this site, though both have published precedents elsewhere. [src: harvard_forest_warming]

### Interpretation offered by the report

These are the report's interpretations, not tested results.
- Zhang et al. (2024) report increased net CH₄ uptake (12-61% across soil depths) and more high-affinity USCα methanotrophs at 0-10 cm under subtropical forest +4°C warming. [src: harvard_forest_warming] The report reads this as support for the idea that warming-induced moisture decrease increases CH₄ availability to methanotrophs. [src: harvard_forest_warming]
- Aliyu et al. (2016) describe coordinated icl/aceA + aceB/glcB upregulation as a stress or C2-substrate signature in Actinobacteria. [src: harvard_forest_warming] The report calls the heated-mineral glyoxylate signal mechanistically self-consistent with Actinobacteria enrichment at Harvard Forest. [src: harvard_forest_warming] See [[entities/glyoxylate-cycle-isocitrate-lyase-and-malate-synthase]] and [[entities/actinomycetota]].
- The report says the CAZyme up-direction of Roy Chowdhury et al. is consistent with its chitinase up-result. [src: harvard_forest_warming]
- DeAngelis et al. (2015) and Pold et al. (2016) document strong genome-content shifts at this site over the same period. [src: harvard_forest_warming]

## Horizon differences

Most warming responses are horizon-specific, with ~39% of DNA KOs organic-only, mineral-only, or sign-flipping. [src: harvard_forest_warming] Correlations of KO responses between horizons are positive but weak. [src: harvard_forest_warming]

| Pool | Pearson r | Spearman ρ | Claim |
|---|---|---|---|
| DNA | 0.075 (p=1.78e-17) | 0.216 (p=2e-134) | [src: harvard_forest_warming] |
| RNA | 0.034 (p=6e-5) | 0.120 (p=4e-47) | [src: harvard_forest_warming] |

The curated C-cycling list is not differentially enriched in any horizon-specific class (OR<1, p>0.87 everywhere). This fits the pmoA/pmoB result, which is up in both horizons. [src: harvard_forest_warming] The report concludes that H3 holds genome-wide, but curated C-cycling categories are not the primary driver of the horizon × warming interaction. [src: harvard_forest_warming]

## Limits on per-gene inference

No individual RNA KO survives FDR (q<0.10) at n=11+11 across 14K KOs, though the direction of the strongest signals is interpretable. [src: harvard_forest_warming] The pmoB mineral signal (p=0.054) and chiA (p=0.074) are not even nominally below 0.05. [src: harvard_forest_warming] The multiple-testing burden at this sample size precludes individual FDR significance. [src: harvard_forest_warming]

## Follow-up proposed by the report

The report proposes a cross-study meta-analysis with NMDC SPRUCE peatland nmdc:sty-11-33fbta56 and Alaskan permafrost thaw nmdc:sty-11-db67n062 to test whether the methanotrophy-up signature reproduces across sites. [src: harvard_forest_warming] It proposes finding which MAGs (metagenome assembled genomes) in the 298-MAG cohort carry upregulated pmoA/pmoB, and whether they are USCα methanotrophs or spread across phyla. [src: harvard_forest_warming] It also proposes the hypothesis that warming activates a ruderal community fraction (Actinobacteria, glyoxylate-cycle-active organisms, methanotrophy), to be tested against Choudoir et al. 2025 pangenome data. [src: harvard_forest_warming]

## Open Directions

- Run the cross-study meta-analysis with the SPRUCE peatland and Alaskan permafrost NMDC studies. This closes the single-site gap for the methanotrophy signature.
- Track pmoA/pmoB to specific MAGs in the 298-MAG cohort. This would show which taxa carry the signal.
- Test the ruderal-subset hypothesis against Choudoir et al. 2025 pangenome data.
- Test the methanotrophy and glyoxylate KOs as a pre-specified small set rather than across 14K KOs. This would reduce the multiple-testing burden that blocks FDR significance.
