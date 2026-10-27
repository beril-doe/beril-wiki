---
type: "Finding"
description: "Gram-negative species have higher metal tolerance scores than Gram-positive species (Cohen's d = -0.61, p < 1e-60, n = 3,272 species), the largest effect among phenotype features tested, but class-stratified analysis shows it cannot be tested within taxonomic classes and is almost entirely a between-lineage signal (Gram-positive Actinomycetes vs Gram-negative Proteobacteria)."
finding_id: "bacdive_phenotype_metal_tolerance--9b04bc8d"
result: "observation"
source: "bacdive_phenotype_metal_tolerance"
quantities: [{"value": "d = -0.61", "what": "Cohen's d for Gram-negative vs Gram-positive metal tolerance score", "unit": "", "denominator": "", "scope": "species"}, {"value": "3,272", "what": "species in the Gram-stain comparison", "unit": "species", "denominator": "", "scope": ""}, {"value": "p < 1e-60", "what": "significance of the Gram-stain association", "unit": "", "denominator": "", "scope": ""}]
caveat: "There are no Gram-positive Proteobacteria and no Gram-negative Actinomycetes in the data, so Gram stain is indistinguishable from being a Proteobacterium in a predictive model."
first_added: "2026-10-27"
source_hash: "9fcabb1ca7fe2bf7740290ce37ec596ac51e60e89249679f42c9408e567a541b"
---
# Gram-negative advantage is the largest effect but is a between-lineage signal

Gram-negative species have higher metal tolerance scores than Gram-positive species (Cohen's d = -0.61, p < 1e-60, n = 3,272 species), the largest effect among phenotype features tested, but class-stratified analysis shows it cannot be tested within taxonomic classes and is almost entirely a between-lineage signal (Gram-positive Actinomycetes vs Gram-negative Proteobacteria). [src: bacdive_phenotype_metal_tolerance]

## Key figures

- **d = -0.61**: Cohen's d for Gram-negative vs Gram-positive metal tolerance score (scope species) [src: bacdive_phenotype_metal_tolerance]
- **3,272 species**: species in the Gram-stain comparison [src: bacdive_phenotype_metal_tolerance]
- **p < 1e-60**: significance of the Gram-stain association [src: bacdive_phenotype_metal_tolerance]

## Evidence

> Gram-negative species have higher metal tolerance scores than Gram-positive species (Cohen's d = -0.61, p < 1e-60, n = 3,272 species). This is the largest effect among all phenotype features tested. However, class-stratified analysis reveals the effect cannot be tested *within* taxonomic classes — it is almost entirely a between-lineage signal (Gram-positive Actinomycetes vs Gram-negative Proteobacteria). The association is mechanistically plausible — the Gram-negative outer membrane provides a permeability barrier restricting metal cation uptake (Biswas et al. 2021; Paulsen et al. 1997) — but statistically confounded with phylogeny. [src: bacdive_phenotype_metal_tolerance]

From the report [[summaries/bacdive_phenotype_metal_tolerance__REPORT]].

## Caveat

There are no Gram-positive Proteobacteria and no Gram-negative Actinomycetes in the data, so Gram stain is indistinguishable from being a Proteobacterium in a predictive model. [src: bacdive_phenotype_metal_tolerance]

> 1. **Gram stain is taxonomy, not a trait**: The Gram-negative advantage in metal tolerance is real (outer membrane barrier; Paulsen et al. 1997) but indistinguishable from "being a Proteobacterium" in a predictive model. There are no Gram-positive Proteobacteria and no Gram-negative Actinomycetes in our data. [src: bacdive_phenotype_metal_tolerance]

## Other caveats in this report

- Coverage varied sharply by phenotype. Each row gives BacDive strains, matched strains, and species with a metal score; species coverage ranged from 4,531 for isolation source to 422 for acetate utilization. [src: bacdive_phenotype_metal_tolerance]
- Five-fold phylogenetically blocked cross-validation used n = 3,994. R² values were 0.063 for gene count alone, 0.163 for phenotypes alone, 0.354 for taxonomy alone, 0.345 for taxonomy plus phenotypes, and 0.633 for the full model. The gene-count-only value is lower than the phenotype-only value, despite a later narrative assertion that gene content explains more variance than all phenotype features combined. [src: bacdive_phenotype_metal_tolerance]
- The report interprets the urease reversal as a lineage-composition effect rather than evidence about nickel-specific tolerance; urease-related nickel handling need not confer general metal tolerance. [src: bacdive_phenotype_metal_tolerance]
- Metal Fitness Atlas scores are genome-based predictions, not direct tolerance measurements. Controlling for metal-cluster count only mitigates circularity; the tested associations remain phenotype-to-genome correlations. [src: bacdive_phenotype_metal_tolerance]
- The 12-organism direct validation set was underpowered and could not test the Gram-stain association within the set. [src: bacdive_phenotype_metal_tolerance]
