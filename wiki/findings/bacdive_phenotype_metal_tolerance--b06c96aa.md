---
type: "Finding"
description: "The full model (taxonomy + phenotype + gene count) achieves R\u00b2 = 0.63, with gene count contributing the lion's share of the improvement over taxonomy (delta R\u00b2 = +0.28 over taxonomy alone); this is a gain within the combined model, not a standalone gene-count result."
finding_id: "bacdive_phenotype_metal_tolerance--b06c96aa"
result: "observation"
source: "bacdive_phenotype_metal_tolerance"
quantities: [{"value": "R\u00b2 = 0.63", "what": "full combined model R\u00b2", "unit": "", "denominator": "", "scope": ""}, {"value": "delta R\u00b2 = +0.28", "what": "improvement over taxonomy alone", "unit": "", "denominator": "", "scope": ""}]
caveat: "Metal Fitness Atlas scores are genome-based predictions, so gene-content predictors are partly circular despite partial-correlation control for n_metal_clusters."
first_added: "2026-11-24"
source_hash: "9fcabb1ca7fe2bf7740290ce37ec596ac51e60e89249679f42c9408e567a541b"
---
# Adding gene count to the combined model lifts R² far above taxonomy

The full model (taxonomy + phenotype + gene count) achieves R² = 0.63, with gene count contributing the lion's share of the improvement over taxonomy (delta R² = +0.28 over taxonomy alone); this is a gain within the combined model, not a standalone gene-count result. [src: bacdive_phenotype_metal_tolerance]

## Key figures

- **R² = 0.63**: full combined model R² [src: bacdive_phenotype_metal_tolerance]
- **delta R² = +0.28**: improvement over taxonomy alone [src: bacdive_phenotype_metal_tolerance]

## Evidence

> The full model (taxonomy + phenotype + gene count) achieves R² = 0.63, with gene count contributing the lion's share of the improvement over taxonomy (delta R² = +0.28 over taxonomy alone). [src: bacdive_phenotype_metal_tolerance]

From the report [[summaries/bacdive_phenotype_metal_tolerance__REPORT]].

## Caveat

Metal Fitness Atlas scores are genome-based predictions, so gene-content predictors are partly circular despite partial-correlation control for n_metal_clusters. [src: bacdive_phenotype_metal_tolerance]

> **Metal Fitness Atlas scores are genome-based predictions**, not direct metal tolerance measurements. Circular reasoning is mitigated by controlling for `n_metal_clusters` in partial correlations, but the phenotype-score associations are ultimately phenotype-to-genome correlations, not phenotype-to-phenotype. [src: bacdive_phenotype_metal_tolerance]

## Other caveats in this report

- The BacDive Gram-stain association cannot be tested within taxonomic classes and is almost entirely a between-lineage signal involving Actinomycetes versus Proteobacteria. [src: bacdive_phenotype_metal_tolerance]
- The BacDive H₂S effect-size estimate is unreliable because there are only 8 negative controls and is likely inflated by small-sample bias. [src: bacdive_phenotype_metal_tolerance]
- The report calls BacDive H1f, predicting H₂S-producer tolerance of Zn, Cu, and Cd, unreliable (d = -0.87) because only 8 negatives likely inflate the effect by small-sample bias. [src: bacdive_phenotype_metal_tolerance]
- All Gram-typed organisms in the direct Fitness Browser–BacDive validation are Gram-negative, preventing within-set testing of H1a. [src: bacdive_phenotype_metal_tolerance]
- The single anaerobe Methanococcus in direct Fitness Browser–BacDive validation has only 1 metal tested versus 4–5 for aerobes, but the report considers n = 1 uninterpretable. [src: bacdive_phenotype_metal_tolerance]
