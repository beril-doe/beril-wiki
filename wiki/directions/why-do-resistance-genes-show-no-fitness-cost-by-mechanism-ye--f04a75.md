---
type: "Research direction"
description: "If mechanism does not predict lab fitness cost, what explains the strong mechanism differences in core versus accessory status?"
hypothesis: "Mechanism differences in conservation reflect origin (intrinsic chromosomal versus mobile acquisition), not cost, so accessory efflux and enzymatic genes sit near mobile elements and core ones sit in the chromosomal backbone."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "AMR and cluster tables are in the catalog; linking to fitness and neighbours needs new joins."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kbase.ke_pangenome.bakta_amr", "kbase.ke_pangenome.gene_cluster", "kescience.fitnessbrowser.gene"]
findings: ["amr_fitness_cost--0371e1c6", "amr_fitness_cost--67395444", "amr_fitness_cost--6ff13010", "amr_pangenome_atlas--b397cdb4"]
conflicts: ["conflict--intrinsic-versus-acquired-resistance-gene-conservation--ff874151"]
papers: ["25861385", "20208551", "23499305", "26203082", "29769716"]
builds_on: ["findings/amr_fitness_cost--0371e1c6", "findings/amr_fitness_cost--67395444", "findings/amr_fitness_cost--6ff13010", "findings/amr_pangenome_atlas--b397cdb4", "conflicts/conflict--intrinsic-versus-acquired-resistance-gene-conservation--ff874151"]
projects: ["amr_fitness_cost", "amr_pangenome_atlas", "amr_strain_variation"]
topics: ["resistance-defense-systems-and-mobile-elements"]
---
# Why do resistance genes show no fitness cost by mechanism yet differ in conservation by mechanism?

If mechanism does not predict lab fitness cost, what explains the strong mechanism differences in core versus accessory status?

## Hypothesis

Mechanism differences in conservation reflect origin (intrinsic chromosomal versus mobile acquisition), not cost, so accessory efflux and enzymatic genes sit near mobile elements and core ones sit in the chromosomal backbone.

## Why it matters

It would show that selection or mobility, not lab cost, shapes resistome structure, and that intrinsic and acquired labels can be measured.

## How to test it

For AMR clusters in Fitness Browser species, classify mechanism, core or accessory status, and distance to mobile genes. Fit a joint model of core status on mechanism, mobile proximity and phylum. Check whether cost differs between recent accessory and long-resident core genes, restricting to species with over 20 genomes.

## What would support or refute it

Support: mobile proximity absorbs the mechanism effect on conservation while cost stays flat. Refute: mechanism still predicts conservation after proximity and phylum are included, or cost differs by origin.

## Data

Approach: lakehouse analysis. Readiness: needs compute. AMR and cluster tables are in the catalog; linking to fitness and neighbours needs new joins.

## Builds on

- Finding: [[findings/amr_fitness_cost--0371e1c6|Resistance mechanism does not explain AMR fitness cost differences]] (Candidate novel)
- Finding: [[findings/amr_fitness_cost--67395444|Mechanism predicts pangenome conservation of AMR genes]] (Candidate novel)
- Finding: [[findings/amr_fitness_cost--6ff13010|AMR knockouts consistently fitter than background across organisms]] (Candidate novel)
- Finding: [[findings/amr_pangenome_atlas--b397cdb4|AMR genes carry slightly less lab fitness cost than other genes]] (Candidate novel)
- Conflict: [[conflicts/conflict--intrinsic-versus-acquired-resistance-gene-conservation--ff874151|Intrinsic Versus Acquired Resistance Genes: Does Conservation Track Lineage?]]

## Closest published work

- [PMID 25861385](https://pubmed.ncbi.nlm.nih.gov/25861385/) The fitness costs of antibiotic resistance mutations.
- [PMID 20208551](https://pubmed.ncbi.nlm.nih.gov/20208551/) Antibiotic resistance and its cost: is it possible to reverse resistance?
- [PMID 23499305](https://pubmed.ncbi.nlm.nih.gov/23499305/) Intrinsic antibiotic resistance: mechanisms, origins, challenges and solutions.
- [PMID 26203082](https://pubmed.ncbi.nlm.nih.gov/26203082/) Fitness cost of antibiotic susceptibility during bacterial infection.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.

25861385 and 20208551 cover costs of resistance; this asks why conservation, not cost, separates mechanisms.
