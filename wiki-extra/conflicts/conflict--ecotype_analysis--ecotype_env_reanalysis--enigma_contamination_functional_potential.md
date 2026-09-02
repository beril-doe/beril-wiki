<!-- tension-hash: 06cd8ad0a82f7cb5 -->
# Genus-Level Null Tests Versus Coverage-Adjusted and Ecotype Associations

The disagreement concerns whether contamination-linked functional or ecological differentiation is absent, weak but detectable after adjustment, or obscured by taxonomic, sampling, and representation choices. The evidence contrasts predeclared genus-level tests with exploratory covariate-adjusted models, and contrasts ecotype analyses whose estimates are not directly comparable because their genome sets and sampling procedures differ. This makes the conflict consequential for deciding whether the observed signals represent biological associations or methodological variation documented on [[concepts/confirmatory-exploratory-ecological-association-discordance]].

## Evidence Sides

**Confirmatory genus-level tests find no robust association.**  
The principal confirmatory tests were null predeclared genus-level Spearman tests, providing no robust monotonic contamination–defense association. The discordance is not resolved by the high-coverage subset or fraction-aware analyses: high-coverage defense tests have global FDR q-values of 0.301 and 0.189, and within-fraction tests are non-significant. [src: enigma_contamination_functional_potential]

**Coverage-adjusted exploratory models detect a possible signal.**  
Relaxed exploratory models adjusting for mapped coverage and additional covariates have FDR q = 0.0462, while the strict model has FDR q = 0.130. The project evidence therefore supports a cautious hypothesis that contamination-linked functional differentiation may exist at finer taxonomic, pathway, or strain resolution than the current genus-level COG-fraction proxies, but it does not establish that hypothesis as a community-wide finding. [src: enigma_contamination_functional_potential]

**Ecotype estimates differ across analyses, but are not directly comparable.**  
The original and reanalysis median partial correlations were 0.003 and 0.081, respectively; however, changed genome sets and downsampling procedures prevent treating the 27x difference as a biological effect. [src: ecotype_env_reanalysis] The new ecotype analysis reports an environment median partial correlation of 0.0025 and a phylogeny median of 0.0143, while the reanalysis median was 0.081. Differing genome coverage, species inclusion, embedding coverage, and sampling procedures prevent treating these values as directly comparable biological estimates. [src: ecotype_analysis] [src: ecotype_env_reanalysis]

## Possible Reconciliations

- **Hypothesis — measurement resolution:** A real association may occur at finer taxonomic, pathway, or strain resolution while remaining undetectable in genus-level COG-fraction proxies. [src: enigma_contamination_functional_potential]
- **Hypothesis — adjustment and power:** Coverage adjustment or unequal genome counts may increase sensitivity to weak correlations, producing exploratory positives without contradicting null unadjusted tests. [src: ecotype_env_reanalysis]
- **Hypothesis — environmental representation:** AlphaEarth embeddings may capture regional epidemiological patterns rather than ecological differences, or may not fully capture ecologically relevant environmental variation. [src: ecotype_env_reanalysis] [src: ecotype_analysis]
- **Hypothesis — distinct biological targets:** Phylogeny may dominate whole-genome gene-content similarity while environmental effects remain confined to specific gene subsets. [src: ecotype_analysis]

## Resolving Work

- Reanalyze the same genome set with predeclared genus-level, pathway-level, and strain-level features, testing whether signal appears only below genus resolution.
- Fit matched models with and without mapped-coverage and covariate adjustment, using identical samples and multiple-testing procedures, to determine whether adjustment creates the discordance.
- Recompute ecotype correlations after fixing species inclusion, genome coverage, embedding coverage, and downsampling, testing whether the 0.003, 0.0025, 0.0143, and 0.081 estimates converge.
- Compare AlphaEarth variables with independently measured environmental variables and regional epidemiological covariates to test which variation the embeddings represent.
- Test environmental associations for targeted gene subsets while controlling for phylogeny, asking whether subset-level effects persist despite phylogeny dominating whole-genome similarity.
