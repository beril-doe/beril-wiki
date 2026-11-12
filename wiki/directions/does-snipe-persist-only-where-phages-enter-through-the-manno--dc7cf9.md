---
type: "Research direction"
description: "The SNIPE membrane nuclease defence domain occurs across dozens of bacterial and archaeal phyla, and SNIPE-bearing species differ from others in environmental embeddings. Is its retention tied to hosts that carry the mannose transporter ManYZ, which phages use for DNA entry?"
hypothesis: "SNIPE-family proteins are retained mainly in genomes that encode ManYZ and are lost or rarer in related genomes lacking it, because the defence only has a target where phage entry goes through that transporter."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The co-occurrence analysis can use existing domain annotations, but Klebsiella has no fitness tables or phage-receptor data, so the decisive phage-challenge test needs new mutant libraries and phage screening."
collections: ["kbase-ke-pangenome", "phagefoundry", "kescience-fitnessbrowser"]
findings: ["snipe_defense_system--5727ec31", "snipe_defense_system--b2833f06", "snipe_defense_system--792b9ec1", "snipe_defense_system--69396dc3", "snipe_defense_system--a878d018"]
conflicts: []
papers: ["41741653", "34032565", "25015235", "42548023"]
builds_on: ["findings/snipe_defense_system--5727ec31", "findings/snipe_defense_system--b2833f06", "findings/snipe_defense_system--792b9ec1", "findings/snipe_defense_system--69396dc3", "findings/snipe_defense_system--a878d018"]
projects: ["snipe_defense_system"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Does SNIPE persist only where phages enter through the mannose transporter?

The SNIPE membrane nuclease defence domain occurs across dozens of bacterial and archaeal phyla, and SNIPE-bearing species differ from others in environmental embeddings. Is its retention tied to hosts that carry the mannose transporter ManYZ, which phages use for DNA entry?

## Hypothesis

SNIPE-family proteins are retained mainly in genomes that encode ManYZ and are lost or rarer in related genomes lacking it, because the defence only has a target where phage entry goes through that transporter.

## Why it matters

A coupling between a defence and one receptor would show that defence repertoires are tailored to receptor use, and would predict which hosts are protected. Absence of coupling would mean the broad phylum spread reflects other targets or mechanisms.

## How to test it

Only an estimated 80.4% of domain-positive clusters are SNIPE-family proteins, and only 54 of 4,572 show the expected nuclease domain, so first restrict to clusters with a confirmed SNIPE-type nuclease domain or a sequence-based family call and keep the domain-only set as a comparison. In the Pangenome Collection, test within genera whether SNIPE presence co-occurs with ManYZ presence. Experimentally, build transposon mutant libraries in SNIPE-carrying Klebsiella pneumoniae strains (NCTC9140 or HS11286), where no fitness data exist. Choose phages by empirical screening of a panel on manYZ-deleted versus intact hosts, since the Klebsiella browser holds genome annotations only and gives no phage-receptor data. Then test whether SNIPE loss lets ManYZ-dependent phages replicate, and whether manYZ loss makes SNIPE dispensable.

## What would support or refute it

Support: within genera, confirmed SNIPE tracks ManYZ presence, and in Klebsiella SNIPE protection against ManYZ-dependent phages disappears in manYZ-deleted hosts. Refute: SNIPE occurs equally in hosts with and without ManYZ, and protection does not depend on the transporter.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The co-occurrence analysis can use existing domain annotations, but Klebsiella has no fitness tables or phage-receptor data, so the decisive phage-challenge test needs new mutant libraries and phage screening.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/phagefoundry|PhageFoundry Browsers]]
- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/snipe_defense_system--5727ec31|DUF4041 SNIPE domain is far more widespread than originally reported]] (Insufficient literature evidence)
- Finding: [[findings/snipe_defense_system--b2833f06|SNIPE-bearing species differ from others in environmental embeddings]] (Insufficient literature evidence)
- Finding: [[findings/snipe_defense_system--792b9ec1|PhageFoundry has no Klebsiella fitness tables to test SNIPE–ManYZ interplay]] (Insufficient literature evidence)
- Finding: [[findings/snipe_defense_system--69396dc3|E. coli K-12 ManXYZ genes show severe fitness defects in few conditions]] (Insufficient literature evidence)
- Finding: [[findings/snipe_defense_system--a878d018|SNIPE nuclease is Mug113 (PF13455), not canonical GIY-YIG PF01541]] (Insufficient literature evidence)

## Closest published work

- [PMID 41741653](https://pubmed.ncbi.nlm.nih.gov/41741653/) A membrane-bound nuclease directly cleaves phage DNA during genome injection.
- [PMID 34032565](https://pubmed.ncbi.nlm.nih.gov/34032565/) Sustained coevolution of phage Lambda and Escherichia coli involves inner- as well as outer-membrane defences and counter-defences.
- [PMID 25015235](https://pubmed.ncbi.nlm.nih.gov/25015235/) A phage tail-derived element with wide distribution among both prokaryotic domains: a comparative genomic and phylogenetic study.
- [PMID 42548023](https://pubmed.ncbi.nlm.nih.gov/42548023/) Recent Advances in the Molecular Mechanisms of Bacterial Anti-Phage Defence Systems.

PMID 41741653 shows a membrane nuclease cleaving phage DNA during injection, and PMID 34032565 reports membrane-level defences in E. coli. Neither relates the defence's distribution across species to the presence of the phage-entry transporter.
