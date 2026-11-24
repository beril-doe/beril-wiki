---
type: "Research direction"
description: "Do species with open pangenomes keep more complete but dispensable pathways because those pathways sit in accessory genes that are gained and lost, or does the link reflect uneven fitness testing?"
hypothesis: "Pathways whose completeness depends on accessory genes are more often fitness-neutral than pathways completed by core genes, and this accounts for most of the link between latent fraction and pangenome openness."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The catalog shows the fitness, pathway and gene-cluster tables, but linking pathway steps to core or accessory clusters is a new computation."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.organism", "kescience.fitnessbrowser.experiment", "kbase.ke_pangenome.gapmind_pathways", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.pangenome"]
findings: ["metabolic_capability_dependency--3bcc11af", "metabolic_capability_dependency--b6cd74ee", "pathway_capability_dependency--342cfb41", "pathway_capability_dependency--63330e78"]
conflicts: ["conflict--latent-metabolic-capability-versus-fitness-dependency--199fd6c8"]
papers: ["24910088", "32589566", "35575545", "40568968"]
builds_on: ["findings/metabolic_capability_dependency--3bcc11af", "findings/metabolic_capability_dependency--b6cd74ee", "findings/pathway_capability_dependency--342cfb41", "findings/pathway_capability_dependency--63330e78", "conflicts/conflict--latent-metabolic-capability-versus-fitness-dependency--199fd6c8"]
projects: ["essential_metabolome", "metabolic_capability_dependency", "pathway_capability_dependency"]
topics: ["metabolic-traits-auxotrophy-and-community-dependence"]
---
# Does the latent share of complete pathways rise with pangenome openness because accessory genes supply them?

Do species with open pangenomes keep more complete but dispensable pathways because those pathways sit in accessory genes that are gained and lost, or does the link reflect uneven fitness testing?

## Hypothesis

Pathways whose completeness depends on accessory genes are more often fitness-neutral than pathways completed by core genes, and this accounts for most of the link between latent fraction and pangenome openness.

## Why it matters

It would show that dispensable metabolism is a feature of how open genomes are structured. That would make auxotrophy and pathway loss predictable from pangenome structure.

## How to test it

For Fitness Browser organisms, label each complete pathway as core-only or accessory-dependent from the pangenome gene clusters and GapMind steps. Compare the share of fitness-neutral pathways between the two groups within species. Then test whether the openness link remains after the accessory-dependent share is added to the model. Control for the number of conditions tested per organism.

## What would support or refute it

Support: accessory-dependent pathways are more often neutral, and the openness link shrinks once they are modelled. Refute: no difference between the groups, or an openness link that stays unchanged. Latent pathways were not separated from active ones by how conserved they are, so a refutation is likely to be informative.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The catalog shows the fitness, pathway and gene-cluster tables, but linking pathway steps to core or accessory clusters is a new computation.

## Builds on

- Finding: [[findings/metabolic_capability_dependency--3bcc11af|Latent pathway fraction rises with pangenome openness across species clades]] (Candidate novel)
- Finding: [[findings/metabolic_capability_dependency--b6cd74ee|Pathway conservation does not separate latent from active pathways]] (Candidate novel)
- Finding: [[findings/pathway_capability_dependency--342cfb41|Pathway variability strongly predicts pangenome openness across bacterial species]] (Candidate novel)
- Finding: [[findings/pathway_capability_dependency--63330e78|Amino acid biosynthesis completeness depends on accessory pangenome genes]] (Candidate novel)
- Conflict: [[conflicts/conflict--latent-metabolic-capability-versus-fitness-dependency--199fd6c8|Latent Pathways: Condition-Dependent Capability or Threshold Artifact?]]

## Closest published work

- [PMID 24910088](https://pubmed.ncbi.nlm.nih.gov/24910088/) Less is more: selective advantages can explain the prevalent loss of biosynthetic genes in bacteria.
- [PMID 32589566](https://pubmed.ncbi.nlm.nih.gov/32589566/) Comparative genomics of the genus Roseburia reveals divergent biosynthetic pathways that may influence colonic competition among species.
- [PMID 35575545](https://pubmed.ncbi.nlm.nih.gov/35575545/) Complex Ecotype Dynamics Evolve in Response to Fluctuating Resources.
- [PMID 40568968](https://pubmed.ncbi.nlm.nih.gov/40568968/) Microbial cross-feeding stabilized by segregation of a dependent mutant from its independent ancestor.

24910088 explains biosynthetic gene loss and 32589566 compares amino acid pathways within one genus. Neither separates core-dependent from accessory-dependent pathways to explain the openness trend.
