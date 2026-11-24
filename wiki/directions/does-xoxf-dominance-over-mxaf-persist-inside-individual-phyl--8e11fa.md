---
type: "Research direction"
description: "The pooled xoxF to mxaF ratio is about 19 to 1, while a model with phylum and family effects gives about 143 to 1. Where does mxaF sit across lineages, and does xoxF dominance hold within families?"
hypothesis: "mxaF is clustered in a small number of families, and within most families that carry either gene xoxF outnumbers mxaF, so the pooled ratio understates xoxF dominance within typical lineages."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The ratio was already computed from these annotation and taxonomy tables; the new family-level modelling needs to be run."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.eggnog_mapper_annotations", "kbase.ke_pangenome.gene", "kbase.ke_pangenome.gene_genecluster_junction", "kbase.ke_pangenome.genome", "kbase.ke_pangenome.gtdb_taxonomy_r214v1", "kbase.ke_pangenome.gtdb_metadata"]
findings: ["lanthanide_methylotrophy_atlas--e22bc5ab", "lanthanide_methylotrophy_atlas--f43717f2"]
conflicts: []
papers: ["32341564", "34597405"]
builds_on: ["findings/lanthanide_methylotrophy_atlas--e22bc5ab", "findings/lanthanide_methylotrophy_atlas--f43717f2"]
projects: ["lanthanide_methylotrophy_atlas"]
topics: ["lanthanide-dependent-methylotrophy"]
---
# Does xoxF dominance over mxaF persist inside individual phyla, or is mxaF concentrated in a few lineages?

The pooled xoxF to mxaF ratio is about 19 to 1, while a model with phylum and family effects gives about 143 to 1. Where does mxaF sit across lineages, and does xoxF dominance hold within families?

## Hypothesis

mxaF is clustered in a small number of families, and within most families that carry either gene xoxF outnumbers mxaF, so the pooled ratio understates xoxF dominance within typical lineages.

## Why it matters

It would show whether the xoxF excess is a broad pattern across lineages or driven by a few large groups. That would shape which taxa to target when searching for calcium-dependent versus lanthanide-dependent methanol oxidizers.

## How to test it

Using the GTDB r214 pangenome, tabulate xoxF (K00114) and mxaF (K14028) carriage per family. Compare the model with family effects against a version that also adds genus, and compare ratios in families with both genes. Re-run excluding xoxF genomes with low completeness.

## What would support or refute it

Support: mxaF is confined to few families and xoxF outnumbers it in most mixed families, in both models. Refute: mxaF is spread widely, or the ratio varies sharply by family and the modelled ratio depends on the random-effect structure.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The ratio was already computed from these annotation and taxonomy tables; the new family-level modelling needs to be run.

## Builds on

- Finding: [[findings/lanthanide_methylotrophy_atlas--e22bc5ab|xoxF outnumbers mxaF roughly nineteen to one across the pangenome]] (Insufficient literature evidence)
- Finding: [[findings/lanthanide_methylotrophy_atlas--f43717f2|Phylogeny-corrected model suggests even stronger xoxF dominance within typical phyla]] (Insufficient literature evidence)

## Closest published work

- [PMID 32341564](https://pubmed.ncbi.nlm.nih.gov/32341564/) A complete domain-to-species taxonomy for Bacteria and Archaea.
- [PMID 34597405](https://pubmed.ncbi.nlm.nih.gov/34597405/) eggNOG-mapper v2: Functional Annotation, Orthology Assignments, and Domain Prediction at the Metagenomic Scale.

The retrieved papers (32341564, 34597405) provide taxonomy and annotation but no xoxF or mxaF distribution, so this goes beyond them by locating the excess across lineages.
