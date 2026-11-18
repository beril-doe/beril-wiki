---
type: "Research direction"
description: "A few places, such as the Atacama region of Chile, carry far more metal-resistant genomes than other regions, and only a handful of grid cells stand out. Do these hotspots lie over naturally metal-rich geology, or near industrial metal release?"
hypothesis: "Hotspot cells lie closer to natural ore deposits and metal-rich rock than to industrial metal-release sites. Local geology therefore predicts metal-resistance prevalence in a cell better than industrial proximity does."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Genome coordinates, resistance calls, and geology and release layers appear in the catalog, but the geospatial joins and the grid analysis would have to be built."
databases: ["arkinlab.envdbs", "kbase.ke_pangenome", "kescience.mgnify"]
tables: ["kbase.ke_pangenome.alphaearth_embeddings_all_years", "kbase.ke_pangenome.bakta_amr", "kbase.ke_pangenome.genome", "arkinlab.envdbs.cmmi_ores", "arkinlab.envdbs.epa_tri_metals", "kescience.mgnify.gene_amr", "kescience.mgnify.genome"]
findings: ["metal_resistance_global_biogeography--181dc531", "metal_resistance_global_biogeography--a8d92f5f"]
conflicts: ["conflict--environmental-resistome--9415d508"]
papers: ["30502597", "29715297", "38004830", "36973286"]
builds_on: ["findings/metal_resistance_global_biogeography--181dc531", "findings/metal_resistance_global_biogeography--a8d92f5f", "conflicts/conflict--environmental-resistome--9415d508"]
projects: ["bacdive_metal_validation", "metal_cross_resistance", "metal_resistance_global_biogeography", "microbeatlas_metal_ecology"]
topics: ["resistance-defense-systems-and-mobile-elements"]
---
# Are metal-resistance hotspots in environmental genomes set by local rock chemistry rather than pollution?

A few places, such as the Atacama region of Chile, carry far more metal-resistant genomes than other regions, and only a handful of grid cells stand out. Do these hotspots lie over naturally metal-rich geology, or near industrial metal release?

## Hypothesis

Hotspot cells lie closer to natural ore deposits and metal-rich rock than to industrial metal-release sites. Local geology therefore predicts metal-resistance prevalence in a cell better than industrial proximity does.

## Why it matters

It would show whether environmental metal resistance mostly records long-term natural selection or recent human contamination. That decides how these genes can be used as pollution indicators.

## How to test it

Place genomes that carry coordinates on a grid and flag the cells with elevated metal-resistance prevalence. For each cell, take the distance to mapped ore deposits and the metal concentrations of local rock. Compare these with the distance to industrial metal-release facilities. Fit a model in which geology and industrial proximity compete to explain prevalence, with sampling effort included. Check whether the Atacama and United States clusters come from several independent studies or from one expedition.

## What would support or refute it

Support: geology predicts the hotspots and industrial proximity adds little. Refutation: industrial proximity predicts prevalence better, or neither explains it and the hotspots trace to single-study sampling.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Genome coordinates, resistance calls, and geology and release layers appear in the catalog, but the geospatial joins and the grid analysis would have to be built.

## Builds on

- Finding: [[findings/metal_resistance_global_biogeography--181dc531|Atacama/Andean Chile is the strongest metal-resistance hotspot]] (Insufficient literature evidence)
- Finding: [[findings/metal_resistance_global_biogeography--a8d92f5f|Metal resistance clusters in a few significant grid-cell hotspots]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--environmental-resistome--9415d508|Do metal-tolerance scores track metal-associated isolation ecology?]]

## Closest published work

- [PMID 30502597](https://pubmed.ncbi.nlm.nih.gov/30502597/) Plastics in the marine environment are reservoirs for antibiotic and metal resistance genes.
- [PMID 29715297](https://pubmed.ncbi.nlm.nih.gov/29715297/) Effect of the natural arsenic gradient on the diversity and arsenic resistance of bacterial communities of the sediments of Camarones River (Atacama Desert, Chile).
- [PMID 38004830](https://pubmed.ncbi.nlm.nih.gov/38004830/) Diversity, Taxonomic Novelty, and Encoded Functions of Salar de Ascotán Microbiota, as Revealed by Metagenome-Assembled Genomes.
- [PMID 36973286](https://pubmed.ncbi.nlm.nih.gov/36973286/) Soil contamination in nearby natural areas mirrors that in urban greenspaces worldwide.

PMID 30502597 and PMID 36973286 describe resistance genes in marine plastic and contaminants in soil, and PMID 29715297 describes an arsenic gradient in one Atacama river. None compares natural geology with industrial release as the explanation for hotspots.
