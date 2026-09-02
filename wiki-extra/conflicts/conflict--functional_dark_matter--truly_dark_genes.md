<!-- tension-hash: 4d0510599daca6da -->
# Dark-Gene Prioritization and Stress Interpretation Depend on Evidence and Subset

The disagreement is whether dark-gene prioritization signals and stress associations describe a stable biological ranking or depend strongly on the evidence type, genomic context, and subset analyzed. The framework combines measured phenotypes, conservation, environmental structure, module membership, and neighborhood context, but these sources can disagree or provide only indirect support. The stress result is especially sensitive to whether the analysis includes all dark genes or only the residual genes that resist reannotation. [[concepts/experimental-prioritization-of-functional-dark-matter]]

## Evidence Sides

**Phenotype-led prioritization versus context-led prioritization.** The framework simultaneously prioritizes genes with strong measured phenotypes and genes that are conserved or environmentally structured, but these evidence types do not guarantee the same ranking. [src: functional_dark_matter] Conservation-dominant or drop-tractability settings retained only 64% of the original fitness-active top 50, while essential-gene rankings changed substantially when tractability or neighbor context was removed. [src: functional_dark_matter] Environmental associations also support hypotheses while remaining vulnerable to sparse metadata, genus-level matching, common-genus effects, and compositional coupling. [src: functional_dark_matter]

**Direct phenotype evidence versus module and neighborhood inference.** 6,142 dark genes belonged to ICA fitness modules, 30,190 dark genes shared a predicted operon with an annotated gene, and 97.2% had at least one annotated neighbor within a five-gene window, but module and neighborhood predictions are guilt-by-association inferences rather than direct experimental validation. [src: functional_dark_matter] The report further cautions that the 97.2% neighbor rate is expected given a 75% genome-wide annotation rate. [src: functional_dark_matter]

**Stress-prominent dark genes versus stress-depleted truly dark genes.** The overall dark-gene analysis reports stress conditions as producing the largest concentration of strong dark-gene phenotypes. [src: functional_dark_matter] In contrast, the truly dark analysis reports stress proportions of 28.7% versus 43.2% for annotation-lag genes among strong-phenotype genes, with OR = 0.53 and p < 0.001, while separately reporting stress at 43.3% versus 54.7% in another comparison. [src: truly_dark_genes]

## Possible Reconciliations

- **Hypothesis — subset composition:** Stress may be prominent among dark genes overall while being less characteristic of the residual genes that resist reannotation.
- **Hypothesis — evidence weighting:** Conservation, tractability, neighbor context, and phenotype strength may measure different properties, so ranking changes may reflect legitimate scope differences rather than contradiction.
- **Hypothesis — indirect versus direct evidence:** Modules and operons may identify useful candidates without establishing that every linked dark gene has the inferred function.
- **Hypothesis — denominator and comparison differences:** The two stress comparisons may use different gene subsets or reference groups, producing different proportions without requiring incompatible biology.

## Resolving Work

- Recompute rankings across phenotype, conservation, tractability, environmental, module, and neighborhood evidence while holding the gene universe and ranking metric constant; test which genes remain stable.
- Experimentally validate a stratified sample of module-linked, operon-linked, and neighborhood-linked dark genes; measure whether inferred functions predict direct fitness phenotypes.
- Reanalyze stress enrichment with explicit denominators, identical phenotype thresholds, and mutually exclusive dark-gene and annotation-lag subsets; determine whether the reported proportions remain distinct.
- Permute genome annotations and neighborhood structure while preserving annotation rate, including a 75% genome-wide annotation-rate null; test whether 97.2% exceeds structural expectation.
- Expand environmental metadata across genera and sampling contexts and use controls for common-genus effects and compositional coupling; assess whether environmental associations replicate.
