---
type: "Research direction"
description: "No lytic phage is known for Hungatella hathewayi, Flavonifractor plautii or Mediterraneibacter gnavus. Is this because phages of these hosts are mostly temperate, or because gut anaerobe phages have simply been under-sampled?"
hypothesis: "Virus sequences assigned to these hosts are mostly integrated or temperate type. Predicted lytic phages are rare even after adjusting for how many genomes exist per host."
approach: "analysis then experiment"
readiness: "unknown"
readiness_basis: "The MAG catalog lists some of these species by name; the catalog showed viral host-assignment tables but not whether they hold lifestyle calls, and MAG counts for these hosts were not shown."
databases: ["kbase.nmdc_mags", "refdata.jgi_virus"]
tables: ["kbase.nmdc_mags.mag_catalog"]
findings: ["ibd_phage_targeting--d7f80dce"]
conflicts: []
papers: ["41726920", "28130329"]
builds_on: ["findings/ibd_phage_targeting--d7f80dce"]
projects: ["ibd_phage_targeting"]
topics: ["translational-microbiome-and-phage-therapeutics"]
---
# Are the missing phages for three gut anaerobes absent because they are temperate or undersampled?

No lytic phage is known for Hungatella hathewayi, Flavonifractor plautii or Mediterraneibacter gnavus. Is this because phages of these hosts are mostly temperate, or because gut anaerobe phages have simply been under-sampled?

## Hypothesis

Virus sequences assigned to these hosts are mostly integrated or temperate type. Predicted lytic phages are rare even after adjusting for how many genomes exist per host.

## Why it matters

If the gap is biological, hybrid strategies such as enzyme inhibitors or engineered lytic-locked phage are needed. If it is under-sampling, targeted isolation from stool could fill it.

## How to test it

From the large environmental viral-sequence collection, pull host assignments and lifestyle calls for these three hosts and compare them to hosts with good phage coverage, normalising by genome counts. Screen the anaerobe genomes and the metagenome-assembled genomes in the MAG catalog for prophage content as an independent measure. Then attempt phage enrichment from stool of Crohn's patients on each host and record plaque-forming or lytic-curve results.

## What would support or refute it

Support: host-assigned viruses are overwhelmingly temperate and enrichments yield no lytic phage. Refutation: lytic phages for these hosts are recovered from stool or already exist at normal rates.

## Data

Approach: analysis then experiment. Readiness: unknown. The MAG catalog lists some of these species by name; the catalog showed viral host-assignment tables but not whether they hold lifestyle calls, and MAG counts for these hosts were not shown.

## Builds on

- Finding: [[findings/ibd_phage_targeting--d7f80dce|E1 Crohn's candidate species replicate in held-out HMP2 cohort]] (Insufficient literature evidence)

## Closest published work

- [PMID 41726920](https://pubmed.ncbi.nlm.nih.gov/41726920/) Enhanced multi-omic viral profiling from microbial community sequencing with BAQLaVa.
- [PMID 28130329](https://pubmed.ncbi.nlm.nih.gov/28130329/) Bacteriophages Targeting Adherent Invasive Escherichia coli Strains as a Promising New Treatment for Crohn's Disease.

PMID 41726920 profiles viral changes in IBD cohort data and PMID 28130329 treats phage against E. coli; neither asks why lytic phages for these anaerobes are missing.
