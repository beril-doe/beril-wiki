---
type: "Finding"
description: "Hierarchical clustering of genes by their 8-condition growth profiles produces an optimal K = 3 with a low silhouette score (0.24); the two large modules (1,160 and 850 genes) are broad generally sensitive vs generally tolerant groups without any specific functional enrichment surviving FDR correction, which the report takes to indicate that gene essentiality varies continuously across conditions rather than falling into discrete functional categories."
finding_id: "adp1_deletion_phenotypes--86a03233"
result: "null result"
source: "adp1_deletion_phenotypes"
quantities: [{"value": "0.24", "what": "silhouette score of the K = 3 clustering", "unit": "", "denominator": "", "scope": "hierarchical clustering, 8-condition profiles"}, {"value": "1,160 and 850", "what": "genes in the two large modules", "unit": "genes", "denominator": "", "scope": ""}]
caveat: "The lack of broad discrete ADP1 modules contrasts with E. coli chemical-genetic modules (Nichols et al.), and the report only proposes, not establishes, that single-gene deletions versus chemical perturbations or more interconnected ADP1 metabolism explain this."
first_added: "2026-10-27"
source_hash: "7d40ea0a5c21fdf6e9852ab3cc9628a50905fba2ddb532cd9dc5aa24117bb6f0"
---
# Gene clustering yields no functional enrichment surviving multiple-testing correction

Hierarchical clustering of genes by their 8-condition growth profiles produces an optimal K = 3 with a low silhouette score (0.24); the two large modules (1,160 and 850 genes) are broad generally sensitive vs generally tolerant groups without any specific functional enrichment surviving FDR correction, which the report takes to indicate that gene essentiality varies continuously across conditions rather than falling into discrete functional categories. [src: adp1_deletion_phenotypes]

## Key figures

- **0.24**: silhouette score of the K = 3 clustering (scope hierarchical clustering, 8-condition profiles) [src: adp1_deletion_phenotypes]
- **1,160 and 850 genes**: genes in the two large modules [src: adp1_deletion_phenotypes]

## Evidence

> Hierarchical clustering of genes by their 8-condition growth profiles produces an optimal K = 3 with a low silhouette score (0.24). The two large modules (1,160 and 850 genes) represent broad "generally sensitive" vs "generally tolerant" groups without any specific functional enrichment surviving FDR correction. This indicates that gene essentiality varies continuously across conditions rather than falling into discrete functional categories. [src: adp1_deletion_phenotypes]

From the report [[summaries/adp1_deletion_phenotypes__REPORT]].

## Caveat

The lack of broad discrete ADP1 modules contrasts with E. coli chemical-genetic modules (Nichols et al.), and the report only proposes, not establishes, that single-gene deletions versus chemical perturbations or more interconnected ADP1 metabolism explain this. [src: adp1_deletion_phenotypes]

> - Nichols et al. (2011) found that chemical-genetic profiles in *E. coli* define "phenotypic modules" extending beyond operon boundaries. We do NOT find discrete modules in ADP1 — only a continuous gradient with one exception (the 24-gene quinate module). This may reflect differences between single-gene deletions (this study) and chemical perturbations (Nichols et al.), or may indicate that ADP1's metabolic architecture is more interconnected than *E. coli*'s. [src: adp1_deletion_phenotypes]

## Other caveats in this report

- This analysis uses single-gene deletions rather than transposon sequencing; the report compares its 625 condition-specific genes with findings from RB-TnSeq. [src: adp1_deletion_phenotypes]
- Growth ratios come from single-timepoint measurements with unknown technical noise, and condition-specificity results assume cross-condition differences are biological. [src: adp1_deletion_phenotypes]
- The 2,034-gene complete matrix excludes 499 essential genes and 316 genes with incomplete data, biasing analysis toward dispensable genes with successful deletions. [src: adp1_deletion_phenotypes]
- Only eight conditions were tested; the approximately five inferred independent dimensions may increase with a broader panel. [src: adp1_deletion_phenotypes]
- The species-level A. baylyi pangenome assignment may have less resolution than a population-level analysis. [src: adp1_deletion_phenotypes]
