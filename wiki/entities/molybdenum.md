---
type: Compound
description: Molybdenum (Mo), an essential metal with conserved stress-associated
  fitness determinants.
sources:
- id: metal_cross_resistance
  resource: ../summaries/metal_cross_resistance__REPORT.md
  title: metal cross resistance
- id: metal_fitness_atlas
  resource: ../summaries/metal_fitness_atlas__REPORT.md
  title: metal fitness atlas
- id: metal_specificity
  resource: ../summaries/metal_specificity__REPORT.md
  title: metal specificity
title: Molybdenum
---
# Molybdenum

## Identity

**Canonical name:** Molybdenum [^metal_cross_resistance]

**Known alias:** Mo [^metal_cross_resistance]

**Stable external identifier:** No stable external identifier was reported in the source document. [^metal_cross_resistance]

## Evidence across projects

Molybdenum was the most independent metal in the 13-metal DvH dataset, showing weaker similarity to the other metals than the remaining metals in that dataset. [^metal_cross_resistance] This finding contributes to the chemistry-dependent magnitude layer of [metal-cross-resistance](../concepts/metal-cross-resistance.md), in which cross-resistance is broadly positive but varies in strength among metal pairs. [^metal_cross_resistance]

The [metal_fitness_atlas__REPORT](../summaries/metal_fitness_atlas__REPORT.md) **refines** this interpretation by showing that molybdenum-associated fitness genes were strongly core-enriched: 302 important genes had a core fraction of 0.950, delta +0.148, OR=5.32, and p=1.3e-14. [^metal_fitness_atlas] Molybdenum was also among the essential metals whose tolerance genes showed stronger core enrichment than toxic-metal tolerance genes; the essential-metal mean core-fraction delta was +0.148 versus +0.081 for toxic metals (U=39, p=0.015). [^metal_fitness_atlas] This **supports** a distinction between conserved cellular functions vulnerable to metal stress and specialized accessory resistance mechanisms, rather than implying that molybdenum responses are uniformly shared across metals. [^metal_fitness_atlas]

The [metal_specificity__REPORT](../summaries/metal_specificity__REPORT.md) **refines** this core-enrichment picture by classifying 185 of 306 molybdenum-important gene records (60.5%) as metal-specific—significant under metal stress but with a sick rate below 5% across non-metal experiments. [^metal_specificity] Thus, strong conservation and substantial condition specificity coexist for molybdenum-associated genes; this result is based on the subset with usable fitness-matrix identifiers. [^metal_specificity]

The result was based on gene-level fitness responses analyzed across diverse bacteria and is part of the cross-resistance structure summarized in [metal_cross_resistance__REPORT](../summaries/metal_cross_resistance__REPORT.md). [^metal_cross_resistance]

## Related pages

- [metal-cross-resistance](../concepts/metal-cross-resistance.md) — synthesis of conserved and chemistry-dependent metal cross-resistance.
- [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) — gene-level fitness correlations across metal conditions.
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — condition-linked gene importance measured across metal experiments.
- [metal_cross_resistance__REPORT](../summaries/metal_cross_resistance__REPORT.md) — source-project summary.
- [metal_fitness_atlas__REPORT](../summaries/metal_fitness_atlas__REPORT.md) — cross-species metal fitness atlas.
- [metal_specificity__REPORT](../summaries/metal_specificity__REPORT.md) — metal-specific versus general-stress gene classification.

[^metal_cross_resistance]: [metal cross resistance](../summaries/metal_cross_resistance__REPORT.md)
[^metal_fitness_atlas]: [metal fitness atlas](../summaries/metal_fitness_atlas__REPORT.md)
[^metal_specificity]: [metal specificity](../summaries/metal_specificity__REPORT.md)
