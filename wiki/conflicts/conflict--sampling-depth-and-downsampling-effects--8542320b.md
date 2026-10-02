<!-- tension-hash: 8542320b237088a6 -->
# Does Differential Missingness Explain the Weak Environment–Gene-Content Signal, or Merely Accompany It?

Two projects in this corpus disagree about what to make of uneven missing data across ecological groups. Missingness here means NaN values — "not a number", i.e. absent entries in the AlphaEarth embedding vectors or in derived correlation statistics — and it is not distributed evenly: Environmental species had a 21% NaN rate compared with 7% for Human-associated species. [src: ecotype_env_reanalysis] If missingness were the driver, filtering out more Environmental species should have left a cleaner, stronger environmental signal behind; it did not. [src: ecotype_env_reanalysis] Whether that non-result retires missingness as an explanation, or whether unaccounted missingness keeps the question open, is the disagreement recorded here. It matters because the reanalysis concludes that missingness, sampling depth, and ecological classification must be analyzed jointly rather than treated as interchangeable explanations. [src: ecotype_env_reanalysis] The tension belongs to [[concepts/sampling-depth-and-downsampling-effects]].

## Evidence Sides

**Missingness is real but does not carry the signal (ecotype_env_reanalysis).** Environmental species had a 21% NaN rate compared with 7% for Human-associated species, yet removing more Environmental species did not produce the expected stronger environmental signal. [src: ecotype_env_reanalysis] The conclusion drawn is not that missingness is absent or harmless, but that missingness, sampling depth, and ecological classification must be analyzed jointly rather than treated as interchangeable explanations. [src: ecotype_env_reanalysis] The null result is reported as a null: no stronger environmental correlation emerged, and none is claimed.

**Missingness is not yet fully inventoried (env_embedding_explorer).** The explorer adds 3,838 records with at least one embedding NaN and uneven metadata coverage, refining rather than resolving this tension. [src: env_embedding_explorer] This side does not assert that missingness explains the weak signal; it records a differently counted layer of missing data — records carrying at least one NaN embedding dimension, alongside patchy metadata — set against the species-level NaN rates above, so the question is not yet closed.

## Possible Reconciliations

- *Hypothesis:* the two measurements are at different granularities — species-level NaN rates versus record-level embedding NaNs plus metadata gaps — so both can hold simultaneously without either being wrong.
- *Hypothesis:* missingness biases group comparisons in a direction that is real but small relative to whatever suppresses the environment–gene-content relationship, leaving the null intact.
- *Hypothesis:* missingness and ecological classification are entangled, such that filtering on one silently re-weights the other and no single-factor removal can isolate an effect.

## Resolving Work

- Re-run the group comparison with the explorer's 3,838 NaN-bearing records [src: env_embedding_explorer] flagged per-dimension rather than dropped, and ask whether the Environmental/Human-associated gap moves at all.
- Model NaN status as an outcome, not a filter: does ecological classification predict missingness after conditioning on sampling depth, and with what residual?
- Impute or mask missing embedding dimensions under several schemes and ask whether the direction of the environmental result is scheme-dependent.
- Quantify metadata coverage separately from embedding completeness [src: env_embedding_explorer], and test whether the 21%-versus-7% contrast [src: ecotype_env_reanalysis] survives conditioning on metadata completeness alone.
