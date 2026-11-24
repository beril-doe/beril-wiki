---
type: "Finding"
description: "In ADP1, 625 genes (31%) have condition specificity score \u2265 1.0, indicating growth importance concentrated on one carbon source."
finding_id: "adp1_deletion_phenotypes--377fb9fe"
result: "observation"
source: "adp1_deletion_phenotypes"
quantities: [{"value": "625", "what": "genes with condition specificity score \u2265 1.0", "unit": "genes", "denominator": "", "scope": ""}, {"value": "31%", "what": "share of genes condition-specific", "unit": "%", "denominator": "", "scope": "ADP1"}]
caveat: "The complete matrix (2,034 genes) excludes essential genes (499) and genes with incomplete data (316), biasing toward dispensable genes with successful deletion mutants."
first_added: "2026-11-24"
source_hash: "7d40ea0a5c21fdf6e9852ab3cc9628a50905fba2ddb532cd9dc5aa24117bb6f0"
---
# Nearly a third of ADP1 genes are specific to one carbon source

In ADP1, 625 genes (31%) have condition specificity score ≥ 1.0, indicating growth importance concentrated on one carbon source. [src: adp1_deletion_phenotypes]

## Key figures

- **625 genes**: genes with condition specificity score ≥ 1.0 [src: adp1_deletion_phenotypes]
- **31%**: share of genes condition-specific (scope ADP1) [src: adp1_deletion_phenotypes]

## Evidence

> 625 genes (31%) have a condition specificity score ≥ 1.0, meaning their growth importance is concentrated on one carbon source. [src: adp1_deletion_phenotypes]

From the report [[summaries/adp1_deletion_phenotypes__REPORT]].

## Caveat

The complete matrix (2,034 genes) excludes essential genes (499) and genes with incomplete data (316), biasing toward dispensable genes with successful deletion mutants. [src: adp1_deletion_phenotypes]

> The complete matrix (2,034 genes) excludes essential genes (499) and genes with incomplete data (316), biasing toward dispensable genes with successful deletion mutants. [src: adp1_deletion_phenotypes]

## Other caveats in this report

- The report suggests that the difference between Acinetobacter baylyi ADP1 and Escherichia coli module structure may reflect deletion versus chemical perturbation methods or greater interconnectedness of ADP1 metabolism. [src: adp1_deletion_phenotypes]
- Acinetobacter baylyi ADP1 growth ratios are single-timepoint measurements with unknown technical noise, and the specificity analysis assumes across-condition variation is biological rather than measurement error. [src: adp1_deletion_phenotypes]
- Only 8 carbon sources were tested in Acinetobacter baylyi ADP1, so the ~5 independent dimensions may increase with additional conditions. [src: adp1_deletion_phenotypes]
- The Acinetobacter baylyi ADP1 analysis uses core/accessory status from the KBase Data Lakehouse species-level Acinetobacter baylyi pangenome, which may have limited resolution compared with population-level analysis. [src: adp1_deletion_phenotypes]
