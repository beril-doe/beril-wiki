---
type: "Dataset"
description: "KBase Data Lakehouse collection of MGnify genomes with metadata, CAZy class counts (genome_cazy) and pre-computed pangenome statistics (pangenome_stats)."
sources: ["summaries/cazyme_pangenome_ecology__REPORT.md", "summaries/comprehensive_metal_ecology__REPORT.md", "summaries/discoveries.md", "summaries/gene_function_ecological_agora__REPORT.md", "summaries/metal_resistance_global_biogeography__REPORT.md", "summaries/plant_microbiome_ecotypes__REPORT.md"]
aliases: ["MGnify", "MGnify MAGs", "MGnify genome catalog", "kescience_mgnify.genome_cazy", "kescience_mgnify.pangenome_stats"]
---
# kescience_mgnify

kescience_mgnify is a collection in the [[entities/kbase-data-lakehouse]] that holds MGnify genomes, also called MGnify MAGs or the MGnify genome catalog. Its tables include genome, genome_cazy and pangenome_stats. [src: cazyme_pangenome_ecology] Projects used it for biome labels, CAZy counts and cross-validation. [src: gene_function_ecological_agora, cazyme_pangenome_ecology, plant_microbiome_ecotypes] Its biome coverage is partial [src: discoveries, gene_function_ecological_agora], and its CAZy resolution is coarse. [src: cazyme_pangenome_ecology]

## Key facts

- The collection is EBI MGnify, a metagenomics service. Its name is `mgnify`, not `magnify`. [src: discoveries]
- The cazyme_pangenome_ecology report used the genome, genome_cazy and pangenome_stats tables for metadata, CAZy counts and pangenome statistics for 49K genomes across 18 biomes. [src: cazyme_pangenome_ecology]
- Another report used the species, biome and genome tables for P4-D1 biome labels, with 28.4% species coverage and 18 biomes. [src: gene_function_ecological_agora]
- The collection supplies an OTU (operational taxonomic unit) × sample abundance matrix via [[entities/microbeatlas]]. That matrix feeds a Levins' niche breadth calculation. [src: comprehensive_metal_ecology]

## CAZyme tables

- Genome_cazy is a small table of about 345K rows. It joined cleanly to kescience_mgnify.genome on genome_id, with no performance issues. [src: cazyme_pangenome_ecology]
- Pivoting 49K genomes × 7 CAZy classes to wide format took seconds in pandas and did not need Spark. [src: cazyme_pangenome_ecology]
- Pangenome_stats is pre-computed, so per-gene tables need no aggregation. [src: cazyme_pangenome_ecology]
- Genome_cazy gives only 7 top-level CAZy (carbohydrate-active enzyme) classes: GH, GT, PL, CE, AA, CB and CL. It does not give individual families. [src: cazyme_pangenome_ecology]
- In this data, CAZyme class composition, particularly GH (glycoside hydrolase) and GT (glycosyl transferases), differs 3–4× across bacterial biomes. The effect survives genome-size and phylogenetic controls. [src: cazyme_pangenome_ecology] See [[concepts/biome-level-carbohydrate-active-enzyme-repertoire-differentiation]] and [[summaries/cazyme_pangenome_ecology__REPORT]].

## Biome labels and coverage

Biome labels cover only part of the species. [src: discoveries, gene_function_ecological_agora] See [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]].

- A cross-project note puts categorical biome coverage at 28.4%. [src: discoveries]
- In the P4-D1 audit of 18,989 species, kescience_mgnify.species biome_id covered 28.4% (5,392 species) with 18 discrete biome categories. [src: gene_function_ecological_agora]
- P4-D1 did not query MGnify's per-sample taxa-coverage matrices. The report names this as a substantive future direction for finer-grained ecological inference. [src: gene_function_ecological_agora]
- For Mycobacteriaceae, the MGnify breakdown shows 53 human-skin, 16 human-vaginal, 15 human-gut and 11 chicken-gut species. [src: gene_function_ecological_agora]

## Metal ecology uses

- The metal_resistance_global_biogeography report extracted 260,652 environmental MAGs (metagenome assembled genomes) from MGnify. 30,497 remained after filtering host-associated biomes. [src: metal_resistance_global_biogeography]
- Of these, 22,356 MAGs had usable coordinates, which is 73.3% coverage of the environmental MAG set. [src: metal_resistance_global_biogeography]
- Of those 22,356 MAGs, 2.8% carry at least one metal resistance type. The report calls metal resistance rare in the global environmental MAG pool. [src: metal_resistance_global_biogeography] See [[concepts/geographic-and-biome-distribution-of-environmental-metal-resistance]].
- In comprehensive_metal_ecology, P1 and P5 use the same per-Mb metal-gene density from the same MGnify MAG dataset. Their predictors are therefore consistent by construction. [src: comprehensive_metal_ecology]
- An exploratory analysis (NB22) used mean completeness and mean contamination per genus from kescience_mgnify.genome, for n = 1,107 genera with quality metadata. [src: comprehensive_metal_ecology]
- The report built a genome-based niche metric, the Shannon entropy of biome_name across MAGs per genus. It had n = 1,006 genera with both metrics. [src: comprehensive_metal_ecology] See [[concepts/robustness-and-replication-of-niche-breadth-associations]].
- In MGnify, 5/8 double-signal KOs (KEGG orthologs) with data were significant for environmental metal enrichment at FDR (false discovery rate) q < 0.1. They were nicC (q = 5.6×10⁻⁵), nikB (q = 2.8×10⁻⁵), gesA (q = 9.4×10⁻⁵), iucD (q = 1.1×10⁻⁴) and norB (q = 7.1×10⁻²). [src: comprehensive_metal_ecology]
- Five double-signal KOs were absent from the MGnify enrichment dataset: nrsD, merE, merD, shp and doxDA. This metric cannot assess them. [src: comprehensive_metal_ecology] See [[concepts/horizontal-transfer-signatures-of-metal-resistance-genes]].

## Plant microbiome use

The plant_microbiome_ecotypes report used the species, genome, gene_mobilome, gene_bgc, genome_kegg_module and genome_cog tables for mobilome, BGC (biosynthetic gene cluster) and KEGG profiles. [src: plant_microbiome_ecotypes] The MGnify catalogue held 20,473 species across 4 biomes. It served as cross-validation. [src: plant_microbiome_ecotypes] See [[concepts/isolation-metadata-versus-metagenomic-cross-validation-of-plant-associated-taxa]], [[concepts/mobile-elements-and-horizontal-transfer-of-plant-interaction-genes]] and [[summaries/plant_microbiome_ecotypes__REPORT]].

- The taxonomy bridge linked the 20,473 species to 1,185 pangenome genera. 9,603 MGnify species fell in matched genera. [src: plant_microbiome_ecotypes]
- The soil biome held 19,472 species in 4,229 genera. [src: plant_microbiome_ecotypes]
- The tomato rhizosphere held 579 species in 309 genera. [src: plant_microbiome_ecotypes]
- The maize rhizosphere held 336 species in 212 genera. [src: plant_microbiome_ecotypes]
- The barley rhizosphere held 86 species in 52 genera. [src: plant_microbiome_ecotypes]
- Soil mobilome analysis found 17,323 entries across 563 pangenome genera with data. It used ISEScan, ICEfinder and geNomad. [src: plant_microbiome_ecotypes]
- Soil BGC analysis classified 17,608 BGCs into MiBIG categories across 579 pangenome genera with data. [src: plant_microbiome_ecotypes] Polyketide made up 23.1%, [src: plant_microbiome_ecotypes] NRP 13.9%, [src: plant_microbiome_ecotypes] Saccharide 13.2%, [src: plant_microbiome_ecotypes] RiPP 12.6% [src: plant_microbiome_ecotypes] and Terpene 12.7%. [src: plant_microbiome_ecotypes]
- Average BGC-to-MiBIG similarity scores ranged from 0.38–0.89. [src: plant_microbiome_ecotypes]
- KEGG modules M00238, M00769, M00136, M00615 and M00438 were each 2–3× enriched in rhizosphere. [src: plant_microbiome_ecotypes]
- Caveat: BGC, mobilome and defense annotations exist only for the soil biome, not for tomato, maize or barley rhizosphere. [src: plant_microbiome_ecotypes]
- The mobilome and BGC analyses therefore compare soil-dwelling plant-associated genera with soil-dwelling non-plant genera. They do not compare rhizosphere with bulk soil. [src: plant_microbiome_ecotypes]
