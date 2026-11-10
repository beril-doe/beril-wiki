---
type: "Finding"
description: "KOs annotated to both regulatory and metabolic pathways show 2\u00d7 the Innovator-Exchange rate (0.57%) of pure regulatory (0.27%) or pure metabolic (0.28%) KOs."
finding_id: "gene_function_ecological_agora--e172b656"
result: "observation"
source: "gene_function_ecological_agora"
quantities: [{"value": "0.57%", "what": "Innovator-Exchange rate of mixed-category KOs", "unit": "%", "denominator": "", "scope": "mixed regulatory-and-metabolic KOs"}, {"value": "0.27%", "what": "Innovator-Exchange rate of pure regulatory KOs", "unit": "%", "denominator": "", "scope": "pure regulatory KOs"}, {"value": "0.28%", "what": "Innovator-Exchange rate of pure metabolic KOs", "unit": "%", "denominator": "", "scope": "pure metabolic KOs"}, {"value": "2\u00d7", "what": "Fold difference of mixed versus pure categories", "unit": "fold", "denominator": "", "scope": ""}]
caveat: "The report cautions that differences across KO categories are small, and that the ancient-skewed 'other' category may partly reflect accidental PROKKA-to-eggNOG mapping."
first_added: "2026-11-09"
source_hash: "ec22f37a485c95d0e067c1984020af5580f9f103cae1582742ed63f035a74a69"
---
# Mixed regulatory-and-metabolic KOs show the highest Innovator-Exchange rate

KOs annotated to both regulatory and metabolic pathways show 2× the Innovator-Exchange rate (0.57%) of pure regulatory (0.27%) or pure metabolic (0.28%) KOs. [src: gene_function_ecological_agora]

## Key figures

- **0.57%**: Innovator-Exchange rate of mixed-category KOs (scope mixed regulatory-and-metabolic KOs) [src: gene_function_ecological_agora]
- **0.27%**: Innovator-Exchange rate of pure regulatory KOs (scope pure regulatory KOs) [src: gene_function_ecological_agora]
- **0.28%**: Innovator-Exchange rate of pure metabolic KOs (scope pure metabolic KOs) [src: gene_function_ecological_agora]
- **2× fold**: Fold difference of mixed versus pure categories [src: gene_function_ecological_agora]

## Evidence

> 3. **The mixed category is the most exchange-active**, not regulatory or metabolic alone. KOs participating in both regulatory and metabolic pathways show 2× the Innovator-Exchange rate (0.57%) of pure regulatory (0.27%) or pure metabolic (0.28%). This is genuinely novel — *the asymmetry that exists in the atlas is between pathway-overlap and pathway-pure KOs, not between regulatory and metabolic per se*. [src: gene_function_ecological_agora]

From the report [[summaries/gene_function_ecological_agora__REPORT]].

## Caveat

The report cautions that differences across KO categories are small, and that the ancient-skewed 'other' category may partly reflect accidental PROKKA-to-eggNOG mapping. [src: gene_function_ecological_agora]

> Differences across categories are small. The "other" category (off-target pathways: ko04xxx organismal systems, ko05xxx human diseases) has the most ancient-skewed profile, consistent with these being mostly evolutionarily-older or eukaryotic-derived annotations that pass through PROKKA → eggNOG mapping accidentally. [src: gene_function_ecological_agora]

## Other caveats in this report

- Bacteroidota PUL Innovator-Exchange was a qualified pass: deep-rank absolute-zero was falsified, but Sankoff recovered the direction. Reported values include d=0.15, gut/rumen enrichment 1.40× at p<10⁻³⁵, phenotype n=577, and LC=0.41. [src: gene_function_ecological_agora]
- The regulatory-versus-metabolic d≥0.3 hypothesis was reframed as a small effect (consumer d=−0.21); regulatory MGE was 4.13% versus metabolic MGE 0.37%. [src: gene_function_ecological_agora]
- Leaf consistency narrows the mycolic-acid finding to Mycobacteriaceae sub-clades; family-rank d=0.31 is described as a population-mixture average. [src: gene_function_ecological_agora]
- The report proposes substrate-scale heterogeneity, tree-aware versus paralog-count operationalization, and tree-rank granularity as reasons Alm's point estimate did not survive scaling from 207 to 18,989 genomes. [src: gene_function_ecological_agora]
- PSII classification depends on rank: genus n=2,350 d=0.08 stable, class n=21 d=1.50 Innovator-Exchange, and phylum d=1.60 Innovator-Isolated. The genus null is described as expected; the phylum reversal is attributed to insufficient reference consumer data. [src: gene_function_ecological_agora]
