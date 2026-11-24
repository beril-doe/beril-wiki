---
type: "Finding"
description: "Of 39,532 Fitness Browser dark genes with pangenome links, bakta v1.12.0 reannotation reclassifies 33,105 (83.7%), leaving 6,427 truly dark genes called hypothetical by both the original pipeline and bakta."
finding_id: "truly_dark_genes--dbb9db3b"
result: "observation"
source: "truly_dark_genes"
quantities: [{"value": "33,105", "what": "dark genes reclassified by bakta", "unit": "", "denominator": "39,532 dark genes with pangenome links", "scope": "Fitness Browser"}, {"value": "83.7%", "what": "fraction reclassified by bakta", "unit": "", "denominator": "", "scope": ""}, {"value": "6,427", "what": "truly dark genes remaining", "unit": "", "denominator": "", "scope": "hypothetical in both pipelines"}]
caveat: "17,479 dark genes (31%) lack pangenome links and could not be assessed by bakta, and an estimated ~2,841 of these may be truly dark."
first_added: "2026-11-24"
source_hash: "c3c61898305ee30bac02c9a1ff4d8c27bd21313ee4b736ea0055ea6d9014adf0"
---
# Bakta reannotation resolves most Fitness Browser dark genes, leaving a hard core

Of 39,532 Fitness Browser dark genes with pangenome links, bakta v1.12.0 reannotation reclassifies 33,105 (83.7%), leaving 6,427 truly dark genes called hypothetical by both the original pipeline and bakta. [src: truly_dark_genes]

## Key figures

- **33,105**: dark genes reclassified by bakta (denominator 39,532 dark genes with pangenome links; scope Fitness Browser) [src: truly_dark_genes]
- **83.7%**: fraction reclassified by bakta [src: truly_dark_genes]
- **6,427**: truly dark genes remaining (scope hypothetical in both pipelines) [src: truly_dark_genes]

## Evidence

> Of 39,532 Fitness Browser dark genes with pangenome links, bakta v1.12.0 reannotation reclassifies 33,105 (83.7%) — leaving just 6,427 "truly dark" genes where both the original pipeline and bakta agree: these are hypothetical proteins. [src: truly_dark_genes]

From the report [[summaries/truly_dark_genes__REPORT]].

## Caveat

17,479 dark genes (31%) lack pangenome links and could not be assessed by bakta, and an estimated ~2,841 of these may be truly dark. [src: truly_dark_genes]

> **Pangenome linkage gap**: 17,479 dark genes (31%) lack pangenome links and could not be assessed by bakta. An estimated ~2,841 of these may be truly dark, representing a 31% coverage gap in our prioritized list. [src: truly_dark_genes]

## Other caveats in this report

- An additional 17,479 Fitness Browser dark genes lack pangenome links and could not be assessed. [src: truly_dark_genes]
- The report estimates ~2,841 additional truly dark genes among 17,479 unlinked dark genes at the 16.3% truly-dark rate, including 2,208 with strong fitness phenotypes. [src: truly_dark_genes]
- The ranked list covers ~69% of the estimated total truly dark gene population. [src: truly_dark_genes]
- Some bakta hypothetical-protein calls may be false negatives for genes with known functions that failed to match the PSC database version tested (v6.0). [src: truly_dark_genes]
- BBH orthologs cover only 32 of 48 Fitness Browser organisms, leaving truly dark genes from the remaining 16 organisms without concordance and ortholog-breadth data. [src: truly_dark_genes]
