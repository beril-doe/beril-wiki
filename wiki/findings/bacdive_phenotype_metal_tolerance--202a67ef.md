---
type: "Finding"
description: "Urease-positive species have significantly lower metal tolerance scores (d = -0.18, p < 1e-5), opposite to the nickel-import prediction; the association is driven by Actinomycetes (d = -0.59, p < 1e-16) and disappears within Gammaproteobacteria (d = +0.08, ns) and Bacilli (d = +0.06, ns)."
finding_id: "bacdive_phenotype_metal_tolerance--202a67ef"
result: "observation"
source: "bacdive_phenotype_metal_tolerance"
quantities: [{"value": "d = -0.18", "what": "overall urease-positive association with metal score", "unit": "", "denominator": "", "scope": "p < 1e-5"}, {"value": "d = -0.59", "what": "urease association within Actinomycetes", "unit": "", "denominator": "", "scope": "p < 1e-16"}, {"value": "d = +0.08", "what": "urease association within Gammaproteobacteria", "unit": "", "denominator": "", "scope": "ns"}, {"value": "d = +0.06", "what": "urease association within Bacilli", "unit": "", "denominator": "", "scope": "ns"}]
caveat: "The report interprets the reversal as a lineage-composition effect, not evidence about nickel-specific tolerance, since urease-related nickel handling need not confer general metal tolerance."
first_added: "2026-10-27"
source_hash: "9fcabb1ca7fe2bf7740290ce37ec596ac51e60e89249679f42c9408e567a541b"
---
# Urease positivity associates with lower metal score, driven by Actinomycetes

Urease-positive species have significantly lower metal tolerance scores (d = -0.18, p < 1e-5), opposite to the nickel-import prediction; the association is driven by Actinomycetes (d = -0.59, p < 1e-16) and disappears within Gammaproteobacteria (d = +0.08, ns) and Bacilli (d = +0.06, ns). [src: bacdive_phenotype_metal_tolerance]

## Key figures

- **d = -0.18**: overall urease-positive association with metal score (scope p < 1e-5) [src: bacdive_phenotype_metal_tolerance]
- **d = -0.59**: urease association within Actinomycetes (scope p < 1e-16) [src: bacdive_phenotype_metal_tolerance]
- **d = +0.08**: urease association within Gammaproteobacteria (scope ns) [src: bacdive_phenotype_metal_tolerance]
- **d = +0.06**: urease association within Bacilli (scope ns) [src: bacdive_phenotype_metal_tolerance]

## Evidence

> Urease-positive species have significantly lower metal tolerance scores (d = -0.18, p < 1e-5), opposite to the prediction that urease positivity (requiring nickel import machinery) would confer nickel tolerance. Class-stratified analysis reveals this is driven by Actinomycetes (d = -0.59, p < 1e-16), where urease-positive species form a distinct low-metal-score subgroup. Within Gammaproteobacteria (d = +0.08, ns) and Bacilli (d = +0.06, ns), the effect disappears — further evidence of phylogenetic confounding. [src: bacdive_phenotype_metal_tolerance]

From the report [[summaries/bacdive_phenotype_metal_tolerance__REPORT]].

## Caveat

The report interprets the reversal as a lineage-composition effect, not evidence about nickel-specific tolerance, since urease-related nickel handling need not confer general metal tolerance. [src: bacdive_phenotype_metal_tolerance]

> Urease-positive bacteria require nickel import and handling machinery (Maier & Benoit 2019), so they should tolerate nickel — yet they show *lower* overall metal tolerance. This is not a true paradox: urease positivity correlates with Actinomycetes and other lineages that have fewer metal resistance genes overall. The nickel-handling machinery associated with urease is narrowly specific to nickel and does not confer general metal tolerance. Furthermore, the tight coupling between urease activity and nickel efflux (Stähler et al. 2006) means that nickel homeostasis in urease producers is a balancing act, not a broad tolerance mechanism. [src: bacdive_phenotype_metal_tolerance]

## Other caveats in this report

- Coverage varied sharply by phenotype. Each row gives BacDive strains, matched strains, and species with a metal score; species coverage ranged from 4,531 for isolation source to 422 for acetate utilization. [src: bacdive_phenotype_metal_tolerance]
- Five-fold phylogenetically blocked cross-validation used n = 3,994. R² values were 0.063 for gene count alone, 0.163 for phenotypes alone, 0.354 for taxonomy alone, 0.345 for taxonomy plus phenotypes, and 0.633 for the full model. The gene-count-only value is lower than the phenotype-only value, despite a later narrative assertion that gene content explains more variance than all phenotype features combined. [src: bacdive_phenotype_metal_tolerance]
- The dataset lacked Gram-positive Proteobacteria and Gram-negative Actinomycetes, preventing separation of Gram-stain effects from these lineage effects in prediction. [src: bacdive_phenotype_metal_tolerance]
- Metal Fitness Atlas scores are genome-based predictions, not direct tolerance measurements. Controlling for metal-cluster count only mitigates circularity; the tested associations remain phenotype-to-genome correlations. [src: bacdive_phenotype_metal_tolerance]
- The 12-organism direct validation set was underpowered and could not test the Gram-stain association within the set. [src: bacdive_phenotype_metal_tolerance]
