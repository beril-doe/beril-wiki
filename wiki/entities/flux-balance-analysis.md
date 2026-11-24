---
type: "Method"
description: "Constraint-based in-silico prediction of metabolic gene requirement from a genome-scale model."
sources: ["summaries/acinetobacter_adp1_explorer__REPORT.md", "summaries/adp1_triple_essentiality__REPORT.md", "summaries/annotation_gap_discovery__REPORT.md", "summaries/respiratory_chain_wiring__REPORT.md"]
aliases: ["FBA"]
---
# flux balance analysis

This page covers flux balance analysis (FBA), the constraint-based in-silico prediction of metabolic gene requirement from a genome-scale model. In ADP1, FBA agreed with TnSeq (transposon sequencing) essentiality for 639 of 866 genes (73.8%). [src: acinetobacter_adp1_explorer] Across 574 organism-carbon source combinations, baseline FBA was overly permissive. [src: annotation_gap_discovery] In ADP1 it also missed condition-specific respiratory requirements. [src: respiratory_chain_wiring] See [[concepts/concordance-of-genome-scale-metabolic-model-predictions-with-experimental-data]] and [[concepts/systematic-blind-spots-of-flux-balance-models-for-condition-specific-requirements]].

## Key facts

- The ADP1 triple-essentiality report defines FBA as measuring metabolic necessity: whether flux through a gene is required for growth in defined media. [src: adp1_triple_essentiality]
- It describes FBA output as binary (essential/dispensable) and as a first-pass computational screen. [src: adp1_triple_essentiality]
- The original ADP1 analysis uses essential, variable or blocked predictions from a ModelSEED metabolic model in minimal media. [src: adp1_triple_essentiality]
- Per-condition FBA flux comes from the `gene_phenotypes` table for 6 matched carbon sources. [src: adp1_triple_essentiality]
- The refined study uses a binary essential versus non-essential classification from ModelSEED predictions. [src: adp1_triple_essentiality]
- It classifies 866 genes in rich media and 866 genes in minimal media. [src: adp1_triple_essentiality]
- FBA-blocked genes have zero predicted flux (n=196). [src: adp1_triple_essentiality]

## Agreement with experiment

In ADP1, 639 of 866 genes (73.8%) with both FBA flux predictions and TnSeq essentiality calls are concordant. [src: acinetobacter_adp1_explorer] Separately, the same report finds that 20% of genes (177/866) change FBA flux class between rich and minimal media, which it reads as condition-dependent metabolic rewiring. [src: acinetobacter_adp1_explorer] See [[summaries/acinetobacter_adp1_explorer__REPORT]] and [[summaries/adp1_triple_essentiality__REPORT]].

## Growth prediction across organisms

Baseline FBA across 574 organism-carbon source combinations had 42.5% overall accuracy. [src: annotation_gap_discovery] Recall was 86.5%, with 244 of 282 growth-positive conditions correctly predicted. [src: annotation_gap_discovery] Precision was only 42.5%, with 244 of 574 growth predictions correct. The report attributes the 330 false positives to overly permissive draft models. [src: annotation_gap_discovery] It notes that draft models built from automated RAST annotations contain systematic errors. [src: annotation_gap_discovery]

The same report's gene-knockout simulation showed zero wildtype growth on minimal carbon source media. This was expected, because the models need the gapfilled reactions themselves to grow on those carbon sources. [src: annotation_gap_discovery] The knockout validation was therefore inconclusive and circular in this context. [src: annotation_gap_discovery] See [[summaries/annotation_gap_discovery__REPORT]].

## Limits for respiratory requirements

The ADP1 FBA model predicts zero flux through NDH-2 on all standard carbon sources and routes all NADH (reduced nicotinamide adenine dinucleotide) through Complex I. [src: respiratory_chain_wiring] It also predicts zero flux through ACIAD3522 on all standard media. The report explains this by growth-rate optimization favoring Complex I, which yields more ATP (adenosine triphosphate) per NADH. [src: respiratory_chain_wiring] The report calls this the fundamental reason FBA fails to predict condition-specific respiratory requirements. FBA assumes the optimal pathway is always used and misses capacity constraints that force suboptimal pathways at high flux. [src: respiratory_chain_wiring] See [[entities/alternative-nadh-dehydrogenase-ndh-2]] and [[summaries/respiratory_chain_wiring__REPORT]].
