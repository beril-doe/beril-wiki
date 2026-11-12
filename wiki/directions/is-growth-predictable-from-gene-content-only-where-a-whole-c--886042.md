---
type: "Research direction"
description: "Growth on amino acids and tryptophan was predictable from gene content while metals, antibiotics and nitrogen sources were not. Is predictability higher where growth depends on presence of a complete pathway, and lower where it depends on accessory or regulatory genes?"
hypothesis: "Carbon-source and amino-acid growth calls with a matching pathway predictor are predicted as well by complete-pathway scores alone as by full gene-content models; calls without a matching complete-pathway predictor are predicted worse by pathway scores alone."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The growth table and pathway scores are in the catalog; genome identifiers must be matched across them, and the catalog did not show how many genomes overlap or which conditions beyond carbon sources it holds."
databases: ["globalusers.carbon_source_phenotypes", "kbase.ke_pangenome"]
tables: ["globalusers.carbon_source_phenotypes.phenotype_data_table", "kbase.ke_pangenome.gapmind_pathways", "kbase.ke_pangenome.eggnog_mapper_annotations"]
findings: ["genotype_to_phenotype_enigma--602fd76d", "genotype_to_phenotype_enigma--ccab2bff"]
conflicts: ["conflict--cross-tenant-data-bridging--d89b8efa"]
papers: ["42271456"]
builds_on: ["findings/genotype_to_phenotype_enigma--602fd76d", "findings/genotype_to_phenotype_enigma--ccab2bff", "conflicts/conflict--cross-tenant-data-bridging--d89b8efa"]
projects: ["fw300_metabolic_consistency", "genotype_to_phenotype_enigma"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Is growth predictable from gene content only where a whole conserved pathway decides it?

Growth on amino acids and tryptophan was predictable from gene content while metals, antibiotics and nitrogen sources were not. Is predictability higher where growth depends on presence of a complete pathway, and lower where it depends on accessory or regulatory genes?

## Hypothesis

Carbon-source and amino-acid growth calls with a matching pathway predictor are predicted as well by complete-pathway scores alone as by full gene-content models; calls without a matching complete-pathway predictor are predicted worse by pathway scores alone.

## Why it matters

It would show which phenotypes can be inferred from genomes alone and which need new kinds of data, and would help explain why tryptophan pathway evidence did not imply tryptophan growth in another strain set.

## How to test it

Join the literature-derived carbon-source growth table (genomes by substrate) to pathway-completeness scores for the same genomes. For each substrate, compare a model using only pathway scores for the matching pathway with a model using all functional orthology annotations, holding out whole genera. Then test whether the gap between the two grows for substrates lacking a matching pathway. Metals, antibiotics and nitrogen sources are not in this table; they would need separate data.

## What would support or refute it

Support: pathway-only models match full models for substrates with a matching pathway and lose performance for those without. Refute: pathway-only models fail even where full models succeed, or succeed where full models fail, meaning predictability tracks something else.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The growth table and pathway scores are in the catalog; genome identifiers must be matched across them, and the catalog did not show how many genomes overlap or which conditions beyond carbon sources it holds.

## Builds on

- Finding: [[findings/genotype_to_phenotype_enigma--602fd76d|Binary growth is predictable from gene content only for some condition classes]] (Insufficient literature evidence)
- Finding: [[findings/genotype_to_phenotype_enigma--ccab2bff|Continuous growth parameters are not predictable across genera from gene content]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--cross-tenant-data-bridging--d89b8efa|Does Genomic and Metabolic Evidence for Tryptophan Imply Measured Growth on It?]]

## Closest published work

- [PMID 42271456](https://pubmed.ncbi.nlm.nih.gov/42271456/) Machine learning-based linking of bacterial genomes to optimal growth pH: a foundation for rational microbial engineering.

PMID 42271456 links genomes to a single trait, growth pH; this asks why predictability differs across substrate classes.
