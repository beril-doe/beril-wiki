---
type: "Research direction"
description: "Why are genes needed under metal stress more often core, and more so for essential metals than toxic ones?"
hypothesis: "Core enrichment of metal-important genes comes from general stress and housekeeping functions; metal-specific genes with no other-stress phenotype are not more core than baseline, and the essential-versus-toxic gap disappears once gene detectability is matched."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The metal experiments and core calls are in cataloged tables, and the matched regression has not been run."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.genefitness", "kescience.fitnessbrowser.experiment", "kescience.fitnessbrowser.specificphenotype", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.gene_genecluster_junction"]
findings: ["metal_fitness_atlas--7bedd365", "metal_fitness_atlas--9bd179d0", "counter_ion_effects--d169eaa1", "field_vs_lab_fitness--6def5903"]
conflicts: []
papers: ["29769716", "25968644", "12829273", "37065130"]
builds_on: ["findings/metal_fitness_atlas--7bedd365", "findings/metal_fitness_atlas--9bd179d0", "findings/counter_ion_effects--d169eaa1", "findings/field_vs_lab_fitness--6def5903"]
projects: ["counter_ion_effects", "field_vs_lab_fitness", "metal_fitness_atlas"]
topics: ["laboratory-fitness-versus-natural-selection-and-gene-conservation"]
---
# Does the core-genome enrichment of metal-stress genes reflect general stress robustness rather than metal-specific selection?

Why are genes needed under metal stress more often core, and more so for essential metals than toxic ones?

## Hypothesis

Core enrichment of metal-important genes comes from general stress and housekeeping functions; metal-specific genes with no other-stress phenotype are not more core than baseline, and the essential-versus-toxic gap disappears once gene detectability is matched.

## Why it matters

It would separate niche-specific selection from general functional importance as the cause of conservation, and show how far metal tolerance can be predicted from the core genome.

## How to test it

Across Fitness Browser organisms with metal experiments, define metal-specific genes (important under a metal, not under NaCl or other stresses), and compare their core fraction with baseline, per metal. Match core and accessory genes on annotation depth and fitness magnitude, and regress core status on magnitude and condition class together. Check whether the essential-versus-toxic difference survives.

## What would support or refute it

Support: metal-specific genes show no core enrichment, or it vanishes after matching. Refute: enrichment stays for metal-specific genes after matching, as in 12 of 14 metals after shared-stress removal.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The metal experiments and core calls are in cataloged tables, and the matched regression has not been run.

## Builds on

- Finding: [[findings/metal_fitness_atlas--7bedd365|Metal-stress fitness genes are enriched in the core genome]] (Candidate novel)
- Finding: [[findings/metal_fitness_atlas--9bd179d0|Essential-metal tolerance genes are more core-enriched than toxic-metal genes]] (Candidate novel)
- Finding: [[findings/counter_ion_effects--d169eaa1|Core-genome enrichment in the Metal Fitness Atlas survives shared-stress removal]] (Candidate novel)
- Finding: [[findings/field_vs_lab_fitness--6def5903|Fitness magnitude predicted conservation more than condition type in DvH]] (Candidate novel)

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.
- [PMID 12829273](https://pubmed.ncbi.nlm.nih.gov/12829273/) Efflux-mediated heavy metal resistance in prokaryotes.
- [PMID 37065130](https://pubmed.ncbi.nlm.nih.gov/37065130/) Large-scale genetic characterization of the model sulfate-reducing bacterium, Desulfovibrio vulgaris Hildenborough.

29769716 and 25968644 provide the fitness assays and 12829273 describes efflux resistance, but none compares core status of metal-specific versus general stress genes.
