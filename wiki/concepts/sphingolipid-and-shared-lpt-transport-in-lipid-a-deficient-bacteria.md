---
type: "Concept"
description: "Whether sphingolipid biosynthesis is induced or constitutive during lipid A loss and whether the sphingolipid transporters share the LPS Lpt machinery; stops at Caulobacter transcript and proteome evidence."
sources: ["summaries/caulobacter_fur_lipida_loss__REPORT.md"]
---
# Sphingolipid and shared Lpt transport in lipid A-deficient bacteria

In Caulobacter crescentus, sphingolipid biosynthesis is constitutive rather than induced during Δlpxc rescue. [src: caulobacter_fur_lipida_loss] The canonical Lpt apparatus is maintained at the transcript level, as the shared-component model predicts. [src: caulobacter_fur_lipida_loss] Protein evidence is a single-replicate pilot, so it is suggestive only. [src: caulobacter_fur_lipida_loss] The source is [[summaries/caulobacter_fur_lipida_loss__REPORT]], and the organism is [[entities/caulobacter-crescentus]].

## Sphingolipid biosynthesis is constitutive

The report rejected its initial hypothesis that Δfur derepresses sphingolipid biosynthesis, because the pathway is not induced. [src: caulobacter_fur_lipida_loss] It concludes that biosynthesis is constitutive and that rescue does not require upregulation. [src: caulobacter_fur_lipida_loss] No biosynthesis genes were significantly up (0/6). [src: caulobacter_fur_lipida_loss] spt was down by -0.64 (FDR 0.002, false discovery rate) and sphk by -0.40 (FDR 0.02). [src: caulobacter_fur_lipida_loss] The hypothesis test passed strongly: 0 biosynthesis genes were up at FDR<0.05, and spt and sphk were slightly down. [src: caulobacter_fur_lipida_loss] The report asserts that the existing CPG pool suffices for rescue. [src: caulobacter_fur_lipida_loss]

From this, the report infers that the cell does not respond to lipid-A loss by making more CPG-biosynthesis transcript, so rescue must be flux-driven or post-transcriptional. [src: caulobacter_fur_lipida_loss] This is an inference from transcript data, not a direct flux measurement.

## Shared Lpt transport

Uchendu, Isom and Klein 2026 (bioRxiv 10.1101/2026.04.12.717747) identified the Caulobacter sphingolipid inner-membrane transporters CCNA_01213/01214/01226 (lptG2/F2/C2). They share the canonical LptB ATPase with LPS transport. [src: caulobacter_fur_lipida_loss]

At the transcript level, the canonical Lpt apparatus is maintained, and no components were down. [src: caulobacter_fur_lipida_loss] MsbA-like CCNA_00307 rose by +0.89 (FDR 0.01). LptC-related CCNA_03716 rose by +0.56 (FDR 0.005). The report says both support Uchendu's shared-component prediction. [src: caulobacter_fur_lipida_loss]

### Protein-level discordance

The protein data are mixed. The report describes transcript-protein discordance in Lpt repurposing. [src: caulobacter_fur_lipida_loss] The Uchendu lptC2 gene CCNA_01226 had transcript change -0.60 (FDR 0.034) but protein log2(4672/4659) = +1.08. [src: caulobacter_fur_lipida_loss] The report states that lptC2 protein accumulates >2-fold despite transcript downregulation, and calls this the first regulatory and proteomic evidence that the shared-component model operates in a Δlpxc strain. [src: caulobacter_fur_lipida_loss]

CCNA_01217 is sphingolipid biosynthesis machinery needed for CHIR-090 tolerance in Zik 2022. [src: caulobacter_fur_lipida_loss] Its protein log2 was +0.77 in 4672 vs 4659, or +0.74 vs wild type. [src: caulobacter_fur_lipida_loss]

These protein results are single-replicate observations. They are consistent with post-transcriptional stabilization when LpxC competition for the shared LptB ATPase disappears, but they do not statistically establish it. [src: caulobacter_fur_lipida_loss] See [[concepts/transcript-protein-discordance-and-single-replicate-proteomics-limits]].

## Predictions

The report's post-transcriptional flux model predicts that strain 4599 (Δlpxc Δfur ΔsspB) maintains or increases its sphingolipid pool without biosynthesis induction, because LpxC competition for shared substrates is gone. [src: caulobacter_fur_lipida_loss] It proposes targeted lipidomics with intact lipid A precursor quantification to test this and the CPG-headgroup prediction. [src: caulobacter_fur_lipida_loss]

## Open Directions

- Replicate the proteomics with several biological replicates, to test whether lptC2 and CCNA_01217 protein increases hold statistically.
- Run targeted lipidomics with lipid A precursor quantification in 4599, to test whether the sphingolipid pool is maintained or increased without biosynthesis induction.
- Measure LptB ATPase occupancy or competition directly, to test the shared-component mechanism behind the protein accumulation.
