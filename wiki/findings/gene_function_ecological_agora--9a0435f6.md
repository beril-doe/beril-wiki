---
type: "Finding"
description: "Alm 2006's r \u2248 0.74 was not reproduced across n=18,989 (r=0.10\u20130.29), although architectural concordance was r=0.67."
finding_id: "gene_function_ecological_agora--9a0435f6"
result: "null result"
source: "gene_function_ecological_agora"
quantities: [{"value": "r=0.10\u20130.29", "what": "observed correlation across four framings", "unit": "r", "denominator": "n=18,989", "scope": "P4-D3"}, {"value": "r \u2248 0.74", "what": "Alm 2006 reported correlation", "unit": "r", "denominator": "", "scope": ""}, {"value": "r=0.67", "what": "architectural concordance (NB17)", "unit": "r", "denominator": "", "scope": "qualitative result holds"}]
caveat: "The report proposes substrate-scale heterogeneity, tree-aware versus paralog-count operationalization, and tree-rank granularity as reasons the point estimate did not survive scaling from 207 to 18,989 genomes."
first_added: "2026-11-09"
source_hash: "ec22f37a485c95d0e067c1984020af5580f9f103cae1582742ed63f035a74a69"
---
# Alm's strong histidine-kinase correlation does not reproduce at GTDB scale

Alm 2006's r ≈ 0.74 was not reproduced across n=18,989 (r=0.10–0.29), although architectural concordance was r=0.67. [src: gene_function_ecological_agora]

## Key figures

- **r=0.10–0.29 r**: observed correlation across four framings (denominator n=18,989; scope P4-D3) [src: gene_function_ecological_agora]
- **r ≈ 0.74 r**: Alm 2006 reported correlation [src: gene_function_ecological_agora]
- **r=0.67 r**: architectural concordance (NB17) (scope qualitative result holds) [src: gene_function_ecological_agora]

## Evidence

> | H4 | Alm 2006 r ≈ 0.74 reproduction at GTDB scale | 2/3/4 | **✗ NOT REPRODUCED** | r=0.10–0.29 (n=18,989) | n/a | NB17 architectural concordance r=0.67 (qualitative result holds) | n/a | n/a | [src: gene_function_ecological_agora]

From the report [[summaries/gene_function_ecological_agora__REPORT]].

## Caveat

The report proposes substrate-scale heterogeneity, tree-aware versus paralog-count operationalization, and tree-rank granularity as reasons the point estimate did not survive scaling from 207 to 18,989 genomes. [src: gene_function_ecological_agora]

> 1. **Alm 2006 r ≈ 0.74 NOT REPRODUCED at full GTDB scale** (P4-D3: r=0.10–0.29). Methodology generalization holds (NB17 architectural concordance r=0.67); point-estimate reproduction does not survive scaling 207 → 18,989 genomes. Three identified mechanisms: substrate-scale heterogeneity, tree-aware vs paralog-count operationalization, tree-rank granularity. [src: gene_function_ecological_agora]

## Other caveats in this report

- Bacteroidota PUL Innovator-Exchange was a qualified pass: deep-rank absolute-zero was falsified, but Sankoff recovered the direction. Reported values include d=0.15, gut/rumen enrichment 1.40× at p<10⁻³⁵, phenotype n=577, and LC=0.41. [src: gene_function_ecological_agora]
- The regulatory-versus-metabolic d≥0.3 hypothesis was reframed as a small effect (consumer d=−0.21); regulatory MGE was 4.13% versus metabolic MGE 0.37%. [src: gene_function_ecological_agora]
- Leaf consistency narrows the mycolic-acid finding to Mycobacteriaceae sub-clades; family-rank d=0.31 is described as a population-mixture average. [src: gene_function_ecological_agora]
- PSII classification depends on rank: genus n=2,350 d=0.08 stable, class n=21 d=1.50 Innovator-Exchange, and phylum d=1.60 Innovator-Isolated. The genus null is described as expected; the phylum reversal is attributed to insufficient reference consumer data. [src: gene_function_ecological_agora]
- M26 donor inference remains exploratory; full DTL reconciliation cross-validation is future work. [src: gene_function_ecological_agora]
