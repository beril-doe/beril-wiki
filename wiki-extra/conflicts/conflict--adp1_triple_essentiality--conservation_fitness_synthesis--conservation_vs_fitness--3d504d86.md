---
title: Graded Fitness Predicts Essentiality, but Binary Assays Disagree
type: Conflict
sources:
- id: adp1_triple_essentiality
  resource: ../../wiki/summaries/adp1_triple_essentiality__REPORT.md
  title: adp1 triple essentiality
- id: fitness_effects_conservation
  resource: ../../wiki/summaries/fitness_effects_conservation__REPORT.md
  title: fitness effects conservation
- id: conservation_vs_fitness
  resource: ../../wiki/summaries/conservation_vs_fitness__REPORT.md
  title: conservation vs fitness
- id: core_gene_tradeoffs
  resource: ../../wiki/summaries/core_gene_tradeoffs__REPORT.md
  title: core gene tradeoffs
- id: conservation_fitness_synthesis
  resource: ../../wiki/summaries/conservation_fitness_synthesis__REPORT.md
  title: conservation fitness synthesis
---
<!-- tension-hash: 55f3e0e9f8379587 -->
# Graded Fitness Predicts Essentiality, but Binary Assays Disagree
The central disagreement is whether transposon-based fitness measurements can stand in for complete-knockout essentiality. Evidence from [essentiality-assay-discordance](../../wiki/concepts/essentiality-assay-discordance.md) supports two conclusions that must be kept separate: continuous fitness contains useful information about knockout lethality, while thresholded RB-TnSeq essentiality shows poor agreement with complete-knockout calls. Conservation and costly-conserved-gene analyses add biological context, but they do not by themselves determine whether a gene is essential under natural conditions.

## Evidence Sides

**Continuous fitness and conservation support an informative gradient.** Continuous transposon fitness contains useful information about knockout lethality, supported by AUC values of 0.700 and 0.725 for inverted fitness. [^adp1_triple_essentiality] The conservation evidence supports this graded-fitness conclusion: across 43 bacteria, essential genes were 82% core versus 66% for always-neutral genes. [^fitness_effects_conservation] A separate 33-organism linkage reports 86.1% core for essential genes versus 81.2% for non-essential genes. [^conservation_vs_fitness] These conservation gradients were directionally consistent, although the gradient was statistically robust yet weak. [^fitness_effects_conservation]

**Thresholded essentiality and natural-fitness interpretations remain unreliable.** Thresholded RB-TnSeq essentiality shows poor agreement with complete-knockout calls: the 0.05-threshold AUC for essentiality fraction was 0.344, with Cohen’s kappa of -0.081. [^adp1_triple_essentiality] Singleton neutrality may reflect poor transposon coverage rather than true neutrality, so conservation cannot independently establish that an apparently neutral insertion mutant retains function. [^fitness_effects_conservation] Likewise, the Costly + Conserved category in core_gene_tradeoffs is inferred from laboratory burden and conservation, not direct evidence of natural selection. [^core_gene_tradeoffs] The synthesis identifies 28,017 genes as both costly and conserved and 5,526 as costly and dispensable, but treats these categories as selection signatures rather than direct natural-fitness measurements. [^conservation_fitness_synthesis] The two conservation results also use different category definitions and organism sets, so neither resolves insertion-versus-complete-knockout disagreement. [^fitness_effects_conservation][^conservation_vs_fitness]

## Possible Reconciliations

- **Hypothesis — graded versus binary measurement:** Continuous fitness may preserve ranking information that is lost when insertion fitness is converted into a thresholded essential/non-essential call.
- **Hypothesis — perturbation and condition scope:** Transposon insertion and complete knockout may differ in perturbation strength, genetic context, or assay condition, producing genuine modality-specific calls.
- **Hypothesis — coverage and category definitions:** Poor transposon coverage could create apparent neutrality, while the two conservation analyses’ different organism sets and category definitions could explain their numerical differences.
- **Hypothesis — ecological scope:** Costly-and-conserved genes may reflect selection-related signatures without implying essentiality in the laboratory or in every natural environment.

## Resolving Work

- Compare continuous insertion fitness and complete-knockout growth for the same genes, conditions, and strains; test whether rank-based prediction remains informative when binary thresholds fail.
- Quantify insertion-site coverage and replicate variance for singleton-neutral genes; test whether coverage-adjusted neutrality improves agreement with complete-knockout calls.
- Reanalyze both conservation datasets using identical organism sets and identical essential/non-essential definitions; test whether the 82% versus 66% and 86.1% versus 81.2% contrasts persist.
- Measure costly-and-conserved genes across ecologically relevant environments; test whether laboratory burden and conservation predict natural fitness rather than merely selection signatures.

[^adp1_triple_essentiality]: [adp1 triple essentiality](../../wiki/summaries/adp1_triple_essentiality__REPORT.md)
[^fitness_effects_conservation]: [fitness effects conservation](../../wiki/summaries/fitness_effects_conservation__REPORT.md)
[^conservation_vs_fitness]: [conservation vs fitness](../../wiki/summaries/conservation_vs_fitness__REPORT.md)
[^core_gene_tradeoffs]: [core gene tradeoffs](../../wiki/summaries/core_gene_tradeoffs__REPORT.md)
[^conservation_fitness_synthesis]: [conservation fitness synthesis](../../wiki/summaries/conservation_fitness_synthesis__REPORT.md)
