---
type: "Research direction"
description: "Are the pathway-based ecotypes seen in Salmonella and Phenylobacterium associated with environment once within-species phylogeny is modelled, or do they only mirror lineage?"
hypothesis: "After regressing out within-species tree distance, ecotype membership still predicts isolation environment in at least some of the ten species with distinct metabolic clusters."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Pathway completeness and tree distances are in the catalog; the corrected association tests need to be run, and the culture step needs new measurements."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.gapmind_pathways", "kbase.ke_pangenome.phylogenetic_tree_distance_pairs", "kbase.ke_pangenome.ncbi_env", "kbase.ke_pangenome.genome"]
findings: ["metabolic_capability_dependency--94b74df5", "ecotype_analysis--38d98bec"]
conflicts: ["conflict--within-species-metabolic-ecotypes-from-pathway-variation--dc402e43"]
papers: ["35575545", "20459825", "24910088"]
builds_on: ["findings/metabolic_capability_dependency--94b74df5", "findings/ecotype_analysis--38d98bec", "conflicts/conflict--within-species-metabolic-ecotypes-from-pathway-variation--dc402e43"]
projects: ["ecotype_analysis", "metabolic_capability_dependency", "pathway_capability_dependency"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Do within-species metabolic ecotypes survive correction for phylogenetic structure?

Are the pathway-based ecotypes seen in Salmonella and Phenylobacterium associated with environment once within-species phylogeny is modelled, or do they only mirror lineage?

## Hypothesis

After regressing out within-species tree distance, ecotype membership still predicts isolation environment in at least some of the ten species with distinct metabolic clusters.

## Why it matters

All ten target species showed metabolic clustering, but phylogeny dominates gene content in 60.5% of species. Whether the clusters are ecological or lineage substructure decides if they count as evidence of adaptation.

## How to test it

For the ten species with metabolic clusters, build GapMind pathway-completeness profiles per genome. Test whether cluster membership is associated with isolation environment, with tree distance from the phylogenetic trees as covariate or via permutation within tree clades. Compare with a null from clusters made on random pathway subsets. Follow with a culture experiment on contrasting strains in Salmonella, grown on carbon sources whose pathways differ between clusters.

## What would support or refute it

Support: environment association stays beyond the permutation null in several species and the culture experiment shows growth differences matching the pathway gap. Refute: the association disappears once clades are controlled, or the predicted growth differences are absent.

## Data

Approach: analysis then experiment. Readiness: needs compute. Pathway completeness and tree distances are in the catalog; the corrected association tests need to be run, and the culture step needs new measurements.

## Builds on

- Finding: [[findings/metabolic_capability_dependency--94b74df5|All ten target species show distinct metabolic ecotype clustering]] (Insufficient literature evidence)
- Finding: [[findings/ecotype_analysis--38d98bec|Phylogeny dominates gene-content similarity in most species analyzed]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--within-species-metabolic-ecotypes-from-pathway-variation--dc402e43|Metabolic Ecotypes: Ecological Signal or Phylogenetic and Sampling Artifact?]]

## Closest published work

- [PMID 35575545](https://pubmed.ncbi.nlm.nih.gov/35575545/) Complex Ecotype Dynamics Evolve in Response to Fluctuating Resources.
- [PMID 20459825](https://pubmed.ncbi.nlm.nih.gov/20459825/) Evolution of metabolic network organization.
- [PMID 24910088](https://pubmed.ncbi.nlm.nih.gov/24910088/) Less is more: selective advantages can explain the prevalent loss of biosynthetic genes in bacteria.

PMID 35575545 shows ecotypes evolving under fluctuating resources in experiments; this direction asks whether natural pathway clusters track environment beyond lineage.
