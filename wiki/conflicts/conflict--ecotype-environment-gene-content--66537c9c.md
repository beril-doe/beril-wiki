<!-- tension-hash: 66537c9cf0b5949a -->
# Does a Strong Geographic Signal in AlphaEarth Embeddings Mean Environment Shapes Gene Content More Strongly?

Two projects disagree on whether the strength of environmental signal in AlphaEarth embeddings predicts how strongly environment correlates with gene content. One project reports a 3.4x environmental geographic gradient in these embeddings. A reanalysis expected that signal to carry over to gene content but found no stronger environmental than human-associated gene-content correlation. It also reported a median partial correlation of 0.0025 in the prior AlphaEarth-based analysis [src: env_embedding_explorer; ecotype_env_reanalysis]. Partial correlation is the association between two variables after controlling for a third. The question matters for [[concepts/ecotype-environment-gene-content]] because it bears on whether embedding-based environment similarity can be read as a predictor of gene-content differences.

## Evidence Sides

**Side A: embeddings carry a strong environmental geographic signal.** AlphaEarth shows a 3.4x environmental geographic gradient [src: env_embedding_explorer; ecotype_env_reanalysis]. This measures how embedding distance changes with geographic separation. It is a property of the environmental descriptors themselves. It is not a measurement of genome content.

**Side B: environment–gene-content correlation is not stronger for environmental species.** The ecotype reanalysis found no stronger environmental than human-associated gene-content correlation. This is a null result for the predicted difference [src: env_embedding_explorer; ecotype_env_reanalysis]. The reanalysis reported a median partial correlation of 0.0025 in the prior AlphaEarth-based analysis [src: env_embedding_explorer; ecotype_env_reanalysis].

**Framing note.** The two sides measure embedding distance versus gene-content distance, not the same phenomenon [src: env_embedding_explorer; ecotype_env_reanalysis]. The tension therefore concerns an expected link between the two quantities, not two contradictory measurements of one quantity.

## Possible Reconciliations

- **Hypothesis 1: decoupled layers.** Embedding geography and gene-content divergence may simply be independent. Environments can differ strongly in AlphaEarth space while species' gene content responds weakly, or responds on timescales the embeddings do not capture.
- **Hypothesis 2: dilution by sample composition.** The comparison sets may mix samples whose environmental descriptors are near-interchangeable. That mixing would mask a real environment–gene-content relationship that a restricted subset could reveal.
- **Hypothesis 3: wrong grain of measurement.** Whole gene-content distance may average over the few functional categories that do respond to environment. A signal in specific gene families could then be lost in a genome-wide statistic.

Each is a hypothesis, not an established finding.

## Resolving Work

- Repeat the AlphaEarth-based partial-correlation analysis restricted to environmental samples only. This asks whether the environment–gene-content correlation is stronger when human-associated samples are left out.
- Directly correlate pairwise AlphaEarth embedding distance with pairwise gene-content distance within species, stratified by sample source. This asks whether the embedding gradient predicts gene-content divergence at all.
- Replace whole-genome gene-content distance with presence/absence of functionally annotated gene families, and test each family against embedding distance with false-discovery-rate (FDR) control, which limits the expected share of false positives. This asks whether environment signal is concentrated in specific functions.
- Compare embedding-based environment similarity against harmonized categorical environment labels as predictors of gene content in the same genome set. This asks whether the weak signal reflects the AlphaEarth proxy itself rather than biology.
