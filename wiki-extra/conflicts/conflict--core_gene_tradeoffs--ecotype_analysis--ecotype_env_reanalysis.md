<!-- tension-hash: 62431ad0bbcdbd63 -->
# Sampling Depth, Missingness, and the Stability of Ecological Correlations

The disagreement is whether weak environment–gene-content associations primarily reflect clinical sampling bias, missingness, and downsampling, or whether they persist after accounting for those factors because the biological relationship is genuinely weak or methodologically dependent. This matters because the interpretation changes from a correctable sampling artifact to a more fundamental decoupling between environmental structure and gene content. The tension is summarized on [[concepts/sampling-depth-and-downsampling-effects]].

## Evidence Sides

**Sampling bias explains the weak environmental relationship.** The AlphaEarth subset is clinically skewed, and the explorer independently confirms the skew. [src: ecotype_env_reanalysis] [src: env_embedding_explorer] This supports sampling bias as a plausible source of distortion, particularly because the explorer adds 3,838 records with at least one embedding NaN and uneven metadata coverage. [src: env_embedding_explorer]

**Sampling bias alone does not explain the weak relationship.** Group comparison confirmed the clinical sampling bias, but the evidence did not support the claim that this skew alone explains the weak environment–gene-content relationship. [src: ecotype_env_reanalysis] Removing more Environmental species also did not produce the expected stronger environmental signal, despite Environmental species having a 21% NaN rate compared with 7% for Human-associated species. [src: ecotype_env_reanalysis] Environmental samples had stronger geographic embedding structure, so spatial signal and gene-content signal remained discordant. [src: env_embedding_explorer]

**The correlation scale is unstable across analyses.** The reanalysis reported a median partial correlation of 0.081 across 183 species, whereas the original analysis reported 0.003. [src: ecotype_env_reanalysis] These absolute values are not comparable because the analyses used different genome sets, sampling strategies, and distance distributions. [src: ecotype_env_reanalysis] Separately, the ecotype_analysis reported a median environmental value of 0.0025 across 172 species and a phylogenetic value of 0.0143, but its different coverage and analysis population do not resolve the discrepancy. [src: ecotype_analysis]

**Functional and pangenome analyses complicate a sampling-only explanation.** Core genes were more burdensome in several functional categories but less burdensome for Cell Wall genes, while Fitness Browser condition types were biased toward experimentally convenient conditions. [src: core_gene_tradeoffs] Pangenome-openness null correlations test whether an openness summary predicts effect sizes, not whether changing genome sampling changes correlation estimates. [src: pangenome_openness]

## Possible Reconciliations

- **Hypothesis — sampling interacts with missingness:** NaN rates, genome depth, and ecological classification may jointly alter the effective comparison population, so removing Environmental species alone would not isolate the relevant bias.
- **Hypothesis — spatial and gene-content signals differ:** Environmental geography may be recoverable in embeddings even when gene-content distances remain weakly associated with environment.
- **Hypothesis — methodological scale differs:** The correlation values may shift with genome-set composition, distance distributions, extraction behavior, and analysis population without changing the within-method environmental-versus-human-associated comparison.
- **Hypothesis — biological signal is function-specific:** Functional aggregation and condition coverage may reveal or obscure ecological effects even under matched genome sampling.

## Resolving Work

- Recompute all analyses on identical genome sets with preregistered environmental and Human-associated strata; test whether correlation estimates converge.
- Stratify by NaN status, sampling depth, ecological classification, and metadata completeness; quantify which factor changes the environmental correlation.
- Compare geographic embedding distances and gene-content distances using the same species and distance distributions; test whether spatial structure predicts gene-content structure.
- Reanalyze Fitness Browser effects with balanced condition types and matched functional categories; test whether condition coverage changes the apparent core-versus-Cell Wall contrast.
- Recalculate pangenome-openness associations under controlled species composition and uncertainty propagation; test whether the null reflects a coarse metric or limited power.
