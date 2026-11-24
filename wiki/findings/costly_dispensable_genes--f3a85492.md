---
type: "Finding"
description: "The SEED category \"Phages, Prophages, Transposable elements, Plasmids\" is 11.7x enriched (FDR=1.3e-17) in costly+dispensable vs costly+conserved genes."
finding_id: "costly_dispensable_genes--f3a85492"
result: "observation"
source: "costly_dispensable_genes"
quantities: [{"value": "11.7x", "what": "enrichment of the SEED phage/transposable element category", "unit": "", "denominator": "", "scope": ""}, {"value": "FDR=1.3e-17", "what": "significance of the enrichment", "unit": "", "denominator": "", "scope": ""}]
caveat: "SEED/KEGG annotations cover only 56-79% of genes; the unannotated fraction may have different functional profiles."
first_added: "2026-11-24"
source_hash: "09c61ea64ca662d2bfa768e341afaf3854e4a5dafe91dd4c4e17eb97d6d663c4"
---
# SEED phage and transposable element category enriched among costly dispensable genes

The SEED category "Phages, Prophages, Transposable elements, Plasmids" is 11.7x enriched (FDR=1.3e-17) in costly+dispensable vs costly+conserved genes. [src: costly_dispensable_genes]

## Key figures

- **11.7x**: enrichment of the SEED phage/transposable element category [src: costly_dispensable_genes]
- **FDR=1.3e-17**: significance of the enrichment [src: costly_dispensable_genes]

## Evidence

> SEED functional enrichment confirms this: the "Phages, Prophages, Transposable elements, Plasmids" category is 11.7x enriched (FDR=1.3e-17) and "Virulence" is 26.7x enriched (FDR=5.6e-14, though based on small counts: 21 vs 4 genes) in costly+dispensable vs costly+conserved genes. [src: costly_dispensable_genes]

From the report [[summaries/costly_dispensable_genes__REPORT]].

## Caveat

SEED/KEGG annotations cover only 56-79% of genes; the unannotated fraction may have different functional profiles. [src: costly_dispensable_genes]

> - SEED/KEGG annotations cover only 56-79% of genes; the unannotated fraction may have different functional profiles [src: costly_dispensable_genes]

## Other caveats in this report

- The report cautions that Virulence enrichment in costly+dispensable genes is based on small counts of 21 vs 4 genes. [src: costly_dispensable_genes]
- The report cautions that the singleton contrast is partly structural because core genes cannot be singletons by definition. [src: costly_dispensable_genes]
- The report proposes costly+dispensable genes as Black Queen process candidates but notes that they are predominantly selfish elements rather than metabolic genes and may precede actual gene loss. [src: costly_dispensable_genes]
- In the costly+dispensable gene analysis, burden is defined as max_fit > 1 in any experiment, so a single experiment can classify a gene as burdensome and make the classification sensitive to fitness-data noise. [src: costly_dispensable_genes]
- The report uses a binary pangenome core/auxiliary classification and notes that the fraction of genomes carrying a gene would provide more resolution. [src: costly_dispensable_genes]
