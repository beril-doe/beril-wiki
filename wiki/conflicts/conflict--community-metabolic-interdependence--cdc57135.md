<!-- tension-hash: cdc57135de0f0da0 -->
# Is Latent Metabolic Capability Condition-Dependent or Partly Fitness-Neutral?

Projects disagree on what "latent capability" means. A latent capability is a metabolic pathway that the genome predicts to be complete but that shows no fitness importance under the conditions tested. One analysis reports that all Latent Capabilities became fitness-important under condition-specific analyses. [src: discoveries] A broader analysis instead classifies a threshold-sensitive fraction of complete pairs as latent under its stated fitness thresholds. [src: metabolic_capability_dependency] This matters for [[concepts/community-metabolic-interdependence]]. That page asks whether genomically complete pathways reflect actual reliance, and these results answer that question differently.

## Evidence Sides

**Side A: latent capability is condition-dependent**

The first study covered 7 Fitness Browser organisms and 23 GapMind pathways. The Fitness Browser is a collection of mutant fitness data, and GapMind is a tool that predicts whether a pathway is complete in a genome. In this study, 41.0% of pathway-organism pairs were Latent Capabilities, and all Latent Capabilities became fitness-important under condition-specific analyses. [src: discoveries]

A newer analysis of 161 pairs **supports** this condition-dependent result. However, its 66 latent pairs and its threshold caveat do not resolve the disagreement. It uses another organism set and pathway set, and its classification is median-based (a median is the middle value of ordered observations). The evidence does not specify how the median enters the classification. [src: pathway_capability_dependency] Side A therefore has partial corroboration from an analysis that is not directly comparable. [src: pathway_capability_dependency]

**Side B: a fraction of complete pathways is latent under fitness thresholds**

The broader analysis classified 267 of 1,695 complete pairs (15.8%) as latent under its stated fitness thresholds. [src: metabolic_capability_dependency] The latent fraction remained between 4.7% and 21.1% across 16 threshold combinations. [src: metabolic_capability_dependency] The result therefore depends on the thresholds chosen, but it does not fall to zero across the combinations tested. [src: metabolic_capability_dependency]

The open question is this: is latent capability generally a condition-dependent dependency, or does a substantial fraction remain fitness-neutral across tested conditions?

## Possible Reconciliations

- *Hypothesis:* The two sides measure different things. Side A asks whether a pathway ever becomes important under any condition subset. Side B asks whether a pathway passes fitness thresholds under its tested conditions. If so, both results could hold at once.
- *Hypothesis:* Classification rules drive the gap. A median-based classification and an explicit fitness-threshold classification may sort borderline pairs differently, so the latent counts would not be comparable.
- *Hypothesis:* Organism and pathway sampling drive the gap. The small study's organism and pathway selection may be enriched for pathways that respond to the conditions profiled, while a broader set includes pathways that no profiled condition engages.
- *Hypothesis:* "All latent pairs become important" partly reflects multiple testing. Searching across many condition-specific analyses raises the chance that any pathway crosses an importance cutoff somewhere.

## Resolving Work

- Re-run both classification schemes, median-based and fixed fitness thresholds, on one shared organism-pathway set. This asks whether the latent fraction changes with the method alone.
- Apply the condition-stratified test from Side A to the 267 latent pairs from Side B. This asks what share become fitness-important under a specific condition and what share stay fitness-neutral.
- Restrict the broader analysis to the 7 organisms and 23 pathways of the small study and compare classifications pair by pair. This isolates how much of the gap comes from sampling.
- Add a multiple-testing correction across condition-specific analyses. This asks whether "becomes fitness-important" survives once the number of conditions searched is controlled for.
- Stratify latent outcomes by pathway type and by condition type, such as stress or nutrient limitation. This asks whether persistent fitness-neutrality is concentrated in particular pathway classes.
