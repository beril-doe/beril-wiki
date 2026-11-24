---
type: "Dataset"
description: "Genome Taxonomy Database genome-based taxonomy (release r214) and how its species boundaries differ from LPSN/DSMZ names."
sources: ["summaries/bacdive_metal_validation__REPORT.md", "summaries/cf_formulation_design__REPORT.md", "summaries/comprehensive_metal_ecology__REPORT.md", "summaries/enigma_carbon_census_1__REPORT.md", "summaries/enigma_contamination_functional_potential__REPORT.md", "summaries/gene_function_ecological_agora__REPORT.md", "summaries/lanthanide_methylotrophy_atlas__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md", "summaries/module_conservation__REPORT.md", "summaries/neon_mag_functional_discovery__REPORT.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md", "summaries/pangenome_openness__REPORT.md", "summaries/phb_granule_ecology__REPORT.md", "summaries/prophage_ecology__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md"]
aliases: ["GTDB r214", "GTDB-r214", "Genome Taxonomy Database"]
---
# GTDB

GTDB (Genome Taxonomy Database, release r214; also GTDB r214, GTDB-r214) is the genome-based taxonomy that underlies the pangenome collection and many analyses in this corpus. Its species boundaries differ from LPSN/DSMZ names, so name matching to other databases is lossy. [src: bacdive_metal_validation] The evidence below comes from many projects that use GTDB as a scaffold, not from tests of GTDB itself.

## Key facts

- GTDB r214 (Parks et al. 2022, Nat Biotechnol) is the taxonomic backbone of the KBase Data Lakehouse pangenome. [src: lanthanide_methylotrophy_atlas] See [[entities/kbase-ke-pangenome]].
- The pangenome scaffold covers 293K genomes and 27,690 species, using the genome, gtdb_species_clade, gtdb_taxonomy_r214v1, gtdb_metadata and pangenome tables. [src: gene_function_ecological_agora]
- The pangenome collection also holds the GTDB-r214 species tree and per-species distance pairs. [src: gene_function_ecological_agora]
- The pangenome-openness report used the GTDB taxonomy and pangenome framework for consistent cross-species comparisons. [src: pangenome_openness]
- Environment metadata covered 293,050 genomes spanning all 27,690 species. [src: phb_granule_ecology]
- One atlas used 18,989 P1B-qualified species representatives spanning the bacterial domain of GTDB r214. [src: gene_function_ecological_agora]
- The Pseudomonas study extracted GapMind carbon pathway predictions for 12,732 genomes across 433 Pseudomonas species clades defined by GTDB r214. [src: pseudomonas_carbon_ecology] The genus spans 5 GTDB subgenera. Pseudomonas s.s. has 19 species and 6,905 genomes, mostly P. aeruginosa. [src: pseudomonas_carbon_ecology] See [[entities/pseudomonas]].
- One report states that its species names follow GTDB taxonomy and may differ from NCBI names. [src: cf_formulation_design]

## Differences from LPSN/DSMZ names

Matching BacDive strains to GTDB species was lossy. Exact species-name agreement linked 33,535 strains (34.5%). [src: bacdive_metal_validation] Removing GTDB suffixes linked 8,692 more (8.9%), for example BacDive "Pseudomonas fluorescens" to GTDB "Pseudomonas fluorescens A". [src: bacdive_metal_validation] That left 55,107 strains (56.6%) with no GTDB species. [src: bacdive_metal_validation] The report attributes this mainly to GTDB using different species boundaries than LPSN/DSMZ. [src: bacdive_metal_validation] See [[concepts/linking-isolate-and-strain-records-to-reference-genome-databases]] and [[concepts/taxonomic-synonymy-and-strain-name-collisions-in-cross-database-matching]].

## Taxonomy bridges

- In the NMDC (National Microbiome Data Collaborative) analysis, mean bridge coverage to GTDB pangenome species was 94.6%, and all 220 samples passed the 30% quality control threshold. [src: nmdc_community_metabolic_ecology] In that cohort, 92% of samples mapped ≥85% of community abundance to GTDB pangenome species. [src: nmdc_community_metabolic_ecology]
- That analysis integrated 305M GapMind pathway records (27,690 GTDB species × 80 pathways) with NMDC multi-omics for 220 samples. [src: nmdc_community_metabolic_ecology] See [[entities/gapmind]].
- The prophage study applied genus-level burden scores to 6,365 NMDC metagenomic samples through a GTDB metadata bridge plus taxonomy_dim genus matching. [src: prophage_ecology]
- The ENIGMA contamination bridge parsed 27,690 GTDB species rows and contained 530 strict clades and 7,380 relaxed clades. [src: enigma_contamination_functional_potential] The report cautions that this stack depends on GTDB and eggNOG conventions, and that genus-level broad COG-style signals can dilute pathway-specific metal-response effects. [src: enigma_contamination_functional_potential] See [[concepts/genus-level-taxonomy-bridging-to-pangenome-clades-and-its-coverage-limits]].
- The ENIGMA isolate deliverable gives 494 strain placements on the GTDB taxonomy, covering 359 distinct strains. [src: enigma_carbon_census_1] Of these, 64 are high-certainty gene-complete-pathway Tier 2 [src: enigma_carbon_census_1], 387 are medium-certainty Tier 2 pathway [src: enigma_carbon_census_1], and 43 are medium-certainty Tier 3 signature enzyme. [src: enigma_carbon_census_1]
- In the module conservation analysis, 3 organisms (Cola, Kang, SB2B) lack pangenome links because their species had too few genomes in GTDB for pangenome construction. This limits the analysis to 29 of 32 organisms. [src: module_conservation]

## Use as a phylogenetic and taxonomic scaffold

- The microbeatlas report ran all PGLS (phylogenetic generalized least squares) and Pagel's λ analyses on the GTDB r214 genus-representative tree, built from 120 concatenated marker genes. [src: microbeatlas_metal_ecology] It calls this the current field standard and the best available reconciliation of phylogenomic signal with 16S taxonomy. [src: microbeatlas_metal_ecology]
- Each genus is one tip, chosen as the GTDB species cluster representative. [src: microbeatlas_metal_ecology] Pagel's λ was computed with phytools::phylosig. [src: microbeatlas_metal_ecology] The tree is public at https://gtdb.ecogenomic.org/. [src: microbeatlas_metal_ecology]
- That report did not test NCBI trees, SILVA-based 16S trees or a different GTDB release, and names this a methodological gap. [src: microbeatlas_metal_ecology] A 16S tree would align better with the 16S-derived niche breadth but resolve genera less well. [src: microbeatlas_metal_ecology] See [[concepts/genus-level-aggregation-tree-choice-and-trait-distribution-assumptions-in-phylogenetic-comparative-analyses]] and [[entities/phylogenetic-generalized-least-squares]].
- In 1,574 genera matched across the GTDB phylogeny and MGnify MAG data (metagenome assembled genomes), per-Mb Tier 1+2 metal-gene KO (KEGG ortholog) density was negatively associated with standardised Levins' niche breadth. The fit gave β = −0.021, SE = 0.0037, p = 2.1×10⁻⁸, Pagel's λ = 0.757 and r² = 0.046. [src: comprehensive_metal_ecology] The archaeal replication on the GTDB archaeal tree (n = 95) gave β = −0.014 (p = 0.119). It was directionally consistent but non-significant, likely from low power. [src: comprehensive_metal_ecology] See [[concepts/metal-gene-density-and-ecological-niche-breadth]].
- Fritz & Purvis D was applied on a GTDB 18,961-tip tree for 309 metal-gene KOs with ≥20 genomes. D = 1 is read as random/HGT-like (horizontal gene transfer) and D = 0 as Brownian/vertical. [src: comprehensive_metal_ecology] See [[concepts/horizontal-transfer-signatures-of-metal-resistance-genes]].
- Lanthanide methylotrophy stratification used GTDB phylum, class, family and genus assignments. [src: lanthanide_methylotrophy_atlas]
- Across 27,690 GTDB species, 21.9% carry phaC. The 6,067 phaC-carrying species span 95 of 142 GTDB phyla but concentrate in a few lineages. [src: phb_granule_ecology] See [[concepts/phylogenetic-distribution-of-phb-synthesis-across-bacteria-and-archaea]].
- Prophage modules A, D and F were all ≥99% prevalent in the top 15 of 142 GTDB phyla. [src: prophage_ecology]

## Reference-database bias

In NEON soil MAG records (MQ+HQ), the fraction with no GTDB genus call was 7.6% at pH < 4.5 (396 records) and 37.0% at pH > 6.5 (1,107 records). [src: neon_mag_functional_discovery] The report proposes culture-mining bias in GTDB as the most parsimonious explanation. It argues that acid-tolerant and peat-soil groups such as Acidobacteriota and Verrucomicrobia have mature species-level representation. [src: neon_mag_functional_discovery] Without independent ground truth, the result fits either true biological novelty or a GTDB coverage gap in alkaline soils. The report favors the coverage gap. [src: neon_mag_functional_discovery] See [[concepts/lineage-novelty-and-reference-database-culture-bias-across-environmental-gradients]].

## Open Directions

- Repeat the tree-based analyses with an NCBI or 16S tree and a different GTDB release to close the tree-sensitivity gap.
- Add a synonymy table between LPSN/DSMZ and GTDB names, to recover some of the 56.6% of unmatched BacDive strains.
- Test the NEON novelty pattern against full-length 16S phylogeny to separate coverage bias from biological novelty.

## Source tables

The kbase_ke_pangenome tables (eggnog_mapper_annotations, gene_cluster, gtdb_taxonomy_r214v1 and others) supplied KO density, taxonomy and environment metadata for several projects. [src: comprehensive_metal_ecology, gene_function_ecological_agora, nmdc_community_metabolic_ecology, prophage_ecology, pseudomonas_carbon_ecology] The ENIGMA census used its annotations against a null denominator of 3109 genomes. [src: enigma_carbon_census_1]
