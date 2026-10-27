---
type: "Finding"
description: "PCA + KMeans clustering on auxiliary gene presence/absence matrices identified valid gene-content ecotypes in 12 of 15 sampled species (80%), averaging 3.7 ecotypes each (range: 2--6), with a mean silhouette score of 0.215 (median: 0.174)."
finding_id: "ecotype_functional_differentiation--7fe6d42b"
result: "observation"
source: "ecotype_functional_differentiation"
quantities: [{"value": "12 of 15", "what": "sampled species with valid gene-content ecotypes", "unit": "species", "denominator": "15 sampled species", "scope": ""}, {"value": "3.7", "what": "mean ecotypes per species (range: 2--6)", "unit": "ecotypes", "denominator": "", "scope": "12 species with valid ecotypes"}, {"value": "0.215", "what": "mean silhouette score (median: 0.174)", "unit": "", "denominator": "", "scope": ""}]
caveat: "Only 12 species from 15 sampled (80%), out of 456 eligible, contributed valid ecotypes, and the size-stratified sample may not capture phylogenetic or ecological breadth."
first_added: "2026-10-27"
source_hash: "465628fbc1a9804913dac4212b73369f7fa168714f0ebe401719451cd96d3751"
---
# Valid gene-content ecotypes found in most sampled species, with overlapping boundaries

PCA + KMeans clustering on auxiliary gene presence/absence matrices identified valid gene-content ecotypes in 12 of 15 sampled species (80%), averaging 3.7 ecotypes each (range: 2--6), with a mean silhouette score of 0.215 (median: 0.174). [src: ecotype_functional_differentiation]

## Key figures

- **12 of 15 species**: sampled species with valid gene-content ecotypes (denominator 15 sampled species) [src: ecotype_functional_differentiation]
- **3.7 ecotypes**: mean ecotypes per species (range: 2--6) (scope 12 species with valid ecotypes) [src: ecotype_functional_differentiation]
- **0.215**: mean silhouette score (median: 0.174) [src: ecotype_functional_differentiation]

## Evidence

> Ecotype clustering via PCA + KMeans on auxiliary gene presence/absence matrices identified valid gene-content ecotypes in 12 of 15 sampled species (80%). Species averaged 3.7 ecotypes each (range: 2--6), with a mean silhouette score of 0.215 (median: 0.174). The clearest ecotype separation was observed in *Erwinia amylovora* (silhouette = 0.468, 2 ecotypes) and *Bacteroides xylanisolvens* (silhouette = 0.366, 6 ecotypes). The weakest signals came from *Staphylococcus simulans* (0.118) and *Streptococcus pseudopneumoniae* (0.131). [src: ecotype_functional_differentiation]

From the report [[summaries/ecotype_functional_differentiation__REPORT]].

## Caveat

Only 12 species from 15 sampled (80%), out of 456 eligible, contributed valid ecotypes, and the size-stratified sample may not capture phylogenetic or ecological breadth. [src: ecotype_functional_differentiation]

> - **Sample size**: 12 species from 15 sampled (80%), out of 456 eligible. The stratified sample ensures representation across pangenome sizes but may not capture phylogenetic or ecological breadth. [src: ecotype_functional_differentiation]

## Other caveats in this report

- The report assigns 1,820 genomes across 12 species to ecotypes and invokes a prior 172-species analysis. It says these species span 6 phyla but names only four; that discrepancy is unresolved. [src: ecotype_functional_differentiation]
- The prespecified adaptive-versus-housekeeping hypothesis received only partial support; adaptive COGs were V, P, G, E, Q, M and K, while housekeeping COGs were J, F, H and C. [src: ecotype_functional_differentiation]
- Housekeeping categories also differentiated frequently, so the significance-rate contrast was modest (1.16x); adaptive effect sizes were reported as 2.1x larger (one-sided Mann–Whitney U, p = 2.53 x 10^-6). [src: ecotype_functional_differentiation]
- The report connects ecotype differentiation in category L to mobile-element genes and to a separate project's reported novel-versus-core enrichment of L (+10.88%) and V (+2.83%); this is a cross-project interpretation, not direct evidence of mechanism here. [src: ecotype_functional_differentiation]
- The large S-category effect points to an annotation gap: some ecotype-differentiating genes have unknown function. [src: ecotype_functional_differentiation]
