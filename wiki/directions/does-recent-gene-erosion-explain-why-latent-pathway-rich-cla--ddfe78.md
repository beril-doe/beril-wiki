---
type: "Research direction"
description: "Do species clades with a higher fraction of latent pathways have more open pangenomes because of recent lineage-specific gene loss, or because of shared phylogeny and sampling?"
hypothesis: "If Black Queen-style erosion drives the clade association (Spearman rho = 0.69, n = 22 clades), latent pathways will show more recent lineage-specific gene loss than active pathways. The association will persist under phylogenetic correction, even though pathway-level conservation did not favour active pathways."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Pangenome and fitness data are in the lakehouse; per-gene loss inference on the tree and PGLS are new compute."
collections: ["kbase-ke-pangenome", "kescience-fitnessbrowser"]
findings: ["metabolic_capability_dependency--6a369153", "metabolic_capability_dependency--b6cd74ee", "metabolic_capability_dependency--f41ac91a", "pathway_capability_dependency--84c4b29b"]
conflicts: ["conflict--community-metabolic-interdependence--cdc57135"]
papers: ["24910088", "35575545", "40568968"]
builds_on: ["findings/metabolic_capability_dependency--6a369153", "findings/metabolic_capability_dependency--b6cd74ee", "findings/metabolic_capability_dependency--f41ac91a", "findings/pathway_capability_dependency--84c4b29b", "conflicts/conflict--community-metabolic-interdependence--cdc57135"]
projects: ["metabolic_capability_dependency", "pathway_capability_dependency"]
topics: ["metabolic-traits-auxotrophy-and-community-dependence"]
---
# Does recent gene erosion explain why latent-pathway-rich clades have open pangenomes?

Do species clades with a higher fraction of latent pathways have more open pangenomes because of recent lineage-specific gene loss, or because of shared phylogeny and sampling?

## Hypothesis

If Black Queen-style erosion drives the clade association (Spearman rho = 0.69, n = 22 clades), latent pathways will show more recent lineage-specific gene loss than active pathways. The association will persist under phylogenetic correction, even though pathway-level conservation did not favour active pathways.

## Why it matters

The pathway-level test did not support lower conservation of latent pathways: the one-sided test for active > latent gave p = 0.94, with latent pathways slightly higher, using a coarse completeness measure. The clade-level openness association is nonetheless positive. Resolving this would show whether dependency evolution leaves a signature only in gene-level loss events, which pathway completeness cannot detect.

## How to test it

In kbase-ke-pangenome, restrict to the 22 clades with fitness-derived latency calls from kescience-fitnessbrowser (48 organisms). Replace pathway-completeness conservation with per-gene presence/absence mapped on the GTDB tree, using direct GapMind step assignments rather than SEED proxies. Count recent singleton or auxiliary losses in latent versus active pathways. Fit phylogenetic generalized least squares (PGLS) of latent fraction on openness. Use the 2,810-species pathway-variability data only as a separate proxy, not as latency.

## What would support or refute it

Support: latent pathways carry excess recent gene loss and the latent-fraction association survives PGLS. Refute: the association vanishes under phylogenetic control, or loss is not concentrated in latent pathways. Results are limited by the threshold sensitivity of the latent fraction (4.7% to 21.1% across 16 threshold combinations).

## Data

Approach: lakehouse analysis. Readiness: needs compute. Pangenome and fitness data are in the lakehouse; per-gene loss inference on the tree and PGLS are new compute.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/metabolic_capability_dependency--6a369153|Clades with more latent pathways have more open pangenomes]] (Candidate novel)
- Finding: [[findings/metabolic_capability_dependency--b6cd74ee|Latent pathways are not less conserved than active pathways]] (Insufficient literature evidence)
- Finding: [[findings/metabolic_capability_dependency--f41ac91a|Many genomically complete pathways show no detectable fitness importance]] (Insufficient literature evidence)
- Finding: [[findings/pathway_capability_dependency--84c4b29b|Pathway variability tracks pangenome openness, strengthening after genome-count control]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--community-metabolic-interdependence--cdc57135|Is Latent Metabolic Capability Condition-Dependent or Partly Fitness-Neutral?]]

## Closest published work

- [PMID 24910088](https://pubmed.ncbi.nlm.nih.gov/24910088/) Less is more: selective advantages can explain the prevalent loss of biosynthetic genes in bacteria.
- [PMID 35575545](https://pubmed.ncbi.nlm.nih.gov/35575545/) Complex Ecotype Dynamics Evolve in Response to Fluctuating Resources.
- [PMID 40568968](https://pubmed.ncbi.nlm.nih.gov/40568968/) Microbial cross-feeding stabilized by segregation of a dependent mutant from its independent ancestor.

PMID 24910088, PMID 35575545 and PMID 40568968 address biosynthetic gene loss and Black Queen-like dynamics in experiments or theory. None relates species-clade latent capability to pangenome openness.
