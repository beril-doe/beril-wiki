<!-- tension-hash: f703048c20c5d6a9 -->
# Strong Environmental Signal or Non-Portable Confounding?

The disagreement is whether environmental associations reflect genuine, fine-scale ecological structure or instead arise mainly from study, batch, sampling, and measurement differences that fail to generalize. The tension matters because pooled analyses suggest substantial environmental predictability, while study-held-out validation and reanalysis results weaken claims that the association is portable across datasets. The evidence is summarized on [[concepts/study-batch-confounding-of-environmental-associations]].

## Evidence Sides

### **Environmental structure is detectable within controlled or local settings**

The cross-study analysis reports environment-model R²=0.35 under random cross-validation, indicating strong environmental differences in the pooled data. [src: euk_in_prok_correlates] The within-NEON analysis nevertheless gives positive predictive performance, with R²=+0.17 ± 0.06. [src: euk_in_prok_correlates] These findings support the possibility that fine-scale environmental structure is real, even if it is not portable across studies. [src: euk_in_prok_correlates]

The original ecotype analysis also reports a median environment partial correlation of 0.0025 versus 0.0143 for phylogeny, and no significant environmental effect in 90.7% of species. [src: ecotype_analysis] The ecotype reanalysis reports an all-species median partial correlation of 0.081. [src: ecotype_env_reanalysis]

### **The pooled environmental association may be confounded and non-portable**

Study-held-out validation gives R²=−0.30 and detection AUC=0.56. [src: euk_in_prok_correlates] This contrasts with the random cross-validation result and indicates that the pooled association does not transfer reliably when the study is held out. [src: euk_in_prok_correlates] Study, batch, and unmeasured protocol variables may be entangled, while constant protocol and batch do not remove possible sub-batch confounding from sampling campaigns. [src: euk_in_prok_correlates]

The ecotype reanalysis found that environmental species did not show stronger environment–gene-content correlations than human-associated species, despite a confirmed clinical sampling bias. [src: ecotype_env_reanalysis] The original analysis had only 28.4% embedding coverage. [src: ecotype_analysis] The reanalysis reports an all-species median partial correlation of 0.081 versus 0.003 in the original analysis, but attributes the discrepancy to different genome inclusion and downsampling. [src: ecotype_analysis, ecotype_env_reanalysis]

## Possible Reconciliations

- **Measurement-scale hypothesis:** Random cross-validation and within-NEON validation may capture real local structure, whereas study-held-out validation tests portability across broader protocol and sampling regimes.
- **Confounding hypothesis:** Environmental variables may correlate with study, batch, campaign, or clinical sampling variables, producing apparent associations that weaken under stricter validation.
- **Coverage hypothesis:** The difference between 0.081 and 0.003 may reflect genome inclusion, downsampling, and the original 28.4% embedding coverage rather than a biological contradiction.
- **Effect-definition hypothesis:** The reported statistics may describe different species sets, correlations, or validation targets, so absolute effect sizes should not be directly compared across methods.

## Resolving Work

- Refit the environmental models with leave-one-study-out, leave-one-campaign-out, and within-study validation to ask whether performance survives each separation.
- Add study, batch, protocol, campaign, and clinical-sampling covariates, then compare residual environmental associations to test whether they explain the signal.
- Reanalyze both ecotype datasets using identical genome inclusion, downsampling, embedding coverage, and correlation definitions to determine whether the 0.081 versus 0.003 difference is methodological.
- Quantify performance separately at fine and broad spatial or environmental scales to test whether genuine local structure coexists with poor cross-study portability.
