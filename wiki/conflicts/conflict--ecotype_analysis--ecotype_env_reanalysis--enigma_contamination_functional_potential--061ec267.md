<!-- tension-hash: 18d0437ea6aba5bf -->
# Confirmatory Nulls versus Exploratory Positives: Do Environmental Gradients Shape Microbial Gene Content?

Several projects in this corpus test variants of a single question — does an environmental gradient (metal contamination, or environment more broadly) leave a detectable imprint on microbial gene content or community composition? — and they disagree in distinct ways that this page keeps separate. Within a single ENIGMA analysis, predeclared confirmatory tests are null while exploratory covariate-adjusted models of the same data are positive. Across successive ecotype analyses, reported median effect sizes for environment-versus-phylogeny differ widely with no agreed basis for comparing them; that gap is recorded here as two paired comparisons — original versus reanalysis, and reanalysis versus the new analysis — so that the reanalysis estimate serves as one pole of each pair rather than as evidence for both sides of a single pair. And the Oak Ridge laboratory-to-field comparison is null in aggregate while significant per genus, in both directions at once. The disagreements matter because they share a structure: whether a signal exists depends on the analysis contract (predeclared versus exploratory), on the covariate and coverage adjustments applied, and on the taxonomic or genomic resolution at which the test is run. None is settled by the evidence in this corpus. This page records all of them; it treats the pangenome-openness result as a candidate reconciliation rather than as a further side, because that project tested a proposed explanation and found it did not apply. Source concept page: [[concepts/confirmatory-exploratory-ecological-association-discordance]].

## Evidence Sides

### Contamination and defense functions in ENIGMA communities

**Side A — the confirmatory null.** The principal tension is between null predeclared genus-level Spearman tests (a rank-correlation test, fixed in advance of seeing the outcome) and positive exploratory models that adjust for mapped coverage and additional covariates. [src: enigma_contamination_functional_potential] The confirmatory tests provide no robust monotonic contamination–defense association. [src: enigma_contamination_functional_potential] The discordance is not resolved by the high-coverage subset or fraction-aware analyses, because high-coverage defense tests have global FDR q-values of 0.301 and 0.189, and within-fraction tests are non-significant. [src: enigma_contamination_functional_potential] (FDR = false discovery rate; a q-value is the FDR-adjusted significance level after correcting for multiple tests.)

**Side B — the coverage-adjusted positive.** The relaxed coverage-adjusted model has FDR q = 0.0462 and the strict model has FDR q = 0.130. [src: enigma_contamination_functional_potential] The two adjusted models therefore point the same way but do not agree in strength, so Side B is internally graded rather than uniform. [src: enigma_contamination_functional_potential]

### Original ecotype estimate versus its reanalysis

**Side A — the original estimate.** The original median partial correlation was 0.003. [src: ecotype_env_reanalysis] (A partial correlation measures association between two variables with a third — here phylogeny or environment — held constant.)

**Side B — the reanalysis estimate.** The reanalysis median partial correlation was 0.081, a 27x difference from the original; the changed genome sets and downsampling procedures prevent treating that difference as a biological effect. [src: ecotype_env_reanalysis]

### Reanalysis versus the new ecotype analysis

**Side A — the reanalysis estimate.** The reanalysis median was 0.081. [src: ecotype_env_reanalysis]

**Side B — the new ecotype analysis.** Its environment median partial correlation was 0.0025 and phylogeny median was 0.0143. The differing genome coverage, species inclusion, embedding coverage, and sampling procedures prevent treating these values as directly comparable biological estimates. [src: ecotype_analysis] [src: ecotype_env_reanalysis]

### Aggregate versus per-genus laboratory-to-field prediction at Oak Ridge

**Side A — aggregate null.** The Oak Ridge evidence **supports** the confirmatory-null side for aggregate laboratory-to-field prediction. [src: lab_field_ecology]

**Side B — per-genus significance, bidirectional.** The same evidence **refines** the exploratory side by showing statistically significant associations in both directions at genus level after multiple-testing correction. This tension is not resolvable from the field correlations alone because pH, dissolved oxygen, carbon sources, temporal history, community interactions, and genus-to-strain variation were not controlled. [src: lab_field_ecology]

## Possible Reconciliations

These are hypotheses, not established findings.

**Resolution mismatch (ENIGMA contamination–defense; Oak Ridge).** The project evidence supports a cautious hypothesis that contamination-linked functional differentiation may exist at finer taxonomic, pathway, or strain resolution than the current genus-level COG-fraction proxies, but it does not establish that hypothesis as a community-wide finding. [src: enigma_contamination_functional_potential] (COG = Clusters of Orthologous Groups, a coarse functional category scheme; a COG-fraction proxy summarises a genome or community as the share of genes in each category.) Under this hypothesis both sides could be right: aggregated genus-level scores would dilute a signal that is real at strain or pathway level, and genus-to-strain variation is likewise an uncontrolled candidate explanation at Oak Ridge. [src: enigma_contamination_functional_potential] [src: lab_field_ecology]

**Coverage as a confounder rather than a nuisance (ENIGMA contamination–defense).** If mapped abundance fraction is correlated with both contamination and the defense score, then unadjusted Spearman tests are confounded and the coverage-adjusted model is the better estimate; if instead the adjustment removes variance that carries the biological signal, the confirmatory null stands. The corpus does not adjudicate between these, and the spread between the relaxed model's FDR q = 0.0462 and the strict model's FDR q = 0.130 is consistent with either reading. [src: enigma_contamination_functional_potential]

**Non-comparable estimands (both ecotype comparisons).** The changed genome sets and downsampling procedures prevent treating the 27x original-versus-reanalysis difference as a biological effect [src: ecotype_env_reanalysis], and the differing genome coverage, species inclusion, embedding coverage, and sampling procedures prevent treating the reanalysis and new-analysis values as directly comparable biological estimates [src: ecotype_analysis] [src: ecotype_env_reanalysis] — so both gaps may be artifacts of what was measured rather than disagreements about nature.

**Measurement-instrument limits (both ecotype comparisons).** The ecotype report proposes — but does not directly establish — that AlphaEarth embeddings may capture regional epidemiological patterns rather than ecological differences, and that unequal genome counts may provide greater statistical power for weak correlations. [src: ecotype_env_reanalysis] The new analysis **supports** this hypothesis as a limitation rather than resolving it: it suggests that AlphaEarth embeddings may not fully capture ecologically relevant environmental variation, while its result that phylogeny generally dominates whole-genome gene-content similarity does not exclude environmental effects on specific gene subsets. [src: ecotype_analysis]

**A tested-and-rejected reconciliation.** A natural explanation — that species differ in effect size because their pangenomes differ in openness (how readily a species accumulates new genes) — does not survive testing. The pangenome-openness result **refines** rather than resolves this tension: openness versus environment was rho = -0.05 with p = 0.54, and openness versus phylogeny was rho = 0.03 with p = 0.73, so the species-level openness metric did not explain either set of ecotype effect sizes. This does not contradict the existence of environmental or phylogenetic gene-content effects; it leaves open whether the effects are confined to functional subsets or are missed by the openness summary. [src: pangenome_openness]

## Resolving Work

**For the ENIGMA confirmatory-versus-exploratory discordance:**
- Preregister the coverage-adjusted model as confirmatory on a held-out or newly collected ENIGMA sample set, with the same covariate list, and ask whether FDR q = 0.0462 replicates when it is no longer an exploratory choice. [src: enigma_contamination_functional_potential]
- Test the confounding hypothesis directly: estimate the association of mapped abundance fraction with both the contamination index and the defense score, and report whether adjustment moves the estimate toward or away from the null. [src: enigma_contamination_functional_potential]
- Repeat the contamination–defense test at pathway and strain resolution rather than genus-level COG fractions, to ask whether the hypothesised finer-resolution signal exists where the coarse proxy is null. [src: enigma_contamination_functional_potential]
- Power-analyse the high-coverage subset before interpreting its global FDR q-values of 0.301 and 0.189, to distinguish "no effect" from "too few samples to detect the exploratory effect size". [src: enigma_contamination_functional_potential]

**For the two ecotype effect-size gaps:**
- Re-run the original, reanalysis, and new ecotype pipelines on one fixed genome set, one fixed species list, and one fixed downsampling rule, and ask how much of the gap between the original median of 0.003, the reanalysis median of 0.081, and the new analysis's environment median of 0.0025 survives when only the method differs. [src: ecotype_env_reanalysis] [src: ecotype_analysis]
- Benchmark AlphaEarth embeddings against measured in-situ physicochemistry for the subset of genomes with both, to test whether the embeddings track ecology or regional sampling. [src: ecotype_env_reanalysis] [src: ecotype_analysis]
- Recompute environment partial correlations on functional gene subsets rather than whole-genome gene content, to test the "effects confined to functional subsets" escape left open by the openness null. [src: pangenome_openness] [src: ecotype_analysis]
- Stratify by genomes-per-species and re-estimate, to test whether unequal genome counts supply the extra statistical power hypothesised to inflate weak correlations. [src: ecotype_env_reanalysis]
- Report environment and phylogeny medians side by side from a single pipeline run, so that the contrast between the new analysis's environment median of 0.0025 and its phylogeny median of 0.0143 is separable from the between-analysis gaps. [src: ecotype_analysis]

**For the Oak Ridge laboratory-to-field discordance:**
- Re-fit the genus-level field correlations with pH, dissolved oxygen, carbon sources, and temporal history as covariates, and ask whether the bidirectional significant associations persist. [src: lab_field_ecology]
- Resolve the detected genera to strain level in the Oak Ridge data and re-test the laboratory-tolerance-to-field-abundance relationship, since genus-to-strain variation is an uncontrolled candidate explanation. [src: lab_field_ecology]
- Specify the estimand of the aggregate test and of the per-genus tests explicitly, then re-run both on matched quantities and matched resolution, to establish whether the aggregate null and the per-genus significance are in conflict at all or are answering different questions. [src: lab_field_ecology]
- Extend the aggregate comparison to more genera and accompany it with a power analysis, to distinguish an aggregate null that reflects no association from one that reflects too few genera to detect the effect. [src: lab_field_ecology]
