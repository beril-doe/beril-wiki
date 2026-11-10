---
type: "Finding"
description: "Cohen's d was 0.146 at UniRef50 resolution (NB08c, positive versus all housekeeping controls) and 0.665\u20133.558 at KO level (NB09c, best pairs against the tRNA-synthetase and RNAP-core housekeeping controls), which the report describes as a 4\u201325\u00d7 amplification depending on positive class; the M18 gate passed."
finding_id: "gene_function_ecological_agora--c2291337"
result: "observation"
source: "gene_function_ecological_agora"
quantities: [{"value": "0.146", "what": "UniRef50 baseline Cohen's d (positive vs all housekeeping)", "unit": "d", "denominator": "", "scope": "NB08c"}, {"value": "0.665\u20133.558", "what": "KO-level Cohen's d, best pairs", "unit": "d", "denominator": "", "scope": "NB09c, tRNA-synthetase and RNAP-core controls"}, {"value": "4\u201325\u00d7", "what": "amplification depending on positive class, as described by the report", "unit": "fold", "denominator": "", "scope": ""}]
caveat: "The change from d=0.146 to d=0.665+ was interpreted as potentially reflecting measurement-grain correction rather than aggregation itself, and the theoretical explanation remained incomplete."
first_added: "2026-11-09"
source_hash: "ec22f37a485c95d0e067c1984020af5580f9f103cae1582742ed63f035a74a69"
---
# Horizontal-transfer effect size is larger at KO level than at UniRef50 level

Cohen's d was 0.146 at UniRef50 resolution (NB08c, positive versus all housekeeping controls) and 0.665–3.558 at KO level (NB09c, best pairs against the tRNA-synthetase and RNAP-core housekeeping controls), which the report describes as a 4–25× amplification depending on positive class; the M18 gate passed. [src: gene_function_ecological_agora]

## Key figures

- **0.146 d**: UniRef50 baseline Cohen's d (positive vs all housekeeping) (scope NB08c) [src: gene_function_ecological_agora]
- **0.665–3.558 d**: KO-level Cohen's d, best pairs (scope NB09c, tRNA-synthetase and RNAP-core controls) [src: gene_function_ecological_agora]
- **4–25× fold**: amplification depending on positive class, as described by the report [src: gene_function_ecological_agora]

## Evidence

> **M18 PASS on the cleanest housekeeping (tRNA-synth + RNAP core).** Cohen's d amplifies from 0.146 (UniRef50 NB08c, pos vs all housekeeping) to 0.665–3.558 (KO NB09c, best pairs) — a **4–25× amplification depending on positive class**. The substrate-hierarchy claim survives at KO resolution. [src: gene_function_ecological_agora]

From the report [[summaries/gene_function_ecological_agora__REPORT]].

## Caveat

The change from d=0.146 to d=0.665+ was interpreted as potentially reflecting measurement-grain correction rather than aggregation itself, and the theoretical explanation remained incomplete. [src: gene_function_ecological_agora]

> The KO aggregation amplification (d=0.146 → 0.665+) is empirically observed; M14 close-reading reframed it as "Alm 2006 worked at single-domain level (UniRef50-comparable), so amplification is metric correction not aggregation per se" but a clearer theoretical framing in REPORT would help Phase 3 interpretation. [src: gene_function_ecological_agora]

## Other caveats in this report

- Bacteroidota PUL Innovator-Exchange was a qualified pass: deep-rank absolute-zero was falsified, but Sankoff recovered the direction. Reported values include d=0.15, gut/rumen enrichment 1.40× at p<10⁻³⁵, phenotype n=577, and LC=0.41. [src: gene_function_ecological_agora]
- The regulatory-versus-metabolic d≥0.3 hypothesis was reframed as a small effect (consumer d=−0.21); regulatory MGE was 4.13% versus metabolic MGE 0.37%. [src: gene_function_ecological_agora]
- Leaf consistency narrows the mycolic-acid finding to Mycobacteriaceae sub-clades; family-rank d=0.31 is described as a population-mixture average. [src: gene_function_ecological_agora]
- The report proposes substrate-scale heterogeneity, tree-aware versus paralog-count operationalization, and tree-rank granularity as reasons Alm's point estimate did not survive scaling from 207 to 18,989 genomes. [src: gene_function_ecological_agora]
- PSII classification depends on rank: genus n=2,350 d=0.08 stable, class n=21 d=1.50 Innovator-Exchange, and phylum d=1.60 Innovator-Isolated. The genus null is described as expected; the phylum reversal is attributed to insufficient reference consumer data. [src: gene_function_ecological_agora]
