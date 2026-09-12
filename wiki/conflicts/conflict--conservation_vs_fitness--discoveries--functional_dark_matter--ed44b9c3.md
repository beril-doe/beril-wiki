<!-- tension-hash: 33410520dc7f3003 -->
# Phenotype, Conservation, and Context Rank Dark Genes Differently

The disagreement is whether strong experimental phenotypes, conservation, environmental structure, and neighborhood-based inference identify the same genes and processes. This matters because the framework combines these evidence types to prioritize functional dark matter, yet their rankings, validation strength, and stress-related interpretations can diverge substantially across datasets and subsets ([[concepts/experimental-prioritization-of-functional-dark-matter]]).

## Evidence Sides

**Phenotype- and context-led prioritization**

The framework simultaneously prioritizes genes with strong measured phenotypes and genes that are conserved or environmentally structured, but these evidence types do not guarantee the same ranking. [src: functional_dark_matter] Environmental associations support hypotheses while remaining vulnerable to sparse metadata, genus-level matching, common-genus effects, and compositional coupling. [src: functional_dark_matter] Overall, stress conditions produced the largest concentration of strong dark-gene phenotypes. [src: functional_dark_matter] Essential genes were enriched in the core genome, with a median odds ratio of 1.56. [src: conservation_vs_fitness] Module and neighborhood evidence also identifies candidates: 6,142 dark genes belonged to ICA fitness modules, 30,190 dark genes shared a predicted operon with an annotated gene, and 97.2% had at least one annotated neighbor within a five-gene window. [src: functional_dark_matter]

**Conservation-, subset-, and method-qualified evidence**

Conservation-dominant or drop-tractability settings retained only 64% of the original fitness-active top 50, while essential-gene rankings changed substantially when tractability or neighbor context was removed. [src: functional_dark_matter] Essentiality was measured under a single growth condition represented by RB-TnSeq library construction, so modest core enrichment does not establish that genes important under stress or other unmeasured conditions will be conserved in the same way. [src: conservation_vs_fitness] The essential-gene definition is also an upper bound because missing insertions can reflect short genes, low-complexity regions, or scaffold edges; essential genes were slightly shorter on average, consistent with insertion bias. [src: conservation_vs_fitness] The 97.2% neighbor rate is expected given a 75% genome-wide annotation rate, and module and neighborhood predictions are guilt-by-association inferences rather than direct experimental validation. [src: functional_dark_matter] Ortholog transfer achieved 95.8% precision and 91.2% coverage for gene-level KO prediction, but Module-ICA had <1% KO-level precision while capturing process-level co-regulation. [src: discoveries] In the truly dark subset, stress proportions were 28.7% versus 43.2% for annotation-lag genes among strong-phenotype genes, with OR = 0.53 and p < 0.001; another comparison reported stress at 43.3% versus 54.7%. [src: truly_dark_genes] Pangenome analyses also disagree: one found no significant relationship between openness and environment or phylogenetic effects (rho=-0.05, p=0.54 and rho=0.03, p=0.73), whereas another found associations between variable metabolic pathways and openness (rho=0.327, p=7.2e-71, and partial rho=0.530, p=2.83e-203 after controlling for genome count). [src: discoveries]

## Possible Reconciliations

- **Hypothesis — scope difference:** Stress may dominate the overall dark-gene set while being less characteristic of the residual genes that resist reannotation.
- **Hypothesis — measurement difference:** RB-TnSeq under one growth condition may measure a narrower form of essentiality than multi-condition fitness.
- **Hypothesis — evidence-product difference:** Ortholog transfer may support gene-level annotation, whereas Module-ICA captures process-level co-regulation; they should not be combined without calibration.
- **Hypothesis — cohort and feature difference:** The pangenome contradiction may result from different species coverage, openness definitions, genome-count controls, or analysis cohorts.

## Resolving Work

- Re-rank the same genes under phenotype, conservation, tractability, neighbor, and environmental evidence, then quantify rank stability and overlap.
- Repeat fitness assays across stress and non-stress conditions, testing whether condition-specific essentiality predicts conservation.
- Validate operon, neighbor, and ICA-module candidates with targeted knockouts or complementation, measuring gene-level versus process-level precision.
- Reanalyze both pangenome studies on a harmonized cohort with identical openness features, environmental variables, phylogenetic controls, and genome-count adjustment.
- Stratify stress enrichment by overall dark, annotation-lag, and truly dark status to determine whether subset composition explains the conflicting proportions.
