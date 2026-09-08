---
type: Gene_Or_Pathway
description: Envelope lipid A pathway examined in Caulobacter lipid A-loss rescue
sources:
- id: caulobacter_fur_lipida_loss
  resource: ../summaries/caulobacter_fur_lipida_loss__REPORT.md
  title: caulobacter fur lipida loss
title: Lipid A biosynthesis
---
# Lipid A biosynthesis

## What this entity is

**Canonical name:** Lipid A biosynthesis pathway.  
**Known aliases:** lipid A pathway; lipid A biosynthetic pathway. [^caulobacter_fur_lipida_loss]  
**Stable external identifier:** No stable pathway identifier was reported in this document. [^caulobacter_fur_lipida_loss]

Lipid A biosynthesis is the envelope pathway disrupted by deletion of [lpxc](lpxc.md) and examined in [caulobacter-crescentus](caulobacter-crescentus.md) as part of the mechanism allowing Δ*fur* Δ*sspB* cells to tolerate Δ*lpxc*. [^caulobacter_fur_lipida_loss]

## Evidence from the document

The comparative analysis tested the Caulobacter lipid A genes LpxA, LpxC, LpxD, LpxB, and LpxK with PaperBLAST and NCBI annotation. [^caulobacter_fur_lipida_loss]

PaperBLAST returned 0 hits for LpxA versus 11 NCBI hits, 0 versus 15 for LpxC, 0 versus 15 for LpxD, 1 versus 18 for LpxB, and 0 versus 18 for LpxK. [^caulobacter_fur_lipida_loss]

The report characterizes these results as an approximately 80% false-negative rate for the tested Caulobacter lipid A genes, attributing the discrepancy to naming-convention and homology-search limitations. [^caulobacter_fur_lipida_loss]

NCBI annotation confirmed that the tested comparator species—[acinetobacter-baumannii](acinetobacter-baumannii.md), [neisseria-meningitidis](neisseria-meningitidis.md), and [moraxella-catarrhalis](moraxella-catarrhalis.md)—were analyzed alongside [caulobacter-crescentus](caulobacter-crescentus.md) for lipid A-related alternatives. [^caulobacter_fur_lipida_loss]

The alternative lipid A-loss routes identified in the comparison were species-specific: *A. baumannii* had PBP1A and Ld-transpeptidases, *N. meningitidis* had 9 capsule-biosynthesis PaperBLAST hits, and *A. baumannii* and *N. meningitidis* had late acyltransferase *lpxX/lpxL* hits numbering 8 and 3, respectively. [^caulobacter_fur_lipida_loss]

The report states that Caulobacter lacked these identified alternatives and instead used its sphingolipid substitution route, linking lipid A loss to [sphingolipid-biosynthesis](sphingolipid-biosynthesis.md). [^caulobacter_fur_lipida_loss]

The lipid A-loss analysis found no canonical Lpt component that was transcriptionally DOWN in the tested contrast; the MsbA-like CCNA_00307 was UP by +0.89 with FDR 0.01, and LptC-related CCNA_03716 was UP by +0.56 with FDR 0.005. [^caulobacter_fur_lipida_loss]

In the single-replicate outer-membrane proteome, LptD changed by log2(4672/4659) = -0.47 and by log2(4672/4580) = -0.62, while LptE changed by -0.78 and -0.68, respectively. [^caulobacter_fur_lipida_loss]

These transcript–protein differences support integration with [multi-omics-integration](../concepts/multi-omics-integration.md), but the single-replicate proteome does not establish statistical significance for the protein-level changes. [^caulobacter_fur_lipida_loss]

## Related pages

- [lpxc](lpxc.md) — lipid A biosynthesis gene whose deletion is central to the Caulobacter rescue analysis. [^caulobacter_fur_lipida_loss]
- [sphingolipid-biosynthesis](sphingolipid-biosynthesis.md) — alternative envelope lipid pathway implicated in Caulobacter lipid A-loss tolerance. [^caulobacter_fur_lipida_loss]
- [multi-omics-integration](../concepts/multi-omics-integration.md) — integrates lipid A-pathway transcript, proteome, fitness, and comparative-annotation evidence. [^caulobacter_fur_lipida_loss]
- [gene-essentiality](../concepts/gene-essentiality.md) — frames the viability and genetic requirements associated with Δ*lpxc*. [^caulobacter_fur_lipida_loss]
- [caulobacter_fur_lipida_loss__REPORT](../summaries/caulobacter_fur_lipida_loss__REPORT.md) — source-project summary. [^caulobacter_fur_lipida_loss]

[^caulobacter_fur_lipida_loss]: [caulobacter fur lipida loss](../summaries/caulobacter_fur_lipida_loss__REPORT.md)
