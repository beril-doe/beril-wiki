---
type: "Finding"
description: "Ddia6719 showed the strongest pairwise signal (delta=+0.093) despite being near-clonal (ANI 99.47%), as it has sufficient accessory gene variation to detect co-inheritance."
finding_id: "cofitness_coinheritance--179c7596"
result: "observation"
source: "cofitness_coinheritance"
quantities: [{"value": "delta=+0.093", "what": "cofit minus random delta phi", "unit": "", "denominator": "", "scope": ""}, {"value": "99.47%", "what": "ANI", "unit": "", "denominator": "", "scope": "Ddia6719"}]
caveat: "The high baseline phi in these species means the absolute phi values are less interpretable."
first_added: "2026-11-24"
source_hash: "c42104325d32cf92b9baff7341246a79f8b8347e87d245d42d91303d7e98b44c"
---
# Near-clonal Ddia6719 shows the strongest pairwise co-inheritance signal

Ddia6719 showed the strongest pairwise signal (delta=+0.093) despite being near-clonal (ANI 99.47%), as it has sufficient accessory gene variation to detect co-inheritance. [src: cofitness_coinheritance]

## Key figures

- **delta=+0.093**: cofit minus random delta phi [src: cofitness_coinheritance]
- **99.47%**: ANI (scope Ddia6719) [src: cofitness_coinheritance]

## Evidence

> The signal is strongest in Ddia6719 (delta=+0.093), which despite being near-clonal (ANI 99.47%) has sufficient accessory gene variation to detect co-inheritance. [src: cofitness_coinheritance]

From the report [[summaries/cofitness_coinheritance__REPORT]].

## Caveat

The high baseline phi in these species means the absolute phi values are less interpretable. [src: cofitness_coinheritance]

> However, the high baseline phi in these species means the absolute phi values are less interpretable. [src: cofitness_coinheritance]

## Other caveats in this report

- In Korea, 95.2% of cofit pairs had NaN phi because both genes had 100% prevalence across 72 genomes, producing zero-variance vectors. [src: cofitness_coinheritance]
- Only ~8,000 of 166,601 Korea pairs were computable, and the report attributes the negative delta to statistical noise rather than a biological signal. [src: cofitness_coinheritance]
- The report suggests that the negative co-fitness-strength association likely reflects a prevalence ceiling effect, because the strongest co-fitness pairs are core genes with near-universal prevalence and little co-occurrence variance. [src: cofitness_coinheritance]
- Most species lacked genomes in the far stratum (>0.05 branch distance), limiting separation of functional coupling from phylogenetic signal. [src: cofitness_coinheritance]
- Ralstonia UW163 and GMI1000 were excluded from primary analysis because they had zero Fitness Browser co-fitness data despite appearing in its organism table. [src: cofitness_coinheritance]
