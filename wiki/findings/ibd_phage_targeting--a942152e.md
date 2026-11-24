---
type: "Finding"
description: "A classifier trained on {HC/IBD status, sex, age} achieves macro AUC 0.80 on pooled cross-validation but only 41 % patient-level agreement with the metagenomic projection on UC Davis."
finding_id: "ibd_phage_targeting--a942152e"
result: "observation"
source: "ibd_phage_targeting"
quantities: [{"value": "0.80", "what": "macro AUC in pooled cross-validation", "unit": "AUC", "denominator": "", "scope": "pooled cross-validation"}, {"value": "41 %", "what": "patient-level agreement with metagenomic projection", "unit": "%", "denominator": "", "scope": "UC Davis"}]
caveat: "The classifier collapses to an IBD-implies-one-ecotype rule because is_ibd is dominant and constant on the test cohort, so metagenomics remains required for patient-level ecotype assignment in an all-CD cohort."
first_added: "2026-11-24"
source_hash: "7bb70c12c17426e8c3553768511907d214bbcaa696a58e3a283e6ad8dd52ff53"
---
# Clinical covariates cannot substitute for metagenomics in assigning ecotypes

A classifier trained on {HC/IBD status, sex, age} achieves macro AUC 0.80 on pooled cross-validation but only 41 % patient-level agreement with the metagenomic projection on UC Davis. [src: ibd_phage_targeting]

## Key figures

- **0.80 AUC**: macro AUC in pooled cross-validation (scope pooled cross-validation) [src: ibd_phage_targeting]
- **41 %**: patient-level agreement with metagenomic projection (scope UC Davis) [src: ibd_phage_targeting]

## Evidence

> A classifier trained on {HC/IBD status, sex, age} achieves macro AUC 0.80 on pooled cross-validation — but only 41 % patient-level agreement with the metagenomic projection on UC Davis. [src: ibd_phage_targeting]

From the report [[summaries/ibd_phage_targeting__REPORT]].

## Caveat

The classifier collapses to an IBD-implies-one-ecotype rule because is_ibd is dominant and constant on the test cohort, so metagenomics remains required for patient-level ecotype assignment in an all-CD cohort. [src: ibd_phage_targeting]

> The classifier collapses to "IBD → E1" because `is_ibd` is the dominant feature and becomes constant on the test cohort. **Metagenomics remains required for patient-level ecotype assignment in an all-CD cohort.** [src: ibd_phage_targeting]

## Other caveats in this report

- The report identifies only temperate phage evidence for M. gnavus, comprising 6 phages. [src: ibd_phage_targeting]
- H. hathewayi and F. plautii are phage-coverage-gap species in the actionable Tier-A set. [src: ibd_phage_targeting]
- The NB13 5-phage E. coli cocktail is directly applicable to only ~8/23 UC Davis patients. [src: ibd_phage_targeting]
- External INPHARED and IMG/VR queries and multi-cohort prospective validation remain out-of-scope clinical-translation prerequisites. [src: ibd_phage_targeting]
- The ecotype framework has real cross-study variance despite Tier-A external replication. [src: ibd_phage_targeting]
