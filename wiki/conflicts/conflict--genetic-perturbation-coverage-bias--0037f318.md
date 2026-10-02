<!-- tension-hash: 0037f3184e555722 -->
# Core-Gene Enrichment in Perturbation Collections: Recoverability Signal, Burden Signal, or Coverage Artifact?

Two projects in this corpus describe core genes — genes present across most genomes in a comparison set — in ways that pull against each other. One reports that a deletion collection's successful coverage is enriched among core genes; another reports that core genes can be substantially burdensome in the laboratory and carry condition-specific costs. A third result, that singleton genes appear near-neutral under tested conditions, adds an interpretive ambiguity of the same shape. Nothing here is a logical contradiction, but the combination bounds what any single perturbation collection can be used to argue: whether observed core enrichment is a statement about gene biology or about what the construction method could recover. This tension is recorded on [[concepts/genetic-perturbation-coverage-bias]].

## Evidence Sides

**Coverage is enriched among core genes.** The ADP1 deletion collection indicates that successful coverage — which genes were recovered as viable, scorable mutants — is enriched among core genes. [src: adp1_deletion_phenotypes]

**Core genes carry laboratory burden and condition-specific costs.** The broader trade-off analysis shows that core genes can carry substantial laboratory burden and condition-specific costs, so membership in the core set does not imply that a gene is cheap to keep or uniformly required. [src: core_gene_tradeoffs]

**The two measure different outcomes, which sets a boundary rather than a verdict.** This is not a direct contradiction because the studies measure different outcomes; the consequence is that core enrichment in a collection cannot by itself establish either low burden or universal essentiality. [src: adp1_deletion_phenotypes, core_gene_tradeoffs]

**Singleton neutrality is ambiguous between biology and coverage.** The Fitness Browser result that singleton genes — genes with no detected homolog elsewhere — were near-neutral under tested conditions is a null result whose cause is undetermined: neutrality may represent genuine lack of measured effect or inadequate transposon coverage, and the analysis does not distinguish these explanations. [src: fitness_effects_conservation]

## Possible Reconciliations

- *Hypothesis:* the two findings describe separate stages of the same pipeline — recoverability determines which genes enter a collection, while burden describes how those genes behave once assayed — so core enrichment and core burden could both hold without either being wrong.
- *Hypothesis:* condition dependence absorbs the apparent conflict, with core genes being reliably recoverable under permissive construction conditions yet costly only in a subset of assayed conditions.
- *Hypothesis:* the singleton null is coverage-limited rather than biological, in which case the same coverage mechanism that enriches core genes in a collection would also depress detectable effects among singletons, making both observations one artifact.

## Resolving Work

- Per-gene mutant-recovery records from the ADP1 collection, cross-tabulated against core/non-core status and against attempted-but-failed constructions: does enrichment persist when failed attempts are the denominator rather than recovered mutants?
- Insertion-density statistics per gene from the transposon libraries underlying the Fitness Browser, compared between singleton and core genes: is singleton near-neutrality accompanied by lower usable coverage?
- Condition-resolved burden calls for genes that are both core and successfully recovered, to test whether recoverability and burden are independent properties or trade off.
- Reconstruction of a coverage-matched gene set — core and non-core genes sampled at equal insertion density — re-scored for fitness effects, asking whether the conservation gradient survives coverage matching.
- Independent, non-transposon perturbation of a sample of singleton genes, to test the null directly rather than inferring it from libraries with unknown coverage.
