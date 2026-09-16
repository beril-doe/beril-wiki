<!-- tension-hash: 5cfe3bff8b732df9 -->
# Sampling bias versus signal: does clinical skew, missingness, or downsampling explain the weak environment–gene-content correlation?

Several projects in this corpus agree that the genome set carrying AlphaEarth embeddings is skewed toward clinical and human-associated isolates, and that species differ in how much embedding data they are missing. They disagree about what follows from that. One reading treats the skew and the missingness as nuisance artifacts that suppress an environmental signal which better sampling would reveal; the competing reading is that both asymmetries are real but neither accounts for the weak environment–gene-content relationship, because the corrections the artifact hypothesis calls for do not strengthen the signal. A third, partly separate disagreement is about scale: the same underlying question has produced median partial correlations differing by more than an order of magnitude across analyses, without agreement on which methodological choice is responsible. This page covers all three disagreements, together with two contributions that modify rather than settle them (function- and condition-coverage effects from `core_gene_tradeoffs`, and the null openness correlations from `pangenome_openness`). Throughout, a *partial correlation* is a correlation between two distance measures after controlling for a third; an *embedding* is a fixed-length numeric vector summarizing a genome's sampling location; *NaN* ("not a number") marks a missing value; *downsampling* means analyzing only a subset of each species' genomes. Source concept page: [[concepts/sampling-depth-and-downsampling-effects]].

## Evidence Sides

### Disagreement 1 — Does clinical sampling skew explain the weak environmental signal?

**Side A — the skew is real, confirmed independently, and is the standing suspect.** The AlphaEarth subset is clinically skewed. [src: ecotype_env_reanalysis] The explorer independently confirms the skew. [src: env_embedding_explorer] The explorer also shows that environmental samples have stronger geographic embedding structure than human-associated samples, so the embeddings that carry the most spatial information belong to the under-represented group. [src: env_embedding_explorer] On this reading the skew remains the leading candidate explanation for why a whole-genome environment–gene-content association is hard to see.

**Side B — the skew is real but does not explain the weak relationship.** The evidence does not support the claim that this skew alone explains the weak environment–gene-content relationship. [src: ecotype_env_reanalysis] The principal tension is precisely between confirmed clinical sampling bias and the absence of a stronger environmental correlation after group comparison. [src: ecotype_env_reanalysis] The stronger geographic embedding structure in environmental samples was the basis of the prediction that environmental species would show the stronger environment–gene-content correlation; that prediction was not borne out, so spatial signal and gene-content signal remain discordant rather than reconciled. [src: env_embedding_explorer, ecotype_env_reanalysis]

### Disagreement 2 — Does differential missingness account for the missing environmental signal?

**Side A — missingness is differential and uneven, so the group comparison rests on unequal data.** Environmental species had a 21% NaN rate compared with 7% for Human-associated species. [src: ecotype_env_reanalysis] The explorer adds 3,838 records with at least one embedding NaN and uneven metadata coverage. [src: env_embedding_explorer] The environmental group therefore loses more species to NaN than the human-associated group, which could slightly bias the comparison. [src: ecotype_env_reanalysis]

**Side B — the asymmetry cannot be what is hiding an environmental signal.** Removing more Environmental species did not produce the expected stronger environmental signal. [src: ecotype_env_reanalysis] The reanalysis holds that because human-associated species already show higher correlations even with this bias present, addressing the NaN imbalance would only strengthen the null result — the missingness asymmetry, if anything, biases toward finding a stronger signal in the environmental group rather than suppressing one. [src: ecotype_env_reanalysis] What the imbalance does indicate is that missingness, sampling depth, and ecological classification must be analyzed jointly rather than treated as interchangeable explanations. [src: ecotype_env_reanalysis] The explorer's additional missingness and coverage evidence **refines** rather than resolves this tension. [src: env_embedding_explorer]

### Disagreement 3 — Why do the correlation magnitudes differ so much across analyses?

**Side A — the magnitudes differ by a large factor.** The reanalysis reported a median partial correlation of 0.081 across 183 species, whereas the original analysis reported 0.003. [src: ecotype_env_reanalysis] The ecotype_analysis provides a separate median environmental value of 0.0025 across 172 species and a phylogenetic value of 0.0143. [src: ecotype_analysis]

**Side B — the magnitudes are not comparable, and the within-method comparison is stable.** The absolute values are not comparable because the analyses used different genome sets, sampling strategies, and distance distributions. [src: ecotype_env_reanalysis] The ecotype_analysis figures do not resolve the tension because its coverage and analysis population also differ. [src: ecotype_analysis] The tension is therefore between the large difference in overall correlation values and the stability of the within-method environmental-versus-human-associated comparison. [src: ecotype_env_reanalysis]

### Modifying contributions (neither side)

The function-specific fitness evidence adds a related interpretive tension rather than resolving the sampling discrepancy: core genes were more burdensome in several functional categories but less burdensome for Cell Wall genes, and the Fitness Browser condition types were biased toward experimentally convenient conditions. [src: core_gene_tradeoffs] This **refines** the claim that sampling controls alone can explain weak whole-genome ecological associations: even with matched genome sampling, condition coverage and functional aggregation could affect which biological signal is visible. [src: core_gene_tradeoffs] The pangenome-openness null correlations do not contradict the sampling-depth result: they test whether an openness summary predicts effect sizes rather than whether changing genome sampling changes correlation estimates. [src: pangenome_openness]

## Possible Reconciliations

These are hypotheses, not findings.

- **Scope hypothesis (Disagreement 1).** Both sides may be right if the skew operates on geographic embedding structure but not on gene-content association — the explorer's stronger geographic structure in environmental samples and the reanalysis's non-improvement of the environmental correlation would then be measurements of different links in the chain rather than contradictory results about one link. [src: env_embedding_explorer, ecotype_env_reanalysis]

- **Confounded-correction hypothesis (Disagreement 2).** If missingness, sampling depth, and ecological classification are entangled, then dropping Environmental species to reduce NaN exposure simultaneously changes depth and classification composition, so any expected signal gain could be cancelled by a loss elsewhere. The reanalysis itself frames these as factors requiring joint rather than interchangeable treatment. [src: ecotype_env_reanalysis]

- **Measurement-scale hypothesis (Disagreement 3).** The 0.081-versus-0.003 gap may reflect no substantive disagreement at all if the two analyses estimate different quantities on different distance distributions; the reanalysis explicitly states the values are not comparable given different genome sets, sampling strategies, and distance distributions. [src: ecotype_env_reanalysis] Under this hypothesis the ecotype_analysis values of 0.0025 across 172 species and 0.0143 remain a third, separately scaled estimate rather than a tiebreaker. [src: ecotype_analysis]

- **Visibility hypothesis (cross-cutting).** Signal strength may depend on which conditions and functional groupings are observed, not only on which genomes are sampled — the direction in which the Cell Wall exception and the convenience-biased condition types point. [src: core_gene_tradeoffs]

- **Power-versus-decoupling hypothesis (cross-cutting).** The openness nulls leave unresolved whether openness fails because pangenome structure is genuinely decoupled from eco-phylogenetic dynamics, because the metric is too coarse, or because the matched species sample and upstream effect estimates limit power. [src: pangenome_openness] Each branch implies a different reading of how much of the weak-signal picture is methodological.

## Resolving Work

**For Disagreement 1 (clinical skew).**
- Re-run the environmental-versus-human-associated group comparison on genome sets matched for sampling category composition, asking whether the skew changes the direction of the group difference at all. [src: ecotype_env_reanalysis]
- Test the geographic-structure and gene-content links on the *same* species set, so that the discordance reported between spatial and gene-content signal is measured within one analysis population rather than across two. [src: env_embedding_explorer, ecotype_env_reanalysis]
- Stratify by the harmonized environment-category scheme rather than a binary environmental/human-associated split, to check whether the skew's effect is category-specific. [src: env_embedding_explorer, ecotype_env_reanalysis]

**For Disagreement 2 (missingness).**
- Model missingness, sampling depth, and ecological classification jointly as covariates rather than removing species, as the reanalysis's own conclusion recommends. [src: ecotype_env_reanalysis]
- Quantify how the 3,838 records with at least one embedding NaN and the uneven metadata coverage distribute over species and categories, and re-estimate correlations under explicit imputation versus listwise deletion. [src: env_embedding_explorer]
- Run a sensitivity sweep over NaN-exclusion thresholds spanning the 21% Environmental and 7% Human-associated rates to test the reanalysis's claim that recovering the dropped environmental species can only strengthen, never overturn, the null. [src: ecotype_env_reanalysis]

**For Disagreement 3 (correlation scale).**
- Execute the controlled reanalysis the corpus already calls for: determine whether the correlation-scale difference is driven mainly by downsampling, genome-set composition, extraction behavior, embedding coverage, condition coverage, missingness, or another methodological factor, varying one factor at a time. [src: ecotype_env_reanalysis, ecotype_analysis, core_gene_tradeoffs]
- Recompute the 0.081-scale and 0.003-scale estimates on a single shared genome set and distance distribution, reporting whether the gap survives. [src: ecotype_env_reanalysis]
- Place the ecotype_analysis environmental value of 0.0025 across 172 species and phylogenetic value of 0.0143 on that shared footing, to test whether its differing coverage and analysis population fully account for its position. [src: ecotype_analysis]
- Repeat the fitness-side analysis with expanded condition coverage and with functional categories disaggregated, testing whether the Cell Wall exception persists when convenience-biased condition types are down-weighted. [src: core_gene_tradeoffs]
- Distinguish the three openness branches by re-testing the openness metric at finer granularity and with a larger matched species sample, which separates "genuinely decoupled" from "too coarse" and from "underpowered". [src: pangenome_openness]
