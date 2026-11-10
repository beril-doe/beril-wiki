---
type: "Research direction"
description: "Does the excess of tail, head and anti-defense modules in human-associated species reflect intact, inducible prophages or scattered domesticated remnants?"
hypothesis: "The human-associated enrichment sits in complete, contiguous prophage regions, so it reflects ongoing phage exposure and counter-defense. Domesticated remnants would instead show scattered modules in all habitats."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Genomes are available, but dedicated prophage calling has not been run on them."
collections: ["kbase-ke-pangenome", "kbase-genomes"]
findings: ["prophage_ecology--fc67e694", "prophage_ecology--9f2125cc", "prophage_ecology--d880eadf", "prophage_ecology--3c13d0b7"]
conflicts: []
papers: ["25092302", "29416123", "34232073", "40639337", "28692019"]
builds_on: ["findings/prophage_ecology--fc67e694", "findings/prophage_ecology--9f2125cc", "findings/prophage_ecology--d880eadf", "findings/prophage_ecology--3c13d0b7"]
projects: ["prophage_ecology"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Are human-associated prophage tail and anti-defense modules active phages or decaying remnants?

Does the excess of tail, head and anti-defense modules in human-associated species reflect intact, inducible prophages or scattered domesticated remnants?

## Hypothesis

The human-associated enrichment sits in complete, contiguous prophage regions, so it reflects ongoing phage exposure and counter-defense. Domesticated remnants would instead show scattered modules in all habitats.

## Why it matters

It would separate an arms-race explanation from a bookkeeping artifact, and indicate whether annotation-based prophage counts can be used to infer phage pressure.

## How to test it

Run a dedicated prophage detector (geNomad or VIBRANT) on genomes from human-associated and freshwater species, matched within genus and within genome-size class. Ask whether tail, head and anti-defense genes sit in complete prophages or as isolated genes. Compare per-genome counts of intact regions and the share of anti-defense genes inside them.

## What would support or refute it

Supported if the habitat gap persists in intact prophages after matching. Refuted if it vanishes once only complete regions are counted, or if genome size alone explains it.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Genomes are available, but dedicated prophage calling has not been run on them.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-genomes|KBase Genomes]]

## Builds on

- Finding: [[findings/prophage_ecology--fc67e694|Tail, head and anti-defense modules enriched in human-associated genomes against null models]] (Insufficient literature evidence)
- Finding: [[findings/prophage_ecology--9f2125cc|Genome size dwarfs environment and phylogeny as predictor of prophage module composition]] (Insufficient literature evidence)
- Finding: [[findings/prophage_ecology--d880eadf|Prophage-associated gene clusters occur in every surveyed species, with modules varying]] (Insufficient literature evidence)
- Finding: [[findings/prophage_ecology--3c13d0b7|No individual TerL lineage shows environment-specific enrichment beyond host phylogeny]] (Insufficient literature evidence)

## Closest published work

- [PMID 25092302](https://pubmed.ncbi.nlm.nih.gov/25092302/) Pervasive domestication of defective prophages by bacteria.
- [PMID 29416123](https://pubmed.ncbi.nlm.nih.gov/29416123/) Lysogeny is prevalent and widely distributed in the murine gut microbiota.
- [PMID 34232073](https://pubmed.ncbi.nlm.nih.gov/34232073/) Distribution of Antimicrobial Resistance and Virulence Genes within the Prophage-Associated Regions in Nosocomial Pathogens.
- [PMID 40639337](https://pubmed.ncbi.nlm.nih.gov/40639337/) Bacteriophage genomes encode both broad and specific counter-defense repertoires to overcome bacterial defense systems.
- [PMID 28692019](https://pubmed.ncbi.nlm.nih.gov/28692019/) Bacteriophage evolution differs by host, lifestyle and genome.

PMID 25092302 showed pervasive domestication of defective prophages, and PMID 40639337 described phage counter-defense repertoires. Neither compares intact versus remnant modules between habitats.
