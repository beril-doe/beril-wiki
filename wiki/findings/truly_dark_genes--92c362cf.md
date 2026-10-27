---
type: "Finding"
description: "Of 39,532 Fitness Browser dark genes with pangenome links, bakta v1.12.0 reannotation reclassifies 33,105 (83.7%), leaving 6,427 \"truly dark\" genes where both the original pipeline and bakta agree these are hypothetical proteins; an additional 17,479 dark genes lack pangenome links and could not be assessed."
finding_id: "truly_dark_genes--92c362cf"
result: "observation"
source: "truly_dark_genes"
quantities: [{"value": "33,105", "what": "dark genes reclassified by bakta v1.12.0 reannotation", "unit": "genes", "denominator": "39,532 Fitness Browser dark genes with pangenome links", "scope": "Fitness Browser dark genes"}, {"value": "83.7%", "what": "share of linked dark genes reclassified by bakta", "unit": "percent", "denominator": "39,532 linked dark genes", "scope": "Fitness Browser"}, {"value": "6,427", "what": "truly dark genes remaining hypothetical under both annotations", "unit": "genes", "denominator": "", "scope": "Fitness Browser"}, {"value": "17,479", "what": "dark genes lacking pangenome links, not assessed", "unit": "genes", "denominator": "", "scope": "Fitness Browser"}]
caveat: "17,479 dark genes (31%) lack pangenome links and could not be assessed by bakta, and an estimated ~2,841 of these may be truly dark, a 31% coverage gap in the prioritized list."
first_added: "2026-10-23"
source_hash: "c3c61898305ee30bac02c9a1ff4d8c27bd21313ee4b736ea0055ea6d9014adf0"
---
# Reannotation resolves most dark genes, leaving small truly dark core

Of 39,532 Fitness Browser dark genes with pangenome links, bakta v1.12.0 reannotation reclassifies 33,105 (83.7%), leaving 6,427 "truly dark" genes where both the original pipeline and bakta agree these are hypothetical proteins; an additional 17,479 dark genes lack pangenome links and could not be assessed. [src: truly_dark_genes]

## Key figures

- **33,105 genes**: dark genes reclassified by bakta v1.12.0 reannotation (denominator 39,532 Fitness Browser dark genes with pangenome links; scope Fitness Browser dark genes) [src: truly_dark_genes]
- **83.7%**: share of linked dark genes reclassified by bakta (denominator 39,532 linked dark genes; scope Fitness Browser) [src: truly_dark_genes]
- **6,427 genes**: truly dark genes remaining hypothetical under both annotations (scope Fitness Browser) [src: truly_dark_genes]
- **17,479 genes**: dark genes lacking pangenome links, not assessed (scope Fitness Browser) [src: truly_dark_genes]

## Evidence

> Of 39,532 Fitness Browser dark genes with pangenome links, bakta v1.12.0 reannotation reclassifies 33,105 (83.7%) — leaving just 6,427 "truly dark" genes where both the original pipeline and bakta agree: these are hypothetical proteins. An additional 17,479 dark genes lack pangenome links and could not be assessed. [src: truly_dark_genes]

From the report [[summaries/truly_dark_genes__REPORT]].

## Caveat

17,479 dark genes (31%) lack pangenome links and could not be assessed by bakta, and an estimated ~2,841 of these may be truly dark, a 31% coverage gap in the prioritized list. [src: truly_dark_genes]

> - **Pangenome linkage gap**: 17,479 dark genes (31%) lack pangenome links and could not be assessed by bakta. An estimated ~2,841 of these may be truly dark, representing a 31% coverage gap in our prioritized list. [src: truly_dark_genes]

## Other caveats in this report

- Extrapolating the 16.3% truly-dark rate to 17,479 unlinked genes yields an estimated ~2,841 additional truly dark genes, including 2,208 with strong fitness phenotypes; the ranked list is estimated to cover ~69% of the total population. [src: truly_dark_genes]
- The report interprets shorter length, accessory-genome enrichment, GC deviation, mobile-element proximity, and narrow taxonomic breadth as consistent with recent acquisition and rapid evolution; this is an inference rather than a direct transfer measurement. [src: truly_dark_genes]
- The 41% hypothetical-neighbor pattern suggests genomic dark islands; recent acquisition, phage derivation, and species-specific neighborhoods are proposed origins, not demonstrated ones. [src: truly_dark_genes]
- Inter-species interaction, novel metabolism, and community-specific behavior are hypotheses proposed to explain community/nutrient enrichment, not established gene functions. [src: truly_dark_genes]
- Some bakta hypothetical-protein calls may be false negatives because known functions failed to match its PSC database at v6.0. [src: truly_dark_genes]
