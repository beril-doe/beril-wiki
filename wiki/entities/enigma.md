---
type: "Dataset"
description: "ENIGMA subsurface field-sample and genome collections (enigma_coral, genome depot) for the Oak Ridge contamination gradient, including Field Research Center groundwater MAG and metal data."
sources: ["summaries/berdl_data_atlas__REPORT.md", "summaries/comprehensive_metal_ecology__REPORT.md", "summaries/discoveries.md", "summaries/enigma_carbon_census_1__REPORT.md", "summaries/enigma_contamination_functional_potential__REPORT.md", "summaries/enigma_sso_asv_ecology__REPORT.md", "summaries/field_vs_lab_fitness__REPORT.md", "summaries/fw300_metabolic_consistency__REPORT.md", "summaries/genotype_to_phenotype_enigma__REPORT.md", "summaries/lab_field_ecology__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md", "summaries/oak_ridge_cultivation_gap__REPORT.md", "summaries/pitfalls.md", "summaries/webofmicrobes_explorer__REPORT.md"]
aliases: ["CORAL", "ENIGMA CORAL", "ENIGMA FRC", "ENIGMA Field Research Center data", "ENIGMA Genome Depot", "ENIGMA ORFRC", "ENIGMA field isolates", "ENIGMA projects", "Genome Depot", "ORFRC", "Oak Ridge FRC", "Zhou Lab 16S", "enigma_coral", "enigma_genome_depot_enigma"]
---
# ENIGMA

ENIGMA's subsurface field samples sit in enigma_coral and its genomes in enigma_genome_depot_enigma, both in the KBase Data Lakehouse. [src: berdl_data_atlas] The collections cover the Oak Ridge contamination gradient, including Field Research Center (FRC) groundwater MAG (metagenome assembled genome) and metal data. [src: comprehensive_metal_ecology] Some analyses on them were limited by data coverage: the three-well FRC metal analysis was uninformative, and the contamination-functional confirmatory tests were null. [src: comprehensive_metal_ecology, discoveries] Later reports add that enigma_coral holds no Desulfovibrio vulgaris Hildenborough data and that its field geochemistry and community data are rich but not yet fully linked. [src: field_vs_lab_fitness, genotype_to_phenotype_enigma, lab_field_ecology] The pitfalls digest warns that many enigma_coral schemas may be partial and that short ENIGMA strain names collide with unrelated NCBI organisms. [src: pitfalls]

## Key facts

- The inventory lists 4,346 ENIGMA SDT samples, 579 ENIGMA DDT measurement 'bricks' and 218,510 ENIGMA SDT ASVs (amplicon sequence variants). [src: berdl_data_atlas]
- It lists 3,110 ENIGMA depot genomes and 6,705 ENIGMA SDT genomes. [src: berdl_data_atlas]
- The field_observational topic accounts for 40% of Data Lakehouse tables, dominated by ENIGMA SDT/DDT structure. [src: berdl_data_atlas]
- The enigma tenant spans 5 topics with entropy 0.43 and is described as deep-but-narrow. [src: berdl_data_atlas]
- ENIGMA holds 36% of tables but appears in only 6 audited BERIL projects. [src: berdl_data_atlas]
- The ENIGMA Genome Depot contains 3,110 genomes and 6.8M proteins, with 3.7M KO and 6.4M COG annotations. [src: genotype_to_phenotype_enigma]
- The local CORAL dataset contains 596 locations and 587 ASV communities, with 123 strains mapped to 24 wells. [src: genotype_to_phenotype_enigma]
- ENIGMA genome sizes range from 2.6 to 11.4 Mb and correlate strongly with KO diversity, which ranges from 1,256-3,014 unique KOs per strain with median 2,121. [src: genotype_to_phenotype_enigma]
- The 2018 Web of Microbes (WoM) snapshot contains 37 organisms across 5 ENIGMA-funded projects. [src: webofmicrobes_explorer] The generated data/wom_projects.csv holds 5 rows of ENIGMA projects with DOIs. [src: webofmicrobes_explorer]
- The WoM snapshot includes 10 ENIGMA groundwater isolates with 1,050 observations in R2A medium. [src: webofmicrobes_explorer]

## Tables and how to join them

For subsurface field samples, the atlas report recommends the enigma_coral SDT/DDT/sample tables. It joins them to genomes through enigma_genome_depot_enigma on genome_id. [src: berdl_data_atlas]

- enigma_coral supplies sdt_sample, sdt_genome, sdt_asv and ddt_ndarray: field samples, MAGs, ASVs and multidimensional measurement datasets. [src: berdl_data_atlas]
- enigma_genome_depot_enigma supplies browser_genome, browser_gene and browser_protein, the genome/gene/protein browser depot. [src: berdl_data_atlas]
- In enigma_coral, sdt_* tables hold scientific data, ddt_* tables hold numerical bricks or arrays, and sys_* tables hold system or metadata rather than primary scientific data. [src: pitfalls]
- ddt_brick* columns are numerical arrays with non-tabular shape, so standard SQL projections may not work as expected. [src: pitfalls]
- Many enigma_coral tables timed out during ingest introspection, so schemas may be partial and should be confirmed with `DESCRIBE EXTENDED` before queries are written. [src: pitfalls]
- For FRC MAG KO (KEGG ortholog) content, the metal-ecology report used browser_genome, browser_gene, browser_protein_kegg_orthologs, browser_kegg_ortholog and browser_sample. [src: comprehensive_metal_ecology]
- ddt_brick0000007 supplies Oak Ridge FRC groundwater metal concentrations. [src: comprehensive_metal_ecology]
- The contamination-functional project used ddt_brick0000010, ddt_brick0000459, ddt_brick0000454, sdt_sample, sdt_community and sdt_location for geochemistry, community composition, taxonomy linkage and sample metadata. [src: enigma_contamination_functional_potential]
- ddt_brick0000454 gives taxonomy only through Genus, with no species or strain rows. [src: discoveries, pitfalls]
- The SSO (Subsurface Observatory) ASV work used sdt_sample, sdt_location, sdt_community, ddt_ndarray, ddt_brick0000457-459 and ddt_brick0000477-479 for sediment and groundwater 16S ASV data, sample metadata and well coordinates. [src: enigma_sso_asv_ecology]
- The Carbon Census used Genome Depot protein reaction, ortholog and enzyme annotations on isolate proteins. It also used an isolate-to-strain-to-NCBI-taxid crosswalk. [src: enigma_carbon_census_1]
- The Carbon Census took SSO field genus occurrence from Zhou Lab 16S and enigma_coral bricks. [src: enigma_carbon_census_1]
- The genotype-to-phenotype report used enigma_coral for growth curves, strain metadata, isolation locations, ASV community data and GTDB-Tk taxonomy. [src: genotype_to_phenotype_enigma]
- It used enigma_genome_depot_enigma for KO, COG, OG (ortholog groups), EC (Enzyme Commission) and GO (Gene Ontology) genome annotations for all 123 ENIGMA strains. Per-genome genomic features derive from the Genome Depot. [src: genotype_to_phenotype_enigma]
- The cultivation-gap report used Genome Depot tables browser_genome, browser_gene, browser_protein, browser_protein_kegg_orthologs, browser_kegg_ortholog and browser_taxon for cultured genome inventory and KO annotations. [src: oak_ridge_cultivation_gap]
- It originally used enigma_coral sdt_bin and sdt_assembly for MAG bin inventory, but assembly FASTAs were inaccessible. [src: oak_ridge_cultivation_gap]
- The lab-field ecology report used ddt_brick0000010 (metal concentrations per sample, 108 sites), ddt_brick0000459 (ASV counts per community, 868K rows) and ddt_brick0000454 (ASV-to-genus mapping, 627K rows) via Spark. [src: lab_field_ecology]
- It describes the previously undocumented CORAL database as containing rich community composition and geochemistry data suitable for ecological analysis. [src: lab_field_ecology]
- Its generated files are site_geochemistry.tsv (108 samples x 48 molecule concentrations), asv_counts.tsv (132K non-zero ASV x community counts), asv_taxonomy.tsv (96K ASVs with genus and phylum), sample_metadata.tsv (108 samples with location and date) and genus_abundance.tsv (relative abundance for 1,391 genera x 108 samples). [src: lab_field_ecology]

## Taxonomy pitfalls

Attempting a species-level bridge directly from genus-only ENIGMA taxonomy can fail or silently reuse genus-level mappings while appearing higher resolution. [src: pitfalls] The pitfalls digest proposes an explicit species-proxy mode (unique genus to single GTDB clade) with mapped-coverage loss reported. [src: pitfalls] It also names metagenomes and an ASV reclassification pipeline as alternatives that support species/strain resolution. [src: pitfalls]

Short ENIGMA field-isolate strain names such as MT20, MT42, GW460-LB6 and FW507-14TSA are not globally unique. They can match unrelated NCBI organisms through ncbi_strain_identifiers. [src: pitfalls] For example, ENIGMA MT20 is Rhodanobacter glycinis from groundwater in Xanthomonadales, whereas GTDB MT20 is clinical Streptococcus pneumoniae in Lactobacillales. [src: pitfalls]

In genotype_to_phenotype_enigma, 12 of 32 pangenome linkages via ncbi_strain_identifiers were incorrect genus matches. [src: pitfalls] Using CORAL brick 522 GTDB-Tk taxonomy and checking genus consistency reduced verified linkages from 32 to 20 and eliminated all false matches. [src: genotype_to_phenotype_enigma] The ENIGMA MT20 strain-name collision contaminated genus-environment profiles with spurious clinical data. [src: pitfalls]

## Metal data at the FRC

The within-site Spearman analysis of 29 MAGs across 3 wells gave burden ρ = −0.41 with p = 0.029. The report classifies it as uninformative because of a data coverage failure. [src: comprehensive_metal_ecology] The FRC data cover n = 3 wells and are uninformative at this sample size. [src: comprehensive_metal_ecology] The report describes coverage for the site-level Spearman replication notebook as limited. [src: comprehensive_metal_ecology] It proposes accessing geochemistry beyond ddt_brick0000007 to obtain groundwater chemistry for the remaining 18 wells with MAG data. [src: comprehensive_metal_ecology] It also proposes using longitudinal MAG data to test whether genera with higher metal-gene density show lower occupancy turnover across time points. [src: comprehensive_metal_ecology]

### Well-level geochemistry linkage

Uranium, nitrate and metal concentrations per well are available in CORAL bricks 10/80. [src: genotype_to_phenotype_enigma] Sample-to-location name resolution is incomplete, so no geochemistry linkage exists yet. [src: genotype_to_phenotype_enigma] The report proposes linking strain-isolation-well coordinates in coral_strain_locations.tsv to per-well geochemistry to test whether acid-tolerant Cluster B strains locally originate from higher-contamination wells. [src: genotype_to_phenotype_enigma]

### Field validation in PRJNA1084851 and groundwater

PRJNA1084851 contains 133 MiSeq 16S amplicon runs, SRR28246018–SRR28246150, from the ENIGMA-funded ORFRC Tennessee Water Research 2024 study "Reproducible responses of geochemical and microbial successional patterns in the subsurface to carbon source amendment" (doi:10.1016/j.watres.2024.121460). [src: microbeatlas_metal_ecology] It sampled 8 groundwater monitoring wells (FW202, FW215, FW216, GP01, GP03, MLSA3, MLSB3, MLSG4). [src: microbeatlas_metal_ecology] CWM (community weighted mean) differed across the 8 wells (Kruskal-Wallis H = 29.10, n = 133 samples, p = 0.0001). [src: microbeatlas_metal_ecology] Wells FW215 and FW216 are known to lie within the U/NO₃ contamination plume. [src: microbeatlas_metal_ecology]

The report states that ENIGMA field-validation Tracks A and B are complete and that a candidate OTU (operational taxonomic unit) list and shortlist were produced. [src: microbeatlas_metal_ecology] Track A used 1,624 KBase Data Lakehouse groundwater samples and found metal-diverse genera significantly more prevalent in groundwater (Spearman ρ = +0.112, p = 0.0019; Mann-Whitney p = 0.007). [src: microbeatlas_metal_ecology] The report states that both tracks independently confirm the PGLS (phylogenetic generalized least squares) prediction in field data. [src: microbeatlas_metal_ecology]

## Desulfovibrio and the field-versus-lab question

The ENIGMA CORAL database (47 tables in enigma_coral) was surveyed for data complementary to Fitness Browser work. [src: field_vs_lab_fitness] It contains no Desulfovibrio vulgaris Hildenborough (DvH) data. [src: field_vs_lab_fitness] All 6,705 genomes and 15,015 genes are Oak Ridge environmental isolates rather than DvH. [src: field_vs_lab_fitness] Its single TnSeq (transposon sequencing) library is for FW300-N2E2 (Pseudomonas), while its DubSeq libraries cover E. coli, P. putida and B. thetaiotaomicron. [src: field_vs_lab_fitness]

It does hold 4,346 field samples with uranium and metals geochemistry across 596 Oak Ridge locations, and 213,044 community-composition ASVs. [src: field_vs_lab_fitness] The report considers these potentially useful for future analyses but not for gene-level fitness analysis. [src: field_vs_lab_fitness] In its DvH experiment classification, Field-stress comprises 78 experiments (10.3%), representing FRC contaminants (uranium, mercury, nitrate, nitrite, oxygen, NO). [src: field_vs_lab_fitness] It classified cobalt, nickel, zinc, copper, manganese, selenium, molybdate, tungstate and aluminum as field heavy metals because DvH encounters them at Oak Ridge FRC sites. [src: field_vs_lab_fitness] It proposes applying the classification to other ENIGMA organisms with Fitness Browser data, such as Pseudomonas FW300 strains. [src: field_vs_lab_fitness] It also proposes using the 213K ASVs and 4,346 field samples to test whether Desulfovibrio abundance at Oak Ridge sites correlates with geochemistry conditions tested in the Fitness Browser. [src: field_vs_lab_fitness] Pseudomonas FW300-N2E3 was isolated from groundwater at the Oak Ridge Field Research Center (ENIGMA SFA), and the FW300 report proposes using its tryptophan overflow to parameterize a community metabolic model of cross-feeding with tryptophan auxotrophs there. [src: fw300_metabolic_consistency]

## Cultivation gap

The cultivation-gap report compares 3,110 ENIGMA Genome Depot cultured-isolate genomes, primarily from the Oak Ridge Field Research Center over 20+ years of cultivation, with 2,279 QC-passing subsurface MAGs from kbase_ke_pangenome collected from groundwater, aquifer and subsurface samples globally. [src: oak_ridge_cultivation_gap] The cohort table lists 3,110 cultured genomes, 3,102 with KO annotations. [src: oak_ridge_cultivation_gap] Cultured isolates are predominantly Proteobacteria with large genomes (5-7 Mbp), while the MAG cohort includes 40% Patescibacteria with streamlined genomes (0.5-1.5 Mbp). [src: oak_ridge_cultivation_gap] The cultured collection is dominated by Pseudomonadaceae (180 genomes), Variovorax (123), Cupriavidus (111) and other Burkholderiales, described as readily cultivable Gammaproteobacteria and Betaproteobacteria. [src: oak_ridge_cultivation_gap]

Limits: the report pivoted from 623 ORFRC-specific MAGs in enigma_coral because their assembly FASTAs were inaccessible from JupyterHub, so its findings concern subsurface systems generally. [src: oak_ridge_cultivation_gap] Its results therefore do not directly measure the cultivation gap at Oak Ridge. [src: oak_ridge_cultivation_gap] Composition differences may reflect geography as much as cultivation bias. [src: oak_ridge_cultivation_gap] Cultured KOs came from the Genome Depot pipeline (unknown tool version) and MAG KOs from bakta via kbase_ke_pangenome.bakta_db_xrefs. [src: oak_ridge_cultivation_gap] The report proposes annotating the 623 ORFRC MAGs once FASTAs become accessible, to build a site-matched coverage table. [src: oak_ridge_cultivation_gap]

For 147 ENIGMA cultured genomes matched by GCF/GCA accession (153 ENIGMA records → 147 unique pangenome genomes), Genome Depot and pangenome eggNOG-mapper KO calls were compared. [src: oak_ridge_cultivation_gap] They agree on 5,751 KOs, with 1,505 Depot-only and 148 eggNOG-only assignments, a pooled-set Jaccard similarity of 0.777. [src: oak_ridge_cultivation_gap]

## SSO geochemistry gap

For the SSO campaign, 221 METALS/ICTOC/ISOTOPES/NH3NO2 sample tubes are registered in CORAL sdt_sample. Zero Assay Geochemistry processes are linked, and the measurement values were never ingested. [src: discoveries] SSO geochemistry has therefore not been loaded into the Data Lakehouse. Environmental inferences rest on community composition alone, and the plume model awaits geochemical confirmation. [src: enigma_sso_asv_ecology] The ASV report names loading these 221 samples as the way to correlate community composition directly with measurements and to validate or refute the plume model. [src: enigma_sso_asv_ecology] Pump-test ASV data (Brick 460-462, wells L8/M5/U2) remain available for extraction. [src: enigma_sso_asv_ecology]

## Contamination and functional potential

The overlap dataset has 108 samples with both geochemistry and community composition. [src: enigma_contamination_functional_potential] The geochemistry matrix has shape (108, 49). [src: enigma_contamination_functional_potential] The data contain 41,711 community taxon rows, 212 distinct communities and 1,392 distinct genera. [src: enigma_contamination_functional_potential] Output tables hold 108 rows (geochemistry matrix), 41,711 rows (community taxon counts) and 108 rows (location metadata). [src: enigma_contamination_functional_potential] The project contributes a reproducible ENIGMA-to-Data Lakehouse functional inference workflow. It has independent strict-versus-relaxed features, mapped-coverage diagnostics, a species-proxy unique-clade sensitivity mode and multi-tier modeling. [src: enigma_contamination_functional_potential]

Primary univariate associations were non-significant for defense, stress, metabolism and mobilome outcomes in both mapping modes. [src: discoveries] Coverage-aware sensitivity models then made the contamination-defense association significant. Coverage-adjusted OLS (ordinary least squares) gave contamination p = 3.98e-4 relaxed and 3.54e-3 strict. [src: discoveries] The high-coverage subset Spearman gave p = 0.0207 relaxed and 0.0098 strict. [src: discoveries] The strongest signal is conditional on mapping coverage and model specification rather than broad across outcomes. [src: discoveries]

After global BH-FDR (Benjamini-Hochberg false discovery rate) correction, confirmatory genus-level defense Spearman tests remained null (p=0.546/0.483; q=0.862/0.849). [src: discoveries] The exploratory relaxed coverage-adjusted defense model retained q=0.046. [src: discoveries] Strict and other sensitivity signals attenuated above q<0.1. [src: discoveries] The report recommends prioritizing null confirmatory evidence and framing positive results as exploratory. [src: discoveries] Four contamination-index constructions (all-metals composite, uranium-only, top-3 variance metals, PCA-PC1) gave no significant confirmatory associations (all q=0.546 across 8 tests). [src: discoveries] The report concludes the null is not an artifact of one index formulation. [src: discoveries]

Computing strict and relaxed mapping independently in NB02 changed 1,140 of 1,590 genus-feature pairs (~71.7%). [src: discoveries] It also changed site stress scores for all 108 samples. [src: discoveries] The report therefore says the sensitivity should not be approximated by copied feature tables. [src: discoveries] The species_proxy_unique_genus mode retained 150 genera, but mean mapped abundance was 0.031 against 0.343 in strict/relaxed genus modes. [src: discoveries] In that mode the defense trend was positive but non-significant (rho=0.169, p=0.081). [src: discoveries] True species-level gains likely require higher-resolution taxonomy or metagenomic mapping. [src: discoveries]

## Carbon Census

The census links 83 named compounds through structures, pathways, ENIGMA isolate strains, GTDB phylogeny, SSO field occurrence and global biome abundance. It is tier-stratified and treats the Tier 0 gap as a result. [src: enigma_carbon_census_1] The pangenome-to-ENIGMA taxonomic bridge is genus-level at best. Isolate-specific transfer of pangenome Tier-2 reconstructions is avoided in favor of direct Genome Depot annotation. [src: enigma_carbon_census_1] The report reads "callable" compounds' structural simplicity at least as much as an annotation-coverage ceiling as biological bioavailability. [src: enigma_carbon_census_1] NB07 was reframed as an SSO field-occurrence atlas. [src: enigma_carbon_census_1] The headline table reports 62 utilizer genera in the SSO field. [src: enigma_carbon_census_1] Top aromatic-utilizer field prevalences are ~0.7–0.9, and 3-hydroxybenzoic-acid utilizers reach 0.90. [src: enigma_carbon_census_1] The file data/environmental_atlas.tsv has 156 rows of SSO field genus occurrence. [src: enigma_carbon_census_1]

## Proposed use

Use case UC2 proposes the enigma ↔ phagefoundry bridge, with 11 shared keys. It asks whether subsurface prophages mobilize metal-resistance along the Oak Ridge contamination gradient. [src: berdl_data_atlas]

See also [[entities/kbase-data-lakehouse]] and [[concepts/geochemical-and-contamination-plume-control-of-subsurface-community-structure]].
