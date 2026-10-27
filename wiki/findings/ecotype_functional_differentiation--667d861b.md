---
type: "Finding"
description: "Mean effect size was 0.0136 for adaptive versus 0.0064 for housekeeping categories, a reported 2.13x ratio."
finding_id: "ecotype_functional_differentiation--667d861b"
result: "observation"
source: "ecotype_functional_differentiation"
quantities: [{"value": "0.0136", "what": "mean effect size, adaptive categories", "unit": "", "denominator": "", "scope": ""}, {"value": "0.0064", "what": "mean effect size, housekeeping categories", "unit": "", "denominator": "", "scope": ""}, {"value": "2.13x", "what": "ratio of adaptive to housekeeping mean effect size", "unit": "", "denominator": "", "scope": ""}]
caveat: "The significance rate difference is modest (1.16x) because housekeeping categories also differentiate in most species, though the effect-size difference is reported as 2.1x larger (p = 2.53 x 10^-6, Mann-Whitney U, one-sided)."
first_added: "2026-10-27"
source_hash: "465628fbc1a9804913dac4212b73369f7fa168714f0ebe401719451cd96d3751"
---
# Adaptive COG categories show larger mean ecotype effect sizes than housekeeping categories

Mean effect size was 0.0136 for adaptive versus 0.0064 for housekeeping categories, a reported 2.13x ratio. [src: ecotype_functional_differentiation]

## Key figures

- **0.0136**: mean effect size, adaptive categories [src: ecotype_functional_differentiation]
- **0.0064**: mean effect size, housekeeping categories [src: ecotype_functional_differentiation]
- **2.13x**: ratio of adaptive to housekeeping mean effect size [src: ecotype_functional_differentiation]

## Evidence

> | Mean effect size | 0.0136 | 0.0064 | 2.13x | [src: ecotype_functional_differentiation]

From the report [[summaries/ecotype_functional_differentiation__REPORT]].

## Caveat

The significance rate difference is modest (1.16x) because housekeeping categories also differentiate in most species, though the effect-size difference is reported as 2.1x larger (p = 2.53 x 10^-6, Mann-Whitney U, one-sided). [src: ecotype_functional_differentiation]

> The significance *rate* difference is modest (1.16x), because housekeeping categories also differentiate in most species. However, the *magnitude* of differentiation (effect size) is 2.1x larger for adaptive categories, and this difference is highly significant (p = 2.53 x 10^-6, Mann-Whitney U, one-sided). [src: ecotype_functional_differentiation]

## Other caveats in this report

- The report assigns 1,820 genomes across 12 species to ecotypes and invokes a prior 172-species analysis. It says these species span 6 phyla but names only four; that discrepancy is unresolved. [src: ecotype_functional_differentiation]
- The prespecified adaptive-versus-housekeeping hypothesis received only partial support; adaptive COGs were V, P, G, E, Q, M and K, while housekeeping COGs were J, F, H and C. [src: ecotype_functional_differentiation]
- The report connects ecotype differentiation in category L to mobile-element genes and to a separate project's reported novel-versus-core enrichment of L (+10.88%) and V (+2.83%); this is a cross-project interpretation, not direct evidence of mechanism here. [src: ecotype_functional_differentiation]
- The large S-category effect points to an annotation gap: some ecotype-differentiating genes have unknown function. [src: ecotype_functional_differentiation]
- With a mean silhouette of 0.215, the inferred ecotypes should be treated as overlapping statistical gene-content tendencies rather than sharply separated lineages. [src: ecotype_functional_differentiation]
