---
type: "Finding"
description: "In costly+dispensable versus costly+conserved genes, the SEED category 'Phages, Prophages, Transposable elements, Plasmids' is 11.7x enriched (FDR=1.3e-17) and 'Virulence' is 26.7x enriched (FDR=5.6e-14, based on small counts: 21 vs 4 genes)."
finding_id: "costly_dispensable_genes--f3a85492"
result: "observation"
source: "costly_dispensable_genes"
quantities: [{"value": "11.7x", "what": "enrichment of Phages/Prophages/Transposable elements/Plasmids SEED category", "unit": "fold", "denominator": "", "scope": "costly+dispensable vs costly+conserved"}, {"value": "26.7x", "what": "enrichment of Virulence SEED category, based on small counts of 21 vs 4 genes", "unit": "fold", "denominator": "", "scope": "costly+dispensable vs costly+conserved"}, {"value": "5.6e-14", "what": "FDR for Virulence enrichment", "unit": "", "denominator": "", "scope": "costly+dispensable vs costly+conserved"}]
caveat: "SEED/KEGG annotations cover only 56-79% of genes, and the unannotated fraction may have different functional profiles."
first_added: "2026-10-27"
source_hash: "09c61ea64ca662d2bfa768e341afaf3854e4a5dafe91dd4c4e17eb97d6d663c4"
---
# Mobile-element and virulence SEED categories enriched versus costly conserved genes

In costly+dispensable versus costly+conserved genes, the SEED category 'Phages, Prophages, Transposable elements, Plasmids' is 11.7x enriched (FDR=1.3e-17) and 'Virulence' is 26.7x enriched (FDR=5.6e-14, based on small counts: 21 vs 4 genes). [src: costly_dispensable_genes]

## Key figures

- **11.7x fold**: enrichment of Phages/Prophages/Transposable elements/Plasmids SEED category (scope costly+dispensable vs costly+conserved) [src: costly_dispensable_genes]
- **26.7x fold**: enrichment of Virulence SEED category, based on small counts of 21 vs 4 genes (scope costly+dispensable vs costly+conserved) [src: costly_dispensable_genes]
- **5.6e-14**: FDR for Virulence enrichment (scope costly+dispensable vs costly+conserved) [src: costly_dispensable_genes]

## Evidence

> SEED functional enrichment confirms this: the "Phages, Prophages, Transposable elements, Plasmids" category is 11.7x enriched (FDR=1.3e-17) and "Virulence" is 26.7x enriched (FDR=5.6e-14, though based on small counts: 21 vs 4 genes) in costly+dispensable vs costly+conserved genes. [src: costly_dispensable_genes]

From the report [[summaries/costly_dispensable_genes__REPORT]].

## Caveat

SEED/KEGG annotations cover only 56-79% of genes, and the unannotated fraction may have different functional profiles. [src: costly_dispensable_genes]

> - SEED/KEGG annotations cover only 56-79% of genes; the unannotated fraction may have different functional profiles [src: costly_dispensable_genes]

## Other caveats in this report

- The singleton contrast is partly structural because core genes cannot be singletons by definition. [src: costly_dispensable_genes]
- The report interprets costly+conserved genes as costly in lab assays but retained by environmental selection. [src: costly_dispensable_genes]
- The report proposes a strain-specific recent mobile-element invasion or genomic expansion as a possible explanation for psRCH2. [src: costly_dispensable_genes]
- The authors interpret costly+dispensable genes as HGT-associated genomic debris, including insertion sequences, prophage remnants, transposases and defense systems; this is interpretation rather than direct provenance measurement. [src: costly_dispensable_genes]
- The report hypothesizes ongoing loss of costly+dispensable genes unless some environments provide compensating selective advantage. [src: costly_dispensable_genes]
