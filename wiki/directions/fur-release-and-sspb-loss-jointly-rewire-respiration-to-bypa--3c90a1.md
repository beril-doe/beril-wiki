---
type: "Research direction"
description: "Is the transcript-level buffering of the cbb3/cyd/fix respiratory operon in the sspB background required for lipid A dispensability, with sphingolipid flux controlled post-transcriptionally?"
hypothesis: "Lipid A dispensability needs both Fur derepression and the sspB-dependent respiratory operon state. Deleting lpxC is not viable in a \u0394fur-only or \u0394sspB-only background, and loss of the respiratory operon blocks rescue, while sphingolipid pools are maintained or increased without induction of biosynthesis genes."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "The transcript evidence exists, but strains, lipidomics and iron-limitation fitness experiments are new."
collections: ["kescience-fitnessbrowser"]
findings: ["caulobacter_fur_lipida_loss--088e2303", "caulobacter_fur_lipida_loss--75b18331"]
conflicts: []
papers: ["35649364", "19520766", "30210482"]
builds_on: ["findings/caulobacter_fur_lipida_loss--088e2303", "findings/caulobacter_fur_lipida_loss--75b18331"]
projects: ["caulobacter_fur_lipida_loss"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Fur release and sspB loss jointly rewire respiration to bypass lipid A

Is the transcript-level buffering of the cbb3/cyd/fix respiratory operon in the sspB background required for lipid A dispensability, with sphingolipid flux controlled post-transcriptionally?

## Hypothesis

Lipid A dispensability needs both Fur derepression and the sspB-dependent respiratory operon state. Deleting lpxC is not viable in a Δfur-only or ΔsspB-only background, and loss of the respiratory operon blocks rescue, while sphingolipid pools are maintained or increased without induction of biosynthesis genes.

## Why it matters

It would establish a two-switch, post-transcriptional route around an essential outer-membrane pathway. Transcript buffering alone does not show these genes are mechanistically critical, so this tests that directly.

## How to test it

In Caulobacter, attempt ΔlpxC in Δfur-only, ΔsspB-only and double backgrounds and compare viability with the triple mutant. Delete the cbb3/cyd/fix operon in the rescued strain. Run targeted lipidomics of sphingolipid and CPG levels. Add RB-TnSeq under bipyridyl, ferric salt and hemin, since the existing compendium has no iron-limitation experiments.

## What would support or refute it

Support: neither single background tolerates ΔlpxC, operon deletion blocks rescue, and sphingolipid levels hold or rise with no spt induction (spt was down -0.64, FDR 0.002). Refute: ΔlpxC is viable with Δfur alone, operon loss does not matter, or sphingolipid levels fall.

## Data

Approach: experiment. Readiness: needs new measurements. The transcript evidence exists, but strains, lipidomics and iron-limitation fitness experiments are new.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/caulobacter_fur_lipida_loss--088e2303|ΔsspB buffers a Fur-dependent respiratory operon at transcript level]] (Insufficient literature evidence)
- Finding: [[findings/caulobacter_fur_lipida_loss--75b18331|Sphingolipid biosynthesis is not transcriptionally induced during rescue]] (Insufficient literature evidence)

## Closest published work

- [PMID 35649364](https://pubmed.ncbi.nlm.nih.gov/35649364/) Caulobacter lipid A is conditionally dispensable in the absence of fur and in the presence of anionic sphingolipids.
- [PMID 19520766](https://pubmed.ncbi.nlm.nih.gov/19520766/) Fur controls iron homeostasis and oxidative stress defense in the oligotrophic alpha-proteobacterium Caulobacter crescentus.
- [PMID 30210482](https://pubmed.ncbi.nlm.nih.gov/30210482/) Iron Deficiency Generates Oxidative Stress and Activation of the SOS Response in Caulobacter crescentus.

PMID 35649364 shows fur mutations and anionic sphingolipids make lipid A dispensable, and PMID 19520766 and PMID 30210482 define the Fur regulon; none tests respiratory-operon buffering or post-transcriptional sphingolipid control.
