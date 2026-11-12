---
type: "Research direction"
description: "Is the soil and sediment enrichment of xoxF that persists inside Acidobacteriota driven by chemistry that makes lanthanides available, such as lower pH?"
hypothesis: "Within Acidobacteriota, xoxF carriage rises with soil acidity and falls in neutral or alkaline soils. The same pattern holds inside other xoxF-carrying phyla, so habitat chemistry rather than taxonomy drives it."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Genome, annotation and biosample attribute tables are listed, but the catalog did not show whether soil pH is recorded for enough genomes."
databases: ["kbase.ke_pangenome", "kbase.nmdc_mags", "nmdc.ncbi_biosamples"]
tables: ["kbase.ke_pangenome.genome", "kbase.ke_pangenome.ncbi_env", "kbase.ke_pangenome.eggnog_mapper_annotations", "kbase.ke_pangenome.gtdb_taxonomy_r214v1", "nmdc.ncbi_biosamples.biosamples_attributes", "kbase.nmdc_mags.mag_catalog"]
findings: ["lanthanide_methylotrophy_atlas--73b82896"]
conflicts: []
papers: ["38369453", "32341564"]
builds_on: ["findings/lanthanide_methylotrophy_atlas--73b82896"]
projects: ["lanthanide_methylotrophy_atlas"]
topics: ["lanthanide-dependent-methylotrophy"]
---
# Does soil acidity, which frees lanthanides, explain xoxF enrichment within Acidobacteriota?

Is the soil and sediment enrichment of xoxF that persists inside Acidobacteriota driven by chemistry that makes lanthanides available, such as lower pH?

## Hypothesis

Within Acidobacteriota, xoxF carriage rises with soil acidity and falls in neutral or alkaline soils. The same pattern holds inside other xoxF-carrying phyla, so habitat chemistry rather than taxonomy drives it.

## Why it matters

It would give a mechanism for the soil signal that survived a within-phylum comparison, and would let soil pH predict where lanthanide-dependent methylotrophy matters.

## How to test it

Link Acidobacteriota genomes, and genomes from other xoxF-carrying phyla, to sample metadata for soil pH, soil type and depth. Model xoxF carriage against pH while holding genus fixed, in isolate genomes and in soil metagenome-assembled genomes separately. Repeat in the other phyla. Add a prediction that could fail: the relationship should be absent for the calcium-dependent methanol enzyme, which does not need lanthanides.

## What would support or refute it

Support: carriage rises as pH falls within genus, in several phyla, and not for the calcium-dependent enzyme. Refute: no pH relationship within genus, or the enrichment is explained by a few soil-specific genera.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Genome, annotation and biosample attribute tables are listed, but the catalog did not show whether soil pH is recorded for enough genomes.

## Builds on

- Finding: [[findings/lanthanide_methylotrophy_atlas--73b82896|Soil enrichment of xoxF persists within Acidobacteriota]] (Candidate novel)

## Closest published work

- [PMID 38369453](https://pubmed.ncbi.nlm.nih.gov/38369453/) Weathered granites and soils harbour microbes with lanthanide-dependent methylotrophic enzymes.
- [PMID 32341564](https://pubmed.ncbi.nlm.nih.gov/32341564/) A complete domain-to-species taxonomy for Bacteria and Archaea.

PMID 38369453 reports xoxF clusters in Acidobacteria in weathered granite and soil but does not test a habitat variable within one phylum. PMID 32341564 supplies the taxonomy used to stratify.
