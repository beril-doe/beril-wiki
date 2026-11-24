---
type: "Research direction"
description: "Are the geographic hotspots of metal resistance among environmental MAGs (metagenome-assembled genomes), such as Atacama/Andean Chile, real regional signals or the output of single expeditions?"
hypothesis: "Most top hotspots, including Atacama, are dominated by one or two bioprojects, and after weighting by project the regional enrichment falls to the level of nearby regions."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The catalog shows coordinates, bioproject fields and environment attributes; the table holding MAG-level metal-resistance calls was not shown in the catalog and would need to be located or computed."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.alphaearth_embeddings_all_years", "kbase.ke_pangenome.ncbi_env"]
findings: ["metal_resistance_global_biogeography--181dc531", "metal_resistance_global_biogeography--44ee4a3c"]
conflicts: []
papers: ["38886447", "36473884"]
builds_on: ["findings/metal_resistance_global_biogeography--181dc531", "findings/metal_resistance_global_biogeography--44ee4a3c"]
projects: ["metal_resistance_global_biogeography"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Is the Atacama metal-resistance hotspot a property of the place or of a single study?

Are the geographic hotspots of metal resistance among environmental MAGs (metagenome-assembled genomes), such as Atacama/Andean Chile, real regional signals or the output of single expeditions?

## Hypothesis

Most top hotspots, including Atacama, are dominated by one or two bioprojects, and after weighting by project the regional enrichment falls to the level of nearby regions.

## Why it matters

Marine depletion and soil enrichment of metal resistance are used to infer where metals shape communities. If hotspots are study artefacts, biogeographic claims need project-aware analysis and targeted resampling.

## How to test it

Take MAGs with coordinates and link them to bioproject and environment metadata through the pangenome embedding table and NCBI environment attributes. For each hotspot cell count distinct bioprojects, then re-estimate enrichment with genomes grouped by project and with leave-one-project-out resampling. Compare Atacama (21.8% prevalence, n=101 MAGs) with matched cells.

## What would support or refute it

Support: leave-one-project-out removes or halves hotspot enrichment. Refute: enrichment stays across several independent projects in the cell.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The catalog shows coordinates, bioproject fields and environment attributes; the table holding MAG-level metal-resistance calls was not shown in the catalog and would need to be located or computed.

## Builds on

- Finding: [[findings/metal_resistance_global_biogeography--181dc531|Atacama/Andean Chile is the top metal-resistance hotspot]] (Candidate novel)
- Finding: [[findings/metal_resistance_global_biogeography--44ee4a3c|Marine MAGs are depleted for metal resistance]] (Candidate novel)

## Closest published work

- [PMID 38886447](https://pubmed.ncbi.nlm.nih.gov/38886447/) Organic fertilization co-selects genetically linked antibiotic and metal(loid) resistance genes in global soil microbiome.
- [PMID 36473884](https://pubmed.ncbi.nlm.nih.gov/36473884/) Genome-resolved insight into the reservoir of antibiotic resistance genes in aquatic microbial community.

38886447 and 36473884 report metal resistance genes in soil and aquatic genomes; neither tests whether regional hotspots persist after controlling for study.
