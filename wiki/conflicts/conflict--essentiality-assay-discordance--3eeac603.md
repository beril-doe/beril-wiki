<!-- tension-hash: 3eeac60399b1bfa3 -->
# Do costly, conserved genes show natural selection, or only lab-inferred selection signatures?

The core-gene trade-off analysis sorts genes into categories such as "Costly + Conserved" from laboratory burden and conservation across a pangenome (the full gene set of related genomes) [src: core_gene_tradeoffs]. The disagreement is about what that category shows. One reading treats it as a signature of genes kept by natural selection. The other holds that, because laboratory measurements can depend on perturbation modality and condition, the category supports only a selection hypothesis, not direct evidence about fitness in nature [src: core_gene_tradeoffs]. The answer determines whether these gene sets, 28,017 costly-and-conserved and 5,526 costly-and-dispensable genes [src: conservation_fitness_synthesis], can serve as evidence about natural environments or only as candidates for ecological testing. The tension comes from [[concepts/essentiality-assay-discordance]].

## Evidence Sides

**Selection-signature reading: costly conservation as a marker of maintained genes**

The core-gene trade-off analysis builds its Costly + Conserved category from laboratory burden and pangenome conservation, and this **refines** how costly conserved genes are interpreted [src: core_gene_tradeoffs]. The synthesis identifies 28,017 genes as both costly and conserved and 5,526 as costly and dispensable, and frames these categories as selection signatures [src: conservation_fitness_synthesis].

**Assay-dependence reading: lab cost cannot directly establish natural selection**

The Costly + Conserved category is inferred from laboratory burden and conservation, and the assay-discordance evidence shows that laboratory measurements can depend on perturbation modality (for example, transposon insertion, which disrupts a gene by inserting a mobile DNA segment, versus complete knockout, which removes the entire gene) and on condition [src: core_gene_tradeoffs]. On this reading, costly conservation should be treated as a selection hypothesis that needs ecological validation, not as direct evidence that a gene is essential in nature [src: core_gene_tradeoffs]. The synthesis **supports** this caution: it explicitly treats its categories as selection signatures rather than direct measurements of natural fitness [src: conservation_fitness_synthesis].

## Possible Reconciliations

- *Hypothesis:* The two readings may operate at different evidential levels. "Selection signature" could describe a statistical pattern, while "essential in nature" is a separate claim the laboratory data cannot reach. If so, both sides could hold once the wording is kept distinct.
- *Hypothesis:* Some Costly + Conserved genes may be costly only under particular laboratory perturbations or conditions. If so, their cost calls would be assay-dependent, and ecological validation would still be needed to judge selection.
- *Hypothesis:* Costs that appear consistently across perturbation modalities and conditions may predict selection in nature better than costs seen in a single assay. If so, a stricter, assay-robust category could support the stronger reading.

## Resolving Work

- **Data:** Costly + Conserved genes with fitness measured by both transposon and complete-knockout methods. **Method:** Compare each gene's burden call between the two modalities. **Question:** What share of the category's cost survives a change of perturbation modality?
- **Data:** Per-condition laboratory fitness profiles for the Costly + Conserved set. **Method:** Classify each gene's cost as condition-specific or condition-general. **Question:** Is costly conservation driven by a few conditions or by cost across the whole condition space?
- **Data:** Environmental metadata for source organisms linked to their laboratory fitness data. **Method:** Test whether costly-conserved content tracks environmental variability. **Question:** Does ecological context validate the selection hypothesis?
- **Data:** The costly-and-dispensable set compared against the costly-and-conserved set. **Method:** Contrast their functions, mobile-element association and phylogenetic distribution. **Question:** Do the two sets differ as a selection model predicts?
