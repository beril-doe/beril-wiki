---
type: "Dataset"
description: "Catalog of AMR genes in Fitness Browser organisms with per-gene fitness costs."
sources: ["summaries/amr_cofitness_networks__REPORT.md", "summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_fitness_cost__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md"]
aliases: ["amr_genes_fb"]
---
# Antimicrobial resistance gene catalog (amr_fitness_cost)

This page covers the Antimicrobial resistance gene catalog (amr_fitness_cost), also known as amr_genes_fb. The catalog has 1,352 rows of AMR genes annotated with class, mechanism, conservation, and tier. [src: amr_fitness_cost]

## Key facts

- Data assembly identified 1,352 AMR genes across 43 organisms, including 178 Tier 1 and 1,174 Tier 2 genes. [src: amr_fitness_cost]
- The companion file data/amr_fitness_noabx.csv has 801 rows of per-gene mean fitness under non-antibiotic conditions. [src: amr_fitness_cost]
- The amr_cofitness_networks project cites the catalog as the source of its AMR genes and the second file as the source of per-gene fitness costs. [src: amr_cofitness_networks]
- A separate file, data/amr_fitness.csv, holds 29,386 fitness measurements for 162 AMR genes in 36 FB organisms. It is listed in the amr_pangenome_atlas report. [src: amr_pangenome_atlas]

## Use in downstream projects

The cofitness analysis used the full intersection of 28 organisms with AMR genes, fitness matrices, and independent component analysis (ICA) modules. [src: amr_cofitness_networks] Of 801 AMR genes with fitness data, 769 (96%) have at least one extra-operon cofitness partner at |r| > 0.3. [src: amr_cofitness_networks] Support-network size did not correlate with AMR gene fitness cost (Spearman rho = −0.006, p = 0.87, N = 769). This is a null result. [src: amr_cofitness_networks] See [[summaries/amr_cofitness_networks__REPORT]] and [[concepts/functional-composition-of-antimicrobial-resistance-cofitness-support-networks]].

The amr_environmental_resistome report cites the project's conservation result: mechanism predicts conservation, with metal resistance 44% accessory and efflux 13% core. [src: amr_environmental_resistome] That report interprets this as ecology-driven. Efflux genes are core because they serve host-associated organisms constitutively. Metal resistance is accessory because it varies with environmental metal exposure. [src: amr_environmental_resistome] See [[concepts/intrinsic-versus-acquired-resistance-gene-conservation]], [[concepts/core-versus-accessory-partitioning-of-gene-functions-and-trait-genes]], [[entities/fitness-browser]] and [[summaries/amr_fitness_cost__REPORT]].
