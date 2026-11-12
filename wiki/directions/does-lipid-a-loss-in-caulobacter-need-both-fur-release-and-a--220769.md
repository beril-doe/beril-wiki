---
type: "Research direction"
description: "Caulobacter can lose lipid A when the iron regulator Fur is absent, and the rescued strain also lacks sspB. Loss of sspB buffers the Fur-dependent micro-aerobic respiratory operon at transcript level, and sphingolipid biosynthesis genes are not switched on in routine rich medium. Does rescue require the respiratory buffering as well as fur loss?"
hypothesis: "As a hypothesis, lipid A loss is tolerated only when fur loss and preserved expression of the cbb3/fix respiratory operon coincide. Either change alone fails, and forcing cbb3 expression substitutes for the sspB deletion."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "The transcript buffering and the absence of sphingolipid gene induction in rich medium are measured, but their causal role in rescue has not been tested, and iron-limitation fitness data are missing."
collections: ["kescience-fitnessbrowser"]
findings: ["caulobacter_fur_lipida_loss--088e2303", "caulobacter_fur_lipida_loss--75b18331"]
conflicts: []
papers: ["35649364", "19520766", "30210482"]
builds_on: ["findings/caulobacter_fur_lipida_loss--088e2303", "findings/caulobacter_fur_lipida_loss--75b18331"]
projects: ["caulobacter_fur_lipida_loss"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Does lipid A loss in Caulobacter need both Fur release and a preserved respiratory operon?

Caulobacter can lose lipid A when the iron regulator Fur is absent, and the rescued strain also lacks sspB. Loss of sspB buffers the Fur-dependent micro-aerobic respiratory operon at transcript level, and sphingolipid biosynthesis genes are not switched on in routine rich medium. Does rescue require the respiratory buffering as well as fur loss?

## Hypothesis

As a hypothesis, lipid A loss is tolerated only when fur loss and preserved expression of the cbb3/fix respiratory operon coincide. Either change alone fails, and forcing cbb3 expression substitutes for the sspB deletion.

## Why it matters

It would explain why a single regulator mutation permits loss of an essential outer-membrane lipid, and would link envelope remodelling to oxygen-linked respiration. The existing data show the respiratory buffering but do not show that it matters for rescue, so this tests whether it does.

## How to test it

In Caulobacter, test viability of the lpxC deletion in a fur-only background and an sspB-only background. Then express the cbb3/fix operon from an independent promoter in the fur-only background and ask whether it restores viability. Measure sphingolipid levels by lipidomics in the rescued strain, to learn whether the pool is maintained without gene induction, which the transcript data alone cannot show. Fitness data did not distinguish the buffered respiratory set from background, so check in new envelope-stress fitness experiments whether these genes matter at all.

## What would support or refute it

Support: lpxC deletion is lethal in either single background and viable in fur-only with forced cbb3 expression. Refute: fur-only is enough for viability, or cbb3 expression does not substitute for sspB loss, consistent with the null fitness result for these genes. Lipidomics separately tells whether the sphingolipid pool is maintained.

## Data

Approach: experiment. Readiness: needs new measurements. The transcript buffering and the absence of sphingolipid gene induction in rich medium are measured, but their causal role in rescue has not been tested, and iron-limitation fitness data are missing.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/caulobacter_fur_lipida_loss--088e2303|ΔsspB buffers a Fur-dependent respiratory operon at transcript level]] (Insufficient literature evidence)
- Finding: [[findings/caulobacter_fur_lipida_loss--75b18331|Sphingolipid biosynthesis is not transcriptionally induced during rescue]] (Insufficient literature evidence)

## Closest published work

- [PMID 35649364](https://pubmed.ncbi.nlm.nih.gov/35649364/) Caulobacter lipid A is conditionally dispensable in the absence of fur and in the presence of anionic sphingolipids.
- [PMID 19520766](https://pubmed.ncbi.nlm.nih.gov/19520766/) Fur controls iron homeostasis and oxidative stress defense in the oligotrophic alpha-proteobacterium Caulobacter crescentus.
- [PMID 30210482](https://pubmed.ncbi.nlm.nih.gov/30210482/) Iron Deficiency Generates Oxidative Stress and Activation of the SOS Response in Caulobacter crescentus.

PMID 35649364 shows fur mutations and anionic sphingolipids make lipid A dispensable, and PMID 19520766 and PMID 30210482 define the Fur regulon. None tests a respiratory-operon requirement or an sspB-linked buffering effect.
