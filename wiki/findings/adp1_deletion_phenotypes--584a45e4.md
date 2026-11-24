---
type: "Finding"
description: "In the ADP1 deletion collection, urea is the most demanding condition, with 97.9% of genes showing severe defects at ratio < 0.5."
finding_id: "adp1_deletion_phenotypes--584a45e4"
result: "observation"
source: "adp1_deletion_phenotypes"
quantities: [{"value": "97.9%", "what": "genes with severe growth defects on urea", "unit": "%", "denominator": "genes in the matrix", "scope": "ratio < 0.5"}]
caveat: "Growth ratios are single-timepoint measurements with unknown technical noise, and the specificity analysis assumes across-condition variation reflects biology, not measurement error."
first_added: "2026-11-24"
source_hash: "7d40ea0a5c21fdf6e9852ab3cc9628a50905fba2ddb532cd9dc5aa24117bb6f0"
---
# Urea is by far the most demanding carbon-source condition in ADP1 deletions

In the ADP1 deletion collection, urea is the most demanding condition, with 97.9% of genes showing severe defects at ratio < 0.5. [src: adp1_deletion_phenotypes]

## Key figures

- **97.9%**: genes with severe growth defects on urea (denominator genes in the matrix; scope ratio < 0.5) [src: adp1_deletion_phenotypes]

## Evidence

> Urea is the most demanding (97.9% of genes show severe defects at ratio < 0.5), while quinate is the most robust (only 1.6% defective). [src: adp1_deletion_phenotypes]

From the report [[summaries/adp1_deletion_phenotypes__REPORT]].

## Caveat

Growth ratios are single-timepoint measurements with unknown technical noise, and the specificity analysis assumes across-condition variation reflects biology, not measurement error. [src: adp1_deletion_phenotypes]

> Growth ratios are single-timepoint measurements with unknown technical noise. The condition specificity analysis assumes that variation across conditions reflects biology, not measurement error. [src: adp1_deletion_phenotypes]

## Other caveats in this report

- The report suggests that the difference between Acinetobacter baylyi ADP1 and Escherichia coli module structure may reflect deletion versus chemical perturbation methods or greater interconnectedness of ADP1 metabolism. [src: adp1_deletion_phenotypes]
- The complete Acinetobacter baylyi ADP1 matrix (2,034 genes) excludes essential genes (499) and genes with incomplete data (316), biasing it toward dispensable genes with successful deletion mutants. [src: adp1_deletion_phenotypes]
- Only 8 carbon sources were tested in Acinetobacter baylyi ADP1, so the ~5 independent dimensions may increase with additional conditions. [src: adp1_deletion_phenotypes]
- The Acinetobacter baylyi ADP1 analysis uses core/accessory status from the KBase Data Lakehouse species-level Acinetobacter baylyi pangenome, which may have limited resolution compared with population-level analysis. [src: adp1_deletion_phenotypes]
