<!-- tension-hash: 18d0437ea6aba5bf -->
# Null Confirmatory Tests Versus Positive Adjusted and Reanalysis Associations

The disagreement concerns whether contamination-, environment-, and phylogeny-linked functional differences represent robust community-wide associations or effects that emerge only after exploratory adjustment, altered sampling, or finer-resolution analysis. The evidence summarized in [[concepts/confirmatory-exploratory-ecological-association-discordance]] is consequential because the apparent signal depends on model specification, genome coverage, taxonomic resolution, and the functional summary used.

## Evidence Sides

**Confirmatory and high-coverage analyses support a null or weak aggregate association.** The predeclared genus-level Spearman tests provide no robust monotonic contamination–defense association. High-coverage defense tests have global FDR q-values of 0.301 and 0.189, and within-fraction tests are non-significant. [src: enigma_contamination_functional_potential] The ecotype analysis also reports environment median partial correlation 0.0025 and phylogeny median 0.0143, compared with a reanalysis median of 0.081; differing genome coverage, species inclusion, embedding coverage, and sampling procedures prevent treating these as directly comparable biological estimates. [src: ecotype_analysis] [src: ecotype_env_reanalysis]

**Exploratory coverage-adjusted models support a positive but specification-sensitive association.** The relaxed coverage-adjusted model has FDR q = 0.0462, while the strict model has FDR q = 0.130. [src: enigma_contamination_functional_potential] The original and reanalysis median partial correlations were 0.003 and 0.081, respectively, although changed genome sets and downsampling procedures prevent treating the 27x difference as a biological effect. [src: ecotype_env_reanalysis] The pangenome-openness result does not explain these effects: openness versus environment was rho = -0.05 with p = 0.54, and openness versus phylogeny was rho = 0.03 with p = 0.73. [src: pangenome_openness]

**Field and reanalysis evidence supports a more conditional interpretation.** Oak Ridge evidence supports the confirmatory-null side for aggregate laboratory-to-field prediction but also shows statistically significant associations in both directions at genus level after multiple-testing correction. [src: lab_field_ecology] The project evidence therefore supports a cautious hypothesis that contamination-linked functional differentiation may exist at finer taxonomic, pathway, or strain resolution than current genus-level COG-fraction proxies, without establishing a community-wide finding. [src: enigma_contamination_functional_potential]

## Possible Reconciliations

- **Hypothesis—measurement resolution:** Effects may be confined to functional subsets, pathways, strains, or gene-content features that genus-level COG-fraction summaries dilute.
- **Hypothesis—coverage and sampling:** Unequal genome counts, changed genome sets, downsampling, and embedding coverage may alter power and effect estimates without changing biology.
- **Hypothesis—environmental representation:** AlphaEarth embeddings may capture regional epidemiological patterns rather than ecological differences, or may not fully capture ecologically relevant variation. [src: ecotype_env_reanalysis] [src: ecotype_analysis]
- **Hypothesis—uncontrolled field structure:** pH, dissolved oxygen, carbon sources, temporal history, community interactions, and genus-to-strain variation may produce associations not resolvable from field correlations alone. [src: lab_field_ecology]

## Resolving Work

- Reanalyze the same genomes with preregistered coverage adjustment and held-out validation to test whether the q = 0.0462 signal replicates under the strict model.
- Increase sampling across genomes, environments, and strains, then use hierarchical models to separate genus, strain, site, and temporal effects.
- Test pathway- and gene-subset associations directly rather than relying only on aggregate COG fractions or species-level openness.
- Recompute ecotype correlations on identical genome sets with matched downsampling and embedding coverage to determine whether 0.003, 0.0143, and 0.081 reflect sampling or biology.
- Measure environmental covariates directly and jointly model them with field outcomes to test whether the bidirectional genus-level associations persist after confounding control.
