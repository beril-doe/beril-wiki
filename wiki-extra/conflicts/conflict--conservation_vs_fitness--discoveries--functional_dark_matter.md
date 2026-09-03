<!-- tension-hash: 33410520dc7f3003 -->
# Does contextual evidence identify the same priorities as direct fitness evidence?

The framework combines measured fitness phenotypes with conservation, environmental structure, modules, and genomic neighborhoods, but these evidence types do not guarantee the same gene ranking. The disagreement matters because contextual signals may broaden discovery beyond experimentally characterized genes while also introducing inference, measurement, and cohort-specific effects. Related contrasts over stress enrichment and pangenome openness show that conclusions may depend strongly on the subset, predictor definitions, and controls used.

## Evidence Sides

**Direct fitness evidence versus conservation and tractability.** The framework prioritizes genes with strong measured phenotypes, while also prioritizing genes that are conserved or environmentally structured; these evidence types do not guarantee the same ranking [src: functional_dark_matter]. In conservation-dominant or drop-tractability settings, only 64% of the original fitness-active top 50 were retained, and essential-gene rankings changed substantially when tractability or neighbor context was removed [src: functional_dark_matter]. Essential genes were enriched in the core genome, but the median odds ratio was 1.56, and essentiality was measured under a single growth condition represented by RB-TnSeq library construction [src: conservation_vs_fitness]. The essential-gene definition is also an upper bound because missing insertions can reflect short genes, low-complexity regions, or scaffold edges; essential genes were slightly shorter on average, consistent with insertion bias [src: conservation_vs_fitness].

**Contextual inference versus direct validation.** 6,142 dark genes belonged to ICA fitness modules, 30,190 dark genes shared a predicted operon with an annotated gene, and 97.2% had at least one annotated neighbor within a five-gene window, but these are guilt-by-association inferences rather than direct experimental validation [src: functional_dark_matter]. The 97.2% neighbor rate is expected given a 75% genome-wide annotation rate [src: functional_dark_matter]. Ortholog transfer achieved 95.8% precision and 91.2% coverage for gene-level KO prediction, whereas Module-ICA had <1% KO-level precision while capturing process-level co-regulation [src: discoveries].

**Overall dark-gene stress signal versus residual truly dark genes.** The overall dark-gene analysis reports stress conditions as producing the largest concentration of strong dark-gene phenotypes [src: functional_dark_matter]. The truly dark analysis instead reports stress proportions of 28.7% versus 43.2% for annotation-lag genes among strong-phenotype genes, with OR = 0.53 and p < 0.001, while separately reporting stress at 43.3% versus 54.7% in another comparison [src: truly_dark_genes].

**Conflicting openness associations.** One analysis found no significant relationship between openness and environment or phylogenetic effects (rho=-0.05, p=0.54 and rho=0.03, p=0.73), whereas another found associations between variable metabolic pathways and openness (rho=0.327, p=7.2e-71, and partial rho=0.530, p=2.83e-203 after controlling for genome count) [src: discoveries].

## Possible Reconciliations

- **Hypothesis — scope:** Overall dark genes and the residual truly dark subset may have different stress compositions.
- **Hypothesis — measurement:** Single-condition RB-TnSeq essentiality may not represent stress or other unmeasured conditions.
- **Hypothesis — evidence product:** Gene-level orthology and process-level Module-ICA predictions may be valid for different purposes and should not share one uncalibrated score.
- **Hypothesis — cohort and predictor definitions:** Openness results may differ because of species coverage, genome-count control, or the tested environmental and phylogenetic features.

## Resolving Work

- Re-rank the same genes under matched phenotype, conservation, tractability, neighbor, and environmental features; test how often top-50 membership changes.
- Replicate essentiality across multiple growth and stress conditions, then compare condition-specific fitness with conservation and core-genome status.
- Benchmark ortholog transfer and Module-ICA against experimentally validated KO functions and calibrate their outputs separately.
- Reanalyze openness associations in identical cohorts with harmonized predictors, species coverage, and genome-count controls.
