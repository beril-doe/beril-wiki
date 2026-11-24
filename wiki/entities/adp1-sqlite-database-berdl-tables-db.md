---
type: "Dataset"
description: "A 15-table SQLite database integrating genome, annotation, metabolic model, phenotype and proteomics data for ADP1 and 13 related genomes."
sources: ["summaries/acinetobacter_adp1_explorer__REPORT.md", "summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/aromatic_catabolism_network__REPORT.md", "summaries/respiratory_chain_wiring__REPORT.md"]
aliases: ["ADP1 database", "berdl_tables.db"]
---
# ADP1 SQLite database (berdl_tables.db)

The ADP1 SQLite database (berdl_tables.db, also called the ADP1 database) is a user-provided database for *Acinetobacter baylyi* ADP1 ([[entities/acinetobacter-baylyi-adp1]]). It holds 15 tables with 461,522 total rows and 135 MB (megabytes) of data for ADP1 and 13 related genomes. [src: acinetobacter_adp1_explorer]

## Key facts

- The database has 15 interconnected tables with 27 relationship pairs (shared columns). [src: acinetobacter_adp1_explorer]
- The user-provided file supplies all 15 tables, covering the ADP1 genome, annotations, metabolic model, phenotypes and proteomics. [src: acinetobacter_adp1_explorer]
- The central `genome_features` table has 5,852 genes and 51 annotation columns spanning six data modalities. [src: acinetobacter_adp1_explorer]
- Core data flow: `genome` → `genome_features` (annotations, essentiality, proteomics, growth) → `pan_genome_features` (pangenome context) → `genome_reactions` (metabolic model) → `gene_phenotypes` (phenotype associations) → `growth_phenotypes_detailed` (FBA predictions). [src: acinetobacter_adp1_explorer]

## Coverage of genes

No single gene has data across all six modalities simultaneously. [src: acinetobacter_adp1_explorer] Pairwise overlaps are substantial, particularly between essentiality, pangenome and proteomics. [src: acinetobacter_adp1_explorer] Coverage by modality:

| Modality | Coverage |
|---|---|
| TnSeq (transposon sequencing) essentiality | 58% [src: acinetobacter_adp1_explorer] |
| Pangenome classification | 54% [src: acinetobacter_adp1_explorer] |
| Proteomics across 7 strains | 41% [src: acinetobacter_adp1_explorer] |
| Mutant growth fitness on 8 carbon sources | 39% [src: acinetobacter_adp1_explorer] |
| FBA (flux balance analysis) metabolic flux | 15% [src: acinetobacter_adp1_explorer] |
| Functional annotations via COG (clusters of orthologous groups), KO (KEGG ortholog), Pfam and UniRef | 34-55% [src: acinetobacter_adp1_explorer] |

## Data not available elsewhere in the KBase Data Lakehouse

- Mutant growth fitness on 8 carbon sources. ADP1 is absent from the Fitness Browser, so this is the only source of condition-specific fitness data for the organism in the lakehouse. [src: acinetobacter_adp1_explorer] See [[concepts/condition-specific-fitness-correlation-across-carbon-sources]].
- Proteomics across 7 engineered strains, with quantitative protein abundances for wild-type and aromatic amino acid pathway mutants. [src: acinetobacter_adp1_explorer]
- TnSeq-based gene essentiality calls on minimal and LB media. [src: acinetobacter_adp1_explorer] See [[concepts/annotation-and-pangenome-correlates-of-gene-essentiality]].

## Other supplied data

The database also supplies FBA predictions with gapfilling metadata, which enable model-experiment concordance analysis. [src: acinetobacter_adp1_explorer] See [[concepts/concordance-of-genome-scale-metabolic-model-predictions-with-experimental-data]].

## Use in other projects

- The deletion-phenotype project used `genome_features` for growth ratios, TnSeq essentiality and functional annotations of 5,852 ADP1 genes. [src: adp1_deletion_phenotypes] See [[summaries/adp1_deletion_phenotypes__REPORT]].
- The aromatic catabolism project used `genome_features`, `gene_phenotypes` and `gene_reaction_data` for growth ratios, FBA predictions across 230 conditions and gene-reaction mappings. [src: aromatic_catabolism_network] See [[summaries/aromatic_catabolism_network__REPORT]].
- The respiratory chain project used `genome_features`, `gene_phenotypes`, `gene_reaction_data` and `genome_reactions` for growth ratios, FBA predictions and reaction stoichiometry. [src: respiratory_chain_wiring] See [[summaries/respiratory_chain_wiring__REPORT]].
