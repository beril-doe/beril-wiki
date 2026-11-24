---
type: "Dataset"
description: "The Lakehouse pangenome collection (gene clusters, per-species pangenome statistics and phylogenetic distance tables) used for pangenome context across projects; excludes the platform itself and the GTDB taxonomy."
sources: ["summaries/acinetobacter_adp1_explorer__REPORT.md", "summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/alphafold_msa_annotation__REPORT.md", "summaries/amr_cofitness_networks__REPORT.md", "summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_fitness_cost__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md", "summaries/amr_strain_variation__REPORT.md", "summaries/annotation_gap_discovery__REPORT.md", "summaries/bacillota_b_subsurface_accessory__REPORT.md", "summaries/berdl_data_atlas__REPORT.md", "summaries/cf_formulation_design__REPORT.md", "summaries/clay_confined_subsurface__REPORT.md", "summaries/cofitness_coinheritance__REPORT.md", "summaries/cog_analysis__REPORT.md", "summaries/comprehensive_metal_ecology__REPORT.md", "summaries/conservation_fitness_synthesis__REPORT.md", "summaries/conservation_vs_fitness__REPORT.md", "summaries/costly_dispensable_genes__REPORT.md", "summaries/counter_ion_effects__REPORT.md", "summaries/ecotype_analysis__REPORT.md", "summaries/ecotype_env_reanalysis__REPORT.md", "summaries/ecotype_functional_differentiation__REPORT.md", "summaries/enigma_carbon_census_1__REPORT.md", "summaries/enigma_contamination_functional_potential__REPORT.md", "summaries/env_embedding_explorer__REPORT.md", "summaries/essential_metabolome__REPORT.md", "summaries/field_vs_lab_fitness__REPORT.md", "summaries/fitness_modules__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/fw300_metabolic_consistency__REPORT.md", "summaries/gc_ecotype_ecology__REPORT.md", "summaries/gene_copy_number_variation__REPORT.md", "summaries/lanthanide_methylotrophy_atlas__REPORT.md", "summaries/lignin_community_enrichment__REPORT.md", "summaries/metabolic_capability_dependency__REPORT.md", "summaries/metal_cross_resistance__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md", "summaries/neon_mag_functional_discovery__REPORT.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md", "summaries/oak_ridge_cultivation_gap__REPORT.md", "summaries/pangenome_openness__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md", "summaries/pgp_pangenome_ecology__REPORT.md", "summaries/phage_defense_arsenal__REPORT.md", "summaries/phb_granule_ecology__REPORT.md", "summaries/pitfalls.md", "summaries/plant_microbiome_ecotypes__REPORT.md", "summaries/prophage_amr_comobilization__REPORT.md", "summaries/prophage_ecology__REPORT.md"]
aliases: ["GTDB r214", "GTDB-r214", "KBase pangenome", "KBase pangenome clusters", "KBase pangenome collection", "KBase pangenome database", "KBase pangenome statistics table", "gene_genecluster_junction", "kbase_ke_pangenome database", "kbase_ke_pangenome.phylogenetic_tree_distance_pairs", "ke_pangenome", "pangenome cluster table", "pangenome table", "phylogenetic_tree_distance_pairs table"]
---
# kbase_ke_pangenome

The kbase_ke_pangenome collection holds 293,059 KBase ke_pangenome genomes, 27,690 GTDB species clades / pangenomes and 132.5M gene clusters. [src: berdl_data_atlas] Projects across the corpus use different subsets of its tables for pangenome context, as listed below. [src: alphafold_msa_annotation, amr_pangenome_atlas, berdl_data_atlas] The collection is attributed to Parks et al. (2022), and GTDB r214 is its taxonomic backbone. [src: conservation_fitness_synthesis, conservation_vs_fitness, lanthanide_methylotrophy_atlas] Later projects add uses for GapMind pathway scores, pangenome openness, defense and PGP marker searches, and metal-gene core/accessory classification. [src: metabolic_capability_dependency, pangenome_openness, phage_defense_arsenal, pgp_pangenome_ecology, metal_fitness_atlas] The pitfalls digest adds schema rules, row counts and coverage gaps that limit how the tables can be joined and queried. [src: pitfalls]

## Key facts

### Size

The collection holds 293,059 KBase ke_pangenome genomes, 27,690 GTDB species clades / pangenomes, 132.5M gene clusters and 1,011,650,903 KBase pangenome genes. [src: berdl_data_atlas] Another phrasing gives ~1.01 B genes across 293K genomes, 27.7K species pangenomes and 132.5M gene clusters. [src: berdl_data_atlas] One report counts 27,702 species in the pangenome database, and another counts 27,690. [src: ecotype_functional_differentiation, functional_dark_matter] Further reports use 27,702 species (PGP, metal fitness atlas, prophage AMR co-mobilization, prophage ecology) and 27,690 species (NMDC, neon, phage defense, PHB). [src: pgp_pangenome_ecology, metal_fitness_atlas, prophage_amr_comobilization, prophage_ecology, nmdc_community_metabolic_ecology, neon_mag_functional_discovery, phage_defense_arsenal, phb_granule_ecology] A gene row is one (genome, gene) pair, so 1.01B genes is about 293K genomes × ~3.4K genes per genome. [src: berdl_data_atlas] The gene table is the largest entity table, with 1,011,650,903 rows. [src: berdl_data_atlas] The same report says kbase owns 79 % of the pangenome topic in the Lakehouse. [src: berdl_data_atlas] One report calls the 293K-genome pangenome the largest annotated bacterial / archaeal collection assembled to date. [src: lanthanide_methylotrophy_atlas] The gene_cluster table has 132,531,501 clusters in the bacterial analysis. [src: alphafold_msa_annotation] One report extracted pan-bacterial data covering 293,000 genomes from the Lakehouse. [src: pathway_capability_dependency] The microbeatlas report counts 6,789 sequenced species in its pangenome join. [src: microbeatlas_metal_ecology] Environment metadata covered 293,050 genomes spanning all 27,690 species in the PHB report. [src: phb_granule_ecology]

The pitfalls digest gives approximate row counts for other tables: ~1B each for gene and gene_genecluster_junction, ~421M for genome_ani, ~93M for eggnog_mapper_annotations, ~833M for interproscan_domains, ~572M for bakta_db_xrefs and ~305M for gapmind_pathways. [src: pitfalls] The plant microbiome report used phylogenetic_tree_distance_pairs with 22.6M rows. [src: plant_microbiome_ecotypes]

For genome and pangenome work the atlas recommends this collection. It cross-references via genome_id and ncbi_taxon_id. [src: berdl_data_atlas] It serves as the canonical genome reference and cross-program join anchor, using the genome, gtdb_species_clade, gtdb_metadata, gene, gene_cluster, pangenome and alphaearth_embeddings_all_years tables. [src: berdl_data_atlas]

### Identifier conventions and pitfalls

- genome.gtdb_taxonomy_id is truncated at genus level. [src: pitfalls]
- gtdb_taxonomy_r214v1.gtdb_taxonomy_id includes species. [src: pitfalls]
- The gtdb_taxonomy_r214v1 table has a column named order, a taxonomic rank. [src: pitfalls] In Spark SQL, order is reserved and causes a parse error if unquoted in a SELECT or JOIN, so it needs backticks. [src: pitfalls]
- Species clade IDs contain a double hyphen, as in s__Escherichia_coli--RS_GCF_000005845.2. [src: pitfalls] The format is s__Genus_species--{representative_genome_id}. [src: pitfalls] Another statement gives it as s__<Genus_species>--<RS_GCF_XXXXXXXXX.X | GB_GCA_XXXXXXXXX.X>. [src: pitfalls]
- genome_id values use RS_GCF_XXXXXXXXX.X or GB_GCA_XXXXXXXXX.X format, for example RS_GCF_000005845.2. [src: pitfalls] Matching is by exact equality only. [src: pitfalls]
- gene_cluster_id values use {contig}_{number} or {prefix}_mmseqsCluster_{number}, for example NZ_CP095497.1_1766. [src: pitfalls]
- The genome_ani table uses genome1_id, genome2_id and ANI, not genome_id_1, genome_id_2 and ani, and capitalization matters. [src: pitfalls] It stores only within-species comparisons, not cross-species ANI. [src: pitfalls]
- eggnog_mapper_annotations.query_name joins to gene_cluster.gene_cluster_id, not gene.gene_id. [src: pitfalls] It is used instead of a gene_cluster_id column. [src: pitfalls]
- Bakta and InterProScan tables join on gene_cluster_id, because annotations are at cluster-representative level, not per gene. [src: pitfalls] The report joins bakta_annotations to gene_cluster directly on gene_cluster_id. [src: pitfalls] gene_genecluster_junction links to gene through gene_id for gene-to-genome mapping. [src: pitfalls]
- gene_cluster has gtdb_species_clade_id, not clade_name. [src: pitfalls] gapmind_pathways has a clade_name column. [src: pitfalls] gene has only gene_id and genome_id, with no species or clade column. [src: pitfalls]
- Gene cluster IDs are meaningful only within a species and cannot be compared across species. [src: pitfalls] To compare gene content across species, the report recommends COG categories, KEGG orthologs in KEGG_ko, or PFAM domains. [src: pitfalls]
- Cross-database Pfam joins must strip versions on the Bakta side. This was undocumented in docs/pitfalls.md for kbase_ke_pangenome and cost ~15 min of debugging. [src: phage_defense_arsenal]
- An attempt to link Fitness Browser organisms to GapMind species clades via NCBI taxonomy IDs in gtdb_metadata returned zero matches, because the column held boolean strings rather than numeric taxids. [src: metabolic_capability_dependency]
- The plant microbiome subclade analysis first mismatched bare NCBI accessions in phylogenetic_tree_distance_pairs with GTDB-prefixed IDs in genome_environment.csv, leaving is_plant_associated entirely NaN (not a number) after merging. [src: plant_microbiome_ecotypes]

### Cluster classification flags and count identities

In gene_cluster, is_core = 1 means present in ≥95% of genomes. [src: pitfalls] is_auxiliary = 1 means present in <95% and >1 genome. [src: pitfalls] is_singleton = 1 means present in exactly 1 genome. [src: pitfalls] The flags are mutually exclusive, with one flag equal to 1 per row. [src: pitfalls] They are stored as integers (0/1), not booleans, so WHERE is_core = true may fail depending on SQL dialect. [src: pitfalls] In the pangenome table, no_core + no_aux_genome equals no_gene_clusters. [src: pitfalls] no_singleton_gene_clusters is a subset of no_aux_genome, so singletons sit inside the auxiliary count. [src: pitfalls]

### Phylogenetic tables and tables that do not exist

The phylogenetic_tree table (species trees from core genes) was available as of 2026-02-11. [src: pitfalls] So was phylogenetic_tree_distance_pairs (pairwise phylogenetic distances). [src: pitfalls] Three tables referenced by other tables or project docs were not found: pangenome_build_protocol (build parameters, although a protocol_id column exists), genomad_mobile_elements (plasmid/virus annotations) and IMG_env (IMG environment metadata). [src: pitfalls] The protocol_id column is therefore a dangling reference. [src: pitfalls]

## Tables used by projects

- Acinetobacter baylyi context: genome, gene_cluster, gene_genecluster_junction, gtdb_species_clade and pangenome, covering 13 genomes and 4,891 clusters. [src: acinetobacter_adp1_explorer]
- Annotation work: gene_cluster, bakta_annotations and interproscan_domains for cluster classification, annotation quality, a UniRef100 bridge and domain hits. [src: alphafold_msa_annotation]
- Fitness Browser cofitness work: interproscan_go, interproscan_domains (Pfam) and bakta_annotations for GO terms, Pfam domains and KEGG orthology. [src: amr_cofitness_networks]
- AMR atlas: bakta_amr, gene_cluster, bakta_annotations, eggnog_mapper_annotations, bakta_pfam_domains, pangenome, genome, gtdb_taxonomy_r214v1, ncbi_env and alphaearth_embeddings_all_years. [src: amr_pangenome_atlas] See [[entities/bakta-amr]].
- Environmental resistome: bakta_amr, gene_cluster, pangenome, ncbi_env, genome, gtdb_taxonomy_r214v1 and alphaearth_embeddings_all_years. [src: amr_environmental_resistome]
- AMR fitness cost: bakta_amr and bakta_annotations for Tier 1 and Tier 2 AMR gene identification. [src: amr_fitness_cost]
- AMR strain variation: gene, gene_genecluster_junction, genome, genome_ani and ncbi_env for genome-level presence/absence, ANI (average nucleotide identity) distances and environmental metadata. [src: amr_strain_variation]
- Annotation gaps: genome, gene_cluster, gene_genecluster_junction, eggnog_mapper_annotations, bakta_annotations and gapmind_pathways. [src: annotation_gap_discovery]
- Bacillota_B: gtdb_taxonomy_r214v1, genome, gtdb_metadata, ncbi_env, gene, gene_genecluster_junction, gene_cluster, eggnog_mapper_annotations, bakta_pfam_domains and bakta_annotations, including protein sequences for a CXXCH motif scan. [src: bacillota_b_subsurface_accessory]
- Clay subsurface: ncbi_env, genome, gtdb_metadata, gtdb_taxonomy_r214v1, gene, gene_genecluster_junction, eggnog_mapper_annotations and gapmind_pathways. [src: clay_confined_subsurface]
- CF formulation: genome, gapmind_pathways and ncbi_env for GapMind metabolic predictions and environmental metadata for 499+ genomes in 6 species clades. [src: cf_formulation_design]
- Cofitness coinheritance: genome-by-cluster presence matrices from gene_genecluster_junction and gene via Spark, and pairwise genome distances from phylogenetic_tree_distance_pairs. [src: cofitness_coinheritance]
- COG analysis: gene_cluster, gene_genecluster_junction and eggnog_mapper_annotations. [src: cog_analysis]
- Metal ecology: eggnog_mapper_annotations, gene_genecluster_junction, gene_cluster, genome and gtdb_taxonomy_r214v1, for KO density per genus from MAG pangenomes. [src: comprehensive_metal_ecology]
- Costly dispensable genes: gene_cluster, gene_genecluster_junction and eggnog_mapper_annotations for pangenome gene clusters, gene-to-cluster mappings and functional annotations. [src: costly_dispensable_genes]
- Counter-ion effects: gene_cluster for core/accessory classification via the FB-pangenome link. [src: counter_ion_effects]
- Ecotype analysis: alphaearth_embeddings (environmental embeddings for geographic coordinates), genome (metadata and taxonomy), ncbi_env (NCBI environmental and isolation-source metadata), pangenome (composition per species) and gene_cluster (presence/absence profiles). [src: ecotype_analysis]
- Ecotype reanalysis: genome, alphaearth_embeddings_all_years, genome_ani, gene and gene_genecluster_junction. [src: ecotype_env_reanalysis]
- Ecotype functional differentiation: pangenome, genome, gene, gene_cluster, gene_genecluster_junction and eggnog_mapper_annotations, across 27,702 bacterial species. [src: ecotype_functional_differentiation]
- ENIGMA carbon census: KEGG/EC/eggNOG functional annotations, with a null denominator of 3109 genomes. [src: enigma_carbon_census_1]
- ENIGMA contamination: gtdb_species_clade, pangenome, gene_cluster and eggnog_mapper_annotations for the taxonomy bridge and COG-derived features. [src: enigma_contamination_functional_potential]
- Environment embedding explorer: alphaearth_embeddings_all_years (64-dim embeddings, cleaned lat/lon, taxonomy) and ncbi_env (EAV format). [src: env_embedding_explorer]
- Essential metabolome: gapmind_pathways and genome, giving 305M predictions over 293K genomes. [src: essential_metabolome]
- Field vs lab fitness: pangenome gene clusters classified as core, auxiliary or singleton. [src: field_vs_lab_fitness]
- Fitness modules: gene_cluster for cluster assignments in cross-organism alignment. [src: fitness_modules]
- Functional dark matter: gene_cluster, gene, gene_genecluster_junction, genome, eggnog_mapper_annotations, gtdb_species_clade, gtdb_taxonomy_r214v1, gtdb_metadata, ncbi_env, alphaearth_embeddings_all_years and gapmind_pathways. [src: functional_dark_matter]
- FW300 metabolic consistency: gapmind_pathways. [src: fw300_metabolic_consistency]
- GC ecotype ecology: a master table of 293,059 GTDB-r214 genomes, 84% with NCBI isolation_source, plus a within-species ANI table. [src: gc_ecotype_ecology]
- Gene copy number variation: gene, gene_genecluster_junction, gene_cluster, genome, eggnog_mapper_annotations, pangenome and gtdb_species_clade. [src: gene_copy_number_variation]
- Lanthanide atlas: eggnog_mapper_annotations, bakta_annotations, gene, gene_genecluster_junction, gene_cluster, genome, gtdb_taxonomy_r214v1 and ncbi_env. [src: lanthanide_methylotrophy_atlas] All its H1/H2/H3 phylogenetic stratification uses GTDB phylum, class, family and genus assignments. [src: lanthanide_methylotrophy_atlas]
- The lignin-enrichment study uses user-provided amplicon data, not Lakehouse queries. [src: lignin_community_enrichment] It proposes mapping lignin-enriched Pseudomonas, Acinetobacter and Comamonas to kbase_ke_pangenome for lignin-degradation gene annotations and aromatic catabolism pathway presence. [src: lignin_community_enrichment]
- Metabolic capability dependency: gapmind_pathways, pangenome and gtdb_metadata for pathway completeness predictions (305M rows, 80 pathways, 293K genomes), pangenome openness and NCBI taxonomy for organism matching. [src: metabolic_capability_dependency]
- Metal cross-resistance: the collection via ortholog groups for core/accessory genome classification. [src: metal_cross_resistance]
- Metal fitness atlas: gene_cluster and eggnog_mapper_annotations for core/accessory classification and functional annotations. [src: metal_fitness_atlas]
- MicrobeAtlas metal ecology: bakta_amr, gene_cluster and gtdb_species_clade for species-level metal AMR annotations and GTDB taxonomy. [src: microbeatlas_metal_ecology] Raw source data in arkinlab_microbeatlas and kbase_ke_pangenome reside in the Lakehouse and are accessible to KBase users. [src: microbeatlas_metal_ecology]
- NEON MAG functional discovery: gtdb_species_clade, gene_cluster and eggnog_mapper_annotations for a 27,690-species pangenome, accessory gene clusters and KO assignments. [src: neon_mag_functional_discovery]
- NMDC community metabolic ecology: gapmind_pathways, gtdb_species_clade and pangenome for GapMind completeness scores (305M rows), GTDB taxonomy bridging and per-species statistics. [src: nmdc_community_metabolic_ecology]
- Oak Ridge cultivation gap: genome, gene, gene_genecluster_junction, bakta_db_xrefs, gtdb_metadata and ncbi_env for functional annotations of a revised subsurface MAG cohort. [src: oak_ridge_cultivation_gap]
- Pangenome openness: the pangenome table via Spark supplies pre-computed openness metrics per species. [src: pangenome_openness]
- Pathway capability dependency: gapmind_pathways with 305M rows. [src: pathway_capability_dependency]
- PGP pangenome ecology: bakta_annotations and gene_cluster for PGP gene cluster extraction with core/auxiliary/singleton flags [src: pgp_pangenome_ecology]; pangenome for species-level genome counts and core/accessory baselines [src: pgp_pangenome_ecology]; gtdb_metadata for per-genome ncbi_isolation_source [src: pgp_pangenome_ecology]; genome for the genome_id to species mapping [src: pgp_pangenome_ecology]; gtdb_taxonomy_r214v1 for phylum/family/genus taxonomy in phylogenetic controls [src: pgp_pangenome_ecology]; and gapmind_pathways for GapMind tryptophan and tyrosine completeness scores. [src: pgp_pangenome_ecology]
- Phage defense arsenal: interproscan_domains, eggnog_mapper_annotations, bakta_pfam_domains, gene_cluster, pangenome, gtdb_metadata, gtdb_taxonomy_r214v1 and genome for defense-marker Pfam hits, core/aux/singleton flags, phylum and genome-size covariates, and species-level pangenome statistics. [src: phage_defense_arsenal]
- PHB granule ecology: eggnog_mapper_annotations, gene_cluster, gtdb_species_clade, pangenome, genome, ncbi_env and alphaearth_embeddings_all_years for PHB gene identification, taxonomy, environment metadata and environmental embeddings. [src: phb_granule_ecology] It also uses gtdb_metadata to bridge NCBI taxid to GTDB genus for NMDC cross-validation. [src: phb_granule_ecology]
- Plant microbiome ecotypes: genome, gene_cluster, pangenome, gtdb_taxonomy_r214v1, gtdb_metadata, bakta_annotations, bakta_pfam_domains, eggnog_mapper_annotations and gapmind_pathways for core pangenome data, functional annotations and pathway predictions. [src: plant_microbiome_ecotypes] It also used phylogenetic_tree and phylogenetic_tree_distance_pairs for within-species phylogenetic distances for subclade clustering (Phase 2). [src: plant_microbiome_ecotypes]
- Prophage AMR co-mobilization: bakta_amr, bakta_annotations and bakta_pfam_domains for AMR and prophage marker identification [src: prophage_amr_comobilization]; gene, gene_genecluster_junction and gene_cluster for gene coordinates and cluster membership [src: prophage_amr_comobilization]; and genome, pangenome and gtdb_taxonomy_r214v1 for species membership, genome counts and taxonomy. [src: prophage_amr_comobilization]

## Coverage and query caveats

- Twelve pangenome records reference species clades absent from gtdb_species_clade. [src: pitfalls] Examples are s__Portiera_aleyrodidarum--RS_GCF_000300075.1, s__Profftella_armatura--RS_GCF_000441555.1 and s__Nanosynbacter_sp022828325--RS_GCF_022828325.1, mostly symbionts and single-genome species. [src: pitfalls] They are valid pangenomes filtered from species metadata, so a LEFT JOIN retains them. [src: pitfalls]
- gene_genecluster_junction has 141 orphan genes relative to gene, which an INNER JOIN silently drops. [src: pitfalls]
- alphaearth_embeddings_all_years covers only ~28% of genomes (~83K/293K) because NCBI latitude/longitude are sparse, so use LEFT JOIN and check coverage. [src: pitfalls]
- The big tables should never be full-scanned. Pre-filter by gtdb_species_clade_id or genome_id before joining. [src: pitfalls]
- Pagination needs ORDER BY, because LIMIT/OFFSET without ordering returns inconsistent results. [src: pitfalls]
- The REST API returns transient 503 errors ("cannot schedule new futures after shutdown") and 504 errors on large queries. The report advises retrying or batching per species. [src: pitfalls]
- Only 18 (28%) of 65 plant-associated species with ≥20 genomes have phylogenetic-tree distance data in phylogenetic_tree_distance_pairs. [src: plant_microbiome_ecotypes] The report calls the 47/65 gap a database limitation, not a methodology issue. [src: plant_microbiome_ecotypes] It limits the full 65-species subclade scan. [src: plant_microbiome_ecotypes] See [[concepts/within-species-subclade-segregation-of-plant-association-and-host-specialization]].

## Project results that rest on it

### Acinetobacter baylyi

A connection scan matched all 4,891 ADP1 database cluster IDs (identifiers) to pangenomes via mapping, a 100% match. [src: acinetobacter_adp1_explorer] All 13 Lakehouse-format genomes in that database belong to s__Acinetobacter_baylyi, clade s__Acinetobacter_baylyi--RS_GCF_000368685.1. [src: acinetobacter_adp1_explorer] That pangenome has 3,207 core and 1,684 accessory gene clusters. [src: acinetobacter_adp1_explorer]

In the deletion-phenotype project, cluster IDs and core/accessory status were cross-referenced through genome_features.pangenome_cluster_id. [src: adp1_deletion_phenotypes] Pangenome-core membership is 93.3% for present dispensable genes and 76.5% for missing dispensable genes (p = 1.4×10⁻²⁰). [src: adp1_deletion_phenotypes] The report concludes that the 272 missing dispensable genes are less conserved across Acinetobacter species. It suggests that dispensability and pangenome status are linked through evolutionary retention pressure. [src: adp1_deletion_phenotypes] Caveat: the status comes from a species-level pangenome, which may have limited resolution compared with a population-level analysis. [src: adp1_deletion_phenotypes]

### Fitness Browser linkage

The costly-dispensable-genes report adds pangenome conservation to Fitness Browser data to separate evolutionarily stable from transient phenotypic genes. [src: costly_dispensable_genes] Its core/auxiliary classification is binary, and the fraction of genomes carrying a gene would give more resolution. [src: costly_dispensable_genes] In conservation_vs_fitness, the linked genes comprise 145,821 core (82.0%) and 32,042 auxiliary (18.0%) genes, including 7,574 singletons as a subset of auxiliary. [src: conservation_vs_fitness] Four Fitness Browser organisms (Cola, Kang, Magneto, SB2B) were unmatched because their species had too few genomes in GTDB for pangenome construction. [src: conservation_vs_fitness] In field_vs_lab_fitness, the Nitratidesulfovibrio vulgaris pangenome has relatively few genomes. This gives a coarse classification and a high baseline core fraction (76.3%) that compresses effect sizes. [src: field_vs_lab_fitness] The report proposes integrating module predictions with core, auxiliary and singleton classes. [src: fitness_modules]

### Metal genes and core classification

In the metal cross-resistance report, the three tiers of metal-important genes all have high core fractions. General-stress genes are 1,484 (18.2% of all metal-important genes), with mean core 92.0% and 57.2% fully core (≥95%). [src: metal_cross_resistance] Metal-shared genes are 2,306 (28.3%), with mean core 91.0% and 50.4% fully core. [src: metal_cross_resistance] Metal-specific genes are 4,372 (53.6%), with mean core 89.8% and 45.7% fully core. [src: metal_cross_resistance] The metal fitness atlas derived a signature of 1,286 KEGG KO terms from conserved metal gene families and used it to score all 27,702 pangenome species. [src: metal_fitness_atlas]

### Metabolic and pathway context

The metabolic capability report queried pangenome openness for 7,334 species from kbase_ke_pangenome.pangenome, and wrote data/pangenome_openness.csv with 7,334 rows. [src: metabolic_capability_dependency] The pathway capability Tier 2 analysis covers 2,810 GTDB species with at least 10 genomes, across 80 GapMind pathways (18 amino acid biosynthesis and 62 carbon source utilization). [src: pathway_capability_dependency] The NMDC report integrates 305M GapMind pathway records (27,690 GTDB species × 80 pathways) with NMDC multi-omics for 220 samples spanning two habitat types. [src: nmdc_community_metabolic_ecology] The pangenome_openness project also generated data/pangenome_stats.csv with pre-computed statistics for target species. [src: pangenome_openness]

### Plant growth promotion, defense and PHB

The PGP report claims the first analysis of PGP gene distribution, co-occurrence and core/accessory status across the full pangenome (27K species, 293K genomes), a ~100× scale-up over prior comparative genomic studies of PGPB. [src: pgp_pangenome_ecology] It found 11,272 of 27,702 species carrying at least one of 13 PGP gene markers, and extracted 32,736 PGP gene clusters. [src: pgp_pangenome_ecology] It has GapMind tryptophan scores for 27,690 species, and 291,279 genomes with ncbi_isolation_source, 93.5% classifiable. [src: pgp_pangenome_ecology]

Phage defense detection of seven anti-phage defense families covered 27,626 of 27,690 (99.8 %) species-level pangenomes and yielded 930,573 marker hits across 825,476 unique gene clusters. [src: phage_defense_arsenal] The arms-race and syndrome analysis set is 7,323 species passing the ≥5-genome pangenome-quality threshold. [src: phage_defense_arsenal]

For PHB, eggNOG annotations of six pathway KEGG KOs identified 118,513 gene clusters across 19,496 species. [src: phb_granule_ecology] Caveat: the pangenome includes both complete genomes and MAGs, which may have variable gene detection rates. [src: phb_granule_ecology]

### Prophage and AMR marker inventories

The full pangenome inventory contains 83,008 AMR gene clusters and 3.47 million prophage marker clusters. [src: prophage_amr_comobilization] Of 27,702 species, 14,669 (52.9%) carry both AMR and prophage markers. [src: prophage_amr_comobilization] A separate prophage ecology report found that all 27,702 species carry prophage-associated gene clusters, 4,005,537 in total identified via eggNOG annotations. [src: prophage_ecology] See [[concepts/annotation-based-prophage-detection-prevalence-and-domesticated-remnants]].

## Further project results and limits

### MicrobeAtlas metal ecology and archaea

The report joins the pangenome database (6,789 sequenced species) with a global atlas of 98,919 OTUs × 463,972 samples. [src: microbeatlas_metal_ecology] It provides data/species_metal_amr.csv with 6,789 rows. [src: microbeatlas_metal_ecology] Only 48 archaeal genera had both MicrobeAtlas representation (≥ 3 OTUs) and AMR data in the collection. [src: microbeatlas_metal_ecology] Adequate archaeal power needs ≥200 genera with AMR data, which requires expanded archaeal pangenome sequencing and annotation. [src: microbeatlas_metal_ecology] The report proposes adding environmental MAGs, particularly Thaumarchaeota, and repeating PGLS once ≥ 100 archaeal genera have AMR data. [src: microbeatlas_metal_ecology] Genus-level mean genome size came from gtdb_metadata via the REST API for 527/606 PGLS genera, and z-scored log(genome_size) was a covariate. [src: microbeatlas_metal_ecology] The 79/606 genera (13%) lacking genome size reduced PGLS n from 606 to 527, but results agreed in direction and significance with full-data models. [src: microbeatlas_metal_ecology]

### NEON and Oak Ridge cohorts

The NEON H4 test NB04 defined a community-level KO union per shared genus as KOs present in ≥ 50% of NEON workflows where the genus has a MAG, contrasted with cultured KE-pangenome accessory content. [src: neon_mag_functional_discovery] Ribosomal proteins appeared field-only in 52 of 54 cases, which the report attributes to an artifact of the is_core = false definition, not biological novelty. [src: neon_mag_functional_discovery]

The Oak Ridge report compares 3,110 ENIGMA Genome Depot cultured isolates with 2,279 QC-passing subsurface MAGs from the collection. [src: oak_ridge_cultivation_gap] Because CORAL assembly FASTAs were inaccessible, the MAGs are global rather than from ORFRC wells, so results do not directly measure the Oak Ridge cultivation gap. [src: oak_ridge_cultivation_gap] Cultured KOs came from the ENIGMA Genome Depot pipeline (unknown version), while MAG KOs came from bakta via bakta_db_xrefs. [src: oak_ridge_cultivation_gap]

### Dark genes and breadth

NB11b queries the full 27,690-species GTDB r214 pangenome. It explodes eggNOG_OGs annotations across 93.5M gene clusters and matches 11,774 dark gene root OGs, rather than using only the 48 FB organisms. [src: functional_dark_matter] Species counts per dark gene range from 1 to 27,482 (median 135, mean 2,128), and phylum counts from 1 to 142. [src: functional_dark_matter] The report maps 30,756 dark gene clusters across 27,690 species. [src: functional_dark_matter]

### Ecotype and environment work

Of 27,702 species, 457 had >= 50 genomes and 456 were eligible after COG coverage filtering. [src: ecotype_functional_differentiation] A stratified random sample of 15 species was drawn, 5 per genome-count bin (50-100, 100-200, 200-300). [src: ecotype_functional_differentiation] The AlphaEarth embeddings table covers 83,287 genomes, 28.4% of 293,059 total. [src: env_embedding_explorer] In the ecotype reanalysis, Klebsiella pneumoniae was excluded because gene cluster extraction exceeded Spark's maxResultSize. [src: ecotype_env_reanalysis] The GC ecotype report used connected components of the ANI ≥ 99% graph from genome_ani, which has no species-clade column. [src: gc_ecotype_ecology] It pivoted ncbi_env from EAV to wide format using content as the value column, and took GC content and genome size from gtdb_metadata as string-typed values cast to numeric. [src: gc_ecotype_ecology] Its phylogenetic regression used the top-10 PCoA axes from branch_distance in phylogenetic_tree_distance_pairs. [src: gc_ecotype_ecology]

### Coverage limits

COG annotations cover ~70% of genes in the COG analysis, and unassigned genes may skew distributions. [src: cog_analysis] Escherichia coli genomes are completely absent from GapMind in this collection. [src: essential_metabolome] The report attributes this to E. coli being excluded from GTDB pangenome construction for having too many genomes for species-level analysis. [src: essential_metabolome] Gene copy number work found the three-way join of gene, gene_genecluster_junction and gene_cluster (~1B rows each) took 140–290 s per species, median ~200 s. [src: gene_copy_number_variation] It estimates ~80 min for a 24-species pilot and recommends CTS batch processing for 100+ species. [src: gene_copy_number_variation] That study tested 24 species across 5 phyla with one pipeline, unlike prior work on single pairs or organisms. [src: gene_copy_number_variation] The ENIGMA taxonomy bridge parsed 27,690 GTDB species rows. [src: enigma_contamination_functional_potential] That report contributes a reproducible ENIGMA-to-Lakehouse functional inference workflow. [src: enigma_contamination_functional_potential]

### Gene-cluster annotation

Of the bacterial gene clusters, 38,804,903 (29.3%) have a real UniProt accession via bakta_annotations.uniref100. [src: alphafold_msa_annotation] In the bacterial dataset, 111,035,431 gene clusters (83.8% of all clusters) have at least one domain annotation. [src: alphafold_msa_annotation] eggNOG annotations propagate within ≥90% AAI clusters. Strain-level marker variants, such as a single non-functional dsrA in an otherwise complete operon, may therefore be missed. [src: clay_confined_subsurface] See [[entities/eggnog-orthologous-groups]].

### AMR

The bakta_amr table has 83,008 AMRFinderPlus hits on representatives of 82,908 distinct clusters across 14,723 species. That is 53.2% of the 27,690 pangenome species. [src: amr_pangenome_atlas] It has 280,337 genomes with ncbi_env data, 93.5% classified per genome. [src: amr_environmental_resistome] One report claims the first simultaneous quantification of within-species AMR variation across >1,300 species, enabled by this resource. [src: amr_strain_variation]

For fitness cost, the report proposes scaling from 25 Fitness Browser organisms to all 293K genomes using gene-cluster conservation patterns. [src: amr_fitness_cost] A caveat applies: most Fitness Browser species have few genomes in GTDB (median 9, range 2–399). This makes the ≥95% prevalence threshold for "core" imprecise. [src: amr_fitness_cost] See [[concepts/linking-fitness-assay-genes-to-pangenome-clusters]].

### Cohorts

The Bacillota_B universe has 314 genomes in its data file. [src: bacillota_b_subsurface_accessory] The report also records 334 Bacillota_B genomes in the pangenome, much smaller than the v1.1 plan's 6,700 estimate. [src: bacillota_b_subsurface_accessory] The report does not reconcile these two figures. The clay cohort was assembled from ncbi_env using clay-related isolation_source / env_* keywords. It was joined to pangenomes via genome.ncbi_biosample_id. [src: clay_confined_subsurface]

In the CF project, the Pseudomonas aeruginosa analysis included 6,760 genomes. Of these, 5,199 had metadata and 1,796 were from lung/respiratory or CF (cystic fibrosis) sources. [src: cf_formulation_design] The report queried NCBI environmental metadata for all pangenome genomes in its five species. [src: cf_formulation_design] Its pangenome analysis covers 499 genomes across 6 species. [src: cf_formulation_design] It integrated this with the PROTECT CF Synbiotic Cocktail Study, which has 4,949 isolates from 175 CF/NCFB patient samples. [src: cf_formulation_design] The Pseudomonas FW300-N2E3 analysis used 3,200 GapMind pathway-genome pair rows for its clade. [src: fw300_metabolic_consistency]

### Query practice

Presence matrices for 11 target species were extracted with Spark by joining gene_genecluster_junction and gene, two billion-row tables. [src: cofitness_coinheritance] BROADCAST hints on small filter tables reduced query time to ~210s per organism. [src: cofitness_coinheritance] See [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]].

## Derived files

- The Fitness Browser files hold 438,000 GO rows, 228,672 Pfam rows and 41,611 KEGG rows. [src: amr_cofitness_networks] Fitness Browser genes are mapped to pangenome clusters using conservation_vs_fitness/data/fb_pangenome_link.tsv. [src: amr_cofitness_networks, amr_fitness_cost]
- AMR files: species_amr_profiles.csv (14,723 rows), species_environment.csv (26,715 rows) and genome_environment.csv (280,337 rows). [src: amr_environmental_resistome]
- AMR atlas files: amr_census.csv (83,008 rows) and amr_species_summary.csv (14,723 rows). [src: amr_pangenome_atlas]
