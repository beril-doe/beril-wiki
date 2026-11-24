---
type: "Concept"
description: "Whether pangenome core/accessory status relates to FBA-experiment discordance; stops at ADP1 evidence."
sources: ["summaries/acinetobacter_adp1_explorer__REPORT.md", "summaries/adp1_triple_essentiality__REPORT.md"]
---
# Pangenome conservation of metabolic-model discordant genes

This page covers pangenome conservation of metabolic-model discordant genes. In Acinetobacter baylyi ADP1, the only organism examined, pangenome status was not significantly enriched in genes where the model and the experiment disagree (odds ratio (OR) = 0.89, p = 0.80). [src: adp1_triple_essentiality] See [[concepts/concordance-of-genome-scale-metabolic-model-predictions-with-experimental-data]] for the broader topic.

## ADP1 evidence

Pangenome status in Acinetobacter baylyi ADP1 was overwhelmingly core across all concordance classes, at 93–100%. [src: adp1_triple_essentiality] Discordant genes showed no significant enrichment for pangenome status (Fisher OR = 0.89, p = 0.80). [src: adp1_triple_essentiality] This is a null result from a single strain. It does not show that no relationship exists. Details are in [[summaries/adp1_triple_essentiality__REPORT]].

The [[summaries/acinetobacter_adp1_explorer__REPORT]] analysis found 227 genes with discordant flux balance analysis (FBA) and transposon sequencing (TnSeq) essentiality calls. It proposes testing them for pathway or regulatory-function enrichment to guide model refinement. [src: acinetobacter_adp1_explorer]

## Proposed extension

The ADP1 report proposes expanding the FBA-growth analysis to other Acinetobacter species across the pangenome. It would compare species with different aromatic degradation capabilities and distinguish species-specific from universal patterns. [src: adp1_triple_essentiality]

## Open Directions

- Test the 227 discordant genes for pathway and regulatory-function enrichment. This would show whether discordance follows function even though no pangenome enrichment was detected.
- Run the multi-species extension. ADP1 genes are almost all core, so species with more accessory genes would test the null better.
