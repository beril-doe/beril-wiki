<!-- tension-hash: 80bc875463e3cae1 -->
# Tension: Do Cofitness and Module Methods Assign Gene Function, or Only Nominate Processes?

The corpus disagrees about what class of claim a fitness-derived inference licenses. One line of evidence benchmarks fitness-based annotation against gene-level identity — a specific KEGG KO (KEGG Orthology identifier, a molecular-function label) per gene — and finds it near-worthless, with module-ICA (independent component analysis, which decomposes fitness matrices into co-varying gene modules) and cofitness voting scoring <1% strict KEGG KO precision against ortholog transfer's 95.8% [src: fitness_modules]. Another line treats process-level and hypothesis-level output as the intended product, not a failed approximation of identity. The disagreement matters because it sets the admissible claim type for every downstream page in [[concepts/cofitness-network-architecture]]: whether a cofitness neighbor is evidence *that a gene does X* or only evidence *that a gene participates in X*.

## Evidence Sides

**Gene-level identity is the benchmark, and fitness methods fail it.** Strict KEGG KO precision was <1% for both module-ICA and cofitness voting — a majority vote over the annotations of a gene's strongest cofitness partners — whereas ortholog transfer (propagating annotation from a characterized ortholog) achieved 95.8% precision, 91.2% coverage, and 0.934 F1 — the harmonic mean of precision and coverage [src: fitness_modules]. On this standard, fitness-derived assignments are not gene function predictions.

**Dark-matter evidence yields hypotheses, not step assignments.** Functional-dark-matter results from GapMind (which maps genes to steps in defined catabolic pathways) and from protein-domain analysis, together with truly-dark evidence from eggNOG (an orthologous-group database) and phenotype clues, identify hypotheses rather than direct gene-to-step assignments [src: functional_dark_matter; truly_dark_genes].

**Donor inference is exploratory, not identification.** The Agora's M26 tree-based donor inference — reconstructing likely gene-transfer donors from phylogenetic placement — is exploratory rather than donor identification [src: gene_function_ecological_agora].

## Possible Reconciliations

- *Hypothesis:* the two sides measure different targets, and the <1% strict KEGG KO precision is a category mismatch rather than a failure rate — module membership encodes process co-regulation, which strict KO matching cannot score [src: fitness_modules].
- *Hypothesis:* claim strength is a pipeline stage, with fitness and tree-based signals nominating candidates and ortholog transfer adjudicating those that have orthologs at all — leaving the orthologless remainder permanently in hypothesis space [src: fitness_modules; truly_dark_genes].
- *Hypothesis:* the disagreement is about reporting conventions, and both sides agree once every inference is emitted with an explicit claim type ("involved in", "candidate for", "assigned").

## Resolving Work

- Re-score module-ICA and cofitness voting against process-level ground truth (KEGG pathway or module membership) rather than strict KO identity, on the same gene set benchmarked in [src: fitness_modules]: does precision rise when the target matches the claim type?
- Restrict the ortholog-transfer benchmark to genes lacking orthologs and re-run all four methods: what is the achievable precision where the 95.8%-precision method cannot apply [src: fitness_modules]?
- Test GapMind and domain-based dark-matter hypotheses against independent phenotype records [src: functional_dark_matter; truly_dark_genes]: what fraction of hypotheses survive, i.e. what is the conversion rate from nomination to assignment?
- Define a hold-out donor set with independently known transfer history and score M26 tree-based inference on it [src: gene_function_ecological_agora]: at what phylogenetic rank, if any, does exploratory output become identification?
- Annotate every fitness-derived prediction in the corpus with a claim-type field and re-audit the concept pages that cite them for overstatement.
