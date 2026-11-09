---
type: "Research direction"
description: "Are the gene-content differences between ecotypes inherited along the species tree, or do they cross lineage boundaries by horizontal transfer?"
hypothesis: "Ecotype-defining genes in mobile-element and defense categories have evolutionary histories that disagree with the core-genome tree more often than housekeeping genes do, meaning they are transferred between lineages and ecotypes are not simply clades."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Gene-cluster presence tables exist, but within-species core trees, per-family gene trees and incongruence scores for the 12 species must be built."
collections: ["kbase-ke-pangenome"]
findings: ["ecotype_functional_differentiation--840b73cb", "ecotype_functional_differentiation--69a046fd", "ecotype_functional_differentiation--667d861b"]
conflicts: ["conflict--adaptive-versus-housekeeping-functional-differentiation--a27e3db1"]
papers: ["35801696", "23332119", "40644951", "33423895"]
builds_on: ["findings/ecotype_functional_differentiation--840b73cb", "findings/ecotype_functional_differentiation--69a046fd", "findings/ecotype_functional_differentiation--667d861b", "conflicts/conflict--adaptive-versus-housekeeping-functional-differentiation--a27e3db1"]
projects: ["cog_analysis", "ecotype_functional_differentiation", "plant_microbiome_ecotypes"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Do ecotype-defining accessory genes move between lineages rather than descend within them?

Are the gene-content differences between ecotypes inherited along the species tree, or do they cross lineage boundaries by horizontal transfer?

## Hypothesis

Ecotype-defining genes in mobile-element and defense categories have evolutionary histories that disagree with the core-genome tree more often than housekeeping genes do, meaning they are transferred between lineages and ecotypes are not simply clades.

## Why it matters

The largest ecotype differences were in adaptive and unknown-function categories, but nothing shows whether these are inherited or transferred. If transfer dominates, ecotypes are assemblages of exchanged genes shaped by selection. If inheritance dominates, they are demographic subpopulations.

## How to test it

For the 12 species with valid gene-content ecotypes, build core-genome trees from the Pangenome Collection and gene trees for ecotype-defining gene families. For each functional category, measure incongruence between gene tree and core tree (for example tree-reconciliation or topology-distance scores), and use it, not scattered presence alone, as the signature of transfer. Compare adaptive with housekeeping categories and unknown-function genes, controlling for gene family size and prevalence.

## What would support or refute it

Support: adaptive and unknown-function families show more gene-tree versus core-tree incongruence than housekeeping families. Refutation: all categories track the core tree equally, or ecotype structure collapses into clade membership.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Gene-cluster presence tables exist, but within-species core trees, per-family gene trees and incongruence scores for the 12 species must be built.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/ecotype_functional_differentiation--840b73cb|Most species-by-COG tests show ecotype differentiation, with every analyzed species affected]] (Insufficient literature evidence)
- Finding: [[findings/ecotype_functional_differentiation--69a046fd|Unknown-function and replication/repair categories show the largest ecotype differences]] (Extends retrieved work)
- Finding: [[findings/ecotype_functional_differentiation--667d861b|Adaptive COG categories show larger mean ecotype effect sizes than housekeeping categories]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--adaptive-versus-housekeeping-functional-differentiation--a27e3db1|Do Adaptive Functions Sit in the Accessory Genome or Inside the Core?]]

## Closest published work

- [PMID 35801696](https://pubmed.ncbi.nlm.nih.gov/35801696/) Core genes can have higher recombination rates than accessory genes within global microbial populations.
- [PMID 23332119](https://pubmed.ncbi.nlm.nih.gov/23332119/) Horizontal gene transfer and the evolution of bacterial and archaeal population structure.
- [PMID 40644951](https://pubmed.ncbi.nlm.nih.gov/40644951/) Genomic diversity of Cronobacter sakazakii across the food system to consumers at the global scale.
- [PMID 33423895](https://pubmed.ncbi.nlm.nih.gov/33423895/) Mechanisms That Shape Microbial Pangenomes.

PMID 35801696 shows core genes can recombine more than accessory genes in global populations, and PMID 40644951 reports category enrichment in accessory content of one species. Neither tests whether ecotype-defining genes depart from the core tree by functional category.
