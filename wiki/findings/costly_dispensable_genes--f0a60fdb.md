---
type: "Finding"
description: "Orphan genes (no ortholog group) comprise 44.5% of costly+dispensable genes vs 13.1% for costly+conserved genes."
finding_id: "costly_dispensable_genes--f0a60fdb"
result: "observation"
source: "costly_dispensable_genes"
quantities: [{"value": "44.5%", "what": "orphan genes among costly+dispensable genes", "unit": "", "denominator": "", "scope": ""}, {"value": "13.1%", "what": "orphan genes among costly+conserved genes", "unit": "", "denominator": "", "scope": ""}]
caveat: "Ortholog group assignment uses BBH across 48 organisms, so genes with orthologs outside this set would be misclassified as orphans."
first_added: "2026-11-24"
source_hash: "09c61ea64ca662d2bfa768e341afaf3854e4a5dafe91dd4c4e17eb97d6d663c4"
---
# Costly dispensable genes are far more often orphans lacking orthologs

Orphan genes (no ortholog group) comprise 44.5% of costly+dispensable genes vs 13.1% for costly+conserved genes. [src: costly_dispensable_genes]

## Key figures

- **44.5%**: orphan genes among costly+dispensable genes [src: costly_dispensable_genes]
- **13.1%**: orphan genes among costly+conserved genes [src: costly_dispensable_genes]

## Evidence

> - **Taxonomically restricted**: 44.5% are orphan genes (no ortholog group) vs 13.1% for costly+conserved [src: costly_dispensable_genes]

From the report [[summaries/costly_dispensable_genes__REPORT]].

## Caveat

Ortholog group assignment uses BBH across 48 organisms, so genes with orthologs outside this set would be misclassified as orphans. [src: costly_dispensable_genes]

> - Ortholog group assignment uses BBH across 48 organisms; genes with orthologs outside this set would be misclassified as orphans [src: costly_dispensable_genes]

## Other caveats in this report

- The report cautions that Virulence enrichment in costly+dispensable genes is based on small counts of 21 vs 4 genes. [src: costly_dispensable_genes]
- The report cautions that the singleton contrast is partly structural because core genes cannot be singletons by definition. [src: costly_dispensable_genes]
- The report proposes costly+dispensable genes as Black Queen process candidates but notes that they are predominantly selfish elements rather than metabolic genes and may precede actual gene loss. [src: costly_dispensable_genes]
- In the costly+dispensable gene analysis, burden is defined as max_fit > 1 in any experiment, so a single experiment can classify a gene as burdensome and make the classification sensitive to fitness-data noise. [src: costly_dispensable_genes]
- SEED/KEGG annotations cover only 56-79% of genes in the costly+dispensable gene analysis, and the unannotated fraction may have different functional profiles. [src: costly_dispensable_genes]
