---
type: "Research direction"
description: "Is the split of genera between groundwater and sediment in the same wells explained by what they do with iron, nitrate and methane, rather than by sampling date?"
hypothesis: "Genera enriched in groundwater (Rhodanobacter, Gallionella, Sideroxydans) carry denitrification and iron-oxidation genes, while sediment-enriched genera (Anaeromyxobacter, Arcobacter, Ca. Methanoperedens) carry iron-reduction, sulfur and methane-oxidation genes, at the same sites."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Genomes for the named genera appear in the catalog, but matched same-date metagenomes of sediment and groundwater are not shown and would need to be generated."
databases: ["enigma.coral", "kbase.ke_pangenome", "kbase.nmdc_mags"]
tables: ["kbase.nmdc_mags.mag_catalog", "kbase.ke_pangenome.genome", "kbase.ke_pangenome.eggnog_mapper_annotations", "kbase.ke_pangenome.gene_cluster", "enigma.coral.sdt_sample", "enigma.coral.sdt_community"]
findings: ["enigma_sso_asv_ecology--51556105"]
conflicts: []
papers: ["22179233", "38391193", "22140175"]
builds_on: ["findings/enigma_sso_asv_ecology--51556105"]
projects: ["enigma_sso_asv_ecology"]
topics: ["subsurface-and-soil-community-ecology"]
---
# Do groundwater-enriched and sediment-enriched genera differ in iron and nitrogen metabolism?

Is the split of genera between groundwater and sediment in the same wells explained by what they do with iron, nitrate and methane, rather than by sampling date?

## Hypothesis

Genera enriched in groundwater (Rhodanobacter, Gallionella, Sideroxydans) carry denitrification and iron-oxidation genes, while sediment-enriched genera (Anaeromyxobacter, Arcobacter, Ca. Methanoperedens) carry iron-reduction, sulfur and methane-oxidation genes, at the same sites.

## Why it matters

Sediment and groundwater were sampled about 18 months apart, so the split might simply reflect time. A functional pattern that holds in matched metagenomes would show that the two habitats run different parts of the nitrogen and iron cycle.

## How to test it

Pull Rhodanobacter and Anaeromyxobacter genomes from the metagenome-assembled genome catalog and the species pangenome collection, and score marker genes for each pathway from the annotation tables. Then run shotgun metagenomes on paired sediment cores and groundwater from the same wells, collected on the same dates, and compare gene content with the 16S-based assignments.

## What would support or refute it

Support: the marker genes sort by habitat as predicted in matched samples. Refute: gene capacity does not differ between habitats, or the split disappears when both are sampled on the same dates, which would show a time effect.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Genomes for the named genera appear in the catalog, but matched same-date metagenomes of sediment and groundwater are not shown and would need to be generated.

## Builds on

- Finding: [[findings/enigma_sso_asv_ecology--51556105|Groundwater and sediment host distinct taxa within the same wells]] (Extends retrieved work)

## Closest published work

- [PMID 22179233](https://pubmed.ncbi.nlm.nih.gov/22179233/) Denitrifying bacteria from the genus Rhodanobacter dominate bacterial communities in the highly contaminated subsurface of a nuclear legacy waste site.
- [PMID 38391193](https://pubmed.ncbi.nlm.nih.gov/38391193/) Metal-oxide precipitation influences microbiome structure in hyporheic zones receiving acid rock drainage.
- [PMID 22140175](https://pubmed.ncbi.nlm.nih.gov/22140175/) Rhodanobacter denitrificans sp. nov., isolated from nitrate-rich zones of a contaminated aquifer.

PMID 22179233 shows Rhodanobacter dominating in both groundwater and sediment but not a paired habitat comparison, and 38391193 links metal oxides to microbiome structure in another system; neither tests gene capacity by habitat.
