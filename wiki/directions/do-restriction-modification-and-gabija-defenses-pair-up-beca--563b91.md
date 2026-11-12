---
type: "Research direction"
description: "Type II restriction-modification and Gabija co-occur far more than chance, while CRISPR-Cas and CBASS are independent despite very different prevalence. Is the pairing explained by transfer on shared mobile elements, or by selection for layered defense?"
hypothesis: "Co-carriage of the two systems stays high in genomes with no called mobile elements. A strain carrying both resists a phage panel better than strains carrying either alone, beyond what the two add up to."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The genome-level co-occurrence step uses listed tables, but the phage-challenge step needs new strains and assays, and domain accessions for each system must be chosen."
databases: ["kescience.mgnify"]
tables: ["kescience.mgnify.gene_eggnog", "kescience.mgnify.gene_mobilome", "kescience.mgnify.genome"]
findings: ["phage_defense_arsenal--40a9f7b2", "phage_defense_arsenal--8c6a7f5f", "phage_defense_arsenal--47aaf35d"]
conflicts: []
papers: ["29371424", "29085076", "42464358", "38643972"]
builds_on: ["findings/phage_defense_arsenal--40a9f7b2", "findings/phage_defense_arsenal--8c6a7f5f", "findings/phage_defense_arsenal--47aaf35d"]
projects: ["phage_defense_arsenal"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Do restriction-modification and Gabija defenses pair up because of linked transfer or layered protection?

Type II restriction-modification and Gabija co-occur far more than chance, while CRISPR-Cas and CBASS are independent despite very different prevalence. Is the pairing explained by transfer on shared mobile elements, or by selection for layered defense?

## Hypothesis

Co-carriage of the two systems stays high in genomes with no called mobile elements. A strain carrying both resists a phage panel better than strains carrying either alone, beyond what the two add up to.

## Why it matters

Whether defenses stack because they are physically linked or because they complement each other bears on how bacterial immunity is assembled, and shows which pairs deserve synergy testing.

## How to test it

Step 1: in the metagenome-assembled genome catalogue, call both systems per genome from eggNOG domain hits, and compare their co-occurrence between genomes with and without called mobile elements. Linked transfer predicts weaker pairing without mobile elements. Step 2: in a tractable host, express each system alone and together, then challenge with a panel of phages and compare protection. A general domain annotation is used because an earlier annotation source missed a classical CRISPR marker.

## What would support or refute it

Support for layered selection: the pairing persists in genomes without mobile elements and the combination protects better than either system alone. Support for linked transfer: the pairing vanishes without mobile elements and the combination adds nothing.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The genome-level co-occurrence step uses listed tables, but the phage-challenge step needs new strains and assays, and domain accessions for each system must be chosen.

## Builds on

- Finding: [[findings/phage_defense_arsenal--40a9f7b2|R-M Type II and Gabija co-occur far more than the permutation null]] (Insufficient literature evidence)
- Finding: [[findings/phage_defense_arsenal--8c6a7f5f|CRISPR-Cas and CBASS are the one pair without significant co-occurrence]] (Insufficient literature evidence)
- Finding: [[findings/phage_defense_arsenal--47aaf35d|Defense-system count tracks prophage burden beyond genome size and phylum]] (Extends retrieved work)

## Closest published work

- [PMID 29371424](https://pubmed.ncbi.nlm.nih.gov/29371424/) Systematic discovery of antiphage defense systems in the microbial pangenome.
- [PMID 29085076](https://pubmed.ncbi.nlm.nih.gov/29085076/) DISARM is a widespread bacterial defence system with broad anti-phage activities.
- [PMID 42464358](https://pubmed.ncbi.nlm.nih.gov/42464358/) Interactions of antiphage defense systems in the ESKAPE pathogen plasmids.
- [PMID 38643972](https://pubmed.ncbi.nlm.nih.gov/38643972/) Defence systems and horizontal gene transfer in bacteria.

PMID 29371424 found defense systems clustered in defense islands, and PMID 42464358 studied defense interactions on plasmids; neither tests whether this specific pair co-occurs beyond mobile-element linkage or protects better together.
