---
type: "Research direction"
description: "Why are deep-clay Bacillota_B genomes larger than soil relatives, against the streamlining seen in other groundwater lineages, and where does the extra DNA lie?"
hypothesis: "The extra genes in deep-clay genomes are mostly accessory operons for sporulation, anaerobic respiration and mobile elements, which help cells persist in porewater that alternates between energy scarcity and bursts of supply. The size difference should remain when compared within genera."
approach: "lakehouse analysis"
readiness: "data in the lakehouse"
readiness_basis: "Genome size, isolation source and annotations for Bacillota_B are in the catalog, although the number of deep-subsurface isolates may be small."
databases: ["kbase.ke_pangenome", "kescience.bacdive"]
tables: ["kbase.ke_pangenome.gtdb_metadata", "kbase.ke_pangenome.genome", "kbase.ke_pangenome.ncbi_env", "kbase.ke_pangenome.eggnog_mapper_annotations", "kescience.bacdive.isolation", "kescience.bacdive.taxonomy"]
findings: ["bacillota_b_subsurface_accessory--0b68d03d", "bacillota_b_subsurface_accessory--b2fd7eb1", "clay_confined_subsurface--eb9811c0"]
conflicts: []
papers: ["38902796", "32252814", "40054447", "37642485"]
builds_on: ["findings/bacillota_b_subsurface_accessory--0b68d03d", "findings/bacillota_b_subsurface_accessory--b2fd7eb1", "findings/clay_confined_subsurface--eb9811c0"]
projects: ["bacillota_b_subsurface_accessory", "clay_confined_subsurface"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Do deep-clay Bacillota_B genomes grow large by keeping extra sporulation and respiration genes?

Why are deep-clay Bacillota_B genomes larger than soil relatives, against the streamlining seen in other groundwater lineages, and where does the extra DNA lie?

## Hypothesis

The extra genes in deep-clay genomes are mostly accessory operons for sporulation, anaerobic respiration and mobile elements, which help cells persist in porewater that alternates between energy scarcity and bursts of supply. The size difference should remain when compared within genera.

## Why it matters

It would show that subsurface life does not always select for small genomes, and that persistence strategy rather than nutrient poverty can set genome size.

## How to test it

Compare genome size and gene content between deep-subsurface-sourced and soil-sourced Bacillota_B genomes, matched within genus using isolation-source records from the genome and strain collections. Sort the extra genes by function, and check whether the enriched gene families found in the deep-clay isolates recur in other deep-subsurface genera. The genus-clumped anchor set must be broadened with additional deep-subsurface isolates.

## What would support or refute it

Support: the size gap persists within genera and the extra genes fall mainly in sporulation, anaerobic respiration and mobile functions that recur across subsurface genera. Refutation: the gap vanishes within genera or is driven by one or two lineages, or the extra genes are spread evenly across functions.

## Data

Approach: lakehouse analysis. Readiness: data in the lakehouse. Genome size, isolation source and annotations for Bacillota_B are in the catalog, although the number of deep-subsurface isolates may be small.

## Builds on

- Finding: [[findings/bacillota_b_subsurface_accessory--0b68d03d|Deep-clay Bacillota_B genomes are larger than soil baselines, not compact]] (Extends retrieved work)
- Finding: [[findings/bacillota_b_subsurface_accessory--b2fd7eb1|Many orthogroups are enriched in deep-clay anchors versus soil baselines]] (Insufficient literature evidence)
- Finding: [[findings/clay_confined_subsurface--eb9811c0|Wood–Ljungdahl and hydrogenase enrichment track lineage, not deep-clay habitat]] (Insufficient literature evidence)

## Closest published work

- [PMID 38902796](https://pubmed.ncbi.nlm.nih.gov/38902796/) Genome streamlining in Parcubacteria transitioning from soil to groundwater.
- [PMID 32252814](https://pubmed.ncbi.nlm.nih.gov/32252814/) Small and mighty: adaptation of superphylum Patescibacteria to groundwater environment drives their genome simplicity.
- [PMID 40054447](https://pubmed.ncbi.nlm.nih.gov/40054447/) Microbial ecosystems and ecological driving forces in the deepest ocean sediments.
- [PMID 37642485](https://pubmed.ncbi.nlm.nih.gov/37642485/) Clay-associated microbial communities and their relevance for a nuclear waste repository in the Opalinus Clay rock formation.

PMID 38902796, PMID 32252814 and PMID 40054447 link groundwater or deep habitats to smaller genomes or to larger ones through dispersal limitation, but none asks which accessory functions make deep-clay Bacillota_B larger within genera.
