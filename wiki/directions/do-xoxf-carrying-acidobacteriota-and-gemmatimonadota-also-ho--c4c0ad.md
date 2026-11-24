---
type: "Research direction"
description: "Acidobacteriota and Gemmatimonadota show high per-genome xoxF rates, yet they are rarely cited in methylotrophy work. Do these genomes carry the PQQ synthesis genes and other lanthanide-associated genes that would indicate real lanthanide-dependent methanol oxidation?"
hypothesis: "Most xoxF-positive Acidobacteriota and Gemmatimonadota genomes carry PQQ synthesis genes and other lanthanide-cassette genes at rates similar to canonical methylotroph families. Genomes lacking them show signs of fragmented assembly or truncated genes."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The annotation and taxonomy tables appear in the catalog, but per-genome cassette scoring and gene-neighbourhood analysis must be run."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.eggnog_mapper_annotations", "kbase.ke_pangenome.bakta_annotations", "kbase.ke_pangenome.gene", "kbase.ke_pangenome.gene_genecluster_junction", "kbase.ke_pangenome.genome", "kbase.ke_pangenome.gtdb_taxonomy_r214v1", "kbase.ke_pangenome.gtdb_metadata"]
findings: ["lanthanide_methylotrophy_atlas--599d45cf"]
conflicts: []
papers: ["34739369", "34597405", "32341564"]
builds_on: ["findings/lanthanide_methylotrophy_atlas--599d45cf"]
projects: ["lanthanide_methylotrophy_atlas"]
topics: ["lanthanide-dependent-methylotrophy"]
---
# Do xoxF-carrying Acidobacteriota and Gemmatimonadota also hold the rest of a lanthanide-use cassette?

Acidobacteriota and Gemmatimonadota show high per-genome xoxF rates, yet they are rarely cited in methylotrophy work. Do these genomes carry the PQQ synthesis genes and other lanthanide-associated genes that would indicate real lanthanide-dependent methanol oxidation?

## Hypothesis

Most xoxF-positive Acidobacteriota and Gemmatimonadota genomes carry PQQ synthesis genes and other lanthanide-cassette genes at rates similar to canonical methylotroph families. Genomes lacking them show signs of fragmented assembly or truncated genes.

## Why it matters

If the cassette is intact, xoxF calls in these phyla would be candidate lanthanide-using methanol oxidizers, a possible extension of lanthanide-dependent methanol oxidation to new phyla pending functional validation. If not, the high rates reflect over-calling of a broad enzyme family.

## How to test it

In the KBase Data Lakehouse pangenome, list genomes with xoxF (eggNOG K00114) in Acidobacteriota, Gemmatimonadota and Beijerinckiaceae/Hyphomicrobiaceae as reference. Score each for PQQ synthesis genes and neighbouring genes using eggNOG and Bakta annotations, gene order on the genome, and genome completeness from the GTDB metadata. Compare cassette completeness between phyla.

## What would support or refute it

Support: cassette completeness in these phyla is similar to the reference families, and gaps track low genome quality. Refute: the cassette is mostly absent even in high-quality genomes, so xoxF calls there do not indicate lanthanide use.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The annotation and taxonomy tables appear in the catalog, but per-genome cassette scoring and gene-neighbourhood analysis must be run.

## Builds on

- Finding: [[findings/lanthanide_methylotrophy_atlas--599d45cf|High xoxF per-genome rates occur in phyla rarely cited for methylotrophy]] (Insufficient literature evidence)

## Closest published work

- [PMID 34739369](https://pubmed.ncbi.nlm.nih.gov/34739369/) Bakta: rapid and standardized annotation of bacterial genomes via alignment-free sequence identification.
- [PMID 34597405](https://pubmed.ncbi.nlm.nih.gov/34597405/) eggNOG-mapper v2: Functional Annotation, Orthology Assignments, and Domain Prediction at the Metagenomic Scale.
- [PMID 32341564](https://pubmed.ncbi.nlm.nih.gov/32341564/) A complete domain-to-species taxonomy for Bacteria and Archaea.

The retrieved papers (34739369, 34597405, 32341564) are annotation and taxonomy tools and report no xoxF rates by phylum, so this goes beyond them by testing whether the calls reflect a full cassette.
