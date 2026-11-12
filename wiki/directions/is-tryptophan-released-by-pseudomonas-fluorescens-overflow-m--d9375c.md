---
type: "Research direction"
description: "Tryptophan rose in the Web of Microbes exometabolome of a groundwater Pseudomonas fluorescens, yet 0 of 50 strains used it as a carbon source. Is the released tryptophan biosynthetic overflow that neighbours can use, or a by-product with no ecological role?"
hypothesis: "The Fitness Browser genes important in the tryptophan-related conditions are mainly biosynthetic and regulatory rather than catabolic. Spent medium from the producing strain restores growth of tryptophan auxotrophs from the same groundwater community."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The gene lists and pathway calls are in the lakehouse, but no spent-medium or auxotroph growth measurements exist."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome", "enigma-coral"]
findings: ["genotype_to_phenotype_enigma--602fd76d", "webofmicrobes_explorer--ab7e4ba4"]
conflicts: ["conflict--cross-tenant-data-bridging--d89b8efa"]
papers: ["30208844", "35694313", "37322284", "35592760"]
builds_on: ["findings/genotype_to_phenotype_enigma--602fd76d", "findings/webofmicrobes_explorer--ab7e4ba4", "conflicts/conflict--cross-tenant-data-bridging--d89b8efa"]
projects: ["fw300_metabolic_consistency", "genotype_to_phenotype_enigma", "webofmicrobes_explorer"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Is tryptophan released by Pseudomonas fluorescens overflow metabolism that cross-feeds auxotrophs?

Tryptophan rose in the Web of Microbes exometabolome of a groundwater Pseudomonas fluorescens, yet 0 of 50 strains used it as a carbon source. Is the released tryptophan biosynthetic overflow that neighbours can use, or a by-product with no ecological role?

## Hypothesis

The Fitness Browser genes important in the tryptophan-related conditions are mainly biosynthetic and regulatory rather than catabolic. Spent medium from the producing strain restores growth of tryptophan auxotrophs from the same groundwater community.

## Why it matters

It would show that a metabolite being produced, having fitness genes and having a complete pathway does not imply it is eaten. It would also name a concrete cross-feeding route in groundwater communities, and a rule for reading exometabolite data.

## How to test it

Step 1, lakehouse: split the 231 tryptophan-associated Fitness Browser genes of the FW300 strains by pathway role (biosynthesis, catabolism, regulation, other) using pathway-step calls from the Pangenome Collection, and by whether tryptophan was a carbon source, a nitrogen source or only present in rich medium. Step 2, experiment: grow the producer, collect spent medium, and test growth of tryptophan auxotrophs. Candidates are Oak Ridge isolates whose pathway call lacks a complete tryptophan route, or a tryptophan-deletion mutant in a reference strain. Controls are fresh medium with and without added tryptophan, and spent medium from a non-producing strain.

## What would support or refute it

Support: biosynthetic genes dominate the list, and spent medium supports auxotroph growth at a level matching added tryptophan. Refute: catabolic or transport genes dominate the list, or spent medium gives no growth beyond the non-producer control, so the released tryptophan is not available to neighbours at useful levels.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The gene lists and pathway calls are in the lakehouse, but no spent-medium or auxotroph growth measurements exist.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/enigma-coral|ENIGMA CORAL]]

## Builds on

- Finding: [[findings/genotype_to_phenotype_enigma--602fd76d|Binary growth is predictable from gene content only for some condition classes]] (Insufficient literature evidence)
- Finding: [[findings/webofmicrobes_explorer--ab7e4ba4|No organism consumption data in the archived Web of Microbes export]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--cross-tenant-data-bridging--d89b8efa|Does Genomic and Metabolic Evidence for Tryptophan Imply Measured Growth on It?]]

## Closest published work

- [PMID 30208844](https://pubmed.ncbi.nlm.nih.gov/30208844/) Web of microbes (WoM): a curated microbial exometabolomics database for linking chemistry and microbes.
- [PMID 35694313](https://pubmed.ncbi.nlm.nih.gov/35694313/) A Defined Medium for Cultivation and Exometabolite Profiling of Soil Bacteria.
- [PMID 37322284](https://pubmed.ncbi.nlm.nih.gov/37322284/) Bacteriophage-mediated lysis supports robust growth of amino acid auxotrophs.
- [PMID 35592760](https://pubmed.ncbi.nlm.nih.gov/35592760/) Dynamic proteome allocation regulates the profile of interaction of auxotrophic bacterial consortia.

PMID 30208844 and PMID 35694313 describe the exometabolomics resource and soil-bacteria medium. PMID 37322284 and PMID 35592760 study auxotroph provisioning in engineered or cultured consortia. None asks whether a natural groundwater strain's released tryptophan sustains auxotrophs while the same strains fail to grow on it.
