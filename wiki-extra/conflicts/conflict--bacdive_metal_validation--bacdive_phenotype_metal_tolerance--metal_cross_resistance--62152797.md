---
title: BacDive Coverage, Metal Association, and Core-Enrichment Estimates Do Not Align
type: Conflict
sources:
- id: bacdive_phenotype_metal_tolerance
  resource: ../../wiki/summaries/bacdive_phenotype_metal_tolerance__REPORT.md
  title: bacdive phenotype metal tolerance
- id: bacdive_metal_validation
  resource: ../../wiki/summaries/bacdive_metal_validation__REPORT.md
  title: bacdive metal validation
- id: metal_cross_resistance
  resource: ../../wiki/summaries/metal_cross_resistance__REPORT.md
  title: metal cross resistance
- id: metal_specificity
  resource: ../../wiki/summaries/metal_specificity__REPORT.md
  title: metal specificity
- id: metal_fitness_atlas
  resource: ../../wiki/summaries/metal_fitness_atlas__REPORT.md
  title: metal fitness atlas
---
<!-- tension-hash: a6ea966a0e510f6d -->
# BacDive Coverage, Metal Association, and Core-Enrichment Estimates Do Not Align

The [composite-resistance-score-limitations](../../wiki/concepts/composite-resistance-score-limitations.md) page records several disagreements between analyses that appear to study related metal-resistance questions but use different matching, aggregation, outcome, gene-set, and threshold definitions. These tensions matter because the reported estimates should not be treated as interchangeable until the underlying datasets and operational definitions are aligned.

## Evidence Sides

**Phenotype-analysis coverage**  
The phenotype analysis reports 37,368 matched strains across 5,647 GTDB species. [^bacdive_phenotype_metal_tolerance]

**Isolation-environment coverage**  
The isolation-environment analysis reports 42,227 matched strains across 6,426 GTDB species. [^bacdive_metal_validation]

**Strong composite-score association**  
The isolation-environment analysis reports a strong heavy-metal association for the composite score, with Cohen’s d = +1.00. [^bacdive_metal_validation]

**No species-scale correlation**  
The metal cross-resistance analysis reports no species-scale correlation with metal-associated isolation, with Spearman rho approximately -0.02, p > 0.8. [^metal_cross_resistance]

**Greater counter-ion overlap**  
The counter-ion analysis reports that metal-important genes overlapped with NaCl-stress genes at 39.8%. [^metal_specificity]

**Lower osmotic-stress overlap**  
The metal-specificity analysis reports that 14.7% were sick under osmotic stress. [^metal_specificity]

**Atlas core fraction**  
The genome-wide fitness atlas reports an 87.4% core fraction for broad metal-important genes. [^metal_fitness_atlas]

**Two-tier and pooled core fractions**  
The pooled core fraction for metal-specific genes was 84.8%, while the cross-resistance analysis reported 92.0%/91.0%/89.8% tiers. [^metal_specificity] [^metal_cross_resistance]

## Possible Reconciliations

- **Hypothesis—matching and filtering:** The coverage totals may differ because the phenotype and isolation-environment analyses used different matching or filtering pipelines. [^bacdive_phenotype_metal_tolerance] [^bacdive_metal_validation]
- **Hypothesis—aggregation and outcome definition:** Cohen’s d = +1.00 and Spearman rho approximately -0.02, p > 0.8 may describe different aggregation levels or metal outcomes rather than contradictory measurements of one identical association. [^bacdive_metal_validation] [^metal_cross_resistance]
- **Hypothesis—thresholds and organism sets:** The 39.8% and 14.7% overlap estimates may differ because of stricter fitness and statistical thresholds and partially different organism sets. [^metal_specificity]
- **Hypothesis—gene-set and conservation definitions:** The 87.4%, 84.8%, and 92.0%/91.0%/89.8% estimates may become more comparable under a common locus set, conservation definition, metal-specificity threshold, and non-metal control set. [^metal_fitness_atlas] [^metal_specificity] [^metal_cross_resistance]

## Resolving Work

- Rebuild a common strain-level BacDive bridge, then compare matching exclusions and filtering decisions; ask whether the totals converge.
- Analyze the same bridged strains with preregistered metal-specific outcomes at strain and species levels; ask whether the association remains Cohen’s d = +1.00 or approaches Spearman rho approximately -0.02, p > 0.8.
- Reanalyze the same organism and gene sets under matched fitness and statistical thresholds; ask whether the 39.8% and 14.7% overlap estimates converge.
- Apply one locus set, conservation definition, metal-specificity threshold, and non-metal control set; ask whether the 87.4%, 84.8%, and 92.0%/91.0%/89.8% core estimates remain distinct.

[^bacdive_phenotype_metal_tolerance]: [bacdive phenotype metal tolerance](../../wiki/summaries/bacdive_phenotype_metal_tolerance__REPORT.md)
[^bacdive_metal_validation]: [bacdive metal validation](../../wiki/summaries/bacdive_metal_validation__REPORT.md)
[^metal_cross_resistance]: [metal cross resistance](../../wiki/summaries/metal_cross_resistance__REPORT.md)
[^metal_specificity]: [metal specificity](../../wiki/summaries/metal_specificity__REPORT.md)
[^metal_fitness_atlas]: [metal fitness atlas](../../wiki/summaries/metal_fitness_atlas__REPORT.md)
