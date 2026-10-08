---
type: "Summary"
description: "Quantitative comparison of Fitness Browser mutant fitness effects with pangenome conservation across ~194,000 genes from 43 bacteria, showing a weak but robust gradient in which fitness-important genes are more often core."
doc_type: "short"
full_text: "sources/fitness_effects_conservation__REPORT.md"
---
# Fitness Effects vs Conservation — Quantitative Analysis

## Overview

This analysis compares genome-wide mutant fitness measurements from the Fitness Browser with pangenome conservation across approximately 194,000 genes from 43 diverse bacteria. RB-TnSeq (random barcode transposon sequencing, a pooled mutant-fitness assay) data, essentiality classifications, condition-specific phenotype annotations, and KBase pangenome gene-cluster mappings were integrated to test whether fitness importance predicts whether genes are core, auxiliary, or singleton. [src: fitness_effects_conservation]

## Key Findings

### Conservation increases with fitness importance

A clear conservation gradient spans fitness categories: essential genes with no viable mutants were 82% core (n=27,693); genes often sick in more than 10% of experiments were 78% core (n=15,989); mixed genes (sick + beneficial) were 70% core (n=20,739); sometimes-sick genes were 72% core (n=25,201); always-neutral genes were 66% core (n=94,889); and sometimes-beneficial genes were 70% core (n=9,705). [src: fitness_effects_conservation]

The same gradient held when genes were binned by their strongest fitness effect: essential genes were 82.2% core, genes with min_fit < -3 were 77.7% core, and genes with min_fit from -1 to 0 were 66.4% core. [src: fitness_effects_conservation]

### Breadth of fitness effects predicts conservation

Fitness breadth was positively associated with core status, although the association was weak in magnitude: Spearman rho=0.086, p=8.1e-230. Essential genes were 82% core, genes affecting 20+ experiments were 79% core, genes affecting 6-20 experiments were 73% core, genes affecting 1-5 experiments were 71% core, and genes with 0 experiments were 66% core. [src: fitness_effects_conservation]

### Core genes show both stronger costs and stronger benefits

Core genes were more likely than auxiliary genes to show a positive fitness effect when deleted: 24.4% were ever beneficial versus 19.9% of auxiliary genes, with OR=0.77 for auxiliary versus core. This runs counter to the expectation that accessory genes are generally costly to carry; the report proposes, as a possible explanation rather than a demonstrated cause, that core genes participate more often in trade-off situations, helping under some conditions while imposing costs under others. [src: fitness_effects_conservation]

Core and auxiliary genes had distinct fitness-effect distributions, with core genes showing heavier tails in both the negative direction, indicating importance, and the positive direction, indicating that carrying the gene is burdensome under particular conditions. [src: fitness_effects_conservation]

### Condition-specific effects are enriched among core genes

Genes tagged with strong condition-specific effects in the `specificphenotype` annotation were 77.3% core, compared with 70.3% for genes without specific phenotypes; the association had OR=1.78 and p=1.8e-97. This contradicts the naive expectation that condition-specific genes would be predominantly accessory; the report suggests, as a possible explanation only, that core genes can have measurable condition-specific effects because they participate in well-characterized pathways. [src: fitness_effects_conservation]

### Ephemeral niche genes

A total of 4,450 genes (2.7%) fit the ephemeral-niche pattern of being neutral overall but critical in one condition. These genes were more common among core genes (3.0%) than auxiliary genes (1.7%) or singleton genes (1.6%); the report proposes, without demonstrating it, that core genes may have more detectable conditional effects because they participate in more pathways. [src: fitness_effects_conservation]

### Novel genes are largely neutral under tested laboratory conditions

Novel singleton genes showed near-zero mean fitness, suggesting that they were largely invisible to the tested laboratory fitness assays rather than systematically beneficial or detrimental. The report notes that this apparent neutrality may also reflect poor transposon coverage. [src: fitness_effects_conservation]

### Overall interpretation

Across the full spectrum, gene fitness importance and pangenome conservation were positively correlated: essential genes were 82% core, whereas always-neutral genes were 66% core, a 16-percentage-point gradient spanning approximately 194,000 genes across 43 diverse bacteria. The gradient was statistically robust but conservation was only weakly predicted by fitness importance. [src: fitness_effects_conservation]

From these patterns the report draws the hypothesis that core genes are the most functionally active genes under the tested conditions, with larger fitness effects in both directions possibly because they are embedded in critical pathways, whereas accessory genes tend to be functionally quieter in laboratory assays. This whole explanation is an inference from the observed distributions, not a measured result; it is consistent with stronger purifying selection on core genes and with pangenome models in which selection contributes to gene-frequency distributions, but the analysis itself does not establish that selection is the sole driver. [src: fitness_effects_conservation]

## Literature Context

As external background, the report cites Luo et al. (2015) as showing that core genes have stronger purifying selection than accessory genes across bacterial species, which it treats as consistent with its finding that genes with stronger fitness effects are more likely core. [src: fitness_effects_conservation]

The report also cites McInerney et al. (2017), who reviewed the gene-sharing network view of pangenomes and argued that gene-frequency distributions reflect a balance of selection, drift, and HGT (horizontal gene transfer); the report interprets its own fitness-conservation gradient as empirical support for selection as a major driver of core-gene maintenance, an interpretation rather than a direct test. [src: fitness_effects_conservation]

## Data Sources

- Fitness Browser: RB-TnSeq mutant fitness data for ~194K genes, attributed to Price et al. (2018). [src: fitness_effects_conservation]
- KBase pangenome link table: gene-to-cluster conservation mapping at `conservation_vs_fitness/data/fb_pangenome_link.tsv`. [src: fitness_effects_conservation]
- Essential genes: essentiality classification from `conservation_vs_fitness/data/essential_genes.tsv`. [src: fitness_effects_conservation]
- Specific phenotypes: condition-specific fitness annotations from the Fitness Browser `specificphenotype` table. [src: fitness_effects_conservation]

The report credits Price et al. (2018) with generating the Fitness Browser data, described as the largest resource of genome-wide mutant fitness data for bacteria, and states that this analysis adds a pangenome conservation dimension to those fitness measurements. [src: fitness_effects_conservation]

## Figures

The report includes figures on conservation by fitness profile (`conservation_by_fitness_profile.png`), fitness magnitude versus conservation (`fitness_magnitude_vs_conservation.png`), fitness breadth versus conservation (`fitness_breadth_vs_conservation.png`), broad versus specific conservation (`broad_vs_specific_conservation.png`), burden genes by conservation (`burden_genes_by_conservation.png`), a cost-benefit portrait (`cost_benefit_portrait.png`), conservation by condition type (`conservation_by_condition_type.png`), fitness distributions by conservation (`fitness_distributions_by_conservation.png`), and novel-gene mean fitness (`novel_gene_mean_fitness.png`). [src: fitness_effects_conservation]

## Caveats

The fitness measurements are biased toward rich media and standard stresses, so many ecological niches are unrepresented. [src: fitness_effects_conservation]

The 16-percentage-point conservation gradient, although statistically robust, means that fitness importance is only a weak predictor of conservation. [src: fitness_effects_conservation]

Fitness measurements were based on single-gene knockouts and therefore did not capture epistatic interactions. [src: fitness_effects_conservation]

The Fitness Browser covered 43 bacteria, primarily Proteobacteria, limiting generalizability to other bacterial lineages. [src: fitness_effects_conservation]

Singleton and novel genes may lack fitness data because of poor transposon coverage rather than true neutrality. [src: fitness_effects_conservation]

## Slots Into

- [[concepts/gene-essentiality]] — links essentiality, fitness-effect magnitude, and fitness breadth to pangenome conservation.
- [[concepts/condition-specific-fitness]] — adds evidence that condition-specific and ephemeral-niche fitness effects are enriched among core genes rather than restricted to accessory genes.
- [[concepts/pangenome-integration]] — connects Fitness Browser mutant phenotypes with core, auxiliary, and singleton gene conservation across bacterial pangenomes.
- [[concepts/laboratory-fitness-versus-natural-selection]] — the essential-to-neutral conservation gradient is robust but weak, and lab conditions are biased toward rich media and single knockouts.
- [[concepts/pangenome-conservation-fitness-decoupling]] — fitness importance and breadth predict core status only weakly.
- [[concepts/core-genome-burden-paradox]] — core genes are more often beneficial when deleted and have heavier fitness tails in both directions.
- [[concepts/costly-dispensable-gene-loss]] — auxiliary genes are not more often burdensome than core genes.
- [[concepts/condition-dependent-gene-tradeoffs]] — trade-offs are proposed as a possible explanation for beneficial core-gene deletions; the ephemeral-niche pattern (neutral overall but critical in one condition) is instead proposed to reflect greater detectability of conditional effects in core genes through pathway participation.
- [[concepts/genetic-perturbation-coverage-bias]] — novel-gene neutrality and Proteobacteria-dominated sampling limit what the assays can detect.
- [[concepts/transposon-callability-bias]] — poor transposon coverage may masquerade as neutrality for singleton genes.
- [[concepts/fitness-condition-coverage-prioritization-bias]] — tested conditions favor rich media and standard stresses.
- [[summaries/conservation_fitness_synthesis__REPORT]] — compares fitness importance and conservation across the full gene spectrum, including the core-gene cost-benefit pattern.
