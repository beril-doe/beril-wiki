---
type: "Research direction"
description: "In Caulobacter, loss of Fur lets cells survive without lipid A, and a further sspB deletion dampens a group of respiratory genes (cbb3, cyd, fix-NOPQ) that Fur loss would otherwise raise. Is lowering that respiratory operon part of what makes lipid A loss tolerable?"
hypothesis: "Cells lacking lipid A and Fur survive only if cbb3-type respiration is kept low. Forcing high expression of the cbb3 operon in the rescued strain will kill it, while deleting cbb3 in a lipid A-deficient, Fur-deficient strain that has no sspB deletion will restore viability."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "Transcriptome and fitness data identify the buffered operon, but no strains altering its expression exist and transcriptomes were taken only in rich medium."
collections: ["kescience-fitnessbrowser"]
findings: ["caulobacter_fur_lipida_loss--088e2303", "caulobacter_fur_lipida_loss--75b18331"]
conflicts: []
papers: ["35649364", "19520766", "30210482"]
builds_on: ["findings/caulobacter_fur_lipida_loss--088e2303", "findings/caulobacter_fur_lipida_loss--75b18331"]
projects: ["caulobacter_fur_lipida_loss"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Does silencing the cbb3 respiratory operon let Caulobacter survive without lipid A?

In Caulobacter, loss of Fur lets cells survive without lipid A, and a further sspB deletion dampens a group of respiratory genes (cbb3, cyd, fix-NOPQ) that Fur loss would otherwise raise. Is lowering that respiratory operon part of what makes lipid A loss tolerable?

## Hypothesis

Cells lacking lipid A and Fur survive only if cbb3-type respiration is kept low. Forcing high expression of the cbb3 operon in the rescued strain will kill it, while deleting cbb3 in a lipid A-deficient, Fur-deficient strain that has no sspB deletion will restore viability.

## Why it matters

It would show that rescue involves metabolic and oxidative-stress control as well as membrane lipids, since sphingolipid synthesis genes were not switched on. It would also redirect antibiotic-resistance models based on lipid A loss.

## How to test it

In Caulobacter strains lacking lpxC and fur, with and without sspB, construct inducible expression of ccoNOPQ and a ccoNOPQ deletion. Measure viability, oxygen consumption and iron-related oxidative stress in rich medium. Use Fitness Browser Caulobacter data to see whether cbb3, cyd and fix genes carry fitness effects under envelope stress. Add iron-limitation experiments, since none exist in the compendium.

## What would support or refute it

Support: forced operon expression kills the rescued strain and deletion restores viability in the strain without sspB deletion. Refutation: viability is unchanged by operon expression or deletion, so the buffering is a side effect.

## Data

Approach: experiment. Readiness: needs new measurements. Transcriptome and fitness data identify the buffered operon, but no strains altering its expression exist and transcriptomes were taken only in rich medium.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/caulobacter_fur_lipida_loss--088e2303|ΔsspB buffers a Fur-dependent respiratory operon at transcript level]] (Insufficient literature evidence)
- Finding: [[findings/caulobacter_fur_lipida_loss--75b18331|Sphingolipid biosynthesis is not transcriptionally induced during rescue]] (Insufficient literature evidence)

## Closest published work

- [PMID 35649364](https://pubmed.ncbi.nlm.nih.gov/35649364/) Caulobacter lipid A is conditionally dispensable in the absence of fur and in the presence of anionic sphingolipids.
- [PMID 19520766](https://pubmed.ncbi.nlm.nih.gov/19520766/) Fur controls iron homeostasis and oxidative stress defense in the oligotrophic alpha-proteobacterium Caulobacter crescentus.
- [PMID 30210482](https://pubmed.ncbi.nlm.nih.gov/30210482/) Iron Deficiency Generates Oxidative Stress and Activation of the SOS Response in Caulobacter crescentus.

PMID 35649364 shows that fur mutations and anionic sphingolipids make lipid A dispensable, and PMID 19520766 and PMID 30210482 define the Fur regulon and iron stress. None tests whether respiratory-operon buffering is required for survival.
