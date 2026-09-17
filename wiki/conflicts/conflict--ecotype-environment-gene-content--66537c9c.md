<!-- tension-hash: 66537c9cf0b5949a -->
# Does environmental sampling carry a stronger environment–gene-content signal than human-associated sampling?

Two projects in this corpus disagree about whether environmental samples should — and do — show tighter coupling between where a genome came from and what genes it carries. One project characterizes the AlphaEarth embedding space (a learned numeric representation of a geographic location, so that two coordinates close in embedding space are environmentally similar) and finds that environmental samples spread far more across that space with distance than human-associated ones. The other project tested the prediction that this steeper environmental gradient should translate into a stronger environment-to-gene-content relationship, and found none. The disagreement matters because the whole ecotype programme on [[concepts/ecotype-environment-gene-content]] rests on the assumption that a better environmental predictor yields a better prediction of functional gene content; if that link fails, environmental embeddings cannot be used as a proxy for selective pressure.

## Evidence Sides

**Side A — the environmental embedding gradient is steep.** AlphaEarth embeddings show a 3.4x environmental geographic gradient, i.e. embedding distance between environmental samples grows 3.4-fold from nearby to intercontinental separations [src: env_embedding_explorer; ecotype_env_reanalysis]. This is a direct measurement over the embedding space itself and is not in dispute as a measurement.

**Side B — the gene-content correlation does not follow.** The ecotype reanalysis found no stronger environmental than human-associated gene-content correlation — a comparative null result, not a weaker-but-present difference — and reported median partial correlation 0.0025 (the correlation between environment similarity and gene-content similarity after controlling for other terms) in the prior AlphaEarth-based analysis, i.e. over that analysis's genome set rather than over the environmental subset that carries the 3.4x gradient [src: env_embedding_explorer; ecotype_env_reanalysis]. On this side, the steeper environmental gradient does not show up as a stronger environmental correlation.

Both sides note that these are not the same quantity: one measures embedding distance, the other measures embedding distance versus gene-content distance [src: env_embedding_explorer; ecotype_env_reanalysis].

## Possible Reconciliations

- *Hypothesis — different quantities.* The two results may be compatible because they are not measured on the same scale: Side A reports a ratio of embedding distances, Side B a partial correlation between environment similarity and gene-content similarity plus a comparative null, and a steeper spread in embedding distance need not raise that correlation.
- *Hypothesis — saturating signal.* Embedding distance may become environmentally uninformative beyond some separation, so the steep upper end of the gradient contributes spread without contributing selective contrast.
- *Hypothesis — gene content responds to axes the embedding does not encode.* Environmental selection on gene content may track local chemistry or host association rather than the landscape features the embedding captures.

## Resolving Work

- Recompute the partial correlation restricted to environmental samples only, with the same partial-correlation specification as the prior analysis, and ask whether the null result survives the restriction.
- Stratify embedding distance into distance bins and fit the embedding-versus-gene-content association within each bin, to test whether the association saturates rather than scaling with the gradient.
- Swap gene-content distance for a pathway-level or trait-level distance and re-test, to ask whether the null is specific to gene-level representation.
- Hold environment category fixed and vary geographic separation (and the reverse), to separate which of the two the embedding is actually tracking.
- Report the environmental and human-associated correlations side by side with matched sample counts, so the "no stronger" claim is tested at equal power rather than inferred.
