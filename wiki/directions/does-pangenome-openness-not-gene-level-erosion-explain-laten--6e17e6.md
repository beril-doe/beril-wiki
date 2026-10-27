---
type: "Research direction"
description: "Clades with a larger fraction of latent pathways (genomically complete, no detectable fitness importance under tested conditions) have more open pangenomes, yet latent and active pathways did not differ significantly in conservation. Does openness predict latency independently of how conserved each pathway's genes are?"
hypothesis: "Latency tracks species-level openness rather than per-pathway gene conservation, because species in variable niches keep complete pathways that the tested laboratory conditions rarely call on. If so, openness will still predict the latent fraction after jointly modelling gene-level core/accessory status, genome count and phylogeny."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Latent calls, openness and pangenome conservation come from lakehouse collections, but the joint phylogeny-aware model and per-step accessory annotation have to be built."
collections: ["kbase-ke-pangenome", "kescience-fitnessbrowser"]
findings: ["metabolic_capability_dependency--6a369153", "metabolic_capability_dependency--b6cd74ee", "metabolic_capability_dependency--f41ac91a", "pathway_capability_dependency--84c4b29b"]
conflicts: ["conflict--metabolic-model-gapfilling--09788ff7"]
papers: ["24910088", "35575545", "40568968"]
builds_on: ["findings/metabolic_capability_dependency--6a369153", "findings/metabolic_capability_dependency--b6cd74ee", "findings/metabolic_capability_dependency--f41ac91a", "findings/pathway_capability_dependency--84c4b29b", "conflicts/conflict--metabolic-model-gapfilling--09788ff7"]
projects: ["metabolic_capability_dependency", "pathway_capability_dependency"]
topics: ["metabolic-models-and-pathway-level-evidence"]
---
# Does pangenome openness, not gene-level erosion, explain latent complete pathways across species clades?

Clades with a larger fraction of latent pathways (genomically complete, no detectable fitness importance under tested conditions) have more open pangenomes, yet latent and active pathways did not differ significantly in conservation. Does openness predict latency independently of how conserved each pathway's genes are?

## Hypothesis

Latency tracks species-level openness rather than per-pathway gene conservation, because species in variable niches keep complete pathways that the tested laboratory conditions rarely call on. If so, openness will still predict the latent fraction after jointly modelling gene-level core/accessory status, genome count and phylogeny.

## Why it matters

It would help separate a niche-breadth account of unused complete pathways from a Black Queen-style account of selective gene loss. It would also show how far pathway completeness can be read as dependence.

## How to test it

Using the Pangenome Collection and Fitness Browser, model each clade's latent fraction against openness and against the share of each pathway's genes that are accessory, jointly. Start from the 22-clade correlation (Spearman rho = 0.69) and the pathway-variability correlation across 2,810 species (partial rho = 0.530 after genome-count control). Add phylogenetic control through taxonomic-group stratification or a phylogenetic regression, and test whether accessory-encoded steps are over-represented among latent calls once openness is fixed. Repeat across the 16 latent-threshold combinations, where the latent fraction ranged from 4.7% to 21.1%.

## What would support or refute it

Support: openness remains a significant predictor of latency after conservation, genome count and phylogeny are modelled, and accessory-encoded steps are over-represented among latent calls. Refute: the association disappears under phylogenetic control or is absorbed by gene-level conservation. A non-significant conservation difference alone does not establish equivalence, so the joint model is the decisive comparison.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Latent calls, openness and pangenome conservation come from lakehouse collections, but the joint phylogeny-aware model and per-step accessory annotation have to be built.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/metabolic_capability_dependency--6a369153|Clades with more latent pathways have more open pangenomes]] (Candidate novel)
- Finding: [[findings/metabolic_capability_dependency--b6cd74ee|Latent pathways are not less conserved than active pathways]] (Insufficient literature evidence)
- Finding: [[findings/metabolic_capability_dependency--f41ac91a|Many genomically complete pathways show no detectable fitness importance]] (Insufficient literature evidence)
- Finding: [[findings/pathway_capability_dependency--84c4b29b|Pathway variability tracks pangenome openness, strengthening after genome-count control]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--metabolic-model-gapfilling--09788ff7|Is latent metabolic capability tied to gene conservation or to pangenome openness?]]

## Closest published work

- [PMID 24910088](https://pubmed.ncbi.nlm.nih.gov/24910088/) Less is more: selective advantages can explain the prevalent loss of biosynthetic genes in bacteria.
- [PMID 35575545](https://pubmed.ncbi.nlm.nih.gov/35575545/) Complex Ecotype Dynamics Evolve in Response to Fluctuating Resources.
- [PMID 40568968](https://pubmed.ncbi.nlm.nih.gov/40568968/) Microbial cross-feeding stabilized by segregation of a dependent mutant from its independent ancestor.

PMID 24910088, 35575545 and 40568968 treat Black Queen-style gene loss and cross-feeding in theory or experiments, but none relates a species clade's latent-capability fraction to pangenome openness.
