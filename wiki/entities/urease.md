---
type: "Gene_Or_Pathway"
description: "Nickel-dependent urease enzyme and its ureA–ureG subunit and accessory gene cluster, covering growth on urea and its use as a metal-tolerance predictor."
sources: ["summaries/adp1_deletion_phenotypes__REPORT.md", "summaries/bacdive_phenotype_metal_tolerance__REPORT.md", "summaries/discoveries.md"]
aliases: ["Urease gene cluster", "ureABCDEFG", "urease gene cluster"]
---
# Urease

This page covers the urease enzyme and its ureA–ureG accessory gene cluster (ureABCDEFG), including growth on urea and use as a metal-tolerance predictor. In the [[entities/acinetobacter-baylyi-adp1]] deletion collection, the urease genes are the urea-specific determinants. [src: adp1_deletion_phenotypes] Across BacDive species, urease positivity predicts lower metal tolerance, not higher. [src: bacdive_phenotype_metal_tolerance]

## Key facts

- In the ADP1 deletion collection, urea is the most demanding condition, with 97.9% of genes showing severe defects at ratio < 0.5. [src: adp1_deletion_phenotypes]
- The top urea-specific ADP1 genes are ureA, ureB, ureC, ureD, ureE, ureF and ureG. Together they are all 7 urease subunits and accessory proteins. [src: adp1_deletion_phenotypes]
- In the ADP1 growth principal component analysis (PCA), PC2 explains 12.7% of variance. It isolates urea with loading = +0.75 and separates nitrogen metabolism from carbon metabolism. [src: adp1_deletion_phenotypes]

## Urease as a metal-tolerance predictor

Urease-positive bacteria need nickel import and handling machinery, so the report expected them to tolerate nickel. [src: bacdive_phenotype_metal_tolerance] The data reversed this (hypothesis H1e). BacDive urease-positive species have lower metal tolerance scores (d = -0.18, p < 1e-5). [src: bacdive_phenotype_metal_tolerance] The univariate row gives d = -0.175, n = 3,035, p = 3.7e-06 and false discovery rate (FDR) q = 9.1e-06. [src: bacdive_phenotype_metal_tolerance] The cross-project digest repeats this result. [src: discoveries]

### Phylogenetic origin of the effect

The effect is driven by Actinomycetes (d = -0.59, p < 1e-16). Urease-positive Actinomycetes form a distinct low-metal-score subgroup. [src: bacdive_phenotype_metal_tolerance] Within Gammaproteobacteria the effect disappears (d = +0.08, ns). [src: bacdive_phenotype_metal_tolerance] It also disappears within Bacilli (d = +0.06, ns). [src: bacdive_phenotype_metal_tolerance] The report states the effect is zero within other classes. [src: bacdive_phenotype_metal_tolerance] It also describes the pangenome-scale urease effect in Gammaproteobacteria as near zero. [src: bacdive_phenotype_metal_tolerance] The report therefore calls this not a true paradox. Urease positivity correlates with Actinomycetes and other lineages that have fewer metal resistance genes. [src: bacdive_phenotype_metal_tolerance] See [[concepts/phylogenetic-confounding-of-phenotype-metal-tolerance-associations]].

In the direct [[entities/fitness-browser]]–BacDive validation, all urease-typed organisms are urease-negative, yet they are routinely tested against nickel. The report calls this consistent with urease status not predicting metal tolerance at pangenome scale. [src: bacdive_phenotype_metal_tolerance]

### Proposed interpretation

The report proposes that urease-associated nickel handling is narrowly nickel-specific and gives no general metal tolerance. [src: bacdive_phenotype_metal_tolerance] It also proposes that nickel homeostasis in urease producers is a balancing act, not a broad tolerance mechanism, because urease activity is tightly coupled to nickel efflux. [src: bacdive_phenotype_metal_tolerance] These are interpretations and were not tested directly.

## Open directions

- The report proposes per-metal fitness profiling of urease+ versus urease- bacteria from the same taxonomic class, ideally Gammaproteobacteria. This would test whether urease+ organisms are nickel-specifically tolerant. [src: bacdive_phenotype_metal_tolerance]
- The report also proposes random barcode transposon sequencing (RB-TnSeq) with matched urease+/- strains under nickel versus other metals. This would directly test whether urease enables nickel-specific tolerance. [src: bacdive_phenotype_metal_tolerance]

See also [[summaries/bacdive_phenotype_metal_tolerance__REPORT]] and [[summaries/adp1_deletion_phenotypes__REPORT]].
