---
type: "Research direction"
description: "Few geolocated environmental genomes carry metal resistance, but a few grid cells, such as the Atacama and Andes region, are hotspots. Do the hotspots track measured metal levels, or do they come from a few intensively sampled studies?"
hypothesis: "Hotspot cells reflect real geochemical enrichment, so the share of genomes with metal resistance rises with measured metal concentration across independent studies within a cell. Hotspots resting on a single study's samples fall away once sampling effort is controlled."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Genome coordinates and sample accessions exist, but joining them to study identifiers and any metal measurements is a new, sizeable join; whether hotspots survive correction for sampling effort has not been tested."
collections: ["kbase-ke-pangenome", "nmdc-ncbi-biosamples", "nmdc-arkin"]
findings: ["metal_resistance_global_biogeography--181dc531", "metal_resistance_global_biogeography--a8d92f5f", "metal_resistance_global_biogeography--2ac1d00b", "amr_environmental_resistome--0cf37cb9"]
conflicts: ["conflict--environmental-resistome--9415d508"]
papers: ["29715297", "38004830", "41845521", "30502597"]
builds_on: ["findings/metal_resistance_global_biogeography--181dc531", "findings/metal_resistance_global_biogeography--a8d92f5f", "findings/metal_resistance_global_biogeography--2ac1d00b", "findings/amr_environmental_resistome--0cf37cb9", "conflicts/conflict--environmental-resistome--9415d508"]
projects: ["amr_environmental_resistome", "bacdive_metal_validation", "metal_cross_resistance", "metal_resistance_global_biogeography", "microbeatlas_metal_ecology"]
topics: ["resistance-defense-systems-and-mobile-elements"]
---
# Do metal-resistance hotspots in environmental genomes follow local metal geochemistry or sampling clusters?

Few geolocated environmental genomes carry metal resistance, but a few grid cells, such as the Atacama and Andes region, are hotspots. Do the hotspots track measured metal levels, or do they come from a few intensively sampled studies?

## Hypothesis

Hotspot cells reflect real geochemical enrichment, so the share of genomes with metal resistance rises with measured metal concentration across independent studies within a cell. Hotspots resting on a single study's samples fall away once sampling effort is controlled.

## Why it matters

If hotspots follow geochemistry, genome-based maps of metal resistance could serve as proxies for contamination or natural metal load. If they are sampling artefacts, the apparent soil-over-marine contrast in genome prevalence needs to be rebuilt before anyone interprets it ecologically.

## How to test it

Use the share of genomes carrying at least one metal-resistance type (2.8% of 22,356 genomes with coordinates; 21.8% in the Atacama/Andean hotspot cell of 101 genomes; 11 hotspot cells and 3 coldspot cells overall), not metal resistance as a share of a species' resistance genes (45% aquatic, 44% soil, 6% human gut). Using the Pangenome Collection and NMDC BioSamples, group genomes in each hotspot cell by sampling study and count independent studies. Where NMDC Multi-omics or BioSamples hold metal measurements near the same coordinates, relate prevalence to measured metal at matched sites. Compare hotspot with non-hotspot cells of similar genome count, with study as a grouping term.

## What would support or refute it

Support: several independent studies in a hotspot cell show raised prevalence, and prevalence rises with the matching measured metal. Refutation: prevalence is driven by one study, or does not rise with measured metal once study is accounted for.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Genome coordinates and sample accessions exist, but joining them to study identifiers and any metal measurements is a new, sizeable join; whether hotspots survive correction for sampling effort has not been tested.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/nmdc-ncbi-biosamples|NMDC BioSamples]]
- Collection: [[data/nmdc-arkin|NMDC Multi-omics]]

## Builds on

- Finding: [[findings/metal_resistance_global_biogeography--181dc531|Atacama/Andean Chile is the strongest metal-resistance hotspot]] (Insufficient literature evidence)
- Finding: [[findings/metal_resistance_global_biogeography--a8d92f5f|Metal resistance clusters in a few significant grid-cell hotspots]] (Insufficient literature evidence)
- Finding: [[findings/metal_resistance_global_biogeography--2ac1d00b|Metal resistance is rare among geolocated environmental MAGs]] (Insufficient literature evidence)
- Finding: [[findings/amr_environmental_resistome--0cf37cb9|Metal resistance dominates soil and aquatic AMR but is rare in gut]] (Extends retrieved work)
- Conflict: [[conflicts/conflict--environmental-resistome--9415d508|Do metal-tolerance scores track metal-associated isolation ecology?]]

## Closest published work

- [PMID 29715297](https://pubmed.ncbi.nlm.nih.gov/29715297/) Effect of the natural arsenic gradient on the diversity and arsenic resistance of bacterial communities of the sediments of Camarones River (Atacama Desert, Chile).
- [PMID 38004830](https://pubmed.ncbi.nlm.nih.gov/38004830/) Diversity, Taxonomic Novelty, and Encoded Functions of Salar de Ascotán Microbiota, as Revealed by Metagenome-Assembled Genomes.
- [PMID 41845521](https://pubmed.ncbi.nlm.nih.gov/41845521/) Microbial diversity, metabolic specialization, and genomic novelty across polyextreme saline lakes of the Central Dry Andes.
- [PMID 30502597](https://pubmed.ncbi.nlm.nih.gov/30502597/) Plastics in the marine environment are reservoirs for antibiotic and metal resistance genes.

PMID 29715297 links arsenic resistance to a natural arsenic gradient in one Atacama river; PMIDs 38004830 and 41845521 describe genomes from single saline-lake and salt-flat sites. None tests whether a global metal-resistance hotspot survives control for study clustering.
