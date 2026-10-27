---
type: "Research direction"
description: "Do xoxF-carrying genomes lacking PQQ evidence from both eggNOG and bakta obtain PQQ from neighbours, or is the gap assembly or annotation error?"
hypothesis: "A subset of PQQ-negative xoxF genomes is genuinely PQQ-auxotrophic: it persists in complete isolate genomes after combining both annotation sources, and the strains grow on methanol only when PQQ or a PQQ-producing partner is supplied."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The genome-level screen is computable from existing annotations, but the decisive rescue growth assays need new measurements."
collections: ["kbase-ke-pangenome", "kbase-genomes", "nmdc-arkin", "enigma-coral"]
findings: ["lanthanide_methylotrophy_atlas--6465f1d3", "lanthanide_methylotrophy_atlas--4129a02d"]
conflicts: []
papers: ["29997591", "41636527", "24816778"]
builds_on: ["findings/lanthanide_methylotrophy_atlas--6465f1d3", "findings/lanthanide_methylotrophy_atlas--4129a02d"]
projects: ["lanthanide_methylotrophy_atlas"]
topics: ["lanthanide-dependent-methylotrophy"]
---
# Do xoxF carriers without PQQ depend on community-supplied cofactor?

Do xoxF-carrying genomes lacking PQQ evidence from both eggNOG and bakta obtain PQQ from neighbours, or is the gap assembly or annotation error?

## Hypothesis

A subset of PQQ-negative xoxF genomes is genuinely PQQ-auxotrophic: it persists in complete isolate genomes after combining both annotation sources, and the strains grow on methanol only when PQQ or a PQQ-producing partner is supplied.

## Why it matters

Genuine cofactor cross-feeding would make lanthanide methylotrophy a community-level trait and change how XoxF-dependent metabolism is modelled. The report notes that eggNOG and bakta calls for PQQ biosynthesis disagree substantially.

## How to test it

Identify xoxF-carrying genomes with no PQQ call from either source, using the union to remove annotation gaps. Score them for completeness and contig-end proximity and separate isolates from MAGs. Among complete isolate genomes retaining the gap, compare with PQQ-positive carriers for biosynthesis loci and candidate transporters, and check whether PQQ producers co-occur in NMDC or ENIGMA CORAL samples. Then grow a PQQ-negative isolate on methanol with and without PQQ or a producer.

## What would support or refute it

Support: persistent PQQ negativity in complete isolate genomes and methanol growth rescued by PQQ or producers. Refutation: gaps vanish with completeness or source union, or growth is unaffected by PQQ.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The genome-level screen is computable from existing annotations, but the decisive rescue growth assays need new measurements.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-genomes|KBase Genomes]]
- Collection: [[data/nmdc-arkin|NMDC Multi-omics]]
- Collection: [[data/enigma-coral|ENIGMA CORAL]]

## Builds on

- Finding: [[findings/lanthanide_methylotrophy_atlas--6465f1d3|Lanthanide-dependent xoxF vastly outnumbers calcium-dependent mxaF across a large genome collection]] (Extends retrieved work)
- Finding: [[findings/lanthanide_methylotrophy_atlas--4129a02d|xoxF dominance holds under several phylogeny-aware corrections, strongest in the mixed model]] (Insufficient literature evidence)

## Closest published work

- [PMID 29997591](https://pubmed.ncbi.nlm.nih.gov/29997591/) Lanthanide-Dependent Methanol Dehydrogenases of XoxF4 and XoxF5 Clades Are Differentially Distributed Among Methylotrophic Bacteria and They Reveal Different Biochemical Properties.
- [PMID 41636527](https://pubmed.ncbi.nlm.nih.gov/41636527/) Beneath the surface: expanding the known repertoire of methylotrophic metabolism.
- [PMID 24816778](https://pubmed.ncbi.nlm.nih.gov/24816778/) PQQ-dependent methanol dehydrogenases: rare-earth elements make a difference.

PMID 24816778 reviews PQQ-dependent dehydrogenases and PMID 41636527 expands the methylotroph repertoire, but neither tests cofactor dependence across a genome collection.
