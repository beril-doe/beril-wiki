---
type: "Finding"
description: "Compared with annotation-lag genes, truly dark genes have median length 121 versus 194 aa, core-genome fraction 43.1% versus 72.7%, has-orthologs 29.3% versus 63.7%, and median ortholog breadth 1 versus 4 organisms, with effect sizes and p-values reported for each."
finding_id: "truly_dark_genes--947aec4f"
result: "observation"
source: "truly_dark_genes"
quantities: [{"value": "121 vs 194", "what": "median gene length, truly dark vs annotation-lag", "unit": "aa", "denominator": "", "scope": ""}, {"value": "43.1% vs 72.7%", "what": "core genome fraction, truly dark vs annotation-lag", "unit": "percent", "denominator": "", "scope": ""}, {"value": "29.3% vs 63.7%", "what": "fraction with orthologs, truly dark vs annotation-lag", "unit": "percent", "denominator": "", "scope": ""}, {"value": "1 vs 4", "what": "median ortholog breadth, truly dark vs annotation-lag", "unit": "organisms", "denominator": "", "scope": ""}]
caveat: "Short genes are harder to annotate and harder to measure fitness for, so the length difference (d = \u22120.432) may partially explain other observed differences."
first_added: "2026-10-23"
source_hash: "c3c61898305ee30bac02c9a1ff4d8c27bd21313ee4b736ea0055ea6d9014adf0"
---
# Truly dark genes are shorter, more accessory, with narrower ortholog breadth

Compared with annotation-lag genes, truly dark genes have median length 121 versus 194 aa, core-genome fraction 43.1% versus 72.7%, has-orthologs 29.3% versus 63.7%, and median ortholog breadth 1 versus 4 organisms, with effect sizes and p-values reported for each. [src: truly_dark_genes]

## Key figures

- **121 vs 194 aa**: median gene length, truly dark vs annotation-lag [src: truly_dark_genes]
- **43.1% vs 72.7%**: core genome fraction, truly dark vs annotation-lag [src: truly_dark_genes]
- **29.3% vs 63.7%**: fraction with orthologs, truly dark vs annotation-lag [src: truly_dark_genes]
- **1 vs 4 organisms**: median ortholog breadth, truly dark vs annotation-lag [src: truly_dark_genes]

## Evidence

> | Median length (aa) | 121 | 194 | d = −0.432 | < 1e-100 | | Core genome fraction | 43.1% | 72.7% | OR = 0.284 | < 1e-100 | | Essential fraction | 18.0% | 13.4% | OR = 1.420 | < 1e-10 | | Mean GC content | 0.542 | 0.584 | d = −0.395 | 2e-115 | | Has orthologs | 29.3% | 63.7% | OR = 0.236 | < 1e-100 | | Ortholog breadth (median orgs) | 1 | 4 | d = −1.072 | < 1e-100 | [src: truly_dark_genes]

From the report [[summaries/truly_dark_genes__REPORT]].

## Caveat

Short genes are harder to annotate and harder to measure fitness for, so the length difference (d = −0.432) may partially explain other observed differences. [src: truly_dark_genes]

> - **Gene length confound**: Short genes are inherently harder to annotate (fewer domains, fewer homologs) AND harder to measure fitness for (fewer TA sites). The length difference (d = −0.432) may partially explain other observed differences. [src: truly_dark_genes]

## Other caveats in this report

- Extrapolating the 16.3% truly-dark rate to 17,479 unlinked genes yields an estimated ~2,841 additional truly dark genes, including 2,208 with strong fitness phenotypes; the ranked list is estimated to cover ~69% of the total population. [src: truly_dark_genes]
- The report interprets shorter length, accessory-genome enrichment, GC deviation, mobile-element proximity, and narrow taxonomic breadth as consistent with recent acquisition and rapid evolution; this is an inference rather than a direct transfer measurement. [src: truly_dark_genes]
- The 41% hypothetical-neighbor pattern suggests genomic dark islands; recent acquisition, phage derivation, and species-specific neighborhoods are proposed origins, not demonstrated ones. [src: truly_dark_genes]
- Inter-species interaction, novel metabolism, and community-specific behavior are hypotheses proposed to explain community/nutrient enrichment, not established gene functions. [src: truly_dark_genes]
- 17,479 dark genes (31%) lack pangenome links and could not be assessed by bakta; ~2,841 potentially truly dark genes among them are extrapolated, yielding a stated 31% prioritization coverage gap. [src: truly_dark_genes]
