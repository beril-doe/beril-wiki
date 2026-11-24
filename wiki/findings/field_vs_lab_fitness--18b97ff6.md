---
type: "Finding"
description: "In DvH, genes important for field-stress conditions are significantly more conserved than baseline (83.6% core, OR=1.58, FDR q=0.026)."
finding_id: "field_vs_lab_fitness--18b97ff6"
result: "observation"
source: "field_vs_lab_fitness"
quantities: [{"value": "83.6%", "what": "core fraction of field-stress important genes", "unit": "", "denominator": "", "scope": ""}, {"value": "1.58", "what": "odds ratio versus baseline", "unit": "", "denominator": "", "scope": ""}, {"value": "0.026", "what": "FDR q-value", "unit": "", "denominator": "", "scope": ""}]
caveat: "The Nitratidesulfovibrio vulgaris pangenome has relatively few genomes, creating a coarse core/auxiliary classification with a high baseline core fraction (76.3%), which compresses effect sizes."
first_added: "2026-11-24"
source_hash: "8bf50c605e80b6db78122bc45bdfce5cb3ef8bc17821932e2e7ab7fb94e5622c"
---
# Field-stress genes are more core than baseline in DvH

In DvH, genes important for field-stress conditions are significantly more conserved than baseline (83.6% core, OR=1.58, FDR q=0.026). [src: field_vs_lab_fitness]

## Key figures

- **83.6%**: core fraction of field-stress important genes [src: field_vs_lab_fitness]
- **1.58**: odds ratio versus baseline [src: field_vs_lab_fitness]
- **0.026**: FDR q-value [src: field_vs_lab_fitness]

## Evidence

> Genes important for field-stress conditions are significantly more conserved than baseline (83.6% core, OR=1.58, FDR q=0.026), as are field-core genes (82.4%, OR=1.46, q=0.026). [src: field_vs_lab_fitness]

From the report [[summaries/field_vs_lab_fitness__REPORT]].

## Caveat

The Nitratidesulfovibrio vulgaris pangenome has relatively few genomes, creating a coarse core/auxiliary classification with a high baseline core fraction (76.3%), which compresses effect sizes. [src: field_vs_lab_fitness]

> The *Nitratidesulfovibrio vulgaris* pangenome has relatively few genomes, creating a coarse core/auxiliary classification with a high baseline core fraction (76.3%), which compresses effect sizes [src: field_vs_lab_fitness]

## Other caveats in this report

- The report considers ENIGMA CORAL field geochemistry and community-composition data potentially useful for future analyses but not for gene-level fitness analysis. [src: field_vs_lab_fitness]
- The DvH fitness-conservation analysis excludes 678 essential genes (80.1% core) because no transposon mutants were recovered and they lack fitness data. [src: field_vs_lab_fitness]
- The report attributes the DvH lab-antibiotic conservation dip at -2 to a small sample (n=109 at -2 vs n=45 at -3). [src: field_vs_lab_fitness]
- The DvH fitness analysis excludes 678 essential genes (80.1% core) because they lack transposon mutants. [src: field_vs_lab_fitness]
- Including excluded DvH essential genes would slightly raise the overall baseline but would not change condition-class comparisons, which use only non-essential genes. [src: field_vs_lab_fitness]
