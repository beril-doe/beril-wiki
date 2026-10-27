---
type: "Finding"
description: "The report concludes that taxonomy alone (phylum/class/order) explains 35.4% of metal tolerance variance and phenotype features alone 16.3%, but taxonomy + phenotype yields R\u00b2 = 34.5%, slightly worse than taxonomy alone, so the phenotype signal is captured by phylogenetic structure, while adding the number of metal resistance gene clusters (n_metal_clusters) boosts the full model to R\u00b2 = 0.63."
finding_id: "bacdive_phenotype_metal_tolerance--885a4ca9"
result: "inference"
source: "bacdive_phenotype_metal_tolerance"
quantities: [{"value": "35.4%", "what": "metal tolerance variance explained by taxonomy alone (phylum/class/order)", "unit": "", "denominator": "", "scope": ""}, {"value": "16.3%", "what": "variance explained by phenotype features alone", "unit": "", "denominator": "", "scope": ""}, {"value": "34.5%", "what": "R\u00b2 for taxonomy + phenotype combined", "unit": "", "denominator": "", "scope": ""}, {"value": "0.63", "what": "R\u00b2 of the full model after adding n_metal_clusters", "unit": "", "denominator": "", "scope": ""}]
caveat: "Metal Fitness Atlas scores are genome-based predictions, not direct metal tolerance measurements, and controlling for n_metal_clusters only mitigates circularity; the associations remain phenotype-to-genome correlations."
first_added: "2026-10-27"
source_hash: "9fcabb1ca7fe2bf7740290ce37ec596ac51e60e89249679f42c9408e567a541b"
---
# Phenotype signal is absorbed by taxonomy; gene-cluster count lifts prediction

The report concludes that taxonomy alone (phylum/class/order) explains 35.4% of metal tolerance variance and phenotype features alone 16.3%, but taxonomy + phenotype yields R² = 34.5%, slightly worse than taxonomy alone, so the phenotype signal is captured by phylogenetic structure, while adding the number of metal resistance gene clusters (n_metal_clusters) boosts the full model to R² = 0.63. [src: bacdive_phenotype_metal_tolerance]

## Key figures

- **35.4%**: metal tolerance variance explained by taxonomy alone (phylum/class/order) [src: bacdive_phenotype_metal_tolerance]
- **16.3%**: variance explained by phenotype features alone [src: bacdive_phenotype_metal_tolerance]
- **34.5%**: R² for taxonomy + phenotype combined [src: bacdive_phenotype_metal_tolerance]
- **0.63**: R² of the full model after adding n_metal_clusters [src: bacdive_phenotype_metal_tolerance]

## Evidence

> The central finding: taxonomy alone (phylum/class/order) explains 35.4% of metal tolerance variance, and phenotype features alone explain 16.3%, but combining taxonomy + phenotype yields R² = 34.5% — slightly *worse* than taxonomy alone. The phenotype signal is entirely captured by phylogenetic structure. Adding the number of metal resistance gene clusters (`n_metal_clusters`) boosts the full model to R² = 0.63, demonstrating that genome-encoded metal resistance repertoire is the true predictor. [src: bacdive_phenotype_metal_tolerance]

From the report [[summaries/bacdive_phenotype_metal_tolerance__REPORT]].

## Caveat

Metal Fitness Atlas scores are genome-based predictions, not direct metal tolerance measurements, and controlling for n_metal_clusters only mitigates circularity; the associations remain phenotype-to-genome correlations. [src: bacdive_phenotype_metal_tolerance]

> - **Metal Fitness Atlas scores are genome-based predictions**, not direct metal tolerance measurements. Circular reasoning is mitigated by controlling for `n_metal_clusters` in partial correlations, but the phenotype-score associations are ultimately phenotype-to-genome correlations, not phenotype-to-phenotype. [src: bacdive_phenotype_metal_tolerance]

## Other caveats in this report

- Coverage varied sharply by phenotype. Each row gives BacDive strains, matched strains, and species with a metal score; species coverage ranged from 4,531 for isolation source to 422 for acetate utilization. [src: bacdive_phenotype_metal_tolerance]
- Five-fold phylogenetically blocked cross-validation used n = 3,994. R² values were 0.063 for gene count alone, 0.163 for phenotypes alone, 0.354 for taxonomy alone, 0.345 for taxonomy plus phenotypes, and 0.633 for the full model. The gene-count-only value is lower than the phenotype-only value, despite a later narrative assertion that gene content explains more variance than all phenotype features combined. [src: bacdive_phenotype_metal_tolerance]
- The dataset lacked Gram-positive Proteobacteria and Gram-negative Actinomycetes, preventing separation of Gram-stain effects from these lineage effects in prediction. [src: bacdive_phenotype_metal_tolerance]
- The report interprets the urease reversal as a lineage-composition effect rather than evidence about nickel-specific tolerance; urease-related nickel handling need not confer general metal tolerance. [src: bacdive_phenotype_metal_tolerance]
- The 12-organism direct validation set was underpowered and could not test the Gram-stain association within the set. [src: bacdive_phenotype_metal_tolerance]
