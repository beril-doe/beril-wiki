---
type: "Research direction"
description: "Species with more variable metabolic pathways have more open pangenomes. Are the variable pathways completed by accessory genes of mobile origin, or by ordinary accessory genes?"
hypothesis: "Pathway variability tracks openness mainly because incomplete pathways are completed by accessory genes. The link stays after controlling for genus, and it is stronger for accessory genes with mobile-element context than for other accessory genes."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Pathway, cluster and annotation tables are in the catalog, but the genome-to-cluster pathway completion mapping needs computing."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.gapmind_pathways", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.pangenome", "kbase.ke_pangenome.bakta_annotations"]
findings: ["pathway_capability_dependency--342cfb41", "pathway_capability_dependency--63330e78", "amr_pangenome_atlas--012985a7"]
conflicts: ["conflict--pangenome-openness-and-its-correlates--472ee9fe"]
papers: ["31639358", "38743630", "41961409", "32589566"]
builds_on: ["findings/pathway_capability_dependency--342cfb41", "findings/pathway_capability_dependency--63330e78", "findings/amr_pangenome_atlas--012985a7", "conflicts/conflict--pangenome-openness-and-its-correlates--472ee9fe"]
projects: ["amr_pangenome_atlas", "amr_strain_variation", "cazyme_pangenome_ecology", "gene_function_ecological_agora", "metabolic_capability_dependency", "pangenome_openness", "pathway_capability_dependency", "pgp_pangenome_ecology"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Is the link between pathway variability and pangenome openness carried by accessory mobile genes?

Species with more variable metabolic pathways have more open pangenomes. Are the variable pathways completed by accessory genes of mobile origin, or by ordinary accessory genes?

## Hypothesis

Pathway variability tracks openness mainly because incomplete pathways are completed by accessory genes. The link stays after controlling for genus, and it is stronger for accessory genes with mobile-element context than for other accessory genes.

## Why it matters

It would show whether metabolic variation in open pangenomes comes from gene exchange or from within-lineage diversification, and whether openness is a metabolic trait or a sampling effect.

## How to test it

Using GapMind pathway calls per genome and cluster status, find species where pathway completeness depends on accessory clusters. Use Bakta annotations for mobile context. Fit pathway variability against openness with controls for genome count and genus, then split by accessory-gene type. Compare against AMR count, whose overall link with openness was near zero.

## What would support or refute it

Support: the link persists within genera and is stronger for mobile-context accessory genes. Refute: it disappears within genera, pointing to phylogeny and sampling depth.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Pathway, cluster and annotation tables are in the catalog, but the genome-to-cluster pathway completion mapping needs computing.

## Builds on

- Finding: [[findings/pathway_capability_dependency--342cfb41|Pathway variability strongly predicts pangenome openness across bacterial species]] (Candidate novel)
- Finding: [[findings/pathway_capability_dependency--63330e78|Amino acid biosynthesis completeness depends on accessory pangenome genes]] (Candidate novel)
- Finding: [[findings/amr_pangenome_atlas--012985a7|Pangenome openness does not correlate with AMR count overall]] (Candidate novel)
- Conflict: [[conflicts/conflict--pangenome-openness-and-its-correlates--472ee9fe|Pangenome Openness: Does It Track AMR, Pathway Variability, Ecology and Gene Gains?]]

## Closest published work

- [PMID 31639358](https://pubmed.ncbi.nlm.nih.gov/31639358/) The Ecology and Evolution of Pangenomes.
- [PMID 38743630](https://pubmed.ncbi.nlm.nih.gov/38743630/) Bacterial lifestyle shapes pangenomes.
- [PMID 41961409](https://pubmed.ncbi.nlm.nih.gov/41961409/) Integrative phylogenomic and pangenome landscape of Bacillus: insights from 10,000 genomes into taxonomy, functional potential, and biotechnological applications.
- [PMID 32589566](https://pubmed.ncbi.nlm.nih.gov/32589566/) Comparative genomics of the genus Roseburia reveals divergent biosynthetic pathways that may influence colonic competition among species.

31639358 and 38743630 relate pangenomes to lifestyle, and 41961409 studies openness in Bacillus. None asks which accessory gene types complete variable pathways.
