---
type: "Concept"
description: "How choice of pairwise strain contrast (cumulative versus isolating) affects the test of CtpA as a proposed LpxF-equivalent, and why borderline thresholds must be pre-registered; stops at CtpA."
sources: ["summaries/caulobacter_fur_lipida_loss__REPORT.md"]
---
# Contrast design and confounding in testing a putative lipid A-processing enzyme

This page covers how the choice of strain contrast affects the test of CtpA as a proposed LpxF-equivalent lipid A-processing enzyme in *Caulobacter crescentus*. The evidence comes from one report, [[summaries/caulobacter_fur_lipida_loss__REPORT]], and one organism. A cumulative contrast gives a significant result, but it confounds several deletions. The contrast pre-registered to isolate the lipid A-loss response fails its bar. The hypothesis therefore stays untested rather than confirmed. [src: caulobacter_fur_lipida_loss]

## The two contrasts

The pre-registered 4599-vs-4584 contrast was designed to isolate the Δlpxc-specific response. The cumulative 4599-vs-4580 contrast conflates Δfur + ΔsspB and Δlpxc effects. [src: caulobacter_fur_lipida_loss]

The cumulative contrast is significant, with logFC +0.76 and FDR (false discovery rate) 0.035. [src: caulobacter_fur_lipida_loss] The report notes it as supplemental evidence, with FDR=0.035. [src: caulobacter_fur_lipida_loss] It also notes that the contrast confounds Δfur and Δlpxc effects. [src: caulobacter_fur_lipida_loss] It reports this result as a supplemental observation consistent with CtpA being Fur-regulated. It is not evidence for lipid-A-loss-driven CtpA induction. [src: caulobacter_fur_lipida_loss]

## The pre-registered test

The pre-registered pass criterion was FDR<0.05 or ≥2× protein. The BORDERLINE criterion required both 0.05 < pvalue < 0.15 and protein detection. [src: caulobacter_fur_lipida_loss]

In 4599-vs-4584, the CtpA (CCNA_03113) transcript gave logFC +0.58, pvalue=0.048 and FDR=0.109. [src: caulobacter_fur_lipida_loss] The pvalue fails the BORDERLINE lower bound of 0.05. The FDR fails the PASS bar of 0.05. [src: caulobacter_fur_lipida_loss] CtpA was not detected in the single-replicate outer-membrane proteome. [src: caulobacter_fur_lipida_loss] The report therefore rejects CtpA upregulation at the pre-registered bar. [src: caulobacter_fur_lipida_loss]

The report corrects earlier drafts that mislabeled this result as BORDERLINE. [src: caulobacter_fur_lipida_loss] A fixed threshold stated in advance settles such a near-threshold case. [src: caulobacter_fur_lipida_loss]

## What this means for the LpxF-substitute hypothesis

The report treats CtpA's hypothesized LpxF-substitute role (Zik 2022) as untested by this work. [src: caulobacter_fur_lipida_loss] The prediction is that CtpA-mediated processing should produce a specific CPG headgroup. [src: caulobacter_fur_lipida_loss] The data do not support that role at the pre-registered bar. [src: caulobacter_fur_lipida_loss] The significant cumulative contrast cannot replace the isolating one. [src: caulobacter_fur_lipida_loss]

## Open Directions

- Run replicated outer-membrane proteomics. Detection in a single-replicate proteome is the gap.
- Add an isolating contrast with more transcript replicates, since pvalue 0.048 and FDR 0.109 sit near the threshold.
- Test directly for the predicted CPG headgroup by lipid analysis.
- Run contrasts that separate Δfur from Δlpxc, to test whether CtpA induction follows Fur regulation.
- Fix thresholds, including borderline handling, before any new contrast is run.
