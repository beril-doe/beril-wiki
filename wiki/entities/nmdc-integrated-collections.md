---
type: "Dataset"
description: "National Microbiome Data Collaborative biosample registry and integrated multi-omics, embeddings and ontology tables (nmdc_metadata, nmdc_arkin)."
sources: ["summaries/berdl_data_atlas__REPORT.md", "summaries/discoveries.md", "summaries/enigma_carbon_census_1__REPORT.md", "summaries/euk_in_prok_correlates__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/gene_function_ecological_agora__REPORT.md", "summaries/neon_mag_functional_discovery__REPORT.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md", "summaries/nmdc_context_audit__REPORT.md", "summaries/phb_granule_ecology__REPORT.md", "summaries/pitfalls.md", "summaries/plant_microbiome_ecotypes__REPORT.md", "summaries/prophage_ecology__REPORT.md", "summaries/snipe_defense_system__REPORT.md"]
aliases: ["NMDC", "NMDC Arkin", "covstats_taxonomy_rollup", "nmdc_arkin", "nmdc_metadata", "nmdc_results"]
---
# NMDC integrated collections

This page covers the NMDC integrated collections: the National Microbiome Data Collaborative biosample registry and integrated multi-omics, embeddings and ontology tables (nmdc_metadata, nmdc_arkin). The inventory lists 16,640 NMDC biosamples. [src: berdl_data_atlas] An audit classifies nmdc.metadata and nmdc.results as genuine NMDC resources and kbase.nmdc_arkin as an Arkin Lab derivation that adds embeddings and traits. [src: nmdc_context_audit]

## Key facts

- nmdc_metadata.biosample_set is the NMDC biosample registry. [src: berdl_data_atlas]
- NMDC is the National Microbiome Data Collaborative, a DOE-BER program. Its LinkML-based data model defines the `*_set` schema in nmdc.metadata. [src: nmdc_context_audit]
- NMDC is also the source of metagenome annotations used in the snipe_defense_system report. [src: snipe_defense_system]
- nmdc_arkin supplies integrated multi-omics, ML embeddings, ontology and reactions through kraken_gold, gottcha_gold, metatranscriptomics_gold, nom_gold, embeddings_v1, trait_features, rhea_reactions, go_terms and ec_terms. [src: berdl_data_atlas]
- The report recommends nmdc_arkin for environmental abundance and multi-omics. Join taxa on ncbi_taxon_id and biogeochemistry on sample_id. [src: berdl_data_atlas]
- The nmdc tenant has the broadest topic coverage: 11 topics, entropy 2.61. [src: berdl_data_atlas]
- nmdc_results supplies gottcha2_classification_report, kraken2_classification_report and centrifuge_output_report_file for per-run read-based taxonomy and eukaryotic fraction. [src: euk_in_prok_correlates]
- nmdc_metadata also supplies biosample_to_workflow_run, biosample_set_associated_studies, data_generation_set* and instrument_set for predictors and study linkage. [src: euk_in_prok_correlates]
- kbase_nmdc_arkin supplies gottcha_gold, kraken_gold, centrifuge_gold and omics_files_table. One report used them for an initial classifier snapshot and feasibility scan. [src: euk_in_prok_correlates]
- The nmdc_arkin collection also supplied centrifuge_gold, omics_files_table, study_table and abiotic_features for species-level community taxonomy, sample-to-file bridging, study metadata and environmental measurements. [src: nmdc_community_metabolic_ecology]
- nmdc_arkin metabolomics_gold supplied per-sample LC-MS (liquid chromatography-mass spectrometry) metabolomics: 3.1M records across 48 studies. [src: nmdc_community_metabolic_ecology]
- Other table uses: taxonomy_features, abiotic_features, taxonomy_dim and trait_features for independent environmental validation via a genus-level taxonomy bridge and trait-condition concordance analysis. [src: functional_dark_matter]
- The prophage_ecology report used taxonomy_features, taxonomy_dim, abiotic_features and study_table for metagenomic cross-validation of prophage burden. [src: prophage_ecology]
- The plant microbiome report used taxonomy_features and study_table for community ecology co-occurrence data. [src: plant_microbiome_ecotypes]
- The PHB (polyhydroxybutyrate) report used study_table, abiotic_features, taxonomy_features, taxonomy_dim, kegg_ko_terms, metabolomics_gold, trait_features and embedding_metadata for PHB inference from taxonomic composition and abiotic correlations. [src: phb_granule_ecology]
- The NEON analysis used nmdc_metadata study, biosample, MAG (metagenome assembled genome) and workflow tables, plus per-workflow KO/COG/Pfam data in functional_annotation_agg. [src: neon_mag_functional_discovery]
- The context audit examined nmdc_metadata biosample_set, study_set, data_generation_set, workflow_execution_set and functional_annotation_agg for genuine NMDC metadata and scale/currency. [src: nmdc_context_audit]
- It treated nmdc_results annotation_kegg_orthology, annotation_statistics, gtdbtk_bacterial_summary and checkm_statistics as genuine NMDC pipeline outputs. [src: nmdc_context_audit]
- It used kbase_nmdc_arkin taxonomy_dim, metabolomics_gold, embeddings_v1, omics_files_table and study_table to characterize the Arkin-lab derivation. [src: nmdc_context_audit]
- In the P4-D1 audit of 18,989 species, NMDC species-taxid overlap covered 9.4% (1,791 species) as supplementary sample-level data. [src: gene_function_ecological_agora] The nmdc_arkin taxonomy_features table provides this P4-D1 sample-level taxa enrichment. [src: gene_function_ecological_agora]
- The snipe_defense_system report's NMDC metagenome ecosystem breakdown was limited: only 2 samples matched the API (application programming interface) query format. It suggests interactive MCP tool queries would improve coverage. [src: snipe_defense_system] Its output nmdc_duf4041_ecosystems.csv holds NMDC ecosystem category counts. [src: snipe_defense_system]

## Scale

| Layer | Count |
|---|---|
| Metatranscriptomic abundance rows (NMDC GOLD) | 75,119,498 [src: berdl_data_atlas] |
| Kraken taxonomic profile rows | 29,023,980 [src: berdl_data_atlas] |
| Gottcha taxonomic profile rows | 482,669 [src: berdl_data_atlas] |
| NOM mass spec assignments | 9,928,244 [src: berdl_data_atlas] |
| GO terms (NMDC integrated) | 48,196 [src: berdl_data_atlas] |
| EC terms (NMDC integrated) | 8,813 [src: berdl_data_atlas] |

The inventory also gives the metatranscriptomic figure as 75M rows. [src: berdl_data_atlas]

The report states, from agent memory, that the metabolomics (3.1M), proteomics (346K) and lipidomics (1.4M) layers are largely untapped. It calls NMDC a primary cross-validation source. [src: berdl_data_atlas] Use cases UC4 (nmdc and protect) and UC5 (nmdc and refdata) both rely on this multi-omics layer. [src: berdl_data_atlas] The functional_dark_matter report did not use NMDC proteomics (346K observations) or metabolomics (3.1M observations). [src: functional_dark_matter]

### Scale and currency audit

The genuine NMDC biosample universe in nmdc.metadata.biosample_set is 16,640 samples. The co-hosted NCBI mirror holds 51.7M, a ~3,000× difference not signaled by the names. [src: nmdc_context_audit] kbase.nmdc_arkin was last committed 2026-05-27 (~6 weeks). [src: nmdc_context_audit] nmdc.metadata, nmdc.results and nmdc.ref_data were last committed 2026-05-20 (~7 weeks). [src: nmdc_context_audit] Row counts on all NMDC tables, including nmdc.results.annotation_kegg_orthology at 1.83B rows, return instantly through Iceberg metadata with SELECT COUNT(*). [src: nmdc_context_audit] The berdl_data_atlas project tags Rhea/GO reference ontologies under nmdc_arkin as "NMDC integrated", which blurs provenance. [src: nmdc_context_audit]

## Genus-level abundance census

The census uses kbase.nmdc_arkin and nmdc_metadata tables: covstats_taxonomy_rollup, sample_file_lookup and biosample_set. [src: enigma_carbon_census_1]

- **Atlas size and coverage.** The atlas holds 3825 taxonomy-bearing metagenomes. The denominator is the set of covstats files with taxonomy. [src: enigma_carbon_census_1] 83/86 genera were detected in 1719 metagenomes. [src: enigma_carbon_census_1] Samples are 99% labeled through two independent ontologies, the ENVO (Environment Ontology) MIxS triad and the GOLD ecosystem path. [src: enigma_carbon_census_1]
- **Macro-environments.** The atlas has soil 2260, freshwater 723, periphyton 472, plant 119 and sediment 42. [src: enigma_carbon_census_1]
- **Labels.** Environment labels come from biosample_set. It is joined to covstats sample_id through kbase.nmdc_arkin.sample_file_lookup. [src: enigma_carbon_census_1] This gives 99% coverage across two ontologies, against ~13% for study_table GOLD alone. [src: enigma_carbon_census_1]
- **Pitfall: denominator.** Use 3825 taxonomy-bearing covstats files, not the ~6700 sample_file_lookup rows. The larger count deflates relative abundances by ~1.75×. [src: enigma_carbon_census_1]
- **Pitfall: rank.** NMDC covstats and Planet Microbe taxonomy.name are species-level. Genus-level claims need species-to-genus aggregation. [src: enigma_carbon_census_1] Any genus-level work over covstats_taxonomy_rollup or Planet Microbe run_to_taxonomy needs this rollup. [src: enigma_carbon_census_1] Filtering on bare genus names matches only near-zero genus-rank reference rows. This bug first gave 0/68 marine genera. [src: enigma_carbon_census_1]

See [[entities/planet-microbe]] and [[concepts/calibration-and-denominators-in-environmental-abundance-contrasts]].

## Taxonomy bridging to pangenomes

Two reports bridged NMDC taxon columns to GTDB genera. The functional_dark_matter report used a two-tier bridge (gtdb_metadata ncbi_taxid plus a taxonomy_dim fallback). It mapped 5 of 6 dark-gene carrier genera to 47 NMDC taxon columns across 6,365 metagenomic samples. [src: functional_dark_matter] The PHB report mapped 2,336 taxon columns through the gtdb_metadata NCBI taxid-to-GTDB-genus bridge and 678 more by direct genus matching through taxonomy_dim. [src: phb_granule_ecology] PHB inference scores for the 6,365 NMDC metagenomic samples were abundance-weighted sums of genus-level phaC prevalence, with a median 87.2% of taxonomic abundance matched to pangenome genera. [src: phb_granule_ecology] The scores correlated with depth at Spearman rho = -0.119, p = 1.14 x 10^-21. [src: phb_granule_ecology] The PHB report proposes using study_table ecosystem columns and env_triads_flattened ENVO terms for richer environmental labels. [src: phb_granule_ecology] It cautions that NMDC studies are biased toward terrestrial/soil environments and underrepresent the full environmental gradient. [src: phb_granule_ecology] See [[concepts/taxonomy-bridging-between-metagenomic-classifiers-and-reference-pangenomes]].

The prophage_ecology report applied genus-level pangenome-derived prophage burden scores to 6,365 NMDC metagenomic samples through a two-tier mapping (GTDB metadata bridge plus taxonomy_dim genus matching). [src: prophage_ecology] With 87.2% median matching coverage, it found 57 significant module-abiotic correlations (FDR < 0.05). [src: prophage_ecology]

The plant_microbiome_ecotypes report's NMDC taxonomy bridge matched 260 of 322 genera (80.7%) to GTDB. [src: plant_microbiome_ecotypes] It lost 62 genera (19.3%). [src: plant_microbiome_ecotypes] All 69 genera in 348 soil/rhizosphere samples had GapMind data across 80 pathways. [src: plant_microbiome_ecotypes] The original NMDC co-occurrence data could not support a PGP (plant growth promoting) versus pathogen exclusion C-score analysis. It held 0 PGP-dominant and 2 pathogen-dominant genera, and the remaining 67 were dual-nature. [src: plant_microbiome_ecotypes] A Phase 2b re-test on refined cohorts found 0 PGP-dominant, 3 pathogen-dominant and 66 dual-or-mixed genera among 69 NMDC co-occurring genera. [src: plant_microbiome_ecotypes]

## NEON coverage

The nmdc_arkin _gold tables return zero NEON rows. [src: neon_mag_functional_discovery] The NEON report therefore excluded them by design, along with external NEON climate-station, vegetation and eddy-covariance data. [src: neon_mag_functional_discovery] See [[entities/nmdc-neon-metagenome-studies]].

## Table schema pitfalls

### Identifiers and joins

- metabolomics_gold, kraken_gold, centrifuge_gold and gottcha_gold use file_id and file_name as primary identifiers, not sample_id. [src: pitfalls]
- Queries using sample_id on these tables raise AnalysisException: UNRESOLVED_COLUMN and stop notebook execution. [src: pitfalls]
- The recommended join key within classifier and metabolomics tables is file_id. [src: pitfalls]
- Direct file_id joins between classifier tables and metabolomics_gold always return zero rows, because the file_id namespaces do not overlap. [src: pitfalls] Classifier files use nmdc:dobj-11-* (metagenomics workflow outputs). [src: pitfalls] Metabolomics files use nmdc:dobj-12-*. [src: pitfalls]
- The two output types for the same biosample are linkable only through the biosample sample_id, such as nmdc:bsm-11-*. [src: pitfalls]
- The bridge is omics_files_table (385,562 rows, confirmed). [src: pitfalls] It has file_id, sample_id, study_id, workflow_type and file_type columns. [src: pitfalls]
- Notebook NB02 of nmdc_community_metabolic_ecology scans nmdc_arkin systematically for tables with both file_id and sample_id. [src: pitfalls]
- abiotic_features uses sample_id as its primary key. [src: pitfalls]

See [[concepts/join-key-validity-and-identifier-format-mismatches]].

### Taxonomy and metabolomics tables

- taxonomy_features has no sample_id or file_id column. Its columns are numeric NCBI taxon IDs such as 7, 11, 33 and 34. [src: pitfalls] Selecting sample_id from it fails immediately. [src: pitfalls] The report describes it as a pivoted matrix whose rows are likely samples and whose columns are taxon abundances. [src: pitfalls]
- For tidy-format joins use kraken_gold, centrifuge_gold or gottcha_gold, which have file_id, rank, name/label and abundance columns. [src: pitfalls]
- metabolomics_gold has kegg (string KEGG compound ID), chebi (double ChEBI ID), name (string), and inchi, inchikey and smiles fields. [src: pitfalls] Column names with spaces, such as Molecular Formula and Area, need backtick quoting. [src: pitfalls]
- annotation_terms_unified is a gene-annotation lookup (COG/EC/GO/KEGG terms) and cannot serve as a metabolite compound lookup. [src: pitfalls]
- trait_features represents ~90 functional groups as individual functional_group:* columns rather than rows. Long-form conversion requires stack(...), not GROUP BY. [src: pitfalls]
- Embedding dimensions vary across tables. embeddings_v1 is 256-dim, while abiotic, biochemical, taxonomy and trait embeddings differ, so a fixed dimensionality must not be assumed. [src: pitfalls]

### abiotic_features columns

Most numeric columns use a _has_numeric_value suffix, for example annotations_tot_org_carb_has_numeric_value. [src: pitfalls] The pH column, annotations_ph, has no suffix, while depth and temperature do. [src: pitfalls] Using a bare name where the suffix is required raises UNRESOLVED_COLUMN. [src: pitfalls] There is no annotations_water_content column. [src: pitfalls] The pitfalls digest recommends annotations_diss_org_carb_has_numeric_value and annotations_conduc_has_numeric_value instead. [src: pitfalls]

The column list includes sample_id, annotations_ph, and temperature, depth, maximum-depth and minimum-depth columns. [src: pitfalls] It also has total organic carbon, total nitrogen content, dissolved organic carbon, conductance, dissolved oxygen, ammonium, total phosphorus, soluble reactive phosphorus and carbon-nitrogen ratio columns. [src: pitfalls] Further columns cover chlorophyll, calcium, magnesium, potassium, manganese and sample size. [src: pitfalls]

Two statements about column types conflict. One says the columns are already double, so CAST is unnecessary but harmless. [src: pitfalls] Another says the numeric measurement columns, including annotations_ammonium_has_numeric_value, annotations_ph and annotations_temp_has_numeric_value, are STRING and need casting before numeric comparison. [src: pitfalls] Casting is safe under both. The table stores 0.0 rather than NULL for unmeasured variables, and the report recommends replacing zeros with NaN (not a number) before analysis. [src: pitfalls]

## Read-based classification runs

One report analyzed native nmdc.results GOTTCHA2 classifications from 2,759 ReadbasedAnalysis runs across 9 studies. [src: euk_in_prok_correlates] NMDC pools biosamples in 1,067/2,759 runs. Biosample-level joins therefore inflate n through pseudoreplication, and the report recommends analysis at workflow_run_id level. [src: euk_in_prok_correlates] The native tables use data_object_id and workflow_run_id keys. They link to biosamples and studies through biosample_to_workflow_run and then biosample_set_associated_studies, which links 99%+ of classified runs. [src: euk_in_prok_correlates] NMDC does not populate DNA-extraction kit, size fractionation/filtration, host-depletion method or library-prep fields. Wet-lab factors therefore cannot be tested. [src: euk_in_prok_correlates]

## Soil metabolomics and Black Queen analysis

Across 131 NMDC soil samples, the analysis correlated community-weighted GapMind amino acid biosynthesis completeness with ambient amino acid metabolomics. It used Spearman correlation. [src: discoveries] See [[entities/gapmind]] and [[concepts/black-queen-dynamics-in-amino-acid-biosynthesis]].

### Sample cohorts

The pathway matrix held 220 samples and 80 GapMind pathways (18 aa, 62 carbon). [src: nmdc_community_metabolic_ecology] Of these, 175 samples had at least one metabolomics file. [src: nmdc_community_metabolic_ecology] The H1 matrix had 131 samples with both amino acid pathway completeness and metabolomics. [src: nmdc_community_metabolic_ecology] The full merged pathway, metabolomics and abiotic matrix had 174 samples. [src: nmdc_community_metabolic_ecology] The 220-sample cohort contained 126 Soil, 33 Freshwater and 61 samples with unrecorded ecosystem type. [src: nmdc_community_metabolic_ecology] The inventory file lists ~220 rows of taxonomy and metabolomics coverage per study. [src: nmdc_community_metabolic_ecology] A classifier comparison file summarizes kraken, centrifuge and gottcha by total rows, species-rank fraction and file counts. [src: nmdc_community_metabolic_ecology]

### Results

- **Direction.** 11/13 tested pathways trend in the direction predicted by the Black Queen Hypothesis (BQH). The binomial sign test gave p = 0.011. [src: discoveries]
- **Significant pathways.** Two pathways reach FDR (false discovery rate) significance (BH-corrected). Leucine has r = −0.390, q = 0.022, n = 62. [src: discoveries] Arginine has r = −0.297, q = 0.049, n = 80. [src: discoveries]
- **Nulls.** Methionine has the largest effect (r = −0.496) but is underpowered and not significant (n = 18, q = 0.117). [src: discoveries] Tyrosine is a non-significant outlier against BQH (r = +0.42). The report suggests it likely reflects an alternative source through phenylalanine hydroxylation. [src: discoveries]
- **Robustness.** The leucine signal holds under soil-only stratification (q = 0.022 unchanged) and study-level blocking. The dataset is 95% single-study. [src: discoveries] 125/131 samples come from nmdc:sty-11-r2h77870. The other 6 come from a second study. [src: discoveries] The report states the same as 95% of samples (125/131) from nmdc:sty-11-r2h77870, with the remaining 6 from nmdc:sty-11-547rwq94. [src: nmdc_community_metabolic_ecology] The report concludes that cross-study LC-MS heterogeneity is effectively absent as a confounder. [src: discoveries] It also says the leucine signal is internally consistent within one analytical protocol. [src: discoveries] It recommends counting study-level representation before treating aggregate NMDC metabolomics as cross-study. [src: discoveries]
- **Claim of novelty.** The report calls this the first demonstration that community-weighted pangenome completeness correlates with measured metabolite pools at landscape scale using public multi-omics data. [src: discoveries]

### Ecosystem structure

PCA (principal component analysis) of the 220-sample × 80-pathway GapMind matrix gave PC1 (principal component 1) explaining 49.4% of variance. PC1 nearly separates Soil from Freshwater (Mann-Whitney p < 0.0001; median PC1 Soil = +3.86, Freshwater = −6.28). [src: discoveries] PC1 loadings are dominated by carbon utilization pathways (glucuronate, fumarate, succinate, cellobiose, galactose), not amino acid pathways. [src: discoveries] Amino acid pathways load more on PC2 (16.6%), which separates sub-clusters within Soil. [src: discoveries] 17/18 amino acid pathways differ across ecosystem types (q < 0.05, Kruskal-Wallis). The report names carbon substrate availability as the primary driver, not biosynthesis capacity. [src: discoveries] Carbon substrate range can therefore confound amino acid analyses. The report recommends PC1-residualized or ecosystem-stratified BQH tests. [src: discoveries] See [[concepts/ecosystem-differentiation-of-community-metabolic-potential]].

### Compound-matching limits

Only ~2% of compounds in nmdc_arkin.metabolomics_gold have KEGG compound IDs. [src: discoveries] Pathway matching therefore uses compound-name substrings. [src: discoveries] Substring matching risks collisions, such as leucine inside isoleucine. The report recommends first-match-wins ordering with longer patterns first. [src: discoveries] Chorismate is rarely detected. Shikimic acid and 3-dehydroshikimic acid proxy it, but they reflect precursor availability, not pool size. [src: discoveries] Three pathways (cys, his, lys) cannot be tested in the 175-sample overlap cohort because their compounds were not detected. [src: discoveries] metabolomics_gold currently lacks KEGG compound annotations for cys, his and lys. Adding them would expand the H1 test set from 13 to 16 testable pathways. [src: nmdc_community_metabolic_ecology]

## Independent validation

In functional_dark_matter, all 4 testable pre-registered predictions were confirmed using NMDC abiotic data. [src: functional_dark_matter] The report calls these independent confirmations, because the NMDC metagenomic samples are entirely separate from the pangenome-based carrier analysis. [src: functional_dark_matter]
