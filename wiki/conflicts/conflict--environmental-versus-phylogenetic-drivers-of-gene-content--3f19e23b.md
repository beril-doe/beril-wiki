<!-- tension-hash: 3f19e23b319150ff -->
# Weak Environment Signal Versus Strong Niche-Breadth Signal in Gene Content

The disagreement concerns how much environment tells us about bacterial gene content, drawing on [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]]. One result finds that environment barely explains gene content (median partial correlation 0.0025) [src: discoveries], while another finds that niche breadth from embeddings correlates with pathway completeness (r=0.392). [src: discoveries] A partial correlation measures association between two variables after adjusting for other variables. A correlation coefficient r measures the strength and direction of a linear association. The tension also covers whether clinical sampling bias explains the weak signal, and whether openness relates to environment, phylogeny or pathway variability. It matters because readings of environmental effects depend on which response variable and species set is used.

## Evidence Sides

**Side A: environment explains little gene content**
- Environment barely explains gene content, with a median partial correlation of 0.0025. [src: discoveries]
- The env_embedding_explorer entry proposes that clinical bias may partly explain the weak environment signal. [src: discoveries, env_embedding_explorer]
- The reanalysis found the opposite pattern and a non-significant difference (p=0.83). A p-value is the probability of a difference at least this large under the null hypothesis of no difference. This is a null result, so it does not support the clinical-bias explanation. [src: discoveries, ecotype_env_reanalysis]
- Openness shows no significant relation to the environment or phylogeny effects. [src: discoveries]

**Side B: ecological breadth tracks metabolic content**
- Niche breadth from embeddings correlates with pathway completeness (r=0.392). [src: discoveries]
- Openness correlates with pathway variability. The report calls this much stronger than the earlier null result. [src: discoveries]

The source text says the first pair of results use different response variables and species sets, so they do not directly conflict. [src: discoveries]

## Possible Reconciliations

- **Hypothesis: different response variables.** Pairwise gene-content similarity may respond weakly to environment, while pathway completeness responds more strongly to niche breadth. This is untested here.
- **Hypothesis: different species sets.** The species behind each result may differ in ways that change the apparent strength of environmental effects.
- **Hypothesis: clinical bias is partial or confounded.** The bias idea was proposed and then met a non-significant, opposite-direction reanalysis, so it stays a hypothesis, not an established explanation.
- **Hypothesis: openness acts through pathway variability.** Openness may relate to pathway variability but not to the environment or phylogeny effects, which would explain the mixed results.

## Resolving Work

- Data: one shared species set with both partial correlations and pathway completeness. Method: compute both responses on identical species. Question: does the contrast persist when species sets match?
- Data: niche breadth and the environment effect per species. Method: relate them directly, for example by rank correlation. Question: do broad-niche species show stronger or weaker environment effects?
- Data: genomes stratified by sample type. Method: repeat the pathway-completeness analysis within each stratum. Question: does the niche-breadth correlation depend on clinical sampling?
- Data: openness, pathway variability and the environment and phylogeny effects. Method: a joint model on the same species. Question: why does openness show a null result for one and a stronger association for the other?
- Data: the ecotype analysis restricted to environmental samples, as env_embedding_explorer proposed. Method: rerun the partial correlations. Question: does the signal change from the weak value reported?
