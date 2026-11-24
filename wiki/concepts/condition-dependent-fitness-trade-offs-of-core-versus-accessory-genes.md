---
type: "Concept"
description: "Genes important in some conditions and burdensome in others, and whether core genes are enriched for such trade-offs relative to accessory genes; stops at laboratory knockout evidence."
sources: ["summaries/conservation_fitness_synthesis__REPORT.md", "summaries/core_gene_tradeoffs__REPORT.md", "summaries/discoveries.md", "summaries/fitness_effects_conservation__REPORT.md"]
---
# Condition-dependent fitness trade-offs of core versus accessory genes

In laboratory knockout fitness data, core genes are more often trade-off genes than accessory genes, and they also show more condition-specific effects. The 1.29x trade-off result appears in both the synthesis dataset and a Fitness Browser (FB) analysis, and the 1.78x condition-specific result appears in the synthesis dataset and in FB. [src: conservation_fitness_synthesis, core_gene_tradeoffs, fitness_effects_conservation] The evidence comes from laboratory knockout fitness only. The reports propose pathway participation and detectability as explanations and caution that condition-specific effects do not imply niche specificity. [src: conservation_fitness_synthesis, core_gene_tradeoffs, fitness_effects_conservation] See also [[concepts/costly-but-conserved-genes-laboratory-burden-versus-conservation]] and [[concepts/gene-fitness-importance-as-a-predictor-of-pangenome-conservation]].

## Trade-off genes are enriched in the core genome

In the FB analysis, 25,271 genes (17.8%) are true trade-off genes: important (fit < -1) in some conditions and burdensome (fit > 1) in others. [src: core_gene_tradeoffs, discoveries] These genes are 1.29x more likely to be core (odds ratio, OR=1.29, p=1.2e-44). [src: core_gene_tradeoffs, discoveries] The synthesis report gives the same 1.29x enrichment in its dataset. [src: conservation_fitness_synthesis]

The same pattern appears for deletion benefits. Core genes were more likely than auxiliary genes to show positive fitness effects when deleted (24.4% ever beneficial versus 19.9%; OR=0.77 for auxiliary vs core, p=5.5e-48). [src: discoveries, fitness_effects_conservation] This runs counter to the expectation that accessory genes carry a cost. [src: discoveries] Core genes also have heavier tails than auxiliary genes in both the important and burdensome directions. [src: fitness_effects_conservation]

## Condition-specific effects

Genes with strong condition-specific effects are 77.3% core versus 70.3% for genes without specific phenotypes (OR=1.78, p=1.8e-97). [src: fitness_effects_conservation] The synthesis report states this as 1.78x more likely to be core. [src: conservation_fitness_synthesis] The core_gene_tradeoffs report reads it as evidence that the conserved genome is functionally active. [src: core_gene_tradeoffs]

"Ephemeral niche" genes are neutral overall but critical in one condition. [src: fitness_effects_conservation] They are more common in core genes (3.0%) than auxiliary (1.7%) or singleton (1.6%) genes. [src: fitness_effects_conservation]

## Proposed explanations

These explanations are proposals from the reports. The cited claims do not describe a direct test of them. One proposal is that core genes have more trade-offs because they sit in more pathways with condition-dependent costs and benefits. [src: core_gene_tradeoffs, discoveries, fitness_effects_conservation] On this view, the result challenges the "streamlining" model in which accessory genes are metabolic burdens. [src: discoveries] A second proposal is that core genes have more measurable condition-specific effects because they take part in well-characterized pathways or more pathways. [src: fitness_effects_conservation]

## Caveats

- Condition-specific does not mean niche-specific. Strongly condition-specific genes are more likely core, because core genes have more detectable effects. [src: conservation_fitness_synthesis]
- Laboratory conditions capture only a fraction of the conditions bacteria face in nature. [src: core_gene_tradeoffs]
- FB condition types are biased toward experimental convenience, not ecological relevance. [src: core_gene_tradeoffs]
- Burden (fit > 1) may reflect trade-offs rather than true dispensability. [src: core_gene_tradeoffs]
- Whether organisms from more variable environments have more core trade-off genes is still open. [src: conservation_fitness_synthesis]

## Open Directions

- Connect laboratory fitness to AlphaEarth environmental data to ask whether organisms from more variable environments have more trade-off genes in their core.
- Test the pathway-participation explanation. Compare trade-off enrichment after controlling for the number of pathways per gene.
- Check whether detectability drives the core enrichment. Compare effect sizes after matching core and accessory genes on expression or annotation depth.
