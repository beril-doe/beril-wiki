---
type: Organism
description: Moraxella catarrhalis comparator in Caulobacter lipid A-loss analysis
sources:
- id: caulobacter_fur_lipida_loss
  resource: ../summaries/caulobacter_fur_lipida_loss__REPORT.md
  title: caulobacter fur lipida loss
title: Moraxella catarrhalis
---
# Moraxella catarrhalis

## Identity

**Canonical name:** *Moraxella catarrhalis*.[^caulobacter_fur_lipida_loss]

**Known alias:** *M. catarrhalis*.[^caulobacter_fur_lipida_loss]

**Stable external identifier:** No NCBI Taxonomy ID or other stable external identifier was reported in the source.[^caulobacter_fur_lipida_loss]

## Role in the comparative analysis

*Moraxella catarrhalis* was one of four species compared with *Caulobacter crescentus*, *Acinetobacter baumannii*, and *Neisseria meningitidis* in the cross-species annotation analysis of lipid A-loss alternatives and regulatory pathways.[^caulobacter_fur_lipida_loss]

NCBI annotation showed that *spt* and *cerR* were Caulobacter-unique across the four-species comparison, with pattern 1000, indicating that *M. catarrhalis* lacked the Caulobacter sphingolipid substitute pathway represented by these genes.[^caulobacter_fur_lipida_loss]

NCBI annotation likewise showed that *chvG* and *chvI* were Caulobacter-restricted across the tested species, with pattern 1000, indicating that *M. catarrhalis* lacked the Caulobacter ChvG-ChvI regulatory circuit.[^caulobacter_fur_lipida_loss]

The source described *M. catarrhalis* as under-annotated in PaperBLAST, with 162 genes total, making PaperBLAST-based absence calls for this species vulnerable to false negatives.[^caulobacter_fur_lipida_loss]

The comparison therefore supports treating the absence of Caulobacter sphingolipid-substitution and ChvG-ChvI systems in *M. catarrhalis* as an annotation-supported comparative result, while deeper Pfam HMM searches against named RefSeq proteomes remain necessary to detect unannotated paralogs.[^caulobacter_fur_lipida_loss]

## Related evidence

This species is discussed in [caulobacter_fur_lipida_loss__REPORT](../summaries/caulobacter_fur_lipida_loss__REPORT.md), which integrates comparative annotation with transcriptomics, proteomics, regulon evidence, and RB-TnSeq fitness data.[^caulobacter_fur_lipida_loss]

The comparative annotation workflow used [kescience-paperblast](kescience-paperblast.md) and contributes to [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md).[^caulobacter_fur_lipida_loss]

[^caulobacter_fur_lipida_loss]: [caulobacter fur lipida loss](../summaries/caulobacter_fur_lipida_loss__REPORT.md)
