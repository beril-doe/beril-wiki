---
type: "Method"
description: "Read-based taxonomic classifier whose NMDC reference database is prokaryote-restricted, so it gives no usable eukaryotic signal."
sources: ["summaries/euk_in_prok_correlates__REPORT.md", "summaries/harvard_forest_warming__REPORT.md"]
aliases: ["Kraken", "kraken2 read-based taxonomy"]
---
# Kraken2

Kraken2 (also Kraken, or kraken2 read-based taxonomy) is a read-based taxonomic classifier. Its NMDC reference database is prokaryote-restricted, so it gives no usable eukaryotic signal. [src: euk_in_prok_correlates] It does recover a prokaryotic warming signal in the Harvard Forest data. [src: harvard_forest_warming]

## Key facts

- Kraken's only eukaryotic kingdom in the NMDC reference database is Metazoa/human. [src: euk_in_prok_correlates]
- Kraken2 and Centrifuge domain-level Eukaryota signals are ≈0 because their NMDC reference databases are prokaryote-restricted. GOTTCHA2 is therefore the only usable eukaryotic estimator in that analysis. [src: euk_in_prok_correlates] See [[concepts/classifier-and-database-limits-for-estimating-eukaryotic-read-fraction]] and [[summaries/euk_in_prok_correlates__REPORT]].
- The NMDC `kraken2_classification_report` taxonomy table has ~29M rows. The report recommends aggregating each classifier to one row per `workflow_run_id` before joining metadata, and never scanning the table unfiltered. [src: euk_in_prok_correlates] See [[concepts/spark-query-scale-limits-and-notebook-session-constraints-in-lakehouse-analyses]].

## Use in the Harvard Forest warming study

The Harvard Forest dataset `data/kraken2_taxa_by_sample.tsv.gz` has 189,465 rows of read-based taxonomy abundances per biosample, rank and taxon. [src: harvard_forest_warming] The phylum analysis ran per-phylum Welch t-tests on kraken2 read-based relative abundance. It used n=14 control and 14 heated direct samples, with BH-FDR (Benjamini-Hochberg false discovery rate) correction across phyla × horizon. [src: harvard_forest_warming]

The site's published compositional warming signal (Actinobacteria up, Acidobacteria down) was recoverable from kraken2 read-based taxonomy at q<0.05 in 14+14 samples. [src: harvard_forest_warming] See [[summaries/harvard_forest_warming__REPORT]] and [[concepts/warming-response-of-soil-microbial-community-composition]].
