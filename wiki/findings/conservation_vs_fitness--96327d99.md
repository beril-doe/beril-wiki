---
type: "Finding"
description: "Essential-unmapped genes (1,259 strain-specific essentials with no pangenome cluster match) are the least characterized, at 44.7% hypothetical."
finding_id: "conservation_vs_fitness--96327d99"
result: "observation"
source: "conservation_vs_fitness"
quantities: [{"value": "1,259", "what": "essential-unmapped genes", "unit": "genes", "denominator": "", "scope": ""}, {"value": "44.7%", "what": "hypothetical fraction of essential-unmapped genes", "unit": "percent", "denominator": "", "scope": ""}]
caveat: "10 organisms were excluded from Phase 2 due to <90% DIAMOND coverage, reducing taxonomic breadth."
first_added: "2026-11-24"
source_hash: "e0d31ced5965dc2bd3597dc43f0c63a33ad3497af8e9ec712d9369ae6c9aa197"
---
# Essential-unmapped genes are the least characterized category

Essential-unmapped genes (1,259 strain-specific essentials with no pangenome cluster match) are the least characterized, at 44.7% hypothetical. [src: conservation_vs_fitness]

## Key figures

- **1,259 genes**: essential-unmapped genes [src: conservation_vs_fitness]
- **44.7%**: hypothetical fraction of essential-unmapped genes [src: conservation_vs_fitness]

## Evidence

> **Essential-unmapped genes** (1,259 strain-specific essentials with no pangenome cluster match) are the least characterized (44.7% hypothetical). [src: conservation_vs_fitness]

From the report [[summaries/conservation_vs_fitness__REPORT]].

## Caveat

10 organisms were excluded from Phase 2 due to <90% DIAMOND coverage, reducing taxonomic breadth. [src: conservation_vs_fitness]

> **10 organisms excluded from Phase 2** due to <90% DIAMOND coverage, reducing taxonomic breadth. [src: conservation_vs_fitness]

## Other caveats in this report

- The 4 unmatched Fitness Browser organisms were Cola, Kang, Magneto, and SB2B because their species had too few genomes in GTDB for pangenome construction. [src: conservation_vs_fitness]
- Gene-length validation shows essential genes are slightly shorter on average, consistent with some transposon insertion bias. [src: conservation_vs_fitness]
- The report treats its essential-gene definition as an upper bound because absent fitness data may reflect short genes, low-complexity regions, or scaffold edges rather than essentiality. [src: conservation_vs_fitness]
- Pangenome clades with only 2 genomes have trivially high core fractions because a gene in both genomes is 100% core, reducing core/auxiliary discrimination. [src: conservation_vs_fitness]
- Escherichia coli was excluded because its main clade was absent from the pangenome due to too many genomes, while Keio (E. coli BW25113) mapped to s__Escherichia_coli_E at only 26.1% coverage. [src: conservation_vs_fitness]
