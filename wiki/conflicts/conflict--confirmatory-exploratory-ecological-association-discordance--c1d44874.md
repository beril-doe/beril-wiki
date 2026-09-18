<!-- tension-hash: c1d4487475aa4fae -->
# Conflict: Two Incompatible Magnitudes for the Environment–Gene-Content Partial Correlation

Two projects in this corpus report the strength of the association between environmental similarity and genome-wide gene-content similarity on very different scales, and neither the difference nor the apparent agreement can be taken at face value. A partial correlation here is the correlation between two distance matrices (environmental distance and gene-content distance) after removing the contribution of a third (phylogenetic distance); the median is taken across species. The original ecotype analysis places that median near zero [src: ecotype_analysis], while the reanalysis places it at 0.081 [src: ecotype_env_reanalysis]; and a third figure — the reanalysis's own quotation of the original — does not match the original page's number [src: ecotype_env_reanalysis, ecotype_analysis]. The disagreement matters because it determines whether "environment barely matters genome-wide" is a measured result or an artifact of which genomes were included and how they were sampled. It surfaces on [[concepts/confirmatory-exploratory-ecological-association-discordance]], [[concepts/genome-wide-versus-locus-specific-ecological-adaptation]], [[concepts/sampling-depth-and-downsampling-effects]], and [[concepts/study-batch-confounding-of-environmental-associations]].

## Evidence Sides

**The original ecotype analysis: a near-null environmental signal, dominated by phylogeny.** Its environment median partial correlation was 0.0025 and its phylogeny median was 0.0143. [src: ecotype_analysis] [src: ecotype_env_reanalysis] It reports no significant environmental effect in 90.7% of species, and its own limitation is that only 28.4% embedding coverage was available — embedding coverage meaning the fraction of genomes with usable environmental embeddings attached. [src: ecotype_analysis, ecotype_env_reanalysis] The original page states this median across its 172-species analysis. [src: ecotype_env_reanalysis, ecotype_analysis]

**The reanalysis: a substantially larger median, but explicitly not a replication.** The reanalysis reports a median partial correlation of 0.081 across 183 species, versus 0.003 in the original analysis. [src: ecotype_env_reanalysis] It attributes the discrepancy to different genome sets and downsampling procedures — downsampling meaning reducing genomes per species before computing distances — and explicitly preserves only the within-method group comparison rather than the absolute value. [src: ecotype_env_reanalysis] Differing genome coverage, species inclusion, embedding coverage, and sampling procedures prevent treating these values as directly comparable biological estimates. [src: ecotype_analysis] [src: ecotype_env_reanalysis]

## Possible Reconciliations

- **Hypothesis (method-scale):** the gap is entirely a measurement-scale artifact of genome inclusion and downsampling, so both medians are internally valid and neither estimates the same population quantity. [src: ecotype_env_reanalysis]
- **Hypothesis (coverage-attenuation):** 28.4% embedding coverage attenuates the original estimate toward zero, and higher-coverage genome sets would raise it. [src: ecotype_analysis]
- **Hypothesis (bookkeeping):** the 0.003 the reanalysis quotes and the 0.0025 the original page reports refer to different subsets or rounding conventions, and the mismatch is a provenance question, not a biological one. [src: ecotype_env_reanalysis, ecotype_analysis]

These must not be reconciled by averaging. [src: ecotype_analysis, ecotype_env_reanalysis]

## Resolving Work

- Run both pipelines on a single fixed genome set covering the intersection of the 172-species and 183-species analyses: does the median gap survive when species inclusion is held constant?
- Recompute the original partial correlations at matched embedding coverage above 28.4%: is the near-zero median a coverage-attenuation effect?
- Apply the reanalysis downsampling procedure to the original genome set and the original procedure to the reanalysis set, crossing method with data: which factor carries the magnitude difference?
- Trace the provenance of the 0.003 versus 0.0025 figures to their computing scripts: are they the same statistic?
- Repeat the within-method environmental-versus-human-associated comparison under each pipeline: does the group contrast stay stable while absolute magnitudes move? [src: ecotype_env_reanalysis]
