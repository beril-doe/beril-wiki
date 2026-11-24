---
type: "Dataset"
description: "Curated reviewed protein database from which exemplar bacterial enzyme sequences were retrieved."
sources: ["summaries/annotation_gap_discovery__REPORT.md", "summaries/paperblast_explorer__REPORT.md"]
aliases: ["UniProt Swiss-Prot"]
---
# Swiss-Prot

This page covers Swiss-Prot (UniProt Swiss-Prot), the curated protein database from which exemplar bacterial enzyme sequences were retrieved. The evidence comes from two projects, each a direct count. [src: annotation_gap_discovery, paperblast_explorer]

## Key facts

- The exemplar set in [[summaries/annotation_gap_discovery__REPORT]] had 328 reviewed bacterial sequences for 75/84 unique Enzyme Commission (EC) numbers, retrieved from the UniProt representational state transfer (REST) application programming interface (API). [src: annotation_gap_discovery]
- [[entities/diamond]] v2.1.16 blastp found 154 hits against these exemplars. The parameters were `--evalue 1e-5 --max-target-seqs 20 --id 25 --query-cover 50 --outfmt 6`. [src: annotation_gap_discovery]

## Role in PaperBLAST

SwissProt contributes the most curated entries to [[entities/paperblast]], with 110K proteins and 182K unique papers. [src: paperblast_explorer] The curated-database table gives 110,171 proteins, 181,916 papers and 1.7 papers/protein. [src: paperblast_explorer]

PaperBLAST covers only part of SwissProt. It includes approximately 19% of the full database (~570K reviewed entries as of 2024). This is the subset matched to PMC open-access literature. [src: paperblast_explorer] Many entries probably lack matching PMC full text. So curated knowledge exists for proteins that PaperBLAST cannot connect to. [src: paperblast_explorer] See [[concepts/literature-coverage-bias-and-text-mining-limits]] and [[summaries/paperblast_explorer__REPORT]].
