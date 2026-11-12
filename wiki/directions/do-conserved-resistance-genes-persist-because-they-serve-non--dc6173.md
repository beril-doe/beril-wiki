---
type: "Research direction"
description: "Resistance mechanism predicts whether a resistance gene is conserved across a species, yet not the growth cost of disrupting it. Are intrinsic efflux pumps and beta-lactamases kept in the core genome for everyday roles under non-antibiotic stress? The mechanism labels behind the conservation result came from keyword matching on product descriptions, not the CARD Antibiotic Resistance Ontology."
hypothesis: "Core resistance genes are more often tagged with condition-specific phenotypes under non-antibiotic stresses (metals, salt, nutrient limitation) than accessory resistance genes. This holds within each mechanism class, and under both keyword-derived and ontology-derived mechanism labels, so conservation reflects a second physiological role rather than resistance."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The fitness and pangenome tables are in the catalog, but the table linking fitness-browser genes to pangenome clusters was not shown and may need to be rebuilt; the ontology remapping must be derived from product descriptions."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.specificphenotype", "kescience.fitnessbrowser.experiment", "kescience.fitnessbrowser.gene", "kbase.ke_pangenome.bakta_amr", "kbase.ke_pangenome.gene_cluster"]
findings: ["amr_fitness_cost--67395444", "amr_fitness_cost--104baecc", "amr_fitness_cost--95a8021f", "amr_pangenome_atlas--9947286c"]
conflicts: ["conflict--pangenome-conservation-fitness-decoupling--8173d997"]
papers: ["25861385", "26203082", "29769716", "12829273"]
builds_on: ["findings/amr_fitness_cost--67395444", "findings/amr_fitness_cost--104baecc", "findings/amr_fitness_cost--95a8021f", "findings/amr_pangenome_atlas--9947286c", "conflicts/conflict--pangenome-conservation-fitness-decoupling--8173d997"]
projects: ["amr_fitness_cost", "amr_pangenome_atlas"]
topics: ["laboratory-fitness-versus-natural-selection-and-gene-conservation"]
---
# Do conserved resistance genes persist because they serve non-antibiotic physiology rather than resistance?

Resistance mechanism predicts whether a resistance gene is conserved across a species, yet not the growth cost of disrupting it. Are intrinsic efflux pumps and beta-lactamases kept in the core genome for everyday roles under non-antibiotic stress? The mechanism labels behind the conservation result came from keyword matching on product descriptions, not the CARD Antibiotic Resistance Ontology.

## Hypothesis

Core resistance genes are more often tagged with condition-specific phenotypes under non-antibiotic stresses (metals, salt, nutrient limitation) than accessory resistance genes. This holds within each mechanism class, and under both keyword-derived and ontology-derived mechanism labels, so conservation reflects a second physiological role rather than resistance.

## Why it matters

If it holds, the conserved fraction of the resistome partly reflects ordinary physiology, and counts of core resistance genes overstate resistance risk. If it fails, conservation by mechanism is better explained by inheritance history and mobility, or by how the classes were labelled.

## How to test it

Link resistance-gene calls in the pangenome to mutant-fitness genes in the 25 bacteria used for the cost comparison. Take mechanism labels from keyword matching on product descriptions, as the earlier work did, and repeat with labels remapped to the CARD Antibiotic Resistance Ontology to see whether the result depends on the labelling. Split genes into core and accessory within each mechanism class (efflux, enzymatic inactivation, metal resistance). Count, per gene, the non-antibiotic experiments with a condition-specific phenotype, then compare core with accessory within each class. Repeat per organism so one species is not driving the pattern. Most of these species have few genomes (median 9), so the core label is imprecise.

## What would support or refute it

Support: core resistance genes have more non-antibiotic condition-specific phenotypes than accessory ones within every mechanism class, under both labelling schemes. Refute: no difference within classes, so the mechanism-conservation link comes from class composition alone. A pattern present only under keyword labels and absent under ontology labels is treated as unsupported.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The fitness and pangenome tables are in the catalog, but the table linking fitness-browser genes to pangenome clusters was not shown and may need to be rebuilt; the ontology remapping must be derived from product descriptions.

## Builds on

- Finding: [[findings/amr_fitness_cost--67395444|Resistance mechanism predicts conservation status though not fitness cost]] (Candidate novel)
- Finding: [[findings/amr_fitness_cost--104baecc|Fitness cost does not vary by resistance mechanism]] (Candidate novel)
- Finding: [[findings/amr_fitness_cost--95a8021f|Core and accessory AMR genes show identical fitness]] (Candidate novel)
- Finding: [[findings/amr_pangenome_atlas--9947286c|Core versus accessory status of AMR genes depends on resistance mechanism]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--pangenome-conservation-fitness-decoupling--8173d997|Do AMR genes of different pangenome prevalence carry different fitness costs?]]

## Closest published work

- [PMID 25861385](https://pubmed.ncbi.nlm.nih.gov/25861385/) The fitness costs of antibiotic resistance mutations.
- [PMID 26203082](https://pubmed.ncbi.nlm.nih.gov/26203082/) Fitness cost of antibiotic susceptibility during bacterial infection.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 12829273](https://pubmed.ncbi.nlm.nih.gov/12829273/) Efflux-mediated heavy metal resistance in prokaryotes.

PMID 25861385 and PMID 26203082 address the cost of resistance but not why resistance genes are conserved; PMID 29769716 reports condition-specific mutant phenotypes without relating them to resistance-gene conservation.
