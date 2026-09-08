# Beril Admin

*Not a person — a BERIL service account. Listed as an author on the projects below.*

ORCID: [0009-0007-0287-2979](https://orcid.org/0009-0007-0287-2979)

## Contributions

[[summaries/acinetobacter_adp1_explorer__REPORT]] analyzed a 15-table, 461,522-row, 135 MB SQLite database for *Acinetobacter baylyi* ADP1 and 13 related genomes, integrating genome features, TnSeq essentiality, flux balance analysis (FBA), mutant growth fitness, proteomics, pangenome classification, functional annotations, metabolic reactions, and growth phenotypes. [src: acinetobacter_adp1_explorer] The project found that the central `genome_features` table contained 5,852 genes and 51 annotation columns, with coverage ranging from 15% for FBA metabolic flux to 58% for TnSeq essentiality, and that no gene had data across all six analyzed modalities. [src: acinetobacter_adp1_explorer] It documented seven engineered ADP1 strains, measured protein abundance for 2,383 genes, and found high cross-strain proteomic correlation consistent with targeted effects of the pathway modifications. [src: acinetobacter_adp1_explorer]

The project connected the database to BERDL, finding matches for 13 of 13 genome IDs, 1,210 of 1,330 reactions, 230 of 230 compounds, and 4,891 of 4,891 cluster IDs, while ADP1 had zero matches in a Fitness Browser organism query. [src: acinetobacter_adp1_explorer] It developed a bridge between ADP1 mmseqs2-style cluster IDs and BERDL centroid gene IDs, mapping all 4,891 BERDL clusters to 4,081 unique ADP1 clusters with a 100% gene-level match across 43,754 genes. [src: acinetobacter_adp1_explorer] Comparing FBA and TnSeq results for 866 genes, the project found 639 concordant genes (73.8%) and 227 discordant genes, while essentiality calls identified 499 essential genes on minimal media and 346 on LB. [src: acinetobacter_adp1_explorer] It also reported condition-specific mutant fitness patterns across eight carbon sources, including a correlation of 0.11 between urea and quinate fitness and correlations of 0.58 and 0.53 for butanediol-acetate with butanediol-lactate and related central-carbon conditions, respectively. [src: acinetobacter_adp1_explorer]

## Projects (1)

- [[summaries/acinetobacter_adp1_explorer__REPORT|acinetobacter_adp1_explorer]]
