---
type: "Finding"
description: "Across 195 ICA modules in 6 organisms, within-module co-occurrence (mean phi=0.229) exceeds prevalence-matched null expectations (mean phi=0.177, 1000 permutations), with delta=+0.053 and 51/195 modules (26%) significant at p<0.05, and 21/195 modules (11%) remaining significant at q<0.05 after Benjamini-Hochberg FDR correction."
finding_id: "cofitness_coinheritance--0fab94f0"
result: "observation"
source: "cofitness_coinheritance"
quantities: [{"value": "+0.053", "what": "mean delta phi, within-module versus prevalence-matched null", "unit": "phi", "denominator": "195 ICA modules", "scope": "6 organisms"}, {"value": "51/195", "what": "modules significant at p<0.05", "unit": "modules", "denominator": "195 modules", "scope": "6 organisms"}, {"value": "21/195", "what": "modules significant at Benjamini-Hochberg FDR q<0.05", "unit": "modules", "denominator": "195 modules", "scope": "6 organisms"}]
caveat: "The complete per-organism table (Koxy 44 modules/14 significant, Btheta 36/22, Putida 38/6, Korea 29/0, Phaeo 37/3, pseudo3_N2E3 40/4) does not sum to the headline module and significant-module counts, and the discrepancy is unresolved."
first_added: "2026-10-27"
source_hash: "c42104325d32cf92b9baff7341246a79f8b8347e87d245d42d91303d7e98b44c"
---
# Module-level co-occurrence exceeds null, but few modules survive FDR correction

Across 195 ICA modules in 6 organisms, within-module co-occurrence (mean phi=0.229) exceeds prevalence-matched null expectations (mean phi=0.177, 1000 permutations), with delta=+0.053 and 51/195 modules (26%) significant at p<0.05, and 21/195 modules (11%) remaining significant at q<0.05 after Benjamini-Hochberg FDR correction. [src: cofitness_coinheritance]

## Key figures

- **+0.053 phi**: mean delta phi, within-module versus prevalence-matched null (denominator 195 ICA modules; scope 6 organisms) [src: cofitness_coinheritance]
- **51/195 modules**: modules significant at p<0.05 (denominator 195 modules; scope 6 organisms) [src: cofitness_coinheritance]
- **21/195 modules**: modules significant at Benjamini-Hochberg FDR q<0.05 (denominator 195 modules; scope 6 organisms) [src: cofitness_coinheritance]

## Evidence

> At the module level, 195 ICA modules across 6 organisms show within-module co-occurrence (mean phi=0.229) significantly exceeding prevalence-matched null expectations (mean phi=0.177, 1000 permutations), with delta=+0.053 and 51/195 modules (26%) significant at p<0.05. After Benjamini-Hochberg FDR correction, 21/195 modules (11%) remain significant at q<0.05. [src: cofitness_coinheritance]

From the report [[summaries/cofitness_coinheritance__REPORT]].

## Caveat

The complete per-organism table (Koxy 44 modules/14 significant, Btheta 36/22, Putida 38/6, Korea 29/0, Phaeo 37/3, pseudo3_N2E3 40/4) does not sum to the headline module and significant-module counts, and the discrepancy is unresolved. [src: cofitness_coinheritance]

> | Organism | Modules | Significant | Mean phi | Null mean | |----------|---------|-------------|----------|-----------| | Koxy | 44 | 14 (32%) | 0.079 | 0.040 | | Btheta | 36 | 22 (61%) | 0.192 | 0.086 | | Putida | 38 | 6 (16%) | 0.266 | 0.202 | | Korea | 29 | 0 (0%) | 0.357 | 0.308 | | Phaeo | 37 | 3 (8%) | 0.108 | 0.095 | | pseudo3_N2E3 | 40 | 4 (10%) | 0.444 | 0.409 | [src: cofitness_coinheritance]

## Other caveats in this report

- Korea's negative delta is qualified by extensive undefined phi values and a small computable subset; the report interprets it as statistical noise. [src: cofitness_coinheritance]
- Nearby genomes have higher cofit-pair phi, but missing far-distance genomes limit phylogenetic control. [src: cofitness_coinheritance]
- The report explains Korea's null module result by high module core prevalence; calling Korea the best pairwise organism conflicts with its earlier negative pairwise delta. [src: cofitness_coinheritance]
- The proposed selective importance of coordinated multi-gene regulation is the report's interpretation, not a separately measured result. [src: cofitness_coinheritance]
- The report makes a cross-project assertion about 48 accessory modules from `module_conservation`; this is an attributed interpretation rather than an independently shown result of this project's analyses. [src: cofitness_coinheritance]
