---
type: "Research direction"
description: "The SNIPE defense domain turned up in 1,696 species across 33 phyla, yet its transporter partner was found by gene name only in E. coli K-12 among the mutant-fitness organisms. Do species carrying the domain also keep a mannose-type transporter more often than relatives lacking it?"
hypothesis: "Within genera that vary in SNIPE carriage, SNIPE-carrying species keep a ManYZ-like transporter more often than non-carriers, because the nuclease is proposed to act on phage DNA injected through that transporter."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Domain annotations are in the catalog, but the Klebsiella phage tables hold no fitness data, so the decisive SNIPE deletion test needs new mutants."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.eggnog_mapper_annotations", "kbase.ke_pangenome.genome", "kbase.ke_pangenome.gtdb_taxonomy_r214v1"]
findings: ["snipe_defense_system--5727ec31", "snipe_defense_system--69396dc3", "snipe_defense_system--792b9ec1"]
conflicts: []
papers: ["41741653", "34032565", "25015235"]
builds_on: ["findings/snipe_defense_system--5727ec31", "findings/snipe_defense_system--69396dc3", "findings/snipe_defense_system--792b9ec1"]
projects: ["snipe_defense_system"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Do SNIPE defense carriers keep a mannose-type transporter more often than relatives?

The SNIPE defense domain turned up in 1,696 species across 33 phyla, yet its transporter partner was found by gene name only in E. coli K-12 among the mutant-fitness organisms. Do species carrying the domain also keep a mannose-type transporter more often than relatives lacking it?

## Hypothesis

Within genera that vary in SNIPE carriage, SNIPE-carrying species keep a ManYZ-like transporter more often than non-carriers, because the nuclease is proposed to act on phage DNA injected through that transporter.

## Why it matters

A consistent co-retention would show the mechanism generalizes beyond E. coli and would suggest why a defense gene might be lost when its transporter is lost.

## How to test it

Using protein-domain annotations in the pangenome, mark species carrying the SNIPE diagnostic domain and detect mannose-type transporter domains in all species. Compare co-occurrence within genera using the genome taxonomy table. Then, in Klebsiella strains that carry SNIPE and an annotated ManYZ, delete SNIPE while keeping the transporter and compare phage susceptibility with the parent strain. Deleting the transporter itself blocks phage entry, so it cannot show what SNIPE adds.

## What would support or refute it

Support: SNIPE carriers retain the transporter more often within genera, and strains that lose SNIPE but keep the transporter lose protection against phages that enter through it. Refute: no co-retention within genera, or removing SNIPE leaves protection unchanged.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Domain annotations are in the catalog, but the Klebsiella phage tables hold no fitness data, so the decisive SNIPE deletion test needs new mutants.

## Builds on

- Finding: [[findings/snipe_defense_system--5727ec31|DUF4041 SNIPE domain is far more widespread than originally reported]] (Insufficient literature evidence)
- Finding: [[findings/snipe_defense_system--69396dc3|E. coli K-12 ManXYZ genes show severe fitness defects in few conditions]] (Insufficient literature evidence)
- Finding: [[findings/snipe_defense_system--792b9ec1|PhageFoundry has no Klebsiella fitness tables to test SNIPE–ManYZ interplay]] (Insufficient literature evidence)

## Closest published work

- [PMID 41741653](https://pubmed.ncbi.nlm.nih.gov/41741653/) A membrane-bound nuclease directly cleaves phage DNA during genome injection.
- [PMID 34032565](https://pubmed.ncbi.nlm.nih.gov/34032565/) Sustained coevolution of phage Lambda and Escherichia coli involves inner- as well as outer-membrane defences and counter-defences.
- [PMID 25015235](https://pubmed.ncbi.nlm.nih.gov/25015235/) A phage tail-derived element with wide distribution among both prokaryotic domains: a comparative genomic and phylogenetic study.

PMID 41741653 describes the membrane nuclease cleaving injected phage DNA; this asks whether transporter co-retention extends across bacteria.
