<!-- tension-hash: 59d3cb46bec0b5cf -->
# Clade-Level Support Versus Pathway-Level and Gene-Class Doubts in Black Queen Gene Loss

The Black Queen Hypothesis proposes that costly genes can be lost adaptively when community members supply their functions as public goods. Projects in the corpus disagree on whether the data show this. One project finds clade-level support from pangenome openness (the share of a species' gene repertoire that is not shared by all its genomes) but no pathway-level separation. Another finds that the candidate genes are mostly selfish elements, not metabolic genes. This matters because most support is correlational, and the question of what the candidate genes are stays open. The tension comes from [[concepts/gene-loss-and-black-queen-hypothesis-tests]].

## Evidence Sides

**Side A: signals consistent with Black Queen at the clade level**

- The pangenome-openness correlation supports the Black Queen framework. It is a Spearman correlation (ρ, a rank-based association measure) of ρ = 0.69 across n = 22 clades. [src: metabolic_capability_dependency]
- The report cites Morris et al. (2012) and D'Souza et al. (2014) as showing gene loss in natural and experimental populations. It contrasts this with its own species-level result. [src: metabolic_capability_dependency]

**Side B: no separation by pathway, and candidates that are not metabolic**

- Pathway conservation does not distinguish latent pathways (complete but fitness-neutral) from active pathways. This is a null result, with p = 0.94. [src: metabolic_capability_dependency]
- The report suggests the signal lies in genome dynamics and community context, not in per-pathway conservation ratios. This is a suggestion, not a tested result. [src: metabolic_capability_dependency]
- The costly+dispensable genes are called Black Queen candidates, yet they are mostly selfish elements and not metabolic genes. [src: costly_dispensable_genes]

## Possible Reconciliations

- **Hypothesis 1: scale dependence.** Black Queen loss may act on whole-genome dynamics in a clade and leave no trace in per-pathway conservation ratios. This restates the report's own suggestion and is untested. [src: metabolic_capability_dependency]
- **Hypothesis 2: different gene classes.** The clade-level signal and the candidate gene list may describe different gene sets. The first may reflect pathway-level streamlining, and the second mostly selfish elements. Nothing in the evidence tests this.
- **Hypothesis 3: earlier stage of loss.** Costly genes that are still present may be caught before loss. This is speculation. It does not show that metabolic loss is occurring.

## Resolving Work

- **Data:** the 22 clades with pangenome openness values. **Method:** repeat the correlation after excluding selfish-element genes from the openness measure. **Question:** does the association survive when mobile elements are removed?
- **Data:** the costly+dispensable gene set. **Method:** annotate each gene as metabolic or mobile and count the classes. **Question:** do any metabolic candidates remain that fit the Black Queen predictions?
- **Data:** latent and active pathway sets. **Method:** compare patterns of gain and loss across the clade phylogeny, not conservation ratios. **Question:** does genome dynamics separate the classes where conservation (p = 0.94) did not?
- **Data:** community composition for each clade. **Method:** test whether latent-pathway fraction tracks the presence of partners that could supply the function. **Question:** is community context the missing signal?
- **Data:** closely related genomes that differ in pathway presence. **Method:** compare loss events with and without a plausible provider. **Question:** is loss directly observed, not inferred from correlation?
