---
type: "Research direction"
description: "In ADP1, quinate-specific defects fall in aromatic degradation, Complex I, iron acquisition and PQQ biosynthesis genes. Quinate dehydrogenase is a PQQ-dependent quinoprotein, which could explain the PQQ genes, but the reason for the iron-acquisition defects is unknown. Are the two defects separate cofactor demands?"
hypothesis: "PQQ-biosynthesis mutants are defective on quinate because the PQQ-dependent quinate dehydrogenase lacks its cofactor, so added PQQ rescues them but not the core aromatic pathway mutants. Iron-acquisition mutants are not rescued by PQQ; whether added iron rescues them is the open part of the question."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Deletion strains exist for ADP1, but rescue experiments are new measurements; the pangenome co-retention check uses data in the lakehouse."
collections: ["kbase-ke-pangenome"]
findings: ["aromatic_catabolism_network--8650ba38", "adp1_deletion_phenotypes--ec39f324", "adp1_deletion_phenotypes--f675f8be"]
conflicts: ["conflict--condition-space-dimensionality--aeb98adb"]
papers: ["3044290", "2855587", "15691962", "18319726"]
builds_on: ["findings/aromatic_catabolism_network--8650ba38", "findings/adp1_deletion_phenotypes--ec39f324", "findings/adp1_deletion_phenotypes--f675f8be", "conflicts/conflict--condition-space-dimensionality--aeb98adb"]
projects: ["adp1_deletion_phenotypes", "adp1_triple_essentiality", "aromatic_catabolism_network"]
topics: ["gene-fitness-landscapes-and-cofitness-modules"]
---
# Do PQQ and iron-acquisition defects on quinate reflect different cofactor demands of quinate growth?

In ADP1, quinate-specific defects fall in aromatic degradation, Complex I, iron acquisition and PQQ biosynthesis genes. Quinate dehydrogenase is a PQQ-dependent quinoprotein, which could explain the PQQ genes, but the reason for the iron-acquisition defects is unknown. Are the two defects separate cofactor demands?

## Hypothesis

PQQ-biosynthesis mutants are defective on quinate because the PQQ-dependent quinate dehydrogenase lacks its cofactor, so added PQQ rescues them but not the core aromatic pathway mutants. Iron-acquisition mutants are not rescued by PQQ; whether added iron rescues them is the open part of the question.

## Why it matters

It would show whether a 'support subsystem' signature in fitness data reflects a specific enzyme cofactor dependency, and whether the iron defect has its own cause, which explains part of why quinate behaves unlike other carbon sources.

## How to test it

Grow ADP1 deletion mutants of PQQ biosynthesis, iron acquisition and core aromatic degradation genes on quinate, with and without added PQQ or iron, and on glucose or succinate as controls. Compare rescue by mutant class. Check in the pangenome whether species carrying the aromatic pathway also keep PQQ synthesis genes.

## What would support or refute it

Support: PQQ restores quinate growth of PQQ mutants but not iron or core pathway mutants, and iron addition has a distinct effect on the iron mutants. Refute: PQQ gives no rescue of PQQ mutants, or rescues other classes too, indicating a nonspecific effect. If iron mutants stay unrescued by both, their cause remains unexplained.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Deletion strains exist for ADP1, but rescue experiments are new measurements; the pangenome co-retention check uses data in the lakehouse.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/aromatic_catabolism_network--8650ba38|Co-fitness assigns most quinate-specific genes to four support subsystems]] (Insufficient literature evidence)
- Finding: [[findings/adp1_deletion_phenotypes--ec39f324|Aromatic degradation genes form the only discrete phenotypic module]] (Extends retrieved work)
- Finding: [[findings/adp1_deletion_phenotypes--f675f8be|Carbon sources split into demanding, moderate and robust growth-defect tiers]] (Extends retrieved work)
- Conflict: [[conflicts/conflict--condition-space-dimensionality--aeb98adb|Aromatic degradation in *Acinetobacter baylyi* ADP1: substrate-specific requirement or model-input gap?]]

## Closest published work

- [PMID 3044290](https://pubmed.ncbi.nlm.nih.gov/3044290/) Bacterial NAD(P)-independent quinate dehydrogenase is a quinoprotein.
- [PMID 2855587](https://pubmed.ncbi.nlm.nih.gov/2855587/) A search for intermediates in the bacterial biosynthesis of PQQ.
- [PMID 15691962](https://pubmed.ncbi.nlm.nih.gov/15691962/) Transcriptional organization of genes for protocatechuate and quinate degradation from Acinetobacter sp. strain ADP1.
- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.

PMID 3044290 shows quinate dehydrogenase is a quinoprotein and PMID 2855587 studies PQQ biosynthesis; they do not test genome-wide whether PQQ and iron gene defects on quinate come from separate cofactor demands.
