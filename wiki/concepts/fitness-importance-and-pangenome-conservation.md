---
type: "Concept"
description: "How mutant fitness importance relates to pangenome conservation"
sources: ["summaries/fitness_effects_conservation__REPORT.md"]
---
# Fitness Importance and Pangenome Conservation

This concept examines whether genome-wide mutant fitness importance predicts whether bacterial genes are core, auxiliary, or singleton in a pangenome. The analysis integrated [[entities/kescience-fitnessbrowser]] measurements, RB-TnSeq (random barcode transposon sequencing) fitness data, essentiality classifications, condition-specific phenotype annotations, and KBase pangenome gene-cluster mappings for approximately 194,000 genes from 43 diverse bacteria. [src: fitness_effects_conservation]

The findings connect [[concepts/gene-essentiality]] with [[concepts/pangenome-integration]], while also refining the expectation that accessory genes are generally more conditionally important than core genes. [src: fitness_effects_conservation]

## Evidence for a Conservation Gradient

Conservation increased with fitness importance across the measured categories, but the relationship was weak in predictive magnitude. Essential genes with no viable mutants were 82% core (n=27,693); genes often sick in more than 10% of experiments were 78% core (n=15,989); mixed genes were 70% core (n=20,739); sometimes-sick genes were 72% core (n=25,201); always-neutral genes were 66% core (n=94,889); and sometimes-beneficial genes were 70% core (n=9,705). [src: fitness_effects_conservation]

The same pattern appeared when genes were grouped by their strongest measured fitness effect: essential genes were 82.2% core, genes with min_fit < -3 were 77.7% core, and genes with min_fit from -1 to 0 were 66.4% core. [src: fitness_effects_conservation]

Fitness breadth was positively associated with core status, with Spearman rho=0.086 and p=8.1e-230. [src: fitness_effects_conservation] Essential genes were 82% core, genes affecting 20+ experiments were 79% core, genes affecting 6-20 experiments were 73% core, genes affecting 1-5 experiments were 71% core, and genes with 0 experiments were 66% core. [src: fitness_effects_conservation]

Across the full analysis, essential genes were 82% core whereas always-neutral genes were 66% core, producing a 16-percentage-point gradient across approximately 194,000 genes from 43 bacteria. [src: fitness_effects_conservation]

## Core Genes Have Both Costs and Benefits

The results contradict the expectation that accessory genes are generally costly to carry. Core genes were more likely than auxiliary genes to show a positive fitness effect when deleted: 24.4% were ever beneficial versus 19.9% of auxiliary genes, with OR=0.77 for auxiliary versus core. [src: fitness_effects_conservation]

Core and auxiliary genes also had distinct fitness-effect distributions, with core genes showing heavier tails in both the negative direction, indicating importance, and the positive direction, indicating burdens when retained or deleted under particular conditions. [src: fitness_effects_conservation]

These results support a trade-off interpretation in which core genes participate in functions that are important under some conditions but can impose condition-dependent costs under others. [src: fitness_effects_conservation] This refines [[concepts/condition-specific-fitness]] by showing that conditional effects are not restricted to pangenome-accessory genes. [src: fitness_effects_conservation]

## Condition-Specific and Ephemeral-Niche Effects

Genes tagged with strong condition-specific effects in the `specificphenotype` annotation were 77.3% core, compared with 70.3% for genes without specific phenotypes; the association had OR=1.78 and p=1.8e-97. [src: fitness_effects_conservation]

A total of 4,450 genes (2.7%) fit the ephemeral-niche pattern of being neutral overall but critical in one condition. [src: fitness_effects_conservation] These genes were more common among core genes (3.0%) than auxiliary genes (1.7%) or singleton genes (1.6%). [src: fitness_effects_conservation]

The enrichment of condition-specific and ephemeral-niche effects among core genes suggests the hypothesis that core genes have more detectable conditional phenotypes because they participate in more pathways. [src: fitness_effects_conservation] This result complements [[concepts/adaptive-versus-housekeeping-functional-differentiation]] without establishing that all core genes are broadly adaptive. [src: fitness_effects_conservation]

## Novel Genes and Assay Visibility

Novel singleton genes showed near-zero mean fitness under the tested laboratory conditions. [src: fitness_effects_conservation] This apparent neutrality may reflect poor transposon coverage rather than true absence of fitness effects. [src: fitness_effects_conservation]

Consequently, the lower conservation of genes with few or no measured phenotypes should not be interpreted as evidence that those genes are biologically unimportant in all environments. [src: fitness_effects_conservation] The result is directly relevant to [[concepts/transposon-callability-bias]] and [[concepts/genetic-perturbation-coverage-bias]]. [src: fitness_effects_conservation]

## Interpretation and Limits

The combined results indicate that core genes were more functionally active under the tested conditions, showing larger fitness effects in both directions, whereas accessory genes tended to be functionally quieter in the laboratory assays. [src: fitness_effects_conservation]

The statistically robust conservation gradient does not make fitness importance a strong standalone predictor: the difference between 82% core among essential genes and 66% core among always-neutral genes was 16 percentage points. [src: fitness_effects_conservation]

The analysis is consistent with stronger purifying selection on core genes and with pangenome models in which selection contributes to gene-frequency distributions, but it does not establish that selection is the sole driver of conservation. [src: fitness_effects_conservation]

Interpretation is limited because the fitness measurements were biased toward rich media and standard stresses, single-gene knockouts did not capture epistatic interactions, the Fitness Browser covered 43 bacteria primarily from Proteobacteria, and singleton or novel genes may lack fitness data because of poor transposon coverage rather than true neutrality. [src: fitness_effects_conservation]

## Relation to Other Concepts

This concept extends [[concepts/gene-essentiality]] by connecting essentiality, fitness-effect magnitude, and fitness breadth to pangenome conservation. [src: fitness_effects_conservation]

It supports [[concepts/condition-specific-fitness]] with evidence that condition-specific and ephemeral-niche effects can be enriched among core genes. [src: fitness_effects_conservation]

It extends [[concepts/pangenome-integration]] by joining Fitness Browser mutant phenotypes to core, auxiliary, and singleton gene classes across bacterial pangenomes. [src: fitness_effects_conservation]

It also informs [[concepts/fitness-importance-versus-ecological-context]], because the observed relationship was measured mainly under laboratory conditions and may not represent fitness importance across untested ecological niches. [src: fitness_effects_conservation]

## Open Directions

- Combine the existing fitness and pangenome data with environmental-condition metadata and test, using stratified models, whether the 82% versus 66% conservation contrast persists outside rich media and standard stresses. [src: fitness_effects_conservation]
- Reanalyze singleton and novel genes after filtering or modeling transposon coverage, asking whether their near-zero mean fitness reflects true neutrality or callability failure. [src: fitness_effects_conservation]
- Use multi-gene perturbation or interaction datasets to test whether the observed conservation gradient changes when epistatic effects omitted by single-gene knockouts are included. [src: fitness_effects_conservation]
- Compare the conservation–fitness relationship across bacterial lineages beyond the primarily Proteobacteria representation in the 43-bacterium Fitness Browser coverage. [src: fitness_effects_conservation]
- Test whether core genes with heavier positive and negative fitness tails show reproducible condition-specific trade-offs across independent experiments rather than assay-specific effects. [src: fitness_effects_conservation]
