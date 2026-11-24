---
type: "Research direction"
description: "Lanmodulin occurs only in three alpha-proteobacterial methylotroph families, and 13 of 62 lanmodulin genomes lack xoxF. Are these missed xoxF calls, or do they use another lanthanide-handling system?"
hypothesis: "The 13 lanmodulin-without-xoxF genomes differ from the other 49 in carrying other lanthanide-associated genes, or in having low genome completeness, rather than being random annotation misses."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The 62 genomes were already identified and the annotation tables are in the catalog; the sequence search and neighbourhood comparison still need to be run."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.bakta_annotations", "kbase.ke_pangenome.eggnog_mapper_annotations", "kbase.ke_pangenome.gene", "kbase.ke_pangenome.gene_genecluster_junction", "kbase.ke_pangenome.gtdb_metadata", "kbase.ke_pangenome.gtdb_taxonomy_r214v1"]
findings: ["lanthanide_methylotrophy_atlas--7bc741c0", "lanthanide_methylotrophy_atlas--1f25da9f"]
conflicts: []
papers: ["34739369", "34597405"]
builds_on: ["findings/lanthanide_methylotrophy_atlas--7bc741c0", "findings/lanthanide_methylotrophy_atlas--1f25da9f"]
projects: ["lanthanide_methylotrophy_atlas"]
topics: ["lanthanide-dependent-methylotrophy"]
---
# Do lanmodulin genomes lacking xoxF use an alternative lanthanide-handling route?

Lanmodulin occurs only in three alpha-proteobacterial methylotroph families, and 13 of 62 lanmodulin genomes lack xoxF. Are these missed xoxF calls, or do they use another lanthanide-handling system?

## Hypothesis

The 13 lanmodulin-without-xoxF genomes differ from the other 49 in carrying other lanthanide-associated genes, or in having low genome completeness, rather than being random annotation misses.

## Why it matters

The co-occurrence of lanmodulin and xoxF fell just under the pre-set 80% threshold. Resolving the 13 genomes would show whether lanmodulin has a role apart from methanol dehydrogenase.

## How to test it

Take the 62 Bakta-validated lanmodulin genomes. For the 13 without xoxF, search the genome sequences for xoxF-like genes by sequence similarity, and compare genome completeness and gene neighbourhoods around lanmodulin with those in the 49 xoxF-positive genomes. Use eggNOG and Bakta annotations and GTDB metadata in the pangenome.

## What would support or refute it

Support: the 13 carry distinct neighbouring genes, or show no xoxF even with sensitive search in complete genomes. Refute: sensitive search recovers xoxF in most of the 13, or they are mostly incomplete genomes, which points to annotation gaps.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The 62 genomes were already identified and the annotation tables are in the catalog; the sequence search and neighbourhood comparison still need to be run.

## Builds on

- Finding: [[findings/lanthanide_methylotrophy_atlas--7bc741c0|Lanmodulin–xoxF co-occurrence falls just below the pre-registered threshold]] (Insufficient literature evidence)
- Finding: [[findings/lanthanide_methylotrophy_atlas--1f25da9f|Lanmodulin is restricted to three alpha-proteobacterial methylotroph families]] (Insufficient literature evidence)

## Closest published work

- [PMID 34739369](https://pubmed.ncbi.nlm.nih.gov/34739369/) Bakta: rapid and standardized annotation of bacterial genomes via alignment-free sequence identification.
- [PMID 34597405](https://pubmed.ncbi.nlm.nih.gov/34597405/) eggNOG-mapper v2: Functional Annotation, Orthology Assignments, and Domain Prediction at the Metagenomic Scale.

The retrieved papers (34739369, 34597405) describe annotation tools, not lanmodulin, so this goes beyond them by asking what the xoxF-free lanmodulin genomes carry.
