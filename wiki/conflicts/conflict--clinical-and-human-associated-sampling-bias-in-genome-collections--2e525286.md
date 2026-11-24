<!-- tension-hash: 2e525286ad489a88 -->
# Clinical Sampling Bias: Explanation for a Weak Environment Signal, or Not?

Genome collections contain many human-associated isolates, and one project proposed that this skew may partly explain why environment (as encoded by AlphaEarth satellite-based embeddings) predicts gene content only weakly. [src: env_embedding_explorer] A reanalysis finds that the bias does not account for the weak signal. [src: ecotype_env_reanalysis] A second disagreement concerns scope: the 38% human-associated figure describes the AlphaEarth subset and may not represent the overall NCBI or pangenome population. [src: env_embedding_explorer] This matters because the counts are well documented, while the effect of the skew on downstream conclusions is mostly argued rather than tested. Both points come from [[concepts/clinical-and-human-associated-sampling-bias-in-genome-collections]].

## Evidence Sides

**Side A: clinical bias may partly explain the weak signal**

- The env_embedding_explorer report proposes that clinical bias may partly explain the weak environment signal. [src: env_embedding_explorer]
- The 38% human-associated figure describes the AlphaEarth subset (genomes that have AlphaEarth embeddings) and may not represent the overall NCBI or pangenome population. [src: env_embedding_explorer] This is a caveat on generalisation and is not a measured effect.

**Side B: clinical bias does not explain it**

- The ecotype reanalysis finds the bias does not account for the weak signal. [src: ecotype_env_reanalysis] This is reported as a null result: the hypothesis that bias explains the signal was not supported.
- The Pseudomonas figures describe one genus only, so they do not by themselves settle the question for other taxa. [src: genotype_to_phenotype_enigma, pseudomonas_carbon_ecology]

## Possible Reconciliations

- **Hypothesis: different questions.** The first report offers a proposal about dilution by clinical genomes, while the reanalysis tests it directly. The proposal may simply have been wrong for this subset.
- **Hypothesis: scope limits.** The 38% figure is specific to the AlphaEarth subset, so the bias may matter more or less in the full NCBI or pangenome population. [src: env_embedding_explorer]
- **Hypothesis: genus-specific patterns.** The Pseudomonas results describe one genus and may not transfer to other groups. [src: genotype_to_phenotype_enigma, pseudomonas_carbon_ecology]

None of these is established, and none should be read as favouring either side.

## Resolving Work

- **Data:** the AlphaEarth subset and the wider NCBI genome set. **Method:** compare the human-associated fraction in each. **Question:** does the 38% figure hold outside the subset?
- **Data:** the ecotype reanalysis species groups. **Method:** repeat the partial-correlation comparison, which measures environment against gene content while controlling for other factors, on an independently built subset. **Question:** does the null result replicate?
- **Data:** genomes from several genera beyond Pseudomonas. **Method:** run the same environment versus gene-content test genus by genus. **Question:** is the null result consistent across genera?
- **Data:** genomes with and without human-associated labels. **Method:** subsample to equalise the clinical fraction, then re-estimate the signal. **Question:** does altering the skew change the weak environment signal at all?
