---
type: "Research direction"
description: "Does the soil and sediment excess of xoxF persist when only close relatives are compared, so that it cannot be explained by which lineages happen to live in soil?"
hypothesis: "Within genera that contain both soil/sediment and non-soil genomes, soil-derived genomes carry xoxF more often than their non-soil relatives, and inferred gain events fall more often on soil branches."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Genome and habitat data are in the lakehouse, but the within-genus tree building and gain/loss reconstruction need new computation."
collections: ["kbase-ke-pangenome", "nmdc-ncbi-biosamples"]
findings: ["lanthanide_methylotrophy_atlas--73b82896", "lanthanide_methylotrophy_atlas--4129a02d"]
conflicts: []
papers: ["38369453", "32341564", "42678158"]
builds_on: ["findings/lanthanide_methylotrophy_atlas--73b82896", "findings/lanthanide_methylotrophy_atlas--4129a02d"]
projects: ["lanthanide_methylotrophy_atlas"]
topics: ["lanthanide-dependent-methylotrophy"]
---
# Is soil habitat associated with xoxF gain inside single lineages, beyond lineage makeup?

Does the soil and sediment excess of xoxF persist when only close relatives are compared, so that it cannot be explained by which lineages happen to live in soil?

## Hypothesis

Within genera that contain both soil/sediment and non-soil genomes, soil-derived genomes carry xoxF more often than their non-soil relatives, and inferred gain events fall more often on soil branches.

## Why it matters

A within-genus association would show that the soil signal is not only a by-product of methylotroph-rich lineages living in soil, and would justify testing selection directly. It would also show whether xoxF can serve as a habitat marker.

## How to test it

In the Pangenome Collection, take genera with genomes from both soil/sediment and other habitats, using habitat labels from NMDC BioSamples where available. Compare xoxF carriage between habitats within each genus. Build genus trees and reconstruct gain and loss to see whether gains map to soil branches. Repeat in several xoxF-carrying phyla, including Acidobacteriota, where the enrichment already survived a within-phylum comparison. Use annotations from both sources, since they disagree for xoxF. This is observational and can show association only. Selection would need a follow-up, such as lanthanide-limited growth of soil and non-soil relatives.

## What would support or refute it

Support: a consistent soil excess within genera across several phyla, with gains concentrated on soil branches. Refutation: the excess disappears within genera, or appears in only one or two lineages, which points to lineage composition.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Genome and habitat data are in the lakehouse, but the within-genus tree building and gain/loss reconstruction need new computation.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/nmdc-ncbi-biosamples|NMDC BioSamples]]

## Builds on

- Finding: [[findings/lanthanide_methylotrophy_atlas--73b82896|Soil enrichment of xoxF persists within Acidobacteriota]] (Candidate novel)
- Finding: [[findings/lanthanide_methylotrophy_atlas--4129a02d|xoxF dominance holds under several phylogeny-aware corrections, strongest in the mixed model]] (Insufficient literature evidence)

## Closest published work

- [PMID 38369453](https://pubmed.ncbi.nlm.nih.gov/38369453/) Weathered granites and soils harbour microbes with lanthanide-dependent methylotrophic enzymes.
- [PMID 32341564](https://pubmed.ncbi.nlm.nih.gov/32341564/) A complete domain-to-species taxonomy for Bacteria and Archaea.
- [PMID 42678158](https://pubmed.ncbi.nlm.nih.gov/42678158/) xoxF-linked methanol oxidation signals recur across wetland metagenomes.

PMID 38369453 found xoxF gene clusters in Acidobacteria and other phyla from weathered granite and soil but did not test habitat against lineage; this asks whether habitat is associated with xoxF within lineages.
