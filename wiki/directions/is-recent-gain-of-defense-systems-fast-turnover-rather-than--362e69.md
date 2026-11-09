---
type: "Research direction"
description: "CRISPR-Cas gene families show most of their gains at genus level and very few ancient gains. Is that because they are gained at a high rate, or because gains are lost quickly so only recent ones remain?"
hypothesis: "Defense genes are gained at a rate similar to other function classes but lost quickly. Recent gains of CRISPR-Cas should therefore be less likely than recent gains of other classes to persist into sister clades or deeper nodes."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Gain-depth estimates exist per class; persistence of gains was not computed and requires a descendant-presence pass over the tree."
collections: ["kbase-ke-pangenome"]
findings: ["gene_function_ecological_agora--c0bd8a1a", "cog_analysis--62995938"]
conflicts: []
papers: ["10097118", "37232518", "21298028"]
builds_on: ["findings/gene_function_ecological_agora--c0bd8a1a", "findings/cog_analysis--62995938"]
projects: ["cog_analysis", "gene_function_ecological_agora"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Is recent gain of defense systems fast turnover rather than fast acquisition?

CRISPR-Cas gene families show most of their gains at genus level and very few ancient gains. Is that because they are gained at a high rate, or because gains are lost quickly so only recent ones remain?

## Hypothesis

Defense genes are gained at a rate similar to other function classes but lost quickly. Recent gains of CRISPR-Cas should therefore be less likely than recent gains of other classes to persist into sister clades or deeper nodes.

## Why it matters

A recent-skewed profile is usually read as intense transfer. Separating turnover from acquisition would change how acquisition-depth profiles are read for defense, resistance and other mobile functions.

## How to test it

Using the acquisition-depth estimates over the species tree, compare CRISPR-Cas, restriction systems and tRNA synthetases. For each gain event, ask whether the gene is still present in descendant genomes at successive depths. Add gain-event counts per branch length to separate rate from persistence, and check the same classes among novel and singleton genes in the 32-species comparison.

## What would support or refute it

Support: defense gains have shorter persistence than gains of other classes at similar depth, with comparable per-branch gain rate. Refutation: persistence is similar across classes, so the recent skew reflects a true higher acquisition rate or a depth-estimation bias.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Gain-depth estimates exist per class; persistence of gains was not computed and requires a descendant-presence pass over the tree.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/gene_function_ecological_agora--c0bd8a1a|Function classes have distinct gene-acquisition depth profiles, CRISPR-Cas most recent-skewed]] (Insufficient literature evidence)
- Finding: [[findings/cog_analysis--62995938|Defense mechanisms are consistently enriched among novel genes]] (Insufficient literature evidence)

## Closest published work

- [PMID 10097118](https://pubmed.ncbi.nlm.nih.gov/10097118/) Horizontal gene transfer among genomes: the complexity hypothesis.
- [PMID 37232518](https://pubmed.ncbi.nlm.nih.gov/37232518/) Empirical Evidence That Complexity Limits Horizontal Gene Transfer.
- [PMID 21298028](https://pubmed.ncbi.nlm.nih.gov/21298028/) Horizontal transfer, not duplication, drives the expansion of protein families in prokaryotes.

PMIDs 10097118 and 37232518 argue that gene complexity limits transfer, and 21298028 shows transfer drives protein-family expansion. None separates acquisition rate from loss for defense systems.
