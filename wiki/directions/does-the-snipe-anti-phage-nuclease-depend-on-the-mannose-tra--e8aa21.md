---
type: "Research direction"
description: "Across SNIPE-domain proteins, does carriage track the presence of ManYZ-type transporters, and does SNIPE protection in E. coli depend on ManYZ?"
hypothesis: "Among SNIPE-family proteins, carrier species keep a ManYZ-type transporter more often than expected from relatedness, and in E. coli, SNIPE protection against phages is lost when manYZ is deleted."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Co-occurrence and the strain scan can be computed now, but the deletion or expression strains need to be built; the lakehouse phage panel covers E. coli only and its SNIPE carriers are unconfirmed."
collections: ["kbase-ke-pangenome", "phagefoundry", "kescience-fitnessbrowser"]
findings: ["snipe_defense_system--5727ec31", "snipe_defense_system--69396dc3", "snipe_defense_system--792b9ec1", "snipe_defense_system--b2833f06"]
conflicts: []
papers: ["41741653", "34032565", "25968644"]
builds_on: ["findings/snipe_defense_system--5727ec31", "findings/snipe_defense_system--69396dc3", "findings/snipe_defense_system--792b9ec1", "findings/snipe_defense_system--b2833f06"]
projects: ["snipe_defense_system"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Does the SNIPE anti-phage nuclease depend on the mannose transporter ManYZ in E. coli?

Across SNIPE-domain proteins, does carriage track the presence of ManYZ-type transporters, and does SNIPE protection in E. coli depend on ManYZ?

## Hypothesis

Among SNIPE-family proteins, carrier species keep a ManYZ-type transporter more often than expected from relatedness, and in E. coli, SNIPE protection against phages is lost when manYZ is deleted.

## Why it matters

It would show that membrane defense nucleases are tied to their phages' entry route, and would predict which hosts SNIPE can protect.

## How to test it

Step 1, lakehouse: in the Pangenome Collection, test co-occurrence of SNIPE-domain clusters (4,572 clusters across 1,696 species; an estimated 3,675, or 80.4%, are SNIPE-family proteins, while the other ~897 may be non-SNIPE multi-domain proteins or annotation noise) with ManYZ-type transporter clusters, against relatedness-matched species. Run the full set and the estimated SNIPE-family subset separately. Check Fitness Browser data for E. coli K-12, where manX, manY and manZ show severe defects in few conditions. Scan the 188 E. coli strains in the PhageFoundry Browsers susceptibility collection for the SNIPE domain; carriers are not yet established. Step 2, experiment: in a carrier, delete manYZ and SNIPE singly and together; if none exist, express SNIPE from a plasmid with and without manYZ. Score the panel phages. Klebsiella is not tested, since panel and fitness data there do not exist.

## What would support or refute it

Supported if co-occurrence beats the relatedness-matched expectation in the SNIPE-family subset and manYZ deletion changes protection in E. coli. Refuted if co-occurrence is random and deletions have no effect. A signal in the full set but not the subset would point to annotation noise.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Co-occurrence and the strain scan can be computed now, but the deletion or expression strains need to be built; the lakehouse phage panel covers E. coli only and its SNIPE carriers are unconfirmed.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/phagefoundry|PhageFoundry Browsers]]
- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/snipe_defense_system--5727ec31|DUF4041 SNIPE domain is far more widespread than originally reported]] (Insufficient literature evidence)
- Finding: [[findings/snipe_defense_system--69396dc3|E. coli K-12 ManXYZ genes show severe fitness defects in few conditions]] (Insufficient literature evidence)
- Finding: [[findings/snipe_defense_system--792b9ec1|PhageFoundry has no Klebsiella fitness tables to test SNIPE–ManYZ interplay]] (Insufficient literature evidence)
- Finding: [[findings/snipe_defense_system--b2833f06|SNIPE-bearing species differ from others in environmental embeddings]] (Insufficient literature evidence)

## Closest published work

- [PMID 41741653](https://pubmed.ncbi.nlm.nih.gov/41741653/) A membrane-bound nuclease directly cleaves phage DNA during genome injection.
- [PMID 34032565](https://pubmed.ncbi.nlm.nih.gov/34032565/) Sustained coevolution of phage Lambda and Escherichia coli involves inner- as well as outer-membrane defences and counter-defences.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.

PMID 41741653 showed the membrane nuclease cleaves phage DNA during injection. This direction asks whether the transporter dependence holds across species and after deleting the transporter in E. coli.
