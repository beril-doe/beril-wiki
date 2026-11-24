---
type: "Finding"
description: "In the BacDive analysis, taxonomy alone (phylum/class/order) explains 35.4% of metal tolerance variance and phenotype features alone explain 16.3%, but combining taxonomy + phenotype yields R\u00b2 = 34.5%, slightly worse than taxonomy alone."
finding_id: "bacdive_phenotype_metal_tolerance--1dfee01c"
result: "inference"
source: "bacdive_phenotype_metal_tolerance"
quantities: [{"value": "35.4%", "what": "metal tolerance variance explained by taxonomy alone", "unit": "", "denominator": "", "scope": ""}, {"value": "16.3%", "what": "variance explained by phenotype features alone", "unit": "", "denominator": "", "scope": ""}, {"value": "34.5%", "what": "R\u00b2 of taxonomy + phenotype", "unit": "", "denominator": "", "scope": ""}]
caveat: "Metal Fitness Atlas scores are genome-based predictions, not direct metal tolerance measurements, so the associations are ultimately phenotype-to-genome correlations."
first_added: "2026-11-24"
source_hash: "9fcabb1ca7fe2bf7740290ce37ec596ac51e60e89249679f42c9408e567a541b"
---
# Taxonomy explains metal tolerance variance; phenotypes add nothing beyond it

In the BacDive analysis, taxonomy alone (phylum/class/order) explains 35.4% of metal tolerance variance and phenotype features alone explain 16.3%, but combining taxonomy + phenotype yields R² = 34.5%, slightly worse than taxonomy alone. [src: bacdive_phenotype_metal_tolerance]

## Key figures

- **35.4%**: metal tolerance variance explained by taxonomy alone [src: bacdive_phenotype_metal_tolerance]
- **16.3%**: variance explained by phenotype features alone [src: bacdive_phenotype_metal_tolerance]
- **34.5%**: R² of taxonomy + phenotype [src: bacdive_phenotype_metal_tolerance]

## Evidence

> The central finding: taxonomy alone (phylum/class/order) explains 35.4% of metal tolerance variance, and phenotype features alone explain 16.3%, but combining taxonomy + phenotype yields R² = 34.5% — slightly *worse* than taxonomy alone. [src: bacdive_phenotype_metal_tolerance]

From the report [[summaries/bacdive_phenotype_metal_tolerance__REPORT]].

## Caveat

Metal Fitness Atlas scores are genome-based predictions, not direct metal tolerance measurements, so the associations are ultimately phenotype-to-genome correlations. [src: bacdive_phenotype_metal_tolerance]

> **Metal Fitness Atlas scores are genome-based predictions**, not direct metal tolerance measurements. Circular reasoning is mitigated by controlling for `n_metal_clusters` in partial correlations, but the phenotype-score associations are ultimately phenotype-to-genome correlations, not phenotype-to-phenotype. [src: bacdive_phenotype_metal_tolerance]

## Other caveats in this report

- The BacDive Gram-stain association cannot be tested within taxonomic classes and is almost entirely a between-lineage signal involving Actinomycetes versus Proteobacteria. [src: bacdive_phenotype_metal_tolerance]
- The BacDive H₂S effect-size estimate is unreliable because there are only 8 negative controls and is likely inflated by small-sample bias. [src: bacdive_phenotype_metal_tolerance]
- The report calls BacDive H1f, predicting H₂S-producer tolerance of Zn, Cu, and Cd, unreliable (d = -0.87) because only 8 negatives likely inflate the effect by small-sample bias. [src: bacdive_phenotype_metal_tolerance]
- All Gram-typed organisms in the direct Fitness Browser–BacDive validation are Gram-negative, preventing within-set testing of H1a. [src: bacdive_phenotype_metal_tolerance]
- The single anaerobe Methanococcus in direct Fitness Browser–BacDive validation has only 1 metal tested versus 4–5 for aerobes, but the report considers n = 1 uninterpretable. [src: bacdive_phenotype_metal_tolerance]
