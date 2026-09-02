<!-- tension-hash: 5395af897a4039cf -->
# Evidence-Rich Prioritization vs. Unequal Condition Coverage

The disagreement concerns whether fitness-based prioritization should primarily exploit organisms and conditions with abundant informative evidence or compensate for organisms whose condition panels are shallow. The tension matters because immediate experimental yield may favor well-observed organisms, while that strategy could systematically underexplore genes whose biology is hidden by unequal coverage. The related evidence on conservation, gene class, and field-versus-lab behavior complicates any simple correction, as described on [[concepts/fitness-condition-coverage-prioritization-bias]].

## Evidence Sides

### **Exploit existing evidence for immediate yield**

Favoring organisms with many informative profiles improves immediate experimental yield: 10 organism–condition experiments achieved 242-of-500 coverage. [src: functional_dark_matter] This supports prioritizing organisms where existing measurements make candidate selection more productive. However, the report does not establish that the highest-ranked organisms have intrinsically more dark-gene biology, so this distinction should not be inferred from their candidate counts alone. [src: functional_dark_matter]

Core genes also showed stronger fitness effects in both negative and positive directions, while novel singleton genes were near-neutral under tested laboratory conditions. [src: fitness_effects_conservation] This indicates that condition-specific detection is not confined to accessory genes. [src: fitness_effects_conservation] In one organism, fitness importance predicted conservation more consistently than field-versus-lab classification. [src: field_vs_lab_fitness]

### **Correct for unequal observation and biological scope**

Favoring organisms with many informative profiles may underexplore genes from organisms whose condition panels are shallow. [src: functional_dark_matter] The conservation result does not resolve this concern: the near-neutral effects of novel singleton genes may reflect poor transposon coverage, and neither result establishes how untested ecological conditions would reorder priorities. [src: fitness_effects_conservation]

A single core-versus-accessory correction is also inadequate. Burden was higher for core genes in several functional categories but higher for non-core genes in Cell Wall genes. [src: core_gene_tradeoffs] This category-specific reversal cautions against applying a single core-versus-accessory correction to fitness-based rankings. [src: core_gene_tradeoffs] Coverage-adjusted rankings may therefore change across organisms with different condition panels and accessory-genome structures, a question that remains unresolved. [src: field_vs_lab_fitness]

## Possible Reconciliations

- **Measurement hypothesis:** The apparent advantage of well-profiled organisms may reflect measurement density rather than intrinsically richer dark-gene biology; candidate counts alone cannot distinguish those explanations. [src: functional_dark_matter]
- **Scope hypothesis:** Core genes may be reliably detectable under tested laboratory conditions, while singleton or accessory genes may become important in untested ecological conditions. The observed near-neutrality of singleton genes may also result from poor transposon coverage. [src: fitness_effects_conservation]
- **Category hypothesis:** Coverage correction may need to be functional-category-specific because core genes and non-core genes reverse their burden patterns in Cell Wall genes. [src: core_gene_tradeoffs]
- **Prediction hypothesis:** Fitness importance may predict conservation within an organism without showing that unequal condition coverage is harmless across organisms. [src: field_vs_lab_fitness]

## Resolving Work

- Assemble organism-by-condition panels with matched sequencing and transposon coverage; re-estimate candidate yield and test whether the 242-of-500 result persists after correcting for observation depth.
- Fit hierarchical models that separate organism, condition, gene class, functional category, and measurement quality; test whether prioritization scores predict newly observed fitness effects in shallow-panel organisms.
- Perform targeted experiments on singleton and accessory genes across laboratory and ecological conditions; ask whether near-neutral laboratory effects become condition-specific outside the tested panel.
- Recompute rankings under organism-level, gene-class, and category-specific coverage adjustments; compare how many selected experiments and newly detected genes change.
- Validate predictions prospectively across organisms with different accessory-genome structures; test whether fitness-based, coverage-adjusted, or hybrid rankings best predict conservation and field relevance.
