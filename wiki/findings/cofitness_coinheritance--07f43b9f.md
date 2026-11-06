---
type: "Finding"
description: "Ralstonia UW163 and GMI1000 have zero co-fitness data in the Fitness Browser despite being in the organism table, so they were excluded from the primary analysis."
finding_id: "cofitness_coinheritance--07f43b9f"
result: "null result"
source: "cofitness_coinheritance"
quantities: []
caveat: "The two Ralstonia organisms are described as the most phylogenetically diverse, lowest-ANI cases, so excluding them removes the species likely most informative."
first_added: "2026-10-27"
source_hash: "c42104325d32cf92b9baff7341246a79f8b8347e87d245d42d91303d7e98b44c"
---
# Ralstonia organisms lack co-fitness data and were excluded

Ralstonia UW163 and GMI1000 have zero co-fitness data in the Fitness Browser despite being in the organism table, so they were excluded from the primary analysis. [src: cofitness_coinheritance]

## Evidence

> Ralstonia UW163 and GMI1000 have zero co-fitness data in the Fitness Browser despite being in the organism table, excluding them from the primary analysis. [src: cofitness_coinheritance]

From the report [[summaries/cofitness_coinheritance__REPORT]].

## Caveat

The two Ralstonia organisms are described as the most phylogenetically diverse, lowest-ANI cases, so excluding them removes the species likely most informative. [src: cofitness_coinheritance]

> - **Ralstonia excluded**: The two Ralstonia organisms (most phylogenetically diverse, lowest ANI) have zero co-fitness data in the Fitness Browser, excluding the species that would likely be most informative. [src: cofitness_coinheritance]

## Other caveats in this report

- Korea's negative delta is qualified by extensive undefined phi values and a small computable subset; the report interprets it as statistical noise. [src: cofitness_coinheritance]
- Nearby genomes have higher cofit-pair phi, but missing far-distance genomes limit phylogenetic control. [src: cofitness_coinheritance]
- The report explains Korea's null module result by high module core prevalence; calling Korea the best pairwise organism conflicts with its earlier negative pairwise delta. [src: cofitness_coinheritance]
- The proposed selective importance of coordinated multi-gene regulation is the report's interpretation, not a separately measured result. [src: cofitness_coinheritance]
- The report makes a cross-project assertion about 48 accessory modules from `module_conservation`; this is an attributed interpretation rather than an independently shown result of this project's analyses. [src: cofitness_coinheritance]
