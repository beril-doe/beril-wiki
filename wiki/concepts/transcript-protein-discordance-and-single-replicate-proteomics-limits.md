---
type: "Concept"
description: "How far single-replicate outer-membrane proteome comparisons can be interpreted against transcript data, using Lpt, lptC2, Pal and related proteins; stops at inference limits and replication needs."
sources: ["summaries/caulobacter_fur_lipida_loss__REPORT.md"]
---
# Transcript-protein discordance and single-replicate proteomics limits

This page covers how far a single-replicate outer-membrane proteome can be read against transcript data. All the evidence comes from one report on Caulobacter crescentus, with one proteome per strain and no per-protein statistics, so only the direction of change can be interpreted. [src: caulobacter_fur_lipida_loss] The report treats its transcript-protein discordances as pilot observations that need replication. [src: caulobacter_fur_lipida_loss] For the wider biology, see [[concepts/sphingolipid-and-shared-lpt-transport-in-lipid-a-deficient-bacteria]] and [[summaries/caulobacter_fur_lipida_loss__REPORT]].

## Canonical Lpt proteins: protein disagrees with the shared-component expectation

The two canonical Lpt proteins that were detected, LptD and LptE, decline in the rescued strain. [src: caulobacter_fur_lipida_loss] LptD fell by -0.47 log2 for 4672/4659 and by -0.62 for 4672/4580. [src: caulobacter_fur_lipida_loss] LptE fell by -0.78 and -0.68 on the same two comparisons. [src: caulobacter_fur_lipida_loss] The report says the MsbA-like and LptC-related transcript upregulation fits the Uchendu 2026 shared-component model. It adds that the two Lpt proteins measured directly move the opposite way. [src: caulobacter_fur_lipida_loss] It labels this post-hoc check as discordant with the transcripts and based on a single replicate. [src: caulobacter_fur_lipida_loss]

The data cannot say why. The decline could reflect reduced demand for LPS-specific transport, or it could contradict the shared-component model, and single-replicate proteomics cannot separate the two. [src: caulobacter_fur_lipida_loss] It also cannot show whether the canonical apparatus is functionally maintained, replaced or downregulated in the Δlpxc state. [src: caulobacter_fur_lipida_loss] Replicated proteomics are needed to settle this. [src: caulobacter_fur_lipida_loss]

MsbA-like CCNA_00307 shows a different limit. It was detected only in rescued strain 4672, at abundance 300, and was NaN (not a number) in the other strains. [src: caulobacter_fur_lipida_loss] Its direction relative to wild type therefore cannot be computed. [src: caulobacter_fur_lipida_loss]

## lptC2: protein up while transcript is down

The report states the lptC2 (CCNA_01226) discordance as a transcript change of -0.60 (FDR, false discovery rate, 0.034) against a protein log2(4672/4659) of +1.08. [src: caulobacter_fur_lipida_loss] The size of the protein increase depends on the baseline. lptC2 protein was already down -0.42 log2 in the intermediate strain (4659/4580). Against wild type the net change is therefore +0.66 log2 (≈1.58×), not +1.08. [src: caulobacter_fur_lipida_loss] The 4672/4659 step is partly a recovery from that earlier decrease. [src: caulobacter_fur_lipida_loss] Both figures are reported, +1.08 against the intermediate strain and +0.66 against wild type. [src: caulobacter_fur_lipida_loss]

The report reads this as suggestive of post-transcriptional stabilization, but it is not statistically established. [src: caulobacter_fur_lipida_loss] The observations are consistent with such stabilization when LpxC competition for the shared LptB ATPase disappears, but they do not establish it. [src: caulobacter_fur_lipida_loss] The proposed post-transcriptional induction of the sphingolipid transporter rests on one replicate. [src: caulobacter_fur_lipida_loss]

CCNA_01217 is a related case. Its protein log2 was +0.77 in 4672 versus 4659, or +0.74 versus wild type. [src: caulobacter_fur_lipida_loss]

## What the data allow

Only direction is interpretable. [src: caulobacter_fur_lipida_loss] The lptC2 protein induction, the Pal-Tol upregulation, the LptD/LptE decline and the CCNA_01217 increase all need replicated proteomics before they are claimed at publication rigor. [src: caulobacter_fur_lipida_loss] The lptC2 induction and Pal-Tol upregulation are the two post-hoc findings the report singles out for replication before publication. [src: caulobacter_fur_lipida_loss] The data provider had already planned to replicate the outer-membrane proteome for summer 2026. [src: caulobacter_fur_lipida_loss] The report also suggests that targeted Western blots on lptC2-tagged and Pal-tagged strains would strengthen the claims. [src: caulobacter_fur_lipida_loss]

## Open Directions

- Analyse the replicated outer-membrane proteome planned for summer 2026. It would give per-protein variance and tell us whether the LptD and LptE declines and the lptC2 increase exceed noise.
- Run Western blots on lptC2-tagged and Pal-tagged strains. This would test the lptC2 and Pal-Tol protein changes without relying on proteomics alone.
- Compare lptC2 across all three strains with replicates. This would settle how much of the +1.08 is recovery from the earlier -0.42 and how much is net induction.
- Obtain a wild-type value for MsbA-like CCNA_00307. At present it was detected only in one strain, so no direction can be computed.
