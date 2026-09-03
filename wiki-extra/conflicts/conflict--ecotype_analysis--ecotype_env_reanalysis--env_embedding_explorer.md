<!-- tension-hash: 7aa1c14b3277bf3d -->
# Embedding Structure, Environmental Effects, and Gene-Content Validity

The disagreement concerns what environmental structure in the embedding can establish about ecological effects on genomes. [[concepts/embedding-cluster-interpretation-limits]] notes that a 38% human-associated composition may reshape the full projection, while the reanalysis found that this bias did not explain the weak environment–gene-content relationship. [[concepts/environmental-embedding-ecological-validity]] adds that environmental similarity was generally weaker than phylogenetic similarity, even though environment dominated for 39.5% of species. The tension matters because visible embedding structure, species-level dominance, and genome-wide gene-content correlation are related but not interchangeable outcomes.

## Evidence Sides

**Embedding composition and geographic structure support an environmental signal**

The embedding analysis leaves open that the 38% human-associated composition may dilute or reshape ecological patterns in the full projection. [src: env_embedding_explorer] Embedding distance also increases with geographic distance, indicating a geographic embedding gradient. [src: env_embedding_explorer] These observations support treating the embedding as potentially environmentally structured, but they do not by themselves establish an organism-level environment–gene-content relationship.

**Genome-level reanalysis finds that human-associated composition does not explain the weak relationship**

The reanalysis, using genome-level classifications, found that the 38% human-associated composition bias did not explain the weak environment–gene-content relationship. [src: ecotype_env_reanalysis] Its finding concerns gene-content correlation rather than visual embedding structure, so it cannot be used as a direct refutation of the embedding’s geographic or ecological organization.

**Phylogeny is broader, but environment dominates for a substantial minority**

The ecotype analysis reports that phylogeny dominated in 60.5% of species, whereas its environment-dominated proportion was 39.5%. [src: ecotype_analysis] It also found that environmental similarity was generally weaker than phylogenetic similarity for explaining genome-wide gene-content similarity, while environment nevertheless dominated in 39.5% of species. [src: ecotype_analysis] This is a within-analysis tension between a broad phylogenetic pattern and species-level exceptions, not evidence that environmental effects are absent. [src: ecotype_analysis]

**The reported partial-correlation medians are not directly comparable**

The original environment measure produced a median partial correlation of 0.0025, whereas the reanalysis reported 0.081 across all 183 species. [src: ecotype_analysis] [src: ecotype_env_reanalysis] The difference contradicts any direct comparison of their absolute effect sizes; the reanalysis attributes the discrepancy to different genome sets, full-genome extraction, and downsampling procedures. [src: ecotype_env_reanalysis]

## Possible Reconciliations

- **Hypothesis — outcome difference:** Geographic or visual embedding structure may be real while remaining weakly predictive of genome-wide gene content.
- **Hypothesis — composition and scope:** The 38% human-associated composition may affect projection geometry without explaining the reanalysis’s genome-level correlation result.
- **Hypothesis — sampling and measurement:** The medians 0.0025 and 0.081 may reflect genome-set, extraction, coverage, and downsampling differences rather than opposing biological effects.
- **Hypothesis — heterogeneous species effects:** Phylogeny may dominate across most species while environmental effects remain strong in the 39.5% environment-dominated subset.

## Resolving Work

- Recompute the embedding and environment–gene-content correlations on the identical genome set, retaining the 38% composition and then matching coverage criteria; test whether the correlation changes.
- Apply the original and reanalysis environmental measures to the same 183 species; compare partial-correlation medians under identical full-genome extraction and downsampling.
- Partition species by phylogeny-dominated versus environment-dominated status and test whether geographic embedding distance predicts gene content within each group.
- Remove or reweight human-associated genomes in sensitivity analyses; test whether geographic gradients and gene-content correlations change independently.
- Use matched species sets and bootstrap confidence intervals to test whether 60.5%, 39.5%, 0.0025, and 0.081 remain distinct under common sampling.
