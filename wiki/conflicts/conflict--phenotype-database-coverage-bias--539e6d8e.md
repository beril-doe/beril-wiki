<!-- tension-hash: 539e6d8e430f97db -->
# Do Within-Species Gene-Content Differences Reflect Ecological Adaptation or Lineage Structure?

Two projects in this corpus examine within-species gene-content variation and reach differently framed conclusions about what drives it. One finds that phylogeny — shared ancestry — usually dominates genome-wide gene-content similarity, with environment dominating in a substantial minority of species and significant environmental effects rare. The other finds pervasive functional differentiation between gene-content ecotypes (within-species subpopulations defined by which accessory genes they carry), but runs no phylogenetic control. The disagreement matters because it determines whether gene-content subsets observed within a species are evidence of ecological structuring or a restatement of lineage composition — the same confounder that motivates [[concepts/phenotype-database-coverage-bias]].

## Evidence Sides

**Phylogeny usually dominates, but not universally.** The ecotype analysis found that phylogeny dominated gene-content similarity in 60.5% of species, but environment dominated in 39.5%; significant environmental effects were detected in only 16 of 172 species. [src: ecotype_analysis] The denominator here is 172 species and the criterion is a significance threshold, not an effect-size ranking — so the two figures describe different things: which term is larger per species, versus how often the environmental term clears significance. This side **refines** rather than contradicts the phenotype database result: lineage is often dominant at genome-wide scale, but the nonzero environmental-dominant subset and the possibility of subset-specific adaptation caution against treating weak whole-genome environmental effects as universal evidence of no ecological structuring. [src: ecotype_analysis]

**Functional subsets differentiate, but the cause is unidentified.** The ecotype-functional study **supports** functional subset differentiation — ecotypes differ in their COG (Clusters of Orthologous Groups, a functional annotation scheme) composition — but its lack of phylogenetic controls creates a tension: COG differences may represent adaptive ecotypes or lineage-linked gene-content structure. [src: ecotype_functional_differentiation] No test in that study distinguishes the two, so the observation is compatible with either side.

## Possible Reconciliations

- **Scale hypothesis:** the two results may be measuring different scales — genome-wide averaging dilutes ecological signal carried by a small gene subset, so weak whole-genome environmental effects and strong subset-level functional differentiation could both hold. [src: ecotype_analysis]
- **Confounding hypothesis:** ecotype clusters may track sublineages, in which case COG differentiation is lineage-linked structure relabelled as ecology. [src: ecotype_functional_differentiation]
- **Heterogeneity hypothesis:** the environment-dominant minority of species may be exactly the species in which ecotype differentiation is genuinely adaptive, making both findings correct on disjoint subsets. [src: ecotype_analysis]

## Resolving Work

- Recompute the ecotype-functional COG comparison with a phylogenetic control (e.g. testing COG differences against within-species tree structure): does functional differentiation survive when sublineage identity is held fixed? [src: ecotype_functional_differentiation]
- Intersect the species carrying gene-content ecotypes with the environment-dominant species from the 172-species set: do ecotypes concentrate there, as the heterogeneity hypothesis predicts? [src: ecotype_analysis, ecotype_functional_differentiation]
- Re-run the environment-versus-phylogeny partial correlations — the association between two variables with the third held constant — on the differentiating COG subsets rather than whole genomes: does environmental signal strengthen when averaging is removed? [src: ecotype_analysis]
- Report, for the 16 of 172 species with significant environmental effects, whether their ecotype structure differs from the non-significant remainder. [src: ecotype_analysis]
- Record the metadata completeness of the environmental annotations used, since undetected effects and absent metadata are indistinguishable in a null result. [src: ecotype_analysis]
