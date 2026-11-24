---
type: "Concept"
description: "Observational tests of whether genera with diverse metal resistance are more prevalent or selected in groundwater and the contaminated, carbon-amended Oak Ridge subsurface; stops at global comparative analyses."
sources: ["summaries/lab_field_ecology__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md"]
---
# Field validation of metal-diversity genera in contaminated groundwater

This page covers observational tests of whether genera with diverse metal resistance are more prevalent in groundwater, and whether they are selected in the contaminated, carbon-amended Oak Ridge subsurface. The evidence comes mostly from one report, [[summaries/microbeatlas_metal_ecology__REPORT]]. It shows a modest prevalence association in groundwater and a within-study temporal and plume signal at Oak Ridge. It shows no groundwater-specific enrichment. For the groundwater analysis, the report says it does not uniquely support a metal-contamination mechanism. [src: microbeatlas_metal_ecology] The report states that ENIGMA field-validation Tracks A and B are complete, that a candidate OTU list and shortlist were produced, and that both tracks independently confirm the PGLS prediction in field data. [src: microbeatlas_metal_ecology]

## Literature Context

The candidate papers mostly show that metal contamination restructures microbial communities and enriches resistance functions. They do not test whether genera with diverse metal resistance are more prevalent in groundwater. In a metagenomic study of a heavy-metal-contaminated groundwater community exposed for about 50 years to metals, nitric acid and organic solvents, species, allelic and metabolic diversity fell sharply [PMID 20182523](https://pubmed.ncbi.nlm.nih.gov/20182523/). The surviving community was simple and mainly clonal denitrifying gamma- and beta-proteobacteria. It was overabundant in genes conferring resistance to nitrate, heavy metals and acetone, and lateral gene transfer was proposed as important for adaptation [PMID 20182523](https://pubmed.ncbi.nlm.nih.gov/20182523/). A study of an abandoned sewage reservoir found metal-resistant species abundant in the most contaminated zone and metal-sensitive species prevailing in the least contaminated zone. Homogeneous selection dominated assembly there [PMID 32683027](https://pubmed.ncbi.nlm.nih.gov/32683027/). Other surveys point the same way. Functional predictions for mercury and arsenic resistance genes increased with pollution at a brownfield [PMID 36804142](https://pubmed.ncbi.nlm.nih.gov/36804142/). Estuarine sediment was enriched in metal-resistant genera [PMID 42575174](https://pubmed.ncbi.nlm.nih.gov/42575174/). In North China industrial groundwater, heavy metals became the key driver of community composition and explained 50.80% of the change [PMID 38754488](https://pubmed.ncbi.nlm.nih.gov/38754488/).

The literature is not uniform on selection. In antimony-contaminated groundwater, Sb drove deterministic heterogeneous selection of bacterial communities. Assembly of Sb-resistant bacteria and archaea was instead dominated by stochastic processes [PMID 37714340](https://pubmed.ncbi.nlm.nih.gov/37714340/). In an alkaline vanadium tailing pond, stochastic processes governed water communities and deterministic processes governed sediment communities [PMID 38181847](https://pubmed.ncbi.nlm.nih.gov/38181847/). Analysis of 242 samples from the NCBI database on nitrate and Cr(VI) contamination also stressed that energy substances and pollutant species shape communities. It named Azoarcus, Pseudomonas and Thauera as candidates for simultaneous reduction, and its resistance gene results (such as chrA) came from PICRUSt2 predictions [PMID 34634272](https://pubmed.ncbi.nlm.nih.gov/34634272/).

The corpus's Oak Ridge time-series result is consistent with this literature. Community weighted mean metal-type diversity was higher in the plume wells FW215/FW216 and rose after carbon amendment (ρ = +0.383, n = 133). This parallels the contaminated-versus-less-contaminated contrasts in the reservoir and groundwater studies [PMID 32683027](https://pubmed.ncbi.nlm.nih.gov/32683027/) [PMID 38754488](https://pubmed.ncbi.nlm.nih.gov/38754488/). It also fits the picture of resistance-enriched survivors under long-term stress [PMID 20182523](https://pubmed.ncbi.nlm.nih.gov/20182523/). The corpus's own caveat applies: only 16.8% of reads could be joined to metal data, and robustness to coverage was not tested. The candidate studies are also mostly amplicon or functional-prediction surveys at single sites, so the agreement is qualitative.

The corpus's groundwater-wide analysis is novel relative to these candidates. Across 1,624 groundwater samples, genus metal-type count correlated with prevalence (ρ = +0.112, p = 0.0019). It did not correlate with fold enrichment (ρ = +0.042, p = 0.242), and that null stays null. None of the candidate papers tests a genus-level trait such as metal-type breadth against prevalence across many samples, so this extends the site-level evidence to a trait-based, cross-site test. The mixed deterministic and stochastic findings in antimony and vanadium systems [PMID 37714340](https://pubmed.ncbi.nlm.nih.gov/37714340/) [PMID 38181847](https://pubmed.ncbi.nlm.nih.gov/38181847/) are a reminder that the modest prevalence effect need not indicate metal selection. This agrees with the report's own caution that it does not uniquely support a contamination mechanism.

The Sulfurimonas counterexample, which declined after amendment, matches the view in [PMID 34634272](https://pubmed.ncbi.nlm.nih.gov/34634272/) that energy substances, not only metals, structure groundwater communities.

## Groundwater prevalence across 1,624 samples (ENIGMA Track A)

**Design.** The report predicted that genera with broader metal-type resistance repertoires, if they are ecological generalists, should be more prevalent across chemically challenging groundwater samples. [src: microbeatlas_metal_ecology] It used 1,624 arkinlab_microbeatlas groundwater samples in the KBase Data Lakehouse (Env_Level_2 = "groundwater"). [src: microbeatlas_metal_ecology] OTU (operational taxonomic unit) counts came through the REST (representational state transfer) API, by joining otu_counts_long and sample_metadata. [src: microbeatlas_metal_ecology] The analysis subset was 767 genera with at least one OTU in groundwater and non-null mean_n_metal_types. [src: microbeatlas_metal_ecology] Prevalence was the mean fraction of the 1,624 samples in which at least one OTU of the genus was detected. [src: microbeatlas_metal_ecology] Fold enrichment was groundwater prevalence % divided by non-groundwater prevalence % across 462,348 samples. [src: microbeatlas_metal_ecology]

**Result.** Metal-type count correlated with prevalence but not with enrichment. The prevalence association was positive (Spearman ρ = +0.112, p = 0.0019). [src: microbeatlas_metal_ecology] The enrichment correlation was not significant (ρ = +0.042, p = 0.242). [src: microbeatlas_metal_ecology] Quartile thresholds were Q1 ≤ 1.0 and Q4 ≥ 1.5 metal types. [src: microbeatlas_metal_ecology] Top-Q4 and bottom-Q1 genera (213 vs 429) differed in prevalence (Mann-Whitney p = 0.007). [src: microbeatlas_metal_ecology] The report summarises this as top-quartile metal-diversity genera being 31% more prevalent in groundwater (Mann-Whitney p=0.007). [src: microbeatlas_metal_ecology] They did not differ in fold enrichment (p = 0.181). [src: microbeatlas_metal_ecology] Median prevalence was 0.81% for top-Q4 genera and 0.62% for bottom-Q1 genera, a ratio of 1.31× (one-sided p = 0.007). [src: microbeatlas_metal_ecology]

**Interpretation.** The report calls this an independent field cross-validation of its PGLS (phylogenetic generalized least squares) finding. It reads the result as consistent with diverse metal resistance being associated with greater ecological range in chemically challenging subsurface environments. [src: microbeatlas_metal_ecology] It describes the effect as modest, consistent with the global PGLS coefficient being a partial correlation after removing phylogenetic structure. [src: microbeatlas_metal_ecology] The null on enrichment means the signal does not show metal-diverse genera being preferentially enriched in groundwater beyond their global baseline. [src: microbeatlas_metal_ecology] The report offers two readings of that null: a general breadth effect, or too little power in the 1,624-sample subset. [src: microbeatlas_metal_ecology] Track A is consistent with the PGLS finding but does not uniquely support a metal-contamination mechanism. [src: microbeatlas_metal_ecology]

### ENIGMA candidate genera

The ENIGMA candidate table (see [[entities/enigma]]) gives these values per genus. [src: microbeatlas_metal_ecology]

| Genus | Groundwater prevalence (%) | Fold enrichment | Metal types |
|---|---|---|---|
| Azospira | 5.21 | 2.3× | 3.0 [src: microbeatlas_metal_ecology] |
| Enterobacter | 4.80 | 1.1× | 3.1 [src: microbeatlas_metal_ecology] |
| Citrobacter | 0.89 | 2.8× | 3.7 [src: microbeatlas_metal_ecology] |
| Enterococcus | 0.71 | 2.8× | 3.3 [src: microbeatlas_metal_ecology] |
| Noviherbaspirillum | 1.01 | 1.4× | 3.0 [src: microbeatlas_metal_ecology] |
| Franconibacter | 0.39 | 1.6× | 3.5 [src: microbeatlas_metal_ecology] |

Pseudomonas is listed with 2.1 metal types and was not in the top 15, so it has no prevalence or enrichment estimate. [src: microbeatlas_metal_ecology] The report reads the 2.8× enrichment of [[entities/citrobacter]] and Enterococcus as consistent with its ENIGMA experimental predictions. [src: microbeatlas_metal_ecology] It describes Azospira as a denitrifier detected in 5.2% of groundwater samples. It has the highest prevalence among high-metal-diversity genera and an established role in groundwater nitrogen cycling. [src: microbeatlas_metal_ecology]

## Oak Ridge subsurface time series (PRJNA1084851, ENIGMA Track B)

**Processing.** The ORFRC (Oak Ridge Field Research Center) Track B pipeline processed 133/133 samples and produced 24,295 OTUs. [src: microbeatlas_metal_ecology] All 133 passed QC (quality control). [src: microbeatlas_metal_ecology] The median depth was 56,908 reads/sample. [src: microbeatlas_metal_ecology] Of the OTUs, 14,021 had genus-level SILVA 138 taxonomy. [src: microbeatlas_metal_ecology] Only 1,637 OTUs, representing 16.8% of reads, could be joined to genus metal diversity data. [src: microbeatlas_metal_ecology] Sample CWM (community weighted mean) metal-type diversity ranged from 1.01–1.83, with mean 1.28 ± 0.19. [src: microbeatlas_metal_ecology]

**Coverage caveat.** CWM excludes the remaining ~83% of reads, whose genera lack SILVA-to-GTDB AMR (antimicrobial resistance) taxonomy matches. [src: microbeatlas_metal_ecology] CWM would be biased upward if the uncovered genera were systematically more metal-sensitive. [src: microbeatlas_metal_ecology] The report has not formally tested robustness to coverage variation. [src: microbeatlas_metal_ecology] It recommends correlating per-sample CWM with covered-read fraction before further use. [src: microbeatlas_metal_ecology] See also [[concepts/genus-level-taxonomy-bridging-to-pangenome-clades-and-its-coverage-limits]].

**Well and time structure.** CWM metal-type diversity was significantly higher in contamination-plume wells FW215/FW216 (Kruskal-Wallis p = 0.0001). [src: microbeatlas_metal_ecology] CWM differed across 8 wells (Kruskal-Wallis H = 29.10, n = 133, p = 0.0001). [src: microbeatlas_metal_ecology] It rose with time after carbon amendment across all wells (Spearman ρ = +0.383, p < 0.0001; n = 133). [src: microbeatlas_metal_ecology] In FW216 alone the rise was stronger (ρ = +0.576, p = 0.0001). [src: microbeatlas_metal_ecology] EVO09 and EVO17 differed in CWM (n = 52 vs 81, p = 0.0012). [src: microbeatlas_metal_ecology] Median CWM by well, from high to low:

| Well | Median CWM |
|---|---|
| FW215 | 1.37 [src: microbeatlas_metal_ecology] |
| FW216 | 1.36 [src: microbeatlas_metal_ecology] |
| GP01 | 1.23 [src: microbeatlas_metal_ecology] |
| GP03 | 1.22 [src: microbeatlas_metal_ecology] |
| MLSB3 | 1.14 [src: microbeatlas_metal_ecology] |
| MLSA3 | 1.09 [src: microbeatlas_metal_ecology] |
| FW202 | 1.08 [src: microbeatlas_metal_ecology] |
| MLSG4 | 1.08 [src: microbeatlas_metal_ecology] |

**Interpretation.** Wells FW215 and FW216 lie within the U/NO₃ contamination plume. [src: microbeatlas_metal_ecology] The report reads their higher CWM as consistent with metal-contaminated subsurface environments selecting genera with broader metal resistance. [src: microbeatlas_metal_ecology] It suggests that carbon amendment progressively selects metal-diverse communities, possibly through reducing conditions that change the speciation of redox-active U, Fe and S. [src: microbeatlas_metal_ecology] It treats the results as within-study support for the core PGLS finding. [src: microbeatlas_metal_ecology] It also says the temporal rise points to active ecological selection under geochemical stress. [src: microbeatlas_metal_ecology] The geochemical pathway is stated only as a possibility. Separately, the report says robustness of CWM to coverage variation has not been formally tested. [src: microbeatlas_metal_ecology]

An earlier report cites Michael et al. (2024) for reproducible microbial succession after carbon amendments at Oak Ridge. It reads its own uranium-abundance correlations as supporting a deterministic response to geochemical perturbation. [src: lab_field_ecology] See [[summaries/lab_field_ecology__REPORT]] and [[concepts/geochemical-and-contamination-plume-control-of-subsurface-community-structure]].

### Taxa that do not follow the metal-diversity pattern

Sulfurimonas (80 OTUs, 96.2% prevalence) declined with time (ρ = −0.323, n = 133, p = 0.0002). [src: microbeatlas_metal_ecology] The report proposes that carbon amendment depletes its preferred electron acceptors, nitrate and oxygen. [src: microbeatlas_metal_ecology] It presents Sulfurimonas as a counterexample: a prevalent generalist driven by electron-acceptor availability rather than metal resistance. Not all dominant groundwater taxa are metal-diverse. [src: microbeatlas_metal_ecology] Nitrospira (25 OTUs, 88.7% prevalence) was most abundant in plume well FW215. [src: microbeatlas_metal_ecology] Candidatus Jorgensenbacteria (Patescibacteria/CPR, candidate phyla radiation; 122 OTUs, 99.2% prevalence) was ubiquitous. [src: microbeatlas_metal_ecology] Citrobacter and Thermodesulfovibrio were not detected, either because they were below detection or because genus names mismatched SILVA nomenclature. [src: microbeatlas_metal_ecology]

## Proposed site-level validation

The report proposes testing whether MicrobeAtlas genera with high metal-type diversity are enriched in mining-impacted, biosolid-amended and estuarine samples versus clean references, to validate environmental co-selection. [src: microbeatlas_metal_ecology]

## Tensions

- The groundwater prevalence association is significant (p = 0.0019), but fold enrichment is not (p = 0.242). [src: microbeatlas_metal_ecology] The report cannot separate a general breadth effect from low power. [src: microbeatlas_metal_ecology]
- The Oak Ridge CWM gradient is read as consistent with plume selection. [src: microbeatlas_metal_ecology] Only 16.8% of reads were joined to metal data, and CWM would be biased upward if the uncovered genera were systematically more metal-sensitive. [src: microbeatlas_metal_ecology]

## Open Directions

- Correlate per-sample CWM with covered-read fraction in PRJNA1084851. This closes the untested coverage bias.
- Run a power analysis, or use a larger groundwater set, for the fold-enrichment test. This would separate a breadth effect from low power.
- Run the proposed site-level test on MicrobeAtlas metadata for mining-impacted, biosolid-amended and estuarine samples against clean references.
- Improve SILVA-to-GTDB genus matching, then re-check the Citrobacter and Thermodesulfovibrio non-detections. See [[concepts/taxonomy-bridging-between-metagenomic-classifiers-and-reference-pangenomes]].
