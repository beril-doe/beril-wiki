---
type: "Research direction"
description: "Does the strong link between genome size and prophage-module content arise because larger genomes retain domesticated, species-wide prophage-derived genes, rather than carrying more recently acquired intact prophages?"
hypothesis: "In larger genomes, the extra prophage-associated gene clusters are mostly core within their species, which suggests domesticated remnants, whereas in smaller genomes they are mostly accessory or single-genome."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The pangenome, annotation and genome-size tables are in the catalog; dedicated prophage calls on a subset would have to be generated."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.eggnog_mapper_annotations", "kbase.ke_pangenome.pangenome", "kbase.ke_pangenome.gtdb_metadata"]
findings: ["prophage_ecology--9f2125cc", "prophage_ecology--d880eadf"]
conflicts: []
papers: ["25092302", "28692019", "29416123"]
builds_on: ["findings/prophage_ecology--9f2125cc", "findings/prophage_ecology--d880eadf"]
projects: ["prophage_ecology"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Are large bacterial genomes rich in prophage modules because those modules become domesticated?

Does the strong link between genome size and prophage-module content arise because larger genomes retain domesticated, species-wide prophage-derived genes, rather than carrying more recently acquired intact prophages?

## Hypothesis

In larger genomes, the extra prophage-associated gene clusters are mostly core within their species, which suggests domesticated remnants, whereas in smaller genomes they are mostly accessory or single-genome.

## Why it matters

Genome size predicted prophage-module composition far more than environment or family-level phylogeny. The annotation-based method counts domesticated remnants as well as intact prophages, so it cannot say what the size effect means. Separating domestication from active carriage would show whether genome size reflects genome-wide tolerance of mobile DNA or long-term retention of useful phage-derived functions.

## How to test it

For species in the pangenome, tally prophage-associated gene clusters by module and by whether the cluster is core, accessory or single-genome in its species. Relate each class to genome size within genera, and compare with non-prophage accessory genes to see whether prophage content scales differently. In a subset, call prophages with a dedicated detector and compare intact calls with annotation-based counts.

## What would support or refute it

Support: the size-linked increase is concentrated in core prophage-derived clusters, and dedicated detection finds little more intact prophage in large genomes. Refute: the increase is in accessory or single-genome clusters and tracks intact prophage calls, favouring active carriage.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The pangenome, annotation and genome-size tables are in the catalog; dedicated prophage calls on a subset would have to be generated.

## Builds on

- Finding: [[findings/prophage_ecology--9f2125cc|Genome size dwarfs environment and phylogeny as predictor of prophage module composition]] (Insufficient literature evidence)
- Finding: [[findings/prophage_ecology--d880eadf|Prophage-associated gene clusters occur in every surveyed species, with modules varying]] (Insufficient literature evidence)

## Closest published work

- [PMID 25092302](https://pubmed.ncbi.nlm.nih.gov/25092302/) Pervasive domestication of defective prophages by bacteria.
- [PMID 28692019](https://pubmed.ncbi.nlm.nih.gov/28692019/) Bacteriophage evolution differs by host, lifestyle and genome.
- [PMID 29416123](https://pubmed.ncbi.nlm.nih.gov/29416123/) Lysogeny is prevalent and widely distributed in the murine gut microbiota.

PMID 25092302 showed that bacteria domesticate defective prophages, and PMID 28692019 related phage evolution to host and genome features; neither asks whether genome size predicts prophage-module content across the pangenome through domesticated core clusters.
