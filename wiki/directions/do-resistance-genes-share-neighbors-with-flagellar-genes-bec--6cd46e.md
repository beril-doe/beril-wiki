---
type: "Research direction"
description: "Resistance genes keep company with flagellar genes in fitness-correlation neighborhoods in several organisms. Could both be controlled by growth on surfaces and in structured habitats, which shaken liquid culture never tests?"
hypothesis: "Resistance-gene knockouts show fitness effects in surface and motility conditions, and these effects correlate with flagellar-gene effects. In shaken liquid culture the same genes appear only as shared dispensables."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "The experiment table lists soft-agar motility assays, but fitness values and correlation tables lie outside the sample shown and the resistance-gene link needs a join."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.experiment", "kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.organism", "kbase.ke_pangenome.bakta_amr"]
findings: ["amr_cofitness_networks--284c5695", "amr_cofitness_networks--9d334076"]
conflicts: ["conflict--antimicrobial-resistance-fitness-cost--cded18a3"]
papers: ["29769716", "23499305", "38323821"]
builds_on: ["findings/amr_cofitness_networks--284c5695", "findings/amr_cofitness_networks--9d334076", "conflicts/conflict--antimicrobial-resistance-fitness-cost--cded18a3"]
projects: ["amr_cofitness_networks", "amr_strain_variation"]
topics: ["resistance-defense-systems-and-mobile-elements"]
---
# Do resistance genes share neighbors with flagellar genes because both are tied to surface life?

Resistance genes keep company with flagellar genes in fitness-correlation neighborhoods in several organisms. Could both be controlled by growth on surfaces and in structured habitats, which shaken liquid culture never tests?

## Hypothesis

Resistance-gene knockouts show fitness effects in surface and motility conditions, and these effects correlate with flagellar-gene effects. In shaken liquid culture the same genes appear only as shared dispensables.

## Why it matters

It would show that the link reflects shared ecology rather than a laboratory artifact. It would also suggest that resistance genes belong to a surface-colonization program.

## How to test it

In fitness-collection organisms with soft-agar motility, plate or biofilm experiments, extract the fitness of resistance genes and flagellar genes. Compare their correlation in surface conditions with that in shaken liquid conditions, against random genes of similar average fitness. In one flagellated organism, such as Pseudomonas fluorescens, run knockout competition in soft agar and in liquid.

## What would support or refute it

Support: resistance and flagellar genes covary more strongly in surface conditions than in liquid, beyond random genes. Refutation: the covariation is equal across conditions or matches random dispensable genes.

## Data

Approach: analysis then experiment. Readiness: needs compute. The experiment table lists soft-agar motility assays, but fitness values and correlation tables lie outside the sample shown and the resistance-gene link needs a join.

## Builds on

- Finding: [[findings/amr_cofitness_networks--284c5695|Flagellum-dependent motility GO term enriched across several organisms]] (Insufficient literature evidence)
- Finding: [[findings/amr_cofitness_networks--9d334076|InterProScan GO annotations reveal AMR cofitness enrichment across organisms]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--antimicrobial-resistance-fitness-cost--cded18a3|Does genomic co-inheritance of resistance genes measure the same network architecture as cofitness?]]

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 23499305](https://pubmed.ncbi.nlm.nih.gov/23499305/) Intrinsic antibiotic resistance: mechanisms, origins, challenges and solutions.
- [PMID 38323821](https://pubmed.ncbi.nlm.nih.gov/38323821/) Machine learning analysis of RB-TnSeq fitness data predicts functional gene modules in Pseudomonas putida KT2440.

PMID 29769716 and PMID 38323821 describe fitness-based gene modules in several bacteria. Neither asks whether resistance genes cluster with flagellar genes because of surface conditions.
