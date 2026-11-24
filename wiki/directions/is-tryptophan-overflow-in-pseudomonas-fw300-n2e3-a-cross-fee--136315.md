---
type: "Research direction"
description: "FW300-N2E3 produces tryptophan and grows on it as sole carbon source, yet the species as a whole cannot catabolize it. Does the excreted tryptophan serve other cells?"
hypothesis: "Tryptophan release by FW300-N2E3 supports growth of a tryptophan-requiring partner, and the strain's tryptophan genes are biosynthetic or regulatory, not catabolic."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The gene mapping can use catalog tables, but the cross-feeding test needs new growth experiments."
databases: ["kbase.ke_pangenome", "kescience.bacdive", "kescience.fitnessbrowser", "kescience.webofmicrobes"]
tables: ["kescience.webofmicrobes.observation", "kescience.webofmicrobes.compound", "kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.experiment", "kbase.ke_pangenome.gapmind_pathways", "kescience.bacdive.metabolite_utilization"]
findings: ["fw300_metabolic_consistency--79d58869", "fw300_metabolic_consistency--a0dac276", "fw300_metabolic_consistency--cd02f79c"]
conflicts: []
papers: ["30208844", "38323821"]
builds_on: ["findings/fw300_metabolic_consistency--79d58869", "findings/fw300_metabolic_consistency--a0dac276", "findings/fw300_metabolic_consistency--cd02f79c"]
projects: ["fw300_metabolic_consistency"]
topics: ["metabolic-models-and-pathway-level-evidence"]
---
# Is tryptophan overflow in Pseudomonas FW300-N2E3 a cross-feeding signal rather than waste?

FW300-N2E3 produces tryptophan and grows on it as sole carbon source, yet the species as a whole cannot catabolize it. Does the excreted tryptophan serve other cells?

## Hypothesis

Tryptophan release by FW300-N2E3 supports growth of a tryptophan-requiring partner, and the strain's tryptophan genes are biosynthetic or regulatory, not catabolic.

## Why it matters

It would show that production-versus-use mismatches in exometabolomics point to exchange. Such mismatches could then guide community design.

## How to test it

Run the deferred step: map FW300-N2E3 fitness genes to GapMind tryptophan pathway steps and classify them as biosynthetic, catabolic or regulatory, using Fitness Browser and Web of Microbes data. Compare BacDive tryptophan use across the P. fluorescens group. Then grow a tryptophan auxotroph with FW300-N2E3 spent medium or in coculture and measure growth.

## What would support or refute it

Support: tryptophan genes are mostly biosynthetic or regulatory, and the auxotroph grows on spent medium in proportion to the tryptophan released. Refute: the strain's fitness depends on catabolic genes, or spent medium does not support the auxotroph.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The gene mapping can use catalog tables, but the cross-feeding test needs new growth experiments.

## Builds on

- Finding: [[findings/fw300_metabolic_consistency--79d58869|Tryptophan is a robust production-versus-utilization discordance]] (Candidate novel)
- Finding: [[findings/fw300_metabolic_consistency--a0dac276|Tryptophan overflow may serve cross-feeding or signaling]] (Candidate novel)
- Finding: [[findings/fw300_metabolic_consistency--cd02f79c|Top fitness genes reflect housekeeping amino acid biosynthesis, not substrate-specific catabolism]] (Candidate novel)

## Closest published work

- [PMID 30208844](https://pubmed.ncbi.nlm.nih.gov/30208844/) Web of microbes (WoM): a curated microbial exometabolomics database for linking chemistry and microbes.
- [PMID 38323821](https://pubmed.ncbi.nlm.nih.gov/38323821/) Machine learning analysis of RB-TnSeq fitness data predicts functional gene modules in Pseudomonas putida KT2440.

The Web of Microbes paper (30208844) describes the exometabolomics resource but reports no tryptophan overflow or exchange role for this strain.
