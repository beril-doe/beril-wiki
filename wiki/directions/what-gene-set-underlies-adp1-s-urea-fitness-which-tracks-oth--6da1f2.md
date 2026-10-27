---
type: "Research direction"
description: "Urea fitness in ADP1 was nearly uncorrelated with quinate (r = 0.11) and weakly correlated with the other conditions (r = 0.12-0.28). Which genes drive that independence, and are they a dedicated module, general growth genes, or an assay-specific effect?"
hypothesis: "The low correlation reflects a modest set of urea-specific genes, enriched in accessory pangenome clusters, rather than a global shift in growth physiology. If instead urea-important genes are mostly shared with other conditions, the independence reflects the assay."
approach: "analysis then experiment"
readiness: "unknown"
readiness_basis: "The ADP1 growth data sit in the explorer's own database rather than a listed collection, and the urea assay's nutrient role is not stated in the findings."
collections: ["kbase-ke-pangenome"]
findings: ["acinetobacter_adp1_explorer--df385e36", "acinetobacter_adp1_explorer--886c47ff"]
conflicts: []
papers: ["18319726"]
builds_on: ["findings/acinetobacter_adp1_explorer--df385e36", "findings/acinetobacter_adp1_explorer--886c47ff"]
projects: ["acinetobacter_adp1_explorer"]
topics: ["metabolic-models-and-pathway-level-evidence"]
---
# What gene set underlies ADP1's urea fitness, which tracks other carbon sources so weakly?

Urea fitness in ADP1 was nearly uncorrelated with quinate (r = 0.11) and weakly correlated with the other conditions (r = 0.12-0.28). Which genes drive that independence, and are they a dedicated module, general growth genes, or an assay-specific effect?

## Hypothesis

The low correlation reflects a modest set of urea-specific genes, enriched in accessory pangenome clusters, rather than a global shift in growth physiology. If instead urea-important genes are mostly shared with other conditions, the independence reflects the assay.

## Why it matters

A dedicated, accessory module would show how condition-specific functions are organised in ADP1. A shared-gene or assay explanation would show the low correlation says little about urea biology.

## How to test it

Establish from the ADP1 explorer database what role urea played in the assay (carbon or nitrogen source, and the medium). Then extract genes whose urea fitness differs from their fitness on the other 7 carbon sources, and test enrichment for urease and accessory loci. Map them via cluster IDs to Acinetobacter pangenome core versus accessory status, since ADP1 is absent from the Fitness Browser. Compare with the 8-condition correlation structure, which gives about 5 independent dimensions.

## What would support or refute it

Support: a small urea-specific set, enriched for urea-utilization and accessory genes, accounts for the low correlation. Refute: urea-important genes mostly overlap those of other conditions, or the pattern disappears once assay conditions are matched.

## Data

Approach: analysis then experiment. Readiness: unknown. The ADP1 growth data sit in the explorer's own database rather than a listed collection, and the urea assay's nutrient role is not stated in the findings.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/acinetobacter_adp1_explorer--df385e36|Urea fitness nearly independent of other carbon-source fitness]] (Insufficient literature evidence)
- Finding: [[findings/acinetobacter_adp1_explorer--886c47ff|ADP1 is absent from the Fitness Browser]] (Insufficient literature evidence)

## Closest published work

- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.

PMID 18319726 supplies the single-gene deletion collection used for growth phenotyping but does not analyse urea-specific gene sets or their pangenome distribution.
