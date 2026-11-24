---
type: "Organism"
description: "Cyanobacterium (SynE) that was an outlier in metal-NaCl overlap due to many NaCl dose-response experiments."
sources: ["summaries/counter_ion_effects__REPORT.md", "summaries/discoveries.md", "summaries/metal_fitness_atlas__REPORT.md", "summaries/pitfalls.md"]
aliases: ["SynE"]
---
# Synechococcus elongatus

This page covers Synechococcus elongatus (SynE), a cyanobacterium that was an outlier in metal–NaCl overlap because of its many NaCl dose-response experiments. Removing it changed the overall result only modestly. [src: counter_ion_effects]

## Key facts

- SynE had 12 NaCl dose-response experiments spanning 0.5–250 mM. Other organisms had 1–6 NaCl experiments. [src: counter_ion_effects, discoveries]
- It flags 32.6% of genes as NaCl-important, 3× higher than the next organism. [src: pitfalls]
- In the metal fitness atlas, SynE is notably metal-sensitive, with 33.6% of genes important across just 2 metals. [src: metal_fitness_atlas]

## The shared-stress outlier

SynE showed 88.6% shared-stress (565/638 genes) in the metal–NaCl comparison. [src: counter_ion_effects] The `n_sick >= 1` threshold is much easier to satisfy with 12 experiments, which explains the inflated rate. [src: counter_ion_effects, discoveries] The pitfalls digest cites this as a case where unequal experiment counts inflate cross-condition overlap statistics. [src: pitfalls] See [[concepts/metal-tolerance-determinants-and-shared-stress-confounding]] and [[concepts/shared-metal-and-osmotic-stress-fitness-determinants]].

## Effect on the overall result

Excluding SynE reduced overall metal–NaCl overlap from 39.8% to 36.7% (3,739/10,183). The report reads this as showing the finding is not driven by SynE. [src: counter_ion_effects, discoveries] The pitfalls digest calls the change modest but worth documenting. [src: pitfalls]

## Related

- [[summaries/counter_ion_effects__REPORT]]
- [[summaries/metal_fitness_atlas__REPORT]]
- [[concepts/metal-fitness-breadth-and-magnitude-across-metals-and-organisms]]
