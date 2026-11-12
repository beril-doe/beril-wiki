---
type: "Research direction"
description: "Within the few Crohn's patients who carry E. coli, do strains with iron-siderophore or genotoxin gene clusters differ from strains without them in how they track disease and bloom?"
hypothesis: "Disease-linked E. coli are those carrying yersiniabactin, enterobactin or colibactin-type clusters. Carriers of strains lacking these clusters look like non-IBD E. coli, so species-level detection (8 of 23 patients) hides the real signal."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The E. coli genome browser can seed the cluster map, but patient-matched strain genotyping needs new isolates or stool assays."
databases: ["phagefoundry.escherichia_genome_browser"]
tables: ["phagefoundry.escherichia_genome_browser.browser_gene", "phagefoundry.escherichia_genome_browser.browser_genome"]
findings: ["ibd_phage_targeting--6d9fa20c", "ibd_phage_targeting--446eca8c"]
conflicts: []
papers: ["35359974", "28130329", "41606218"]
builds_on: ["findings/ibd_phage_targeting--6d9fa20c", "findings/ibd_phage_targeting--446eca8c"]
projects: ["ibd_phage_targeting"]
topics: ["translational-microbiome-and-phage-therapeutics"]
---
# Is Crohn's-linked E. coli a siderophore-and-genotoxin subset rather than the whole species?

Within the few Crohn's patients who carry E. coli, do strains with iron-siderophore or genotoxin gene clusters differ from strains without them in how they track disease and bloom?

## Hypothesis

Disease-linked E. coli are those carrying yersiniabactin, enterobactin or colibactin-type clusters. Carriers of strains lacking these clusters look like non-IBD E. coli, so species-level detection (8 of 23 patients) hides the real signal.

## Why it matters

Species-level targeting would hit harmless E. coli and miss the harmful subset. A strain-cluster rule would give a narrower, testable phage target and help explain why E. coli is rarer in this cohort than the adherent-invasive E. coli literature implies.

## How to test it

Build a cluster-presence map across E. coli genomes with known source and compare Crohn's-linked genomes with others. Then genotype the E. coli isolates or stool DNA of the 8 carrier patients for the cluster genes and test whether cluster-positive carriers have higher E. coli load and stronger disease markers than cluster-negative carriers. Also ask which other taxa carry the same clusters in patients without detectable E. coli.

## What would support or refute it

Support: cluster-positive strains cluster in disease samples and cluster-negative strains do not. Refutation: cluster content is the same in disease and healthy E. coli, or non-carriers show no other siderophore-bearing taxon, so the signal is species abundance.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The E. coli genome browser can seed the cluster map, but patient-matched strain genotyping needs new isolates or stool assays.

## Builds on

- Finding: [[findings/ibd_phage_targeting--6d9fa20c|E. coli is rarer in this Crohn's cohort than AIEC literature implies]] (Extends retrieved work)
- Finding: [[findings/ibd_phage_targeting--446eca8c|Tier-A core gene clusters are enriched for iron-siderophore and genotoxin themes]] (Insufficient literature evidence)

## Closest published work

- [PMID 35359974](https://pubmed.ncbi.nlm.nih.gov/35359974/) Prevalence, Abundance, and Virulence of Adherent-Invasive Escherichia coli in Ulcerative Colitis, Colorectal Cancer, and Coeliac Disease.
- [PMID 28130329](https://pubmed.ncbi.nlm.nih.gov/28130329/) Bacteriophages Targeting Adherent Invasive Escherichia coli Strains as a Promising New Treatment for Crohn's Disease.
- [PMID 41606218](https://pubmed.ncbi.nlm.nih.gov/41606218/) From niche to niche: investigating microbial communities and their specialised metabolite gene clusters in human microbiomes.

PMID 35359974 reports adherent-invasive E. coli prevalence by disease group and PMID 28130329 proposes phages against these strains; neither relates strain-level cluster content to carriage in a small Crohn's cohort.
