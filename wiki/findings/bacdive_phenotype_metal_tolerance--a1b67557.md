---
type: "Finding"
description: "The overall catalase effect is d = +0.10, marginally supporting H1d, but within Actinomycetes (d = -0.62, p < 1e-5), Gammaproteobacteria (d = -0.49, p = 0.004) and Betaproteobacteria (d = -0.51, p = 0.006) catalase-negative species score higher; the report attributes the overall positive effect to between-class composition."
finding_id: "bacdive_phenotype_metal_tolerance--a1b67557"
result: "correction"
source: "bacdive_phenotype_metal_tolerance"
quantities: [{"value": "d = +0.10", "what": "overall catalase effect on metal score", "unit": "", "denominator": "", "scope": ""}, {"value": "d = -0.62", "what": "catalase effect within Actinomycetes", "unit": "", "denominator": "", "scope": "p < 1e-5"}, {"value": "d = -0.49", "what": "catalase effect within Gammaproteobacteria", "unit": "", "denominator": "", "scope": "p = 0.004"}, {"value": "d = -0.51", "what": "catalase effect within Betaproteobacteria", "unit": "", "denominator": "", "scope": "p = 0.006"}]
caveat: "Composite metal scores cannot show whether particular phenotypes predict tolerance to particular metals; testing that for the 27K species would require per-metal scores."
first_added: "2026-10-27"
source_hash: "9fcabb1ca7fe2bf7740290ce37ec596ac51e60e89249679f42c9408e567a541b"
---
# Catalase association reverses within every major class (Simpson's paradox)

The overall catalase effect is d = +0.10, marginally supporting H1d, but within Actinomycetes (d = -0.62, p < 1e-5), Gammaproteobacteria (d = -0.49, p = 0.004) and Betaproteobacteria (d = -0.51, p = 0.006) catalase-negative species score higher; the report attributes the overall positive effect to between-class composition. [src: bacdive_phenotype_metal_tolerance]

## Key figures

- **d = +0.10**: overall catalase effect on metal score [src: bacdive_phenotype_metal_tolerance]
- **d = -0.62**: catalase effect within Actinomycetes (scope p < 1e-5) [src: bacdive_phenotype_metal_tolerance]
- **d = -0.49**: catalase effect within Gammaproteobacteria (scope p = 0.004) [src: bacdive_phenotype_metal_tolerance]
- **d = -0.51**: catalase effect within Betaproteobacteria (scope p = 0.006) [src: bacdive_phenotype_metal_tolerance]

## Evidence

> 3. **Catalase exhibits Simpson's paradox**: The overall catalase effect is d = +0.10 (catalase-positive species have slightly higher metal scores), marginally supporting H1d. But class-stratified analysis reveals the *opposite* within every major class: catalase-negative species score higher within Actinomycetes (d = -0.62, p < 1e-5), Gammaproteobacteria (d = -0.49, p = 0.004), and Betaproteobacteria (d = -0.51, p = 0.006). The overall positive effect is an artifact of between-class composition — catalase-positive classes (Proteobacteria) happen to have higher metal scores than catalase-negative classes. This is the same Simpson's paradox pattern as urease, reinforcing the phylogenetic confounding narrative. [src: bacdive_phenotype_metal_tolerance]

From the report [[summaries/bacdive_phenotype_metal_tolerance__REPORT]].

## Caveat

Composite metal scores cannot show whether particular phenotypes predict tolerance to particular metals; testing that for the 27K species would require per-metal scores. [src: bacdive_phenotype_metal_tolerance]

> Test whether specific phenotypes predict tolerance to specific metals (e.g., catalase → copper, urease → nickel) rather than composite metal scores. This would require per-metal scores for the 27K species. [src: bacdive_phenotype_metal_tolerance]

## Other caveats in this report

- Coverage varied sharply by phenotype. Each row gives BacDive strains, matched strains, and species with a metal score; species coverage ranged from 4,531 for isolation source to 422 for acetate utilization. [src: bacdive_phenotype_metal_tolerance]
- Five-fold phylogenetically blocked cross-validation used n = 3,994. R² values were 0.063 for gene count alone, 0.163 for phenotypes alone, 0.354 for taxonomy alone, 0.345 for taxonomy plus phenotypes, and 0.633 for the full model. The gene-count-only value is lower than the phenotype-only value, despite a later narrative assertion that gene content explains more variance than all phenotype features combined. [src: bacdive_phenotype_metal_tolerance]
- The dataset lacked Gram-positive Proteobacteria and Gram-negative Actinomycetes, preventing separation of Gram-stain effects from these lineage effects in prediction. [src: bacdive_phenotype_metal_tolerance]
- The report interprets the urease reversal as a lineage-composition effect rather than evidence about nickel-specific tolerance; urease-related nickel handling need not confer general metal tolerance. [src: bacdive_phenotype_metal_tolerance]
- Metal Fitness Atlas scores are genome-based predictions, not direct tolerance measurements. Controlling for metal-cluster count only mitigates circularity; the tested associations remain phenotype-to-genome correlations. [src: bacdive_phenotype_metal_tolerance]
