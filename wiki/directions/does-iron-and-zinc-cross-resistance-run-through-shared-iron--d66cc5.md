---
type: "Research direction"
description: "Iron and zinc show unexpectedly strong shared fitness effects across bacteria. Is that coupling carried by genes that build or repair iron-sulfur cluster proteins?"
hypothesis: "Genes shared between iron and zinc stress are enriched for iron-sulfur cluster assembly and repair. Removing these genes should weaken iron-zinc coupling more than it weakens coupling between other metal pairs."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Experiment, gene and function-description tables are shown, while gene-level fitness values sit in tables outside the sample shown; the cross-metal matrices would be rebuilt."
databases: ["kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.experiment", "kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.kgroupdesc"]
findings: ["metal_cross_resistance--8b1ef6ba", "metal_cross_resistance--fbb37c50"]
conflicts: ["conflict--metal-cross-resistance--59068bf5"]
papers: ["31586033", "37272830", "22125499"]
builds_on: ["findings/metal_cross_resistance--8b1ef6ba", "findings/metal_cross_resistance--fbb37c50", "conflicts/conflict--metal-cross-resistance--59068bf5"]
projects: ["metal_cross_resistance", "metal_specificity"]
topics: ["resistance-defense-systems-and-mobile-elements"]
---
# Does iron and zinc cross-resistance run through shared iron-sulfur cluster maintenance genes?

Iron and zinc show unexpectedly strong shared fitness effects across bacteria. Is that coupling carried by genes that build or repair iron-sulfur cluster proteins?

## Hypothesis

Genes shared between iron and zinc stress are enriched for iron-sulfur cluster assembly and repair. Removing these genes should weaken iron-zinc coupling more than it weakens coupling between other metal pairs.

## Why it matters

It would give a mechanism for a cross-resistance pattern that is currently only described. It would also help decide whether universal positive metal cross-resistance reflects a specific vulnerability or a general stress response.

## How to test it

In the organisms of the fitness collection that have iron and zinc experiments, find the genes important under both metals and annotate them for iron-sulfur cluster biogenesis. Test enrichment against genes shared by other metal pairs. Recompute iron-zinc coupling after removing the iron-sulfur genes and compare the drop with other pairs. Then test iron-sulfur cluster mutants of Escherichia coli for zinc sensitivity that iron supplementation rescues.

## What would support or refute it

Support: iron-sulfur genes are enriched among genes shared by iron and zinc, coupling falls when they are removed, and iron rescues the mutants. Refutation: the shared genes fall in envelope or transport functions and removing iron-sulfur genes leaves the coupling intact.

## Data

Approach: analysis then experiment. Readiness: needs compute. Experiment, gene and function-description tables are shown, while gene-level fitness values sit in tables outside the sample shown; the cross-metal matrices would be rebuilt.

## Builds on

- Finding: [[findings/metal_cross_resistance--8b1ef6ba|Iron and zinc show unexpectedly strong cross-resistance]] (Extends retrieved work)
- Finding: [[findings/metal_cross_resistance--fbb37c50|Gene-level metal cross-resistance is almost uniformly positive across diverse bacteria]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--metal-cross-resistance--59068bf5|Universal Positive Metal Cross-Resistance: Metal-Specific Mechanism or General-Stress Response?]]

## Closest published work

- [PMID 31586033](https://pubmed.ncbi.nlm.nih.gov/31586033/) Zinc excess increases cellular demand for iron and decreases tolerance to copper in Escherichia coli.
- [PMID 37272830](https://pubmed.ncbi.nlm.nih.gov/37272830/) Functional Characterization of FeoAB in Iron Acquisition and Pathogenicity in Riemerella anatipestifer.
- [PMID 22125499](https://pubmed.ncbi.nlm.nih.gov/22125499/) Evidence-based annotation of gene function in Shewanella oneidensis MR-1 using genome-wide fitness profiling across 121 conditions.

PMID 31586033 shows zinc excess disturbs iron homeostasis in E. coli, and PMID 37272830 links iron uptake to zinc responses. Both are single-organism studies, and neither tests iron-sulfur genes as the carrier of coupling across many species.
