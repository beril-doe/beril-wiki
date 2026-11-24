---
type: "Dataset"
description: "NSF open-ocean sample collection held as planetmicrobe_planetmicrobe."
sources: ["summaries/berdl_data_atlas__REPORT.md", "summaries/enigma_carbon_census_1__REPORT.md", "summaries/pitfalls.md"]
aliases: ["planetmicrobe", "planetmicrobe_planetmicrobe"]
---
# Planet Microbe

Planet Microbe (also planetmicrobe, planetmicrobe_planetmicrobe) is the National Science Foundation open-ocean sample collection held in the KBase Data Lakehouse. It is small in table count but unique in sample provenance, and one project has used it as a marine contrast. [src: berdl_data_atlas]

## Key facts

- NSF (Planet Microbe) contributes 3.5% of the KBase Data Lakehouse tables. [src: berdl_data_atlas]
- The inventory lists 2,371 Planet Microbe samples. [src: berdl_data_atlas]
- The `sample` table in `planetmicrobe_planetmicrobe` supplies these samples. [src: berdl_data_atlas]
- The data atlas report proposes Planet Microbe, DOE-FE NETL and DOI USGS as external validation sets for DOE-BER-anchored analyses, because their sample types (open ocean, produced waters) are unique. [src: berdl_data_atlas] See [[concepts/funding-agency-and-topic-coverage-of-a-shared-data-platform]] and [[summaries/berdl_data_atlas__REPORT]].

## Use in the ENIGMA carbon census

The census used Planet Microbe taxonomy plus the run, experiment, sample, project and campaign tables for a global marine genus abundance contrast. [src: enigma_carbon_census_1] It reports 302 Planet Microbe runs, with 68 of 68 genera positive. [src: enigma_carbon_census_1]

The marine atlas is mostly a negative biome contrast. Terrestrial and freshwater genera sit at ~1e-3 to 1e-4 in open ocean. [src: enigma_carbon_census_1] Genuine marine members are the exception. Alteromonas has abundance 0.048 in 240/302 runs, with prevalence 0.79. [src: enigma_carbon_census_1] Cosmopolitan Pseudomonas has abundance 0.011. [src: enigma_carbon_census_1] Sphingomonas has abundance 0.0063. [src: enigma_carbon_census_1]

The census itself calls the marine arm small and gene-blind. It has 302 runs with presence/abundance only, so it suits only a negative biome contrast. [src: enigma_carbon_census_1] See [[summaries/enigma_carbon_census_1__REPORT]] and [[concepts/biome-abundance-atlases-as-a-proxy-for-catabolic-potential]].

## Pitfalls

### Species-level taxonomy

Planet Microbe `taxonomy.name`, like NMDC covstats, is species-level. Genus-level abundance claims need species-to-genus aggregation first. [src: enigma_carbon_census_1] Any genus-level analysis over `run_to_taxonomy` or `covstats_taxonomy_rollup` needs this rollup. [src: enigma_carbon_census_1, pitfalls]

Filtering on a bare genus name matches only near-zero rows that carry the genus rank as a literal name. It does not sum the species in that genus. [src: pitfalls, enigma_carbon_census_1] This bug first made the census show 0/68 marine genera present in Planet Microbe. The genera were not absent. The filter matched only genus-rank reference rows. [src: pitfalls, enigma_carbon_census_1] See [[summaries/pitfalls]] and [[entities/nmdc-integrated-collections]].

### Empty tables and raw mirror

In `planetmicrobe_planetmicrobe` and `planetmicrobe_planetmicrobe_raw`, the `project` and `library` tables are empty (count=0). Joins through them return nothing. [src: pitfalls] The `_raw` database mirrors the curated one structurally, so each query should pick one explicitly. [src: pitfalls]
