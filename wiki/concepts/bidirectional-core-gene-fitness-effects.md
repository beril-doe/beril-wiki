---
type: "Concept"
description: "Core genes can impose both fitness costs and benefits across conditions."
sources: ["summaries/fitness_effects_conservation__REPORT.md"]
---
# Bidirectional fitness effects of core genes

Core genes are not uniformly beneficial to retain or uniformly costly to delete: across tested conditions, they show stronger fitness effects in both negative and positive directions than auxiliary genes. This pattern links [[concepts/gene-essentiality]], [[concepts/condition-dependent-gene-tradeoffs]], and [[concepts/pangenome-conservation-fitness-decoupling]]. [src: fitness_effects_conservation]

The evidence comes from integrating RB-TnSeq (random barcode transposon sequencing) mutant-fitness measurements, essentiality classifications, condition-specific phenotype annotations, and pangenome gene-cluster mappings across approximately 194,000 genes from 43 diverse bacteria. [src: fitness_effects_conservation] The underlying measurements were obtained primarily in rich media and standard laboratory stresses, so the observed bidirectionality describes the tested assay space rather than all natural environments. [src: fitness_effects_conservation]

## Core genes have stronger effects in both directions

Core genes were more likely than auxiliary genes to show a positive fitness effect when deleted: 24.4% of core genes were ever beneficial versus 19.9% of auxiliary genes, with OR=0.77 for auxiliary versus core. [src: fitness_effects_conservation] Core and auxiliary genes also had distinct fitness-effect distributions, with core genes showing heavier tails in both the negative direction, indicating greater importance under some conditions, and the positive direction, indicating that retaining or deleting them can impose burdens under particular conditions. [src: fitness_effects_conservation]

This **supports** the hypothesis that core genes are embedded in pathways whose value depends on environmental or physiological context, rather than the simpler expectation that accessory genes are generally costly to carry while core genes are uniformly advantageous. [src: fitness_effects_conservation] The result **refines** [[concepts/fitness-importance-and-pangenome-conservation]] by showing that conservation is compatible with both strong dependency and condition-specific cost. [src: fitness_effects_conservation]

## Conservation and fitness importance

A conservation gradient accompanied the fitness categories: essential genes with no viable mutants were 82% core (n=27,693); genes often sick in more than 10% of experiments were 78% core (n=15,989); mixed genes were 70% core (n=20,739); sometimes-sick genes were 72% core (n=25,201); always-neutral genes were 66% core (n=94,889); and sometimes-beneficial genes were 70% core (n=9,705). [src: fitness_effects_conservation] The same pattern appeared when genes were binned by their strongest fitness effect: essential genes were 82.2% core, genes with min_fit < -3 were 77.7% core, and genes with min_fit from -1 to 0 were 66.4% core. [src: fitness_effects_conservation]

Fitness breadth was positively associated with core status, although the association was weak in magnitude: Spearman rho=0.086, p=8.1e-230. [src: fitness_effects_conservation] Essential genes were 82% core, genes affecting 20+ experiments were 79% core, genes affecting 6-20 experiments were 73% core, genes affecting 1-5 experiments were 71% core, and genes with 0 experiments were 66% core. [src: fitness_effects_conservation] These results **support** a relationship between functional importance, breadth of measured effects, and conservation, but the weak association **limits** conservation as a standalone proxy for fitness importance. [src: fitness_effects_conservation]

## Condition-specific and ephemeral effects

Genes tagged with strong condition-specific effects in the `specificphenotype` annotation were 77.3% core, compared with 70.3% for genes without specific phenotypes; the association had OR=1.78 and p=1.8e-97. [src: fitness_effects_conservation] This finding **contradicts** the expectation that condition-specific genes are predominantly accessory and instead suggests that core genes can have detectable condition-specific effects because they participate in well-characterized pathways. [src: fitness_effects_conservation]

A total of 4,450 genes (2.7%) fit the ephemeral-niche pattern of being neutral overall but critical in one condition. [src: fitness_effects_conservation] These genes were more common among core genes (3.0%) than auxiliary genes (1.7%) or singleton genes (1.6%). [src: fitness_effects_conservation] This result **supports** the interpretation that core genes can be conditionally important while appearing neutral in aggregate, and it **extends** [[concepts/condition-specific-fitness]] by connecting conditional effects to pangenome status. [src: fitness_effects_conservation]

## Limits on interpretation

Novel singleton genes showed near-zero mean fitness in the tested laboratory assays, but this apparent neutrality may reflect poor transposon coverage rather than genuinely absent effects. [src: fitness_effects_conservation] The measurements used single-gene knockouts and therefore did not capture epistatic interactions. [src: fitness_effects_conservation] The Fitness Browser covered 43 bacteria, primarily Proteobacteria, limiting generalizability to other bacterial lineages. [src: fitness_effects_conservation] These limitations mean that the bidirectional core-gene pattern is a measured result in the available perturbation and condition space, not evidence that every core gene has opposing effects in nature. [src: fitness_effects_conservation]

The complete project analysis is summarized in [[summaries/fitness_effects_conservation__REPORT]]. [src: fitness_effects_conservation]

## Open Directions

- Reanalyze the Fitness Browser data with condition-stratified effect distributions and interaction terms to test whether the heavier positive and negative tails of core genes persist within matched assay conditions. [src: fitness_effects_conservation]
- Combine transposon coverage metrics with singleton and auxiliary-gene fitness estimates to distinguish true neutrality from callability-limited missing data. [src: fitness_effects_conservation]
- Compare single-gene knockout effects with multi-gene or combinatorial perturbation data to test whether epistasis explains additional bidirectional effects among core genes. [src: fitness_effects_conservation]
- Add environmental-condition data beyond rich media and standard stresses to test whether the core-gene cost-benefit pattern transfers to natural niche conditions. [src: fitness_effects_conservation]
- Use phylogenetically stratified models across the 43 bacteria to test whether the association between fitness breadth and core status is lineage-specific or broadly transferable. [src: fitness_effects_conservation]
