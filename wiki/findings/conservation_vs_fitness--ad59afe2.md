---
type: "Finding"
description: "In the Fitness Browser conservation analysis, essential genes are 86.1% core vs 81.2% for non-essential genes."
finding_id: "conservation_vs_fitness--ad59afe2"
result: "observation"
source: "conservation_vs_fitness"
quantities: [{"value": "86.1%", "what": "fraction of essential genes that are core", "unit": "percent", "denominator": "essential genes", "scope": ""}, {"value": "81.2%", "what": "fraction of non-essential genes that are core", "unit": "percent", "denominator": "non-essential genes", "scope": ""}]
caveat: "The essential gene definition is an upper bound, because genes without fitness data may lack transposon insertions due to being short, in low-complexity regions, or at scaffold edges, not necessarily because they are essential."
first_added: "2026-11-24"
source_hash: "e0d31ced5965dc2bd3597dc43f0c63a33ad3497af8e9ec712d9369ae6c9aa197"
---
# Essential genes are modestly more likely to be core

In the Fitness Browser conservation analysis, essential genes are 86.1% core vs 81.2% for non-essential genes. [src: conservation_vs_fitness]

## Key figures

- **86.1%**: fraction of essential genes that are core (denominator essential genes) [src: conservation_vs_fitness]
- **81.2%**: fraction of non-essential genes that are core (denominator non-essential genes) [src: conservation_vs_fitness]

## Evidence

> Essential genes are **86.1% core** vs 81.2% for non-essential genes [src: conservation_vs_fitness]

From the report [[summaries/conservation_vs_fitness__REPORT]].

## Caveat

The essential gene definition is an upper bound, because genes without fitness data may lack transposon insertions due to being short, in low-complexity regions, or at scaffold edges, not necessarily because they are essential. [src: conservation_vs_fitness]

> **Essential gene definition is an upper bound**: Genes without fitness data may lack transposon insertions due to being short, in low-complexity regions, or at scaffold edges -- not necessarily because they are essential. [src: conservation_vs_fitness]

## Other caveats in this report

- The 4 unmatched Fitness Browser organisms were Cola, Kang, Magneto, and SB2B because their species had too few genomes in GTDB for pangenome construction. [src: conservation_vs_fitness]
- Gene-length validation shows essential genes are slightly shorter on average, consistent with some transposon insertion bias. [src: conservation_vs_fitness]
- Pangenome clades with only 2 genomes have trivially high core fractions because a gene in both genomes is 100% core, reducing core/auxiliary discrimination. [src: conservation_vs_fitness]
- Escherichia coli was excluded because its main clade was absent from the pangenome due to too many genomes, while Keio (E. coli BW25113) mapped to s__Escherichia_coli_E at only 26.1% coverage. [src: conservation_vs_fitness]
- RB-TnSeq essentiality is defined under specific library-construction conditions and would not capture genes essential only under stress. [src: conservation_vs_fitness]
