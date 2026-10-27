---
type: "Finding"
description: "Across 3,751 species with oxygen tolerance data, the anaerobe-aerobe difference in metal tolerance was negligible (d = -0.016, p = 0.55); the three-group Kruskal-Wallis test was marginally significant (H = 8.53, p = 0.014) but judged biologically trivial."
finding_id: "bacdive_phenotype_metal_tolerance--c1e60f42"
result: "null result"
source: "bacdive_phenotype_metal_tolerance"
quantities: [{"value": "d = -0.016", "what": "anaerobe-aerobe difference in metal tolerance", "unit": "", "denominator": "", "scope": "p = 0.55"}, {"value": "3,751", "what": "species with oxygen tolerance data", "unit": "species", "denominator": "", "scope": ""}, {"value": "0.221", "what": "mean score of facultative anaerobes (aerobes 0.216, anaerobes 0.215)", "unit": "", "denominator": "", "scope": ""}]
caveat: "BacDive phenotype coverage is biased toward well-studied organisms such as Pseudomonas and E. coli, with sparse data for poorly studied species."
first_added: "2026-10-27"
source_hash: "9fcabb1ca7fe2bf7740290ce37ec596ac51e60e89249679f42c9408e567a541b"
---
# Oxygen tolerance does not track metal tolerance score

Across 3,751 species with oxygen tolerance data, the anaerobe-aerobe difference in metal tolerance was negligible (d = -0.016, p = 0.55); the three-group Kruskal-Wallis test was marginally significant (H = 8.53, p = 0.014) but judged biologically trivial. [src: bacdive_phenotype_metal_tolerance]

## Key figures

- **d = -0.016**: anaerobe-aerobe difference in metal tolerance (scope p = 0.55) [src: bacdive_phenotype_metal_tolerance]
- **3,751 species**: species with oxygen tolerance data [src: bacdive_phenotype_metal_tolerance]
- **0.221**: mean score of facultative anaerobes (aerobes 0.216, anaerobes 0.215) [src: bacdive_phenotype_metal_tolerance]

## Evidence

> Despite 3,751 species with oxygen tolerance data, the anaerobe-aerobe difference in metal tolerance is negligible (d = -0.016, p = 0.55). Facultative anaerobes have the highest mean score (0.221) versus aerobes (0.216) and anaerobes (0.215). The Kruskal-Wallis test across all three groups is marginally significant (H = 8.53, p = 0.014), but the effect is biologically trivial. [src: bacdive_phenotype_metal_tolerance]

From the report [[summaries/bacdive_phenotype_metal_tolerance__REPORT]].

## Caveat

BacDive phenotype coverage is biased toward well-studied organisms such as Pseudomonas and E. coli, with sparse data for poorly studied species. [src: bacdive_phenotype_metal_tolerance]

> - **BacDive testing bias**: well-studied organisms (Pseudomonas, E. coli) have many phenotype tests; poorly-studied species have sparse data. [src: bacdive_phenotype_metal_tolerance]

## Other caveats in this report

- Coverage varied sharply by phenotype. Each row gives BacDive strains, matched strains, and species with a metal score; species coverage ranged from 4,531 for isolation source to 422 for acetate utilization. [src: bacdive_phenotype_metal_tolerance]
- Five-fold phylogenetically blocked cross-validation used n = 3,994. R² values were 0.063 for gene count alone, 0.163 for phenotypes alone, 0.354 for taxonomy alone, 0.345 for taxonomy plus phenotypes, and 0.633 for the full model. The gene-count-only value is lower than the phenotype-only value, despite a later narrative assertion that gene content explains more variance than all phenotype features combined. [src: bacdive_phenotype_metal_tolerance]
- The dataset lacked Gram-positive Proteobacteria and Gram-negative Actinomycetes, preventing separation of Gram-stain effects from these lineage effects in prediction. [src: bacdive_phenotype_metal_tolerance]
- The report interprets the urease reversal as a lineage-composition effect rather than evidence about nickel-specific tolerance; urease-related nickel handling need not confer general metal tolerance. [src: bacdive_phenotype_metal_tolerance]
- Metal Fitness Atlas scores are genome-based predictions, not direct tolerance measurements. Controlling for metal-cluster count only mitigates circularity; the tested associations remain phenotype-to-genome correlations. [src: bacdive_phenotype_metal_tolerance]
