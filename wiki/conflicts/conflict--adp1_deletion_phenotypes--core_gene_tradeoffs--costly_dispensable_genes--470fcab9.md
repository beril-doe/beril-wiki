<!-- tension-hash: 7fcaa25a3c774ca3 -->
# Missing Perturbation Coverage: Conservation Signal or Measurement Artifact?

One project in this corpus reports the association at the heart of this page: in the ADP1 deletion collection, genes that are well annotated and pangenome-core (present in essentially all genomes of a species) are the genes most likely to be *present and measurable* in a genetic perturbation collection [src: adp1_deletion_phenotypes]. That project declines to adjudicate what the association means, and three neighbouring projects bound the interpretation from different directions without measuring collection coverage themselves. One reading treats coverage as a readout of biology: conserved genes are recoverable because they are real, intact, and well-behaved. The competing reading treats coverage as a readout of the experiment: conserved genes are recoverable because mutant construction and measurement succeed for them and because they are not lost to fragment misclassification. The disagreement matters because the two readings send opposite instructions to anyone reusing these collections: under the first, absence from a collection is evidence about a gene; under the second, absence is evidence about the assay. This page covers four distinct disagreements that share this root, all as stated on [[concepts/genetic-perturbation-coverage-bias]]: (1) the mechanism behind the missing-data pattern, (2) whether core enrichment implies low burden, (3) whether singleton neutrality is real, and (4) whether the costly–dispensable classification is robust enough to extend the argument.

## Evidence Sides

**Biological conservation drives coverage.** The ADP1 deletion-collection analysis reports an association between perturbation coverage, annotation quality, and pangenome-core status, and biological conservation is one of the candidate explanations it offers for that association [src: adp1_deletion_phenotypes]. Under this reading, coverage tracks which genes are genuinely conserved and functional.

**Technical difficulty and misclassification drive coverage.** The same report offers, as equally live alternatives, technical difficulty in constructing or measuring mutants and misclassified gene fragments — or some combination of these factors with conservation [src: adp1_deletion_phenotypes]. Crucially, the report does not establish which mechanism causes the missing-data pattern, so the association should not be interpreted as proof that evolutionary conservation directly determines deletion-mutant recovery [src: adp1_deletion_phenotypes]. This side is therefore not a rival finding but a declared non-identification: the study cannot separate the mechanisms with the data it has.

**Core enrichment in a collection implies low burden.** The ADP1 collection indicates that successful coverage is enriched among core genes [src: adp1_deletion_phenotypes]. Read naively, this invites the inference that core genes are the tractable, low-cost, near-universally-essential fraction of the genome.

**Core genes carry substantial laboratory burden.** The broader trade-off analysis shows that core genes can carry substantial laboratory burden and condition-specific costs [src: core_gene_tradeoffs]. This is not a direct contradiction of the coverage result, because the two studies measure different outcomes, but it draws a hard boundary on interpretation: core enrichment in a collection cannot by itself establish either low burden or universal essentiality [src: adp1_deletion_phenotypes, core_gene_tradeoffs].

**Singleton neutrality is a genuine null result.** The Fitness Browser analysis reports that singleton genes — genes found in only one genome — were near-neutral under tested conditions [src: fitness_effects_conservation].

**Singleton neutrality is a coverage failure.** The same analysis notes that this neutrality may instead reflect inadequate transposon coverage in RB-TnSeq (random barcode transposon sequencing, in which a pooled library of barcoded transposon insertion mutants is assayed for fitness), and the analysis does not distinguish these explanations [src: fitness_effects_conservation]. A gene that is thinly sampled by insertions will look neutral whether or not it is.

**Mobile-element enrichment narrows interpretation toward horizontally acquired DNA.** Mobile-element enrichment and poor annotation narrow the biological interpretation of costly non-conserved genes toward horizontally acquired DNA [src: costly_dispensable_genes]. This is a narrowing of interpretation, not a demonstration that the class is horizontally acquired.

**The costly–dispensable classification is fragile.** The same project adds a boundary rather than a resolution. Its classification of burden used max_fit > 1 in any experiment, so a single experiment can classify a gene as burdensome and the result is sensitive to fitness-data noise; its 90% identity DIAMOND threshold may also miss recently acquired genes with low sequence similarity [src: costly_dispensable_genes]. DIAMOND is a fast protein sequence-similarity search program, and in this project the 90% identity cutoff governs the linking of Fitness Browser genes to pangenome gene clusters — that is, it controls how conservation and dispensability are assigned, not how ortholog groups are built [src: costly_dispensable_genes]. Consequently the horizontal-acquisition reading does not establish that such genes are systematically absent from perturbation collections [src: costly_dispensable_genes].

## Possible Reconciliations

These are hypotheses, not findings; none is established by the cited reports.

- **Confounding rather than competition (mechanism).** Conservation, annotation quality, and constructability may be correlated causes rather than rivals: conserved genes are longer-studied, hence better annotated, hence better targeted by construction primers and better resolved against fragment calls. If so, both sides are right and neither is separable without an intervention that breaks the correlation [src: adp1_deletion_phenotypes].
- **Different outcome variables (burden).** The coverage result and the trade-off result may both hold because presence in a collection measures constructability while burden measures fitness cost in a condition; a gene can be easy to delete and expensive to carry. The tension then dissolves into a scope difference, which is exactly the boundary the concept page draws [src: adp1_deletion_phenotypes, core_gene_tradeoffs].
- **Detection floor (singletons).** Near-neutrality and insufficient insertion density are indistinguishable at low coverage; both sides could be right for different singletons, with the mixture unknown until per-gene insertion counts are conditioned on [src: fitness_effects_conservation].
- **Definitional fragility (costly–dispensable).** A max_fit > 1 single-experiment rule and a 90% identity linking threshold could each distort the costly–dispensable class — the first by admitting noise-driven calls, the second by missing recently acquired genes with low sequence similarity — so the mobile-element signal may be a robust core inside a noisy shell rather than a property of the whole class [src: costly_dispensable_genes].

## Resolving Work

**Mechanism behind the missing-data pattern**
- Compare, gene by gene, the ADP1 genes absent from the deletion collection against construction-attempt records: if absence tracks documented construction failures rather than core status, the technical explanation gains [src: adp1_deletion_phenotypes].
- Re-call the ADP1 gene set with an independent structural annotation and re-test the coverage–core association after removing calls flagged as fragments, to quantify how much of the pattern is misclassification [src: adp1_deletion_phenotypes].
- Fit coverage as a function of core status with annotation quality held fixed; a surviving core effect is the part conservation could plausibly own [src: adp1_deletion_phenotypes].

**Does core enrichment imply low burden?**
- Intersect the ADP1 covered-gene set with the trade-off analysis's burdensome core genes and report the overlap directly, rather than inferring burden from coverage [src: adp1_deletion_phenotypes, core_gene_tradeoffs].
- Measure burden for covered core genes in the same organism and conditions in which coverage was scored, so the two outcome variables are no longer measured on different systems [src: core_gene_tradeoffs].
- State and test the specific prediction that separates the sides: if core enrichment implied low burden, condition-specific costs among covered core genes should be rare [src: adp1_deletion_phenotypes, core_gene_tradeoffs].

**Is singleton neutrality real?**
- Stratify the singleton fitness results by per-gene insertion counts and report neutrality only within the well-sampled stratum [src: fitness_effects_conservation].
- Power-analyse the tested conditions: establish the smallest fitness effect detectable per singleton, and report how many singletons had the power to reject neutrality at all [src: fitness_effects_conservation].
- Assay a sample of singletons with targeted, non-transposon perturbations, where coverage is guaranteed by construction, and ask whether neutrality survives [src: fitness_effects_conservation].

**Is the costly–dispensable class robust?**
- Replace the max_fit > 1 in any experiment rule with a replicate-supported or multi-experiment criterion and re-run the mobile-element and annotation comparisons; report how much of the signal survives [src: costly_dispensable_genes].
- Re-run the Fitness-Browser-to-pangenome linking below the 90% identity DIAMOND threshold and quantify how many genes change conservation status, which bounds the missed-recent-acquisition error [src: costly_dispensable_genes].
- Test the outstanding question directly — whether costly non-conserved genes are systematically absent from perturbation collections — by intersecting the costly–dispensable set with collection membership, since the current evidence does not establish this [src: costly_dispensable_genes].
