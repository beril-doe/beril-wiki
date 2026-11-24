---
type: "Finding"
description: "Essential-core enrichment was statistically significant in 18 of 33 organisms by Fisher's exact test with BH-FDR q < 0.05."
finding_id: "conservation_vs_fitness--631185af"
result: "observation"
source: "conservation_vs_fitness"
quantities: [{"value": "18 of 33 organisms", "what": "organisms with significant essential-core enrichment", "unit": "", "denominator": "", "scope": "Fisher's exact test, BH-FDR q < 0.05"}]
caveat: "Clades with only 2 genomes have trivially high core fractions (a gene in both genomes = 100% = core), reducing the discriminative power of core/auxiliary classification."
first_added: "2026-11-24"
source_hash: "e0d31ced5965dc2bd3597dc43f0c63a33ad3497af8e9ec712d9369ae6c9aa197"
---
# Essential-core enrichment is significant in just over half of organisms

Essential-core enrichment was statistically significant in 18 of 33 organisms by Fisher's exact test with BH-FDR q < 0.05. [src: conservation_vs_fitness]

## Key figures

- **18 of 33 organisms**: organisms with significant essential-core enrichment (scope Fisher's exact test, BH-FDR q < 0.05) [src: conservation_vs_fitness]

## Evidence

> **18 of 33 organisms** show statistically significant enrichment (Fisher's exact test, BH-FDR q < 0.05) [src: conservation_vs_fitness]

From the report [[summaries/conservation_vs_fitness__REPORT]].

## Caveat

Clades with only 2 genomes have trivially high core fractions (a gene in both genomes = 100% = core), reducing the discriminative power of core/auxiliary classification. [src: conservation_vs_fitness]

> **Pangenome coverage varies**: Clades with only 2 genomes have trivially high core fractions (a gene in both genomes = 100% = core), reducing the discriminative power of core/auxiliary classification. [src: conservation_vs_fitness]

## Other caveats in this report

- The 4 unmatched Fitness Browser organisms were Cola, Kang, Magneto, and SB2B because their species had too few genomes in GTDB for pangenome construction. [src: conservation_vs_fitness]
- Gene-length validation shows essential genes are slightly shorter on average, consistent with some transposon insertion bias. [src: conservation_vs_fitness]
- The report treats its essential-gene definition as an upper bound because absent fitness data may reflect short genes, low-complexity regions, or scaffold edges rather than essentiality. [src: conservation_vs_fitness]
- Escherichia coli was excluded because its main clade was absent from the pangenome due to too many genomes, while Keio (E. coli BW25113) mapped to s__Escherichia_coli_E at only 26.1% coverage. [src: conservation_vs_fitness]
- RB-TnSeq essentiality is defined under specific library-construction conditions and would not capture genes essential only under stress. [src: conservation_vs_fitness]
