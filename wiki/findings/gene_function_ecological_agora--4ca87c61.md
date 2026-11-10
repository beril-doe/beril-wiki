---
type: "Finding"
description: "PSII Innovator-Exchange was supported at class rank in Cyanobacteria, with producer d=+1.50, consumer d=+0.70, 2.77\u00d7 photic-aquatic enrichment at p<10\u207b\u2075\u00b2, and LC=0.88."
finding_id: "gene_function_ecological_agora--4ca87c61"
result: "observation"
source: "gene_function_ecological_agora"
quantities: [{"value": "+1.50", "what": "producer Cohen's d", "unit": "d", "denominator": "", "scope": "Cyanobacteriia class rank, PSII"}, {"value": "+0.70", "what": "consumer Cohen's d", "unit": "d", "denominator": "", "scope": "Cyanobacteriia class rank, PSII"}, {"value": "2.77\u00d7", "what": "photic aquatic biome enrichment", "unit": "fold", "denominator": "", "scope": "p<10\u207b\u2075\u00b2"}, {"value": "0.88", "what": "leaf consistency (LC)", "unit": "", "denominator": "", "scope": "4.4\u00d7 atlas"}]
caveat: "Classification depends on rank: genus (n=2,350, d=0.08) is stable, class (n=21, d=1.50) is Innovator-Exchange, and phylum (d=1.60) is Innovator-Isolated, with the phylum reversal attributed to insufficient reference consumer data."
first_added: "2026-11-09"
source_hash: "ec22f37a485c95d0e067c1984020af5580f9f103cae1582742ed63f035a74a69"
---
# Photosystem II innovation is exchange-type, but only at Cyanobacteriia class rank

PSII Innovator-Exchange was supported at class rank in Cyanobacteria, with producer d=+1.50, consumer d=+0.70, 2.77× photic-aquatic enrichment at p<10⁻⁵², and LC=0.88. [src: gene_function_ecological_agora]

## Key figures

- **+1.50 d**: producer Cohen's d (scope Cyanobacteriia class rank, PSII) [src: gene_function_ecological_agora]
- **+0.70 d**: consumer Cohen's d (scope Cyanobacteriia class rank, PSII) [src: gene_function_ecological_agora]
- **2.77× fold**: photic aquatic biome enrichment (scope p<10⁻⁵²) [src: gene_function_ecological_agora]
- **0.88**: leaf consistency (LC) (scope 4.4× atlas) [src: gene_function_ecological_agora]

## Evidence

> | H3 | Cyanobacteria → Innovator-Exchange on PSII | 3 | **✅ SUPPORTED at class rank** | producer d=+1.50, consumer d=+0.70 (NB16) | 2.77× photic aquatic p<10⁻⁵² (NB23) | BacDive thin (n=4); env-cluster 0 marine 35.6% (NB25) | 0% MGE-machinery (NB26c); 10.91% gene-neighborhood ≈ baseline 10.6% (NB26g) | **LC=0.88 (4.4× atlas) — canonical class-defining innovation**, validates Cardona 2018 framing | [src: gene_function_ecological_agora]

From the report [[summaries/gene_function_ecological_agora__REPORT]].

## Caveat

Classification depends on rank: genus (n=2,350, d=0.08) is stable, class (n=21, d=1.50) is Innovator-Exchange, and phylum (d=1.60) is Innovator-Isolated, with the phylum reversal attributed to insufficient reference consumer data. [src: gene_function_ecological_agora]

> 2. **PSII rank-dependence**: genus n=2,350 d=0.08 STABLE → class n=21 d=1.50 INNOVATOR-EXCHANGE → phylum d=1.60 INNOVATOR-ISOLATED. Class rank is biologically appropriate per Cardona 2018 (PSII evolved before Cyanobacteria diversification); genus null is *expected* under that framing. Phylum reversal is a substrate artifact (insufficient ref consumer data). [src: gene_function_ecological_agora]

## Other caveats in this report

- Bacteroidota PUL Innovator-Exchange was a qualified pass: deep-rank absolute-zero was falsified, but Sankoff recovered the direction. Reported values include d=0.15, gut/rumen enrichment 1.40× at p<10⁻³⁵, phenotype n=577, and LC=0.41. [src: gene_function_ecological_agora]
- The regulatory-versus-metabolic d≥0.3 hypothesis was reframed as a small effect (consumer d=−0.21); regulatory MGE was 4.13% versus metabolic MGE 0.37%. [src: gene_function_ecological_agora]
- Leaf consistency narrows the mycolic-acid finding to Mycobacteriaceae sub-clades; family-rank d=0.31 is described as a population-mixture average. [src: gene_function_ecological_agora]
- The report proposes substrate-scale heterogeneity, tree-aware versus paralog-count operationalization, and tree-rank granularity as reasons Alm's point estimate did not survive scaling from 207 to 18,989 genomes. [src: gene_function_ecological_agora]
- M26 donor inference remains exploratory; full DTL reconciliation cross-validation is future work. [src: gene_function_ecological_agora]
