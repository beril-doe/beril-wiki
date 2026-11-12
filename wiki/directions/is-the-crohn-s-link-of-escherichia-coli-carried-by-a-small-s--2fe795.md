---
type: "Research direction"
description: "E. coli was detectable in only 8 of 23 Crohn's patients in the UC Davis cohort. Is its disease association confined to strains carrying iron-siderophore and genotoxin clusters rather than to the species as a whole?"
hypothesis: "Among E. coli carriers, the disease-linked signal comes from strains with yersiniabactin, enterobactin or colibactin-type clusters. Strains without them show no disease association."
approach: "analysis then experiment"
readiness: "unknown"
readiness_basis: "Cohort sample metadata is in the catalog; the catalog did not show whether the genome browser carries cluster calls or whether the cohort data resolve strains."
databases: ["arkinlab.cmd_reference", "phagefoundry.escherichia_genome_browser"]
tables: ["arkinlab.cmd_reference.sample_metadata"]
findings: ["ibd_phage_targeting--6d9fa20c", "ibd_phage_targeting--446eca8c"]
conflicts: []
papers: ["35359974", "28130329"]
builds_on: ["findings/ibd_phage_targeting--6d9fa20c", "findings/ibd_phage_targeting--446eca8c"]
projects: ["ibd_phage_targeting"]
topics: ["translational-microbiome-and-phage-therapeutics"]
---
# Is the Crohn's link of Escherichia coli carried by a small siderophore-and-genotoxin strain subset?

E. coli was detectable in only 8 of 23 Crohn's patients in the UC Davis cohort. Is its disease association confined to strains carrying iron-siderophore and genotoxin clusters rather than to the species as a whole?

## Hypothesis

Among E. coli carriers, the disease-linked signal comes from strains with yersiniabactin, enterobactin or colibactin-type clusters. Strains without them show no disease association.

## Why it matters

It would decide whether phage cocktails should target E. coli by strain virulence content rather than by species. A species-wide cocktail would then also target strains that lack the disease-linked clusters.

## How to test it

Gather E. coli genomes from the Escherichia genome browser and public assemblies and call siderophore and genotoxin clusters in each. Build a marker panel that separates strains with and without them. Apply the panel to E. coli abundance data across IBD cohorts, using the pooled cohort sample metadata for disease labels. Compare marker-positive and marker-negative carriers between Crohn's and non-IBD subjects. Then confirm in stool from the UC Davis patients by strain-resolved metagenomics.

## What would support or refute it

Support: only marker-positive carriers differ between Crohn's and non-IBD. Refutation: marker-negative carriers show the same difference, or marker-positive carriers do not differ from controls.

## Data

Approach: analysis then experiment. Readiness: unknown. Cohort sample metadata is in the catalog; the catalog did not show whether the genome browser carries cluster calls or whether the cohort data resolve strains.

## Builds on

- Finding: [[findings/ibd_phage_targeting--6d9fa20c|E. coli is rarer in this Crohn's cohort than AIEC literature implies]] (Extends retrieved work)
- Finding: [[findings/ibd_phage_targeting--446eca8c|Tier-A core gene clusters are enriched for iron-siderophore and genotoxin themes]] (Insufficient literature evidence)

## Closest published work

- [PMID 35359974](https://pubmed.ncbi.nlm.nih.gov/35359974/) Prevalence, Abundance, and Virulence of Adherent-Invasive Escherichia coli in Ulcerative Colitis, Colorectal Cancer, and Coeliac Disease.
- [PMID 28130329](https://pubmed.ncbi.nlm.nih.gov/28130329/) Bacteriophages Targeting Adherent Invasive Escherichia coli Strains as a Promising New Treatment for Crohn's Disease.

PMID 35359974 reports how common adherent-invasive E. coli is in disease cohorts, and PMID 28130329 proposes phage against it; neither asks whether virulence-cluster content, not carriage, explains the signal within carriers.
