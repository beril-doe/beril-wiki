---
type: "Research direction"
description: "Novel and singleton genes are strongly enriched for mobile-element functions, yet the cross-clade innovation photosystem II shows no mobile-element cargo enrichment. Could the difference reflect gain age, with the signature decaying after integration?"
hypothesis: "Recently gained genes sit next to mobile-element machinery much more often than deeply gained genes. Mobile elements could then account for much recent novelty while leaving no trace in older innovations."
approach: "lakehouse analysis"
readiness: "unknown"
readiness_basis: "Gain depths and gene neighbourhoods come from separate projects, and the findings do not show them joined for the singleton set."
collections: ["kbase-ke-pangenome"]
findings: ["cog_analysis--7a21065f", "cog_analysis--62995938", "costly_dispensable_genes--31cecf6a"]
conflicts: ["conflict--horizontal-gene-transfer-driven-innovation--60dc31ce"]
papers: ["21298028", "30809245", "40644951"]
builds_on: ["findings/cog_analysis--7a21065f", "findings/cog_analysis--62995938", "findings/costly_dispensable_genes--31cecf6a", "conflicts/conflict--horizontal-gene-transfer-driven-innovation--60dc31ce"]
projects: ["cog_analysis", "costly_dispensable_genes", "gene_function_ecological_agora"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Does the mobile-element signature of novel genes fade as their gains age?

Novel and singleton genes are strongly enriched for mobile-element functions, yet the cross-clade innovation photosystem II shows no mobile-element cargo enrichment. Could the difference reflect gain age, with the signature decaying after integration?

## Hypothesis

Recently gained genes sit next to mobile-element machinery much more often than deeply gained genes. Mobile elements could then account for much recent novelty while leaving no trace in older innovations.

## Why it matters

It would reconcile two readings of novelty as one process seen at different ages. It would also show that a mobile-element marker undercounts old transfers, so the share of novelty from mobile routes is underestimated.

## How to test it

Assign each novel or singleton gene cluster a gain depth from the tree-based gain analysis of the gene-function atlas. Measure mobile-element neighbourhood rates by depth bin with one neighbourhood definition applied to the singleton set and to the photosystem II, polysaccharide-utilization and mycolic-acid sets. Test whether the rate falls steadily with depth. The focal-set nulls come from three gene sets only, so the singleton extension is new ground.

## What would support or refute it

Support: a falling rate with depth, recent gains near the singleton enrichment level and deep gains near baseline. Refute: a flat rate across depths, meaning the projects differ by gene set rather than age.

## Data

Approach: lakehouse analysis. Readiness: unknown. Gain depths and gene neighbourhoods come from separate projects, and the findings do not show them joined for the singleton set.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/cog_analysis--7a21065f|Mobile elements dominate enrichment among novel genes across sampled species]] (Extends retrieved work)
- Finding: [[findings/cog_analysis--62995938|Defense mechanisms are consistently enriched among novel genes]] (Insufficient literature evidence)
- Finding: [[findings/costly_dispensable_genes--31cecf6a|Costly dispensable genes are strongly enriched for mobile-element keywords]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--horizontal-gene-transfer-driven-innovation--60dc31ce|Do Mobile Elements Carry Most Bacterial Gene Novelty, or Do Focal Innovations Arrive Without an MGE-Cargo Signal?]]

## Closest published work

- [PMID 21298028](https://pubmed.ncbi.nlm.nih.gov/21298028/) Horizontal transfer, not duplication, drives the expansion of protein families in prokaryotes.
- [PMID 30809245](https://pubmed.ncbi.nlm.nih.gov/30809245/) Bacterial 'Grounded' Prophages: Hotspots for Genetic Renovation and Innovation.
- [PMID 40644951](https://pubmed.ncbi.nlm.nih.gov/40644951/) Genomic diversity of Cronobacter sakazakii across the food system to consumers at the global scale.

PMID 21298028 shows horizontal transfer drives protein family expansion, and PMID 30809245 describes prophages as innovation hotspots. Neither follows how the mobile-element signal changes with gain age.
