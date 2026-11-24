---
type: "Dataset"
description: "The KBase Data Lakehouse platform itself, which hosts the proteomics, genome feature, annotation and pangenome collections; individual collections such as kbase_ke_pangenome are separate pages."
sources: ["summaries/adp1_triple_essentiality__REPORT.md", "summaries/annotation_gap_discovery__REPORT.md", "summaries/berdl_data_atlas__REPORT.md", "summaries/caulobacter_fur_lipida_loss__REPORT.md", "summaries/comprehensive_metal_ecology__REPORT.md", "summaries/discoveries.md", "summaries/euk_in_prok_correlates__REPORT.md", "summaries/gene_function_ecological_agora__REPORT.md", "summaries/lanthanide_methylotrophy_atlas__REPORT.md", "summaries/nmdc_context_audit__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md", "summaries/pitfalls.md", "summaries/truly_dark_genes__REPORT.md", "summaries/webofmicrobes_explorer__REPORT.md"]
aliases: ["Data Lakehouse", "Lakehouse", "kbase_ke_pangenome"]
---
# KBase Data Lakehouse

The KBase Data Lakehouse inventory contains 1,740 deduplicated tables across 119 databases, 17 tenants, and 10 funding agencies / programs, spanning 17 biological topics. [src: berdl_data_atlas] It is also called the Data Lakehouse or Lakehouse. Its pangenome collection of 293K genomes is described by one report as the largest annotated bacterial / archaeal collection assembled to date. [src: lanthanide_methylotrophy_atlas]

## Key facts

- It holds ~1.01 B KBase pangenome genes across 293K genomes / 27.7K species pangenomes / 132.5M gene clusters; see [[entities/kbase-ke-pangenome]]. [src: berdl_data_atlas]
- It has 536 schema-level cross-tenant bridges, defined by 29 canonical join keys. [src: berdl_data_atlas]
- The atlas report calls it simultaneously broad (17 tenants, 10 funding programs, 17 topics) and deep (billion-row gene records and protein clusters, hundred-million-row community profile tables, tens of millions of fitness measurements). [src: berdl_data_atlas]
- The atlas surveys every accessible tenant. [src: berdl_data_atlas]
- Reference layers for biochemistry, mass spec, growth phenotype, viral genomes, and environmental embeddings are queryable from one Spark cluster. [src: berdl_data_atlas]
- The report's data/table_topic_map.csv has 1,740 rows cataloguing each tenant, agency, program, database and table with topic tags and column names. [src: berdl_data_atlas]
- The report's build_inventory.py and data_volume.py rebuild the canonical CSVs from the live cluster in ~95 s and ~60 s respectively. The report recommends rerunning them at each major ingest milestone. [src: berdl_data_atlas]
- The report proposes using its audience messages and per-entity headline numbers to seed a one-page data-availability summary on the KBase / BERIL UI. [src: berdl_data_atlas]
- One report claims the first characterization of Web of Microbes (WoM) data in a multi-collection lakehouse context. [src: webofmicrobes_explorer]
- The pathway capability report obtained its data from the Lakehouse through Spark on JupyterHub. [src: pathway_capability_dependency]

## Collections and what projects used them

- ADP1 work: the platform supplies proteomics expression across 7 Acinetobacter strains for the refined study, genome features and annotations for both studies, and pangenome cluster assignments for the original study. [src: adp1_triple_essentiality] The refined study added average log2 expression for 2,383 genes. [src: adp1_triple_essentiality] The original study's cluster_id_mapping.csv has 4,891 mappings from the Lakehouse to ADP1 pangenome cluster IDs. [src: adp1_triple_essentiality] The shared ADP1 database integrates genome features, phenotypes, flux balance analysis (FBA) predictions, and Lakehouse pangenome annotations. [src: adp1_triple_essentiality]
- Annotation gap work used kescience_fitnessbrowser (organism, experiment, genefitness, gene) for carbon source experiments, fitness scores and annotations. [src: annotation_gap_discovery] It used kbase_ke_pangenome (genome, gene_cluster, gene_genecluster_junction, eggnog_mapper_annotations, bakta_annotations, gapmind_pathways) for gene clusters, Enzyme Commission (EC)/KEGG annotations and pathway completeness. [src: annotation_gap_discovery] It used kbase_msd_biochemistry (reaction, reagent) for gapfilled reaction definitions and stoichiometry. [src: annotation_gap_discovery]
- Caulobacter work used kescience_fitnessbrowser (organism, experiment, fitbyexp_caulo, gene) for a 198-experiment Caulobacter random barcode transposon sequencing (RB-TnSeq) fitness ranking. [src: caulobacter_fur_lipida_loss] It used kescience_paperblast (gene, genepaper, snippet, curatedgene) for a literature scout and cross-species presence/absence. [src: caulobacter_fur_lipida_loss] Lakehouse fitness data gave multi-condition resolution for the envelope arm of one hypothesis, but iron-limitation experiments were unavailable in the Caulobacter Fitness Browser compendium. [src: caulobacter_fur_lipida_loss]
- Metal ecology work drew on several collections:
  - kbase_ke_pangenome supplied KEGG ortholog (KO) density per genus from metagenome assembled genome (MAG) pangenomes. [src: comprehensive_metal_ecology]
  - kescience_mgnify supplied an operational taxonomic unit (OTU) × sample abundance matrix via MicrobeAtlas for Levins' niche breadth. [src: comprehensive_metal_ecology]
  - arkinlab_microbeatlas supplied sample_metadata for pH, temperature and biome confounder checks. [src: comprehensive_metal_ecology]
  - kescience_bacdive supplied isolation, strain and taxonomy tables for geographic niche breadth, pending NB09 execution. [src: comprehensive_metal_ecology]
  - enigma_genome_depot_enigma supplied browser tables for ENIGMA FRC MAG KO content. [src: comprehensive_metal_ecology]
  - enigma_coral supplied ddt_brick0000007 for Oak Ridge FRC groundwater metal concentrations. [src: comprehensive_metal_ecology]
  - arkinlab_envdbs supplied cmmi_ores for exploratory ore deposit proximity analysis. [src: comprehensive_metal_ecology]
- An exploratory phylogenetic generalized least squares (PGLS) analysis tested 9 TIER1 KOs detectable in the pangenome against 22 environmental niche-breadth responses. [src: comprehensive_metal_ecology] Spark-side aggregation of arkinlab_microbeatlas returned 10,040 genera, of which 1,224 matched the PGLS input. [src: comprehensive_metal_ecology]
- NMDC work used kbase_nmdc_arkin (gottcha_gold, kraken_gold, centrifuge_gold, omics_files_table) for an initial classifier snapshot and feasibility scan. [src: euk_in_prok_correlates] A study-breadth scan is documented in data/01_data_landscape.md. [src: euk_in_prok_correlates] That scan found no on-system source of per-sample eukaryotic read fraction across many studies. MGnify is a MAG catalog, SPIRE/GEM/Tara are MAG collections, and Earth Microbiome Project (EMP) is 16S. [src: euk_in_prok_correlates]
- A gene-neighborhood pipeline combining the kbase_genomes feature–contig cross-walk with bakta product keyword matching is presented as reusable for cargo-on-MGE measurement. [src: gene_function_ecological_agora]
- The gene function ecological agora work used these kbase_ke_pangenome tables:
  - genome, gtdb_species_clade, gtdb_taxonomy_r214v1, gtdb_metadata and pangenome supply the core scaffold of 293K genomes / 27,690 species, genome quality, species pangenome size, and environmental isolation_source. [src: gene_function_ecological_agora]
  - gene_cluster, gene_genecluster_junction and gene provide species-specific cluster membership with ~1B junction rows. [src: gene_function_ecological_agora]
  - bakta_annotations, bakta_db_xrefs, bakta_pfam_domains and bakta_amr provide Bakta v1.12.0 reannotation of 132M cluster reps, UniRef tier mapping, AMR-Finder products, and Pfam hits. [src: gene_function_ecological_agora]
  - eggnog_mapper_annotations provides KO, COG, KEGG_Pathway, and BRITE annotations per gene_cluster. [src: gene_function_ecological_agora]
  - interproscan_domains, interproscan_go and interproscan_pathways provide authoritative Pfam annotations with 833M hits and 83.8% cluster coverage, GO, and MetaCyc plus KEGG pathways. [src: gene_function_ecological_agora]
  - kbase_genomes feature, contig_x_feature and name tables support P4-D2 gene-neighborhood cross-walking through 1B feature records with start/end/strand/contig and a 1B-row name table mapping pangenome gene_id ↔ feature_id. [src: gene_function_ecological_agora]
- Composition-based donor inference was deferred because the requisite data were unavailable on the Lakehouse. [src: gene_function_ecological_agora] Per-CDS sequence data (codon usage, k-mers) were not in its queryable schemas. [src: gene_function_ecological_agora]
- Pathway capability work used kbase_ke_pangenome.gapmind_pathways with 305M rows and cached ~3.9 GB locally across all extracts. [src: pathway_capability_dependency] Its pan-bacterial data were extracted from the Lakehouse and cover 293,000 genomes. [src: pathway_capability_dependency]
- Truly dark genes work queried the Lakehouse for Pfam, cross-references, eggNOG, gene properties, and orthologs in 02_spark_enrichment.ipynb. [src: truly_dark_genes] It used kescience_fitnessbrowser gene and ortholog for gene length, GC, position, and cross-organism orthologs. [src: truly_dark_genes] It used kbase_ke_pangenome bakta_pfam_domains, bakta_db_xrefs and eggnog_mapper_annotations for Pfam hits, database cross-references, and eggNOG functional annotations. [src: truly_dark_genes]
- Web of Microbes work used:
  - kescience_webofmicrobes compound, environment, organism, project and observation for metabolite production/excretion profiles. [src: webofmicrobes_explorer]
  - kescience_fitnessbrowser organism, gene and experiment for organism overlap and condition matching. [src: webofmicrobes_explorer]
  - kbase_msd_biochemistry molecule for compound name/formula matching for reaction-level annotation. [src: webofmicrobes_explorer]
  - kbase_ke_pangenome pangenome and gapmind_pathways for species clade counts and pathway predictions. [src: webofmicrobes_explorer]
  - The report proposes rerunning data/wom_ingest/ when newer WoM data become available, to update kescience_webofmicrobes and enable currently blocked consumption analyses. [src: webofmicrobes_explorer]

### Coverage of selected datasets

| Dataset | Coverage |
|---|---|
| kbase_ke_pangenome.ncbi_env | 88.8% biosample geographic coverage [src: discoveries] |
| kescience_mgnify | 28.4% categorical biome [src: discoveries] |
| kescience_bacdive | 32% phenotype via GCF→GCA fallback [src: discoveries] |
| kescience_fitnessbrowser | ~30 organisms with bidirectional best hit (BBH) coverage [src: discoveries] |

## Catalog currency

Historical static inventory files lagged the live catalog and omitted several databases relevant to gut-microbiome and phage work. [src: discoveries] The central digest recommends the access-aware helpers get_databases, get_tables and get_table_schema from berdl_notebook_utils for current discovery. [src: discoveries] PhageFoundry has 7 databases in the tenant, not the 5 documented. [src: discoveries] Omitted databases it lists:

- kescience_mgnify is EBI MGnify, relevant to IBD-cohort cross-validation. [src: discoveries]
- phagefoundry_ecoliphages_genomedepot, with a duplicate _genomedepot variant, holds E. coli phage genomes relevant to targeting adherent-invasive Escherichia coli (AIEC). [src: discoveries]
- kescience_interpro holds InterPro domain annotations, a primary source for virulence-factor classification. [src: discoveries]
- kescience_pubmed supports literature text mining and is a sibling of kescience_paperblast. [src: discoveries]
- pangenome_bakta is a Bakta-pangenome slice distinct from kbase_ke_pangenome. [src: discoveries]
- arkinlab_microbeatlas has 464K global 16S samples, a prevalence and biogeography baseline. [src: discoveries]
- protect_integration is a second Protect-tenant database beyond protect_genomedepot. [src: discoveries]
- u_kazakov__klebsiella_genomedepot and u_kazakov__strain_modelling hold user-owned Klebsiella phage-host work. [src: discoveries]

An audit of the NMDC collections found further catalog gaps:

- Three NMDC-related databases, nmdc_arkin, nmdc_mags and nmdc_neon, sit outside the nmdc tenant in kbase. They are invisible to users browsing the nmdc tenant because the inventory groups by catalog prefix. [src: nmdc_context_audit]
- The audited catalog has no table Comment, empty database Properties, and owner tgu2, so it gives zero human-readable context. [src: nmdc_context_audit]
- get_databases() returns both dotted Iceberg and underscore Hive aliases for every tenant database, so results need deduplication to the dotted form to avoid double-counting. [src: nmdc_context_audit] The broader namespace migration is documented repo-wide in docs/pitfalls.md. [src: nmdc_context_audit]

## Namespace, tenancy and access

See [[concepts/lakehouse-namespace-migration-tenancy-and-authentication]] and [[concepts/metadata-introspection-versus-data-read-access-in-spark-based-catalogs]]. The pitfalls digest is a quick reference for avoiding common issues when querying Lakehouse databases. [src: pitfalls]

- Collections are migrating from Delta to Iceberg. Table addresses change from underscore-joined identifiers to catalog.namespace.table identifiers, for example kbase.ke_pangenome.genome was previously kbase_ke_pangenome.genome. [src: pitfalls]
- Only the leading underscore changes; the table name is unchanged. [src: pitfalls]
- The kbase_ke_pangenome database lives under the kbase tenant, not kbase_ke. [src: pitfalls] Its ingestion configuration uses tenant "kbase" and dataset "ke_pangenome". [src: pitfalls]
- The report recommends live, access-aware catalog discovery (SET plus parsing spark.sql.catalog.*, or notebook helpers) to resolve current collection addresses. [src: pitfalls] It recommends the dotted form for migrated collections, with an underscore fallback if the dotted name is not found. [src: pitfalls]
- get_group_sql_warehouse(tenant_name) verifies tenant access, and ErrorResponse error 20040 means the user is not in the group. [src: pitfalls]
- Access failures can surface as S3 access denied, 403 Forbidden, Token denied, or AccessControlException. These reflect authorization rather than a technical fault. [src: pitfalls] The report identifies the Tenant Browser as the route to request table access. [src: pitfalls]
- DESCRIBE DATABASE EXTENDED kbase.nmdc_* raises ForbiddenException for a kesciencero/microbialdiscoveryforge principal even though COUNT(*) succeeds on the same tables. Metadata introspection and data reads therefore have different access surfaces. [src: nmdc_context_audit]
- The .env authentication variable is KBASE_AUTH_TOKEN, not KB_AUTH_TOKEN. [src: pitfalls]

## Working constraints

Only 33.3% of Bakta's 17.6M distinct UniRef50 IDs exist in kbase_uniprot.uniprot_identifier. [src: discoveries] That table has 2.5B rows. [src: discoveries] Joins touching it can exceed spark.driver.maxResultSize (1GB) via broadcast exchange. [src: discoveries] The recommended fix is SET spark.sql.autoBroadcastJoinThreshold = -1 to force sort-merge joins. [src: discoveries] The NMDC kraken2_classification_report table has ~29M rows. The report recommends aggregating each classifier to one row per workflow_run_id before joining metadata. [src: euk_in_prok_correlates]

The pitfalls digest prefers direct Spark SQL via get_spark_session() over the REST API for queries and repeated table counts. It considers the REST API acceptable for small one-off queries. [src: pitfalls]

get_spark_session from berdl_notebook_utils.setup_spark_session works in regular Python scripts on JupyterHub, so full pipelines can run from the command line without jupyter nbconvert. [src: discoveries] The auto-import in /configs/ipython_startup/00-notebookutils.py affects only notebook kernels. [src: discoveries] Running jupyter nbconvert --execute on notebooks that call spark.sql(...).toPandas() on large results causes DeadKernelError. [src: discoveries] The workaround is cache-check logic in Spark cells, so nbconvert can run locally from cached CSVs after the first JupyterHub run. Live Spark outputs should be captured interactively. [src: discoveries]

Limits on use appear in the data themselves: exact GapMind-gapfilling concordance was limited because the available Lakehouse data report pathway step counts, not individual step identities. [src: annotation_gap_discovery]

## Citations used by projects

One report names Price et al. (2018), "Mutant phenotypes for thousands of bacterial genes of unknown function," Nature 557(7706):503, as the primary citation for kescience_fitnessbrowser. [src: caulobacter_fur_lipida_loss] It names Price et al. (2021), "PaperBLAST: Text Mining Papers for Information about Homologs," mSystems 6(1):e00185-19, for kescience_paperblast. [src: caulobacter_fur_lipida_loss] It names Arkin et al. (2018), "KBase: The United States Department of Energy Systems Biology Knowledgebase," Nature Biotechnology 36(7):566-569, for the KBase infrastructure. [src: caulobacter_fur_lipida_loss]
