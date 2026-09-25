<!-- tension-hash: 744fe541f5a71c61 -->
# Does Environment Shape Gene Content Only in Specific Subsystems?

Across the corpus, one reanalysis reports a null for environment as a driver of broad gene-content similarity, while two other projects report significant environmental structure in narrower functional feature spaces — prophage modules and metal-associated gene-family profiles. The disagreement matters because it determines whether "ecotype" differentiation is a whole-genome phenomenon that phylogeny already explains, or a subsystem-level phenomenon invisible to genome-wide similarity measures. It also matters methodologically: the three results use different feature spaces and different response variables, so a naive reading would treat an artefact of feature choice as a biological exception. See [[concepts/ecotype-environment-gene-content]].

## Evidence Sides

**Broad environmental null.** The ecotype reanalysis found that environmental species do not show stronger environment–gene-content coupling than human-associated species: environmental median partial correlation (a partial correlation measures the association between two variables while the effect of a further variable is held constant) 0.051 versus human-associated 0.084, with a Mann-Whitney U test (a rank-based nonparametric comparison of two groups) giving U=1536, p=0.83 [src: ecotype_env_reanalysis]. This is a null result and stays a null result — it does not assert that environment is irrelevant, only that the expected environmental enrichment in broad gene-content similarity was not detected.

**Subsystem-specific environmental signal.** Prophage modules — annotation-defined blocks of phage-derived genes integrated in bacterial genomes — showed environment effects that survived genome-size and host-family controls, with environment F=30.04 versus phylogeny F=6.17, plus significant within-quartile tests [src: prophage_ecology]. Separately, the soil-metal analysis reported 2,355 significant COG–metal associations (COG = Cluster of Orthologous Groups, a gene-family annotation scheme) and a conditional db-RDA R² = 0.799 (db-RDA = distance-based redundancy analysis, an ordination regressing community composition on predictors after conditioning out nuisance terms) [src: soil_metal_functional_genomics]. That second result is hedged on its own terms: its tests concern metal-linked COG variation in soil and remain vulnerable to co-contamination, conditional-R² interpretation, non-independent tests, effect-size uncertainty, and spatial mismatch [src: soil_metal_functional_genomics].

## Possible Reconciliations

*Hypothesis 1 — genuine subsystem exception.* Environment may structure mobile and stress-response subsystems while leaving the genome-wide gene-content backbone phylogenetically determined, so both results could be simultaneously correct at their respective scales.

*Hypothesis 2 — feature-space artefact.* The significant results may arise because annotation-defined prophage modules and metal-associated COG profiles concentrate variance that broad gene-content similarity dilutes; on this hypothesis the "exception" is a property of the feature space, not of biology.

*Hypothesis 3 — structured confounding.* Environment labels may co-vary with sampling batch, contamination history and geography, so the significant environmental terms could index confounders rather than ecological selection — the reason the soil-metal result carries its conditional-R² and non-independence caveats [src: soil_metal_functional_genomics].

## Resolving Work

- Re-run the ecotype partial-correlation analysis restricted to prophage-module and metal-associated COG feature subsets, on the same species set, asking whether the null becomes significant when only those subsystems are scored.
- Apply the prophage PERMANOVA design (permutational multivariate analysis of variance) to broad gene content in the same genomes, asking whether environment beats phylogeny under matched controls.
- Report the unconditional db-RDA R² for metals alongside the conditional figure, asking how much total rather than residual COG variance metals explain.
- Build a common environmental metadata vocabulary across the three projects and re-test with matched species, asking whether disagreement persists once the denominators align.
- Model non-independent, co-contaminating metals jointly (partial correlation across metals), asking how many of the associations survive.
