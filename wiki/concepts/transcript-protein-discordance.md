---
type: "Concept"
description: "Transcript and protein measurements can diverge, exposing post-transcriptional regulation."
sources: ["summaries/caulobacter_fur_lipida_loss__REPORT.md"]
---
# Transcript–protein discordance reveals post-transcriptional control

Transcript–protein discordance occurs when changes in RNA abundance and protein abundance differ in direction or magnitude, making it evidence for regulation between transcription and protein accumulation rather than a simple transcript-level response. [src: caulobacter_fur_lipida_loss] In the Δfur ΔsspB Δlpxc rescue context, the strongest evidence is concentrated in lipid-transport and outer-membrane components, although the single-replicate proteome limits the strength of mechanistic inference. [src: caulobacter_fur_lipida_loss]

The measurements are summarized in [[summaries/caulobacter_fur_lipida_loss__REPORT]] and connect directly to [[concepts/multi-omics-integration]]. [src: caulobacter_fur_lipida_loss]

## Lpt apparatus: opposing RNA and protein responses

At the transcript level, no canonical Lpt component was DOWN in the analyzed contrast. [src: caulobacter_fur_lipida_loss] The MsbA-like CCNA_00307 was UP by +0.89 with FDR 0.01, while the LptC-related CCNA_03716 was UP by +0.56 with FDR 0.005. [src: caulobacter_fur_lipida_loss]

The detected canonical proteins moved in the opposite direction: LptD changed by log2(4672/4659) = -0.47 and by log2(4672/4580) = -0.62, while LptE changed by -0.78 and -0.68, respectively. [src: caulobacter_fur_lipida_loss] This **contradicts** a model in which the transcript-level increases uniformly propagate into increased Lpt protein abundance and instead supports regulation at translation, protein stability, complex assembly, or turnover. [src: caulobacter_fur_lipida_loss]

CCNA_00307 was detected only in the rescued strain, at abundance 300 in 4672 and NaN in the other strains, so its direction relative to the wild-type baseline was uncomputable. [src: caulobacter_fur_lipida_loss]

## Sphingolipid-transport discordance

The sphingolipid transporter CCNA_01226 (*lptC2*) showed transcript -0.60 with FDR 0.034 but protein log2(4672/4659) = +1.08. [src: caulobacter_fur_lipida_loss] Because its protein level was already DOWN by -0.42 log2 in 4659/4580, its net protein change versus the wild-type baseline was +0.66 log2, reported as approximately 1.58×. [src: caulobacter_fur_lipida_loss]

CCNA_01217 protein changed by +0.77 in 4672 versus 4659, or +0.74 versus wild type. [src: caulobacter_fur_lipida_loss] Together, these observations are **consistent with** post-transcriptional stabilization or retention of sphingolipid-transport machinery, but they do not establish that mechanism statistically because the outer-membrane proteome had a single replicate per strain. [src: caulobacter_fur_lipida_loss]

The broader sphingolipid biosynthesis pathway was not transcriptionally induced: 0/6 biosynthesis genes were UP, *spt* was DOWN by -0.64 with FDR 0.002, and *sphk* was DOWN by -0.40 with FDR 0.02. [src: caulobacter_fur_lipida_loss] The transporter-level protein increases therefore **refine** the interpretation from pathway induction to possible maintenance or stabilization of transport capacity during lipid A loss. [src: caulobacter_fur_lipida_loss]

## Pal-Tol remodeling as a convergent response

Pal/CCNA_00784 was induced at both transcript and protein levels, with transcript +2.08 and protein +2.84. [src: caulobacter_fur_lipida_loss] Its appearance in the late ChvI cohort provides an independent regulatory connection to the remodeling response. [src: caulobacter_fur_lipida_loss]

The report interprets Pal-Tol upregulation primarily through retrograde phospholipid transport and outer-membrane lipid homeostasis after loss of outer-leaflet lipid A. [src: caulobacter_fur_lipida_loss] Direct Pal–peptidoglycan contacts and a Caulobacter division-associated role remain additional context rather than direct measurements from this project. [src: caulobacter_fur_lipida_loss]

Because Pal shows concordant RNA and protein induction while LptD and LptE show protein decreases despite transcript-level increases elsewhere in the apparatus, the data support a **component-specific** rather than globally uniform post-transcriptional response. [src: caulobacter_fur_lipida_loss]

## Evidence limits and interpretation

The outer-membrane proteome had a single replicate per strain, so no per-protein statistics were available. [src: caulobacter_fur_lipida_loss] The *lptC2* protein induction, Pal-Tol upregulation, LptD/LptE decline, and CCNA_01217 increase therefore require replicated proteomics before publication-level claims can be made. [src: caulobacter_fur_lipida_loss]

The transcriptome used a single PYE rich-medium growth condition, so the observed discordance describes this experimental context rather than a demonstrated response across iron or envelope conditions. [src: caulobacter_fur_lipida_loss] The findings **support** a hypothesis of post-transcriptional control in the rescued strain, but they do not identify the responsible process or establish causality. [src: caulobacter_fur_lipida_loss]

## Open Directions

- Collect replicated outer-membrane proteomes across the rescued, intermediate, and wild-type strains, then test whether LptD, LptE, CCNA_01226, CCNA_01217, and Pal show reproducible RNA–protein discordance. [src: caulobacter_fur_lipida_loss]
- Measure targeted *lptC2*, CCNA_01217, LptD, LptE, and Pal abundance with targeted proteomics or immunoblotting, then ask whether the observed protein changes persist after normalization to wild-type baseline. [src: caulobacter_fur_lipida_loss]
- Pair RNA-seq with ribosome profiling and protein half-life measurements, then distinguish translational control from differential protein stability as explanations for the opposing transcript and protein directions. [src: caulobacter_fur_lipida_loss]
- Perform lipidomics and Tol-Pal phospholipid-transport assays, then test whether the protein-level changes restore outer-membrane lipid homeostasis after loss of lipid A. [src: caulobacter_fur_lipida_loss]
