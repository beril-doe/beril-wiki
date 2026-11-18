---
type: "Research direction"
description: "When environment is measured directly (for example soil pH) rather than inferred from sampling coordinates, does it predict which accessory genes free-living bacteria carry, after accounting for relatedness?"
hypothesis: "Within free-living species, differences in directly measured pH between isolation sites predict differences in accessory gene content beyond what relatedness explains, even though the coordinate-based embedding signal is near zero."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Biosample attributes, genome distances, embeddings and gridded soil properties are listed, but how many species have usable pH values was not visible in the catalog."
databases: ["arkinlab.microbeatlas", "kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.ncbi_env", "kbase.ke_pangenome.genome_ani", "kbase.ke_pangenome.gtdb_metadata", "kbase.ke_pangenome.alphaearth_embeddings_all_years", "arkinlab.microbeatlas.enriched_metadata_gee"]
findings: ["ecotype_analysis--aa4707c1", "ecotype_analysis--9366534f", "ecotype_env_reanalysis--82307b2c", "env_embedding_explorer--7dd94f0f"]
conflicts: ["conflict--ecotype-environment-gene-content--66537c9c", "conflict--genome-wide-versus-locus-specific-ecological-adaptation--3fea06ca"]
papers: ["31227022", "34523223", "29975997", "23332119"]
builds_on: ["findings/ecotype_analysis--aa4707c1", "findings/ecotype_analysis--9366534f", "findings/ecotype_env_reanalysis--82307b2c", "findings/env_embedding_explorer--7dd94f0f", "conflicts/conflict--ecotype-environment-gene-content--66537c9c", "conflicts/conflict--genome-wide-versus-locus-specific-ecological-adaptation--3fea06ca"]
projects: ["ecotype_analysis", "ecotype_env_reanalysis", "ecotype_functional_differentiation", "env_embedding_explorer"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Does measured soil acidity predict accessory gene content where satellite-derived place descriptors do not?

When environment is measured directly (for example soil pH) rather than inferred from sampling coordinates, does it predict which accessory genes free-living bacteria carry, after accounting for relatedness?

## Hypothesis

Within free-living species, differences in directly measured pH between isolation sites predict differences in accessory gene content beyond what relatedness explains, even though the coordinate-based embedding signal is near zero.

## Why it matters

Broad analyses found no stronger environment effect in free-living than in host-associated bacteria, which conflicts with other studies. If direct measurements recover a signal, the earlier null reflects a weak environmental proxy and not weak habitat structuring of gene content.

## How to test it

Choose species with many genomes whose biosample records report pH or soil descriptors, and link them to measured or gridded soil pH for the sample site. For each species, correlate pairwise pH difference with pairwise accessory-gene dissimilarity while controlling for pairwise genome distance. Compare free-living and host-associated species, and compare against the same species' coordinate-embedding result.

## What would support or refute it

Support: a consistent positive pH-gene-content association in free-living species that is absent or weaker in host-associated species and stronger than the embedding result. Refute: no association with direct pH either, which would point to real weakness of whole-genome environment effects.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Biosample attributes, genome distances, embeddings and gridded soil properties are listed, but how many species have usable pH values was not visible in the catalog.

## Builds on

- Finding: [[findings/ecotype_analysis--aa4707c1|No significant difference in environment effects between free-living and host-associated bacteria]] (In tension with retrieved work)
- Finding: [[findings/ecotype_analysis--9366534f|Environment effects on gene content are not significant in most species]] (Extends retrieved work)
- Finding: [[findings/ecotype_env_reanalysis--82307b2c|Environmental species show no stronger environment–gene-content correlation than human-associated species]] (Insufficient literature evidence)
- Finding: [[findings/env_embedding_explorer--7dd94f0f|Prior weak embedding-gene content link may reflect clinical dilution, untested here]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--ecotype-environment-gene-content--66537c9c|Does a Strong Geographic Signal in AlphaEarth Embeddings Mean Environment Shapes Gene Content More Strongly?]]
- Conflict: [[conflicts/conflict--genome-wide-versus-locus-specific-ecological-adaptation--3fea06ca|Weak Genome-Wide Environmental Signal: Locus-Specific Adaptation or Measurement Limits?]]

## Closest published work

- [PMID 31227022](https://pubmed.ncbi.nlm.nih.gov/31227022/) Microbial indicators of environmental perturbations in coral reef ecosystems.
- [PMID 34523223](https://pubmed.ncbi.nlm.nih.gov/34523223/) Keep your friends close: Host compartmentalisation of microbial communities facilitates decoupling from effects of habitat fragmentation.
- [PMID 29975997](https://pubmed.ncbi.nlm.nih.gov/29975997/) Pan-Genomics of Lactobacillus plantarum Revealed Group-Specific Genomic Profiles without Habitat Association.
- [PMID 23332119](https://pubmed.ncbi.nlm.nih.gov/23332119/) Horizontal gene transfer and the evolution of bacterial and archaeal population structure.

PMIDs 31227022 and 34523223 report weaker environment responses in host-associated communities using direct environmental measurements; this direction applies that kind of measurement to gene content across many species.
