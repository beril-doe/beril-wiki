---
type: "Dataset"
description: "NCBI BioSample environmental metadata, including isolation_source and ENVO env_broad_scale fields, used to classify genomes by environment of isolation."
sources: ["summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_strain_variation__REPORT.md", "summaries/cf_formulation_design__REPORT.md", "summaries/discoveries.md", "summaries/ecotype_env_reanalysis__REPORT.md", "summaries/env_embedding_explorer__REPORT.md", "summaries/gc_ecotype_ecology__REPORT.md", "summaries/gene_function_ecological_agora__REPORT.md", "summaries/lanthanide_methylotrophy_atlas__REPORT.md", "summaries/nmdc_context_audit__REPORT.md", "summaries/pitfalls.md", "summaries/plant_microbiome_ecotypes__REPORT.md", "summaries/prophage_ecology__REPORT.md"]
aliases: ["BioSample EAV", "ENVO", "ENVO env_broad_scale metadata", "NCBI BioSample harvest", "NCBI environment metadata", "env_broad_scale", "isolation_source", "ncbi_env", "nmdc.ncbi_biosamples"]
---
# ncbi_env environmental metadata

This page covers ncbi_env environmental metadata: NCBI BioSample fields, including isolation_source and ENVO env_broad_scale, used to classify genomes by environment of isolation. Projects use the kbase_ke_pangenome.ncbi_env table, which is EAV (entity-attribute-value) data with 4.1M rows. [src: env_embedding_explorer, gene_function_ecological_agora] See [[entities/kbase-ke-pangenome]] and [[entities/kbase-data-lakehouse]].

## Key facts

- The table has 334 distinct harmonized attribute names. [src: env_embedding_explorer]
- The most populated attributes are collection_date (273K genomes), geo_loc_name (272K) and isolation_source (245K). [src: env_embedding_explorer]
- A separate harvest, nmdc.ncbi_biosamples, holds 51,711,888 biosamples and 756,112,544 attribute rows. [src: nmdc_context_audit]
- The nmdc_context_audit report classifies it as an external re-host of NCBI data, and names NCBI BioSample as its true authority. [src: nmdc_context_audit]
- That report lists it as last committed on 2026-03-09 and as the stalest resource at about 4 months. [src: nmdc_context_audit]
- The report says the Lakehouse mirror adds an attribute-harmonization layer that makes 51.7M raw NCBI samples analytically usable. [src: nmdc_context_audit]
- The audit used the tables biosamples_flattened, biosamples_attributes, bioprojects_flattened and sra_biosamples_bioprojects to establish NCBI rather than NMDC provenance and scale. [src: nmdc_context_audit]

## How to query it

The table is EAV, not flat. Its columns are accession (BioSample ID), attribute_name, content, display_name, harmonized_name, id and package_content. [src: pitfalls] It has multiple rows per sample. [src: pitfalls] Users should pivot it or filter by harmonized_name, and should not assume one row per sample. [src: pitfalls]

To get genome metadata, join genome.ncbi_biosample_id to ncbi_env.accession. [src: pitfalls] Then filter attribute_name for isolation_source, collection_date, geo_loc_name and host, and pivot from long to wide. [src: pitfalls] One project pivoted on isolation_source, host, env_broad_scale, env_medium and lat_lon. It noted that the value column is content, not attribute_value. [src: gc_ecotype_ecology]

## Coverage

In an audit of 18,989 species, species-level coverage was 76.8% for isolation_source (text) [src: gene_function_ecological_agora], 88.8% for geo_loc_name (country/region text) [src: gene_function_ecological_agora], 48.6% for env_broad_scale (ENVO, a controlled vocabulary) [src: gene_function_ecological_agora] and 47.3% for lat_lon (numeric coordinates). [src: gene_function_ecological_agora] The same figures are restated as the report's summary of BioSample environmental metadata. [src: gene_function_ecological_agora] Another report cites 88.8% biosample geographic coverage for ecological validation. [src: discoveries]

The gene_function_ecological_agora report recommends that future kbase_ke_pangenome projects use these internal environment tables before external NMDC, MGnify or BacDive queries. [src: gene_function_ecological_agora] It found the internal tables richer than its earlier plan's external-substrate list suggested. [src: gene_function_ecological_agora]

A separate analysis counted genomes rather than species. Among the AlphaEarth genomes (see [[entities/alphaearth-environmental-embeddings]]), env_broad_scale covers 34,800 genomes (41.8%) [src: env_embedding_explorer], env_local_scale 31,541 (37.9%) [src: env_embedding_explorer] and env_medium 31,483 (37.8%). [src: env_embedding_explorer] The report states the env_broad_scale figure as 42%. [src: env_embedding_explorer]

## ENVO env_broad_scale

The env_broad_scale ENVO ontology field is cleaner than isolation-source text but covers only 42% of genomes. [src: env_embedding_explorer] Many values are bare ENVO IDs without labels, or generic terms such as "not applicable" and "missing". [src: env_embedding_explorer] Where available, terms such as "marine biome [ENVO:00000447]" give standardized categories. [src: env_embedding_explorer] The ecotype_env_reanalysis report proposes repeating its analysis with these terms, since they may classify environments more accurately. [src: ecotype_env_reanalysis] The env_embedding_explorer report proposes comparing ENVO-based classification with keyword harmonization to assess accuracy. [src: env_embedding_explorer]

## Uses in projects

- amr_environmental_resistome: 280,337 genomes have ncbi_env data, with 93.5% classified per genome. [src: amr_environmental_resistome] It wrote data/genome_environment.csv with 280,337 rows. [src: amr_environmental_resistome] Majority-vote species environments cover 95% of species (13,981 species). [src: amr_environmental_resistome]
- amr_strain_variation: the NCBI keyword classifier assigns environments to 91% of species (1,190/1,307). [src: amr_strain_variation]
- plant_microbiome_ecotypes: plant association was determined for 293,059 GTDB r214 genomes using primary NCBI isolation_source regex matching, ncbi_env EAV cross-validation and BacDive isolation records. [src: plant_microbiome_ecotypes] ncbi_env cross-validation upgraded 695 genomes. [src: plant_microbiome_ecotypes] The report used ncbi_env for environmental metadata for genome classification. [src: plant_microbiome_ecotypes]
- prophage_ecology: classification of 293,050 genomes via NCBI isolation_source yielded 10 categories with ≥30 species. [src: prophage_ecology]
- cf_formulation_design: the report queried NCBI environmental metadata for all pangenome genomes in its five formulation species to assess lung association. [src: cf_formulation_design]

## Caveats

- Per-genome parsing in amr_strain_variation gave 52.7% "Unknown" labels (94,957/180,025 genomes), because most BioSample records lack structured isolation metadata. [src: pitfalls] The same report found that only 2 species had enough within-species environmental diversity for chi-squared testing under strict expected-frequency criteria. [src: amr_strain_variation]
- Collection dates are incomplete: only 70% of genomes had parseable dates. [src: amr_strain_variation] The report suggests this, rather than a true absence of trends, explains its null temporal result. It cites documented AMR expansions in S. aureus and K. pneumoniae. [src: amr_strain_variation]
- Clinical isolates are heavily overrepresented in NCBI, and soil and aquatic species are undersampled. The "clinical species carry more AMR" finding therefore partly reflects that clinical species are sequenced because they have AMR. [src: amr_environmental_resistome]
- In prophage_ecology, isolation_source is sparse and inconsistently labeled, and its 10 categories collapse substantial within-category variation. [src: prophage_ecology] The "other_unknown" category holds 9,659 species (35%), which limits statistical power. [src: prophage_ecology]
- In lanthanide_methylotrophy_atlas, the classification is text-mining-derived with hierarchical regex priorities. Its host_associated class is broad and includes gut, skin, oral and infection contexts. [src: lanthanide_methylotrophy_atlas] Misclassifications are possible, but the report states that soil/sediment enrichment and host depletion survive. [src: lanthanide_methylotrophy_atlas]

See also [[concepts/harmonizing-free-text-isolation-source-and-environment-metadata]] and [[concepts/sampling-bias-and-metadata-sparsity-in-amr-resistome-surveys]].
