---
type: "Finding"
description: "Essential-core genes are the most enzyme-rich (41.9%) and best-annotated (87% with known function) category."
finding_id: "conservation_vs_fitness--3b44ab09"
result: "observation"
source: "conservation_vs_fitness"
quantities: [{"value": "41.9%", "what": "enzyme fraction of essential-core genes", "unit": "percent", "denominator": "", "scope": ""}, {"value": "87%", "what": "essential-core genes with known function", "unit": "percent", "denominator": "", "scope": ""}]
caveat: "RB-TnSeq essentiality is defined under the specific library construction conditions, so genes essential only under stress conditions would not be captured."
first_added: "2026-11-24"
source_hash: "e0d31ced5965dc2bd3597dc43f0c63a33ad3497af8e9ec712d9369ae6c9aa197"
---
# Essential-core genes are the most enzyme-rich and best annotated

Essential-core genes are the most enzyme-rich (41.9%) and best-annotated (87% with known function) category. [src: conservation_vs_fitness]

## Key figures

- **41.9%**: enzyme fraction of essential-core genes [src: conservation_vs_fitness]
- **87%**: essential-core genes with known function [src: conservation_vs_fitness]

## Evidence

> **Essential-core genes** are the most enzyme-rich (41.9%) and best-annotated (87% with known function). [src: conservation_vs_fitness]

From the report [[summaries/conservation_vs_fitness__REPORT]].

## Caveat

RB-TnSeq essentiality is defined under the specific library construction conditions, so genes essential only under stress conditions would not be captured. [src: conservation_vs_fitness]

> **Single growth condition for essentiality**: RB-TnSeq essentiality is defined under the specific library construction conditions. Genes essential only under stress conditions would not be captured. [src: conservation_vs_fitness]

## Other caveats in this report

- The 4 unmatched Fitness Browser organisms were Cola, Kang, Magneto, and SB2B because their species had too few genomes in GTDB for pangenome construction. [src: conservation_vs_fitness]
- Gene-length validation shows essential genes are slightly shorter on average, consistent with some transposon insertion bias. [src: conservation_vs_fitness]
- The report treats its essential-gene definition as an upper bound because absent fitness data may reflect short genes, low-complexity regions, or scaffold edges rather than essentiality. [src: conservation_vs_fitness]
- Pangenome clades with only 2 genomes have trivially high core fractions because a gene in both genomes is 100% core, reducing core/auxiliary discrimination. [src: conservation_vs_fitness]
- Escherichia coli was excluded because its main clade was absent from the pangenome due to too many genomes, while Keio (E. coli BW25113) mapped to s__Escherichia_coli_E at only 26.1% coverage. [src: conservation_vs_fitness]
