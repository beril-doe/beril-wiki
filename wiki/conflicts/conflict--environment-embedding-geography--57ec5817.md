<!-- tension-hash: 57ec58173a2616fe -->
# Do environment embeddings carry gene-content signal, or only geographic structure?

Satellite-derived environment embeddings behave as ecology should — similarity falls off with geographic separation (distance-decay) — yet when the same embeddings are scored against microbial gene content, the association is close to nothing: a median partial correlation (the correlation of environment with gene content after removing phylogenetic relatedness) of 0.0025 [src: env_embedding_explorer; ecotype_analysis]. A reanalysis restricted to environmental species did not rescue the signal, and its own environmental median does not match the earlier one. This matters because the whole premise of embedding-based ecology in [[concepts/environment-embedding-geography]] — that remote-sensed environment is a usable proxy for the selective regime a genome experiences — rests on which of these readings is right.

## Evidence Sides

**Embeddings encode real spatial structure.** Embeddings show clear geographic distance-decay, which is the expected behaviour of a variable tracking environment; the disagreement is that environment similarity nonetheless had median partial correlation 0.0025 with gene content [src: env_embedding_explorer; ecotype_analysis]. On this reading the embedding is informative and the failure lies downstream — in the genome set being compared, not in the environmental variable.

**Phylogeny, not environment, tracks gene content.** The ecotype analysis found environmental median 0.0025 and phylogenetic median 0.0143 [src: ecotype_env_reanalysis; ecotype_analysis]. Environment is not merely weak here; it is weaker than relatedness on the same pairs, so any environment-first account of gene content has to explain why the phylogenetic term outranks it.

**Restricting to environmental species does not produce the expected signal, and shifts the estimate.** The environmental-only reanalysis found median 0.051 versus 0.084 for human-associated species, U=1536, p=0.83 (Mann-Whitney U, a rank-based test of whether one group's values exceed another's) [src: ecotype_env_reanalysis; ecotype_analysis]. This is a null result, and it points opposite to the prediction that environmental species would score higher. It also places the environmental median at 0.051, where the ecotype analysis reports 0.0025 for nominally the same quantity [src: ecotype_env_reanalysis; ecotype_analysis].

## Possible Reconciliations

- *Hypothesis:* the two environmental medians differ because of analysis construction rather than biology — the studies used different genome sets, species filters, and downsampling, so the estimates cannot be reconciled by averaging [src: ecotype_env_reanalysis; env_embedding_explorer].
- *Hypothesis:* the geographic structure in the embeddings and their near-zero partial correlation with gene content are measuring different things, so both observations could hold at once; no project in this corpus states a mechanism for this, and it remains an untested proposition.
- *Hypothesis:* filtering to environmental species removes dilution but simultaneously removes statistical power, leaving a test that is null for sampling reasons rather than ecological ones. Only the null itself is sourced — median 0.051 versus 0.084, U=1536, p=0.83 [src: ecotype_env_reanalysis; ecotype_analysis]; neither the dilution premise nor the power premise is asserted by any project here, so this hypothesis is untested.

## Resolving Work

- Re-run both pipelines on a single frozen genome set with one species filter and one downsampling rule, asking whether 0.0025 and 0.051 converge when construction is held fixed [src: ecotype_env_reanalysis; env_embedding_explorer].
- Report per-species partial correlations with confidence intervals, not medians alone, to establish whether the environmental distribution is genuinely centred near zero or merely wide.
- Power-analyse the environmental-versus-human comparison at its actual species counts: what effect size could U=1536, p=0.83 have detected [src: ecotype_env_reanalysis; ecotype_analysis]?
- Substitute measured in-situ environmental variables for embeddings on the same pairs, testing whether the weak signal is an embedding-resolution limit or a real absence.
- Stratify by gene category (core versus accessory) to test whether environment outranks the phylogenetic median of 0.0143 in any subset [src: ecotype_env_reanalysis; ecotype_analysis].
