---
type: "Finding"
description: "Costly+dispensable genes are 7.45x more likely than costly+conserved genes to contain mobile element keywords in their descriptions (transposase, integrase, phage, IS element, recombinase, prophage; OR=7.45, p=4.6e-71)."
finding_id: "costly_dispensable_genes--31cecf6a"
result: "observation"
source: "costly_dispensable_genes"
quantities: [{"value": "7.45x", "what": "odds of mobile element keywords in descriptions, costly+dispensable vs costly+conserved", "unit": "", "denominator": "", "scope": ""}, {"value": "p=4.6e-71", "what": "significance of the odds ratio", "unit": "", "denominator": "", "scope": ""}]
caveat: "Burden is defined as max_fit > 1 in any experiment, so a single experiment can classify a gene as burdensome, making the classification sensitive to noise in the fitness data."
first_added: "2026-11-24"
source_hash: "09c61ea64ca662d2bfa768e341afaf3854e4a5dafe91dd4c4e17eb97d6d663c4"
---
# Costly dispensable genes are strongly enriched for mobile-element keywords

Costly+dispensable genes are 7.45x more likely than costly+conserved genes to contain mobile element keywords in their descriptions (transposase, integrase, phage, IS element, recombinase, prophage; OR=7.45, p=4.6e-71). [src: costly_dispensable_genes]

## Key figures

- **7.45x**: odds of mobile element keywords in descriptions, costly+dispensable vs costly+conserved [src: costly_dispensable_genes]
- **p=4.6e-71**: significance of the odds ratio [src: costly_dispensable_genes]

## Evidence

> They are **7.45x more likely** to contain mobile element keywords in their descriptions (transposase, integrase, phage, IS element, recombinase, prophage; OR=7.45, p=4.6e-71). [src: costly_dispensable_genes]

From the report [[summaries/costly_dispensable_genes__REPORT]].

## Caveat

Burden is defined as max_fit > 1 in any experiment, so a single experiment can classify a gene as burdensome, making the classification sensitive to noise in the fitness data. [src: costly_dispensable_genes]

> - "Burden" is defined as max_fit > 1 in any experiment -- a single experiment can classify a gene as burdensome, making this sensitive to noise in the fitness data [src: costly_dispensable_genes]

## Other caveats in this report

- The report cautions that Virulence enrichment in costly+dispensable genes is based on small counts of 21 vs 4 genes. [src: costly_dispensable_genes]
- The report cautions that the singleton contrast is partly structural because core genes cannot be singletons by definition. [src: costly_dispensable_genes]
- The report proposes costly+dispensable genes as Black Queen process candidates but notes that they are predominantly selfish elements rather than metabolic genes and may precede actual gene loss. [src: costly_dispensable_genes]
- SEED/KEGG annotations cover only 56-79% of genes in the costly+dispensable gene analysis, and the unannotated fraction may have different functional profiles. [src: costly_dispensable_genes]
- The report uses a binary pangenome core/auxiliary classification and notes that the fraction of genomes carrying a gene would provide more resolution. [src: costly_dispensable_genes]
