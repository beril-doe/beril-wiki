---
type: "Finding"
description: "Clustering ADP1 growth profiles failed to find discrete functional modules (silhouette = 0.24, no enrichments survive FDR), which the report interprets as a continuous phenotype landscape."
finding_id: "adp1_deletion_phenotypes--a8d264c1"
result: "null result"
source: "adp1_deletion_phenotypes"
quantities: [{"value": "0.24", "what": "silhouette score", "unit": "", "denominator": "", "scope": ""}]
caveat: "The difference from E. coli may reflect single-gene deletions versus chemical perturbations, or a more interconnected ADP1 metabolic architecture."
first_added: "2026-11-24"
source_hash: "7d40ea0a5c21fdf6e9852ab3cc9628a50905fba2ddb532cd9dc5aa24117bb6f0"
---
# Clustering finds no discrete functional modules in ADP1 phenotypes

Clustering ADP1 growth profiles failed to find discrete functional modules (silhouette = 0.24, no enrichments survive FDR), which the report interprets as a continuous phenotype landscape. [src: adp1_deletion_phenotypes]

## Key figures

- **0.24**: silhouette score [src: adp1_deletion_phenotypes]

## Evidence

> The failure of clustering to find discrete functional modules (silhouette = 0.24, no enrichments survive FDR) is itself informative — it means the phenotype landscape is a continuum. [src: adp1_deletion_phenotypes]

From the report [[summaries/adp1_deletion_phenotypes__REPORT]].

## Caveat

The difference from E. coli may reflect single-gene deletions versus chemical perturbations, or a more interconnected ADP1 metabolic architecture. [src: adp1_deletion_phenotypes]

> This may reflect differences between single-gene deletions (this study) and chemical perturbations (Nichols et al.), or may indicate that ADP1's metabolic architecture is more interconnected than *E. coli*'s. [src: adp1_deletion_phenotypes]

## Other caveats in this report

- Acinetobacter baylyi ADP1 growth ratios are single-timepoint measurements with unknown technical noise, and the specificity analysis assumes across-condition variation is biological rather than measurement error. [src: adp1_deletion_phenotypes]
- The complete Acinetobacter baylyi ADP1 matrix (2,034 genes) excludes essential genes (499) and genes with incomplete data (316), biasing it toward dispensable genes with successful deletion mutants. [src: adp1_deletion_phenotypes]
- Only 8 carbon sources were tested in Acinetobacter baylyi ADP1, so the ~5 independent dimensions may increase with additional conditions. [src: adp1_deletion_phenotypes]
- The Acinetobacter baylyi ADP1 analysis uses core/accessory status from the KBase Data Lakehouse species-level Acinetobacter baylyi pangenome, which may have limited resolution compared with population-level analysis. [src: adp1_deletion_phenotypes]
