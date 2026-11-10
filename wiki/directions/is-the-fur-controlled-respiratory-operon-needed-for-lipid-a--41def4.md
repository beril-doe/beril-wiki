---
type: "Research direction"
description: "Does the Fur-repressed micro-aerobic respiratory operon, which the sspB deletion buffers at the transcript level, actually matter for survival of lipid-A-free cells?"
hypothesis: "Lipid-A-free Caulobacter survives only if cbb3-type respiration stays on. The sspB deletion helps maintain it when Fur is lost, so supplying the operon should partly replace the need for the sspB deletion."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "Needs new strain constructions; existing transcript data show buffering but do not establish that these genes are required for rescue."
collections: []
findings: ["caulobacter_fur_lipida_loss--088e2303", "caulobacter_fur_lipida_loss--75b18331"]
conflicts: []
papers: ["35649364", "19520766", "30210482"]
builds_on: ["findings/caulobacter_fur_lipida_loss--088e2303", "findings/caulobacter_fur_lipida_loss--75b18331"]
projects: ["caulobacter_fur_lipida_loss"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Is the Fur-controlled respiratory operon needed for lipid A loss in Caulobacter?

Does the Fur-repressed micro-aerobic respiratory operon, which the sspB deletion buffers at the transcript level, actually matter for survival of lipid-A-free cells?

## Hypothesis

Lipid-A-free Caulobacter survives only if cbb3-type respiration stays on. The sspB deletion helps maintain it when Fur is lost, so supplying the operon should partly replace the need for the sspB deletion.

## Why it matters

It would show whether lipid A dispensability is a coupled envelope and energy-state change, rather than only a sphingolipid effect. The buffered transcripts so far only show buffering, not a requirement, and no induction of sphingolipid genes was seen in rich medium.

## How to test it

In the Caulobacter ΔlpxC background, test viability with fur deleted alone, sspB deleted alone, and both. In ΔfurΔlpxC, express the cbb3/cyd/fix operon (CCNA_01466-01476) from an inducible promoter and score rescue without the sspB deletion. Measure oxygen consumption in each strain, and sphingolipid pools, noting that earlier transcripts came only from rich PYE medium.

## What would support or refute it

Supported if viability tracks respiratory operon expression and operon supply substitutes for the sspB deletion. Refuted if rescue works with the operon silenced, or if operon supply gives no benefit.

## Data

Approach: experiment. Readiness: needs new measurements. Needs new strain constructions; existing transcript data show buffering but do not establish that these genes are required for rescue.

## Builds on

- Finding: [[findings/caulobacter_fur_lipida_loss--088e2303|ΔsspB buffers a Fur-dependent respiratory operon at transcript level]] (Insufficient literature evidence)
- Finding: [[findings/caulobacter_fur_lipida_loss--75b18331|Sphingolipid biosynthesis is not transcriptionally induced during rescue]] (Insufficient literature evidence)

## Closest published work

- [PMID 35649364](https://pubmed.ncbi.nlm.nih.gov/35649364/) Caulobacter lipid A is conditionally dispensable in the absence of fur and in the presence of anionic sphingolipids.
- [PMID 19520766](https://pubmed.ncbi.nlm.nih.gov/19520766/) Fur controls iron homeostasis and oxidative stress defense in the oligotrophic alpha-proteobacterium Caulobacter crescentus.
- [PMID 30210482](https://pubmed.ncbi.nlm.nih.gov/30210482/) Iron Deficiency Generates Oxidative Stress and Activation of the SOS Response in Caulobacter crescentus.

PMID 35649364 linked fur loss and anionic sphingolipids to lipid A dispensability and PMIDs 19520766 and 30210482 defined the Fur regulon. None tests respiratory chain requirement.
