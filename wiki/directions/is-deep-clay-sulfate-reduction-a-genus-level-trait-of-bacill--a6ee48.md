---
type: "Research direction"
description: "Within Bacillota_B, does carriage of dissimilatory sulfate reduction mark particular genera, or does it mark deep-clay habitat?"
hypothesis: "Sulfate-reduction carriage in deep-clay Bacillota_B isolates reflects a few genera such as Desulfosporosinus. Deep-clay habitat adds no gene content beyond what those genera already carry."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The genomes, taxonomy and annotations appear in the catalog; the genus-level comparison has not been run."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.genome", "kbase.ke_pangenome.gtdb_taxonomy_r214v1", "kbase.ke_pangenome.eggnog_mapper_annotations", "kbase.ke_pangenome.gene_cluster"]
findings: ["clay_confined_subsurface--ef6ee9c9", "clay_confined_subsurface--eb9811c0", "clay_confined_subsurface--7edbee75"]
conflicts: []
papers: ["27739431", "37642485", "31852805", "33824425"]
builds_on: ["findings/clay_confined_subsurface--ef6ee9c9", "findings/clay_confined_subsurface--eb9811c0", "findings/clay_confined_subsurface--7edbee75"]
projects: ["clay_confined_subsurface"]
topics: ["subsurface-and-soil-community-ecology"]
---
# Is deep-clay sulfate reduction a genus-level trait of Bacillota_B or an adaptation to deep clay?

Within Bacillota_B, does carriage of dissimilatory sulfate reduction mark particular genera, or does it mark deep-clay habitat?

## Hypothesis

Sulfate-reduction carriage in deep-clay Bacillota_B isolates reflects a few genera such as Desulfosporosinus. Deep-clay habitat adds no gene content beyond what those genera already carry.

## Why it matters

It would separate lineage effects from habitat selection in subsurface genomics. It would also show whether the deep-clay sulfate-reduction pattern is more than a sampling effect.

## How to test it

Split the Bacillota_B genomes into genera using the GTDB taxonomy in the pangenome tables. Compare dsrAB-aprAB-sat carriage between the 5 deep-clay isolates and soil-baseline isolates within each genus. Use eggNOG annotations to search for accessory genes unique to deep clay. Re-check the iron-reduction contrast with the corrected markers.

## What would support or refute it

Support: carriage matches genus identity and no deep-clay accessory genes appear. Refute: deep-clay isolates differ from same-genus baseline isolates, or deep-clay-specific accessory genes appear. With only 5 deep genomes, only large effects are detectable.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The genomes, taxonomy and annotations appear in the catalog; the genus-level comparison has not been run.

## Builds on

- Finding: [[findings/clay_confined_subsurface--ef6ee9c9|Only sulfate reduction survives phylogenetic control within Bacillota_B]] (Candidate novel)
- Finding: [[findings/clay_confined_subsurface--eb9811c0|Wood–Ljungdahl carriage tracks Bacillota_B lineage, not deep-clay habitat]] (Candidate novel)
- Finding: [[findings/clay_confined_subsurface--7edbee75|Corrected iron-reduction comparison shows no significant cohort differences]] (Candidate novel)

## Closest published work

- [PMID 27739431](https://pubmed.ncbi.nlm.nih.gov/27739431/) Reconstructing a hydrogen-driven microbial metabolic network in Opalinus Clay rock.
- [PMID 37642485](https://pubmed.ncbi.nlm.nih.gov/37642485/) Clay-associated microbial communities and their relevance for a nuclear waste repository in the Opalinus Clay rock formation.
- [PMID 31852805](https://pubmed.ncbi.nlm.nih.gov/31852805/) Stability of Microbial Community Profiles Associated with Compacted Bentonite from the Grimsel Underground Research Laboratory.
- [PMID 33824425](https://pubmed.ncbi.nlm.nih.gov/33824425/) Evolutionary stasis of a deep subsurface microbial lineage.

The Opalinus Clay and bentonite papers (27739431, 31852805, 37642485) describe sulfate reducers but do not control for phylogeny in a genome comparison.
