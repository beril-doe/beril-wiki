<!-- tension-hash: 5395af897a4039cf -->
# Exploitation Versus Correction in Fitness-Condition Prioritization

The prioritization system faces a tension between exploiting organisms with abundant informative evidence and correcting for unequal observation across condition panels. This matters because rankings that maximize immediate experimental yield may systematically underrepresent genes from organisms with shallow coverage, while rankings that compensate for coverage may sacrifice near-term discovery. The evidence also cautions against treating core-versus-accessory status as a universal correction: observed fitness effects and burdens vary by gene class and functional category. See [[concepts/fitness-condition-coverage-prioritization-bias]].

## Evidence Sides

### **Exploit existing evidence**

Favoring organisms with many informative profiles improves immediate experimental yield, as illustrated by the 242-of-500 coverage achieved by 10 organism–condition experiments, but may underexplore genes from organisms whose condition panels are shallow. [src: functional_dark_matter] The report does not establish that the highest-ranked organisms have intrinsically more dark-gene biology, so this distinction should not be inferred from their candidate counts alone. [src: functional_dark_matter]

The conservation analysis supports using observed fitness evidence rather than assuming that only accessory genes matter: core genes showed stronger fitness effects in both negative and positive directions, while novel singleton genes were near-neutral under tested laboratory conditions. [src: fitness_effects_conservation] In one organism, fitness importance predicted conservation more consistently than field-versus-lab classification. [src: field_vs_lab_fitness]

### **Correct for unequal observation**

Genes from organisms with shallow condition panels may be underexplored when prioritization favors organisms with many informative profiles. [src: functional_dark_matter] Near-neutral effects for novel singleton genes may reflect poor transposon coverage rather than genuinely low importance. [src: fitness_effects_conservation] Neither result establishes how untested ecological conditions would reorder priorities. [src: fitness_effects_conservation]

A single core-versus-accessory adjustment may also be misleading: burden was higher for core genes in several functional categories but higher for non-core genes in Cell Wall genes. [src: core_gene_tradeoffs] Thus, correction may need to account for functional category and measurement quality rather than applying one global penalty or boost. The field-versus-lab result does not show that unequal condition coverage is harmless. [src: field_vs_lab_fitness]

## Possible Reconciliations

- **Hypothesis — evidence density and biological value are different objectives:** Existing profiles may identify experiments with the highest immediate yield, while coverage correction may improve discovery of biology that is currently poorly observed.
- **Hypothesis — apparent singleton neutrality is partly technical:** Poor transposon coverage could suppress measured effects, allowing core genes to appear more informative without proving that singleton genes are biologically less important.
- **Hypothesis — context-specific gene-class effects:** Core and non-core status may interact with functional category, explaining why core genes carry higher burden in several categories while non-core genes carry higher burden in Cell Wall genes.
- **Hypothesis — organism and environment modify the ranking:** A ranking that works in one organism or laboratory panel may change when applied to organisms with different accessory-genome structures or to ecological conditions not yet tested.

## Resolving Work

- Assemble matched condition panels across organisms with shallow and deep coverage; compare raw and coverage-adjusted rankings to ask whether selected genes and organisms change.
- Reanalyze transposon insertion density and fitness-effect uncertainty for novel singleton and core genes; test whether correcting for poor coverage removes the near-neutral singleton pattern.
- Stratify ranking performance by functional category, especially Cell Wall genes; measure whether category-specific corrections outperform a single core-versus-accessory adjustment.
- Validate top-ranked and coverage-corrected candidates in both laboratory and ecologically relevant conditions; ask whether untested environments reorder priorities.
- Compare predicted conservation from fitness importance, field-versus-lab classification, and coverage-adjusted scores across organisms to determine which signal generalizes.
