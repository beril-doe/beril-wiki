---
type: "Research direction"
description: "Only 4 of 37 rare-earth acid mine drainage MAGs carry any xoxF and none carry lanmodulin. Does a larger collection of rare-earth-impacted metagenomes show a higher xoxF rate than comparable sites without rare-earth enrichment?"
hypothesis: "xoxF-bearing genomes are more common in rare-earth-impacted metagenomes than in matched non-impacted samples from the same phyla, whereas lanmodulin stays rare."
approach: "analysis then experiment"
readiness: "unknown"
readiness_basis: "The catalog lists biosample and MAG tables but does not show how many rare-earth-impacted samples or MAG annotations they hold."
databases: ["kbase.nmdc_mags", "nmdc.metadata", "nmdc.ncbi_biosamples"]
tables: ["nmdc.ncbi_biosamples.biosamples_attributes", "kbase.nmdc_mags.mag_catalog", "nmdc.metadata.workflow_execution_set_mags_list"]
findings: ["lanthanide_methylotrophy_atlas--5d1414b7"]
conflicts: []
papers: ["34739369", "32341564"]
builds_on: ["findings/lanthanide_methylotrophy_atlas--5d1414b7"]
projects: ["lanthanide_methylotrophy_atlas"]
topics: ["lanthanide-dependent-methylotrophy"]
---
# Does rare-earth supply select for the xoxF cassette in rare-earth-impacted metagenomes?

Only 4 of 37 rare-earth acid mine drainage MAGs carry any xoxF and none carry lanmodulin. Does a larger collection of rare-earth-impacted metagenomes show a higher xoxF rate than comparable sites without rare-earth enrichment?

## Hypothesis

xoxF-bearing genomes are more common in rare-earth-impacted metagenomes than in matched non-impacted samples from the same phyla, whereas lanmodulin stays rare.

## Why it matters

The small drainage set can only describe. A larger comparison would show whether rare-earth availability is linked to xoxF carriage in nature or whether the gene's spread is independent of the environment.

## How to test it

Find rare-earth-impacted samples (mining tailings, leachate, bioreactors) using biosample attributes and NMDC metadata. Count xoxF and lanmodulin in their MAGs, and compare with MAGs from other environments within the same phyla, using a model with phylum and family effects.

## What would support or refute it

Support: a higher within-phylum xoxF rate in rare-earth-impacted samples. Refute: rates match those of other environments. The catalog did not show whether enough such samples exist in the lakehouse, so too few samples would leave the question open.

## Data

Approach: analysis then experiment. Readiness: unknown. The catalog lists biosample and MAG tables but does not show how many rare-earth-impacted samples or MAG annotations they hold.

## Builds on

- Finding: [[findings/lanthanide_methylotrophy_atlas--5d1414b7|REE-AMD metagenome-assembled genomes carry no lanmodulin]] (Insufficient literature evidence)

## Closest published work

- [PMID 34739369](https://pubmed.ncbi.nlm.nih.gov/34739369/) Bakta: rapid and standardized annotation of bacterial genomes via alignment-free sequence identification.
- [PMID 32341564](https://pubmed.ncbi.nlm.nih.gov/32341564/) A complete domain-to-species taxonomy for Bacteria and Archaea.

The retrieved papers (34739369, 32341564) are tools and do not address rare-earth environments, so this adds an environment comparison.
