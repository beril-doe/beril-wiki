---
type: "Research direction"
description: "Gene modules defined by correlated fitness show a larger co-inheritance signal than gene pairs, with the highest values for accessory modules. That module result is fragile: the accessory-versus-core difference was only borderline, accessory modules were about 5% of the mapped set, and in one organism no module qualified. Do accessory modules, where they exist, travel together as physical units?"
hypothesis: "The small set of accessory fitness modules is enriched for genes that sit close together in genomes and near mobile-element markers, which would explain their co-occurrence across strains. Core modules and cofit pairs outside modules lack this clustering. Failure of this prediction would mean the module signal reflects shared ancestry or prevalence."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Module memberships, gene coordinates and pangenome presence/absence are in the lakehouse; the work is coordinate-based distance computation and matched nulls, limited by the small number of accessory modules."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["cofitness_coinheritance--0fab94f0", "cofitness_coinheritance--67c8c90f", "module_conservation--d13bfcb2"]
conflicts: ["conflict--cofitness-network-architecture--52cc7c49", "conflict--cofitness-network-architecture--f152c7da"]
papers: ["34499026", "32100706", "40304385", "38948139"]
builds_on: ["findings/cofitness_coinheritance--0fab94f0", "findings/cofitness_coinheritance--67c8c90f", "findings/module_conservation--d13bfcb2", "conflicts/conflict--cofitness-network-architecture--52cc7c49", "conflicts/conflict--cofitness-network-architecture--f152c7da"]
projects: ["cofitness_coinheritance", "metal_cross_resistance", "module_conservation"]
topics: ["gene-fitness-landscapes-and-cofitness-modules"]
---
# Could the weak co-inheritance of accessory fitness modules reflect physical co-transfer units?

Gene modules defined by correlated fitness show a larger co-inheritance signal than gene pairs, with the highest values for accessory modules. That module result is fragile: the accessory-versus-core difference was only borderline, accessory modules were about 5% of the mapped set, and in one organism no module qualified. Do accessory modules, where they exist, travel together as physical units?

## Hypothesis

The small set of accessory fitness modules is enriched for genes that sit close together in genomes and near mobile-element markers, which would explain their co-occurrence across strains. Core modules and cofit pairs outside modules lack this clustering. Failure of this prediction would mean the module signal reflects shared ancestry or prevalence.

## Why it matters

It would separate real co-transfer from inherited relatedness for the one class of modules where co-inheritance looks strongest, and show whether fitness modules can be evolutionary units as well as regulatory ones.

## How to test it

Take the accessory module families (fewer than half core genes) and prevalence-matched core modules across the Fitness Browser organisms. Take gene coordinates from the pangenome genomes and measure distance between module members and closeness to transposase, integrase and phage genes. Compare with prevalence-matched random accessory gene sets and with cofit pairs outside modules. Repeat within the closest-related genomes only, to check the result is not driven by ancestry. Report per organism, because the per-organism module counts do not sum to the headline totals and the accessory class is small.

## What would support or refute it

Support: accessory module members cluster physically and near mobile markers more than prevalence-matched random sets, and the pattern holds in near-clonal strains. Refute: module members are scattered like random accessory genes, so the co-inheritance signal reflects ancestry or prevalence. If too few accessory modules are testable in any organism, the question stays open rather than refuted.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Module memberships, gene coordinates and pangenome presence/absence are in the lakehouse; the work is coordinate-based distance computation and matched nulls, limited by the small number of accessory modules.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/cofitness_coinheritance--0fab94f0|Module-level co-occurrence exceeds null, but few modules survive FDR correction]] (Extends retrieved work)
- Finding: [[findings/cofitness_coinheritance--67c8c90f|Pairwise co-fitness shows only weak positive co-occurrence signal across organisms]] (Extends retrieved work)
- Finding: [[findings/module_conservation--d13bfcb2|Some module families are accessory-dominated, possibly mobile or niche-specific]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--cofitness-network-architecture--52cc7c49|Do Cofitness Co-inheritance Signals Generalize Better at the Module Level Than for Gene Pairs?]]
- Conflict: [[conflicts/conflict--cofitness-network-architecture--f152c7da|Functional Coupling or Shared Ancestry? Cross-Organism Signals in Fitness Networks]]

## Closest published work

- [PMID 34499026](https://pubmed.ncbi.nlm.nih.gov/34499026/) Gene-gene relationships in an Escherichia coli accessory genome are linked to function and mobility.
- [PMID 32100706](https://pubmed.ncbi.nlm.nih.gov/32100706/) Coinfinder: detecting significant associations and dissociations in pangenomes.
- [PMID 40304385](https://pubmed.ncbi.nlm.nih.gov/40304385/) Heterogeneity in recombination rates and accessory gene co-occurrence distinguish Pseudomonas aeruginosa phylogroups.
- [PMID 38948139](https://pubmed.ncbi.nlm.nih.gov/38948139/) Cofitness network connectivity determines a fuzzy essential zone in open bacterial pangenome.

PMID 34499026 and PMID 32100706 show accessory genes co-occur beyond chance in pangenomes; this direction tests whether fitness-defined accessory modules are physically linked mobile units, which those papers did not examine.
