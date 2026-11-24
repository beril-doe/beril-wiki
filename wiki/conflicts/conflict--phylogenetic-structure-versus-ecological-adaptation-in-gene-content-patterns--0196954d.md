<!-- tension-hash: 0196954d3cb84eb8 -->
# Gene-Content Similarity Tracks Phylogeny, Yet GC Content Tracks Isolation Category: An Apparent Tension

This page records an apparent tension between specific findings, not a corpus-wide disagreement. One report finds that phylogeny (shared ancestry, as encoded in a tree) dominates gene-content similarity in 60.5% of species. [src: ecotype_analysis] Another finds that within-species GC content (the fraction of guanine and cytosine bases in a genome) stays associated with isolation category in 82% of testable species after continuous phylogenetic control. [src: gc_ecotype_ecology] The two analyses use different responses (gene content versus GC) and different controls, and the source concept page does not reconcile them. It matters because readers may take either result as a general statement about phylogeny versus ecological adaptation. See [[concepts/phylogenetic-structure-versus-ecological-adaptation-in-gene-content-patterns]].

## Evidence Sides

**Side A: phylogeny dominates, and environment signal is weak or uncontrolled**

- Phylogeny dominates gene-content similarity in 60.5% of species. The median environment partial correlation (the association left after accounting for the other predictor) is 0.0025. [src: ecotype_analysis]
- Salmonella and Phenylobacterium show environment–cluster correlations that suggest ecological selection. [src: metabolic_capability_dependency] The same report says phylogenetic confounding is possible without explicit correction. [src: metabolic_capability_dependency]
- Pseudomonas lifestyle-pathway differences are reported as subtle, while the genus-level split is large. [src: pseudomonas_carbon_ecology] The lifestyle comparisons lack phylogenetic control. [src: pseudomonas_carbon_ecology]

**Side B: GC–ecology associations survive phylogenetic control**

- 82% of testable species keep significant GC–isolation-category associations under continuous phylogenetic control. [src: gc_ecotype_ecology]

## Possible Reconciliations

- **Hypothesis 1: different responses.** Gene content may be more constrained by ancestry than GC content is, so both results can hold. Neither report tests this directly.
- **Hypothesis 2: different controls.** The phylogenetic control in the GC analysis differs from the partial-correlation framework used for gene content, so the two may not measure the same quantity.
- **Hypothesis 3: uncontrolled confounding.** The Salmonella, Phenylobacterium and Pseudomonas lifestyle signals may shrink under explicit phylogenetic correction. This is untested.

## Resolving Work

- Data: the same species set with both gene-content and GC measurements. Method: apply one identical phylogenetic control to both responses. Question: does the environment effect differ by response or only by method?
- Data: the species behind the 60.5% figure. Method: rerun the gene-content test using the continuous phylogenetic control from the GC analysis. Question: does the median environment partial correlation of 0.0025 change?
- Data: Salmonella and Phenylobacterium environment–cluster correlations. Method: add explicit phylogenetic correction. Question: do the correlations persist?
- Data: Pseudomonas lifestyle comparisons within a subgenus. Method: phylogenetically controlled regression. Question: does the subtle lifestyle signal remain distinguishable from the genus-level split?
- Data: species that are testable in both analyses. Method: cross-tabulate which species are phylogeny-dominated for gene content and GC-associated. Question: do the same species show both patterns?
