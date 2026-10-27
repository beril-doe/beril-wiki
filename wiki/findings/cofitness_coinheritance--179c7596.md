---
type: "Finding"
description: "The report attributes the strongest pairwise signal in Ddia6719 (delta=+0.093) to sufficient accessory gene variation to detect co-inheritance despite near-clonality (ANI 99.47%)."
finding_id: "cofitness_coinheritance--179c7596"
result: "inference"
source: "cofitness_coinheritance"
quantities: [{"value": "+0.093", "what": "pairwise delta phi for Ddia6719", "unit": "phi", "denominator": "", "scope": "Ddia6719"}, {"value": "99.47%", "what": "ANI of Ddia6719", "unit": "%", "denominator": "", "scope": "Ddia6719"}]
caveat: "The high baseline phi in near-clonal species (Ddia6719, pseudo3_N2E3 with ANI 99.66%) means their absolute phi values are less interpretable."
first_added: "2026-10-27"
source_hash: "c42104325d32cf92b9baff7341246a79f8b8347e87d245d42d91303d7e98b44c"
---
# Near-clonal Ddia6719 still shows the strongest pairwise co-inheritance signal

The report attributes the strongest pairwise signal in Ddia6719 (delta=+0.093) to sufficient accessory gene variation to detect co-inheritance despite near-clonality (ANI 99.47%). [src: cofitness_coinheritance]

## Key figures

- **+0.093 phi**: pairwise delta phi for Ddia6719 (scope Ddia6719) [src: cofitness_coinheritance]
- **99.47%**: ANI of Ddia6719 (scope Ddia6719) [src: cofitness_coinheritance]

## Evidence

> The signal is strongest in Ddia6719 (delta=+0.093), which despite being near-clonal (ANI 99.47%) has sufficient accessory gene variation to detect co-inheritance. [src: cofitness_coinheritance]

From the report [[summaries/cofitness_coinheritance__REPORT]].

## Caveat

The high baseline phi in near-clonal species (Ddia6719, pseudo3_N2E3 with ANI 99.66%) means their absolute phi values are less interpretable. [src: cofitness_coinheritance]

> - **Near-clonal species behave differently**: Ddia6719 (ANI 99.47%) shows the strongest pairwise signal (delta=+0.093), while pseudo3_N2E3 (ANI 99.66%) also shows positive delta (+0.026). Despite low overall genome diversity, these species have sufficient accessory gene variation to detect co-inheritance. However, the high baseline phi in these species means the absolute phi values are less interpretable. [src: cofitness_coinheritance]

## Other caveats in this report

- Korea's negative delta is qualified by extensive undefined phi values and a small computable subset; the report interprets it as statistical noise. [src: cofitness_coinheritance]
- Nearby genomes have higher cofit-pair phi, but missing far-distance genomes limit phylogenetic control. [src: cofitness_coinheritance]
- The report explains Korea's null module result by high module core prevalence; calling Korea the best pairwise organism conflicts with its earlier negative pairwise delta. [src: cofitness_coinheritance]
- The proposed selective importance of coordinated multi-gene regulation is the report's interpretation, not a separately measured result. [src: cofitness_coinheritance]
- The report makes a cross-project assertion about 48 accessory modules from `module_conservation`; this is an attributed interpretation rather than an independently shown result of this project's analyses. [src: cofitness_coinheritance]
