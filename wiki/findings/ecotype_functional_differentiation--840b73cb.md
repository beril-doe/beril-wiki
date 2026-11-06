---
type: "Finding"
description: "Chi-square and Fisher's exact tests showed 170 of 257 species x COG tests (66.1%) were significant after BH-FDR correction (q < 0.05), and all 12 species analyzed (those with valid ecotypes) showed at least one significantly differentiated COG category."
finding_id: "ecotype_functional_differentiation--840b73cb"
result: "observation"
source: "ecotype_functional_differentiation"
quantities: [{"value": "170 of 257", "what": "species x COG tests significant after BH-FDR correction", "unit": "tests", "denominator": "257 species x COG tests", "scope": "q < 0.05"}, {"value": "66.1%", "what": "fraction of species x COG tests significant", "unit": "percent", "denominator": "257 tests", "scope": "q < 0.05"}, {"value": "12", "what": "species with at least one significantly differentiated COG category (all species analyzed)", "unit": "species", "denominator": "12 species with valid ecotypes", "scope": ""}]
caveat: "Without controlling for within-species phylogeny (e.g., using core-genome trees), adaptive ecotypes cannot be distinguished from demographic subpopulations, so differentiation may reflect phylogenetic substructure rather than ecological specialization."
first_added: "2026-10-27"
source_hash: "465628fbc1a9804913dac4212b73369f7fa168714f0ebe401719451cd96d3751"
---
# Most species-by-COG tests show ecotype differentiation, with every analyzed species affected

Chi-square and Fisher's exact tests showed 170 of 257 species x COG tests (66.1%) were significant after BH-FDR correction (q < 0.05), and all 12 species analyzed (those with valid ecotypes) showed at least one significantly differentiated COG category. [src: ecotype_functional_differentiation]

## Key figures

- **170 of 257 tests**: species x COG tests significant after BH-FDR correction (denominator 257 species x COG tests; scope q < 0.05) [src: ecotype_functional_differentiation]
- **66.1%**: fraction of species x COG tests significant (denominator 257 tests; scope q < 0.05) [src: ecotype_functional_differentiation]
- **12 species**: species with at least one significantly differentiated COG category (all species analyzed) (denominator 12 species with valid ecotypes) [src: ecotype_functional_differentiation]

## Evidence

> Chi-square and Fisher's exact tests revealed that 170 of 257 species x COG tests (66.1%) were statistically significant after BH-FDR correction (q < 0.05). All 12 species showed at least one significantly differentiated COG category, strongly rejecting H0 (that ecotype gene content variation is functionally random). [src: ecotype_functional_differentiation]

From the report [[summaries/ecotype_functional_differentiation__REPORT]].

## Caveat

Without controlling for within-species phylogeny (e.g., using core-genome trees), adaptive ecotypes cannot be distinguished from demographic subpopulations, so differentiation may reflect phylogenetic substructure rather than ecological specialization. [src: ecotype_functional_differentiation]

> - **Phylogenetic confounding**: Gene-content ecotypes may reflect phylogenetic substructure within species rather than ecological specialization. Without controlling for within-species phylogeny (e.g., using core-genome trees), we cannot distinguish adaptive ecotypes from demographic subpopulations. [src: ecotype_functional_differentiation]

## Other caveats in this report

- The report assigns 1,820 genomes across 12 species to ecotypes and invokes a prior 172-species analysis. It says these species span 6 phyla but names only four; that discrepancy is unresolved. [src: ecotype_functional_differentiation]
- The prespecified adaptive-versus-housekeeping hypothesis received only partial support; adaptive COGs were V, P, G, E, Q, M and K, while housekeeping COGs were J, F, H and C. [src: ecotype_functional_differentiation]
- Housekeeping categories also differentiated frequently, so the significance-rate contrast was modest (1.16x); adaptive effect sizes were reported as 2.1x larger (one-sided Mann–Whitney U, p = 2.53 x 10^-6). [src: ecotype_functional_differentiation]
- The report connects ecotype differentiation in category L to mobile-element genes and to a separate project's reported novel-versus-core enrichment of L (+10.88%) and V (+2.83%); this is a cross-project interpretation, not direct evidence of mechanism here. [src: ecotype_functional_differentiation]
- The large S-category effect points to an annotation gap: some ecotype-differentiating genes have unknown function. [src: ecotype_functional_differentiation]
