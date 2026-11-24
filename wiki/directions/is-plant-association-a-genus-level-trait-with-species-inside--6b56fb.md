---
type: "Research direction"
description: "Once shared ancestry is controlled, do plant-associated species differ from non-plant relatives in the same genus in plant-association marker genes?"
hypothesis: "Most plant-association markers separate genera, not species within genera, so a model that controls for ancestry and corrects for the many markers tested retains few markers."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Taxonomy and tree-distance tables are in the catalog; marker tables were not shown and the models need running."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.gtdb_species_clade", "kbase.ke_pangenome.gtdb_metadata", "kbase.ke_pangenome.phylogenetic_tree_distance_pairs"]
findings: ["plant_microbiome_ecotypes--9a9aeb0d"]
conflicts: ["conflict--adversarial-review-pre-registration-and-multiple-testing-discipline--8182f8cb"]
papers: ["29255260", "22792073", "26633631", "25179219"]
builds_on: ["findings/plant_microbiome_ecotypes--9a9aeb0d", "conflicts/conflict--adversarial-review-pre-registration-and-multiple-testing-discipline--8182f8cb"]
projects: ["gene_function_ecological_agora", "microbeatlas_metal_ecology", "plant_microbiome_ecotypes"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Is plant association a genus-level trait, with species inside a genus not distinguished by marker genes?

Once shared ancestry is controlled, do plant-associated species differ from non-plant relatives in the same genus in plant-association marker genes?

## Hypothesis

Most plant-association markers separate genera, not species within genera, so a model that controls for ancestry and corrects for the many markers tested retains few markers.

## Why it matters

It would show that plant adaptation signals in genomes largely reflect which lineages occupy plants, changing how marker panels are used to predict plant lifestyle.

## How to test it

Using GTDB species clades and metadata in the pangenome collection, rerun the within-genus comparison with many more shuffles than the earlier 200, a regression that uses genome tree distances to control ancestry, and a correction for the 15 markers tested together.

## What would support or refute it

Support: few markers remain after ancestry control and correction. Refute: many markers still separate plant from non-plant species within genera.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Taxonomy and tree-distance tables are in the catalog; marker tables were not shown and the models need running.

## Builds on

- Finding: [[findings/plant_microbiome_ecotypes--9a9aeb0d|Most marker plant-association signals are genus-scale, not species-scale]] (Candidate novel)
- Conflict: [[conflicts/conflict--adversarial-review-pre-registration-and-multiple-testing-discipline--8182f8cb|Tension: Review Closure and Pre-registration Claims Versus Residual Gaps in Reported Rigor]]

## Closest published work

- [PMID 29255260](https://pubmed.ncbi.nlm.nih.gov/29255260/) Genomic features of bacterial adaptation to plants.
- [PMID 22792073](https://pubmed.ncbi.nlm.nih.gov/22792073/) Comparative genomics of plant-associated Pseudomonas spp.: insights into diversity and inheritance of traits involved in multitrophic interactions.
- [PMID 26633631](https://pubmed.ncbi.nlm.nih.gov/26633631/) Functional overlap of the Arabidopsis leaf and root microbiota.
- [PMID 25179219](https://pubmed.ncbi.nlm.nih.gov/25179219/) Analysis of genes contributing to plant-beneficial functions in Plant Growth-Promoting Rhizobacteria and related Proteobacteria.

29255260 and 22792073 describe plant-associated genomic features but do not test whether signals persist within genera.
