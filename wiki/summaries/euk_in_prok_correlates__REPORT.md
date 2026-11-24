---
type: "Summary"
description: "Summary of the project Metadata Correlates of Eukaryotic Contamination in NMDC Prokaryote-Targeted Metagenomes."
doc_type: "short"
full_text: "sources/euk_in_prok_correlates__REPORT.md"
---
# Metadata Correlates of Eukaryotic Contamination in NMDC Prokaryote-Targeted Metagenomes

Summary of the project Metadata Correlates of Eukaryotic Contamination in NMDC Prokaryote-Targeted Metagenomes. The report's headline is a cautionary result: within a single public collection, the eukaryotic fraction is so strongly structured by study/batch that a cross-study metadata-correlate analysis is confounded and over-claims. [src: euk_in_prok_correlates] A genuine environmental signal is recoverable only within a batch-controlled soil study. [src: euk_in_prok_correlates]

## Key Findings

### Prevalence and source of eukaryotic reads

Eukaryotic reads are widespread and mostly plant or algal. The analysis uses GOTTCHA2 classifications from 2,759 ReadbasedAnalysis runs across 9 studies. [src: euk_in_prok_correlates] The response is GOTTCHA2 relative eukaryotic abundance, combining Eukaryota and plastid at superkingdom rank, per run. [src: euk_in_prok_correlates] Of the runs, 77% carry detectable eukaryotic reads, with a median eukaryotic fraction of 2.7% and a mean of 13.3%. [src: euk_in_prok_correlates] 23% of runs have none, and 20% exceed 20% eukaryotic. [src: euk_in_prok_correlates] Among runs with detectable eukaryotic reads, plastid (chloroplast) DNA is a median 100% of the eukaryotic signal. [src: euk_in_prok_correlates] The report concludes that photosynthetic DNA, not animal-host DNA, dominates. [src: euk_in_prok_correlates]

Sources differ by sample matrix:

| Matrix | Eukaryote detection | Plastid share of eukaryotes | Main source |
|---|---|---|---|
| Aquatic (freshwater) | 99.5% | 1.00 | algal plastid [src: euk_in_prok_correlates] |
| Terrestrial (soil) | 55.7% | 0.43 | plant plastid plus soil fungi/protists [src: euk_in_prok_correlates] |
| Plants (roots) | 100% | 0.03 | root-associated fungi/protists, non-plastid [src: euk_in_prok_correlates] |

The report reads this as co-sampled photosynthetic environmental DNA rather than laboratory or animal-host contamination. [src: euk_in_prok_correlates] It proposes that the magnitude is set at collection, by sample composition and dilution by microbial biomass. [src: euk_in_prok_correlates] This is consistent with the near-absence of any sequencing-platform or read-depth effect once environment is considered. [src: euk_in_prok_correlates]

### Univariate association with environment, and its confounding

The univariate association with matrix is strong. The Kruskal–Wallis test gives H=77.8, p=1.3×10⁻¹⁷, and all pairwise matrix contrasts are significant after BH-FDR (Benjamini-Hochberg false discovery rate) correction. [src: euk_in_prok_correlates] The report labels it strong but confounded. [src: euk_in_prok_correlates] Three points limit it:
- Once Unknown or missing metadata are excluded, ecosystem_type reduces to Soil, Freshwater and Roots. That test is identical to the matrix test and is not independent confirmation. [src: euk_in_prok_correlates]
- An earlier version kept the Unknown bucket, which has the highest median eukaryotic fraction. It reported an inflated p≈10⁻⁵⁰, which was a missingness artifact and was removed. [src: euk_in_prok_correlates]
- Each biome is ~80–100% nested within a single study, so the environment signal cannot be separated from study/batch. [src: euk_in_prok_correlates]

### Cross-study prediction fails

Gradient-boosted models of the eukaryotic fraction show that environment does not generalize across studies. [src: euk_in_prok_correlates] A study_id-only model reaches random-CV (cross-validation) R² of 0.24, which the report calls the batch ceiling. [src: euk_in_prok_correlates] The environment model reaches 0.35 under random CV, so within random CV it is somewhat higher than the study_id-only model. [src: euk_in_prok_correlates] Under out-of-study GroupKFold it falls to −0.30. [src: euk_in_prok_correlates] Adding sequencing metadata gives −0.39. [src: euk_in_prok_correlates] The report's summary is that environment explains no more variance than study_id alone, and that it does worse than predicting the mean when whole studies are held out. [src: euk_in_prok_correlates] The claims do not say how that statement reconciles with the 0.35 versus 0.24 random-CV figures, so the two are given here as the report states them. Out-of-study detection AUC (area under curve) is 0.56, about chance. [src: euk_in_prok_correlates] Platform and depth metadata do not help. [src: euk_in_prok_correlates] A naive cross-collection regression would therefore report a strong but largely spurious, batch-driven association. [src: euk_in_prok_correlates] The report recommends GroupKFold by study or within-study contrasts. [src: euk_in_prok_correlates] Its inference is non-parametric or cross-validated because of zero inflation and batch structure. [src: euk_in_prok_correlates]

### Depth (suggestive only)

Across studies, measured depth correlates negatively with eukaryotic fraction (Spearman ρ = −0.29, p=5.2×10⁻⁷, n=292 runs with measured depth). Shallower samples carry more eukaryotic DNA. [src: euk_in_prok_correlates] This is not batch-controlled. The measured-depth runs come from a handful of non-soil studies, and the dominant NEON soil study records no depth. [src: euk_in_prok_correlates] The report reads it as suggestive only. [src: euk_in_prok_correlates]

### Within-study effect in NEON soil

With batch fixed, the environment effect is real. The batch-controlled analysis restricts to the dominant NEON soil metagenome study, with 1,186 runs, one sampling program and constant protocol/batch. [src: euk_in_prok_correlates] Aboveground vegetation and geography clearly drive soil eukaryotic content, with Arctic tundra and herbaceous/wetland soils far above temperate forest/cropland. [src: euk_in_prok_correlates]
- **Vegetation:** across 11 env_local_scale levels, Kruskal H=119.1, p=7.6×10⁻²¹. [src: euk_in_prok_correlates] Median eukaryotic fractions are 23% in sedge/forb herbaceous soil, 14% in emergent wetland, 13% in dwarf scrub and 2% in evergreen forest. [src: euk_in_prok_correlates] The fraction is ≈0 in deciduous forest, cropland and pasture. [src: euk_in_prok_correlates]
- **Geography:** across 47 sites, Kruskal H=310.4, p=2.4×10⁻⁴⁶. [src: euk_in_prok_correlates] The fraction is highest at Arctic tundra sites: Utqiaġvik 30%, Caribou-Poker Creeks 22% and Toolik 17%. Temperate forests are at 2–8%. [src: euk_in_prok_correlates]
- **Prediction:** local environment plus geography gives within-study 5-fold R² = +0.17 ± 0.06. This contrasts with the cross-study R² of −0.30. [src: euk_in_prok_correlates]

The report interprets this as aboveground photosynthetic input largely setting eukaryotic contamination of soil metagenomes. [src: euk_in_prok_correlates] Metadata-field-resolved correlate analysis of eukaryotic fraction is feasible only under batch control. [src: euk_in_prok_correlates]

### Novelty and contributions

To the report's knowledge, this is the first attempt to regress a measured eukaryotic read fraction against collection, processing and sequencing metadata within a standardized public multi-omics collection (NMDC). [src: euk_in_prok_correlates] It contributes a reusable run-level eukaryotic-fraction pipeline over NMDC nmdc.results. [src: euk_in_prok_correlates]

### Relation to the literature

- Matrix/biome as the primary correlate aligns with Eisenhofer, Alberdi & Woodcroft (2026, mSystems, PMID 41854267), who report biome-specific prokaryotic fraction across 136,284 metagenomes. [src: euk_in_prok_correlates]
- It also aligns with Sobolev et al. (2025, IJMS, PMID 41373768), who show sample matrix with extraction kit drives eukaryotic admixture. [src: euk_in_prok_correlates]
- Plastid/chloroplast dominance matches Chevokina et al. (2025, Front Plant Sci, PMID 41560914) and plant-host-depletion literature including Wang et al. (2026, Plant Biotechnol J, PMID 41078118). [src: euk_in_prok_correlates]
- Anthony et al. (2024, Environ Microbiome, PMID 39095861) attribute poor soil metagenome resolution to plant/eukaryotic DNA. [src: euk_in_prok_correlates]
- Batch confounding qualifies the Eisenhofer et al. cross-collection correlate, which is essentially biome, because within NMDC a biome correlate is inseparable from study/batch. [src: euk_in_prok_correlates]
- It connects to Salter et al. (2014, BMC Biology, PMID 25387460), who identify biomass/batch as the master variable. [src: euk_in_prok_correlates]
- It also connects to Ortiz-Chura et al. (2024, Anim Microbiome, PMID 39456104), who quantify metadata and structure limitations of public collections (>40% missing basic fields). [src: euk_in_prok_correlates]
- The within-study vegetation/geography effect aligns with Holm et al. (2025, Environ Microbiome, PMID 40708004), which links vegetation, land use and geography to soil microbial variation. [src: euk_in_prok_correlates]

### Practical guidance

- Kraken2 and Centrifuge show domain-level Eukaryota signals of ≈0 because their NMDC reference databases are prokaryote-restricted. GOTTCHA2 is the only usable estimator here. [src: euk_in_prok_correlates] Kraken's only eukaryotic kingdom is Metazoa/human. [src: euk_in_prok_correlates] The report recommends GOTTCHA2, which is plastid- and eukaryote-aware. [src: euk_in_prok_correlates]
- Aggregate each classifier to one row per workflow_run_id before joining metadata, because the kraken2_classification_report table has ~29M rows. [src: euk_in_prok_correlates]
- Analyse at the workflow_run_id level. NMDC pools biosamples in 1,067/2,759 runs, so biosample-level joins inflate n through pseudoreplication. [src: euk_in_prok_correlates]
- Native nmdc.results tables bridge to biosamples and studies through biosample_to_workflow_run and biosample_set_associated_studies. This links 99%+ of classified runs. [src: euk_in_prok_correlates]

## Data and Methods

The data are native GOTTCHA2 results for 2,759 runs in 9 studies. [src: euk_in_prok_correlates] Tests are Kruskal–Wallis and Mann–Whitney with BH-FDR, plus gradient boosting with GroupKFold by study. [src: euk_in_prok_correlates]
- nmdc_results supplies gottcha2_classification_report, kraken2_classification_report and centrifuge_output_report_file for per-run read-based taxonomy and eukaryotic fraction. [src: euk_in_prok_correlates]
- nmdc_metadata supplies biosample_set, biosample_to_workflow_run, biosample_set_associated_studies, data_generation_set* and instrument_set for environment, collection and sequencing predictors and study linkage. [src: euk_in_prok_correlates]
- kbase_nmdc_arkin supplies gottcha_gold, kraken_gold, centrifuge_gold and omics_files_table for the initial classifier snapshot and feasibility scan. [src: euk_in_prok_correlates]

## Caveats and Open Work

### Limits

- Only GOTTCHA2 can estimate eukaryotic reads here. [src: euk_in_prok_correlates] Its values are database-dependent and should be read as relative/ordinal, not calibrated absolute contamination. [src: euk_in_prok_correlates]
- Study and batch confounding blocks any cross-study environment claim. [src: euk_in_prok_correlates]
- NMDC's read-based taxonomy spans only ~9 studies, with one soil study at ≈43% of runs, so the cross-study generalization test is under-powered. [src: euk_in_prok_correlates]
- The data-landscape scan found no on-system source with per-sample eukaryotic read fraction across many studies. MGnify is a MAG (metagenome assembled genomes) catalog, SPIRE/GEM/Tara are MAG collections, and EMP (Earth Microbiome Project) is 16S. [src: euk_in_prok_correlates]
- The within-study result is demonstrated for one soil study only and may not extend to aquatic or host-associated collections. [src: euk_in_prok_correlates]
- Even within the study, env_local_scale and geography may track sampling-campaign sub-batches, so within-study control is not randomized. [src: euk_in_prok_correlates]
- NMDC does not populate DNA-extraction kit, size fractionation/filtration, host-depletion method or library-prep fields, so wet-lab factors cannot be tested. [src: euk_in_prok_correlates] Processing booleans in biosample_to_workflow_run are near-constant, with has_filtration all false. [src: euk_in_prok_correlates] Host depletion and extraction kit, the strongest literature levers, remain in the unmeasured residual. [src: euk_in_prok_correlates]
- 1,067 of 2,759 runs pool multiple biosamples and inherit metadata from a single representative biosample (MIN(biosample_id)). [src: euk_in_prok_correlates] Differing local metadata injects predictor label noise, a conservative bias that can only weaken associations, not manufacture them. [src: euk_in_prok_correlates]

### Proposed next analyses

- Break the batch confound with more studies, for example the SPF corpus (136K metagenomes / thousands of studies) or a broader collection, to enable a properly powered cross-study analysis. [src: euk_in_prok_correlates]
- Extend the within-study design to aquatic and plant-associated studies to test whether the vegetation/geography effect generalizes beyond soil. [src: euk_in_prok_correlates]
- Test whether the algal-plastid versus root-fungal source split holds within batch-controlled cohorts. [src: euk_in_prok_correlates]
- Acquire wet-lab metadata (extraction kit, host-depletion method, size fraction) to test the strongest literature levers that NMDC omits. [src: euk_in_prok_correlates]
- Calibrate GOTTCHA2 eukaryotic fraction against a spike-in or SPF estimate to move from ordinal to calibrated estimates. [src: euk_in_prok_correlates]

## Slots Into

- [[concepts/study-and-batch-confounding-of-cross-collection-metadata-correlates]]: environment R² falls from 0.35 under random CV to −0.30 under out-of-study GroupKFold. [src: euk_in_prok_correlates]
- [[concepts/within-study-environmental-drivers-of-eukaryotic-dna-in-soil-metagenomes]]: within NEON soil, vegetation and geography are significant and the within-study R² is +0.17. [src: euk_in_prok_correlates]
- [[concepts/sources-and-prevalence-of-eukaryotic-contamination-in-prokaryote-targeted-metagenomes]]: 77% of runs have detectable eukaryotic reads, and plastid DNA dominates. [src: euk_in_prok_correlates]
- [[concepts/classifier-and-database-limits-for-estimating-eukaryotic-read-fraction]]: Kraken2 and Centrifuge are near zero for Eukaryota, so GOTTCHA2 is the usable estimator. [src: euk_in_prok_correlates]
- [[concepts/unmeasured-wet-lab-metadata-as-a-limit-on-contamination-correlates]]: NMDC lacks extraction kit, host-depletion, size-fraction and library-prep fields. [src: euk_in_prok_correlates]
