---
type: "Finding"
description: "In the BacDive metal-tolerance analysis, Gram-negative species have higher metal tolerance scores than Gram-positive species (Cohen's d = -0.61, p < 1e-60, n = 3,272 species), the largest effect among all phenotype features tested."
finding_id: "bacdive_phenotype_metal_tolerance--64bdb166"
result: "observation"
source: "bacdive_phenotype_metal_tolerance"
quantities: [{"value": "d = -0.61", "what": "Cohen's d, Gram-negative vs Gram-positive metal tolerance score", "unit": "", "denominator": "", "scope": "BacDive species"}, {"value": "n = 3,272 species", "what": "species with Gram stain and metal score", "unit": "", "denominator": "", "scope": ""}]
caveat: "The Gram-stain effect cannot be tested within taxonomic classes and is almost entirely a between-lineage signal (Gram-positive Actinomycetes vs Gram-negative Proteobacteria)."
first_added: "2026-11-24"
source_hash: "9fcabb1ca7fe2bf7740290ce37ec596ac51e60e89249679f42c9408e567a541b"
---
# Gram-negative species score higher on metal tolerance than Gram-positive species

In the BacDive metal-tolerance analysis, Gram-negative species have higher metal tolerance scores than Gram-positive species (Cohen's d = -0.61, p < 1e-60, n = 3,272 species), the largest effect among all phenotype features tested. [src: bacdive_phenotype_metal_tolerance]

## Key figures

- **d = -0.61**: Cohen's d, Gram-negative vs Gram-positive metal tolerance score (scope BacDive species) [src: bacdive_phenotype_metal_tolerance]
- **n = 3,272 species**: species with Gram stain and metal score [src: bacdive_phenotype_metal_tolerance]

## Evidence

> Gram-negative species have higher metal tolerance scores than Gram-positive species (Cohen's d = -0.61, p < 1e-60, n = 3,272 species). This is the largest effect among all phenotype features tested. [src: bacdive_phenotype_metal_tolerance]

From the report [[summaries/bacdive_phenotype_metal_tolerance__REPORT]].

## Caveat

The Gram-stain effect cannot be tested within taxonomic classes and is almost entirely a between-lineage signal (Gram-positive Actinomycetes vs Gram-negative Proteobacteria). [src: bacdive_phenotype_metal_tolerance]

> However, class-stratified analysis reveals the effect cannot be tested *within* taxonomic classes — it is almost entirely a between-lineage signal (Gram-positive Actinomycetes vs Gram-negative Proteobacteria). [src: bacdive_phenotype_metal_tolerance]

## Other caveats in this report

- The BacDive H₂S effect-size estimate is unreliable because there are only 8 negative controls and is likely inflated by small-sample bias. [src: bacdive_phenotype_metal_tolerance]
- The report calls BacDive H1f, predicting H₂S-producer tolerance of Zn, Cu, and Cd, unreliable (d = -0.87) because only 8 negatives likely inflate the effect by small-sample bias. [src: bacdive_phenotype_metal_tolerance]
- All Gram-typed organisms in the direct Fitness Browser–BacDive validation are Gram-negative, preventing within-set testing of H1a. [src: bacdive_phenotype_metal_tolerance]
- The single anaerobe Methanococcus in direct Fitness Browser–BacDive validation has only 1 metal tested versus 4–5 for aerobes, but the report considers n = 1 uninterpretable. [src: bacdive_phenotype_metal_tolerance]
- The matched phenotype data contain no Gram-positive Proteobacteria and no Gram-negative Actinomycetes. [src: bacdive_phenotype_metal_tolerance]
