---
type: "Research direction"
description: "Do species that split into more metabolic ecotypes occupy a wider range of environments than species with few ecotypes, beyond what the number of sequenced genomes and the pangenome's openness explain?"
hypothesis: "Among species with many genomes, the count of metabolic ecotypes rises with the breadth of environments the genomes were drawn from. Phylogenetic grouping alone does not account for this."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Pathway scores, genome-to-species links and environment text are in the catalog; the ecotype clustering and embedding-based breadth must be computed, with embedding coverage limited."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.gapmind_pathways", "kbase.ke_pangenome.genome", "kbase.ke_pangenome.pangenome", "kbase.ke_pangenome.gtdb_metadata", "kbase.ke_pangenome.ncbi_env"]
findings: ["pathway_capability_dependency--4df15631", "pathway_capability_dependency--84c4b29b", "pathway_capability_dependency--f655b856"]
conflicts: []
papers: ["24465487", "22928415"]
builds_on: ["findings/pathway_capability_dependency--4df15631", "findings/pathway_capability_dependency--84c4b29b", "findings/pathway_capability_dependency--f655b856"]
projects: ["pathway_capability_dependency"]
topics: ["metabolic-models-and-pathway-level-evidence"]
---
# Do species with more metabolic ecotypes live across a wider range of environments?

Do species that split into more metabolic ecotypes occupy a wider range of environments than species with few ecotypes, beyond what the number of sequenced genomes and the pangenome's openness explain?

## Hypothesis

Among species with many genomes, the count of metabolic ecotypes rises with the breadth of environments the genomes were drawn from. Phylogenetic grouping alone does not account for this.

## Why it matters

Variable pathways track pangenome openness, but phylogeny dominates gene content in most species, so an ecological explanation is unproven. A link to environmental breadth would show that metabolic ecotypes are habitat adaptation rather than lineage structure.

## How to test it

For the species with at least 50 genomes and several variable pathways, cluster genomes by pathway presence to count ecotypes. Measure environmental breadth as the spread of satellite-derived environmental embeddings per species, and as the number of distinct isolation-source categories. Model ecotype count against breadth with genome count, openness and genus as covariates. Keep only species whose genomes have embeddings (about 28% of genomes), and repeat the analysis within each family.

## What would support or refute it

Support: breadth predicts ecotype count within families after covariates. Refute: the relation disappears within families or tracks only genome count, which would mean ecotypes mostly reflect sampling and lineage.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Pathway scores, genome-to-species links and environment text are in the catalog; the ecotype clustering and embedding-based breadth must be computed, with embedding coverage limited.

## Builds on

- Finding: [[findings/pathway_capability_dependency--4df15631|Species with many genomes split into a handful of metabolic ecotypes]] (Insufficient literature evidence)
- Finding: [[findings/pathway_capability_dependency--84c4b29b|Pathway variability tracks pangenome openness, strengthening after genome-count control]] (Insufficient literature evidence)
- Finding: [[findings/pathway_capability_dependency--f655b856|Planned test of ecotypes against environmental niche breadth was not run]] (Insufficient literature evidence)

## Closest published work

- [PMID 24465487](https://pubmed.ncbi.nlm.nih.gov/24465487/) Metabolic flexibility as a major predictor of spatial distribution in microbial communities.
- [PMID 22928415](https://pubmed.ncbi.nlm.nih.gov/22928415/) Mapping the niche space of soil microorganisms using taxonomy and traits.

PMID 24465487 links metabolic flexibility to spatial distribution of communities, and PMID 22928415 maps soil niche space with taxonomy and traits. Neither relates within-species metabolic ecotype counts to environmental breadth across thousands of species.
