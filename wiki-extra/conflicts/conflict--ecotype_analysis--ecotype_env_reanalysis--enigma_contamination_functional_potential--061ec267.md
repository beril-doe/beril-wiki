<!-- tension-hash: 18d0437ea6aba5bf -->
# Do contamination–environment associations disappear under confirmation, or shift with resolution and measurement?

The disagreement concerns whether contamination-linked ecological and functional associations are absent, or are obscured by taxonomic resolution, coverage adjustment, genome sampling, and environmental measurement. The evidence spans confirmatory versus exploratory contamination models, ecotype reanalyses, pangenome summaries, and Oak Ridge laboratory-to-field comparisons. As summarized on [[concepts/confirmatory-exploratory-ecological-association-discordance]], the results do not support a single community-wide interpretation, but they do identify several testable sources of discordance.

## Evidence Sides

### **Confirmatory and aggregate analyses favor null or weak effects**

The predeclared genus-level Spearman tests provide no robust monotonic contamination–defense association, and the high-coverage subset and fraction-aware analyses do not resolve the discordance: high-coverage defense tests have global FDR q-values of 0.301 and 0.189, and within-fraction tests are non-significant. [src: enigma_contamination_functional_potential]

The Oak Ridge evidence supports the confirmatory-null side for aggregate laboratory-to-field prediction. However, field correlations alone cannot resolve the tension because pH, dissolved oxygen, carbon sources, temporal history, community interactions, and genus-to-strain variation were not controlled. [src: lab_field_ecology]

### **Adjusted exploratory models and finer-scale interpretations allow positive effects**

The relaxed coverage-adjusted model has FDR q = 0.0462, while the strict model has FDR q = 0.130. [src: enigma_contamination_functional_potential] Oak Ridge analyses also show statistically significant associations in both directions at genus level after multiple-testing correction. [src: lab_field_ecology]

The project evidence therefore supports a cautious hypothesis that contamination-linked functional differentiation may exist at finer taxonomic, pathway, or strain resolution than the current genus-level COG-fraction proxies, but it does not establish that hypothesis as a community-wide finding. [src: enigma_contamination_functional_potential]

### **Ecotype estimates disagree in magnitude but are not directly comparable**

The original and reanalysis median partial correlations were 0.003 and 0.081, respectively, but changed genome sets and downsampling procedures prevent treating the 27x difference as a biological effect. [src: ecotype_env_reanalysis] The new ecotype analysis found an environment median partial correlation of 0.0025 and a phylogeny median of 0.0143, while the reanalysis median was 0.081. Differing genome coverage, species inclusion, embedding coverage, and sampling procedures prevent treating these values as directly comparable biological estimates. [src: ecotype_analysis] [src: ecotype_env_reanalysis]

The pangenome-openness result did not explain either set of ecotype effect sizes: openness versus environment was rho = -0.05 with p = 0.54, and openness versus phylogeny was rho = 0.03 with p = 0.73. [src: pangenome_openness]

## Possible Reconciliations

- **Hypothesis—resolution:** Effects may be confined to functional subsets, pathways, strains, or other finer taxonomic levels rather than appearing in genus-level aggregates. [src: enigma_contamination_functional_potential]
- **Hypothesis—measurement:** AlphaEarth embeddings may capture regional epidemiological patterns rather than ecological differences, or may not fully capture ecologically relevant environmental variation. [src: ecotype_env_reanalysis] [src: ecotype_analysis]
- **Hypothesis—power and sampling:** Unequal genome counts, changed genome sets, and downsampling may alter power for weak correlations without changing biology. [src: ecotype_env_reanalysis]
- **Hypothesis—unmeasured context:** Laboratory-to-field associations may depend on uncontrolled environmental and community variables. [src: lab_field_ecology]

## Resolving Work

- Reanalyze contamination–defense associations across genus, species, strain, pathway, and COG-fraction levels using identical samples and preregistered covariates; test whether positive effects persist below genus resolution.
- Repeat all ecotype analyses on a harmonized genome set with matched species inclusion, embedding coverage, and downsampling; test whether the median partial correlations converge.
- Partition gene-content similarity into whole-genome and functional subsets, then compare each with environment and phylogeny; test whether openness misses subset-specific effects.
- Collect matched pH, dissolved oxygen, carbon-source, temporal, and community-interaction data for Oak Ridge samples; fit multivariable models to test whether genus-level associations remain after environmental control.
- Replicate significant exploratory findings in an independent cohort with held-out validation; test whether adjusted associations generalize beyond the discovery data.
