---
type: "Research direction"
description: "Do metal-specific fitness genes differ from general sick genes in core status because they are accessory efflux and uptake systems acquired by horizontal transfer?"
hypothesis: "Metal-specific genes are more often accessory and mobile-element-linked than general sick genes, and essential-metal genes carry the larger core shift, because they serve ancient metal homeostasis rather than detoxification."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Metal-condition fitness and pangenome tables are in the catalog, but gene-class labelling and neighbourhood analysis need compute."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.experiment", "kbase.ke_pangenome.gene_cluster", "kescience.fitnessbrowser.seedannotation"]
findings: ["metal_specificity--22ced2b7", "metal_fitness_atlas--7bedd365", "metal_fitness_atlas--9bd179d0", "counter_ion_effects--d169eaa1", "metal_fitness_atlas--b6961196"]
conflicts: []
papers: ["29769716", "12829273", "30729256", "27474723"]
builds_on: ["findings/metal_specificity--22ced2b7", "findings/metal_fitness_atlas--7bedd365", "findings/metal_fitness_atlas--9bd179d0", "findings/counter_ion_effects--d169eaa1", "findings/metal_fitness_atlas--b6961196"]
projects: ["counter_ion_effects", "metal_fitness_atlas", "metal_specificity"]
topics: ["gene-fitness-landscapes-and-cofitness-modules"]
---
# Why do metal-specific genes lean less toward the core genome than general stress genes?

Do metal-specific fitness genes differ from general sick genes in core status because they are accessory efflux and uptake systems acquired by horizontal transfer?

## Hypothesis

Metal-specific genes are more often accessory and mobile-element-linked than general sick genes, and essential-metal genes carry the larger core shift, because they serve ancient metal homeostasis rather than detoxification.

## Why it matters

It would show whether metal tolerance is a conserved core capability or a patchy acquired trait, and why bioleaching specialists show no extra signal.

## How to test it

Across Fitness Browser organisms with metal experiments, label genes as metal-specific, shared-stress or general sick. Compare core fraction, nearness to mobile-element genes, and annotation keywords using pangenome core flags and SEED annotations. Fit metal class (essential vs toxic) with organism as a random effect, excluding single-organism metals.

## What would support or refute it

Support: metal-specific genes are more accessory and mobile-linked, and essential-metal genes keep the core shift in 3 or more organisms. Refute: no mobile-element difference, or the essential-toxic contrast depends on one organism.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Metal-condition fitness and pangenome tables are in the catalog, but gene-class labelling and neighbourhood analysis need compute.

## Builds on

- Finding: [[findings/metal_specificity--22ced2b7|Metal-specific genes are less core-enriched than general sick genes]] (Candidate novel)
- Finding: [[findings/metal_fitness_atlas--7bedd365|Metal-stress fitness genes are enriched in the core genome]] (Candidate novel)
- Finding: [[findings/metal_fitness_atlas--9bd179d0|Essential-metal tolerance genes are more core-enriched than toxic-metal genes]] (Candidate novel)
- Finding: [[findings/counter_ion_effects--d169eaa1|Core-genome enrichment in the Metal Fitness Atlas survives shared-stress removal]] (Candidate novel)
- Finding: [[findings/metal_fitness_atlas--b6961196|Bioleaching genera are not enriched for metal-tolerance signature]] (Candidate novel)

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 12829273](https://pubmed.ncbi.nlm.nih.gov/12829273/) Efflux-mediated heavy metal resistance in prokaryotes.
- [PMID 30729256](https://pubmed.ncbi.nlm.nih.gov/30729256/) Gene function and expression regulation of RuvRCAB in bacterial Cr(VI), As(III), Sb(III), and Cd(II) resistance.
- [PMID 27474723](https://pubmed.ncbi.nlm.nih.gov/27474723/) Novel Metal Cation Resistance Systems from Mutant Fitness Analysis of Denitrifying Pseudomonas stutzeri.

29769716 and 12829273 describe fitness data and efflux systems but not core versus accessory status of metal-specific genes.
