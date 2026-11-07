---
type: "Research direction"
description: "Are phyla with no detected PHB, such as Campylobacterota, Gemmatimonadota, Nanoarchaeota and Marinisomatota, lacking storage altogether, or have they substituted another reserve such as glycogen or polyphosphate?"
hypothesis: "Phyla without phaC retain glycogen, polyphosphate or lipid storage at rates similar to PHB-carrying phyla. The absence reflects substitution rather than loss of storage, except in genome-reduced phyla such as Patescibacteria."
approach: "lakehouse analysis"
readiness: "data in the lakehouse"
readiness_basis: "Phylum-level phaC counts exist, and alternative storage genes can be searched in the same pangenome annotations."
collections: ["kbase-ke-pangenome", "kbase-uniprot"]
findings: ["phb_granule_ecology--0215baea"]
conflicts: []
papers: ["31151997", "34322108"]
builds_on: ["findings/phb_granule_ecology--0215baea"]
projects: ["phb_granule_ecology"]
topics: ["metabolic-traits-auxotrophy-and-community-dependence"]
---
# Do phyla without PHB carry other carbon-storage systems instead?

Are phyla with no detected PHB, such as Campylobacterota, Gemmatimonadota, Nanoarchaeota and Marinisomatota, lacking storage altogether, or have they substituted another reserve such as glycogen or polyphosphate?

## Hypothesis

Phyla without phaC retain glycogen, polyphosphate or lipid storage at rates similar to PHB-carrying phyla. The absence reflects substitution rather than loss of storage, except in genome-reduced phyla such as Patescibacteria.

## Why it matters

It would show whether feast-and-famine lifestyles select for storage in general or for PHB in particular. It would also show whether PHB absence in these phyla marks genome reduction or a different strategy.

## How to test it

In the Pangenome Collection, score the storage pathways for glycogen, polyphosphate and neutral lipid across species of the PHB-absent phyla and PHB-rich phyla. Compare the share of species with any storage pathway, and test whether PHB absence goes with presence of an alternative pathway after accounting for genome size.

## What would support or refute it

Support: PHB-absent phyla show alternative storage in most species, with a rate comparable to PHB-carrying phyla. Refutation: PHB-absent phyla also lack the alternatives, especially among small genomes, which points to storage loss tied to genome reduction.

## Data

Approach: lakehouse analysis. Readiness: data in the lakehouse. Phylum-level phaC counts exist, and alternative storage genes can be searched in the same pangenome annotations.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-uniprot|UniProt Annotations]]

## Builds on

- Finding: [[findings/phb_granule_ecology--0215baea|Several major phyla have no detected PHB]] (Extends retrieved work)

## Closest published work

- [PMID 31151997](https://pubmed.ncbi.nlm.nih.gov/31151997/) Systematic Analysis of Metabolic Pathway Distributions of Bacterial Energy Reserves.
- [PMID 34322108](https://pubmed.ncbi.nlm.nih.gov/34322108/) Developing Bioprospecting Strategies for Bioplastics Through the Large-Scale Mining of Microbial Genomes.

PMID 31151997 surveys energy-reserve pathways across 8282 bacterial proteomes and links reserve loss to genome reduction. It does not ask, phylum by phylum, whether a missing PHB pathway is replaced by another reserve in genome-based species sets that include metagenome-assembled genomes.
