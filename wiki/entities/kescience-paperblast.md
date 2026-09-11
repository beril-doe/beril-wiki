---
type: "Dataset"
description: "KBase Data Lakehouse dataset linking protein sequences, genes, annotations, and literature."
sources: ["summaries/berdl_data_atlas__REPORT.md", "summaries/caulobacter_fur_lipida_loss__REPORT.md", "summaries/paperblast_explorer__REPORT.md"]
---
# KEScience PaperBLAST

## Identity

**Canonical name:** KEScience PaperBLAST. [src: berdl_data_atlas]

**Known alias:** PaperBLAST. [src: berdl_data_atlas]

**Stable external identifier:** No stable external identifier is reported in the source document. [src: berdl_data_atlas]

KEScience PaperBLAST is a dataset containing curated gene assignments derived from literature. [src: berdl_data_atlas] The PaperBLAST explorer **supports and broadens** this description: the `kescience_paperblast` collection contains **12.4 million rows across 14 tables** linking protein sequences and genes to literature, curated annotations, structural data, and PubMed Central full-text snippets. [src: paperblast_explorer]

The Caulobacter analysis **refines** this description by showing that PaperBLAST retrieval can miss known genes under naming-convention differences: its screen returned 0 hits for LpxA, LpxC, LpxD, and LpxK, and 1 for LpxB, versus 11, 15, 15, 18, and 18 NCBI hits, respectively. [src: caulobacter_fur_lipida_loss] The report characterized this as an approximately 80% false-negative rate for the tested Caulobacter lipid A genes, while retaining cross-species absence conclusions only when independently supported by NCBI annotation and literature. [src: caulobacter_fur_lipida_loss]

## Key Facts

The BERDL Data Atlas inventory contains **255,096 PaperBLAST curated gene assignments**. [src: berdl_data_atlas] The explorer **supports** this inventory figure by listing `curatedgene` with **255,096** curated annotations. [src: paperblast_explorer]

The atlas lists `kescience_paperblast` among the literature resources recommended for data-use planning, alongside [[entities/kescience-pubmed]]. [src: berdl_data_atlas]

PaperBLAST is part of the broader KBase Data Lakehouse inventory of **1,740 deduplicated tables across 119 databases, 17 tenants, and 10 funding agencies or programs**. [src: berdl_data_atlas]

The explorer **refines** expectations about coverage: **551K (65.6%)** of **841K** genes with any text-mined paper link have exactly one paper, and at **50%** sequence identity, **31,653** protein families have zero papers while **159,046** have exactly one. [src: paperblast_explorer] It also identifies **5,218** multi-member families representing **14,534** sequences with no literature. [src: paperblast_explorer]

A cross-database analysis found **129,823** VIMSS cross-references linking PaperBLAST to the Fitness Browser, providing a literature-to-fitness bridge. [src: paperblast_explorer]

The Caulobacter result **supports** using PaperBLAST as a literature-oriented scouting resource but **refines** its interpretation: naming-convention false negatives mean that absence of a PaperBLAST hit should not by itself establish absence of a gene or pathway. [src: caulobacter_fur_lipida_loss]

## Related Pages

- [[summaries/berdl_data_atlas__REPORT]] — source summary describing the PaperBLAST inventory and recommended uses.
- [[summaries/paperblast_explorer__REPORT]] — source summary quantifying PaperBLAST’s literature concentration, protein-family coverage, and Fitness Browser linkage.
- [[summaries/caulobacter_fur_lipida_loss__REPORT]] — source summary documenting PaperBLAST retrieval limits in Caulobacter lipid A-gene comparisons.
- [[entities/kescience-pubmed]] — related KEScience literature dataset.
- [[entities/uniprot]] — reference protein resource listed alongside PaperBLAST in the atlas.
