---
type: "Dataset"
description: "KEGG orthologs (KOs) and modules used for functional annotation, enrichment and benchmark labels, with names resolved from the KEGG REST API and legacy snapshots."
sources: ["summaries/amr_cofitness_networks__REPORT.md", "summaries/fitness_modules__REPORT.md", "summaries/genotype_to_phenotype_enigma__REPORT.md", "summaries/harvard_forest_warming__REPORT.md", "summaries/neon_mag_functional_discovery__REPORT.md"]
aliases: ["KEGG KO", "KEGG module and orthology resources", "KEGG modules", "KEGG ortholog", "KEGG orthology", "KO"]
---
# KEGG

This page covers KEGG orthologs (KOs) and KEGG modules used for functional annotation, enrichment and benchmark labels. KOs served as named, interpretable model features in the ENIGMA growth report. [src: genotype_to_phenotype_enigma] They also served as targets in an ortholog-transfer benchmark, where ortholog transfer scored well. [src: fitness_modules] They were too gene-specific for module-level enrichment. [src: fitness_modules] The KEGG module name table in the KBase Data Lakehouse is empty apart from module IDs, so names had to come from the KEGG REST API and legacy snapshots. [src: neon_mag_functional_discovery]

## Key facts

- A KO is a KEGG ortholog. The ENIGMA growth report describes KOs as standardized functional annotations, where each KO ID represents a specific enzymatic reaction or transport function with a defined role in metabolism. [src: genotype_to_phenotype_enigma]
- In the Harvard Forest report, DNA and RNA KEGG KO annotations come from the table nmdc_results.annotation_kegg_orthology. [src: harvard_forest_warming]
- The Harvard Forest file data/ko_counts_by_sample.tsv.gz has 561,330 rows of KO counts per biosample, DNA or RNA source, and KO. [src: harvard_forest_warming]

## KOs as model features (ENIGMA growth modeling)

The ENIGMA genotype-to-phenotype report used KO presence/absence as its feature set. Features come from genome depot protein-to-KO annotations. [src: genotype_to_phenotype_enigma] The combined corpus has 46,389 pairs across 727 genomes and 363 conditions, with 4,293 shared KOs as features. [src: genotype_to_phenotype_enigma]

The report filters KOs by prevalence across the 727-genome corpus. It removes 456 core KOs present in >95% of genomes because they have no discriminative power. [src: genotype_to_phenotype_enigma] It also removes 2,406 rare KOs present in <5% of genomes because they are too sparse for statistical learning. [src: genotype_to_phenotype_enigma] The report states that 4,305 informative KOs are retained as named KEGG orthologs for SHAP (Shapley additive explanations) interpretability. [src: genotype_to_phenotype_enigma] This count differs from the 4,293 features given for the combined corpus. [src: genotype_to_phenotype_enigma] The cited claims do not reconcile the two numbers.

The report favors KOs over genome-scale scalars because KOs carry condition-specific mechanistic information. Its example is that K10440 (ribose transporter) directly enables ribose utilization. It favors KOs over PCA (principal component analysis) or embeddings because each feature is a named gene function. Such a function can be interpreted via KEGG pathway maps and validated against independent fitness data. [src: genotype_to_phenotype_enigma] No PCA is used, so every feature is a named KO. [src: genotype_to_phenotype_enigma]

## KOs as benchmark labels and annotation (fitness modules, AMR)

In the fitness_modules NB07 held-out benchmark, 20% of KEGG-annotated genes were withheld and 4 methods predicted KO groups. [src: fitness_modules] Ortholog transfer reached 95.8% strict precision, 91.2% coverage and an F1 of 0.934. [src: fitness_modules] See ortholog transfer function prediction and [[concepts/function-prediction-for-uncharacterized-genes-by-guilt-by-association-and-ortholog-transfer]].

The report attributes near-zero strict KO precision for Module-ICA and cofitness to the fact that KEGG KO groups are gene-level assignments, averaging ~1.2 genes per unique KO. [src: fitness_modules] A module with 20 annotated members typically has 20 different KOs. [src: fitness_modules] The report concludes that KEGG KOs are too gene-specific for module-level enrichment. [src: fitness_modules] See [[concepts/annotation-coverage-and-resolution-in-genome-wide-cofitness-analysis]].

In the AMR cofitness networks report, old KEGG annotations identified 2 mechanism-specific terms at FDR (false discovery rate) <0.05, lipoprotein and toluene tolerance. InterProScan GO (Gene Ontology) identified 0. [src: amr_cofitness_networks]

## KO and module data in metagenomic projects

Harvard Forest's metatranscriptome assembly recovered 14,302 distinct KOs versus 12,863 in the metagenome. [src: harvard_forest_warming] The report cautions that KO data from contig annotations measure transcript-pool composition, not TPM-quantified expression. Contig-level annotation count approximates relative transcript abundance but is biased by assembly quality. [src: harvard_forest_warming] See [[concepts/dna-versus-rna-pool-sensitivity-to-environmental-perturbation]].

The NEON report used nmdc_arkin.kegg_ko_module and kegg_module_terms for KO-to-module mapping in Fisher enrichment. [src: neon_mag_functional_discovery] The table kegg_module_terms has empty name, description and category columns for all 370 modules, and only module_id is populated. [src: neon_mag_functional_discovery] This limited habitat interpretation, so labels for top hits were assigned from external KEGG references. [src: neon_mag_functional_discovery] The report resolved enriched module names from the KEGG REST (representational state transfer) API (application programming interface) plus legacy KEGG snapshots. It recorded them in data/kegg_module_names.tsv. [src: neon_mag_functional_discovery] See annotation and environmental metadata table gaps in the data lakehouse and [[concepts/habitat-and-soil-chemistry-structuring-of-metagenomic-functional-gene-content]].

## Source summaries

Source summaries: [[summaries/amr_cofitness_networks__REPORT]], [[summaries/fitness_modules__REPORT]], [[summaries/genotype_to_phenotype_enigma__REPORT]], [[summaries/harvard_forest_warming__REPORT]], [[summaries/neon_mag_functional_discovery__REPORT]].
