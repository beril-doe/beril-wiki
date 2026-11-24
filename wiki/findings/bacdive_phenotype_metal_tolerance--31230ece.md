---
type: "Finding"
description: "The BacDive urease effect is driven by Actinomycetes (d = -0.59, p < 1e-16), where urease-positive species form a distinct low-metal-score subgroup."
finding_id: "bacdive_phenotype_metal_tolerance--31230ece"
result: "observation"
source: "bacdive_phenotype_metal_tolerance"
quantities: [{"value": "d = -0.59", "what": "urease effect within Actinomycetes", "unit": "", "denominator": "", "scope": ""}, {"value": "p < 1e-16", "what": "significance of the Actinomycetes urease effect", "unit": "", "denominator": "", "scope": ""}]
caveat: "Metal Fitness Atlas scores are genome-based predictions, not direct metal tolerance measurements, so the associations are phenotype-to-genome correlations."
first_added: "2026-11-24"
source_hash: "9fcabb1ca7fe2bf7740290ce37ec596ac51e60e89249679f42c9408e567a541b"
---
# Reversed urease effect is driven by Actinomycetes

The BacDive urease effect is driven by Actinomycetes (d = -0.59, p < 1e-16), where urease-positive species form a distinct low-metal-score subgroup. [src: bacdive_phenotype_metal_tolerance]

## Key figures

- **d = -0.59**: urease effect within Actinomycetes [src: bacdive_phenotype_metal_tolerance]
- **p < 1e-16**: significance of the Actinomycetes urease effect [src: bacdive_phenotype_metal_tolerance]

## Evidence

> Class-stratified analysis reveals this is driven by Actinomycetes (d = -0.59, p < 1e-16), where urease-positive species form a distinct low-metal-score subgroup. [src: bacdive_phenotype_metal_tolerance]

From the report [[summaries/bacdive_phenotype_metal_tolerance__REPORT]].

## Caveat

Metal Fitness Atlas scores are genome-based predictions, not direct metal tolerance measurements, so the associations are phenotype-to-genome correlations. [src: bacdive_phenotype_metal_tolerance]

> **Metal Fitness Atlas scores are genome-based predictions**, not direct metal tolerance measurements. Circular reasoning is mitigated by controlling for `n_metal_clusters` in partial correlations, but the phenotype-score associations are ultimately phenotype-to-genome correlations, not phenotype-to-phenotype. [src: bacdive_phenotype_metal_tolerance]

## Other caveats in this report

- The BacDive Gram-stain association cannot be tested within taxonomic classes and is almost entirely a between-lineage signal involving Actinomycetes versus Proteobacteria. [src: bacdive_phenotype_metal_tolerance]
- The BacDive H₂S effect-size estimate is unreliable because there are only 8 negative controls and is likely inflated by small-sample bias. [src: bacdive_phenotype_metal_tolerance]
- The report calls BacDive H1f, predicting H₂S-producer tolerance of Zn, Cu, and Cd, unreliable (d = -0.87) because only 8 negatives likely inflate the effect by small-sample bias. [src: bacdive_phenotype_metal_tolerance]
- All Gram-typed organisms in the direct Fitness Browser–BacDive validation are Gram-negative, preventing within-set testing of H1a. [src: bacdive_phenotype_metal_tolerance]
- The single anaerobe Methanococcus in direct Fitness Browser–BacDive validation has only 1 metal tested versus 4–5 for aerobes, but the report considers n = 1 uninterpretable. [src: bacdive_phenotype_metal_tolerance]
