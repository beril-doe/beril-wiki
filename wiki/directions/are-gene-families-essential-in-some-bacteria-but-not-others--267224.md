---
type: "Research direction"
description: "Of 17,222 ortholog families (groups of genes in different species descended from one ancestral gene) across 48 bacteria, 4,799 are essential in some organisms and not in others. Does a backup copy within the genome (a paralog, a related gene arising from duplication) or an alternative pathway explain why a family is essential in one organism and dispensable in another?"
hypothesis: "A family is dispensable in an organism that carries a paralog or an alternative route, and essential in organisms that lack one. This should hold after accounting for growth medium, library depth and insertion bias."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Essentiality calls and pangenome gene content are in the lakehouse. Paralog and pathway features need computing."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["essential_genome--5e670ea8", "essential_genome--8a3a7af5"]
conflicts: []
papers: ["36097170", "33753464", "42726091", "15035042"]
builds_on: ["findings/essential_genome--5e670ea8", "findings/essential_genome--8a3a7af5"]
projects: ["essential_genome"]
topics: ["gene-fitness-landscapes-and-cofitness-modules"]
---
# Are gene families essential in some bacteria but not others rescued by backup copies?

Of 17,222 ortholog families (groups of genes in different species descended from one ancestral gene) across 48 bacteria, 4,799 are essential in some organisms and not in others. Does a backup copy within the genome (a paralog, a related gene arising from duplication) or an alternative pathway explain why a family is essential in one organism and dispensable in another?

## Hypothesis

A family is dispensable in an organism that carries a paralog or an alternative route, and essential in organisms that lack one. This should hold after accounting for growth medium, library depth and insertion bias.

## Why it matters

It would show that essentiality is set by genome context, not only by gene function. That would improve essential-gene prediction and drug-target choice.

## How to test it

For the variably essential families, compare organisms where the family is essential with those where it is not. Record paralog count and completeness of alternative pathways from pathway predictions, using Fitness Browser essentiality and the Pangenome Collection. Control for the growth medium of each library, the number of transposon insertions per library, gene length and insertion bias (short genes may look essential only because they lack insertions), by matching or adding them as covariates. Check whether backup presence predicts essentiality beyond phylogenetic relatedness. Then knock down predictable cases, such as ribosomal-protein families, in an organism lacking the backup and one carrying it.

## What would support or refute it

Support: dispensability tracks backup presence, predicts it beyond relatedness and after the library controls, and knockdowns behave as predicted. Refute: backup presence is unrelated to variable essentiality once medium, depth and insertion bias are controlled, which would indicate that technical or condition differences drive the variation.

## Data

Approach: analysis then experiment. Readiness: needs compute. Essentiality calls and pangenome gene content are in the lakehouse. Paralog and pathway features need computing.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/essential_genome--5e670ea8|Only a small fraction of ortholog families are universally essential]] (Insufficient literature evidence)
- Finding: [[findings/essential_genome--8a3a7af5|Fifteen gene families are essential in every organism tested]] (Extends retrieved work)

## Closest published work

- [PMID 36097170](https://pubmed.ncbi.nlm.nih.gov/36097170/) A bacterial pan-genome makes gene essentiality strain-dependent and evolvable.
- [PMID 33753464](https://pubmed.ncbi.nlm.nih.gov/33753464/) Non-essential ribosomal proteins in bacteria and archaea identified using COGs.
- [PMID 42726091](https://pubmed.ncbi.nlm.nih.gov/42726091/) Comparative essentialome analysis of six Pectobacteriaceae strains using the TNSEEK pipeline identifies conserved and strain-specific fitness determinants.
- [PMID 15035042](https://pubmed.ncbi.nlm.nih.gov/15035042/) Comparative genomics, minimal gene-sets and the last universal common ancestor.

PMID 36097170 and PMID 42726091 describe strain-dependent essential genes within one species or family, and PMID 33753464 shows some ribosomal proteins are dispensable. None tests whether backup genes explain variable essentiality across many species.
