---
type: "Research direction"
description: "Isolates from heavy-metal sites score higher on predicted metal tolerance, and the effect persists within Proteobacteria. Does it arise from extra metal-resistance genes in strains of the same species, or from contaminated sites favoring different species?"
hypothesis: "Within species that have genomes from both contaminated and non-contaminated sources, contaminated-source genomes carry more metal-resistance gene annotations. Species identity explains little of the contamination effect."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Isolation, strain and pangenome tables are in the catalog, but species-name matching is partial and the number of species with both source classes was not shown."
databases: ["kbase.ke_pangenome", "kescience.bacdive"]
tables: ["kescience.bacdive.isolation", "kescience.bacdive.strain", "kbase.ke_pangenome.genome", "kbase.ke_pangenome.gtdb_metadata", "kbase.ke_pangenome.gtdb_species_clade", "kbase.ke_pangenome.eggnog_mapper_annotations"]
findings: ["bacdive_metal_validation--09db2bda", "bacdive_metal_validation--1ac30de6", "bacdive_metal_validation--60f073d0"]
conflicts: []
papers: ["41601069", "33540257", "37290750"]
builds_on: ["findings/bacdive_metal_validation--09db2bda", "findings/bacdive_metal_validation--1ac30de6", "findings/bacdive_metal_validation--60f073d0"]
projects: ["bacdive_metal_validation"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Do metal-contaminated-site strains gain metal genes within species, not through species sorting?

Isolates from heavy-metal sites score higher on predicted metal tolerance, and the effect persists within Proteobacteria. Does it arise from extra metal-resistance genes in strains of the same species, or from contaminated sites favoring different species?

## Hypothesis

Within species that have genomes from both contaminated and non-contaminated sources, contaminated-source genomes carry more metal-resistance gene annotations. Species identity explains little of the contamination effect.

## Why it matters

It would separate recent gene gain within a species from species-level sorting, which changes how predicted metal scores should be used to flag contaminated-site organisms.

## How to test it

Label pangenome genomes by isolation source using genome metadata, and cross-check with culture-collection isolation records matched by species name (the strain table holds no genome accession). Keep species with genomes from both source classes. Count metal-resistance annotations per genome from the functional annotation table (efflux and transporter names for copper, zinc, cadmium, arsenic, mercury) and compare classes with species as a fixed effect, checking whether the contamination effect vanishes once species is included.

## What would support or refute it

Support: a within-species excess of metal-resistance annotations in contaminated-source genomes, graded from heavy-metal to industrial sources. Refute: no within-species difference, meaning the earlier signal reflects which species are isolated, or the small heavy-metal group.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Isolation, strain and pangenome tables are in the catalog, but species-name matching is partial and the number of species with both source classes was not shown.

## Builds on

- Finding: [[findings/bacdive_metal_validation--09db2bda|Heavy-metal contamination isolates score higher on predicted metal tolerance than baseline]] (Insufficient literature evidence)
- Finding: [[findings/bacdive_metal_validation--1ac30de6|Contamination signal persists within the dominant phylum Pseudomonadota]] (Extends retrieved work)
- Finding: [[findings/bacdive_metal_validation--60f073d0|Metal-tolerance score effect appears to grade with contamination category]] (Insufficient literature evidence)

## Closest published work

- [PMID 41601069](https://pubmed.ncbi.nlm.nih.gov/41601069/) Co-selection for heavy metal and multidrug resistance: Cadmium primes bacterial antibiotic resistance by enhancing intrinsic oxidative stress tolerance.
- [PMID 33540257](https://pubmed.ncbi.nlm.nih.gov/33540257/) Heavy metal pollution promotes antibiotic resistance potential in the aquatic environment.
- [PMID 37290750](https://pubmed.ncbi.nlm.nih.gov/37290750/) Genotypic and Phenotypic Characterization of Antimicrobial and Heavy Metal Tolerance in Salmonella enterica and Escherichia coli Isolates from Swine Feed Mills.

PMID 41601069 and PMID 33540257 link metal contamination to resistance at community level; this tests gene gain within species.
