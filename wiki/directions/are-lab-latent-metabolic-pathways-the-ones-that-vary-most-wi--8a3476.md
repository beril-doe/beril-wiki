---
type: "Research direction"
description: "About a sixth of genomically complete pathways show no fitness importance in the lab, yet latent pathways are no less conserved across species than active ones. Is Black Queen gene loss visible inside species, with latent pathways present in fewer conspecific genomes?"
hypothesis: "Within a species, pathways classed as latent in the lab-tested strain are complete in a smaller and more variable share of that species' genomes than pathways classed as active."
approach: "analysis then experiment"
readiness: "unknown"
readiness_basis: "Per-genome pathway calls and organism lists are in the catalog, but the catalog did not show the per-gene fitness values needed to regenerate latent labels, and only some fitness organisms have matching pathway data."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kbase.ke_pangenome.gapmind_pathways", "kbase.ke_pangenome.gtdb_species_clade", "kbase.ke_pangenome.gtdb_taxonomy_r214v1", "kescience.fitnessbrowser.organism", "kescience.fitnessbrowser.experiment"]
findings: ["metabolic_capability_dependency--f41ac91a", "metabolic_capability_dependency--b6cd74ee", "metabolic_capability_dependency--6a369153", "pathway_capability_dependency--250e9510", "pathway_capability_dependency--61e28c8b"]
conflicts: []
papers: ["22448042", "24910088", "35575545", "40568968"]
builds_on: ["findings/metabolic_capability_dependency--f41ac91a", "findings/metabolic_capability_dependency--b6cd74ee", "findings/metabolic_capability_dependency--6a369153", "findings/pathway_capability_dependency--250e9510", "findings/pathway_capability_dependency--61e28c8b"]
projects: ["metabolic_capability_dependency", "pathway_capability_dependency"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Are lab-latent metabolic pathways the ones that vary most within a species?

About a sixth of genomically complete pathways show no fitness importance in the lab, yet latent pathways are no less conserved across species than active ones. Is Black Queen gene loss visible inside species, with latent pathways present in fewer conspecific genomes?

## Hypothesis

Within a species, pathways classed as latent in the lab-tested strain are complete in a smaller and more variable share of that species' genomes than pathways classed as active.

## Why it matters

A within-species signal would show that Black Queen-like loss acts over short timescales and would flag which complete pathways in model strains are dispensable in nature. A null would mean latency reflects the narrow lab conditions.

## How to test it

Take the latent and active labels the earlier analyses defined for the barcoded-fitness organisms. Link each organism to its species group through the organism table and the species-clade table. From the per-genome pathway calls, compute the share of conspecific genomes with a complete pathway for each pathway. Compare latent with active pathways in the same species, separating carbon-source from amino-acid pathways and correcting for genome count. If the labels must be regenerated, per-gene fitness values are needed, and the catalog did not show them.

## What would support or refute it

Support: latent pathways are complete in fewer and more variable conspecific genomes than active ones. Refute: the two classes are equally variable within species.

## Data

Approach: analysis then experiment. Readiness: unknown. Per-genome pathway calls and organism lists are in the catalog, but the catalog did not show the per-gene fitness values needed to regenerate latent labels, and only some fitness organisms have matching pathway data.

## Builds on

- Finding: [[findings/metabolic_capability_dependency--f41ac91a|Many genomically complete pathways show no detectable fitness importance]] (Insufficient literature evidence)
- Finding: [[findings/metabolic_capability_dependency--b6cd74ee|Latent pathways are not less conserved than active pathways]] (Insufficient literature evidence)
- Finding: [[findings/metabolic_capability_dependency--6a369153|Clades with more latent pathways have more open pangenomes]] (Candidate novel)
- Finding: [[findings/pathway_capability_dependency--250e9510|Latent capability outnumbers active dependency among model-bacteria pathways]] (Insufficient literature evidence)
- Finding: [[findings/pathway_capability_dependency--61e28c8b|Every latent-capability pair becomes fitness-important under some condition type]] (Insufficient literature evidence)

## Closest published work

- [PMID 22448042](https://pubmed.ncbi.nlm.nih.gov/22448042/) The Black Queen Hypothesis: evolution of dependencies through adaptive gene loss.
- [PMID 24910088](https://pubmed.ncbi.nlm.nih.gov/24910088/) Less is more: selective advantages can explain the prevalent loss of biosynthetic genes in bacteria.
- [PMID 35575545](https://pubmed.ncbi.nlm.nih.gov/35575545/) Complex Ecotype Dynamics Evolve in Response to Fluctuating Resources.
- [PMID 40568968](https://pubmed.ncbi.nlm.nih.gov/40568968/) Microbial cross-feeding stabilized by segregation of a dependent mutant from its independent ancestor.

PMID 22448042 and PMID 24910088 describe adaptive loss of dispensable biosynthetic functions, and PMID 35575545 and PMID 40568968 show dependency evolution in experiments; none relates fitness-defined latent pathways to within-species pathway variation in natural genomes.
