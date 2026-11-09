---
type: "Finding"
description: "After leaf-consistency heterogeneity was found, the supported claim was refined to the mycolate-producing sub-clade of Mycobacteriaceae (10 of 13 genera; producer d=0.39 at genus rank), with the consumer-side Innovator-Isolated component weaker than the original family-rank framing implied."
finding_id: "gene_function_ecological_agora--a4ce9393"
result: "correction"
source: "gene_function_ecological_agora"
quantities: [{"value": "10 of 13", "what": "genera in the mycolic-positive sub-clade", "unit": "genera", "denominator": "13 Mycobacteriaceae genera", "scope": ""}, {"value": "0.39", "what": "producer Cohen's d in the sub-clade", "unit": "d", "denominator": "", "scope": "genus rank"}]
caveat: "g__Mycobacterium itself sat in the mycolic-low sub-clade (mean LC=0.36, median 0.08), which the report attributes to an 11-KO panel calibrated to M. tuberculosis-complex-style mycolate biosynthesis."
first_added: "2026-11-09"
source_hash: "ec22f37a485c95d0e067c1984020af5580f9f103cae1582742ed63f035a74a69"
---
# Mycolic-acid Innovator-Isolated claim narrows to a sub-clade of Mycobacteriaceae

After leaf-consistency heterogeneity was found, the supported claim was refined to the mycolate-producing sub-clade of Mycobacteriaceae (10 of 13 genera; producer d=0.39 at genus rank), with the consumer-side Innovator-Isolated component weaker than the original family-rank framing implied. [src: gene_function_ecological_agora]

## Key figures

- **10 of 13 genera**: genera in the mycolic-positive sub-clade (denominator 13 Mycobacteriaceae genera) [src: gene_function_ecological_agora]
- **0.39 d**: producer Cohen's d in the sub-clade (scope genus rank) [src: gene_function_ecological_agora]

## Evidence

> 3. **Refined supported claim**: "the mycolate-producing sub-clade of Mycobacteriaceae (10 of 13 genera) is mycolic-acid Innovator-Isolated, producer d=0.39 at genus rank." More precisely targeted than the family-rank framing; the consumer-side Innovator-Isolated component is weaker than the original family-rank framing implied. [src: gene_function_ecological_agora]

From the report [[summaries/gene_function_ecological_agora__REPORT]].

## Caveat

g__Mycobacterium itself sat in the mycolic-low sub-clade (mean LC=0.36, median 0.08), which the report attributes to an 11-KO panel calibrated to M. tuberculosis-complex-style mycolate biosynthesis. [src: gene_function_ecological_agora]

> **Surprising finding**: g__Mycobacterium itself sits in the mycolic-low sub-clade (mean LC=0.36, median 0.08). Reason: the project's 11-KO mycolic panel is calibrated to long-chain Mycobacterium-style mycolate biosynthesis, but only the M. tuberculosis complex carries ALL panel KOs at high prevalence; many environmental Mycobacterium species don't. The mycolic-positive sub-clade is the broader Mycobacteriales/Corynebacteriales lineages that uniformly carry the panel. [src: gene_function_ecological_agora]

## Other caveats in this report

- Bacteroidota PUL Innovator-Exchange was a qualified pass: deep-rank absolute-zero was falsified, but Sankoff recovered the direction. Reported values include d=0.15, gut/rumen enrichment 1.40× at p<10⁻³⁵, phenotype n=577, and LC=0.41. [src: gene_function_ecological_agora]
- The regulatory-versus-metabolic d≥0.3 hypothesis was reframed as a small effect (consumer d=−0.21); regulatory MGE was 4.13% versus metabolic MGE 0.37%. [src: gene_function_ecological_agora]
- Leaf consistency narrows the mycolic-acid finding to Mycobacteriaceae sub-clades; family-rank d=0.31 is described as a population-mixture average. [src: gene_function_ecological_agora]
- The report proposes substrate-scale heterogeneity, tree-aware versus paralog-count operationalization, and tree-rank granularity as reasons Alm's point estimate did not survive scaling from 207 to 18,989 genomes. [src: gene_function_ecological_agora]
- PSII classification depends on rank: genus n=2,350 d=0.08 stable, class n=21 d=1.50 Innovator-Exchange, and phylum d=1.60 Innovator-Isolated. The genus null is described as expected; the phylum reversal is attributed to insufficient reference consumer data. [src: gene_function_ecological_agora]
