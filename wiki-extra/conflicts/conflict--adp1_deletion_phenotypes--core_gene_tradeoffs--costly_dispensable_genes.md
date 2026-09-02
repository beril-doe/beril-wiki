<!-- tension-hash: 7fcaa25a3c774ca3 -->
# Does perturbation coverage reflect biological conservation or technical bias?

The disagreement concerns how to interpret the association between perturbation coverage, gene annotation, and pangenome-core status. One interpretation treats enrichment of successful coverage among core genes as evidence that biologically conserved genes are more recoverable, while another emphasizes construction difficulty, measurement limits, fragment misclassification, and incomplete experimental coverage. This matters because collection-level coverage patterns may otherwise be mistaken for evidence about gene essentiality, burden, or evolutionary importance. See [[concepts/genetic-perturbation-coverage-bias]].

## Evidence Sides

**Biological conservation explains coverage enrichment**

The ADP1 collection indicates that successful coverage is enriched among core genes. This pattern is consistent with biological conservation contributing to whether genes can be recovered in deletion-mutant collections. However, the report does not establish which mechanism causes the missing-data pattern, and the association should not be interpreted as proof that evolutionary conservation directly determines deletion-mutant recovery. [src: adp1_deletion_phenotypes]

The Fitness Browser result that singleton genes were near-neutral under tested conditions creates a related possibility: genes that appear weakly constrained may genuinely lack measured effects under the tested conditions. [src: fitness_effects_conservation]

**Technical and measurement factors explain coverage gaps**

The same observed association could reflect technical difficulty in constructing or measuring mutants, misclassified gene fragments, or some combination of these factors, rather than biological conservation alone. [src: adp1_deletion_phenotypes] Neutrality among singleton genes may also represent inadequate transposon coverage, and the analysis does not distinguish this explanation from a genuine lack of measured effect. [src: fitness_effects_conservation]

Core enrichment does not establish either low burden or universal essentiality: the broader trade-off analysis shows that core genes can carry substantial laboratory burden and condition-specific costs. These studies measure different outcomes, so the findings are not a direct contradiction, but they set a boundary on interpretation. [src: adp1_deletion_phenotypes, core_gene_tradeoffs] In addition, the costly–dispensable classification used max_fit > 1 in any experiment, making burden classification sensitive to fitness-data noise, while its 90% identity DIAMOND threshold may miss recently acquired genes with low sequence similarity. [src: costly_dispensable_genes]

## Possible Reconciliations

- **Hypothesis — outcome specificity:** Core status may improve deletion-mutant recovery while not implying low laboratory burden, because collection coverage and fitness burden measure different outcomes.
- **Hypothesis — mixed mechanisms:** Biological conservation, construction difficulty, measurement limitations, and misclassified fragments may each contribute to the same missing-data pattern.
- **Hypothesis — condition dependence:** Singleton genes may be genuinely near-neutral under tested conditions while still showing effects in untested conditions; inadequate transposon coverage could produce the same observed result.
- **Hypothesis — classification limits:** Mobile-element enrichment and poor annotation may narrow the interpretation of costly non-conserved genes toward horizontally acquired DNA without proving that such genes are systematically absent from perturbation collections. [src: costly_dispensable_genes]

## Resolving Work

- Compare deletion construction success, sequencing quality, annotation confidence, and fragment status across core, accessory, and singleton genes; test whether coverage remains associated with core status after technical covariates are controlled.
- Re-measure singleton and poorly covered genes with matched perturbation methods and sufficient independent mutants; ask whether apparent neutrality reflects inadequate coverage or reproducible lack of effect.
- Test the same genes across multiple laboratory conditions and quantify burden separately from deletion recovery; ask whether core enrichment persists when condition-specific costs are included.
- Reanalyze costly–dispensable classifications across alternative fitness thresholds and identity thresholds; ask whether mobile-element enrichment and low annotation similarity are robust to those choices.
- Compare genes absent from perturbation collections with independently curated gene models and pangenome evidence; ask whether missing genes are biological absences, misclassified fragments, or technical failures.
