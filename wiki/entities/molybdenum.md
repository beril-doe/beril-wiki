---
type: "Compound"
description: "Molybdenum (Mo), an essential metal with conserved stress-associated fitness determinants."
sources: ["summaries/metal_cross_resistance__REPORT.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/metal_specificity__REPORT.md"]
---
# Molybdenum

## Identity

**Canonical name:** Molybdenum [src: metal_cross_resistance]

**Known alias:** Mo [src: metal_cross_resistance]

**Stable external identifier:** No stable external identifier was reported in the source document. [src: metal_cross_resistance]

## Evidence across projects

Molybdenum was the most independent metal in the 13-metal DvH dataset, showing weaker similarity to the other metals than the remaining metals in that dataset. [src: metal_cross_resistance] This finding contributes to the chemistry-dependent magnitude layer of [[concepts/metal-cross-resistance]], in which cross-resistance is broadly positive but varies in strength among metal pairs. [src: metal_cross_resistance]

The [[summaries/metal_fitness_atlas__REPORT]] **refines** this interpretation by showing that molybdenum-associated fitness genes were strongly core-enriched: 302 important genes had a core fraction of 0.950, delta +0.148, OR=5.32, and p=1.3e-14. [src: metal_fitness_atlas] Molybdenum was also among the essential metals whose tolerance genes showed stronger core enrichment than toxic-metal tolerance genes; the essential-metal mean core-fraction delta was +0.148 versus +0.081 for toxic metals (U=39, p=0.015). [src: metal_fitness_atlas] This **supports** a distinction between conserved cellular functions vulnerable to metal stress and specialized accessory resistance mechanisms, rather than implying that molybdenum responses are uniformly shared across metals. [src: metal_fitness_atlas]

The [[summaries/metal_specificity__REPORT]] **refines** this core-enrichment picture by classifying 185 of 306 molybdenum-important gene records (60.5%) as metal-specific—significant under metal stress but with a sick rate below 5% across non-metal experiments. [src: metal_specificity] Thus, strong conservation and substantial condition specificity coexist for molybdenum-associated genes; this result is based on the subset with usable fitness-matrix identifiers. [src: metal_specificity]

The result was based on gene-level fitness responses analyzed across diverse bacteria and is part of the cross-resistance structure summarized in [[summaries/metal_cross_resistance__REPORT]]. [src: metal_cross_resistance]

## Related pages

- [[concepts/metal-cross-resistance]] — synthesis of conserved and chemistry-dependent metal cross-resistance.
- [[concepts/cofitness-network-architecture]] — gene-level fitness correlations across metal conditions.
- [[concepts/condition-specific-fitness]] — condition-linked gene importance measured across metal experiments.
- [[summaries/metal_cross_resistance__REPORT]] — source-project summary.
- [[summaries/metal_fitness_atlas__REPORT]] — cross-species metal fitness atlas.
- [[summaries/metal_specificity__REPORT]] — metal-specific versus general-stress gene classification.
