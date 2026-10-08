<!-- tension-hash: 1f2162673aeeba2f -->
# Do the original and reanalysis environment effect sizes for ecotypes measure the same thing?

Two projects in the corpus report a median partial correlation for an environment measure across species. A partial correlation is the association between two variables after the influence of other variables is statistically removed. The two medians differ markedly, and this **contradicts** any direct comparison of their absolute effect sizes [src: ecotype_env_reanalysis]. This matters for [[concepts/environment-embedding-geography]], because conclusions about how strongly environment structures microbial genomic patterns depend on whether such effect sizes can be compared. The open question is whether the gap reflects biology or is an artefact of method.

## Evidence Sides

**Original environment measure (ecotype analysis)**

- The original analysis reports a median partial correlation of 0.0025 for its environment measure [src: ecotype_analysis; ecotype_env_reanalysis].

**Reanalysis across all species (ecotype environment reanalysis)**

- The reanalysis reports a median partial correlation of 0.081 across all 183 species [src: ecotype_analysis; ecotype_env_reanalysis].
- The reanalysis attributes the discrepancy to three differences [src: ecotype_env_reanalysis]:
  - different genome sets;
  - full-genome extraction;
  - downsampling procedures.
- On this account, the two absolute effect sizes cannot be compared directly [src: ecotype_env_reanalysis].

The supplied evidence does not establish which median is closer to the true environmental signal. The methodological attribution is the reanalysis's own account of the discrepancy [src: ecotype_env_reanalysis].

## Possible Reconciliations

- **Hypothesis (genome-set composition):** The reanalysis attributes part of the discrepancy to different genome sets [src: ecotype_env_reanalysis]. Species membership alone may shift the median, independent of any real change in environmental signal.
- **Hypothesis (extraction depth):** Full-genome extraction may capture accessory genes (genes present in some but not all genomes of a species) that carry environmental structure. A narrower extraction would miss those genes and dampen the effect.
- **Hypothesis (downsampling):** Downsampling may reduce noise from over-represented lineages, raising partial correlations. Alternatively, it may inflate variance in sparsely sampled species.
- **Hypothesis (both valid in scope):** Each median may be internally valid for its own pipeline. In that case, the tension concerns comparability rather than which result is correct.

## Resolving Work

- **Genome-set swap:** Re-run the original environment partial-correlation pipeline on the reanalysis genome set, and the reverse. This tests whether genome-set composition alone accounts for the difference in medians.
- **Extraction ablation:** Hold the genome set and downsampling fixed, then compare full-genome extraction with the original extraction scheme. This tests whether gene-content depth changes the environmental partial correlation.
- **Downsampling sensitivity:** Repeat the reanalysis over the 183 species with and without downsampling, and at several subsample sizes. This tests whether the median is stable to sampling procedure.
- **Per-species paired comparison:** For species present in both analyses, compare per-species partial correlations rather than medians. This shows whether the shift is uniform or driven by a subset of species.
- **Shared environment definition audit:** Document each project's environment variable and distance metric side by side. This tests whether the two "environment" measures are operationally equivalent before any effect sizes are compared.
