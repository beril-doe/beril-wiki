---
type: "Finding"
description: "The report states that the 8 carbon sources partition into demanding, moderate, and robust tiers based on the fraction of genes showing growth defects; urea is the most demanding (97.9% of genes show severe defects at ratio < 0.5) and quinate the most robust (only 1.6% defective), and the tier structure is consistent across multiple thresholds."
finding_id: "adp1_deletion_phenotypes--f675f8be"
result: "observation"
source: "adp1_deletion_phenotypes"
quantities: [{"value": "97.9%", "what": "fraction of genes with severe growth defects on urea", "unit": "%", "denominator": "", "scope": "ratio < 0.5"}, {"value": "1.6%", "what": "fraction of genes defective on quinate", "unit": "%", "denominator": "", "scope": "most robust carbon source"}]
caveat: "The complete matrix (2,034 genes) excludes essential genes (499) and genes with incomplete data (316), biasing toward dispensable genes with successful deletion mutants."
first_added: "2026-10-27"
source_hash: "7d40ea0a5c21fdf6e9852ab3cc9628a50905fba2ddb532cd9dc5aa24117bb6f0"
---
# Carbon sources split into demanding, moderate and robust growth-defect tiers

The report states that the 8 carbon sources partition into demanding, moderate, and robust tiers based on the fraction of genes showing growth defects; urea is the most demanding (97.9% of genes show severe defects at ratio < 0.5) and quinate the most robust (only 1.6% defective), and the tier structure is consistent across multiple thresholds. [src: adp1_deletion_phenotypes]

## Key figures

- **97.9%**: fraction of genes with severe growth defects on urea (scope ratio < 0.5) [src: adp1_deletion_phenotypes]
- **1.6%**: fraction of genes defective on quinate (scope most robust carbon source) [src: adp1_deletion_phenotypes]

## Evidence

> The 8 carbon sources partition into demanding, moderate, and robust tiers based on the fraction of genes showing growth defects. Urea is the most demanding (97.9% of genes show severe defects at ratio < 0.5), while quinate is the most robust (only 1.6% defective). This tier structure is consistent across multiple thresholds. [src: adp1_deletion_phenotypes]

From the report [[summaries/adp1_deletion_phenotypes__REPORT]].

## Caveat

The complete matrix (2,034 genes) excludes essential genes (499) and genes with incomplete data (316), biasing toward dispensable genes with successful deletion mutants. [src: adp1_deletion_phenotypes]

> - The complete matrix (2,034 genes) excludes essential genes (499) and genes with incomplete data (316), biasing toward dispensable genes with successful deletion mutants. [src: adp1_deletion_phenotypes]

## Other caveats in this report

- The report contrasts its lack of discrete ADP1 modules, apart from the 24-gene quinate module, with published E. coli chemical-genetic modules; differing perturbation methods or organismal architecture are proposed, not established, explanations. [src: adp1_deletion_phenotypes]
- This analysis uses single-gene deletions rather than transposon sequencing; the report compares its 625 condition-specific genes with findings from RB-TnSeq. [src: adp1_deletion_phenotypes]
- Growth ratios come from single-timepoint measurements with unknown technical noise, and condition-specificity results assume cross-condition differences are biological. [src: adp1_deletion_phenotypes]
- Only eight conditions were tested; the approximately five inferred independent dimensions may increase with a broader panel. [src: adp1_deletion_phenotypes]
- The species-level A. baylyi pangenome assignment may have less resolution than a population-level analysis. [src: adp1_deletion_phenotypes]
