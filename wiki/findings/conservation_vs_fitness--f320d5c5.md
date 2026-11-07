---
type: "Finding"
description: "Among 3,683 essential-auxiliary genes, 38.2% were hypothetical and 13.4% enzymes, with top subsystems ribosomes, DNA replication, type 4 secretion and plasmid replication, which the report suggests reflects strain-specific variants of core machinery plus mobile genetic elements."
finding_id: "conservation_vs_fitness--f320d5c5"
result: "inference"
source: "conservation_vs_fitness"
quantities: [{"value": "3,683", "what": "essential-auxiliary genes", "unit": "genes", "denominator": "", "scope": ""}, {"value": "38.2%", "what": "share of essential-auxiliary genes that are hypothetical", "unit": "%", "denominator": "essential-auxiliary genes", "scope": ""}, {"value": "13.4%", "what": "share of essential-auxiliary genes that are enzymes", "unit": "%", "denominator": "essential-auxiliary genes", "scope": ""}]
caveat: "Clades with only 2 genomes have trivially high core fractions (a gene in both genomes is 100% core), reducing the discriminative power of core/auxiliary classification."
first_added: "2026-10-27"
source_hash: "e0d31ced5965dc2bd3597dc43f0c63a33ad3497af8e9ec712d9369ae6c9aa197"
---
# Essential-auxiliary genes are poorly characterized and may reflect strain-specific machinery

Among 3,683 essential-auxiliary genes, 38.2% were hypothetical and 13.4% enzymes, with top subsystems ribosomes, DNA replication, type 4 secretion and plasmid replication, which the report suggests reflects strain-specific variants of core machinery plus mobile genetic elements. [src: conservation_vs_fitness]

## Key figures

- **3,683 genes**: essential-auxiliary genes [src: conservation_vs_fitness]
- **38.2%**: share of essential-auxiliary genes that are hypothetical (denominator essential-auxiliary genes) [src: conservation_vs_fitness]
- **13.4%**: share of essential-auxiliary genes that are enzymes (denominator essential-auxiliary genes) [src: conservation_vs_fitness]

## Evidence

> **Essential-auxiliary genes** (3,683 genes essential for viability but not in all strains) are poorly characterized (38.2% hypothetical) and less likely to be enzymes (13.4%). Top subsystems: ribosomes, DNA replication, type 4 secretion, plasmid replication -- suggesting strain-specific variants of core machinery plus mobile genetic elements. [src: conservation_vs_fitness]

From the report [[summaries/conservation_vs_fitness__REPORT]].

## Caveat

Clades with only 2 genomes have trivially high core fractions (a gene in both genomes is 100% core), reducing the discriminative power of core/auxiliary classification. [src: conservation_vs_fitness]

> - **Pangenome coverage varies**: Clades with only 2 genomes have trivially high core fractions (a gene in both genomes = 100% = core), reducing the discriminative power of core/auxiliary classification. [src: conservation_vs_fitness]

## Other caveats in this report

- 34 organisms had >=90% mapping coverage, but only 33 entered downstream analysis because Dyella79 had a locus-tag mismatch. [src: conservation_vs_fitness]
- Putative essential genes were slightly shorter on average, consistent with possible transposon-insertion bias. [src: conservation_vs_fitness]
- The report characterizes the essential-core association as modest (OR=1.56), noting that many genes are core irrespective of essentiality. [src: conservation_vs_fitness]
- The report cites TraDIS work in E. coli K-12 as a precedent for gene-length bias in transposon-based essentiality calls. [src: conservation_vs_fitness]
- The putative-essential definition is an upper bound: absent fitness data may reflect short genes, low-complexity regions, or scaffold edges rather than essentiality; shorter average gene length suggests some insertion bias. [src: conservation_vs_fitness]
