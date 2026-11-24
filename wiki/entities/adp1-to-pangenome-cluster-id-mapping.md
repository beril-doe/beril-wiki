---
type: "Method"
description: "A bridge joining ADP1 pangenome cluster IDs to Lakehouse gene clusters through member gene IDs."
sources: ["summaries/acinetobacter_adp1_explorer__REPORT.md", "summaries/adp1_deletion_phenotypes__REPORT.md"]
aliases: ["cluster_id_mapping"]
---
# ADP1 to pangenome cluster ID mapping

This page covers the ADP1 to pangenome cluster ID mapping (also called cluster_id_mapping). It is a bridge that joins ADP1 pangenome cluster identifiers (IDs) to the KBase Data Lakehouse gene clusters through member gene IDs. [src: acinetobacter_adp1_explorer] See [[summaries/acinetobacter_adp1_explorer__REPORT]] for the full report.

## Key facts

- The two systems use different naming. ADP1 uses mmseqs2-style cluster IDs (`NHSXFYEX_mmseqsCluster_NNNN`), and the Lakehouse uses centroid gene IDs (`NC_005966.1_1024`). The two have 0% direct string match, so a plain join on cluster ID fails. [src: acinetobacter_adp1_explorer]
- The bridge runs through the Lakehouse `gene_genecluster_junction` table. Lakehouse cluster IDs map to member gene IDs. Those IDs match the `feature_id` column in the ADP1 `pan_genome_features` table, which carries the ADP1-style `cluster_id`. [src: acinetobacter_adp1_explorer]
- All 4,891 Lakehouse clusters mapped to 4,081 unique ADP1 clusters, with 100% gene-level match across 43,754 genes. [src: acinetobacter_adp1_explorer]
- The saved table `data/cluster_id_mapping.csv` has 4,891 rows. [src: acinetobacter_adp1_explorer]
- With this table, any Lakehouse pangenome annotation, including eggNOG and functional predictions, can be joined to ADP1 genes. [src: acinetobacter_adp1_explorer]
- The notebook `03_cluster_id_mapping.ipynb` builds the bridge. [src: acinetobacter_adp1_explorer]

## Related use in another project

The adp1_deletion_phenotypes analysis of Acinetobacter baylyi ADP1 takes pangenome cluster IDs and core/accessory status from `kbase_ke_pangenome`. It cross-references them through the `pangenome_cluster_id` column in `genome_features`. [src: adp1_deletion_phenotypes] See [[entities/kbase-ke-pangenome]] and [[summaries/adp1_deletion_phenotypes__REPORT]].

## Caveats

The mapping goes through 3 tables and is 100% complete. That indirection could still cause edge cases for clusters that split or merge between the two pangenome analyses. [src: acinetobacter_adp1_explorer] The 0% string match is an example of the problem described in [[concepts/join-key-validity-and-identifier-format-mismatches]]. [src: acinetobacter_adp1_explorer]
