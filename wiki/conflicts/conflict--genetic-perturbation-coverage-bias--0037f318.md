<!-- tension-hash: 0037f3184e555722 -->
# Does Core-Gene Enrichment in Perturbation Collections Signal Low Burden or Mask Hidden Costs?

Perturbation collections are libraries of mutants made by gene deletion or by transposon insertion, in which a mobile DNA element is inserted into a gene to disrupt it. They are used to infer what genes do. Projects in the corpus agree that core (conserved) genes behave distinctively, but they point in different interpretive directions. In the ADP1 deletion collection, successful coverage is enriched among core genes. A broader trade-off analysis shows that core genes can carry substantial laboratory burden and condition-specific costs [src: adp1_deletion_phenotypes, core_gene_tradeoffs]. These studies measure different outcomes, so this is not a direct contradiction. It does set a boundary on interpretation: core enrichment in a collection cannot by itself establish either low burden or universal essentiality [src: adp1_deletion_phenotypes, core_gene_tradeoffs]. A related ambiguity affects singleton genes, a non-core conservation class. This matters for the parent concept, [[concepts/genetic-perturbation-coverage-bias]], because coverage patterns could be misread as biological signal.

## Evidence Sides

**Side A: Collection coverage is enriched among core genes.**
The ADP1 collection indicates that successful coverage, meaning genes for which mutants were recovered, is enriched among core genes [src: adp1_deletion_phenotypes, core_gene_tradeoffs]. Read naively, this enrichment could be taken as a sign that core genes carry low laboratory burden.

**Side B: Core genes can carry substantial laboratory burden and condition-specific costs.**
The broader trade-off analysis shows that core genes can impose burden under laboratory conditions and incur costs that depend on condition [src: adp1_deletion_phenotypes, core_gene_tradeoffs]. This argues against reading core enrichment in a collection as evidence of low burden.

**Related side: Singleton neutrality is ambiguous.**
In the Fitness Browser, a database of transposon-mutant fitness measurements across bacteria, singleton genes were near-neutral under tested conditions [src: fitness_effects_conservation]. This neutrality may reflect a genuine lack of measured effect or inadequate transposon coverage. The analysis does not distinguish between these explanations [src: fitness_effects_conservation].

## Possible Reconciliations

- **Hypothesis 1:** The studies measure different outcomes [src: adp1_deletion_phenotypes, core_gene_tradeoffs]. The hypothesis is that mutant recoverability and condition-specific burden are independent properties, so core genes could be both well covered and costly. This is untested.
- **Hypothesis 2:** Collection construction favors annotated, conserved genes. That bias would make coverage a property of the collection rather than of gene burden. This is a hypothesis.
- **Hypothesis 3:** Singleton near-neutrality partly reflects sparse transposon coverage rather than biology. This hypothesis is untested, because the analysis does not separate the two explanations [src: fitness_effects_conservation].

## Resolving Work

- **Recoverability versus burden:** Pair ADP1 mutant-recovery status with per-condition fitness for the same genes. Use a stratified comparison (testing the association separately within each conservation class) to ask whether recoverability among core genes is independent of measured burden.
- **Coverage-controlled neutrality:** Use Fitness Browser insertion-density data for singleton versus core genes. Re-test neutrality restricted to genes with adequate insertion coverage, to ask whether singleton near-neutrality persists once coverage is controlled.
- **Condition specificity:** Apply trade-off fitness profiles across the conditions tested for core genes. Ask whether the burden is concentrated in a subset of conditions that collection-based studies do not sample.
- **Annotation as a confounder:** Fit a joint model of mutant coverage, a single regression that estimates the effects of annotation status and conservation class together. Ask whether core enrichment in collections is explained by annotation rather than conservation.
