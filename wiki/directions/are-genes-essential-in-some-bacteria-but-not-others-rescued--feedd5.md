---
type: "Research direction"
description: "Across 48 bacteria, just over a quarter of ortholog families are essential in some organisms and dispensable in others, and a family counted as universally essential only needs to be essential wherever it occurs; only 15 families are essential in all 48 organisms. What makes the same family essential in one genome and dispensable in another?"
hypothesis: "Variable essentiality is mostly explained by the dispensable organisms having a paralog or an alternative route that covers the function. Genetic background differences unrelated to redundancy explain little."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Essentiality calls, ortholog families and genome content are in the lakehouse, but the redundancy scoring still has to be built."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["essential_genome--5e670ea8", "essential_genome--8a3a7af5", "essential_genome--876909a2"]
conflicts: []
papers: ["36097170", "33753464", "15035042", "42726091", "25894004"]
builds_on: ["findings/essential_genome--5e670ea8", "findings/essential_genome--8a3a7af5", "findings/essential_genome--876909a2"]
projects: ["essential_genome"]
topics: ["gene-fitness-landscapes-and-cofitness-modules"]
---
# Are genes essential in some bacteria but not others rescued by redundancy?

Across 48 bacteria, just over a quarter of ortholog families are essential in some organisms and dispensable in others, and a family counted as universally essential only needs to be essential wherever it occurs; only 15 families are essential in all 48 organisms. What makes the same family essential in one genome and dispensable in another?

## Hypothesis

Variable essentiality is mostly explained by the dispensable organisms having a paralog or an alternative route that covers the function. Genetic background differences unrelated to redundancy explain little.

## Why it matters

If redundancy explains it, essentiality can be predicted from genome content and the short list essential in every organism becomes a stable core. If not, essentiality depends on hidden organism-specific physiology that gene-content models will miss.

## How to test it

For variably essential families in the Fitness Browser, compare organisms where the family is essential with those where it is dispensable. Count paralogs in each genome and look for an alternative enzyme covering the same reaction. Use the Pangenome Collection to check whether the same contrast holds across strains within a species. Test the strongest candidates by deleting the paralog in a dispensable organism and checking whether essentiality appears.

## What would support or refute it

Support: dispensable organisms consistently carry extra copies or alternative routes, and removing them restores essentiality. Refute: paralog and pathway content do not differ between the groups, and essentiality does not shift after paralog removal.

## Data

Approach: analysis then experiment. Readiness: needs compute. Essentiality calls, ortholog families and genome content are in the lakehouse, but the redundancy scoring still has to be built.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/essential_genome--5e670ea8|Only a small fraction of ortholog families are universally essential]] (Insufficient literature evidence)
- Finding: [[findings/essential_genome--8a3a7af5|Fifteen gene families are essential in every organism tested]] (Extends retrieved work)
- Finding: [[findings/essential_genome--876909a2|Clade size does not predict essentiality rate; core link weak]] (Candidate novel)

## Closest published work

- [PMID 36097170](https://pubmed.ncbi.nlm.nih.gov/36097170/) A bacterial pan-genome makes gene essentiality strain-dependent and evolvable.
- [PMID 33753464](https://pubmed.ncbi.nlm.nih.gov/33753464/) Non-essential ribosomal proteins in bacteria and archaea identified using COGs.
- [PMID 15035042](https://pubmed.ncbi.nlm.nih.gov/15035042/) Comparative genomics, minimal gene-sets and the last universal common ancestor.
- [PMID 42726091](https://pubmed.ncbi.nlm.nih.gov/42726091/) Comparative essentialome analysis of six Pectobacteriaceae strains using the TNSEEK pipeline identifies conserved and strain-specific fitness determinants.
- [PMID 25894004](https://pubmed.ncbi.nlm.nih.gov/25894004/) Evolutionary Conservation of Bacterial Essential Metabolic Genes across All Bacterial Culture Media.

PMID 36097170 and PMID 42726091 describe strain-dependent essential genes within one species or family, and PMID 33753464 shows some ribosomal proteins are dispensable in some lineages. None tests redundancy as the cause across dozens of distant bacteria.
