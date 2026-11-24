---
type: "Concept"
description: "Practical limits of Lakehouse annotation and metadata tables for MAG-level and NMDC-derived analysis (empty labels, missing coverage, zero-row or excluded tables, zeroed abiotic features); stops at identifier-format join failures."
sources: ["summaries/discoveries.md", "summaries/euk_in_prok_correlates__REPORT.md", "summaries/harvard_forest_warming__REPORT.md", "summaries/neon_mag_functional_discovery__REPORT.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md", "summaries/pitfalls.md"]
---
# Annotation and environmental-metadata table gaps in the Data Lakehouse

Lakehouse annotation and metadata tables have practical gaps for MAG-level (metagenome assembled genome) and NMDC-derived analysis: partial annotation coverage, empty labels, and zeroed abiotic features. [src: neon_mag_functional_discovery, harvard_forest_warming] The caveats below come from several project reports and from the central pitfalls digest, so each is stated for the dataset or source it names. [src: neon_mag_functional_discovery, harvard_forest_warming, nmdc_community_metabolic_ecology, pitfalls] The page stops at identifier-format join failures, which are covered in [[concepts/join-key-validity-and-identifier-format-mismatches]]. See also [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]].

## Literature Context

The one candidate paper describes Microbiome Datahub, an open-access platform for metagenome-assembled genomes (MAGs). It addresses a problem close to the one this page covers. The authors say MAG datasets deposited in public repositories such as INSDC are often hard to reuse. They cite heterogeneous quality, inconsistent taxonomic and functional annotations, and insufficiently curated environmental metadata [PMID 41840729](https://pubmed.ncbi.nlm.nih.gov/41840729/). They also note that secondary databases such as MGnify, IMG/M and SPIRE reconstruct MAGs de novo from public reads. These databases therefore do not represent the MAGs originally reported in publications [PMID 41840729](https://pubmed.ncbi.nlm.nih.gov/41840729/).

Their remedy is to collect 214,427 MAGs and re-annotate them uniformly. The pipeline uses DFAST for gene prediction, CheckM for quality, GTDB-Tk for taxonomy, PZLAST for MBGD ortholog clusters and KEGG Orthology IDs, and the Metagenome and Microbes Environmental Ontology for environmental metadata [PMID 41840729](https://pubmed.ncbi.nlm.nih.gov/41840729/). The abstract reports that about 19% of proteins were not assigned to MBGD ortholog clusters. The authors read this as a sign of novelty [PMID 41840729](https://pubmed.ncbi.nlm.nih.gov/41840729/). This is an abstract-level finding about that platform. It says nothing about the KBase Data Lakehouse.

The corpus's findings are consistent with the paper's general diagnosis. Both find that functional annotation and environmental metadata are incomplete and uneven, and that this limits MAG-level reuse. Examples from this page are the 57% workflow coverage of nmdc_results.annotation_kegg_orthology (1,799 / 3,137), the habitat-biased loss of soil genera, and the empty name, description and category columns in nmdc_arkin.kegg_module_terms. The Lakehouse's zeroed abiotic_features, which are all zeros for Harvard Forest, are another example. The paper's unassigned-protein fraction is a different kind of gap. It reflects possibly novel proteins, while the Lakehouse gaps come from missing or empty table content. The two should not be equated.

The corpus extends the paper in one respect. It documents specific failure modes inside a single integrated platform: a silent loss of cohort members on joins, zeros stored in place of NULL, and zero-row tables. The paper does not report these. It also leaves open how well curated ontology-based environmental annotation would fix the abiotic gaps seen here. The paper does not test that, and it gives no evidence on NMDC-derived data. Whether a re-annotation approach like Microbiome Datahub's would fill the NEON soil gap is a hypothesis, not a finding. No candidate contradicts the corpus.

## Partial per-gene annotation coverage

In the NEON data, per-gene NMDC annotation is partial and habitat-biased, so per-MAG analyses lose whole groups of genera. [src: neon_mag_functional_discovery, pitfalls]

- nmdc_results.annotation_kegg_orthology covers only 57% of NEON MetagenomeAnnotation workflows (1,799 / 3,137). [src: neon_mag_functional_discovery, pitfalls] See [[entities/nmdc-results-annotation-kegg-orthology]].
- The pitfalls digest says annotation_kegg_orthology (1.83 B rows), pfam_annotation_gff (2.68 B rows) and annotation_enzyme_commission (1.23 B rows) do not cover every MetagenomeAnnotation workflow in functional_annotation_agg. [src: pitfalls]
- The 43% gap is non-random and strongly correlated with habitat and genus. [src: pitfalls]
- Any per-MAG analysis that joins members_id to gene_id silently drops genera with zero coverage. [src: pitfalls]
- The H4 cohort of 246 MAGs collapsed to 73 MAGs across 19 genera, biased toward water habitats. [src: pitfalls]
- The later KEGG module enrichment was driven heavily by cyanobacterial photosystem modules, which the report attributes partly to biology and partly to a habitat-skewed cohort. [src: pitfalls]
- The report recorded this as a generalizable pitfall. [src: neon_mag_functional_discovery]

The NB04b cohort results by habitat group are:

| Group | Per-gene KO coverage | NB04b outcome |
|---|---|---|
| Surface-water cyanobacteria (Planktothrix, Dolichospermum, Rubrivivax) | 100% | All 27 MAGs survived [src: neon_mag_functional_discovery] |
| Benthic generalists (Ferruginibacter, Flavobacterium, UBA953) | ~85% | 16 / 19 survived [src: neon_mag_functional_discovery] |
| Soil acidobacteria (Sulfotelmatobacter, Palsa-465, Palsa-1447) | ~30% | 12 / 40 survived [src: neon_mag_functional_discovery] |
| Soil cultured genera (Mycobacterium, Bradyrhizobium, Acidoferrum) | ~10% | 5 / 65 survived [src: neon_mag_functional_discovery] |
| Soil unculturable / novel (Acidocella, BOG-234, Pseudolabrys, Pseudonocardia, Reyranella) | 0% | 0 / 28 survived [src: neon_mag_functional_discovery, pitfalls] |

Whether pfam_annotation_gff and annotation_enzyme_commission fill the soil gap is unknown. Bounded SQL (structured query language) could not query their per-workflow coverage. [src: neon_mag_functional_discovery] The pitfalls digest advises querying coverage per study and habitat first and treating effect sizes as cohort-conditional. [src: pitfalls]

## Empty labels and sparse compound IDs

Reference tables can hold identifiers without readable labels, and metabolite tables carry few KEGG IDs. [src: neon_mag_functional_discovery, discoveries]

- nmdc_arkin.kegg_module_terms has empty name, description and category columns for all 370 modules. Only module_id is populated. [src: neon_mag_functional_discovery]
- The NEON report therefore resolved module IDs and names against an external KEGG reference. [src: neon_mag_functional_discovery] This limited its habitat interpretation. [src: neon_mag_functional_discovery] See [[entities/kegg]].
- Only ~2% of compounds in nmdc_arkin.metabolomics_gold have KEGG compound IDs. [src: discoveries] Separately, the community metabolic ecology report gives a 2% annotation rate for KEGG compound IDs in the NMDC data. It says this limits KEGG-based matching and leaves cysteine, histidine and lysine untestable. [src: nmdc_community_metabolic_ecology] The claims do not state that the two figures describe the same population.
- Those three amino acid pathways (cys, his, lys) lack KEGG compound annotations. The report says improving this would expand the H1 test set from 13 to 16 testable pathways. [src: nmdc_community_metabolic_ecology]
- All 33 Freshwater samples lacked paired NMDC metabolomics. They were excluded from H1 but kept for H2 (principal component analysis, PCA) using pathway completeness alone. [src: nmdc_community_metabolic_ecology]

## Zeroed or absent environmental features

Abiotic metadata were often unusable, which removes environmental covariates. [src: harvard_forest_warming, nmdc_community_metabolic_ecology, pitfalls]

- The abiotic_features table stores 0.0 rather than NULL for unmeasured variables. The pitfalls digest recommends replacing zeros with NaN (not a number) before analysis. [src: pitfalls] It also notes there is no annotations_water_content column. [src: pitfalls]
- Harvard Forest abiotic_features are all zeros, which the report calls an NMDC parsing artifact specific to that study. No soil temperature, pH or nitrogen measurements are in the Lakehouse. The +5°C treatment label is the only environmental contrast. [src: harvard_forest_warming]
- In the community metabolic ecology report, abiotic features were all NaN for the 174-sample matrix. This prevented partial correlations controlling for gradients that could confound H1 and H2. [src: nmdc_community_metabolic_ecology] See [[concepts/confounding-and-robustness-in-environmental-metabolomics-genomics-association]].
- The NEON soil study in euk_in_prok_correlates has zero non-null depth values. Its depth association is therefore cross-study and not part of the batch-controlled result. [src: euk_in_prok_correlates]
- NMDC does not populate DNA-extraction kit, size fractionation/filtration, host-depletion method or library-prep fields, so wet-lab factors cannot be tested. [src: euk_in_prok_correlates] Processing booleans in biosample_to_workflow_run are near-constant, and has_filtration is all false. [src: euk_in_prok_correlates] See [[concepts/unmeasured-wet-lab-metadata-as-a-limit-on-contamination-correlates]].

## Excluded, empty or unbalanced tables

- The nmdc_arkin _gold tables return zero NEON rows. [src: neon_mag_functional_discovery] The NEON report excluded them by design, along with external NEON portal data (climate stations, vegetation, eddy-covariance). [src: neon_mag_functional_discovery]
- Harvard Forest used only nmdc_metadata and nmdc_results tables. [src: harvard_forest_warming] It therefore has no quantitative metabolomics, NOM or proteomics, although equivalent layers exist in nmdc_arkin.{nom_gold, metabolomics_gold, proteomics_gold}. [src: harvard_forest_warming]
- Harvard Forest omics coverage is unbalanced because the NMDC pipeline produced no metagenomes for organic-direct or some mineral-direct samples. This drives the H1 sensitivity caveat. [src: harvard_forest_warming]
- All Harvard Forest organic-horizon DNA samples are lab-incubated, because direct organic DNA was not produced. Incubation cannot be factored out cleanly. [src: harvard_forest_warming]
- data/nmdc_metabolomics_coverage.csv has 0 rows. It was saved before the omics_files_table bridge was found and is superseded by analysis_ready_matrix.csv. [src: nmdc_community_metabolic_ecology]
- The four kescience_structural_biology tables start empty and grow with Phenix agent usage, so cross-project queries return nothing until projects accumulate. [src: pitfalls]
- In planetmicrobe_planetmicrobe and planetmicrobe_planetmicrobe_raw, the project and library tables are empty (count=0), so joins through them return nothing. [src: pitfalls]

## Open Directions

- Query per-workflow coverage of pfam_annotation_gff and annotation_enzyme_commission for NEON soil workflows. This would show whether they fill the soil-genus gap left by annotation_kegg_orthology.
- Repeat the H4 cohort analysis with coverage-stratified weighting by habitat. This would separate real photosystem enrichment from habitat skew.
- Recover the Harvard Forest abiotic measurements from NMDC source records, or add the nmdc_arkin gold layers. This would give a covariate beyond the treatment label.
- Rerun the community metabolic ecology matrix with zeros converted to NaN and a check for any real abiotic values. This would show whether partial correlations are possible.
- Ingest the 221 SSO sample-tube geochemistry values, so the registered samples have linked assays.
