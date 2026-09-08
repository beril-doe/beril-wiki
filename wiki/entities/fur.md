---
type: Gene_Or_Pathway
description: Iron-responsive regulator linked to Caulobacter transport and respiratory
  changes
sources:
- id: caulobacter_fur_lipida_loss
  resource: ../summaries/caulobacter_fur_lipida_loss__REPORT.md
  title: caulobacter fur lipida loss
title: Fur
---
# Fur

## What this entity is

Fur is the iron-responsive regulator in *Caulobacter crescentus* whose derepression is associated with transport, iron-uptake, and respiratory transcriptional changes. [^caulobacter_fur_lipida_loss]

- **Canonical name:** Fur. [^caulobacter_fur_lipida_loss]
- **Known aliases:** No additional aliases were specified in this document. [^caulobacter_fur_lipida_loss]
- **Stable external identifier:** No stable external identifier was reported in this document. [^caulobacter_fur_lipida_loss]

## Evidence from caulobacter_fur_lipida_loss

The 4584-vs-4580 contrast, comparing Δ*fur* Δ*sspB* Δ*rsaA* with Δ*rsaA*, correlated with Leaden 2018’s Δ*fur* signal across 93 differentially expressed genes, with Spearman ρ = 0.315, p = 2.08e-03, and 71% sign concordance. [^caulobacter_fur_lipida_loss]

Of those 93 genes, 53 were buffered in the present data, showing logFC approximately 0 despite Leaden values of -5 to -9. [^caulobacter_fur_lipida_loss]

The buffered set was dominated by the cbb3 / cyd / *fix*-NOPQ micro-aerobic respiratory operon, including CCNA_01466-01476, *ccoNOPQ*, *cydCDA*, and *fixG/H/I*. [^caulobacter_fur_lipida_loss]

These results statistically support Fur derepression, but the mechanistic importance of the Δ*sspB*-buffered respiratory program for Δ*lpxc* rescue remains a hypothesis. [^caulobacter_fur_lipida_loss]

Fur-derepressed transport and iron-uptake targets included ChvT (CCNA_03108), CCNA_02910, CCNA_00210, CCNA_02048, and CCNA_00028. [^caulobacter_fur_lipida_loss]

ChvT had envelope-stress |*t*| = 43.7, while the other listed Fur-derepressed TBDTs had envelope-stress |*t*| values of 9-28. [^caulobacter_fur_lipida_loss]

The Caulobacter RB-TnSeq fitness compendium contained 198 experiments, including 22 envelope-stress experiments and zero iron-limitation experiments. [^caulobacter_fur_lipida_loss]

The genome-wide envelope-stress background contained 1311 phenotype-bearing genes among 3943 genes, or 33.25%. [^caulobacter_fur_lipida_loss]

Path A, the 32-gene concordant-strong Fur signature, contained 17 phenotype-bearing genes, or 53.1%, corresponding to 1.60× enrichment with hypergeometric p = 0.016. [^caulobacter_fur_lipida_loss]

Path B, the 26-gene SspB-buffered set, contained 9 phenotype-bearing genes, or 34.6%, corresponding to 1.04× enrichment with p = 0.515, making it indistinguishable from the genome background. [^caulobacter_fur_lipida_loss]

The lower Path B enrichment does not establish that the buffered respiratory program is required for envelope remodeling, whereas the Path A result provides condition-specific fitness support for the strong Fur signature. [^caulobacter_fur_lipida_loss]

## Related evidence and pages

This entity is linked to [condition-specific-fitness](../concepts/condition-specific-fitness.md), where the background-calibrated RB-TnSeq results distinguish the supported Path A enrichment from the unsupported Path B respiratory hypothesis. [^caulobacter_fur_lipida_loss]

It also contributes to [gene-essentiality](../concepts/gene-essentiality.md) because Fur-released and peptidoglycan-remodeling gene sets were tested for condition-specific fitness phenotypes associated with Δ*lpxc* viability. [^caulobacter_fur_lipida_loss]

The transcript, proteomic, fitness, regulon, and comparative-annotation evidence contributes to [multi-omics-integration](../concepts/multi-omics-integration.md). [^caulobacter_fur_lipida_loss]

The fitness evidence was bridged through [kescience-fitnessbrowser](kescience-fitnessbrowser.md), and the organismal context is [caulobacter-crescentus](caulobacter-crescentus.md). [^caulobacter_fur_lipida_loss]

The complete project report is summarized at [caulobacter_fur_lipida_loss__REPORT](../summaries/caulobacter_fur_lipida_loss__REPORT.md). [^caulobacter_fur_lipida_loss]

[^caulobacter_fur_lipida_loss]: [caulobacter fur lipida loss](../summaries/caulobacter_fur_lipida_loss__REPORT.md)
