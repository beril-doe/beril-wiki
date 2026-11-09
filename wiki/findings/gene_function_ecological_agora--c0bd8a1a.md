---
type: "Finding"
description: "Across six functional classes, the genus-level (recent) gain percentage ranged from 24.7 for strict tRNA synthetases to 58.7 for CRISPR-Cas, while the ancient (phylum-or-above) gain percentage was 10.7 for tRNA synthetases and 2.4 for CRISPR-Cas."
finding_id: "gene_function_ecological_agora--c0bd8a1a"
result: "observation"
source: "gene_function_ecological_agora"
quantities: [{"value": "58.7", "what": "recent (genus-level) gain share for pos_crispr_cas", "unit": "%", "denominator": "20,898 total gains", "scope": "CRISPR-Cas"}, {"value": "24.7", "what": "recent (genus-level) gain share for neg_trna_synth_strict", "unit": "%", "denominator": "15,060 total gains", "scope": "strict tRNA synthetases"}, {"value": "10.7", "what": "ancient gain share for neg_trna_synth_strict", "unit": "%", "denominator": "15,060 total gains", "scope": "strict tRNA synthetases"}, {"value": "2.4", "what": "ancient gain share for pos_crispr_cas", "unit": "%", "denominator": "20,898 total gains", "scope": "CRISPR-Cas"}]
caveat: "M22 estimates gain location and depth, not donor\u2013recipient flow; the report cites compositional-signal degradation after ~10\u2013100 Myr and infeasible per-family DTL reconciliation as limits."
first_added: "2026-11-09"
source_hash: "ec22f37a485c95d0e067c1984020af5580f9f103cae1582742ed63f035a74a69"
---
# Function classes have distinct gene-acquisition depth profiles, CRISPR-Cas most recent-skewed

Across six functional classes, the genus-level (recent) gain percentage ranged from 24.7 for strict tRNA synthetases to 58.7 for CRISPR-Cas, while the ancient (phylum-or-above) gain percentage was 10.7 for tRNA synthetases and 2.4 for CRISPR-Cas. [src: gene_function_ecological_agora]

## Key figures

- **58.7 %**: recent (genus-level) gain share for pos_crispr_cas (denominator 20,898 total gains; scope CRISPR-Cas) [src: gene_function_ecological_agora]
- **24.7 %**: recent (genus-level) gain share for neg_trna_synth_strict (denominator 15,060 total gains; scope strict tRNA synthetases) [src: gene_function_ecological_agora]
- **10.7 %**: ancient gain share for neg_trna_synth_strict (denominator 15,060 total gains; scope strict tRNA synthetases) [src: gene_function_ecological_agora]
- **2.4 %**: ancient gain share for pos_crispr_cas (denominator 20,898 total gains; scope CRISPR-Cas) [src: gene_function_ecological_agora]

## Evidence

> | Class | recent% (genus-level gain) | older_recent% | mid% | older% | **ancient% (phylum-or-above)** | total gains | |---|---|---|---|---|---|---| | pos_crispr_cas | **58.7** | 27.6 | 7.0 | 4.3 | **2.4** | 20,898 | | pos_tcs_hk | 45.1 | 32.9 | 10.6 | 7.0 | 4.4 | 518,106 | | pos_betalac | 44.2 | 32.7 | 10.7 | 7.5 | 4.9 | 139,000 | | neg_ribosomal_strict | 38.9 | 33.3 | 12.4 | 9.1 | 6.3 | 79,168 | | neg_rnap_core_strict | 38.5 | 34.2 | 12.2 | 9.0 | 6.0 | 4,086 | | neg_trna_synth_strict | **24.7** | 31.8 | 17.5 | 15.2 | **10.7** | 15,060 | [src: gene_function_ecological_agora]

From the report [[summaries/gene_function_ecological_agora__REPORT]].

## Caveat

M22 estimates gain location and depth, not donor–recipient flow; the report cites compositional-signal degradation after ~10–100 Myr and infeasible per-family DTL reconciliation as limits. [src: gene_function_ecological_agora]

> - **M22 is recipient-and-depth attribution, not donor-recipient flow.** Per the v2.9 DESIGN_NOTES rationale, donor inference at deep ranks is constrained out by codon-amelioration timescales (post-amelioration composition signal degrades for events older than ~10–100 Myr) and by computational scale (per-family DTL reconciliation infeasible at GTDB). M22 reports the rank-LCA of leaves under each gain event — the topological location where the gain landed, not who donated it. [src: gene_function_ecological_agora]

## Other caveats in this report

- Bacteroidota PUL Innovator-Exchange was a qualified pass: deep-rank absolute-zero was falsified, but Sankoff recovered the direction. Reported values include d=0.15, gut/rumen enrichment 1.40× at p<10⁻³⁵, phenotype n=577, and LC=0.41. [src: gene_function_ecological_agora]
- The regulatory-versus-metabolic d≥0.3 hypothesis was reframed as a small effect (consumer d=−0.21); regulatory MGE was 4.13% versus metabolic MGE 0.37%. [src: gene_function_ecological_agora]
- Leaf consistency narrows the mycolic-acid finding to Mycobacteriaceae sub-clades; family-rank d=0.31 is described as a population-mixture average. [src: gene_function_ecological_agora]
- The report proposes substrate-scale heterogeneity, tree-aware versus paralog-count operationalization, and tree-rank granularity as reasons Alm's point estimate did not survive scaling from 207 to 18,989 genomes. [src: gene_function_ecological_agora]
- PSII classification depends on rank: genus n=2,350 d=0.08 stable, class n=21 d=1.50 Innovator-Exchange, and phylum d=1.60 Innovator-Isolated. The genus null is described as expected; the phylum reversal is attributed to insufficient reference consumer data. [src: gene_function_ecological_agora]
